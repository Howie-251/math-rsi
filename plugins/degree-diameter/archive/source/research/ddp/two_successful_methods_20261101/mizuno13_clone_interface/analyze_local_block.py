from pathlib import Path
from collections import Counter,defaultdict
import json,time,resource

D=Path(__file__).resolve().parent
T=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(120,121))
K=json.loads((D/'LINE_KERNELS.json').read_text());C=K['chart'];M=json.loads((D/'MAPPING_DATA.json').read_text());S=json.loads((D/'STRUCTURE.json').read_text())
V=[tuple((x//3**i)%3 for i in range(5)) for x in range(243)]
def rank(vectors):
    rows=[list(x) for x in vectors];r=0
    for j in range(5):
        k=next((i for i in range(r,len(rows)) if rows[i][j]),None)
        if k is None:continue
        rows[r],rows[k]=rows[k],rows[r];z=pow(rows[r][j],-1,3);rows[r]=[v*z%3 for v in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][j]:
                z=rows[i][j];rows[i]=[(a-z*b)%3 for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows):break
    return r
def projective(v):
    z=pow(next(x for x in v if x),-1,3)
    return tuple(x*z%3 for x in v)
def encoded(v):return sum(x*3**i for i,x in enumerate(v))
def port_neighbors(u,p,x,remove_loop=True):
    e=C[u][p];xx=V[x];y=[sum(a*b for a,b in zip(row,xx))%3 for row in e['A']]
    result={243*e['target']+encoded([(a+t*b)%3 for a,b in zip(y,e['b'])]) for t in range(3)}
    if remove_loop:result.discard(243*u+x)
    return sorted(result)
classes=[]
for u,row in enumerate(C):
    dirs={projective(e['source_line_kernel']) for e in row};assert len(dirs)==4 and rank(list(dirs))==2
    W={tuple((a*x+b*y)%3 for x,y in zip(list(dirs)[0],next(v for v in dirs if rank([list(dirs)[0],v])==2))) for a in range(3) for b in range(3)}
    assert len(W)==9 and {projective(v) for v in W if any(v)}==dirs
    classes.append({'controller':u,'projective_directions':sorted(dirs),'W_vectors':sorted(W)})
assert len({tuple(tuple(v) for v in x['W_vectors']) for x in classes})==1
nonself=0;assert all(e['target']!=0 for e in C[0])
shared0=set(port_neighbors(0,0,0)) & set(port_neighbors(0,0,2))
assert shared0
selfcase=S['self_ports'][0];u=selfcase['controller'];p=selfcase['port'];y=encoded(C[u][p]['source_line_kernel'])
raw0=port_neighbors(u,p,0,False);rawy=port_neighbors(u,p,y,False);after0=port_neighbors(u,p,0,True);aftery=port_neighbors(u,p,y,True)
assert raw0==rawy and set(after0)&set(aftery)
u=0
centers=[code for code,v in enumerate(V) if v[0]==v[1]==0];assert len(centers)==27
ordinary=defaultdict(list);main=defaultdict(list);spare=defaultdict(list)
for x in centers:
    for p in range(4):
        for v in port_neighbors(u,p,x):ordinary[v].append(x)
    v=243*M['main_fiber_target'][u]+M['main_fiber_coordinate_maps'][u][x];main[v].append(x)
    v=M['spare_vertex_map'][243*u+x]
    if v>=0:spare[v].append(x)
allload=defaultdict(list)
for name,part in [('ordinary',ordinary),('M',main),('P',spare)]:
    for v,xs in part.items():
        for x in xs:allload[v].append({'kind':name,'center':243*u+x})
collisions=[{'old_vertex':v,'providers':ps} for v,ps in sorted(allload.items()) if len(ps)>1]
byfiber=Counter(v//243 for v in allload)
res={'status':'CAP14_ALL81_FIBER_BLOCKS_EXCLUDED_BY_COMMON_W_COSSETS','all_controllers_checked':364,'W_dimension':2,'common_W_projective_directions':classes[0]['projective_directions'],'common_W_vectors':classes[0]['W_vectors'],'four_lines_exhaust_all_projective_lines_of_W':True,'any_same_fiber_full_neighborhood_clone_center_count_upper':27,'same_fiber_bound_scope':'Any center subset in one original243-point fiber, cap14, all old edges retained, each clone uses full oldN(v). Not only affine hyperplanes. Not a global clone count bound.','ordinary_raw_threepoint_neighbor_sets_of_line_partner_centers_equal':True,'nonself_example':{'controller':0,'port':0,'center_labels':[0,2],'shared_ordinary_neighbors':sorted(shared0)},'selfport_example':{'controller':selfcase['controller'],'port':selfcase['port'],'source_coordinates':[0,y],'source_labels':[243*selfcase['controller'],243*selfcase['controller']+y],'raw_neighbors_equal':raw0,'neighbors_after_loop_removal':[after0,aftery],'shared_after_loop_removal':sorted(set(after0)&set(aftery))},'single_27_center_probe':{'controller':u,'reason_chosen':'first controller0; no self port and no P endpoints; M coordinate map is affine','center_rule':'x0=y0=0, arbitrary x1,y1,z inF3','center_local_labels':centers,'center_global_labels':[243*u+x for x in centers],'ordinary_neighbor_union_size':len(ordinary),'ordinary_max_provider_count':max(map(len,ordinary.values())),'M_image_count':len(main),'P_image_count':len(spare),'old_neighbor_union_size':len(allload),'total_neighbor_incidences':sum(map(len,allload.values())),'max_old_load':max(map(len,allload.values())),'old_union_counts_by_fiber':dict(sorted(byfiber.items())),'ordinary_M_overlap_size':len(set(ordinary)&set(main)),'all_collision_count':len(collisions),'first_collisions':collisions[:20],'cap14_feasible_for_this_27_center_set':not collisions},'selected_fiber_M_target':M['main_fiber_target'][0],'preprocessing_CPU_seconds':time.process_time()-T,'source_BFS_runs':0,'full_graph_generated':False,'solver_calls':0}
(D/'LOCAL_27_BOUND_AND_PROBE.json').write_text(json.dumps(res,indent=2)+'\n')
(D/'COMMON_W_CERTIFICATE.json').write_text(json.dumps({'all_controllers':classes,'CPU_counted_in':'LOCAL_27_BOUND_AND_PROBE.json'},indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k not in ['common_W_vectors','nonself_example','selfport_example']}))
print('examples',json.dumps({'nonself':res['nonself_example'],'self':res['selfport_example']}))
