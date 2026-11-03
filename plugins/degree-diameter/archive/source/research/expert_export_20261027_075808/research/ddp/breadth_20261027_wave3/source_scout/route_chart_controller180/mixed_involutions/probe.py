from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;started=time.process_time()
assert not (P/'RESULT.json').exists(), 'Do not restart this completed finite scope.'
data=json.loads((P.parent/'group.json').read_text());perms=[tuple(p) for p in data['permutations']];idx={p:i for i,p in enumerate(perms)}
small=[[idx[tuple(p[q[i]] for i in range(5))] for q in perms] for p in perms]
table=[[60*((g//60+h//60)%3)+small[g%60][h%60] for h in range(180)] for g in range(180)]
inv=data['inverse'];assert all(table[g][inv[g]]==table[inv[g]][g]==0 for g in range(180))
pair_pool=[g for g in range(1,180) if g<inv[g]]
involutions=[g for g in range(1,180) if inv[g]==g]
assert len(pair_pool)==82 and len(involutions)==15
step_inverse=[1,0,2,3]
words=[w for w in product(range(4),repeat=5) if all(w[i+1]!=step_inverse[w[i]] for i in range(4))];assert len(words)==324
tested=0;hist=Counter();best=None;hit=None;cursor=None
for pair_index,a in enumerate(pair_pool):
 for inv_pair_index,(c,d) in enumerate(combinations(involutions,2)):
  S=[a,inv[a],c,d];seen={}
  for w in words:
   g=0
   for j in w:g=table[g][S[j]]
   seen.setdefault(g,w)
  count=len(seen);hist[count]+=1;tested+=1;cursor=dict(pair_index=pair_index,involution_pair_index=inv_pair_index)
  if best is None or count>best['exact_NB5_reached']:best=dict(S=S,exact_NB5_reached=count,missing=[g for g in range(180) if g not in seen],candidate_index=tested,cursor=cursor)
  if count==180:hit=dict(S=S,group_generator_inverse_map=step_inverse,identity_route_words={str(g):list(seen[g]) for g in range(180)});break
  if time.process_time()-started>4.8:break
 if hit or time.process_time()-started>4.8:break
result=dict(status='FOUND_EXACT_NB5_CONTROLLER' if hit else ('COMPLETE_8610_MIXED_COMPOSITION_NO_HIT' if tested==8610 else 'CPU_STOP_SAVED_CURSOR'),group='A5 direct_product C3',controller_vertices=180,controller_degree=4,scope='Exactly one distinct noninvolution inverse-pair and two distinct nonidentity involutions',scope_count=8610,candidates_checked=tested,actual_step_inverse=step_inverse,best=best,histogram=dict(sorted(hist.items())),CPU_seconds=time.process_time()-started,cursor=cursor,hit=hit,full_lift_generated=False,new_lower_bound=False)
if hit:
 S=hit['S'];edges=sorted({tuple(sorted((g,table[g][s]))) for g in range(180) for s in S});assert len(edges)==360 and all(u!=v for u,v in edges)
 (P/'controller.edges').write_text('180 360\n'+''.join(f'{u} {v}\n' for u,v in edges))
 ext=[[table[g][S[2]],table[g][S[3]]] for g in range(180)]
 bp=[-1]*180;bm=[-1]*180;done=set();cycles=[]
 for start in range(180):
  if start in done:continue
  previous=-1;u=start;cycle=[]
  while u not in done:
   done.add(u);cycle.append(u);v=ext[u][0] if previous<0 else next(x for x in ext[u] if x!=previous)
   bp[u]=v;bm[v]=u;previous,u=u,v
  assert u==start and len(cycle)>=4 and len(cycle)%2==0;cycles.append(cycle)
 labels=[[table[g][S[0]],table[g][S[1]],bp[g],bm[g]] for g in range(180)]
 assert all(len(set(row))==4 for row in labels)
 assert all(labels[labels[g][j]][j^1]==g for g in range(180) for j in range(4))
 chart_words=[w for w in product(range(4),repeat=5) if all(w[i+1]!=(w[i]^1) for i in range(4))]
 routes=[]
 for root in range(180):
  found={}
  for w in chart_words:
   v=root
   for j in w:v=labels[v][j]
   found.setdefault(v,list(w))
  assert len(found)==180
  routes.append([found[v] for v in range(180)])
 (P/'controller.labels.json').write_text(json.dumps(dict(symbols=['a','a^-1','b','b^-1'],inverse_symbols=[1,0,3,2],neighbors_by_label=labels,oriented_involution_union_cycles=cycles))+'\n')
 (P/'controller.route_words.json').write_text(json.dumps(routes)+'\n')
 (P/'group_definition.json').write_text(json.dumps(dict(group='A5 direct_product C3',vertex_encoding='60*t+permutation_index',permutations=perms,S=S,group_generator_inverse=step_inverse,product_convention='(p,t)*(q,u)=(p composed with q,t+u mod3)',multiplication_table=table))+'\n')
 result['labelled_exact_NB5_pairs_verified']=180*180
 result['CPU_seconds_including_label_and_route_export']=time.process_time()-started
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['histogram','best','hit']}));print('best',best)
