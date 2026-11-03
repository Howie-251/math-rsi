from pathlib import Path
from collections import Counter
import json
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
started=time.process_time()
source=ROOT/'research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.labels.json'
x=json.loads(source.read_text());adj=x['out'];inv=x['inverse'];assert x['n']==72 and inv==[3,2,1,0]
slots=[]
for root in range(72):
    counts=[[0]*5 for _ in range(72)];words={}
    def walks(u,word):
        counts[u][len(word)]+=1
        if len(word)==4:words.setdefault(u,tuple(word))
        else:
            for t,v in enumerate(adj[u]):walks(v,word+[t])
    walks(root,[])
    for v in range(72):
        if counts[v]==[0,0,0,0,1]:
            slots.append(dict(source=root,target=v,word=words[v]))
required=sorted({tuple(s['word']) for s in slots})
assert len(slots)==468 and len(required)==26
assert (0,0,0,0) in required and (3,3,3,3) in required
assert (1,1,1,1) not in required and (2,2,2,2) not in required
assert all(tuple(inv[t] for t in reversed(w)) in required for w in required)
assert all(w[i+1]!=inv[w[i]] for w in required for i in range(3))
old=json.loads((ROOT/'research/ddp/breadth_20261027_wave10/binary1152_edge_local/unique4_controller_slots.json').read_text())
assert required==list(map(tuple,old['word_types']))
assert {(s['source'],s['target'],tuple(s['word'])) for s in slots}=={(s['source'],s['target'],tuple(s['word'])) for s in old['slots']}
data=dict(status='REQUIRED_WORDS_REDERIVED_MATCH',source=str(source.relative_to(ROOT)),
          inverse=inv,label_meanings=['a','b','b^-1','a^-1'],
          unique4_ordered_slots=468,required_word_types=26,required_words=required,
          word_slot_multiplicity=[sum(tuple(s['word'])==w for s in slots) for w in required],
          aaaadddd_required=True,bbbbcccc_required=False,bbbb_prefilter_allowed=False,
          slots=slots,ordinary_BFS_performed=False,CPU_seconds=time.process_time()-started)
(OUT/'required_words.json').write_text(json.dumps(data,indent=2)+'\n')
(OUT/'words.txt').write_text('26\n'+''.join(' '.join(map(str,w))+'\n' for w in required))
print(json.dumps({k:data[k] for k in ['status','unique4_ordered_slots','required_word_types','CPU_seconds']}))
