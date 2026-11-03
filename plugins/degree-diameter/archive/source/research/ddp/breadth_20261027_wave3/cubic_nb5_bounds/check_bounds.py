"""Small exact arithmetic and forced local-walk evidence; no graph search."""
from collections import Counter, deque
from pathlib import Path
import json
import time

P=Path(__file__).resolve().parent
assert not (P/'terminal.json').exists(), 'Completed evidence exists; do not restart.'
started=time.process_time()

def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]: a.pop()
    return a
def subtract(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]-=v
    return trim(c)
N=[[1],[0,1],[-3,0,1]]
for k in range(3,6): N.append(subtract([0]+N[-1],[2*v for v in N[-2]]))
assert N[4]==[6,0,-7,0,1] and N[5]==[0,16,0,-9,0,1]
assert sum(v*3**i for i,v in enumerate(N[4]))==24
assert sum(v*3**i for i,v in enumerate(N[5]))==48

prime=7
def canon(a): return trim([x%prime for x in a])
def remainder(a,b):
    a=canon(a);b=canon(b)
    while a!=[0] and len(a)>=len(b):
        shift=len(a)-len(b)
        scale=a[-1]*pow(b[-1],prime-2,prime)%prime
        for j,v in enumerate(b): a[j+shift]=(a[j+shift]-scale*v)%prime
        a=canon(a)
    return a
def multiply(a,b,modulus):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return remainder(c,modulus)
def power(a,n,modulus):
    result=[1]
    while n:
        if n&1: result=multiply(result,a,modulus)
        a=multiply(a,a,modulus);n//=2
    return result
def gcd(a,b):
    a=canon(a);b=canon(b)
    while b!=[0]:a,b=b,remainder(a,b)
    inv=pow(a[-1],prime-2,prime)
    return canon([inv*x for x in a])
h5=[5,2,0,5,0,1]  # x^5-9*x^3+16*x-2 modulo7, low coefficient first.
r=[0,1];powers=[]
for j in range(1,6):
    r=power(r,7,h5);powers.append(dict(frobenius_power=j,remainder=r))
linear_difference=subtract(powers[0]['remainder'],[0,1])
linear_gcd=gcd(h5,linear_difference)
assert powers[-1]['remainder']==[0,1] and linear_gcd==[1]
rabin=dict(prime=7,polynomial_low_first=h5,frobenius_remainders=powers,
           gcd_with_x7_minus_x=linear_gcd,x_7_power5_congruent_x=True,
           conclusion='Degree5 is prime. Divisibility into x^(7^5)-x and no linear factor imply irreducibility overF7, hence overQ.')

def cycle(k):return k,[(i,(i+1)%k) for i in range(k)]
def theta(lengths):
    edges=[];fresh=2
    for length in lengths:
        route=[0]+list(range(fresh,fresh+length-1))+[1]
        fresh+=length-1;edges.extend(zip(route,route[1:]))
    return fresh,edges
def local_supports(n,edges,length=5):
    records=[]
    for root in range(n):
        adj=[set() for _ in range(n)]
        for u,v in edges:adj[u].add(v);adj[v].add(u)
        assert max(map(len,adj))<=3
        distance=[-1]*n;distance[root]=0;q=deque([root])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if distance[v]<0:distance[v]=distance[u]+1;q.append(v)
        q=deque(i for i in range(n) if distance[i]<length)
        while q:
            u=q.popleft()
            while len(adj[u])<3:
                v=len(adj);adj.append({u});adj[u].add(v)
                distance.append(distance[u]+1)
                if distance[v]<length:q.append(v)
        endpoints=Counter()
        def walk(previous,current,steps):
            if steps==length:endpoints[current]+=1;return
            for v in adj[current]:
                if v!=previous:walk(current,v,steps+1)
        walk(-1,root,0)
        assert sum(endpoints.values())==3*2**(length-1)
        records.append(dict(root=root,distinct_exact_NB_endpoints=len(endpoints),
                            diagonal_multiplicity=endpoints.get(root,0)))
    return records
cores=[('C3',cycle(3)),('C4',cycle(4)),('C5',cycle(5)),
       ('theta_1_4_4',theta([1,4,4])),('theta_2_3_3',theta([2,3,3])),
       ('theta_3_2_2',theta([3,2,2])),('triangle_C5_shared_edge',theta([1,2,4])),
       ('triangle_C5_shared_path2',theta([1,2,3])),('diamond',theta([1,2,2])),
       ('two_triangles_bridge',(6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3)]))]
local=[]
for name,(n,edges) in cores:
    records=local_supports(n,edges)
    local.append(dict(core=name,vertices=n,edges=edges,length=5,
                      best_root_order_upper_bound=min(x['distinct_exact_NB_endpoints'] for x in records),
                      root_records=records))
assert [x['best_root_order_upper_bound'] for x in local]==[46,43,47,45,44,41,39,35,29,42]
four=local_supports(*cycle(4),length=4)
assert all(x['distinct_exact_NB_endpoints']==21 for x in four)
data=dict(status='COMPLETE_SMALL_ARITHMETIC_AND_FORCED_CORE_CHECKS',
          NB_polynomial_coefficients_low_first=N,
          NB4_row_sum=24,NB5_row_sum=48,
          quartic_x4_minus7x2_plus4=dict(rational_root_values={'1':-2,'2':-8,'4':148},
             quadratic_factor_cases='a=0 requires integers b+d=-7,bd=4, impossible; b=d=+/-2 requires a^2=11 or3, impossible.'),
          quintic_irreducibility=rabin,local_NB5_core_bounds=local,local_C4_NB4=four,
          nb4_general_controller_order_upper_bound=20,
          nb5_general_controller_order_upper_bound=44,
          nb5_orders_above_threshold_still_open=[42,44],
          random_graph_searches=0,large_graphs_generated=0,
          CPU_seconds=time.process_time()-started)
(P/'RESULTS.json').write_text(json.dumps(data,indent=2)+'\n')
terminal=dict(status='COMPLETE_NB4_STOP_NB5_42_44_OPEN',running=False,
              nb4_22_excluded=True,nb5_48_excluded=True,nb5_46_excluded=True,
              nb5_42_excluded=False,nb5_44_excluded=False,
              claimed_nb5_order_at_most40=False,
              CPU_seconds=time.process_time()-started,random_graph_searches=0,
              large_graphs_generated=0,restarts=0,pending=[],
              evidence_level='Self-contained rational-spectrum argument plus finite field arithmetic and small forced-core endpoint enumeration; not Lean or cross-family certification.')
(P/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal))
