from pathlib import Path
from collections import Counter,defaultdict
import json,time
P=Path(__file__).resolve().parent;A=P/'author_recipe';start=time.process_time()
construction=json.loads((A/'deg12_diam6_n364032_construction.json').read_text())
rows=[[int(x) for x in line.split()] for line in (A/'deg12_diam6_n364032_pattern_graph.adj').read_text().splitlines() if line.strip()]
assert len(rows)==9720 and all(row[0]==i for i,row in enumerate(rows))
adj=[r[1:] for r in rows]
assert all(len(set(row))==len(row) and i not in row and all(0<=v<9720 and i in adj[v] for v in row) for i,row in enumerate(adj))
cutrows=[[int(x) for x in line.split()] for line in (A/'deg12_diam6_n364032_subdivided_edges.txt').read_text().splitlines() if line.strip()]
assert len(cutrows)==9720 and [r[0] for r in cutrows]==list(range(354312,364032))
assert len({tuple(sorted(r[1:])) for r in cutrows})==9720
byline=defaultdict(list)
for new,line,point in cutrows:
 assert 177156<=line<354312 and 0<=point<177156
 byline[line].append(new-354312)
sizes=Counter(map(len,byline.values()))
assert sizes=={7:840,8:480}
assert len({r[2] for r in cutrows})==9720
internal=external=0;external_by_line_size=defaultdict(Counter)
for ids in byline.values():
 group=set(ids)
 for u in ids:
  assert group-{u}<=set(adj[u])
  ins=sum(v in group for v in adj[u]);outs=len(adj[u])-ins
  internal+=ins;external+=outs;external_by_line_size[len(ids)][outs]+=1
degree=Counter(map(len,adj))
assert degree=={10:9720}
facts={'status':'PRIMARY_RECIPE_PROVES_FULL12REGULAR_NO_SPARE_ENTRY',
 'primary_description_URL':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g6.html',
 'primary_package_URL':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD6/deg12_diam6_n364032.zip',
 'primary_package_bytes':(P/'author_recipe.zip').stat().st_size,'source_credit':'Dharunish Yugeswardeenoo, October7 2026',
 'source_order_published':364032,'source_D_published':6,'source_D_reverified':False,
 'full_literal_acquired':False,'literal_n_header':None,'literal_m_header':None,
 'base_object':'Incidence graph of split Cayley generalized hexagon H(11)',
 'base_n':354312,'base_degree_published':12,'base_m_derived':2125872,
 'new_vertices_actual_package':9720,'subdivisions_actual_package':9720,
 'subdivided_old_edges_distinct':True,'points_subdivided_distinct':True,
 'used_spread_line_group_sizes':dict(sizes),'pattern_degree_histogram_actual':dict(degree),
 'pattern_n':9720,'pattern_m':sum(map(len,adj))//2,
 'same_line_clique_edges':internal//2,'external_pattern_edges':external//2,
 'external_degree_by_line_group_size':{str(k):dict(v) for k,v in external_by_line_size.items()},
 'degree_preservation_proof':'Every old endpoint loses one incidence edge and gains its subdivision neighbor for each cut, preserving base degree12. Each new vertex has its two old endpoints plus exactly10 distinct pattern neighbors. Thus the author-defined full source is12regular.',
 'full_degree_histogram_from_recipe':{'12':364032},'full_m_derived':2184192,
 'free_vertices_from_recipe':0,'free_slots_from_recipe':0,'min_saturated_neighbors_from_recipe':12,
 'onefault_prototypes_from_recipe':0,'zero_fault_prototypes_from_recipe':0,
 'scope_closed':'Retain all edges of this intended12regular source and append any nonempty connected new part under maxdegree12; no old vertex can accept a new edge. The star/proxy family requiring free old pins has no legal pins.',
 'recipe_binding_gap':'Package has no base adjacency; construction.json states that point/line labels use the author own H(11) numbering and cannot reconstruct the full graph from another independently labelled hexagon. Full source/author-numbered base must be obtained before any distance or deletion operation.',
 'D6_source_acceptance_scope':'Official description says its generator package has not been independently verified by the maintainer. This worker certifies only degree consequences of the supplied recipe, not its diameter.',
 'BFS':0,'distance_caches':0,'candidate_graphs':0,'MIP':0,'CPU_seconds':time.process_time()-start}
(P/'SOURCE_FACTS.json').write_text(json.dumps(facts,indent=2)+'\n')
res={'status':'FIXED_PRESERVE_OLD_EDGES_STAR_ENTRY_CLOSED_RECIPE_REGULARITY',
 'prediction':'REFUTED_FOR_PRIMARY_RECIPE','source_order':364032,'source_degree_from_recipe':12,
 'free_from_recipe':0,'minSatN_from_recipe':12,'onefaultcount_from_recipe':0,
 'literal_downloaded':False,'full_graph_generated':False,'source_BFS':0,'candidate_generated':False,
 'actual_new_n':None,'actual_new_D':None,'ordinary_bad_unordered_pairs':None,
 'CPU_seconds':facts['CPU_seconds'],'pending':[]}
(P/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n')
(P/'terminal.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:facts[k] for k in ['pattern_degree_histogram_actual','used_spread_line_group_sizes','external_degree_by_line_group_size','full_degree_histogram_from_recipe','free_vertices_from_recipe','min_saturated_neighbors_from_recipe','CPU_seconds']},indent=2))
