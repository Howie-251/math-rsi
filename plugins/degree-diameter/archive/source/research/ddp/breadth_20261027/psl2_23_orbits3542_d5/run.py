from pathlib import Path
from collections import deque,Counter
import json,pickle,random,sys,time,os

D=Path(__file__).resolve().parent
P=23;N0=1518;N1=2024;N=N0+N1
I=(1,0,0,1)
def canon(z):
    w=tuple((-x)%P for x in z)
    return min(z,w)
def mul(a,b):
    x,y,z,w=a;r,s,t,u=b
    return canon(((x*r+y*t)%P,(x*s+y*u)%P,(z*r+w*t)%P,(z*s+w*u)%P))
def inv(a):
    x,y,z,w=a
    return canon((w,(-y)%P,(-z)%P,x))
def power(a,n):
    z=I
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n//=2
    return z
def save(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
def bfs(adj,root):
    dist=[-1]*N;dist[root]=0;q=deque([root])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if dist[b]<0:dist[b]=dist[a]+1;q.append(b)
    return dist
def reachable_score(masks):
    misses=[];reached=[]
    for root in (0,N0):
        seen=front=1<<root
        for depth in range(5):
            nxt=0
            while front:
                bit=front&-front;front-=bit;nxt|=masks[bit.bit_length()-1]
            front=nxt&~seen;seen|=front
        misses.append(N-seen.bit_count());reached.append(seen)
    return (N0*misses[0]+N1*misses[1])//2,misses,reached
def orbital_edges(item,perms):
    root=item['representative'];start=root[0]*N+root[1]
    seen={start};todo=[start]
    while todo:
        a,b=divmod(todo.pop(),N)
        for p in perms:
            u,v=p[a],p[b]
            if u>v:u,v=v,u
            code=u*N+v
            if code not in seen:seen.add(code);todo.append(code)
    result=sorted(seen)
    deg=[0]*N
    for code in result:
        a,b=divmod(code,N);assert a!=b;deg[a]+=1;deg[b]+=1
    x,y=item['degree_vector']
    assert all(v==x for v in deg[:N0]) and all(v==y for v in deg[N0:])
    return result
def graph_from(items,cache,perms,bits):
    masks=[0]*N;edges=[]
    for item in items:
        key=item['id']
        if key not in cache:cache[key]=orbital_edges(item,perms)
        for code in cache[key]:
            u,v=divmod(code,N);masks[u]|=bits[v];masks[v]|=bits[u];edges.append(code)
    assert len(edges)==N*7//2 and all(x.bit_count()==7 for x in masks)
    return masks,edges
def degree_subsets(items,target):
    result=[]
    def rec(pos,remaining,chosen):
        if remaining==0:result.append(chosen);return
        if pos==len(items):return
        for j in range(pos,len(items)):
            d=max(items[j]['degree_vector'])
            if d<=remaining:rec(j+1,remaining-d,chosen+[items[j]['id']])
    rec(0,target,[])
    return result
def choose_items(prep,index):
    ni=len(prep['cross']);nb=len(prep['B_subsets'])
    cross=index%ni;index//=ni;b=index%nb;a=index//nb
    ids=prep['A_subsets'][a]+prep['B_subsets'][b]+[prep['cross'][cross]['id']]
    return [prep['item_by_id'][i] for i in ids],{'A_subset_index':a,'B_subset_index':b,'cross_orbital_index':cross,'orbital_ids':ids}
def save_best(score,misses,edges,choice,evaluation):
    save('best.json',{'n':N,'edges':len(edges),'minimum_degree':7,'maximum_degree':7,'target_D':5,'bad_unordered_pairs':score,'root_misses':misses,'choice':choice,'evaluation':evaluation,'diameter':'pending root independent final check'})
    (D/'best.edges').write_text(f'{N} {len(edges)}\n'+''.join(f'{code//N} {code%N}\n' for code in sorted(edges)))

def prepare():
    start=time.process_time();group=set()
    for a in range(P):
        for c in range(P):
            if not a and not c:continue
            if a:
                ai=pow(a,-1,P)
                for b in range(P):group.add(canon((a,b,c,(1+b*c)*ai%P)))
            else:
                b=(-pow(c,-1,P))%P
                for d in range(P):group.add(canon((a,b,c,d)))
    G=sorted(group);G.remove(I);G.insert(0,I);IX={g:i for i,g in enumerate(G)}
    assert len(G)==6072
    r=next(g for g in G[1:] if power(g,12)==I and power(g,6)!=I and power(g,4)!=I)
    H=[power(r,3*j) for j in range(4)];K=[power(r,4*j) for j in range(3)]
    assert len(set(H))==4 and len(set(K))==3
    def cosets(stab):
        lookup=[-1]*6072;reps=[]
        for g in G:
            if lookup[IX[g]]>=0:continue
            j=len(reps);reps.append(g)
            for h in stab:lookup[IX[mul(g,h)]]=j
        return reps,lookup
    AR,AL=cosets(H);BR,BL=cosets(K)
    assert len(AR)==N0 and len(BR)==N1
    U=(1,1,0,1);W=canon((0,(-1)%P,1,0));generators=[U,W]
    generated={I};todo=[I]
    while todo:
        x=todo.pop()
        for s in generators:
            y=mul(s,x)
            if y not in generated:generated.add(y);todo.append(y)
    assert len(generated)==6072
    perms=[[AL[IX[mul(s,a)]] for a in AR]+[N0+BL[IX[mul(s,b)]] for b in BR] for s in generators]
    assert all(sorted(p)==list(range(N)) for p in perms)
    def internal(stab,reps,lookup,offset,cap,prefix):
        classes={}
        for v,g in enumerate(reps[1:],1):
            gi=inv(g)
            neigh=tuple(sorted({lookup[IX[mul(h,z)]] for h in stab for z in (g,gi)}))
            assert 0 not in neigh
            classes.setdefault(neigh,v)
        histogram=Counter(len(x) for x in classes)
        result=[]
        for neigh,v in sorted(classes.items(),key=lambda z:z[1]):
            degree=len(neigh)
            if degree<=cap:
                result.append({'id':prefix+str(len(result)),'representative':[offset,offset+v],'degree_vector':[degree,0] if not offset else [0,degree],'root_neighbor_set':[offset+x for x in neigh]})
        return result,dict(sorted(histogram.items()))
    A,Ahist=internal(H,AR,AL,0,3,'A')
    B,Bhist=internal(K,BR,BL,N0,4,'B')
    cross=[];used=set()
    for j,g in enumerate(BR):
        if j in used:continue
        neigh=sorted({BL[IX[mul(h,g)]] for h in H});assert len(neigh)==4
        used.update(neigh)
        cross.append({'id':'C'+str(len(cross)),'representative':[0,N0+j],'degree_vector':[4,3],'root_neighbor_set':[N0+x for x in neigh]})
    assert len(cross)==506 and len(used)==2024
    AA=degree_subsets(A,3);BB=degree_subsets(B,4)
    total=len(AA)*len(BB)*len(cross)
    if total:
        picks=list(range(total)) if total<=1000 else random.Random(20261027354).sample(range(total),1000)
    else:picks=[]
    items=A+B+cross;prep={'group_matrices':G,'matrix_index':IX,'H':H,'K':K,'AR':AR,'BR':BR,'AL':AL,'BL':BL,'perms':perms,'cross':cross,'A_subsets':AA,'B_subsets':BB,'item_by_id':{x['id']:x for x in items},'selection':picks}
    inputs={'group':'PSL(2,23)=SL2(F23)/{+I,-I}','group_order':6072,'canonicalization':'lexicographically smaller of M and -M','torus_generator_order12':r,'H_C4_generators':[power(r,3)],'K_C3_generators':[power(r,4)],'H':H,'K':K,'orbit_sizes':[N0,N1],'n':N,'degree':7,'target_D':5,'comparison_saved_baseline':2810,'permutation_generators':generators,'generated_group_order_verified':len(generated),'internal_A_orbital_degree_histogram':Ahist,'internal_B_orbital_degree_histogram':Bhist,'eligible_internal_A':A,'eligible_internal_B':B,'cross_orbital_count':len(cross),'cross_degree_vector':[4,3],'A_degree3_subsets':AA,'B_degree4_subsets':BB,'full_composition_count':total,'selected_encoded_combinations':picks,'selection_seed':20261027354,'selection_count':len(picks),'scope':'One fixed common order12 torus generator r, H=<r^3>,K=<r^4>; one cross orbital plus internal A degree3 and B degree4; selected unique encoded combinations only','CPU_budget_seconds':90,'workers':1}
    save('inputs.json',inputs)
    if not picks:
        save('terminal.json',{'status':'NO_DEGREE7_ORBITAL_COMPOSITION_FOR_FIXED_STABILIZERS','running':False,'CPU_seconds':time.process_time()-start,'pending':[],'new_graphs':0});return
    cache={};bits=[1<<i for i in range(N)]
    items,choice=choose_items(prep,picks[0]);firstbegan=time.process_time();masks,edges=graph_from(items,cache,perms,bits);val,miss,reach=reachable_score(masks);first_eval_CPU=time.process_time()-firstbegan
    # Independent full edge expansion uses every matrix in G and direct multiplication,
    # rather than the two-generator orbital BFS used by production.
    direct=set()
    def act(g,label):
        if label<N0:return AL[IX[mul(g,AR[label])]]
        return N0+BL[IX[mul(g,BR[label-N0])]]
    for item in items:
        u,v=item['representative']
        for g in G:
            a,b=act(g,u),act(g,v)
            if a>b:a,b=b,a
            direct.add(a*N+b)
    assert direct==set(edges)
    adj=[[] for _ in range(N)]
    for code in direct:
        a,b=divmod(code,N);adj[a].append(b);adj[b].append(a)
    distances=[bfs(adj,r) for r in (0,N0)]
    ordinary=[sum(1<<i for i,x in enumerate(row) if 0<=x<=5) for row in distances]
    assert ordinary==reach and all(len(x)==7 for x in adj)
    save('first_calibration.json',{'formal_evaluation':1,'selected_encoded_combination':picks[0],'choice':choice,'all_explicit_edges_equal_direct_matrix_expansion':True,'all_adjacencies_degree7':True,'ordinary_BFS_roots':2,'ordinary_BFS_distances':distances,'radius5_sets_equal':True,'first_score_reused':val,'root_misses':miss,'initial_production_graph_score_CPU_seconds':first_eval_CPU})
    prep.update({'orbital_edge_cache':cache,'first_score':val,'first_misses':miss,'first_edges':edges,'first_choice':choice})
    save_best(val,miss,edges,choice,1)
    preparation_CPU=time.process_time()-start;prep['preparation_CPU_seconds']=preparation_CPU
    with (D/'prepared.pkl').open('wb') as f:pickle.dump(prep,f)
    save('prepare.json',{'status':'READY_WITH_FIRST_FORMAL_CANDIDATE_CALIBRATED','CPU_seconds':preparation_CPU,'group_order':6072,'internal_A_orbital_degree_histogram':Ahist,'internal_B_orbital_degree_histogram':Bhist,'eligible_A':len(A),'eligible_B':len(B),'A_compositions':len(AA),'B_compositions':len(BB),'cross_orbitals':506,'full_composition_count':total,'fixed_selected_count':len(picks),'first_graph_score_CPU_seconds':first_eval_CPU,'crude_uncached_graph_total_CPU_estimate':preparation_CPU+len(picks)*first_eval_CPU,'first_bad_pairs':val,'first_root_misses':miss,'running':False})
    print((D/'prepare.json').read_text())

def search():
    start=time.process_time()
    with (D/'prepared.pkl').open('rb') as f:prep=pickle.load(f)
    elapsed=prep['preparation_CPU_seconds'];cache=prep['orbital_edge_cache'];bits=[1<<i for i in range(N)]
    best=prep['first_score'];miss=prep['first_misses'];done=1;hit=best==0;timeout=False
    save('run.json',{'running':True,'pid':os.getpid(),'selected_combinations':len(prep['selection']),'completed':1,'preparation_CPU_seconds':elapsed})
    for j,encoded in enumerate(prep['selection'][1:],1):
        if hit:break
        if elapsed+time.process_time()-start>89.5:timeout=True;break
        items,choice=choose_items(prep,encoded);masks,edges=graph_from(items,cache,prep['perms'],bits);value,deficits,reach=reachable_score(masks);done+=1
        if value<best:
            best=value;miss=deficits;save_best(best,miss,edges,choice,done)
        if value==0:hit=True;break
        if done%100==0:save('progress.json',{'completed':done,'best_bad_unordered_pairs':best,'total_CPU_seconds':elapsed+time.process_time()-start,'running':True})
    terminal={'status':'FOUND_D5' if hit else 'CPU_BUDGET_PREFIX_NO_D5' if timeout else 'COMPLETE_SELECTED_ORBITAL_PROFILE_NO_D5','found_D5':hit,'running':False,'fixed_selected_count':len(prep['selection']),'completed_combinations':done,'scope_exhausted':done==len(prep['selection']),'entire_orbit_graph_family_exhausted':False,'first_score_reused':True,'best_bad_unordered_pairs':best,'best_root_misses':miss,'preparation_CPU_seconds':elapsed,'search_CPU_seconds':time.process_time()-start,'total_CPU_seconds':elapsed+time.process_time()-start,'CPU_budget_seconds':90,'workers':1,'restarts':0,'pending':['root-independent-final-check'],'new_BFS_roots_calibration':2,'next_encoded_combination':prep['selection'][done] if done<len(prep['selection']) else None}
    save('terminal.json',terminal);save('run.json',terminal);print(json.dumps(terminal))

if __name__=='__main__':
    if sys.argv[1]=='prepare':prepare()
    elif sys.argv[1]=='search':search()
