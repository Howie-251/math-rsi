from pathlib import Path
import json
import resource
import time

started=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(2,2))
here=Path(__file__).resolve().parent
project=here.parents[3]
source=project/'research/ddp/breadth_20261027_wave2/triangle_factor33_controller/best.edges'
rows=[list(map(int,s.split())) for s in source.read_text().splitlines() if s.strip() and not s.startswith('#')]
assert rows[0]==[33,66]
edges={tuple(sorted(e)) for e in rows[1:]}
assert len(edges)==66
adj=[set() for _ in range(33)]
for u,v in edges:adj[u].add(v);adj[v].add(u)
extra=[]
for u in range(33):
    assert {3*(u//3)+j for j in range(3)}-{u} <= adj[u]
    extra.append(sorted(v for v in adj[u] if v//3!=u//3))
    assert len(adj[u])==4 and len(extra[u])==2
mixed=[u for u in range(33) if extra[u][0]//3!=extra[u][1]//3]
assert mixed
root=mixed[0]
old_to_new=[-1]*33
new_to_old=[]
assigned_triangles=set()
contacts=[]
def assign_triangle(touched,from_new):
    tri=touched//3
    assert tri not in assigned_triangles
    block=len(new_to_old)//3
    vertices=[touched]+sorted({3*tri,3*tri+1,3*tri+2}-{touched})
    for old in vertices:
        old_to_new[old]=len(new_to_old)
        new_to_old.append(old)
    assigned_triangles.add(tri)
    contacts.append({'new_block':block,'old_triangle':tri,'touched_old_vertex':touched,
                     'anchor_new_vertex':3*block,'first_contact_from_new':from_new,
                     'old_vertices_in_new_order':vertices})
assign_triangle(root,None)
scan=0
while scan<len(new_to_old):
    old=new_to_old[scan]
    for neighbor in extra[old]:
        if neighbor//3 not in assigned_triangles:
            assign_triangle(neighbor,scan)
    scan+=1
assert len(new_to_old)==33 and sorted(old_to_new)==list(range(33))
new_edges={tuple(sorted((old_to_new[u],old_to_new[v]))) for u,v in edges}
assert len(new_edges)==66
assert {tuple(sorted((new_to_old[u],new_to_old[v]))) for u,v in new_edges}==edges
new_adj=[set() for _ in range(33)]
for u,v in new_edges:new_adj[u].add(v);new_adj[v].add(u)
root_extra=sorted(v for v in new_adj[0] if v//3!=0)
assert root_extra==[3,6]
checks=[]
for b in range(1,11):
    external=sorted({v for u in range(3*b,3*b+3) for v in new_adj[u] if v//3!=b})
    m=external[0]
    checks.append({'block':b,'m_b':m,'all_external_neighbor_labels':external,
                   'm_b_less_than_3b':m<3*b,'anchor_edge_present':3*b in new_adj[m],
                   'm_b_equals_first_contact':m==contacts[b]['first_contact_from_new']})
assert all(c['m_b_less_than_3b'] and c['anchor_edge_present'] and c['m_b_equals_first_contact'] for c in checks)
ms=[c['m_b'] for c in checks]
assert ms==sorted(ms)
permutation={'source':str(source.relative_to(project)),'chosen_old_mixed_root':root,
             'chosen_root_old_external_neighbors':extra[root],
             'old_to_new':old_to_new,'new_to_old':new_to_old,'first_contacts':contacts}
(here/'PERMUTATION.json').write_text(json.dumps(permutation,indent=2)+'\n')
(here/'CERTIFICATE.json').write_text(json.dumps({'nonroot_blocks':checks,'m_sequence':ms},indent=2)+'\n')
with (here/'RELABELED33.edges').open('w') as out:
    out.write('33 66\n')
    for u,v in sorted(new_edges):out.write(f'{u} {v}\n')
result={'status':'PASS_ONE_SAVED_OBJECT','source':str(source.relative_to(project)),
        'objects_checked':1,'chosen_old_root':root,'root_external_neighbors_after_relabel':root_extra,
        'all_original_edges_preserved':True,'literal_permutation_bijective':True,
        'checked_nonroot_blocks':10,'m_sequence':ms,'all_conditions_pass':True,
        'general_labeling_theorem_proved_by_this_test':False,
        'random_controllers_generated':0,'bfs_runs':0,'nb3_runs':0,'solver_calls':0,
        'cpu_seconds':time.process_time()-started}
(here/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,separators=(',',':')))
