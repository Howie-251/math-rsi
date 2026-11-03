#!/usr/bin/env python3
"""One bounded GF4-plane controller-capacity transfer, with current-R2 extensions."""
import collections,json,math,os,pathlib,resource,time,warnings
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
START=time.process_time()
D=pathlib.Path(__file__).resolve().parent
ROOT=D.parents[4]
SOURCE_REL=pathlib.Path('research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/graph_d20_D3_n3840.edges')
PARAM_REL=SOURCE_REL.parent/'PARAMETERS.json'
def save(name,x):(D/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def cpu():return time.process_time()-START
def guard():
    if cpu()>29:raise RuntimeError('whole30CPU budget reserve reached')
def mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return z
def dot(a,b):
    z=0
    for x,y in zip(a,b):z^=mul(x,y)
    return z
def decode(c):return [c%4,c//4%4,c//16]
def encode(v):return sum(x*4**j for j,x in enumerate(v))
def mv(T,x):return [dot(row,x) for row in T]

def structure(P):
    began=time.process_time();C,T,L,inv=[P[k] for k in ['controller','dart_matrices','directions','inverse_ports']]
    assert len(C)==60 and all(len(set(row))==5 for row in C)
    assert all(C[C[u][p]][inv[p]]==u for u in range(60) for p in range(5))
    assert P['field']==4 and P['field_polynomial']=='w^2+w+1' and P['vertex_label']=='64*u+x0+4*x1+16*x2'
    normal=[1,1,2];products=[dot(normal,d) for d in L];assert all(products)
    plane=[c for c in range(64) if dot(normal,decode(c))==0];assert len(plane)==16
    darts=[]
    for u in range(60):
        for p,v in enumerate(C[u]):
            guard();mapped=mv(T[u][p],L[p]);target=L[inv[p]]
            scale=next((s for s in range(1,4) if [mul(s,x) for x in target]==mapped),None)
            assert scale is not None
            assert len({encode(mv(T[u][p],decode(c))) for c in range(64)})==64
            lines=[]
            for c in plane:
                base=mv(T[u][p],decode(c))
                line=sorted(encode([base[j]^mul(t,target[j]) for j in range(3)]) for t in range(4))
                assert len(set(line))==4;lines.append(line)
            flat=[x for line in lines for x in line];assert sorted(flat)==list(range(64))
            darts.append({'source':u,'port':p,'target':v,'reverse_port':inv[p],
                          'direction_scale':scale,'plane_center_neighbor_lines':lines,'covered':64,'overlap':0})
    result={'field':'GF4, xor addition, polynomial0b111 multiplication','normal':normal,'normal_dot_directions':products,
            'plane_local_codes':plane,'controller_darts_checked':len(darts),'all_chart_maps_bijective':True,
            'all_source_direction_lines_map_to_reverse_direction_lines':True,'all16lines_partition_target64':True,
            'darts':darts,'CPU_seconds':time.process_time()-began}
    save('PLANE_DART_CHECK.json',result)
    return C,plane,darts

def solve(C,k):
    import numpy as np
    from scipy.optimize import milp,Bounds,LinearConstraint
    from scipy.sparse import csc_matrix
    began=time.process_time();A=np.zeros((60,60))
    for b,row in enumerate(C):
        for a in row:A[b,a]+=1
    with warnings.catch_warnings(record=True) as ws:
        warnings.simplefilter('always')
        opt=milp(c=-np.ones(60),integrality=np.ones(60),bounds=Bounds(np.zeros(60),np.full(60,k)),
                 constraints=LinearConstraint(csc_matrix(A),np.full(60,-np.inf),np.full(60,k)),
                 options={'time_limit':8.,'mip_rel_gap':0.,'threads':1,'disp':False})
    r=None
    if opt.x is not None:
        r=[int(round(float(v))) for v in opt.x]
        assert max(abs(float(v)-q) for v,q in zip(opt.x,r))<1e-5
        assert all(0<=q<=k for q in r)
        assert all(sum(r[a] for a in row)<=k for row in C)
    count=sum(r) if r is not None else None
    global_upper=12*k
    # A numerical MILP optimal status is retained as a solver report, not an
    # independently certified upper bound. Counting-bound attainment is exact.
    proven=bool(count==global_upper)
    res={'k':k,'solver':'scipy.optimize.milp / bundled HiGHS','solver_calls':1,'threads':1,
         'status_code':int(opt.status),'message':str(opt.message),'r':r,'sum_r':count,
         'feasible_lower_bound':count,'counting_upper_bound':global_upper,
         'exact_optimum':proven,'upper_bound':count if proven else global_upper,
         'solver_reports_optimum':bool(opt.status==0 and r is not None),
         'solver_optimality_independently_certified':False,
         'mip_dual_bound':None if getattr(opt,'mip_dual_bound',None) is None else float(-opt.mip_dual_bound),
         'mip_gap':None if getattr(opt,'mip_gap',None) is None else float(opt.mip_gap),
         'mip_node_count':None if getattr(opt,'mip_node_count',None) is None else int(opt.mip_node_count),
         'warnings':[str(w.message) for w in ws],'CPU_seconds':time.process_time()-began,'time_limit_seconds':8}
    save(f'SEARCH_k{k}.json',res);guard();return res

def read_source(darts,plane):
    with (ROOT/SOURCE_REL).open() as f:
        n,m=map(int,f.readline().split());assert (n,m)==(3840,38400)
        edges=[tuple(map(int,line.split())) for line in f if line.strip()]
    assert len(edges)==m
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    assert all(len(row)==20 for row in adj)
    for dart in darts:
        u,v=dart['source'],dart['target']
        for c,line in zip(plane,dart['plane_center_neighbor_lines']):
            actual=sorted(z-64*v for z in adj[64*u+c] if z//64==v)
            assert actual==line
    save('LITERAL_PLANE_BINDING.json',{'source_edge_file_reads':1,'source_n':n,'source_m':m,
         'checked_center_dart_lines':60*5*16,'all_literal_center_neighbor_lines_match_parameters':True,
         'old_source_BFS_runs':0,'source_D3':'inherited independent all3840-root acceptance'})
    return edges,adj

def construct(k,r,C,plane,source_edges,oldadj):
    began=time.process_time();cap=20+k;load=[sum(r[a] for a in row) for row in C];assert max(load)<=k
    adj=[row.copy() for row in oldadj];degree=list(map(len,adj));edges=source_edges.copy();steps=[]
    for a in range(60):
        for j in range(r[a]):
            for c in plane:
                guard();owner=64*a+c;pins=sorted(oldadj[owner]);assert len(set(pins))==20
                n=len(adj);pin_degrees=[degree[s] for s in pins];assert max(pin_degrees)<cap
                distance=[-1]*n;queue=[]
                for s in pins:distance[s]=0;queue.append(s)
                for x in queue:
                    if distance[x]==2:continue
                    for y in adj[x]:
                        if distance[y]<0:distance[y]=distance[x]+1;queue.append(y)
                assert len(queue)==n
                hist=collections.Counter(distance);assert set(hist)<={0,1,2}
                steps.append({'new_vertex':n,'owner':owner,'controller':a,'plane_local_code':c,'multiplicity_copy':j,
                              'pins':pins,'pin_degrees_before_addition':pin_degrees,'current_n_before_addition':n,
                              'closed_R2_current_covered':len(queue),'uncovered_targets':0,'pin_distance_histogram':dict(hist)})
                adj.append(pins.copy());degree.append(20)
                for s in pins:adj[s].append(n);degree[s]+=1;edges.append((s,n))
    n=len(adj);t=len(steps);assert n==3840+16*sum(r) and len(edges)==38400+20*t
    assert all(degree[v]==20+load[v//64] for v in range(3840))
    assert max(degree)<=cap
    rows=sorted((min(u,v),max(u,v)) for u,v in edges)
    assert len(rows)==len(set(rows)) and all(u!=v for u,v in rows)
    name=f'graph_d{cap}_D3_n{n}.edges'
    with (D/name).open('w') as f:
        f.write(f'{n} {len(rows)}\n')
        for u,v in rows:f.write(f'{u} {v}\n')
    save(f'RECIPE_d{cap}.json',{'source_file':str(SOURCE_REL),'source_parameter_file':str(PARAM_REL),
          'source_D3_inherited':True,'field':'GF4 / polynomial w^2+w+1','center_plane_normal':[1,1,2],
          'center_plane_rhs':0,'plane_local_codes':plane,'controller_multiplicities':r,'old_fiber_loads':load,
          'new_vertices':t,'fixed_clone_pins':'full original source open neighborhood of owner','steps':steps})
    result={'status':'PRODUCER_COMPLETE_GRAPH_BY_CURRENT_R2_EXTENSION_INDUCTION','Delta':cap,'D':3,'n':n,'m':len(rows),
            'new_roots':t,'degree_histogram':dict(collections.Counter(degree)),'max_degree':max(degree),
            'all_source_edges_preserved':True,'simple':True,'connected':True,'diameter_at_most3':True,
            'diameter_exact3_basis':'n exceeds maximum-degree-cap diameter2 Moore bound',
            'current_complete_R2_pin_union_checks':t,'uncovered_targets_each_step':0,
            'source_old_root_BFS_runs':0,'new_root_ordinary_BFS_runs':0,'graph_file':name,'recipe_file':f'RECIPE_d{cap}.json',
            'previous_project_example_n':{1:3900,2:4125}[k],'local_order_gain':n-{1:3900,2:4125}[k],
            'CPU_seconds':time.process_time()-began,'global_record_claim':False,'public_comparison':'PENDING',
            'fresh_independent_new_graph_validation':'pending_root'}
    save(f'GRAPH_RESULT_d{cap}.json',result);return result

def main():
    if (D/'RESULT.json').exists():raise SystemExit('bounded batch already complete; no rerun')
    soft,hard=resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU,(30 if hard<0 else min(30,hard),hard))
    P=json.loads((ROOT/PARAM_REL).read_text());C,plane,darts=structure(P)
    save('CONTROLLER_CAPACITY_MODEL.json',{'controller':C,'variables':60,'r_domains':'0..k integers','k':[1,2],
          'constraints':'sum neighboring controller r <= k','objective':'max sum r','counting_upper':{'1':12,'2':24},
          'normal':[1,1,2],'field':'GF4','solver_calls':2,'solver_time_limit_each_seconds':8,'whole_CPU_limit_seconds':30})
    searches=[solve(C,k) for k in (1,2)];eligible=[]
    for s in searches:
        previous={1:3900,2:4125}[s['k']]
        if s['r'] is not None and 3840+16*s['sum_r']>previous:eligible.append(s)
    graphs=[]
    if eligible:
        edges,adj=read_source(darts,plane)
        for s in eligible:graphs.append(construct(s['k'],s['r'],C,plane,edges,adj))
    whole=cpu();assert whole<30
    result={'status':'BOUNDED_BATCH_COMPLETE','graphs':graphs,'searches':searches,'new_graphs_generated':len(graphs),
            'whole_CPU_seconds':whole,'workers':1,'source_edge_file_reads':int(bool(eligible)),'source_old_root_BFS_runs':0,
            'solver_calls':2,'confirmed_records':0,'global_comparison':'PENDING','no_additional_k_seed_or_plane_search':True}
    save('RESULT.json',result);save('TERMINAL.json',{'running':False,'status':'COMPLETE','whole_CPU_seconds':whole,
          'solver_calls':2,'generated_graphs':len(graphs),'no_more_work_scheduled':True})
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
