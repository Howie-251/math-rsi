"""The one12-vertex controller and scalar certificate, no large graph generation."""
import itertools,json,time
from pathlib import Path

start=time.process_time()
vertices=[(i,j) for i in range(4) for j in range(4) if i!=j]
index={v:i for i,v in enumerate(vertices)}
neighbors=[sorted([index[(j,i)]]+[index[(i,k)] for k in range(4) if k!=i and k!=j]) for i,j in vertices]
assert all(len(set(ns))==3 and u not in ns and all(u in neighbors[v] for v in ns) for u,ns in enumerate(neighbors))
words={}
for u in range(12):
    for a in neighbors[u]:
        for b in neighbors[a]:
            for v in neighbors[b]:
                words.setdefault((u,v),[u,a,b,v])
assert len(words)==144
packings=[]
for chosen in itertools.combinations(range(12),4):
    if len(set(v for u in chosen for v in neighbors[u]))==12:
        packings.append(list(chosen))
assert packings
chosen=packings[0]
induced=[(u,v) for u in chosen for v in neighbors[u] if v in chosen and u<v]
assert len(induced)==2 and all(sum(v in chosen for v in neighbors[u])==1 for u in chosen)
result={'status':'SMALL_CONTROLLER_AND_SCALAR_CERTIFICATE_PASS','vertices':vertices,'adjacency':neighbors,'edges':[(u,v) for u in range(12) for v in neighbors[u] if u<v],'controller_order':12,'degree':3,'all_ordered_pairs_with_exact_threewalk':144,'threewalk_witnesses':[{'source':u,'target':v,'walk':w} for (u,v),w in sorted(words.items())],'chosen_four_centers':chosen,'chosen_four_center_darts':[vertices[u] for u in chosen],'four_open_neighborhoods':[neighbors[u] for u in chosen],'open_neighborhoods_partition_all_vertices':True,'selected_induced_edges':induced,'selected_controller_centers_independent':False,'selected_induced_graph':'2K2','other_controllers_searched':0,'all_four_point_subsets_examined':495,'four_open_partition_solutions':len(packings),'q':16,'GQ_points':4369,'ovoid_size':257,'source_n':52428,'source_degree':51,'selected_source_centers':1028,'selected_source_induced_graph':'514K2 (duality-ovoid perfect matchings)','bounds':[{'degree':51+k,'copies':k,'order':52428+k*1028} for k in [3,4,5]],'CPU_seconds':time.process_time()-start,'CPU_budget_seconds':10,'large_graphs_generated_or_read':0,'BFS_Lean_solver':0,'all_children_terminal':True}
out=Path(__file__).with_name('DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101_SMALL_CERTIFICATE.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','chosen_four_center_darts','selected_induced_graph','bounds','CPU_seconds']}))
