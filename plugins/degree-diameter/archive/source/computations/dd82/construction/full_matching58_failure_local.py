"""Read-only graph diagnosis: block routes and common coordinate centralizer.

No new graph is proposed, no optimization is performed, and no BFS is run.
"""
from itertools import permutations
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"computations/dd82/construction/full_matching58_anneal_run"


def main():
    cpu,wall=time.process_time(),time.monotonic()
    rows=[list(map(int,line.split())) for line in (OUT/"candidate.best.edges").read_text().splitlines()]
    assert rows[0]==[58,232]
    adj=[set() for _ in range(58)]
    for u,v in rows[1:]:adj[u].add(v);adj[v].add(u)
    q={}
    for i in range(8):
        for j in range(8):
            if i==j:continue
            image=[]
            for a in range(6):
                neighbours=adj[10+6*i+a]&set(range(10+6*j,16+6*j))
                assert len(neighbours)==1
                image.append(next(iter(neighbours))-(10+6*j))
            assert sorted(image)==list(range(6))
            q[i,j]=tuple(image)
    S=[[0]*6 for _ in range(6)];composites=[]
    for k in range(8):
        if k in (1,6):continue
        image=[q[k,6][q[1,k][a]] for a in range(6)]
        composites.append(dict(intermediate_fibre=k,permutation=image))
        for a,b in enumerate(image):S[a][b]+=1
    K=[row[:] for row in S]
    for a,b in enumerate(q[1,6]):K[a][b]+=1
    assert S==[[6*int(a==b) for b in range(6)] for a in range(6)]
    assert all(q[1,6][a]!=a for a in range(6))
    block=dict(fibre_pair=[1,6],Q16=q[1,6],S=S,K=K,
        rows=[dict(coordinate=a,S_values=S[a],S_support=[b for b in range(6) if S[a][b]],
                   S_support_count=sum(v>0 for v in S[a]),K_values=K[a],
                   K_support=[b for b in range(6) if K[a][b]],K_support_count=sum(v>0 for v in K[a]))
              for a in range(6)],
        two_step_composites=composites,
        replacement_formula="For any replacement M of Q16 alone, K=6I+M and bad_block=24+number_of_fixed_points(M)",
        replacement_lower_bound=24,
        scope="All other 27 interfaces fixed to this actual candidate; no exclusion of the general family")

    free=[q[i,j] for i in range(1,8) for j in range(i+1,8)]
    is_matching=lambda p: all(p[a]!=a and p[p[a]]==a for a in range(6))
    matching_entries=[p for p in free if is_matching(p)]
    all_perms=list(permutations(range(6)))
    matching_catalog={p for p in all_perms if is_matching(p)}
    # The actual duplicate routing and the observed complete fifteen-element
    # matching palette motivate this symmetry diagnosis. It is not a graph search.
    assert len(matching_entries)==20 and set(matching_entries)==matching_catalog
    assert len(matching_catalog)==15
    centralizer=[p for p in all_perms
                 if all(all(p[qv[a]]==qv[p[a]] for a in range(6)) for qv in free)]
    assert centralizer==[tuple(range(6))]
    symmetry=dict(reason="Twenty of the twenty-one actual free interfaces are fixed-point-free involutions, and their distinct values are all fifteen perfect matchings on six coordinates; S=6I also exposes repeated boundary channels",
        free_interfaces_checked=21,coordinate_permutations_checked=720,
        perfect_matching_interface_entries=20,distinct_perfect_matching_values=15,
        contains_all_fifteen_perfect_matchings=True,
        centralizer_order=len(centralizer),centralizer=centralizer,
        conclusion="No nonidentity automorphism fixing each fibre and using one common coordinate permutation on all eight fibres (with parents and twins fixed)",
        scope="This common-coordinate subgroup only, not the full graph automorphism group")
    path=OUT/"best.failure_summary.json"
    record=json.loads(path.read_text())
    record["bad_block_route_diagnosis"]=block
    record["common_coordinate_centralizer"]=symmetry
    record["local_diagnosis_resources"]=dict(cpu_seconds=time.process_time()-cpu,
        wall_seconds=time.monotonic()-wall,new_graph_candidates=0,new_bfs_runs=0,solver_calls=0)
    path.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(S=S,K=K,centralizer_order=len(centralizer),
                         resources=record["local_diagnosis_resources"])))


if __name__=="__main__":main()
