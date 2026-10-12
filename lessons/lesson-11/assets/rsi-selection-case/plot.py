"""Optional figure reproduction; requires an existing matplotlib installation."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
summary=json.loads((HERE/'recorded/summary.json').read_text())
fig,axes=plt.subplots(1,2,figsize=(11,4.2),layout='constrained')
colors={'equal':'#9E1B32','heterogeneous':'#285E8E'}
for scenario in ('equal','heterogeneous'):
 groups=[g for g in summary['groups'] if g['scenario']==scenario and g['method']=='history']
 for ax,key in zip(axes,('history_optimism','final_score')):
  x=[g['candidate_count'] for g in groups]; y=[g['metrics'][key]['mean'] for g in groups]
  errors=[[y[i]-g['metrics'][key]['ci95'][0] for i,g in enumerate(groups)],[g['metrics'][key]['ci95'][1]-y[i] for i,g in enumerate(groups)]]
  ax.errorbar(x,y,yerr=errors,color=colors[scenario],marker='o',capsize=4,label=scenario)
  ax.set_xscale('log',base=4);ax.set_xticks([1,4,16,64],labels=['1','4','16','64']);ax.set_xlabel('Number of candidates K');ax.grid(alpha=.18)
axes[0].set_ylabel('Selected historical score minus true probability')
axes[0].set_title('Historical selection optimism')
axes[1].set_ylabel('Independent final success rate')
axes[1].axhline(.65,color='#666666',linestyle='--',linewidth=1,label='Equal true probability 0.65')
axes[1].set_title('Final evaluation after selection is frozen')
axes[1].legend(frameon=False,fontsize=9)
fig.suptitle('Actual CPU run on synthetic Bernoulli environments | 500 repeats, 95% bootstrap intervals',fontsize=11)
out=HERE/'figures';out.mkdir(exist_ok=True)
fig.savefig(out/'selection-diagnosis.png',dpi=180)
plt.close(fig)
