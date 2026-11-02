"""Exact short-word counts in the fixed phase quotient; no lifted graph."""
from collections import Counter, defaultdict
from pathlib import Path
import json
import time

started=time.process_time()
out=Path(__file__).resolve().parent
recipe=json.loads((out.parent/'construction.author.json').read_text())
assert recipe['construction']['base_vertices']==3
# Named darts, each immediately followed by its precise inverse dart.
spec=[(0,1,0),(0,2,0),(1,2,6),(0,1,10),(0,1,14),(2,2,3)]
darts=[]
for i,(u,v,j) in enumerate(spec):
    darts.extend([{'id':2*i,'inverse':2*i+1,'from':u,'to':v,'phase':j%36},
                  {'id':2*i+1,'inverse':2*i,'from':v,'to':u,'phase':(-j)%36}])
outgoing=[[d for d in darts if d['from']==u] for u in range(3)]
assert all(len(row)==4 for row in outgoing)
slots=[]
layer_sizes=[]
for root in range(3):
    states={(root,0,-1):1}
    totals=Counter({(root,0):1})
    by_length=[Counter({(root,0):1})]
    for length in range(1,10):
        nxt=defaultdict(int)
        for (v,j,last),count in states.items():
            for d in outgoing[v]:
                if d['id']!=(last^1):
                    nxt[d['to'],(j+d['phase'])%36,d['id']]+=count
        states=nxt
        count=Counter()
        for (v,j,last),n in states.items():count[v,j]+=n
        assert sum(count.values())==4*3**(length-1)
        totals.update(count);by_length.append(count)
    assert sum(totals.values())==39365
    layer_sizes.append([sum(c.values()) for c in by_length])
    for target in range(3):
        for j in range(36):
            slots.append({'root_base':root,'target_base':target,'phase':j,
                          'word_count_le9':totals[target,j],
                          'word_counts_by_length':[c[target,j] for c in by_length]})
minimum=min(s['word_count_le9'] for s in slots)
thin=[s for s in slots if s['word_count_le9']==minimum]
r={'status':'COMPLETE_FIXED_PHASE_QUOTIENT_CAPACITY','prediction_disposition':'SUPPORTED' if minimum<109 else 'REFUTED',
   'phase_order':36,'base_vertices':3,'slots_count':324,
   'root_total_words_le9':39365,'length_counts_per_root':layer_sizes,
   'minimum_words_per_slot':minimum,'minimum_slots':thin,
   'slot_wordcount_histogram':dict(Counter(s['word_count_le9'] for s in slots)),
   'module81_excluded_by_phase_count':minimum<81,
   'module109_excluded_by_phase_count':minimum<109,
   'all_translation_module_orders_above_minimum_excluded':minimum,
   'source73_count_consistency':minimum>=73,
   'word_scope':'Allreduced named-edge walks length0..9, notonlylength9; inverse loop darts correctly distinguished. Immediatebacktracksdeletewithoutchanging endpoint in an ordinaryvoltagelift.',
   'capacity_scope':'Forfixedphase/base dartgraph any valid translationmodule andaction, one word has oneendpoint. A slot with fewerthanN words cannotcoverN fiberpoints. Passingthis count doesnotgiveexistence.',
   'darts':darts,'CPU_seconds':time.process_time()-started,
   'graph_generation':False,'source_BFS':0,'parameter_grid':False,'pending':[]}
(out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(out/'SLOTS.json').write_text(json.dumps(slots,indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k not in ['darts','slot_wordcount_histogram']},indent=2))
