"""Uniform fractional outer 5-graph: exact universal obstruction for all twelve centre links."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,time
HERE=Path(__file__).resolve().parent
start=time.process_time();m=json.loads((HERE/'MODEL.json').read_text());den=comb(21,5);weight=Q(29,den);caps=m['simple_orbit_capacities'];assert sum(caps)==den
ns=[weight*c for c in caps];P=[[Q(v)for v in row]for row in m['probabilities']];scores=[sum(n*p for n,p in zip(ns,row))for row in P];marg=[sum(n*a for n,a in zip(ns,row))for row in m['constraint_coefficients']]
assert sum(ns)==29 and all(x>=lo and(hi is None or x<=hi)for x,lo,hi in zip(marg,m['lower'],m['upper']))
all_color_scores=[Q(29*(comb(r,5)if r>=5 else 0)+29*(comb(21-r,5)if 21-r>=5 else 0),den)for r in range(22)]
assert min(scores)==min(all_color_scores)==Q(58,57)>1
out=dict(scope=__doc__,status='EXACT_UNIFORM_FRACTIONAL_OBSTRUCTION',not_a_hypergraph=True,whole_outer_vertex_count=21,all_outer_5sets=den,weight_on_every_outer_5set=str(weight),outer_total_weight='29',outer_degree_of_every_vertex=str(29*Q(5,21)),outer_codegree_of_every_pair=str(29*Q(5*4,21*20)),counts=[dict(edge=e,count=str(n))for e,n in zip(m['edges'],ns)],exact_minimum_score=str(min(scores)),marginals=[str(x)for x in marg],score_by_red_vertex_count=[str(x)for x in all_color_scores],minimum_attained_red_counts=[r for r,z in enumerate(all_color_scores)if z==min(all_color_scores)],verified_orbit_families=len(scores),scope_of_analytic_extension='For any of the twelve actual centre links, attach this fractional outer graph. It satisfies pointwise minimum degree and pair-cover inequalities; all legal colouring mixtures have mono first moment >=58/57. This does not assert an integer outer graph.',cpu_seconds=time.process_time()-start)
assert out['outer_codegree_of_every_pair']=='29/21'
(HERE/'UNIFORM_OBSTRUCTION.json').write_text(json.dumps(out,indent=2)+'\n');print({k:out[k]for k in ['exact_minimum_score','outer_degree_of_every_vertex','outer_codegree_of_every_pair','cpu_seconds']})
