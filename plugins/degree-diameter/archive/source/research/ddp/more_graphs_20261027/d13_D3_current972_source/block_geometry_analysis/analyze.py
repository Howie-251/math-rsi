from pathlib import Path
from collections import defaultdict,Counter
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
source=P.parent/'source972.edges'
it=iter(map(int,source.read_text().split()));n=next(it);m=next(it);adj=[set() for _ in range(n)]
for _ in range(m):
 u,v=next(it),next(it);adj[u].add(v);adj[v].add(u)
def v(x):return (x%3,x//3%3,x//9)
def num(x):return x[0]+3*x[1]+9*x[2]
def add(x,y):return tuple((a+b)%3 for a,b in zip(x,y))
def sub(x,y):return tuple((a-b)%3 for a,b in zip(x,y))
def mul(a,x):return tuple(a*b%3 for b in x)
def canon(d):
 if not any(d):return None
 a=next(a for a in d if a)
 return tuple(a*b%3 for b in d)
def line(points):
 if len(set(points))!=3:return None
 x,y,z=map(v,sorted(points))
 if add(add(x,y),z)!=(0,0,0):return None
 return canon(sub(y,x))
def plane(f,d):return tuple(sorted({num(add(mul(a,f),mul(b,d))) for a in range(3) for b in range(3)}))
blocks=[];neighbor_sets=[]
for b in range(36):
 lo=27*b;vertices=range(lo,lo+27)
 inside={u:sorted(x-lo for x in adj[u] if x//27==b) for u in vertices}
 fixed=[u-lo for u in vertices if not inside[u]]
 assert len(fixed)==3
 tau=[inside[u][0] if inside[u] else u-lo for u in vertices]
 offset=v(tau[0]);cols=[sub(v(tau[e]),offset) for e in [1,3,9]]
 fit=all(add(offset,add(mul(v(x)[0],cols[0]),add(mul(v(x)[1],cols[1]),mul(v(x)[2],cols[2]))))==v(tau[x]) for x in range(27))
 sets={tuple(sorted({x//27 for x in adj[u] if x//27!=b})) for u in vertices}
 neighbor_sets.append(next(iter(sets)) if len(sets)==1 else None)
 blocks.append({'block':b,'free_local':fixed,'free_line_direction':line(fixed),'internal_affine_fit':fit,
 'internal_affine_matrix_columns':cols if fit else None,'internal_affine_offset':offset if fit else None,
 'equitable_external_target_blocks':neighbor_sets[-1],'distinct_external_target_block_sets':len(sets)})
relations=[];directions=defaultdict(list)
if all(x is not None and len(x)==4 for x in neighbor_sets):
 for b in range(36):
  for c in neighbor_sets[b]:
   if b>=c:continue
   grouped=defaultdict(list)
   for x in range(27):
    right=tuple(sorted(u-27*c for u in adj[27*b+x] if u//27==c))
    grouped[right].append(x)
   ok=len(grouped)==9 and all(len(rs)==len(ls)==3 for rs,ls in grouped.items()) and len(set(y for rs in grouped for y in rs))==27
   ld=[line(ls) for ls in grouped.values()];rd=[line(rs) for rs in grouped]
   affine=ok and all(x is not None for x in ld+rd) and len(set(ld))==len(set(rd))==1
   rec={'left':b,'right':c,'K3_3_components9':ok,'parallel_affine_lines':affine,
    'left_direction':ld[0] if affine else None,'right_direction':rd[0] if affine else None}
   if affine:
    directions[b].append((c,ld[0]));directions[c].append((b,rd[0]))
   freeb={27*b+x for x in blocks[b]['free_local']};freec={27*c+x for x in blocks[c]['free_local']}
   rec['free_to_free_edges']=sum(vv in freec for uu in freeb for vv in adj[uu])
   relations.append(rec)
 summaries=[]
 for b in range(36):
  f=blocks[b]['free_line_direction'];ds=[d for _,d in directions[b]]
  if f is None or len(ds)!=4:continue
  nonzero={plane(f,d) for d in ds if canon(d)!=canon(f)}
  k=len(nonzero)
  own_union=3+6*k
  entries=[{'to':c,'kernel_direction':d,'free_line_parallel':canon(d)==canon(f)} for c,d in directions[b]]
  summaries.append({'block':b,'fixed_line_direction':f,'edge_directions':entries,
   'distinct_edge_directions':len(set(ds)),'distinct_nonzero_directions_mod_fixed_line':k,
   'each_single_free_pin_own_block_R2':1+2*len(set(ds)),
   'all_three_free_own_block_R2_union':own_union,
   'ownblock_formula_scope':'Exact own-block R2 from freepoints because first internal step absent and two-external-step return is through the same baseedge.'})
else:summaries=[]
result={'status':'BLOCK_STRUCTURE_ANALYSIS_COMPLETE','n':n,'m':m,
 'prediction_affine_involutions':all(x['internal_affine_fit'] for x in blocks),
 'affine_internal_count':sum(x['internal_affine_fit'] for x in blocks),
 'free_affine_line_count':sum(x['free_line_direction'] is not None for x in blocks),
 'equitable_four_neighbor_blocks':all(x is not None and len(x)==4 for x in neighbor_sets),
 'undirected_quotient_edge_count':len(relations),'K3_3_relation_count':sum(x['K3_3_components9'] for x in relations),
 'affine_parallel_relation_count':sum(x['parallel_affine_lines'] for x in relations),
 'free_to_free_edge_count':sum(x['free_to_free_edges'] for x in relations),
 'block_local_own_R2_union_histogram':dict(Counter(x['all_three_free_own_block_R2_union'] for x in summaries)),
 'projected_direction_count_histogram':dict(Counter(x['distinct_nonzero_directions_mod_fixed_line'] for x in summaries)),
 'free_line_parallel_oriented_edge_count':sum(x['free_line_parallel'] for r in summaries for x in r['edge_directions']),
 'blocks':blocks,'relations':relations,'ownblock_summaries':summaries,
 'ordinary_BFS':0,'R2_balls_or_full_coverage_matrix_recomputed':0,'solver_runs':0,'candidate_graphs':0,
 'CPU_seconds':time.process_time()-start}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
for k in ['status','affine_internal_count','free_affine_line_count','equitable_four_neighbor_blocks','undirected_quotient_edge_count','K3_3_relation_count','affine_parallel_relation_count','free_to_free_edge_count','block_local_own_R2_union_histogram','projected_direction_count_histogram','free_line_parallel_oriented_edge_count','CPU_seconds']:print(k,result[k])
