"""Exact source-key partition and each member's own selected blue colouring."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
HERE=Path(__file__).resolve().parent

def read(path):return [json.loads(x) for x in path.open()]
def key(r):return (tuple(r['inventory']),r['nine'],tuple(map(tuple,r['higher'])),tuple(r['J']))
def verify_colour(masks,blue,expected):
 assert len(masks)==35
 blue=sum(1<<v for v in blue);pos=Counter();neg=Counter()
 for m in masks:
  if m&blue and m&~blue:continue
  (pos if not m&~blue else neg)[5-m.bit_count()]+=1
 lower=max(max(0,18-sum(5-m.bit_count() for m in masks if m>>v&1 and m.bit_count()>=2)) for v in range(6) if blue>>v&1)
 sig=(pos[4],pos[3],pos[2],pos[1],neg[1],neg[2],neg[3],neg[4],lower)
 assert sig==tuple(expected)
 return sig
source=read(HERE.parent/'CENSUS_NONGATED.jsonl');base={key(r) for r in source};assert len(base)==8569
nine=read(HERE.parent/'nine_gate_selection_20261020'/'NINE_CANDIDATE_SOURCES.jsonl')
eight=read(HERE/'NEW_EIGHT_363.jsonl');mixed=read(HERE/'MIXED21_SOURCES47.jsonl');tail=read(HERE/'AFTER_MIXED21_TAIL139.jsonl')
seen=set()
for name,rs in [('nine',nine),('eight',eight),('mixed21',mixed),('tail',tail)]:
 ks={key(r) for r in rs};assert len(ks)==len(rs) and not seen&ks and ks<=base;seen|=ks
 if name=='tail':continue
 for r in rs:
  if name=='nine':sig=verify_colour([q[0] for q in r['indexed_source_roles']],r['blue'],r['signature'])
  else:sig=verify_colour(r['trace_masks'],r['selected_blue'],r['selected_signature'])
  p4,p3,p2,p1,n1,n2,t,b,_=sig
  if name=='nine':assert p4==9 and p3==p2==p1==n1==n2==0 and t<=3 and t+b<=20
  elif name=='eight':assert p4==8 and p3==p2==p1==n1==n2==0 and t<=1 and b<=20
  else:assert p4+p3==8 and p3<=2 and p2==p1==n1==n2==t==0 and b<=21
assert seen==base and (len(nine),len(eight),len(mixed),len(tail))==(8020,363,47,139)
for r in tail:
 assert len(r['choices'])==35 and len({tuple(c['blue']) for c in r['choices']})==35
 for c in r['choices']:verify_colour(r['trace_masks'],c['blue'],c['signature'])
cells=Counter((tuple(r['inventory']),r['nine']) for r in tail)
out={'status':'PASS','old_nongated_universe':8569,'disjoint_new_covered':{'nine':8020,'eight':363,'mixed21':47},'remaining':139,
 'original_necessary_domain':123621,'old_covered':115052,'total_now_covered':123482,
 'union_exactly_original8569':True,'own_selected_blue_replayed_for_all_new_passes':True,'all_remaining_35_blue_menus_replayed':True,
 'remaining_by_inventory_nine':[{'inventory':i,'nine':n,'count':v} for (i,n),v in sorted(cells.items())],
 'whole_requested_inventory_cleared':False}
(HERE/'CHAIN_SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
