"""Numerical validation of GPT-2 attention-head intervention semantics."""
import unittest
import torch
from transformers import GPT2Config, GPT2LMHeadModel
from run import replace_slice, validate_policy

class HeadTests(unittest.TestCase):
    def test_policy(self):
        validate_policy({'layer':9,'position':'last','component':'attention_heads','heads':[0,1]})
        for heads in ([],[True],[12],[1,1]):
            with self.assertRaises(ValueError):validate_policy({'layer':9,'position':'last','component':'attention_heads','heads':heads})
    def test_only_selected_head_and_position_changed(self):
        hidden=torch.arange(48.).reshape(1,3,16);original=hidden.clone();replacement=-torch.ones(1,16)
        out=replace_slice(hidden,replacement,1,list(range(4,8)))
        self.assertTrue(torch.equal(hidden,original));self.assertTrue(torch.equal(out[:,0],hidden[:,0]));self.assertTrue(torch.equal(out[:,2],hidden[:,2]))
        self.assertTrue(torch.equal(out[:,1,:4],hidden[:,1,:4]));self.assertTrue(torch.equal(out[:,1,8:],hidden[:,1,8:]));self.assertTrue((out[:,1,4:8]==-1).all())
    def test_union_and_noop(self):
        h=torch.randn(1,3,16);r=torch.randn(1,16)
        single=replace_slice(replace_slice(h,r,2,list(range(4))),r,2,list(range(8,12)))
        joint=replace_slice(h,r,2,list(range(4))+list(range(8,12)))
        self.assertTrue(torch.equal(single,joint));self.assertTrue(torch.equal(replace_slice(h,h[:,2,:],2,list(range(4))),h))
    def test_real_gpt2_projection_hook(self):
        torch.manual_seed(1)
        model=GPT2LMHeadModel(GPT2Config(n_layer=1,n_head=2,n_embd=16,vocab_size=32,n_positions=8,attn_pdrop=0,resid_pdrop=0,embd_pdrop=0)).eval()
        tokens=torch.tensor([[1,2,3]]);cache={}
        def capture(module,inputs):cache['x']=inputs[0].detach().clone()
        handle=model.transformer.h[0].attn.c_proj.register_forward_pre_hook(capture)
        with torch.no_grad():baseline=model(tokens).logits
        handle.remove()
        replacement=cache['x'][:,2,:].clone()
        def noop(module,inputs):return (replace_slice(inputs[0],replacement,2,list(range(8))),)
        handle=model.transformer.h[0].attn.c_proj.register_forward_pre_hook(noop)
        with torch.no_grad():patched=model(tokens).logits
        handle.remove();self.assertTrue(torch.allclose(baseline,patched,atol=1e-6))
        # Explicit reference: change concatenated heads, then apply the same output projection.
        x=cache['x'];r=torch.zeros_like(replacement);modified=replace_slice(x,r,2,list(range(8)))
        expected=modified@model.transformer.h[0].attn.c_proj.weight+model.transformer.h[0].attn.c_proj.bias
        self.assertTrue(torch.allclose(model.transformer.h[0].attn.c_proj(modified),expected,atol=1e-6))
if __name__=='__main__':unittest.main()
