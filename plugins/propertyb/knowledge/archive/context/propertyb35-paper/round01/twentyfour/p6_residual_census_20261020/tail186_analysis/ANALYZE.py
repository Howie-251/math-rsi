"""Reconstruct every tail input independently; never reuse a menu blue witness."""
from pathlib import Path
from itertools import combinations
from collections import Counter,defaultdict
import json,time
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'nine_gate_selection_20261020'/'TAIL549.jsonl'
PAIRS=tuple(combinations(range(6),2));BLUES=tuple(combinations(range(6),2))+tuple(combinations(range(6),3))
START=time.process_time()
def key(r):return (tuple(r['inventory']),r['nine'],tuple(map(tuple,r['higher'])),tuple(r['J']))
def new8(s):return s[0]==8 and all(s[k]==0 for k in range(1,6)) and s[6]<=1 and s[7]<=20

def reconstruct(r):
 deg=[8+int(v==r['nine']) for v in range(6)]
 traces=[tuple(range(5))]+list(map(tuple,r['higher']))
 for p,n in zip(PAIRS,r['J']):traces.extend([p]*n)
 known=Counter(v for t in traces for v in t);u=[deg[v]-known[v] for v in range(6)]
 for v,n in enumerate(u):traces.extend([(v,)]*n)
 assert len(traces)==35 and min(u)>=0
 assert Counter(v for t in traces for v in t)==dict(enumerate(deg))
 h=[sum(v in t for t in r['higher']) for v in range(6)]
 sd=[sum(n for e,n in zip(PAIRS,r['J']) if v in e) for v in range(6)]
 lower=[max(0,18-sum(5-len(t) for t in traces if v in t and len(t)>=2)) for v in range(6)]
 choices=[]
 for blue in BLUES:
  B=set(blue);pos=Counter();neg=Counter();roles=[]
  ps=[];ns=[]
  for i,t in enumerate(traces):
   T=set(t)
   if T<=B:pos[5-len(t)]+=1;ps.append(i);roles.append((i,'P',5-len(t)))
   elif T.isdisjoint(B):neg[5-len(t)]+=1;ns.append(i);roles.append((i,'N',5-len(t)))
  assert 0 not in ps+ns
  sig=(pos[4],pos[3],pos[2],pos[1],neg[1],neg[2],neg[3],neg[4],max(lower[v] for v in blue))
  choices.append({'blue':blue,'blue_mask':sum(1<<v for v in blue),'signature':sig,
      'positive_source_indices':ps,'negative_source_indices':ns,
      'private_star_counts':[u[v] for v in blue],
      'private_star_union_lower_bounds':[lower[v] for v in blue],
      'blue_point_P_degree':[deg[v] for v in blue],
      'blue_point_J_degree':[sd[v] for v in blue],
      'blue_point_high_frequency':[h[v] for v in blue]})
 original={c['blue_mask']:tuple(c['signature']) for c in r['own_blue_choices']}
 assert original=={c['blue_mask']:c['signature'] for c in choices}
 return {'inventory':r['inventory'],'nine':r['nine'],'higher':r['higher'],'J':r['J'],
  'original_menu_id':r['menu_id'],'trace_masks':[sum(1<<v for v in t) for t in traces],
  'singleton_counts':u,'J_degrees':sd,'high_frequency':h,'private_star_union_lower_bounds':lower,
  'choices':choices}

seen=set();accepted=[];tail=[];cells=Counter();freq=Counter();cleanmenus=Counter()
for line in SOURCE.open():
 r=json.loads(line);k=key(r);assert k not in seen;seen.add(k)
 out=reconstruct(r);win=next((c for c in out['choices'] if new8(c['signature'])),None)
 if win:accepted.append(dict(out,selected_blue=win['blue'],selected_signature=win['signature']))
 else:
  tail.append(out);cells[(tuple(r['inventory']),r['nine'])]+=1
  ss={c['signature'][:8] for c in out['choices']}
  for s in ss:freq[s]+=1
  cleanmenus[tuple(sorted(s for s in ss if all(s[k]==0 for k in (2,3,4,5))))]+=1
assert len(seen)==549 and len(accepted)==363 and len(tail)==186
for name,data in [('NEW_EIGHT_363.jsonl',accepted),('TAIL186.jsonl',tail)]:
 with (HERE/name).open('w') as f:
  for r in data:f.write(json.dumps(r,separators=(',',':'))+'\n')
# All following interfaces are diagnostic targets, never newly accepted gates.
preds={
 '10P4_Tle2_Ble18':lambda s:s[:6]==(10,0,0,0,0,0) and s[6]<=2 and s[7]<=18,
 '10P4_Tle4_Ntotalle20':lambda s:s[:6]==(10,0,0,0,0,0) and s[6]<=4 and s[6]+s[7]<=20,
 '8mixed_2small_Tle2_Ntotalle21':lambda s:sum(s[:4])==8 and s[1]<=2 and all(s[k]==0 for k in (2,3,4,5)) and s[6]<=2 and s[6]+s[7]<=21,
 '8P4_Tle2_Ble19':lambda s:s[:6]==(8,0,0,0,0,0) and s[6]<=2 and s[7]<=19,
 '8mixed_2small_T0_Ble21':lambda s:sum(s[:4])==8 and s[1]<=2 and all(s[k]==0 for k in (2,3,4,5)) and s[6]==0 and s[7]<=21,
}
cov={k:set() for k in preds};witness={k:[] for k in preds};best=Counter()
for i,r in enumerate(tail):
 clean=[c for c in r['choices'] if all(c['signature'][k]==0 for k in (2,3,4,5))]
 assert clean
 best[min((c['signature'][:8] for c in clean),key=lambda s:(sum(s[:4]),s[1],s[6],s[7]))]+=1
 for name,pred in preds.items():
  cc=next((c for c in r['choices'] if pred(c['signature'][:8])),None)
  if cc:cov[name].add(i);witness[name].append({'tail_index':i,'blue':cc['blue'],'signature':cc['signature'],
    'private_star_counts':cc['private_star_counts'],'private_star_union_lower_bounds':cc['private_star_union_lower_bounds'],
    'blue_point_P_degree':cc['blue_point_P_degree'],'blue_point_J_degree':cc['blue_point_J_degree'],
    'blue_point_high_frequency':cc['blue_point_high_frequency']})
out={'status':'ALL549_SOURCE_RECONSTRUCTION_PASS','inputs':549,'indexed_colourings':549*35,'new_eight_count_filter':363,'remaining':186,
 'new_eight_status':'PROVED exact8P4,N3<=1,N4<=20,L18,D7: proofs/propertyb35/EIGHT_POSITIVE_ONE_TRIPLE_TWENTY_REPAIR.md; root paper acceptance, cross-model scope pending.',
 'cells':[{'inventory':k[0],'nine':k[1],'count':v} for k,v in sorted(cells.items())],
 'tail_clean_count_menus':len(cleanmenus),
 'diagnostic_candidate_coverage_not_proved':{k:len(v) for k,v in cov.items()},
 'diagnostic_pairwise_union_not_proved':{' + '.join(ks):len(cov[ks[0]]|cov[ks[1]]) for ks in combinations(preds,2)},
 'best_clean_signatures':[{'counts':s,'inputs':n} for s,n in best.most_common()],
 'top_signatures':[{'counts':s,'inputs':n} for s,n in freq.most_common(25)],
 'candidate_witnesses':witness,'cpu_seconds':time.process_time()-START}
(HERE/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k not in ('candidate_witnesses','top_signatures')})
