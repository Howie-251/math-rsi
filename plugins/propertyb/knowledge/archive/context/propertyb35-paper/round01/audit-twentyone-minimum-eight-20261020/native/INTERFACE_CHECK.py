"""Fresh checks of actual-domain interfaces, independent of verifier claims."""
from pathlib import Path
from collections import Counter
from itertools import combinations, product
from math import comb
from fractions import Fraction
import json
import time

P = Path(__file__).resolve().parent
ROOT = P.parents[4]
B = ROOT/"context/propertyb35-paper/round01/middle"
start = time.process_time()
def read(name):
    return json.loads((B/name).read_text())
def parts(total, low=1):
    if total == 0:
        yield ()
    for x in range(low, total+1):
        for tail in parts(total-x, x):
            yield (x,)+tail

spectra = []
for e in range(7):
    for part in parts(e):
        if len(part) <= 7-e:
            spectra.append([8]*(14+e)+[9]*(7-e-len(part))+[9+x for x in part])
saved = read("min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_RESULT.json")
assert spectra == [z["degrees"] for z in saved["jobs"]]
assert len(spectra) == 15 and spectra[-1] == [8]*20+[15]
assert [sum(comb(d,2) for d in spectra[i]) for i in (8,9,11,12)] == [651,650,655,653]

pairdata = read("delta8_strong_pair_transfer_20261020/PAIR_RESULT.json")
support = {}
for sid, ds in enumerate(spectra):
    for x,y in set(combinations(ds,2)):
        for c in range(5,min(x,y)+1):
            support.setdefault((x,y,c),set()).add(sid)
assert support == {(z["degrees"][0],z["degrees"][1],z["codegree"]):
                   set(z["spectrum_ids"]) for z in pairdata["cases"]}
for z in pairdata["cases"]:
    x,y = z["degrees"]; c=z["codegree"]
    assert {int(k):v for k,v in z["counts"].items()} == {
        0:35-x-y+c,1:x-c,2:y-c,3:c}
tails = [z for z in pairdata["cases"] if not z["strict"]]
assert {(tuple(z["degrees"]),z["codegree"],tuple(z["spectrum_ids"])) for z in tails} == {
    ((10,12),5,(8,)),((11,11),5,(9,)),((10,13),5,(11,)),((11,12),5,(12,))}

# Rebuild all prefix residuals from the full orbit record, with only minF>=8.
base = read("three_nonunit_direct_repair_20261020/RESULT.json")
table = {tuple(z["types"]):z for z in base["residual_types"]}
order = ["P",0,2,3,4]
generic = set(); actual = set(); histogram=Counter()
for z in base["orbits"]:
    tr=tuple(z["traces"])
    lower = [table[tuple(sorted(("P" if m>>v&1 else m.bit_count()
                                for m in tr),key=order.index))]["first_failure_k"]
             for v in range(5)]
    left=31-sum(lower)
    if left<0:
        continue
    for extra in product(range(left+1),repeat=5):
        if sum(extra)!=left:
            continue
        a=tuple(x+y for x,y in zip(lower,extra)); generic.add((tr,a))
        degrees=[1+a[v]+sum(m>>v&1 for m in tr) for v in range(5)]
        if min(degrees)>=8:
            actual.add((tr,a))
            histogram[sum(max(d-9,0) for d in degrees)]+=1
assert len(generic)==119 and len(actual)==25
assert histogram=={0:1,1:11,2:11,3:1,4:1}
five=read("three_nonunit_direct_repair_20261020/FIVE_LOCK_FULL83.json")
assert actual=={(tuple(z["traces"]),tuple(z["attachments"])) for z in five["cases"]
                if min(z["selected_degrees"])>=8}

# Rebuild marked families directly from the exceptional spectra and side roles.
quads=set()
for z in tails:
    sid=z["spectrum_ids"][0]; ds=spectra[sid].copy()
    u,v=z["degrees"]; ds.remove(u);ds.remove(v)
    for a,b in set(combinations(ds,2)):
        quads.add((u,v,max(a,b),min(a,b)))
assert len(quads)==6
families=set()
for u,v,a,b in quads:
    families.add(("same",(u,v,a,b),3))
    for x,y in {(a,b),(b,a)}:
        families.add(("cross",(u,x,v,y),5))
dom=read("c3_unique_high_pair_five_20261020/DOMAIN.json")
assert families=={(f["role"],tuple(f["degrees"]),f["marked_pair"])
                  for f in dom["profile"]["families"]}
assert len(families)==14
for sid in (8,9,11,12):
    ds=spectra[sid]
    for indices in combinations(range(21),4):
        if 19 in indices and 20 in indices:
            continue
        selected=[ds[i] for i in indices]
        assert max(selected)<=13 and sum(max(d-9,0) for d in selected)<=4

# Independent exact normalization of the one-/two-flip original-H criteria.
D=comb(21,10)
def C(n,k): return comb(n,k) if 0<=k<=n else 0
p=Fraction(C(16,5)+C(16,10),D)
q=Fraction(C(12,5)+C(12,6),D)
weights=[C(8+j,1+j)+C(8+j,6) for j in range(5)]
assert p==Fraction(2,57) and q==Fraction(1716,D)
assert weights==[36,120,330,792,1716]
assert Fraction(5)*(2-35*p)/(2*q)==Fraction(1190,3)
assert (2-35*p)*20*D==5445440
f=[sum((s//5+int(i<s%5))*(s//5+int(j<s%5))
       for i in range(5) for j in range(i)) for s in range(31)]
increments=[f[s+1]-f[s] for s in range(30)]
assert increments==sorted(increments) and f[30]==360
for n in range(397,526):
    full,rem=divmod(2*n,30)
    assert full+(rem>0)<=35

out={"status":"PASS","spectra":15,"exceptional_W":[651,650,655,653],
     "pair_parameters":len(support),"strict_pairs":len(pairdata["cases"])-len(tails),
     "q3_generic":len(generic),"q3_min8":len(actual),"q3_no_excess_filter":True,
     "marked_families":len(families),"global_C3_caller_discharge":True,
     "two_flip_integer_threshold":5445440,
     "cpu_seconds":time.process_time()-start}
(P/"INTERFACE_CHECK.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out))
