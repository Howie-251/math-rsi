"""One fixed quad configuration for each one-J inventory; stop at first nonpositive D."""
from itertools import combinations,combinations_with_replacement,permutations
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent
P=127;triples=[x for x in range(128) if x.bit_count()==3];pairs=[x for x in range(128) if x.bit_count()==2]
def move(mask,p):return sum(1<<p[i] for i in range(7) if mask&(1<<i))
def canonical(quads,internal):
    group=[p for p in permutations(range(7)) if sorted(move(T,p) for T in internal)==sorted(internal)]
    return min(tuple(sorted(move(T,p) for T in quads)) for p in group),len(group)
specs=[dict(I=1,internal=[31],quads=[15,51,92,106],n3=2),
       dict(I=2,internal=[124,115],quads=[51,92],n3=3)]
results=[];start=time.process_time();failed=False
for spec in specs:
    quads,order=canonical(spec['quads'],spec['internal']);internal=spec['internal']
    c=[sum(T>>v&1 for T in internal) for v in range(7)]
    b=[sum(T>>v&1 for T in quads) for v in range(7)]
    raw=necessary=0;minimum=10**9;worstbest=0;first=None
    for Ts in combinations_with_replacement(triples,spec['n3']):
        a=[sum(T>>v&1 for T in Ts) for v in range(7)]
        if any(2*a[v]+3*b[v]>15-4*c[v] for v in range(7)):continue
        high=Ts+quads;distinct=set(high)
        cover0=internal+list(high)
        for J in pairs:
            raw+=1;s=[J>>v&1 for v in range(7)]
            u=[8-c[v]-a[v]-b[v]-s[v] for v in range(7)]
            if min(u)<0 or any(s[v]+2*a[v]+3*b[v]>15-4*c[v] for v in range(7)):continue
            if any(not any(pair&T==pair for T in cover0+[J]) for pair in pairs):continue
            assert sum(u)==27
            necessary+=1;W=M=0;best=99;bestQ=None;witnesses=[]
            for Q in triples:
                if Q in distinct or Q&J==J:continue
                m=sum(u[v] for v in range(7) if Q>>v&1);t=int(not Q&J)
                weight=max(0,12-m-t);miss=sum(not Q&T for T in distinct)
                W+=weight;M+=weight*miss
                if not miss:
                    score=m+t
                    if score<best:best=score;bestQ=Q
                    if score<=11:witnesses.append(dict(Q=Q,P4=m,T3=t,B4=27-m))
            D=W-M
            if D<=0 or best>11:
                first=dict(internal=internal,quads=quads,triples=Ts,J=J,c=c,a=a,b=b,u=u,
                           W=W,M=M,D=D,minimum_proper_m_plus_t=best,best_Q=bestQ,
                           all_gate_compatible_Q=witnesses)
                failed=True;break
            minimum=min(minimum,D);worstbest=max(worstbest,best)
        if failed:break
    results.append(dict(I=spec['I'],fixed_quad_masks=quads,stabilizer_order=order,
                        pair_iterations_after_high_degree_prescreen=raw,necessary=necessary,
                        complete_this_fixed_position=not failed,minimum_D_on_accepted=minimum,
                        worst_best_m_plus_t_on_accepted=worstbest,failure=first))
    if failed:break
result=dict(scope=__doc__,full_quad_orbit_domain_completed=False,rows=results,cpu_seconds=time.process_time()-start)
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
