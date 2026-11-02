"""Bounded exact search of balanced repeat-component quotients.

This searches quotient matrices, not original graphs. A completed run is
external integer-computation evidence, not a Lean-certified classification.
Default: five components, each even and at least four (actual B<=2).
"""
import argparse
import itertools
import json
import math
import os
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[3]


def partitions(total, count, least=2):
    if count == 1:
        if total >= least:
            yield (total,)
        return
    for first in range(least, total // count + 1):
        for tail in partitions(total-first, count-1, first):
            yield (first,) + tail


def row_domain(n, i, trace):
    """All balanced integer rows satisfying the diagonal quadratic identity."""
    others = [j for j in range(len(n)) if j != i]
    row = [0]*len(n)
    col = [0]*len(n)
    out = []
    def rec(pos, used, square):
        if pos == len(others):
            d = 8-used
            if d > trace or d >= n[i] or d*d+d+square != n[i]+10:
                return
            row[i] = col[i] = d
            out.append((tuple(row), tuple(col)))
            return
        j = others[pos]
        g = math.gcd(n[i], n[j])
        a, b = n[j]//g, n[i]//g
        for t in range(min((8-used)//a, 8//b)+1):
            r, c = a*t, b*t
            if square+r*c > n[i]+10:
                break
            row[j], col[j] = r, c
            rec(pos+1, used+r, square+r*c)
    rec(0,0,0)
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--components",type=int,default=5,choices=(5,7,9))
    ap.add_argument("--seconds",type=float,default=30)
    args=ap.parse_args()
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    start=time.monotonic(); deadline=start+args.seconds
    k=args.components; trace=(17-k)//2
    sizes=[tuple(2*x for x in p) for p in partitions(31,k)]
    complete=0; zero_domain=0; nodes=0; labelled=0; found={}
    row_counts=[]; active=None; timed_out=False
    def check_time():
        if time.monotonic()>deadline:
            raise TimeoutError
    try:
        for n in sizes:
            active=n; check_time()
            domains=[row_domain(n,i,trace) for i in range(k)]
            row_counts.append([len(x) for x in domains])
            if any(not d for d in domains):
                zero_domain+=1; complete+=1; continue
            order=sorted(range(k),key=lambda i:len(domains[i]))
            assigned={}
            def search(pos,diagonal):
                nonlocal nodes,labelled
                nodes+=1
                if nodes%256==0:check_time()
                if pos==k:
                    if diagonal!=trace:return
                    R=tuple(assigned[i][0] for i in range(k))
                    labelled+=1
                    # Matrices with the same ordered sizes are relabelled only
                    # within equal-size groups.
                    variants=(tuple(R[p[i]][p[j]] for i in range(k) for j in range(k))
                              for p in itertools.permutations(range(k))
                              if all(n[p[i]]==n[i] for i in range(k)))
                    flat=min(variants)
                    rr=[list(flat[i*k:(i+1)*k]) for i in range(k)]
                    d1=[(i,j) for i in range(k) for j in range(k)
                        if (i==j and n[i]>=14 and rr[i][i]>=4)
                        or (i!=j and n[i]>=14 and n[j]>=14
                            and rr[i][j]>=4 and rr[j][i]>=3)]
                    found[(n,flat)]={"sizes":n,"R":rr,"necessary_D1_pairs":d1}
                    return
                i=order[pos]
                for row,col in domains[i]:
                    if diagonal+row[i]>trace:continue
                    good=True
                    for j,(rj,cj) in assigned.items():
                        if row[j]!=cj[i] or col[j]!=rj[i]:
                            good=False;break
                        if sum(row[z]*cj[z] for z in range(k))+row[j]!=n[j]:
                            good=False;break
                        if sum(rj[z]*col[z] for z in range(k))+rj[i]!=n[i]:
                            good=False;break
                    if good:
                        assigned[i]=(row,col)
                        search(pos+1,diagonal+row[i])
                        del assigned[i]
            search(0,0)
            complete+=1
    except TimeoutError:
        timed_out=True
    report={"status":"TIME_BUDGET_EXHAUSTED" if timed_out else "COMPLETE_QUOTIENT_SEARCH",
            "components":k,"minimum_component_size":4,"trace":trace,
            "size_partitions_total":len(sizes),"size_partitions_completed":complete,
            "partitions_with_empty_row_domain":zero_domain,"active_partition":active,
            "search_nodes":nodes,"labelled_solutions":labelled,
            "canonical_quotients":list(found.values()),
            "maximum_single_row_domain":max((max(a) for a in row_counts),default=0),
            "wall_seconds":time.monotonic()-start,"cpu_count":1,
            "scope":"Balanced integer component quotient candidates, not original graph existence",
            "D1_marks":"Conditional on the reviewed H,K>=14 paper chain",
            "independent_review":"not yet performed"}
    path=ROOT/f"computations/dd82/n62/component_quotients_{k}.json"
    path.write_text(json.dumps(report,indent=2)+"\n")
    brief={a:b for a,b in report.items() if a!="canonical_quotients"}
    brief["canonical_count"]=len(found)
    brief["with_D1_marks"]=sum(bool(q["necessary_D1_pairs"]) for q in found.values())
    print(json.dumps(brief,indent=2))


if __name__=="__main__":
    main()

