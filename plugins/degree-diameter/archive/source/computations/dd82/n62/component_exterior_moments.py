"""Bounded exterior-incidence relaxation for a D1 heavy component of size12.

Floating LP is only discovery. Any separator retained is reconstructed as
integers and checked exactly on the declared finite (x,y) domain. This
checks a necessary moment system, not a graph or the whole D1 branch.
"""
from fractions import Fraction
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import itertools
import json
import os
import time

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
import numpy as np
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "computations/dd82/n62/component_exterior_moments.json"


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def main():
    start = time.monotonic()
    reports = []
    h = 12
    for k, a, b in [(12, 4, 4), (16, 4, 3), (20, 5, 3), (24, 6, 3), (28, 7, 3)]:
        assert h * a == k * b
        for s, t in itertools.product(range(9 - a), range(9 - b)):
            rhs = [62-h-k, h*(8-s-a), k*(8-t-b),
                   h*(h+2-s*s-a*(b-1)),
                   k*(k+2-t*t-b*(a-1)), h*(k-a*(s+t+1))]
            if min(rhs) < 0:
                continue
            points = [(x,y) for x in range(9) for y in range(9-x)
                      if (s+1)*x+b*y <= h and a*x+(t+1)*y <= k]
            features = [[1,x,y,x*(x-1),y*(y-1),x*y] for x,y in points]
            matrix = np.array(features, dtype=float).T
            fit = linprog(np.zeros(len(points)), A_eq=matrix, b_eq=rhs,
                          bounds=(0,None), method="highs", options={"time_limit": 1.0})
            item = dict(h=h,k=k,a=a,b=b,s=s,t=t,rhs=rhs,
                        domain=points,status=int(fit.status),
                        meaning="moment relaxation only")
            if fit.success:
                item["status_label"] = "LP_RELAXATION_FEASIBLE"
                item["floating_weights"] = [[*p,float(weight)] for p,weight in zip(points,fit.x)
                                            if weight > 1e-8]
            elif fit.status == 2:
                sep = linprog(np.array(rhs), A_ub=-matrix.T,
                              b_ub=np.zeros(len(points)), bounds=[(-1,1)]*6,
                              method="highs", options={"time_limit": 1.0})
                assert sep.success and sep.fun < -1e-7
                rational = [Fraction(float(z)).limit_denominator(10000) for z in sep.x]
                scale = lcm(*(q.denominator for q in rational))
                ints = [int(q*scale) for q in rational]
                divisor = reduce(gcd, map(abs,ints))
                ints = [v//divisor for v in ints]
                values = [dot(ints,row) for row in features]
                target = dot(ints,rhs)
                assert min(values) >= 0 and target < 0
                item.update(status_label="EXACT_SEPARATOR_FOR_MOMENT_SYSTEM",
                            separator=ints,domain_min=min(values),rhs_value=target)
            else:
                item["status_label"] = "UNRESOLVED_LP_STATUS"
            reports.append(item)
    output=dict(scope="Order62 D1, |H|=12, H and K distinct; conditional exterior moments",
                feature_order=["1","x","y","x(x-1)","y(y-1)","xy"],
                wall_seconds=time.monotonic()-start,cpu_count=1,
                cases=reports,
                nonclaims=["LP feasibility is not graph existence",
                           "This is not an original-graph proof or complete order62 exclusion",
                           "The necessary moment derivation requires a separate paper review"])
    OUT.write_text(json.dumps(output,indent=2)+"\n")
    for item in reports:
        print(json.dumps({key:item[key] for key in
                         ("k","a","b","s","t","status_label")}),flush=True)
    print(json.dumps(dict(cases=len(reports),wall_seconds=output["wall_seconds"])))


if __name__ == "__main__":
    main()
