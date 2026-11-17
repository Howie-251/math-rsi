"""One fixed geometry; one <=15s matching feasibility call; no Hamilton search."""
import json
import time
from pathlib import Path
from ortools.sat.python import cp_model

ROOT=Path(__file__).resolve().parent
O={31,47,55,59,61}
E={5,9,18}
ANCHORS={0,3}
def short(a,b): return (a^b).bit_count()==1
def direction(a,b): return (a^b).bit_length()-1
def canon(a,b): return sorted((a,b))

def main():
    V=set(range(64))-O-E-ANCHORS
    edges=[(u,u^(1<<k)) for u in sorted(V) for k in range(6) if (u^(1<<k)) in V and u<(u^(1<<k))]
    model=cp_model.CpModel()
    x=[model.new_bool_var(f'e{u}_{v}') for u,v in edges]
    for u in sorted(V): model.add(sum(x[i] for i,e in enumerate(edges) if u in e)==1)
    for k in range(6): model.add(sum(x[i] for i,e in enumerate(edges) if direction(*e)==k)>=2)
    solver=cp_model.CpSolver()
    solver.parameters.num_search_workers=1
    solver.parameters.random_seed=0
    solver.parameters.max_time_in_seconds=15
    started=time.monotonic(); status=solver.solve(model)
    out=dict(caller='/root',gap='R7-2X-SAME',geometry_count=1,solver_calls=1,
             constraints='vertex degree exactly one; six directional counts at least two',
             solver='OR-Tools CP-SAT',version=__import__('ortools').__version__,
             seed=0,workers=1,solver_limit_seconds=15,solver_status=solver.status_name(status),
             solver_elapsed_seconds=time.monotonic()-started,
             no_Hamilton_constraints=True,no_matching_family_enumeration=True)
    if status not in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        out['interpretation']='Fixed geometry infeasible' if status==cp_model.INFEASIBLE else 'UNKNOWN; stop without changing input'
    else:
        B=sorted([list(e) for i,e in enumerate(edges) if solver.value(x[i])])
        A=sorted(canon(u^3,v^3) for u,v in B)
        faces={}
        gates=[]
        for name,M in [('A',A),('B',B)]:
            covered=[u for e in M for u in e]
            assert len(covered)==54 and len(set(covered))==54 and all(short(*e) for e in M)
            free=set(range(64))-set(covered)
            H=free-ANCHORS
            odd={u for u in H if u.bit_count()%2}
            even=H-odd
            counts=[sum(direction(*e)==k for e in M) for k in range(6)]
            assert len(odd)==5 and len(even)==3 and min(counts)>=2
            neighbor_edges=[canon(d,o) for d in ANCHORS for o in odd if short(d,o)]
            assert not neighbor_edges
            faces[name]=dict(edges=M,O=sorted(odd),E=sorted(even),internal_free=sorted(free),
                             direction_counts=counts,f=5,anchor_to_O_edges=neighbor_edges)
            for d in sorted(ANCHORS):
                for k in range(6):
                    OX={u for u in odd if (u>>k&1)!=(d>>k&1)}
                    EX={u for u in even if (u>>k&1)!=(d>>k&1)}
                    EY=even-EX; delta=len(OX)-len(EX)
                    gates.append(dict(response=name,d=d,k=k,delta=delta,EY=sorted(EY),
                                      original_cross_edges=counts[k],M_pass=delta in (0,1),
                                      candidate_N_pass=delta==2 and bool(EY) and counts[k]>=3))
        assert set(faces['B']['O'])==O and set(faces['B']['E'])==E
        global_edges=sorted(A+[[u+64,v+64] for u,v in B]+[[0,64],[3,67]])
        covered=[u for e in global_edges for u in e]
        assert len(global_edges)==56 and len(covered)==len(set(covered))==112
        holes=sorted(set(range(128))-set(covered))
        hole_edges=[canon(u,v) for u in holes for v in holes if u<v and short(u,v)]
        counts=[sum(direction(*e)==k for e in global_edges) for k in range(7)]
        assert not hole_edges and counts[6]==2 and min(counts[:6])>=4
        assert set(faces['A']['internal_free'])&set(faces['B']['internal_free'])==ANCHORS
        expected={('B',0):[3,3,3,3,3,4],('B',3):[-1,-1,3,3,3,4],
                  ('A',0):[-1,-1,3,3,3,4],('A',3):[3,3,3,3,3,4]}
        for (name,d),want in expected.items():
            assert [g['delta'] for g in gates if g['response']==name and g['d']==d]==want
        assert all(g['delta'] not in (0,1,2) for g in gates)
        out.update(status='FIXED_ODD_MARGIN_JOINT_RESIDUAL_VERIFIED',faces=faces,edges=global_edges,
                   edge_count=56,direction_counts=counts,m=2,two_edge_directions=[6],holes=holes,
                   even_holes=[v for v in holes if v.bit_count()%2==0],
                   odd_holes=[v for v in holes if v.bit_count()%2],hole_edges=hole_edges,
                   inclusion_maximal=True,common_local_internal_free=[0,3],margin_gates=gates,
                   all_24_delta_avoid_012=True,
                   scope='Joint residual of listed sufficient rules and proposed N; not an R7 counterexample')
    path=ROOT/'R7_ODD_MARGIN_RESIDUAL_WITNESS.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('solver_status','solver_elapsed_seconds')}))
    if 'direction_counts' in out: print(out['direction_counts'])

if __name__=='__main__': main()
