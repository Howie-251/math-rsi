"""Frequency/capacity relaxation only; no high-trace or J-source enumeration."""
from itertools import product
from pathlib import Path
import json
import time

start = time.process_time()
DIR = Path(__file__).parent
old = {(17,0,0),(15,1,0),(14,0,1),(0,4,3),(1,2,4),(2,0,5),
       (0,1,5),(0,7,1),(5,0,4),(13,2,0),(12,1,1),(11,0,2),
       (11,3,0),(9,4,0)}

def safe(n2,n3,n4,a,b,s):
    m, k1, k2, t = 7-a-b-s, n4-b, n3-a, n2-s
    assert min(m,k1,k2,t) >= 0
    if m == 0:
        return "empty_red"
    if k1 == 0:
        if m <= 4 and k2 <= 3:
            return "four_large_three_pairs"
        if m <= 3 and k2 <= 4 and t <= 35:
            return "three_large_four_pairs"
        if m <= 2 and k2 < 16:
            return "two_foursets_pair_count"
        if k2 == 0:
            if m <= 5:
                return "five_foursets_total35"
            if m <= 6 and t <= 6:
                return "six_foursets_six_T"
            if m <= 7 and t <= 4:
                return "seven_foursets_four_T"
    k = k1+k2
    if k <= 1:
        if m <= 4:
            return "forbid_one_four_min3"
        if m <= 5 and t <= 3:
            return "forbid_one_five_min3_three_T"
    if k <= 2:
        if m <= 3 and t <= 7:
            return "forbid_two_three_min2"
        if m <= 4 and t <= 4:
            return "forbid_two_four_mixed"
        if m <= 5 and t <= 2:
            return "forbid_two_five_mixed"
    if k <= 3 and m <= 2:
        return "forbid_three_two_nonempty"
    if k1 == 1:
        if m <= 2 and k2 < 9:
            return "forbid_quad_two_min3"
        if m <= 3 and k2 <= 2 and t < (3-k2)*9:
            return "forbid_quad_three_parameter"
    if k1 == 2 and m <= 2 and k2 < 4:
        return "forbid_quads_two_min2"
    return None

def cells(n2,n3,n4,core):
    result=[]
    for a in range(n3+1):
        for b in range(n4+1):
            cap=min(n2,8-int(core)-a-b,15-4*int(core)-2*a-3*b)
            if cap < 0:
                continue
            ss=[s for s in range(cap+1)
                if not core or not safe(n2,n3,n4,a,b,s)]
            if not ss:
                continue
            # This is checked, rather than assuming q-failure monotonicity.
            assert ss == list(range(max(ss)+1)),(n2,n3,n4,a,b,ss)
            result.append((a,b,max(ss)))
    return result

def maximum_capacity(n2,n3,n4):
    # dp[(sum a,sum b)] = (largest J capacity, one seven-point witness).
    dp={(0,0):(0,[])}
    for core in [True]*5+[False]*2:
        nxt={}
        for (A,B),(value,witness) in dp.items():
            for a,b,cap in cells(n2,n3,n4,core):
                AA,BB=A+a,B+b
                if AA>3*n3 or BB>4*n4:
                    continue
                z=value+cap
                if (AA,BB) not in nxt or z>nxt[(AA,BB)][0]:
                    nxt[(AA,BB)]=(z,witness+[(a,b,cap)])
        dp=nxt
    return dp.get((3*n3,4*n4))

rows=[]
for n4 in range(6):
    for n3 in range(9):
        n2=17-2*n3-3*n4
        if n2<0:
            continue
        answer=maximum_capacity(n2,n3,n4)
        maximum = None if answer is None else answer[0]
        contradiction=answer is None or maximum<2*n2
        row=dict(inventory=[n2,n3,n4], previously_closed=(n2,n3,n4) in old,
                 actual_J_degree=2*n2, maximum_failure_J_capacity=maximum,
                 capacity_contradiction=contradiction)
        if answer is not None:
            row["capacity_witness"]=answer[1]
        rows.append(row)
assert len(rows)==33
new=[r["inventory"] for r in rows if r["capacity_contradiction"] and not r["previously_closed"]]
remaining=[r["inventory"] for r in rows if not r["capacity_contradiction"] and not r["previously_closed"]]
out=dict(status="COMPLETE_SCALAR_RELAXATION", scope="seven point frequencies and q-failure capacities; not source or H realization",
         previous_closed=sorted(old), previous_closed_count=len(old),
         new_capacity_contradictions=new, remaining_relaxation_inventories=remaining,
         rows=rows, cpu_seconds=time.process_time()-start)
(DIR/"CHECK.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:out[k] for k in ["previous_closed_count","new_capacity_contradictions","remaining_relaxation_inventories","cpu_seconds"]},indent=2))
