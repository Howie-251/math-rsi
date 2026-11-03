from pathlib import Path
from collections import Counter
from itertools import combinations
import json,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(3,3));P=Path(__file__).resolve().parent;started=time.process_time();source=P.parent.parent/'second_mechanism/rajiv252.edges'
raw=[tuple(map(int,line.split())) for line in source.read_text().splitlines() if line.strip()];E=raw[1:] if raw[0]==(252,630) else raw;E={tuple(sorted(e)) for e in E};adj=[[] for _ in range(252)]
for u,v in E:adj[u].append(v);adj[v].append(u)
for row in adj:row.sort()
projection=[[] for _ in range(42)];ends={}
for c in range(147,252):
 a=tuple(v for v in adj[c] if v<42);assert len(a)==2;ends[c]=a;projection[a[0]].append(a[1]);projection[a[1]].append(a[0])
def components(vertices,nb):
 unseen=set(vertices);out=[]
 while unseen:
  r=min(unseen);unseen.remove(r);todo=[r];comp=[]
  while todo:
   u=todo.pop();comp.append(u)
   for v in nb[u]:
    if v in unseen:unseen.remove(v);todo.append(v)
  out.append(sorted(comp))
 return out
cells=components(range(42),projection);Bnb={b:[v for v in adj[b] if 42<=v<147] for b in range(42,147)};triangles=components(range(42,147),Bnb)
assert len(cells)==7 and all(len(c)==6 and all(set(projection[u])==set(c)-{u} for u in c) for c in cells)
assert len(set(ends.values()))==105 and len(triangles)==35 and all(len(t)==3 and all(set(Bnb[b])==set(t)-{b} for b in t) for t in triangles)
cell_of={a:i for i,c in enumerate(cells) for a in c};triangle_of={b:i for i,t in enumerate(triangles) for b in t};c_cell={c:cell_of[a[0]] for c,a in ends.items()};tri_records=[];tri_cells=[]
for ti,bs in enumerate(triangles):
 cs=sorted({c for b in bs for c in adj[b] if c>=147});bycell={u:[c for c in cs if c_cell[c]==u] for u in sorted({c_cell[c] for c in cs})};assert len(cs)==9 and len(bycell)==3
 for u,cc in bycell.items():assert len(cc)==3 and sorted(a for c in cc for a in ends[c])==cells[u]
 tri_cells.append(tuple(bycell));tri_records.append(dict(triangle_id=ti,B_vertices=bs,A_cells=list(bycell),C_by_A_cell={u:[dict(C=c,A_edge=ends[c]) for c in cc] for u,cc in bycell.items()}))
assert len(set(tri_cells))==35 and set(tri_cells)==set(combinations(range(7),3))
synthemes={};C_records=[]
for c in range(147,252):
 u=c_cell[c];bs=[b for b in adj[c] if 42<=b<147];tis=[triangle_of[b] for b in bs];assert len(tis)==len(set(tis))==3
 pairs=tuple(sorted(tuple(v for v in tri_cells[ti] if v!=u) for ti in tis));assert all(len(x)==2 for x in pairs) and sorted(v for pair in pairs for v in pair)==[v for v in range(7) if v!=u]
 synthemes[c]=pairs;C_records.append(dict(id=c,A_cell=u,A_edge=ends[c],B_neighbors=bs,B_triangle_ids=tis,syntheme_on_other6_cells=pairs))
def matchings(U):
 U=tuple(U)
 if not U:return [()]
 a=U[0];out=[]
 for b in U[1:]:
  out.extend(tuple(sorted(((a,b),)+m)) for m in matchings([x for x in U if x not in (a,b)]))
 return out
def pentads(U):
 ms=matchings(U);return [tuple(sorted(p)) for p in combinations(ms,5) if len({pair for m in p for pair in m})==15]
A_records=[];Acoord={};Ccoord={}
for u in range(7):
 all_s=set(matchings([v for v in range(7) if v!=u]));cs=[c for c in range(147,252) if c_cell[c]==u];assert {synthemes[c] for c in cs}==all_s and len(cs)==15
 all_p=set(pentads([v for v in range(7) if v!=u]));assert len(all_p)==6
 actual_p=set()
 for a in cells[u]:
  pc=tuple(sorted(synthemes[c] for c in adj[a]));actual_p.add(pc);Acoord[u,pc]=a;A_records.append(dict(id=a,cell=u,pentad_of5_synthemes=pc,C_neighbors=adj[a]))
 assert actual_p==all_p
 for c in cs:Ccoord[u,synthemes[c]]=c
B_records=[];Bcoord={}
for b in range(42,147):
 T=tri_cells[triangle_of[b]];cs=[c for c in adj[b] if c>=147];assert len(cs)==3 and {c_cell[c] for c in cs}==set(T)
 rem=[]
 for c in cs:
  pair=tuple(x for x in T if x!=c_cell[c]);assert pair in synthemes[c];rem.append(tuple(p for p in synthemes[c] if p!=pair))
 assert rem[0]==rem[1]==rem[2] and sorted(x for pair in rem[0] for x in pair)==[x for x in range(7) if x not in T]
 Bcoord[T,rem[0]]=b;B_records.append(dict(id=b,triple=T,matching_on_complement4=rem[0],C_neighbors=cs))
for T in combinations(range(7),3):assert {M for TT,M in Bcoord if TT==T}==set(matchings([x for x in range(7) if x not in T]))
# Generate every edge from the combinatorial coordinates, without using A7 permutations.
reconstructed=set()
for (u,pc),a in Acoord.items():
 for sy in pc:reconstructed.add(tuple(sorted((a,Ccoord[u,sy]))))
for (T,M),b in Bcoord.items():
 for u in T:
  sy=tuple(sorted((tuple(x for x in T if x!=u),)+M));reconstructed.add(tuple(sorted((b,Ccoord[u,sy]))))
 for (TT,MM),bb in Bcoord.items():
  if TT==T and b<bb:reconstructed.add((b,bb))
assert reconstructed==E and len(E)==630
maps=dict(A_cells=cells,B_triangles=tri_records,A_vertices=A_records,B_vertices=B_records,C_vertices=C_records)
(P/'coordinate_tables.json').write_text(json.dumps(maps,indent=2)+'\n')
(P/'regenerated252.edges').write_text('252 630\n'+''.join(f'{u} {v}\n' for u,v in sorted(reconstructed)))
result=dict(status='CELL_MODEL_AND_COMPLETE_COMBINATORIAL_RULE_RECOVERED',source_edges=str(source),A_projected_component_sizes=[len(c) for c in cells],A_projection_simple=True,B_component_sizes=[len(t) for t in triangles],B_triples_are_all35_cell_triples=True,B_triangle_in_each_cell_is_K6_perfectmatching=True,C_other6_cells_form_perfectmatching=True,C_per_cell=15,A_pentads_per_cell=6,B_vertices_per_triple=3,A7_permutation_generators_recovered=False,source_edge_equality=True,vertices=252,edges=630,degrees=dict(Counter(map(len,adj))),BFS_performed=False,new_parameters_searched=False,CPU_seconds=time.process_time()-started)
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
