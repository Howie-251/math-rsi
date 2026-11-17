# Critical two-pool order and private-edge probes

2026-11-17. Scope: necessary finite projections of the proposed 57-point
double-no-fork critical domain in section 4 of
`N7_74_BIDIRECTIONAL_RED_FOURS_20261117.md`. These are same-session exact
computations and short hand proofs. No external review, solver, or production
encoding was invoked or modified. The satisfying projections are not
57-point models.

## 1. A reusable order lemma

Let K be a pool whose labels all have ambient red outgoing rank four, and
let A=K\End_B3(K) have four labels a1<a2<a3<a4. Then a1,a2 are the earliest
two labels of K.

Indeed, if k in K\A lay before a2, at most one A-label would precede k.
Every triple in the five-label set A union {k} would therefore end in A.
Such a triple cannot be blue by the definition of A. All five labels would
form an actual red five inside K, contradicting their outgoing rank four.
Consequently every K\A label is later than a2. Reflection gives that c3,c4
are the latest two labels of H when C=H\Src_B3(H) has four labels.

Since the critical identities give c3 in K\A and a2 in H\C, both versions
imply a2<c3. This proof uses the original physical pools and ambient ranks;
it does not require a new finite-model assumption.

## 2. Exhaustive eight-label necessary projection

There are 70 interleavings of two disjoint ordered four-label sets. Reflection
and interchange of A,C identify 43 orbits; 16 orders are fixed by this
involution. `order_probe.py` exhaustively solved one representative per orbit.

The projection includes complete packet axioms, no R7/B6/weak7, hereditary
double-no-fork, red A and C, the two ambient red fans, all stated ambient rank
upper bounds restricted to the eight labels, and the following legal pool
projections:

- K contains A union {c3}; no blue triple in these five labels can end in A.
- H contains C union {a2}; no blue triple in these five labels can start in C.

Exactly 17 original orders are inconsistent: precisely those with c3<a2.
All 11 inconsistent representatives have one-node DPLL refutations consisting
only of unit propagation, replayed by a separate reason-checking routine.
The other 53 original orders have satisfying full eight-label colorings.
`audit_outputs.py` separately checked the colorings directly against packet,
path, rank, fan and pool semantics, including reflected orders; all passed.

The SAT models do not realize the ambient lower-rank witnesses. In particular,
all retained examples have no blue five on the eight labels; the ambient
blue-five first/last-pair certificates require additional physical labels.
The computation establishes the exact strength of the listed projection,
not that these orders extend to the original critical domain.

Raw records and colorings are in `order_cases/`; `summary.json` and
`direct_audit.json` give the batch and semantic recheck. Each inconsistent
record retains every clause, its mathematical reason, and the complete
replayable implication certificate.

## 3. Two actual private middle edges after A<C

For this second probe the parent supplied the stronger established input
A<C with all triples meeting both anchor sets blue. Consider actual private
middle edges a4 -> h and k -> c1, where k is in K\A and h is in H\C.
The former edge has an actual red six with third/fourth labels a4,h; the
latter has an actual red six with third/fourth labels k,c1. Their other
labels lie outside A union C. The probe does not invent those witnesses.

The order lemma gives

```
a2 < k < c1,       a4 < h < c3.
```

Thus k lies in one of (a2,a3), (a3,a4), (a4,c1), and h in one of
(a4,c1), (c1,c2), (c2,c3). The common central gap additionally distinguishes
k<h, k=h and h<k. These are exactly eleven endpoint types.

For an actual red-six middle edge u -> w, the following are sound necessary
blue bridges:

```
i u w is blue for every i in K with i<u;
u w j is blue for every j in H with j>w.
```

A red first bridge would prepend i to the actual red-four suffix and give
outgoing rank at least five at i; a red second bridge would append j to the
actual red-four prefix and give incoming rank at least five at j.

`private_edge_probe.py` uses these bridges, the fixed anchor colors, the
earlier necessary constraints, and the proven cheap-pool middle cover for
all red sixes retained in the projection. Four types are inconsistent,
exactly k<a4 together with c1<h. All four again have one-node implication
refutations. The seven remaining types have satisfying necessary endpoint
projections, including each of k<h, k=h and k>h in the central gap.

## 4. Uniform hand proof of the four rejected types

Assume k<a4<c1<h. Since k is outside A, choose a real blue triple
(x,i,k) inside K; since h is outside C, choose a real blue triple (h,j,y)
inside H. Their complete physical order is

```
x < i < k < a4 < c1 < h < j < y.
```

The actual middle edge k -> c1 gives blue triples (i,k,c1) and (k,c1,h).
The first and last entries of packet (i,k,c1,h) are therefore blue. The
one-change axiom forces its other entries blue, in particular (i,k,h).

The actual middle edge a4 -> h gives blue triples (k,a4,h) and (a4,h,j).
Packet (k,a4,h,j) similarly forces (k,h,j) blue. We obtain the actual blue
six (x,i,k,h,j,y), contradiction. Therefore

```
k > a4  OR  h < c1.
```

The same argument applies to any actual edges a -> h and k -> c with
a in A, c in C, k in K\A, h in H\C and k<a<c<h. It only uses the two
actual middle edges, pool ranks, and the two real blue triples; their
red-six witnesses may share other labels. No endpoint-disjointness assumption
is imposed on those witnesses.

The four finite contradictions thus have a complete general hand proof.
The seven remaining endpoint projections do not establish actual compatible
red-six witnesses or classify their possible shared external labels.
`private_direct.py` independently checked all seven explicit colorings against
the packet, path, rank, fan, pool, middle-cover and private-edge bridge
predicates directly, without using the clause compiler. All passed; all seven
have zero local red sixes. The result is retained in
`private_direct_audit.json` and makes the missing actual private witnesses
particularly explicit.

## 5. Evidence and reproduction

All project execution was on the authoritative Linux server via the existing
OpenSSH transport wrapper, in the exclusive directory
`/data/ktqiu_hdd/math_agent/tmp/n7_joint57_order_20261117`. Batches had internal
90-second and external 105-second limits; they completed in a few seconds.
`run.json`, `direct_run.json`, `private_run.json` and `core_run.json` retain
actual command and exit evidence. External solver invocations: zero.
`private_direct_run.json` additionally records the final direct semantic check.

The order source SHA256 was
`aed5ae737f489a1ecbedcb4f7d78433fe055e000e78cd15c9fae90fb95e2c7e9`.
`order_cases/` and `private_cases/` retain full inputs, clause reasons,
explicit satisfying colorings and replayable refutations. `private_cores.json`
contains backward implication cores of the four endpoint contradictions.

To reproduce, put `order_probe.py`, `audit_outputs.py`,
`private_edge_probe.py` and `extract_private_cores.py` into a fresh Linux
directory, since outputs use exclusive creation, and run each in that order
with `/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B`, under the stated
timeouts. No third-party Python dependency is required.
