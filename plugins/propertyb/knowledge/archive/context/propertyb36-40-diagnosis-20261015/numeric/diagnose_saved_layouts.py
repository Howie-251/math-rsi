"""Exact M=34..39 slack diagnosis; no layout search and no Lean run.

All nonempty trace counts and all positions are fixed. Only the empty count
is increased by M-34. Selected representatives are deliberately stratified;
their success ratios are not population estimates or new-parameter coverage.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HIGH = ROOT / "context/propertyb34/round01/high-math"
OLD = ROOT / "context/propertyb34/round02/twentyfive"
sys.dont_write_bytecode = True
sys.path[:0] = [str(HIGH), str(ROOT / "computations"),
               str(ROOT / "computations/propertyb33/round01")]
from bare_layout import BareLayout
from multilock import Profile, rows as independent_rows, total_bound, json_value
from pure_quota import certificate


def select(source, family, extras=()):
    data = json.loads((HIGH / source).read_text())["results"]
    strict = sorted((r for r in data if Q(r["bound"]) < 1), key=lambda r: (Q(r["bound"]), r["id"]))
    selected = {}
    for q in (0, 10, 25, 50, 75, 90, 99, 100):
        r = strict[(len(strict)-1)*q//100]
        selected.setdefault(r["id"], [r, []])[1].append(f"bound quantile {q}%")
    for case, why in extras:
        r = next(r for r in data if r["id"] == case)
        selected.setdefault(case, [r, []])[1].append(why)
    return [dict(family=family, source=source, label=f"{family}:{case}", reasons=why, **r)
            for case, (r, why) in selected.items()]


def analyze_sample(row):
    ns = {int(t): n for t, n in row["counts"].items() if n}
    v = row.get("v", 25)
    positions = row["positions"]
    assert sum(ns.values()) == 34
    baseline = Profile(v, 5, positions, ns)
    certs = [certificate(baseline, i) for i in range(len(positions))]
    deduction = {positions[i]: z["loss"] for i, z in enumerate(certs)}
    engine = BareLayout(v, positions)
    _, base_rows = engine.bound(ns, True)
    choices = [min(range(3), key=lambda j: r[j] - (deduction.get(k+1, Q()) if j == 2 else 0))
               for k, r in enumerate(base_rows)]
    series = []
    for M in range(34, 40):
        changed = dict(ns)
        changed[0] = ns.get(0, 0) + M-34
        bare, abc = engine.bound(changed, True)
        corrected = [tuple(z - (deduction.get(k+1, Q()) if j == 2 else 0)
                           for j, z in enumerate(r)) for k, r in enumerate(abc)]
        value = sum((min(r) for r in corrected), Q())
        fixed = sum((r[c] for r, c in zip(corrected, choices)), Q())
        free = sum((min(r) for k, r in enumerate(corrected) if k+1 not in positions), Q())
        locked = value-free
        if M == 34 and "bound" in row:
            assert value <= Q(row["bound"]), (row["label"], value, row["bound"])
            if row["family"] != "q5":
                assert value == Q(row["bound"]), (row["label"], value, row["bound"])
        # Independent ordered-type-pair implementation at both endpoints.
        if M in (34, 39):
            replay = independent_rows(Profile(v, 5, positions, changed), deductions=deduction)
            assert total_bound(replay) == value
            assert all((a[0],a[1],a[2]) == (b["A"],b["B"],b["C"]) for a,b in zip(abc,replay))
        series.append(dict(M=M, proves_lower_bound_if_scope_covered=M+1,
            empty_count=changed[0], bare=bare, corrected=value, fixed_old_choice=fixed,
            strict=value<1, free_contribution=free, locked_contribution=locked,
            rows=[dict(k=k+1,A=a,B=b,C=c,deduction=deduction.get(k+1,Q()),
                       corrected_C=corrected[k][2],bound=min(corrected[k]))
                  for k,(a,b,c) in enumerate(abc)]))
    assert len({r["locked_contribution"] for r in series}) == 1
    return dict(label=row["label"],family=row["family"],source=row.get("source"),
        reasons=row["reasons"],v=v,positions=positions,counts=ns,
        saved_bound=row.get("bound"),quota_certificates=certs,
        old_choices=choices,series=series,
        last_strict_M=max((r["M"] for r in series if r["strict"]),default=None))


def analyze_affine_family(family, witness):
    B=family["full"]
    inc=[sum(bool(t&(1<<i)) for t in B) for i in range(9)]
    base_empty=sum(inc)-len(B)-24
    pos=witness["positions"]
    assert max(pos)-min(pos)==8
    eng=BareLayout(25,pos)
    lows=family["lows"]
    def counts(low,M):
        return {0:base_empty+M-34,**{1<<i:7-inc[i]-int(i in low) for i in range(9)},**{t:1 for t in B}}
    series=[]
    slopes0=None
    for M in range(34,40):
        ns=counts(lows[0],M)
        _,actual_rows=eng.bound(ns,True)
        # On the five-low slice, every free-position row is independent of color.
        free=sum((min(r) for k,r in enumerate(actual_rows) if k+1 not in pos),Q())
        _,all_high=eng.bound(counts([],M),True)
        high=[min(all_high[pos[i]-1]) for i in range(9)]
        slopes=[]
        for i in range(9):
            _,one_low=eng.bound(counts([i],M),True)
            slopes.append(min(one_low[pos[i]-1])-high[i])
        constant=free+sum(high,Q())
        if slopes0 is None:slopes0=slopes
        assert slopes==slopes0
        max_value=Q(-1)
        for low in lows:
            actual,rr=eng.bound(counts(low,M),True)
            predicted=constant+sum((slopes[i] for i in low),Q())
            assert predicted==actual
            assert sum((min(r) for k,r in enumerate(rr) if k+1 not in pos),Q())==free
            max_value=max(max_value,actual)
        top=sorted(family["eligible"],key=lambda i:slopes[i],reverse=True)[:5]
        assert constant+sum((slopes[i] for i in top),Q())==max_value
        series.append(dict(M=M,constant=constant,slopes=slopes,free=free,
            top_five=top,maximum=max_value,strict=max_value<1,
            strict_colorings=sum(eng.bound(counts(low,M))<1 for low in lows),colors=len(lows)))
    return dict(base=family["base"],positions=pos,target=witness["target"],
        full=B,incidences=inc,series=series)


if __name__=="__main__":
    started=time.monotonic()
    selected=select("V25_NINE_Q5_BOUNDS.json","q5",[(4423,"tightest original q5"),
        (2153,"officially built actual caller"),(4424,"affine source family127"),
        (7680,"affine source family200"),(11687,"affine source family365"),
        (11691,"saved noncontiguous layout")])
    selected+=select("V25_NINE_Q8_BOUNDS.json","q8")
    selected+=select("V25_NINE_Q9_BOUNDS.json","q9")
    for source,family in [("V25_TENTH_BOUNDS.json","q9+tenth"),("V25_Q8_TENTH_BOUNDS.json","q8+tenth")]:
        groups=json.loads((HIGH/source).read_text())["results"]
        for group in groups:
            case=max(enumerate(group["cases"]),key=lambda z:Q(z[1]["bound"]))
            selected.append(dict(family=family,source=source,
                label=f"{family}:base{group['base']}:degree{group['new_degree']}:case{case[0]}",
                reasons=["tightest stored tenth-extension witness in this base/degree branch"],**case[1]))
    lowdir=ROOT/"context/propertyb34-feasibility-20261013/low-vertices"
    for name,indices in [("RESULTS.json",[23,29,35]),("EXTRA_RESULTS.json",[1,6,14])]:
        cases=json.loads((lowdir/name).read_text())["cases"]
        for i in indices:
            selected.append({**cases[i],"family":"nineteen","source":str((lowdir/name).relative_to(ROOT)),
                "label":f"nineteen:{name}:{i}","reasons":["single degree5/6/7 or representative loose/tight triple/strong pair; original nested quotas retained"]})
    for v in range(18,26):
        selected.append(dict(family="no_lock",label=f"no_lock:v{v}",v=v,
            positions=[],counts={0:34},reasons=["unconditional no-lock control at this vertex count"]))
    samples=[analyze_sample(r) for r in selected]
    fams=json.loads((OLD/"Q5_COLORED_CERTIFICATES.json").read_text())["families"]
    pilots=json.loads((OLD/"Q5_AFFINE_FAMILY_PILOT.json").read_text())["families"]
    affine=[analyze_affine_family(fams[p["base"]],p["chosen"][0]) for p in pilots]
    summary={}
    for family in dict.fromkeys(s["family"] for s in samples):
        group=[s for s in samples if s["family"]==family]
        summary[family]=dict(sample_count=len(group),strict_counts={str(M):sum(s["series"][M-34]["strict"] for s in group) for M in range(34,40)})
    output=dict(scope=__doc__,elapsed_seconds=time.monotonic()-started,
        selection="bound quantiles 0,10,25,50,75,90,99,100 percent plus named caller/family examples; tightest existing tenth cases; no-lock controls",
        no_new_layout_search=True,no_lean=True,summary=summary,samples=samples,affine_families=affine)
    (HERE/"SAVED_LAYOUT_SLACK.json").write_text(json.dumps(json_value(output),indent=2)+"\n")
    print(json.dumps(dict(elapsed_seconds=output["elapsed_seconds"],summary=summary,
        affine=[dict(base=f["base"],maxima=[str(r["maximum"]) for r in f["series"]]) for f in affine]),indent=2))
