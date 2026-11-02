#!/usr/bin/env python3
"""One bounded new controller-capacity batch, then two complete retained-edge graphs."""
import collections,json,pathlib,time
D=pathlib.Path(__file__).resolve().parent
ROOT=D.parents[3]
START=time.process_time()
def save(name,x):(D/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def bits(mask):
    while mask:
        z=mask&-mask;yield z.bit_length()-1;mask-=z

def rank_mod(A,p):
    M=[[x%p for x in row] for row in A];r=0;pivots=[]
    for c in range(len(M[0])):
        pivot=next((i for i in range(r,len(M)) if M[i][c]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r];v=pow(M[r][c],-1,p);M[r]=[v*x%p for x in M[r]]
        for i in range(r+1,len(M)):
            if M[i][c]:
                v=M[i][c];M[i]=[(a-v*b)%p for a,b in zip(M[i],M[r])]
        pivots.append(c);r+=1
    return {'prime':p,'rank':r,'pivot_columns':pivots}

def packing1(C,limit):
    began=time.process_time();nm=[sum(1<<b for b in row) for row in C]
    conflict=[sum(1<<b for b in range(30) if nm[a]&nm[b]) for a in range(30)]
    best=[];chosen=[];nodes=0;expired=False
    def dfs(av):
        nonlocal best,nodes,expired
        nodes+=1
        if nodes%1024==0 and time.process_time()-began>=limit:expired=True;return
        if expired or len(best)==7:return
        if len(chosen)>len(best):best=chosen.copy()
        if not av or len(chosen)+av.bit_count()<=len(best):return
        resources=0
        for a in bits(av):resources|=nm[a]
        if len(chosen)+resources.bit_count()//4<=len(best):return
        v=max(bits(av),key=lambda a:((conflict[a]&av).bit_count(),-a))
        chosen.append(v);dfs(av&~conflict[v]);chosen.pop()
        if not expired:dfs(av&~(1<<v))
    dfs((1<<30)-1)
    r=[int(a in best) for a in range(30)]
    return {'k':1,'r':r,'sum_r':len(best),'initial_global_upper':7,
            'upper_bound':len(best) if not expired or len(best)==7 else 7,
            'exact_optimum':not expired or len(best)==7,'status':'TIME_LIMIT_FEASIBLE' if expired else 'EXACT',
            'nodes':nodes,'CPU_seconds':time.process_time()-began,'CPU_budget_seconds':limit}

def packing2(C,seed,limit,modrank):
    began=time.process_time();best=[2*x for x in seed];bestval=sum(best);cur=[0]*30;res=[2]*30
    nodes=0;expired=False
    full=next((z for z in modrank if z['rank']==30),None)
    upper=14 if full else 15
    def dfs(av,total):
        nonlocal best,bestval,nodes,expired
        nodes+=1
        if nodes%1024==0 and time.process_time()-began>=limit:expired=True;return
        if expired or bestval==upper:return
        domain={a:min(res[b] for b in C[a]) for a in bits(av)}
        domain={a:d for a,d in domain.items() if d}
        if total>bestval:best=cur.copy();bestval=total
        if not domain:return
        possible=[0]*30
        for a,d in domain.items():
            for b in C[a]:possible[b]+=d
        bound=min(sum(domain.values()),sum(min(res[b],possible[b]) for b in range(30))//4)
        if total+bound<=bestval:return
        v=max(domain,key=lambda a:(sum(3-res[b] for b in C[a]),sum(possible[b] for b in C[a]),-a))
        rest=sum(1<<a for a in domain if a!=v)
        vals=[1,2,0] if domain[v]==2 else [1,0]
        for q in vals:
            cur[v]=q
            for b in C[v]:res[b]-=q
            dfs(rest,total+q)
            for b in C[v]:res[b]+=q
            cur[v]=0
            if expired or bestval==upper:break
    if bestval<upper:dfs((1<<30)-1,0)
    return {'k':2,'r':best,'sum_r':bestval,'initial_global_upper':15,'rank_refined_upper':upper,
            'upper_bound':bestval if not expired or bestval==upper else upper,
            'exact_optimum':not expired or bestval==upper,'status':'TIME_LIMIT_FEASIBLE' if expired else 'EXACT',
            'modular_full_rank_witness':full,'nodes':nodes,'CPU_seconds':time.process_time()-began,'CPU_budget_seconds':limit}

def read_source(path):
    with path.open() as f:
        n,m=map(int,f.readline().split());assert (n,m)==(3750,37500)
        edges=[tuple(map(int,line.split())) for line in f if line.strip()]
    assert len(edges)==m
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    return edges,adj

def construct(k,r,C,source_edges,oldadj):
    began=time.process_time();cap=20+k
    plane=[c for c in range(125) if (c%5+c//5%5+c//25)%5==0]
    assert len(plane)==25
    load=[sum(r[a] for a in C[b]) for b in range(30)]
    assert max(load)<=k
    centers=[(a,j,c) for a in range(30) for j in range(r[a]) for c in plane]
    adj=[row.copy() for row in oldadj];degree=list(map(len,adj));edges=source_edges.copy();steps=[]
    for a,j,c in centers:
        assert time.process_time()-START<29
        owner=125*a+c;pins=sorted(oldadj[owner]);assert len(pins)==20 and len(set(pins))==20
        n=len(adj);old_degrees=[degree[s] for s in pins]
        assert all(x<cap for x in old_degrees)
        distance=[-1]*n;queue=[]
        for s in pins:distance[s]=0;queue.append(s)
        for x in queue:
            if distance[x]==2:continue
            for y in adj[x]:
                if distance[y]<0:distance[y]=distance[x]+1;queue.append(y)
        assert len(queue)==n
        hist=collections.Counter(distance);assert set(hist)<={0,1,2}
        steps.append({'new_vertex':n,'owner':owner,'controller':a,'plane_local_code':c,'multiplicity_copy':j,
                      'pins':pins,'old_pin_degrees':old_degrees,'source_n_before_step':n,
                      'closed_R2_current_covered':len(queue),'uncovered_targets':0,'pin_distance_histogram':dict(hist)})
        adj.append(pins.copy());degree.append(20)
        for s in pins:adj[s].append(n);degree[s]+=1;edges.append((s,n))
    t=len(steps);n=len(adj)
    assert n==3750+25*sum(r) and len(edges)==37500+20*t
    assert all(degree[v]==20+load[v//125] for v in range(3750))
    assert max(degree)<=cap and min(degree)==20
    rows=sorted((min(u,v),max(u,v)) for u,v in edges)
    assert len(set(rows))==len(rows) and all(u!=v for u,v in rows)
    filename=f'graph_d{cap}_D3_n{n}.edges'
    with (D/filename).open('w') as f:
        f.write(f'{n} {len(rows)}\n')
        for u,v in rows:f.write(f'{u} {v}\n')
    recipe={'parameters':[cap,3],'source_n':3750,'source_m':37500,'source_file':str(SOURCE_REL),
            'source_parameter_file':str(PARAM_REL),'source_D3_inherited':True,
            'center_plane_normal':[1,1,1],'center_plane_rhs':0,'plane_local_codes':plane,
            'controller_multiplicities':r,'old_fiber_loads':load,'new_vertices':t,'steps':steps}
    save(f'RECIPE_d{cap}.json',recipe)
    result={'status':'PRODUCER_COMPLETE_GRAPH_BY_CURRENT_R2_EXTENSION_INDUCTION','Delta':cap,'D':3,
            'n':n,'m':len(rows),'min_degree':min(degree),'max_degree':max(degree),
            'degree_histogram':dict(collections.Counter(degree)),'new_roots':t,
            'current_complete_R2_pin_union_checks':t,'uncovered_targets_each_step':0,
            'all_source_edges_preserved':True,'simple':True,'connected':True,
            'diameter_at_most3':True,'diameter_exact3_basis':'Order exceeds degree-cap diameter2 Moore bound',
            'source_old_root_BFS_runs':0,'new_root_ordinary_BFS_runs':0,
            'graph_file':filename,'recipe_file':f'RECIPE_d{cap}.json','CPU_seconds':time.process_time()-began,
            'comparison_status':'PENDING_PRIMARY_GLOBAL_BASELINE','confirmed_record':False,
            'independent_new_graph_validation':'pending_root'}
    save(f'GRAPH_RESULT_d{cap}.json',result)
    return result

PARAM_REL=pathlib.Path('research/ddp/refresh_20261029/f5_full_d20_D3/PARAMETERS.json')
SOURCE_REL=pathlib.Path('research/ddp/refresh_20261029/f5_full_d20_D3/graph_d20_D3_n3750.edges')
def main():
    if (D/'RESULT.json').exists():raise SystemExit('bounded batch already complete')
    P=json.loads((ROOT/PARAM_REL).read_text());C=P['controller']
    assert len(C)==30 and all(len(set(row))==4 for row in C)
    A=[[int(j in C[i]) for j in range(30)] for i in range(30)]
    modrank=[rank_mod(A,p) for p in [5,7,11]]
    save('CONTROLLER_CAPACITY_MODEL.json',{'controller':C,'constraints':'sum neighboring r<=k','k':[1,2],
          'fixed_plane_normal':[1,1,1],'fixed_plane_rhs':0,'modular_ranks':modrank})
    one=packing1(C,5);save('SEARCH_k1.json',one)
    two=packing2(C,one['r'],10,modrank);save('SEARCH_k2.json',two)
    for search in [one,two]:
        assert all(sum(search['r'][a] for a in C[b])<=search['k'] for b in range(30))
    source_edges,oldadj=read_source(ROOT/SOURCE_REL)
    graphs=[construct(1,one['r'],C,source_edges,oldadj),construct(2,two['r'],C,source_edges,oldadj)]
    whole=time.process_time()-START;assert whole<30
    result={'status':'TWO_COMPLETE_PRODUCER_VALIDATED_NEW_PARAMETER_GRAPHS_COMPARISON_PENDING',
            'graphs':graphs,'controller_searches':[one,two],'whole_CPU_seconds':whole,'CPU_budget_seconds':30,
            'workers':1,'source_edge_file_reads':1,'old_source_D3_reverified':False,'source_old_root_BFS_runs':0,
            'new_graphs_generated':2,'confirmed_record_graphs':0,'pending':['root_independent_new_graph_acceptance','degree21_22_primary_public_comparison']}
    save('RESULT.json',result);save('TERMINAL.json',{'running':False,'status':'COMPLETE','whole_CPU_seconds':whole,'confirmed_records':0})
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
