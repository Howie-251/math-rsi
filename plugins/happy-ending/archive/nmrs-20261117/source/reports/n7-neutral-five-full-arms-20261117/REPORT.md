# Five neutral m7 I ports: actual positive control and scoped exclusions

2026-11-17. The verified positive result is a genuine17-point Q7 domain with
five actual K roots, five genuinely red6-neutral I right ports, complete blue5
and red6 arms, and one actual shared minimum-partner p order. Its red6 paths
all end at one actual point. Five distinct final endpoints were not realized.
Six specified distinct-end templates/skeletons were excluded by actual DRAT
verification and independent full CNF reconstruction. No74-point claim or
universal five-distinct-end impossibility follows.

## Genuine17-point positive control

`single-root-gap17/colors.json` is a complete coloring on0..16. Let

```
P = [0,1,2]
A = [3,4,5,6,7]
B = [8,9,10,11,12]
T = [13,14,15,16]
```

Every pair(a,b) in A×B is an actual I pair: P+a+b is blue5 and a+b+T is
red6. The full actual I graph is exactly K5,5 and has maximum matching5.
This I-pair graph must not be confused with the red6 FIRST/LAST endpoint
graph: its red6 actual end set is only{16}.

Kissat returned SAT in0.0322 seconds. `check_model.py` directly checked every
one of44,552 CNF clauses, all packets, complete actual arms, no blue6/red7/
weak7, red6 neutrality of every marked b, no ambient red5 between marked b
endpoints, and absence of blue5/red5 in A and blue5 in B. Both colors attain
their permitted maxima5/6. Actual red6 sources are{1,2,3,4,5,6,7}; the only
actual red6 final point is16. These are actual-domain checks, not annotations.

`check_p.py` independently constructs and checks one common strict order of
all136 actual point pairs and the true minimum incident pair p at each point.
Its actual R7 split is U=R={0..7}, L={8..16}, G=empty, K=A. Thus the full
K/L origin of all five I roots is realized. In particular p(a)=8 for each
a∈A and p(b)=7 for each b∈B; the rest of p and the complete pair order are
stored in `pair-order.json`.

Color SHA256:
`4f5d5966f2e5d8fc78fd771a6005e95bff1ac8d9a6d57f6e3571b022baf1852d`.
This is a finite abstract signotope example; no planar realization is claimed.

## Exact leaf payment and the requested single-sided flow

`flow.py` independently reconstructs all89 actual red6 paths from colors.
The actual red6 endpoint graph has S={1..7}, E={16}, T=empty. All seven pure
sources are leaves with the one counterpart16. Thus d_16=7 and the canonical
leaf payment is J={16}, W={1..7}, B_leaf=6. W is retired, not physically deleted.
Every original K root belongs to W; no K root belongs to J.

After paying J there are no actual red6 paths, U0 is empty, and ν=κ=s=d=0.
This was computed twice as separate left-only networks: once using all
ambient true-neutral points as L0 and once using only the five marked I
ports. No right pool was merged and no double-sided optimum is asserted.
The resulting physical cover cost is |J|+κ=1. In the original domain before
J, the endpoint matching has size1; point16 is a unit cut and a red6 exists,
so the original left-only flow also has κ=ν=1 and s=0.

This example distinguishes five true ports from five injected distinct
red6 final endpoints. The roots are genuine K and have no II/G neighbor
before payment, but all five lose their source role after the explicit leaf
payment. Therefore their mere prepayment existence does not guarantee a
surviving five-root flow, extra congestion, or positive savings s.

## Distinct-end probes: exact limited scope

Every row below has actual Kissat UNSAT and successful drat-trim exit0 with
`s VERIFIED`. A second program `audit.py`, importing no generator, rebuilt
every variable domain and exact CNF clause stream and verified the bound
CNF hash. These are conditional template/skeleton exclusions.

| Probe | Actual slots | Clauses | Solver sec | Checker sec |
|---|---:|---:|---:|---:|
| P3/C3 common, common-gap five different ends |21|106817|0.0645|0.2654|
| P3/C3 common, separated five different ends |21|106323|0.0645|0.2151|
| Two P3/C3 groups3+2, common gap |27|300592|0.1147|0.4156|
| Two P3/C3 groups3+2, separated |27|300038|1.0170|0.6665|
| Five staggered red tails/ends, common P3, separated |33|683197|3.4225|10.1888|
| Free full-arm candidates on one common-gap skeleton |26|276435|2.0194|10.5893|

The33-point case places each complete red tail/end before the next marked
I pair, retaining a common blue prefix. Thus it is not merely the template
where every tail lies after all marked B endpoints. Its input is still
specified and does not cover arbitrary interleavings or blue prefixes.

The last probe is not a shared-prefix/shared-tail template. It fixes only

```
A = [3,4,5,6,7]
B = [8,9,10,11,12]
e = [17,19,21,23,25]
```

For all15 staircase actual I edges(a_i,b_j), j<=i, a blue5 witness can
choose any three earlier actual points; a red6 witness to e_j can choose
any three points strictly between b_j and e_j. There are294 blue candidates
and1,526 red candidates, with arbitrary intersections and interleavings.
An existential selector disjunction requires one actual color-valid path;
one-way reachability alone is never used to assert path existence. Forward
exact-length DP is used only for prohibitions. This probe excludes one
26-point endpoint/root skeleton and one end assignment; it does not cover
other positions, cardinalities or permutations.

The original21-point common-gap proof has a161-clause extracted core and
13 proof lines. Its small core CNF/proof were replayed separately:
drat-trim exit0, `s VERIFIED`. `core-binding.json` binds the core as an
actual original-clause submultiset; `core-decoded.json` gives variable meanings.
The26-point probe also retains an extracted4,437-clause core.

## Mathematical and evidence boundaries

The parent's independent mathematical observation rules out a complete
red6 FIRST/LAST endpoint K5,5 between five K roots and five different final
points. It explains a major danger of common-tail templates. It does not
identify the I-pair graph K5,5 with that FIRST/LAST graph; the17-point positive
control has the former and only one final point.

An attempted general replacement of (a_j,b_j,x,y,c,e_j) by
(a_i,b_1,x,y,c,e_j) was rejected because the new bridge(b_1,x,y) lacks a
known color. That attempted argument is not a theorem or a claimed
generalization of any exclusion here. Red bridge cases can copy a suffix;
blue bridge cases remain separate necessary structure.

No distinct-end SAT domain was found, so no leaf/flow values were invented
for those UNSAT instances. The actual leaf/flow calculation belongs only
to the checked17-point single-root example. No general five-port or
five-injected-end theorem was proved, no74-point candidate was excluded,
and no global numeric bound changed.

All scientific work ran under
`/data/ktqiu_hdd/math_agent/reports/n7-neutral-five-full-arms-20261117`
using `/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B`, the production
external Kissat executable and the explicit repaired drat-trim path.
Windows only edited, transferred, hashed source snapshots and unpacked
evidence. Exact old generator snapshots `build-v1.py` through `build-v4.py`
match the corresponding recorded source hashes; original CNFs/proofs/logs
remain unchanged. The generic historical `scope` string in the17-point
raw result still says different roots; its `input.json`, this report and
independent audit explicitly record the single root16 and govern its scope.

The separate eight-parameter actual23-point examples and their stronger
full-arm positive conclusion remain in the sibling n8 report. They are not
replaced by the m7 conditional UNSAT probes.
