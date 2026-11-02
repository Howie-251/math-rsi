"""Two frozen GF9 module controls; do not execute the old source constructor."""
from collections import Counter, deque
from datetime import datetime, timezone
from pathlib import Path
import json
import time

OUT = Path(__file__).resolve().parent
import resource
resource.setrlimit(resource.RLIMIT_CPU,(15,16))
start=time.process_time()
add=[[((a%3+b%3)%3)+3*((a//3+b//3)%3) for b in range(9)] for a in range(9)]
mul=[[((a%3*(b%3)+2*(a//3)*(b//3))%3)+3*((a%3*(b//3)+(a//3)*(b%3))%3) for b in range(9)] for a in range(9)]
neg=[next(b for b in range(9) if add[a][b]==0) for a in range(9)]
def mm(A,B):
    return tuple(add[mul[A[2*i]][B[j]]][mul[A[2*i+1]][B[2+j]]] for i in range(2) for j in range(2))
def mv(A,v):
    x,y=v%9,v//9
    return add[mul[A[0]][x]][mul[A[1]][y]]+9*add[mul[A[2]][x]][mul[A[3]][y]]
def vn(v): return neg[v%9]+9*neg[v//9]
def hm(h,k):
    u,v=h%3,h//3; a,b=k%3,k//3
    return (u+(-a if v%2 else a))%3+3*((v+b)%8)
I=(1,0,0,1); beta=(0,2,1,2); K=(1,2,0,2)
vadd=[[add[a%9][b%9]+9*add[a//9][b//9] for b in range(81)] for a in range(81)]
chi=[pow(2,j,5) for j in range(8)]
reports=[]
for scalar,vb in [(s,v) for s in [4,8] for v in range(81) if v!=19]:
    case_start=time.process_time(); case=OUT/f'scalar{scalar}_B{vb}';case.mkdir(exist_ok=True)
    alpha=tuple(mul[scalar][x] for x in K)
    ap=[I];bp=[I]
    for _ in range(8):ap.append(mm(ap[-1],alpha))
    for _ in range(3):bp.append(mm(bp[-1],beta))
    assert ap[8]==bp[3]==I and mm(alpha,beta)==mm(bp[2],alpha)
    rho=[mm(bp[u],ap[v]) for v in range(8) for u in range(3)]
    if vb==0: assert all(mm(rho[h],rho[k])==rho[hm(h,k)] for h in range(24) for k in range(24))
    def gm(g,k):
        nv,q=g%81,g//81; z,h=q%5,q//5
        nw,r=k%81,k//81; zz,hh=r%5,r//5
        return vadd[nv][mv(rho[h],nw)]+81*((z+chi[h//3]*zz)%5+5*hm(h,hh))
    def gi(g):
        nv,q=g%81,g//81;z,h=q%5,q//5;u,v=h%3,h//3
        hi=(-(-1 if v%2 else 1)*u)%3+3*((-v)%8)
        return vn(mv(rho[hi],nv))+81*((-chi[hi//3]*z)%5+5*hi)
    def enc(x,y,z,u,v):return x+9*y+81*(z+5*(u+3*v))
    E=0; A=enc(0,1,1,1,4); B=enc(vb%9,vb//9,4,1,7)
    Y=enc(0,0,0,0,1); D=enc(0,2,4,1,4)
    volts=[E,A,gi(A),B,gi(B),Y,gi(Y),D,gi(D)]
    assert all(gm(g,gi(g))==gm(gi(g),g)==0 for g in volts)
    ports=[[(1,0),(1,1),(1,3),(0,5),(0,6)],[(0,0),(0,2),(0,4),(1,7),(1,8)]]
    group_n=9720; n=19440
    qnext=[]
    for q in range(120):
        z,h=q%5,q//5;row=[]
        for d in volts:
            r=d//81;zz,hh=r%5,r//5
            row.append((z+chi[h//3]*zz)%5+5*hm(h,hh))
        qnext.append(row)
    shifts=[[mv(rho[h],d%81) for d in volts] for h in range(24)]
    graph=[]
    for node in range(n):
        base,g=divmod(node,group_n);nv=g%81;q=g//81;h=q//5
        row=[target*group_n+vadd[nv][shifts[h][j]]+81*qnext[q][j] for target,j in ports[base]]
        if vb==0: assert len(set(row))==5 and node not in row
        graph.append(row)
    if vb==0: assert all(u in graph[v] for u,row in enumerate(graph) for v in row)
    roots=[]
    for root in [0,group_n]:
        dist=[-1]*n;dist[root]=0;queue=deque([root])
        while queue:
            u=queue.popleft()
            for v in graph[u]:
                if dist[v]<0:dist[v]=dist[u]+1;queue.append(v)
        reached=sum(x>=0 for x in dist)
        roots.append(dict(root=root,visited=reached,eccentricity=max(dist),
            R8_missing=sum(x<0 or x>8 for x in dist),distance_histogram=dict(sorted(Counter(dist).items()))))
    connected=all(x['visited']==n for x in roots)
    diameter=max(x['eccentricity'] for x in roots) if connected else None
    hit=connected and diameter<=8
    result=dict(status='POSITIVE_REQUIRES_INDEPENDENT_ACCEPTANCE' if hit else 'FIXED_CONTROL_FAILED',
        n=n,m=48600,degree=5,simple=True,undirected=True,connected=connected,
        scalar=scalar,B_vector=[vb%9,vb//9],B_vector_id=vb,B_fixed_by_beta=(mv(beta,vb)==vb),B_H_orbit_representative=min(mv(R,vb) for R in rho),B_H_orbit_size=len(set(mv(R,vb) for R in rho)),alpha=list(alpha),beta=list(beta),voltage_ids=volts,
        roots=roots,actual_global_D=diameter,ordinary_bad_unordered_pairs=None,
        acceptance_argument='Left deck group action has exactly the two base fibers as orbits. One representative of each was fully BFS checked.',
        accepted_D8=hit,source_D7_BFS_repeated=0,CPU_seconds=time.process_time()-case_start)
    if hit:
        p=case/'graph_d5_D8_n19440.edges'
        with p.open('w') as f:
            f.write(f'{n} 48600\n');count=0
            for u,row in enumerate(graph):
                for v in sorted(row):
                    if u<v:f.write(f'{u} {v}\n');count+=1
        assert count==48600
        result['graph_file']=str(p)
    (case/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');reports.append(result)
    (OUT/'checkpoint.json').write_text(json.dumps(dict(status='RUNNING',completed=len(reports),cursor=[scalar,vb],CPU_seconds=time.process_time()-start))+'\n')
    if hit: print(json.dumps(result))
    if hit:break
result=dict(status='HIT_REQUIRES_INDEPENDENT_ACCEPTANCE' if any(x['accepted_D8'] for x in reports) else 'COMPLETE_FREE_B_FAMILY_NO_HIT',
    controls=reports,untried_new_cases=160-len(reports),inherited_old_controls=2,CPU_seconds=time.process_time()-start,new_lower_bound_claimed=False)
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(dict(running=False,status=result['status'],pending=[]),indent=2)+'\n')

print(json.dumps({k:v for k,v in result.items() if k!="controls"}))
