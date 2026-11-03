"""Exhaustive integer 3-component quotient diagnostic, not graph existence.

Every actual quotient has row sum8, trace7, positive even component sizes,
R²+R=10I+1n^T, and balanced edge counts. Retain only sizes>=4 (B<=2).
The D1 marks use the paper minimum-size bounds and do not assert realizability.
"""
from pathlib import Path
import itertools
import json
import os
import time

ROOT = Path(__file__).resolve().parents[3]
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})


def main():
    start = time.monotonic()
    found, tested = {}, 0
    for a,e in itertools.product(range(8),repeat=2):
        i = 7-a-e
        if not 0<=i<=8:
            continue
        for b in range(9-a):
            for d in range(9-e):
                for g in range(9-i):
                    r = ((a,b,8-a-b),(d,e,8-d-e),(g,8-i-g,i))
                    tested += 1
                    m = [[sum(r[u][z]*r[z][v] for z in range(3))+r[u][v]
                          -10*(u==v) for v in range(3)] for u in range(3)]
                    if m[0]!=m[1] or m[1]!=m[2]:
                        continue
                    n = m[0]
                    if any(x<4 or x%2 for x in n):
                        continue
                    assert sum(n)==62
                    if any(n[u]*r[u][v]!=n[v]*r[v][u] for u in range(3) for v in range(3)):
                        continue
                    variants = []
                    for p in itertools.permutations(range(3)):
                        variants.append((tuple(n[u] for u in p),
                                         tuple(r[u][v] for u in p for v in p)))
                    key = min(variants)
                    nn, flat = key
                    rr = [list(flat[j:j+3]) for j in (0,3,6)]
                    possibilities = []
                    for h,k in itertools.product(range(3),repeat=2):
                        if h==k:
                            permitted = nn[h]>=14 and rr[h][h]>=4
                        else:
                            permitted = nn[h]>=14 and nn[k]>=14 and rr[h][k]>=4 and rr[k][h]>=3
                        if permitted:
                            possibilities.append([h,k])
                    found[key] = dict(sizes=nn,R=rr,necessary_D1_component_pairs=possibilities)
    report = dict(status="EXHAUSTIVE_QUOTIENT_DIAGNOSTIC_ONLY",tested_matrices=tested,
                  canonical_quotients=list(found.values()),
                  wall_seconds=time.monotonic()-start,cpu_count=1,
                  scope="Integer equitable quotient possibilities, not full B or original G",
                  nonclaims=["No surviving quotient is asserted realizable",
                             "Connected B and all other component counts are outside this run",
                             "D1 marks depend on the current paper minimum-size proof"])
    out = ROOT / "computations/dd82/n62/three_component_quotients.json"
    out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
