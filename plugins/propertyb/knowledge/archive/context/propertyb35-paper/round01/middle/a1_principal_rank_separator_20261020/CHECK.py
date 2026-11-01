"""Two explicit graph separators, no H or graph search."""
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
sources=[P.parent/'a1_rank_component_wedge_budget_20261020/VERIFY.json',P.parent/'a1_critical_core_singleton_degree_20261020/CHECK.json']
rows=[]
for src in sources:
 j=json.loads(src.read_text());E={tuple(e) for e in j['graph_edges']};N=35
 d=[sum(v in e for e in E) for v in range(N)]
 # In these two saved literal graphs the three largest degree vertices give the separator.
 C=tuple(sorted(sorted(range(N),key=lambda v:(-d[v],v))[:3]));S=[v for v in range(N) if v not in C]
 uncovered=[e for e in E if not set(e)&set(C)]
 assert len(E)==76 and C==(0,1,25) and not uncovered
 assert len(S)==32
 # A putative5-set realization would force B[S,S]=4I32, rank32>21.
 rho_total=sum(1 for _ in S);assert rho_total==32>21
 rows.append({'source':str(src),'Gamma_edges':len(E),'top3_cover':C,'cover_degrees':[d[v] for v in C],'outside_independent_set':S,'outside_size':32,'uncovered_edges':uncovered,'components_after_deletion':[1]*32,'principal_rank_lower':rho_total,'putative_ground_dimension':21,'excess_rank':rho_total-21,'conclusion':'no realization as non-one-intersection graph of distinct5sets on21points'})
out={'status':'PASS_LITERAL_SEPARATOR_ONLY','scope':'explicit two graph witnesses excluded by principal rank,not rejection of25momentprofiles','rows':rows,'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print({'status':out['status'],'covers':[r['top3_cover'] for r in rows],'ranks':[r['principal_rank_lower'] for r in rows],'cpu_seconds':out['cpu_seconds']})
