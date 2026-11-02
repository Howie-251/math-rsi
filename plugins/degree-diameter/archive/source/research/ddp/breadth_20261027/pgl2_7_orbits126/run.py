from pathlib import Path
from collections import deque
import json, time

OUT=Path(__file__).resolve().parent
START=time.process_time()
BUDGET=90.0
def save(name,data):
    (OUT/name).write_text(json.dumps(data,indent=2)+'\n')
def canonical(z):
    x=next(a for a in z if a)
    inv=pow(x,-1,7)
    return tuple(a*inv%7 for a in z)
I=(1,0,0,1)
G=sorted({canonical((a,b,c,d)) for a in range(7) for b in range(7) for c in range(7) for d in range(7) if (a*d-b*c)%7})
G.remove(I);G.insert(0,I)
INDEX={g:i for i,g in enumerate(G)}
assert len(G)==336
def matmul(x,y):
    a,b,c,d=x;e,f,g,h=y
    return canonical(((a*e+b*g)%7,(a*f+b*h)%7,(c*e+d*g)%7,(c*f+d*h)%7))
M=[[INDEX[matmul(a,b)] for b in G] for a in G]
INV=[row.index(0) for row in M]
def subgroup(gens):
    seen={0};todo=[0]
    while todo:
        x=todo.pop()
        for a in gens:
            y=M[x][a]
            if y not in seen:seen.add(y);todo.append(y)
    return sorted(seen)
def order(x):
    y=x;k=1
    while y:
        y=M[y][x];k+=1
    return k
r=next(x for x in range(1,336) if order(x)==4)
t=next(x for x in range(1,336) if x not in subgroup([r]) and M[x][x]==0 and M[M[x][r]][INV[x]]==INV[r])
H=subgroup([r,t]);K=subgroup([r])
assert len(H)==8 and len(K)==4
def cosets(H):
    remaining=set(range(336));reps=[];lookup=[-1]*336;sets=[]
    while remaining:
        a=min(remaining);C={M[a][h] for h in H};j=len(reps)
        for b in C:lookup[b]=j
        remaining-=C;reps.append(a);sets.append(sorted(C))
    assert all(x>=0 for x in lookup)
    return reps,lookup,sets
HR,HL,HC=cosets(H);KR,KL,KC=cosets(K)
assert len(HR)==42 and len(KR)==84
PERMS=[[HL[M[a][x]] for x in HR]+[42+KL[M[a][x]] for x in KR] for a in range(336)]
assert all(sorted(p)==list(range(126)) for p in PERMS)
remaining={(a,b) for a in range(126) for b in range(a+1,126)}
orbitals=[]
while remaining:
    u,v=min(remaining)
    E=sorted({tuple(sorted((p[u],p[v]))) for p in PERMS})
    assert all(a!=b for a,b in E) and set(E)<=remaining
    remaining-=set(E)
    deg=[0]*126
    for a,b in E:deg[a]+=1;deg[b]+=1
    assert len(set(deg[:42]))==1 and len(set(deg[42:]))==1
    orbitals.append({'id':len(orbitals),'representative':[u,v],'edges':E,'degrees':[deg[0],deg[42]]})
eligible=[x for x in orbitals if max(x['degrees'])<=6]
for x in eligible:
    masks=[0]*126
    for a,b in x['edges']:masks[a]|=1<<b;masks[b]|=1<<a
    x['adj_masks']=masks
save('inputs.json',{'group':'PGL(2,7), matrices modulo nonzero scalar','canonicalization':'first nonzero matrix entry is 1','matrices':G,'identity_index':0,'H_generators':[r,t],'K_generators':[r],'H_generator_matrices':[G[r],G[t]],'K_generator_matrices':[G[r]],'H':H,'K':K,'H_order':8,'K_order':4,'orbit_sizes':[42,84],'roots':[0,42],'vertex_labels':'0..41 left cosets gH,42..125 left cosets gK','H_coset_representatives':HR,'K_coset_representatives':KR,'all_orbital_count':len(orbitals),'eligible_orbitals':[{k:v for k,v in x.items() if k!='adj_masks'} for x in eligible],'scope':'All subsets of the saved eligible unordered-pair orbitals whose degree vector is exactly (6,6), for these one fixed H and K','CPU_budget_seconds':BUDGET,'workers':1})
counts={'degree6_subsets_scored':0,'DFS_nodes':0,'first_calibration_BFS_roots':0,'best_diagnostic_BFS_roots':0,'new_full_graphs_saved':0}
best=None;hit=False;timedout=False
def bfs(adj,root):
    dist=[-1]*126;dist[root]=0;todo=deque([root])
    while todo:
        u=todo.popleft()
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;todo.append(v)
    return dist
def score(masks):
    misses=[];reachmasks=[]
    for root in (0,42):
        seen=1<<root;front=seen
        for depth in range(3):
            nxt=0
            while front:
                b=front & -front;front-=b;nxt|=masks[b.bit_length()-1]
            front=nxt & ~seen;seen|=front
        misses.append(126-seen.bit_count());reachmasks.append(seen)
    return (42*misses[0]+84*misses[1])//2,misses,reachmasks
def evaluate(chosen,masks):
    global best,hit
    value,misses,reach=score(masks)
    counts['degree6_subsets_scored']+=1
    if counts['degree6_subsets_scored']==1:
        # Independent first formal graph expansion uses the saved orbit representatives
        # and direct matrix multiplication/coset lookup, rather than search masks.
        E=set()
        for i in chosen:
            u,v=eligible[i]['representative']
            for a in range(336):
                def act(label):
                    if label<42:return HL[INDEX[matmul(G[a],G[HR[label]])]]
                    return 42+KL[INDEX[matmul(G[a],G[KR[label-42]])]]
                x,y=act(u),act(v);E.add(tuple(sorted((x,y))))
        adj=[set() for _ in range(126)]
        for u,v in E:adj[u].add(v);adj[v].add(u)
        assert len(E)==378 and all(len(x)==6 for x in adj)
        D=[bfs(adj,r) for r in (0,42)]
        independent=[sum(1<<v for v,d in enumerate(row) if 0<=d<=3) for row in D]
        assert independent==reach
        counts['first_calibration_BFS_roots']=2
        save('first_calibration.json',{'selected_orbitals':[eligible[i]['id'] for i in chosen],'edges':len(E),'degrees':[len(x) for x in adj],'radius3_masks_equal':True,'ordinary_BFS_distances':D,'first_score_reused':value,'new_BFS_roots':2})
    if best is None or value<best['bad_unordered_pairs']:
        E=sorted({tuple(e) for i in chosen for e in eligible[i]['edges']})
        adj=[[] for _ in range(126)]
        for u,v in E:adj[u].append(v);adj[v].append(u)
        # Full distances from the two proven orbit representatives diagnose the saved
        # candidate only; root owns the eventual independent all-126-root check.
        D=[bfs(adj,r) for r in (0,42)]
        counts['best_diagnostic_BFS_roots']+=2
        diameter=max(map(max,D)) if all(min(row)>=0 for row in D) else None
        best={'n':126,'edges':len(E),'minimum_degree':6,'maximum_degree':6,'target_D':3,'diameter_from_two_proven_orbit_roots':diameter,'connected':diameter is not None,'bad_unordered_pairs':value,'root_misses':misses,'selected_orbitals':[eligible[i]['id'] for i in chosen],'evaluation':counts['degree6_subsets_scored']}
        save('best.json',best)
        (OUT/'best.edges').write_text('126 378\n'+''.join(f'{u} {v}\n' for u,v in E))
        counts['new_full_graphs_saved']+=1
    if value==0:hit=True
def dfs(pos,d0,d1,chosen,masks):
    global timedout
    counts['DFS_nodes']+=1
    if hit:return
    if counts['DFS_nodes']%256==0 and time.process_time()-START>BUDGET-0.5:
        timedout=True;return
    if d0==6 and d1==6:
        evaluate(chosen,masks);return
    if pos==len(eligible) or timedout:return
    x=eligible[pos];a,b=x['degrees']
    if d0+a<=6 and d1+b<=6:
        dfs(pos+1,d0+a,d1+b,chosen+[pos],[u|v for u,v in zip(masks,x['adj_masks'])])
    if not hit and not timedout:dfs(pos+1,d0,d1,chosen,masks)
dfs(0,0,0,[],[0]*126)
cpu=time.process_time()-START
save('terminal.json',{'status':'FOUND_TARGET_D3' if hit else 'PARTIAL_CPU_BUDGET_NO_D3' if timedout else 'COMPLETE_FIXED_H8_K4_ORBITAL_SUBSETS_NO_D3','running':False,'scope_exhausted':not timedout and not hit,'entire_PGL_family_exhausted':False,'CPU_seconds':cpu,'CPU_budget_seconds':BUDGET,'workers':1,'restarts':0,**counts,'all_orbital_count':len(orbitals),'eligible_orbital_count':len(eligible),'found_D3':hit,'best':best,'pending':['root-independent-final-check'] if best else []})
print(json.dumps({'CPU_seconds':cpu,'all_orbitals':len(orbitals),'eligible_orbitals':len(eligible),**counts,'best':best,'hit':hit,'timedout':timedout}))
