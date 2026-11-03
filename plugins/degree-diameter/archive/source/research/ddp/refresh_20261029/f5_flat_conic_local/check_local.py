#!/usr/bin/env python3
"""One fixed proper-color translation rule; cached return words only."""
import itertools,json,time
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
start=time.process_time()
P=json.loads((HERE.parent/'f5_full_d20_D3/PARAMETERS.json').read_text());C=P['controller']
structure=json.loads((HERE.parents[1]/'breadth_20261027_wave4/mizuno_d3_source/controller_structure.json').read_text())
V=[(1,t,t*t%5) for t in range(5)]+[(0,0,1)]
def det(a,b,c):return (a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]))%5
conic_checks=[dict(colors=list(ijk),determinant=det(*(V[i] for i in ijk))) for ijk in itertools.combinations(range(6),3)]
assert all(x['determinant'] for x in conic_checks)
colors={};kind={}
for tri in structure['triangles']:
 a,b,c=sorted(tri)
 for edge,col in zip([(a,b),(a,c),(b,c)],[0,1,2]):colors[edge]=col;kind[edge]='triangle'
cycles=[]
for cyc in structure['external_2factor_cycles']:
 i=cyc.index(min(cyc));forward=cyc[i:]+cyc[:i];backward=[forward[0]]+forward[:0:-1];s=min(forward,backward);cycles.append(s)
 for j,col in enumerate([3,4,3,4,5]):
  edge=tuple(sorted((s[j],s[(j+1)%5])));assert edge not in colors;colors[edge]=col;kind[edge]='external'
assert len(colors)==60 and set(colors)=={tuple(sorted((a,b))) for a in range(30) for b in C[a]}
assert all(len({colors[tuple(sorted((a,b)))] for b in C[a]})==4 for a in range(30))
inputs=dict(field=5,controller=C,linear_maps='all identity',color_vectors=V,triangle_coefficients=[0,1,4],external_coefficients=[1,4],canonical_pentagons=cycles,conic_triple_checks=conic_checks,
 edges=[dict(vertices=list(e),color=colors[e],kind=kind[e],direction=V[colors[e]]) for e in sorted(colors)],candidate_count=1)
(HERE/'INPUT.json').write_text(json.dumps(inputs,indent=2)+'\n')
allv=set(itertools.product(range(5),repeat=3));results=[]
for a in [0,20,28,22,9]:
 saved=json.loads((HERE.parent/f'f5_d10_closed_route_diagnosis/CYCLE_ROOT_{a}.json').read_text());words=saved['closed_words']
 assert Counter(len(w['ports']) for w in words)=={0:1,2:4,3:2,4:28}
 unions={0:set(),2:set(),3:set(),4:set()};details=[]
 for word in words:
  vertices=word['vertices'];image={(0,0,0)}
  for u,v in zip(vertices,vertices[1:]):
   e=tuple(sorted((u,v)));direction=V[colors[e]];A=[0,1,4] if kind[e]=='triangle' else [1,4];sign=1 if u<v else -1
   image={tuple((x[i]+sign*t*direction[i])%5 for i in range(3)) for x in image for t in A}
  length=len(word['ports']);unions[length]|=image
  details.append(dict(vertices=vertices,edge_colors=[colors[tuple(e)] for e in word['edges']],endpoint_count=len(image),endpoints=sorted(image)))
 total=set.union(*unions.values());even=unions[0]|unions[2]|unions[4]
 ext=[tuple(sorted((a,b))) for b in C[a] if kind[tuple(sorted((a,b)))]=='external']
 result=dict(root=a,return_word_counts=dict(sorted(Counter(len(w['ports']) for w in words).items())),union_by_length={k:len(v) for k,v in unions.items()},even_union=len(even),triangle_union=len(unions[3]),triangle_added=len(unions[3]-even),total=len(total),missing=sorted(allv-total),external_edges=[list(e) for e in ext],external_colors=[colors[e] for e in ext],external_gap_shapes=[2,2],all_source_coordinates_equivalent_by_translation=True,word_data=details)
 (HERE/f'ROOT_{a}.json').write_text(json.dumps(result,indent=2)+'\n');results.append({k:v for k,v in result.items() if k!='word_data'})
summary=dict(status='SINGLE_CONIC_LOCAL_PREDICTION_SUPPORTED' if all(x['total']==125 for x in results) else 'SINGLE_CONIC_LOCAL_PREDICTION_REFUTED',candidate_count=1,roots=results,all_five_local_same_fibers_covered=all(x['total']==125 for x in results),same_gap_root_fullcover=[x['root'] for x in results if x['total']==125],new_controller_word_enumerations=0,whole_graphs_expanded=0,BFS_runs=0,coloring_searches=0,CPU_seconds=time.process_time()-start)
(HERE/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
