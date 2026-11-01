"""Fresh-review arithmetic replay; reads project sources, writes only beside this file."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
from math import comb, ceil
import json
import re
import subprocess
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
SOURCE = ROOT / "context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020"
started = time.monotonic()

def f(s):
    # Sum of cross-group products after distributing s into five balanced groups.
    groups = [s // 5 + (i < s % 5) for i in range(5)]
    return sum(groups[i] * groups[j] for i in range(5) for j in range(i))

@lru_cache(None)
def threshold(n, edges, offset):
    if edges < 0 or edges > comb(n, 2):
        return None
    if n == 0:
        return 0
    choices = []
    isolated = threshold(n - 1, edges, offset)
    universal = threshold(n - 1, edges - n + 1, offset + 1)
    if isolated is not None:
        choices.append(f(offset) + isolated)
    if universal is not None:
        choices.append(f(offset + n - 1) + universal)
    return max(choices)

def allocation(n, budget):
    caps = [33*n[0], 26*n[1]+339, 24*n[2], 13*n[3], 4*n[4]]
    alloc = [0]*5
    for j in (4, 3, 2, 1, 0):
        alloc[j] = min(caps[j], budget)
        budget -= alloc[j]
    value = F(sum(c*w for c,w in zip(alloc,(36,120,330,792,1716))),2) + 3432*n[1]
    return alloc, value

def lower(N, t):
    return max(0, N-21, ceil(F(8*N*(N-21)-105*t,84)),
               ceil(F(8*N*(N-21),189)),
               ceil(F(152*N*(N-21)-2037*t,1428)))

# Exact sample coefficients and single/double-flip normalization.
D = comb(21,10)
p = F(comb(16,5)+comb(16,10), D)
q = F(comb(12,5)+comb(12,6), D)
r = [F(comb(8+j,1+j)+comb(8+j,6),D) for j in range(5)]
assert p == F(2,57) and q == F(1716,D)
assert [int(x*D) for x in r] == [36,120,330,792,1716]
assert F(5)*(2-35*p)/(2*q) == F(1190,3)
assert (2-35*p)*10*D == 2722720
direct = [F(34*35+91*6,1820),
          F(33*35+91*6,1820)+F(147,4368),
          F(33*35+91*7,1820)]
assert direct == [F(434,455),F(1007,1040),F(448,455)]
assert all(x<1 for x in direct)
assert [21*(j-1)**2-8*(j-1) for j in range(5)] == [29,0,13,68,165]
assert ceil(F(152*34*13,441)/2 - F(13*55,42)) == 60
assert ceil(F(152*34*13,441)/2 - F(13*52,42)) == 61
assert ceil(F(152*33*12,441)/2 - F(13*61,42)) == 50
assert 2*(6+7+8+8+8)-15 == 59
assert 616+110*19+374*6+66*3+1430*3 == 9438 > 9278

# Recompute T; no saved threshold value is used in the new filtering.
saved_T = json.loads((SOURCE.parent/"a1_middle_wedge_capacity_20261020/GRAPH_PILOT.json").read_text())["threshold_Pmax"]
for n1 in range(397,547):
    assert threshold(35,n1,0) == saved_T[str(n1)]

# A different moment parameterization: choose (n2,n3,n4), recover tau,n1,n0.
domain = set()
survivors = {}
for t in range(9):
    for n3 in range(94):
        for n2 in range(281):
            tau = n2+3*n3+6*t-140
            if not 0<=tau<=140:
                continue
            n1 = 648-2*n2-3*n3-4*t
            n0 = 595-n1-n2-n3-t
            n = (n0,n1,n2,n3,t)
            if min(n)<0 or not 397<=n1<=546:
                continue
            assert sum(n)==595 and sum(j*n[j] for j in range(5))==648
            assert sum(comb(j,2)*n[j] for j in range(5))==140+tau
            key = (n,tau)
            domain.add(key)
            c,v = allocation(n,threshold(35,n1,0))
            if v>=2722720:
                survivors[key] = (c,v)
assert len(domain)==21615 and len(survivors)==25
saved = json.loads((SOURCE/"SIMPLE_CHAIN_RESULT.json").read_text())
saved_keys = {(tuple(p["n"]),p["tau"]) for p in saved["profiles"]}
assert set(survivors)==saved_keys

# Compile both read-only project sources to reviewer-owned executables.
binaries = []
for filename,label in [("SIMPLE_CHAIN_DP.cpp","prefix"),("SIMPLE_CHAIN_FREQUENCY_VERIFY.cpp","frequency")]:
    exe = OUT / label
    result = subprocess.run(["clang++","-O3","-std=c++17",str(SOURCE/filename),"-o",str(exe)],capture_output=True,text=True)
    assert result.returncode==0, result.stderr
    binaries.append(exe)

keys = sorted({(595-n[1],n[4]) for n,tau in survivors})
assert len(keys)==19
records = {}
for E,t in keys:
    first,second = [json.loads(subprocess.check_output([str(exe),str(E),str(t)],text=True)) for exe in binaries]
    assert first["bound"]==second["bound"]
    qs=first["q"]
    assert len(qs)==35 and min(qs)>=2 and max(qs)<=34
    assert qs==sorted(qs,reverse=True) and sum(qs)==2*E
    assert qs[0]<=E-60+2*t and qs[12]<=E-61+2*t
    assert sum(qs[:2])<=E-49+2*t
    assert all(sum(qs[:i])<=E+comb(i,2)-lower(35-i,t) for i in range(1,36))
    assert sum(f(34-q) for q in qs)==first["bound"]
    records[E,t]=dict(E=E,n4=t,bound=first["bound"],q=qs)
assert {(r["e"],r["n4_cap"],r["bound"]) for r in saved["records"]} == {(e,t,r["bound"]) for (e,t),r in records.items()}

checked_profiles=[]
remaining=[]
for n,tau in sorted(survivors):
    dp=records[595-n[1],n[4]]["bound"]
    budget=min(dp,threshold(35,n[1],0))
    c,v=allocation(n,budget)
    row=dict(n=list(n),tau=tau,dp=dp,P_bound=budget,C=c,L=str(v))
    checked_profiles.append(row)
    if v>=2722720:
        remaining.append(row)
assert len(remaining)==1 and remaining[0]["n"]==[33,523,0,31,8] and remaining[0]["tau"]==1
assert remaining[0]["L"]=="2725500"
assert max(F(r["L"]) for r in checked_profiles if F(r["L"])<2722720)==2721300

# Compare the actual main-text table, not just an associated JSON.
main = (ROOT/"proofs/propertyb35/TWENTYONE_UNIQUE_SIX_ONE_SEVEN.md").read_text()
table=set()
for m in re.finditer(r"^\|(\d+,\d+,\d+,\d+,\d+)\|(\d+)\|(\d+)\|(\d+)\|$",main,re.M):
    table.add((tuple(map(int,m[1].split(","))),int(m[2]),int(m[3]),int(m[4])))
assert table=={(tuple(r["n"]),r["tau"],r["dp"],int(r["L"])) for r in checked_profiles}

result=dict(
    status="PASS",
    scope="Fresh threshold recurrence and alternative complete moment parameterization; compile/replay both existing degree DPs; all witness constraints and all 25 allocations/main-text rows.",
    threshold_values_recomputed=150,
    threshold_states=threshold.cache_info().currsize,
    moment_domain=21615,
    first_survivors=25,
    degree_keys=19,
    after_degree=remaining,
    final_coupling="Mathematically reviewed: original n4=8 forces an Hbar quad triangle, hence original tau>=3; contradicts unique remaining tau=1.",
    direct_failure_bounds=list(map(str,direct)),
    largest_excluded_L="2721300",
    smallest_strict_margin=2722720-2721300,
    records=list(records.values()),
    profiles=checked_profiles,
    elapsed_seconds=time.monotonic()-started,
    old_large_certificates_replayed=False,
    lean_executed=False
)
(OUT/"INDEPENDENT_CHECK.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k not in ("records","profiles")},indent=2))
