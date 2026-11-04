"""Attempt a fixed-extension obstruction. Failure is not a mathematical counterexample."""
import json,itertools
from pathlib import Path
from single_bridge_probe import solve
from four_hole_surgery import edge,edges,repair
ROOT=Path(__file__).resolve().parent
u,z,w,t,x,v=0,3,61,62,57,59
# Fixed complementary matching; switched squares are chosen to block geodesic connectors.
complement={edge(a,a^2) for a in range(64) if not a&2}
complement-={edge(x,v),edge(16,18),edge(17,19),edge(32,34),edge(33,35),edge(8,10),edge(12,14)}
complement|={edge(16,17),edge(18,19),edge(32,33),edge(34,35),edge(8,12),edge(10,14)}
assert len(complement)==31
artificial={edge(u,w),edge(z,t)}
mandatory=sorted(complement|artificial|{edge(8,10),edge(16,18)})
result=solve(6,mandatory,x,v,5,seconds=20,allowed_long=artificial)
if result['status']!='FOUND':
    attempt={'status':'NO_COUNTEREXAMPLE_ESTABLISHED','solver_result':result,
             'parameters':{'u':u,'z':z,'w':w,'t':t,'x':x,'v':v},
             'complement_matching':sorted(complement),'mandatory_edges':mandatory,
             'meaning':'This fixed complementary matching produced no Hamilton intermediate witness; solver status is not an independently certified impossibility proof.'}
    (ROOT/'fixed_extension_obstruction_attempt.json').write_text(json.dumps(attempt,indent=2),encoding='utf8')
    print(json.dumps({'status':attempt['status'],'solver_result':result}))
    raise SystemExit(0)
kpath=result['path'];ke=edges(kpath)
p=ke-complement
m=sorted(p-artificial)
assert len(m)==30 and len({a^b for a,b in m})==6
assert {a for e in m for a in e}==set(range(64))-{u,z,w,t}
assert len([a for e in m for a in e])==len({a for e in m for a in e})
nm={a:b for e in complement for a,b in (e,e[::-1])}

def alternating_connectors(max_cuts):
    forbidden={u,w,x,v}
    def rec(path,remaining):
        current=path[-1]
        if remaining==0:
            if (current^t).bit_count()==1 and edge(current,t) not in ke:
                yield tuple(path+[t])
            return
        for bit in range(6):
            a=current^(1<<bit)
            if a in forbidden or a in path or a==t or a not in nm:continue
            if edge(current,a) in ke:continue
            b=nm[a]
            if b in forbidden or b in path or b==t:continue
            yield from rec(path+[a,b],remaining-1)
    for count in range(1,max_cuts+1):yield from rec([z],count)

fixed=repair(kpath,m,u,z,w,t,x,v,alternating_connectors(5))
assert fixed is not None
assert fixed['extra_cuts']>=3
geodesic_cut_pairs=0
for target in (w,t):
    bits=[1<<i for i in range(6) if (z^target)&(1<<i)]
    assert len(bits)==5
    for order in itertools.permutations(bits):
        route=[z]
        for bit in order:route.append(route[-1]^bit)
        geodesic_cut_pairs+=all(edge(route[i],route[i+1]) in complement for i in (1,3))
assert geodesic_cut_pairs==0
certificate={'n':6,'u':u,'z':z,'w':w,'t':t,'x':x,'v':v,'matching':m,
             'intermediate_path':kpath,'complement_matching':sorted(complement),
             'artificial_edges':sorted(artificial),'proved_extra_cut_lower_bound':3,
             'reason':'Exhaustive coordinate-permutation check found no geodesic connector with both cut edges in the fixed complementary matching.',
             **fixed}
(ROOT/'fixed_extension_obstruction.json').write_text(json.dumps(certificate,indent=2),encoding='utf8')
print(json.dumps({'status':'FOUND','matching_directions':len({a^b for a,b in m}),
                  'proved_lower_bound':3,'actual_extra_cuts':fixed['extra_cuts'],
                  'connector':fixed['connector']}))
