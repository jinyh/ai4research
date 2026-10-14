"""Reproduce audit observations against the unmodified source (synthetic CPU fixtures).

Run from repository root:
PYTHONPATH=src .venv-check/bin/python notes/source_audit_checks.py
Assertions describe current behavior, not desired regression-test expectations.
"""

import asyncio
import copy
import json
import tempfile
from pathlib import Path
from types import SimpleNamespace

from simple_scibuddy.coevolve.context import validate_assessment
from simple_scibuddy.coevolve.evidence import public_evidence
from simple_scibuddy.coevolve.program import propose
from simple_scibuddy.harness.broker import run_episode
from simple_scibuddy.harness.messages import classify_messages
from simple_scibuddy.inference.client import RecordingPolicy


class CharacterTokenizer:
    def encode(self, text, **kwargs):
        return list(map(ord, text))

    def decode(self, tokens, **kwargs):
        return ''.join(map(chr, tokens))

    def apply_chat_template(self, messages, **kwargs):
        return self.encode(''.join(m['content'] for m in messages))


async def budget_case(root, source):
    class SyntheticContainer:
        def __init__(self, image, folder, kind, **kwargs):
            self.sent = []
            self.events = iter(
                [{'op': 'execute', 'code': f'print({i})'} for i in range(5)]
                + [{'op': 'generate', 'messages': [
                    {'role': 'user', 'source': 'task', 'content': 'Q'},
                    *[{'role': 'user', 'source': source, 'content': str(i) * 1900}
                      for i in range(5)],
                ]}, {'op': 'submit', 'text': '<answer>A</answer>'}]
            )
            self.tool_index = 0

        async def start(self, **kwargs):
            pass

        async def send(self, value):
            self.sent.append(value)

        async def receive(self):
            return next(self.events)

        async def execute(self, code, timeout):
            value = {'stdout': str(self.tool_index) * 1900, 'error': None}
            self.tool_index += 1
            return value

        async def collect(self):
            pass

        async def close(self):
            pass

    async def generate(payload, **kwargs):
        answer = list(map(ord, '<answer>A</answer>'))
        return {'response_ids': [answer], 'response_logprobs': [[-0.5] * len(answer)],
                'stop_reasons': ['stop']}

    task = SimpleNamespace(
        environment={'image': 'synthetic'}, lake_path=root, assets=root / 'assets',
        public={'id': 'fixture', 'family': 'science', 'source_group': 'fixture',
                'split': 'train', 'prompt': 'Q'},
        verify=lambda text: {'score': 1.0, 'answer_format_valid': True},
    )
    policy = RecordingPolicy(SimpleNamespace(generate=generate), CharacterTokenizer(), {},
                             'synthetic', source, context=24576, max_tokens=4096)
    episode = await run_episode(task, root / 'harness.py', policy, root / source, 'SYSTEM',
                                container_factory=SyntheticContainer,
                                tool_response_tokens=2048, tool_history_tokens=8192)
    assert episode['reward'] == 1 and 'error' not in episode
    call = episode['calls'][0]
    return {'visible_evidence_tokens': sum(len(m['content']) for m in call['messages'][1:]),
            'clipping_events': len(call['tool_history_clipping']),
            'input_tokens': len(call['prompt_ids'])}


def main():
    with tempfile.TemporaryDirectory(prefix='sciencebuddy-audit-') as temporary:
        root = Path(temporary)
        (root / 'assets').mkdir()
        (root / 'harness.py').write_text('def run(task, api): pass\n')
        honest = asyncio.run(budget_case(root, 'tool'))
        relabeled = asyncio.run(budget_case(root, 'harness'))
        assert honest['visible_evidence_tokens'] <= 8192
        assert relabeled['visible_evidence_tokens'] == 9500
        assert relabeled['clipping_events'] == 0
        assert relabeled['input_tokens'] + 4096 <= 24576

        fabricated, _ = classify_messages(
            [{'role': 'user', 'source': 'tool', 'content': 'FABRICATED_RESULT'}], 'Q', [], 1)
        assert fabricated[0]['content'] == 'FABRICATED_RESULT'

        reply = 'Please reconsider that answer. Please check your work and try again.'
        fields = {'question': 'Q', 'outputs/0/text': '<answer>A</answer>',
                  'answer': '<answer>A</answer>', 'reply': reply}
        assessment = {
            'feedback_type': 'correction', 'reward': -1,
            'evidence': 'A reply that was never provided',
            'user_request': {'interpretation': 'Invented specific feedback',
                             'quote': 'NONEXISTENT_USER_QUOTE', 'specific_issue_explicit': True},
            'observations': [{'field': 'outputs/0/text', 'quote': 'NONEXISTENT_EXECUTION_QUOTE',
                              'interpretation': 'Invented observation'}],
            'related_fields': ['outputs/0/text'], 'uncertainty': 'Synthetic audit fixture',
        }
        assert validate_assessment(assessment, fields, reply, 'correction') == (True, None)
        episode = {
            'task_id': 'a', 'public_task': {'prompt': 'Q'},
            'calls': [{'text': '<answer>A</answer>', 'completion_ids': [1]}],
            'tool_calls': [], 'submissions': [{'text': '<answer>A</answer>', 'call_index': 0}],
            'user_feedback': [{'reply': reply, 'valid': True, 'feedback_type': 'correction',
                               'assessment': assessment}],
            'stop_reason': 'first_answer_evaluation',
        }
        evidence = public_evidence(episode)
        assert evidence['prm_annotations'][0]['assessment']['observations'][0]['quote'] == (
            'NONEXISTENT_EXECUTION_QUOTE')

        episode['user_feedback'][0].update(valid=False, assessment={})
        record = public_evidence(episode)
        other = copy.deepcopy(record)
        other['task_id'] = 'b'
        assert record['trace'] and not record['feedback'] and not record['diagnostics']

        def should_not_call(*args, **kwargs):
            raise AssertionError('Improver should not be called when evidence catalog is empty')

        result = propose(SimpleNamespace(generate_command=should_not_call), root / 'harness.py',
                         [record, other], [], root / 'candidate.py')
        assert result['status'] == 'skipped'
        print(json.dumps({
            'tool_source': honest,
            'relabeled_harness_source': relabeled,
            'fabricated_tool_text_accepted_after_one_execute': True,
            'nonexistent_prm_quotes_retained_in_public_evidence': True,
            'invalid_prm_with_two_clean_wrong_answers': result,
            'fixtures': 'Character tokenizer, fake containers and model; real broker and validators',
        }, indent=2))


if __name__ == '__main__':
    main()
