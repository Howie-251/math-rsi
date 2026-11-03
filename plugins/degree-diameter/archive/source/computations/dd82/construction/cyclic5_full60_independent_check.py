"""Read-only reconstruction of the actual full-C5 CNF; no generator imports.

No solver, graph search or BFS is invoked. Only a short check record is added.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/"computations/dd82/construction"
OUT=BASE/"cyclic5_full60_run"


def read(name):return json.loads((OUT/name).read_text())


def main():
    cpu,wall=time.process_time(),time.monotonic()
    palette=read("palette.json")["orbits"]
    variables=read("variables.json")
    counters=read("degree_counters.json")
    coverage=read("coverage.json")
    by_key={(r["a"],r["b"],r["shift"]):r["variable"] for r in palette}
    assert len(by_key)==354 and set(by_key.values())==set(range(1,355))
    def edge(u,v):
        assert u!=v
        if u>v:u,v=v,u
        a,b=u//5,v//5;d=(v%5-u%5)%5
        if a==b:d=min(d,5-d)
        return by_key[a,b,d]
    pair_map={(u,v):edge(u,v) for u,v in combinations(range(60),2)}
    assert {tuple(r[:2]):r[2] for r in read("edge_variables.json")["rows"]}==pair_map
    groups={q:set() for q in range(1,355)}
    for pair,q in pair_map.items():groups[q].add(pair)
    assert all(len(v)==5 for v in groups.values())
    for item in palette:
        assert set(map(tuple,item["edges"]))==groups[item["variable"]]
        assert tuple(item["representative"]) in groups[item["variable"]]
    assert set(pair_map)==set(combinations(range(60),2))

    seed=read("seed.json");seed_edges=set(map(tuple,seed["edges"]))
    values={q:next(iter(es)) in seed_edges for q,es in groups.items()}
    assert all(all((e in seed_edges)==values[q] for e in es) for q,es in groups.items())
    assert sum(values.values())==48
    thresholds={(a,p,k):v for v,a,p,k in variables["degree_variables"]}
    assert len(thresholds)==5940
    expected=[]
    def clause(*lits):expected.append(tuple(lits))
    for a,row in enumerate(counters):
        assert row["orbit"]==a and row["vertex"]==5*a
        inputs=[edge(5*a,v) for v in range(60) if v!=5*a]
        assert inputs==row["inputs"] and len(inputs)==59
        hist=Counter(inputs)
        assert len(hist)==57 and sorted(q for q,n in hist.items() if n==2)==sorted([by_key[a,a,1],by_key[a,a,2]])
        total=0
        for p,x in enumerate(inputs,1):
            total+=values[x]
            for k in range(1,min(p,9)+1):
                z=thresholds[a,p,k];same=thresholds.get((a,p-1,k));lower=thresholds.get((a,p-1,k-1))
                values[z]=total>=k
                if k==1:
                    if same is None:clause(-z,x);clause(z,-x)
                    else:clause(-same,z);clause(-x,z);clause(-z,same,x)
                elif same is None:
                    clause(-z,x);clause(-z,lower);clause(z,-x,-lower)
                else:
                    clause(-same,z);clause(-x,-lower,z);clause(-z,same,x);clause(-z,same,lower)
        assert total==8
        assert row["final_thresholds"]==[thresholds[a,59,k] for k in range(1,10)]
        clause(thresholds[a,59,8]);clause(-thresholds[a,59,9])
    assert len(expected)==22968
    for a in range(12):clause(-by_key[a,a,1],-by_key[a,a,2])
    normalization_ids=[]
    for a in (0,1):
        for s in (1,2):clause(-by_key[a,a,s]);normalization_ids.append(len(expected))
    bound_count=0
    for a,b in combinations(range(12),2):
        cross=[by_key[a,b,s] for s in range(5)]
        for subset in combinations(cross,4):clause(*(-v for v in subset));bound_count+=1
        for endpoint in (a,b):
            for s in (1,2):
                for subset in combinations(cross,3):
                    clause(-by_key[endpoint,endpoint,s],*(-v for v in subset));bound_count+=1
        for sa in (1,2):
            for sb in (1,2):
                for subset in combinations(cross,2):
                    clause(-by_key[a,a,sa],-by_key[b,b,sb],*(-v for v in subset));bound_count+=1
    assert bound_count==5610
    gates={z:(left,right) for z,left,right in variables["and_variables"]}
    used_gates=[];coverage_ids={}
    for index,row in enumerate(coverage):
        assert row["orbit_index"]==index and row["pair"]==palette[index]["representative"]
        u,v=row["pair"];assert row["direct"]==edge(u,v)
        assert [p["middle"] for p in row["paths"]]==[w for w in range(60) if w not in (u,v)]
        for p in row["paths"]:
            z=p["output"];left,right=edge(u,p["middle"]),edge(p["middle"],v)
            assert (left,right)==(p["left"],p["right"])==gates[z]
            clause(-z,left);clause(-z,right);clause(z,-left,-right)
            values[z]=values[left] and values[right];used_gates.append(z)
        clause(row["direct"],*(p["output"] for p in row["paths"]))
        assert len(expected)==row["clause_id"];coverage_ids[len(expected)]=row
    assert len(used_gates)==len(set(used_gates))==20532
    assert set(used_gates)==set(gates) and len(values)==26826
    actual=[]
    for line in (OUT/"input.cnf").read_text().splitlines():
        if line.startswith("p "):assert line.split()==["p","cnf","26826","90544"]
        else:
            row=list(map(int,line.split()));assert row[-1]==0;actual.append(tuple(row[:-1]))
    assert actual==expected and len(actual)==90544
    false_ids=[i+1 for i,c in enumerate(actual) if not any(values[abs(v)]==(v>0) for v in c)]
    failed_coverage=[coverage_ids[i] for i in false_ids if i in coverage_ids]
    failed_units=[i for i in false_ids if i in normalization_ids]
    assert len(false_ids)==6 and len(failed_coverage)==4 and len(failed_units)==2
    listed=[int(x) for x in (OUT/"seed.assignment.txt").read_text().split()[1:] if int(x)]
    assert {abs(x):x>0 for x in listed}==values
    def shift(u,t):return 5*(u//5)+(u%5+t)%5
    expanded={tuple(sorted((shift(r["pair"][0],t),shift(r["pair"][1],t))))
              for r in failed_coverage for t in range(5)}
    old_map=json.loads((BASE/"cyclic5_twelve_orbits60_signature_lift_run/seed20/automorphism.json").read_text())["old_to_new"]
    old_graph=[tuple(map(int,line.split())) for line in (BASE/"petersen_all_matchings_run/candidate.best.edges").read_text().splitlines()][1:]
    assert {tuple(sorted((old_map[u],old_map[v]))) for u,v in old_graph}==seed_edges
    old_bfs=json.loads((BASE/"petersen_all_matchings_run/candidate.best.verification.json").read_text())
    old_bad={tuple(sorted(old_map[v] for v in row["pair"])) for row in old_bfs["bad_pairs"]}
    assert expanded==old_bad and len(expanded)==20
    result=dict(scope="Prepared full free-C5 order-60 CNF and old-seed consistency; no SAT decision",
        independent_generator_imports=False,source_and_actual_cnf_checked=True,
        primary_orbits=354,pair_partition_size=1770,degree_inputs=59,distinct_degree_inputs=57,
        degree_internal_weight=2,threshold_variables=5940,actual_paths=20532,
        guarded_multiplicity_clauses=5610,all_90544_clauses_match_expected=True,
        variables=26826,seed_assignment_independently_matches=True,
        false_coverage_clause_ids=[r["clause_id"] for r in failed_coverage],false_normalization_clause_ids=failed_units,
        expanded_bad_pairs_match_existing_bfs=True,expanded_bad_pair_count=20,
        solver_calls=0,new_bfs_runs=0,new_searches=0,
        cpu_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
        review_independence="same-family",acceptance_status="provisional")
    (OUT/"independent_check.json").write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=="__main__":main()
