<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Frozen larger row pools: exact minimum remains nine

2026-11-17. The sealed 115-row milestone proves at least nine holes. Subsequent
work produced a frozen 215-row pool from 33 checked source kernels and, after
the final separate transport merge, a 271-row pool. Both larger pools have
independently verified nine-hole vectors. Their exact matrix minimum remains
nine; ten/eleven holes were not proved. The ordinary-866-at-most-61 candidate
therefore remains the mathematical endpoint of this run.

These are necessary matrices. Their feasible hole vectors are neither full
shared-label models nor actual signotope/planar avoiding constructions. The
original at-most-nine/ten/eleven full-model solves all timed out at 20 seconds.
No new full-model SAT result or all-budget exclusion is inferred from them.

## Frozen 215-row package

`appendix9plus/final-delivery/` is the locally returned standalone package.
Its actual Linux verification returned PASS in 5.91 seconds, reconstructing
all 93 baseline rows, every semantic clause and proof of 33 source kernels,
all four legal images, the inherited <=8 counter/proof, and the current
nine-hole vector. Its SHA256 is
`8797cbb5d4cc73c50207890559ad5bf761641685b502cf76cef4be01e48ee8cb`;
its 99-file manifest SHA256 is
`411770124dbb9d4a061f811d23add2319a38e04bed5a77b8aa663612ad38d73e`.
The original `milestone9/` was not modified.

The 215-row nine-hole survivor is

```
1238 1358 1468 1578 2367 2456 2457 3456 3457
```

Nine-hole adaptive batches rejected 18 additional distinct masks; the final
small batch rejected three more. Every rejection has successful full-CNF and
small-core proof checks. Only occupied states were fixed: neither budget units
nor positive hole units entered these kernels. The core rows therefore apply
universally whenever their supports are occupied. All raw large formulas and
proofs remain on Linux; the returned package contains the small proof chain.

## Four legal images

Let G=[4]x[4], rho(x,y)=(5-x,5-y), and D(I)=rho(G minus I). For I strictly
contained in J, D(J) is strictly contained in D(I) and
`D(I) minus D(J)=rho(J minus I)`. Pull target reversed-pair labels back by rho.
Chronological order and coordinate values both reverse, preserving strict blue
x-growth and red y-growth. Packets read backward and same-end paths reverse
with their colors unchanged. This is a pullback of actual path-existence
semantics, not a mechanical interchange of asymmetric reach4 variables.

True transpose T swaps grid coordinates and colors while retaining time.
The four code maps are W, rho8([8] minus W), rho8(W), and [8] minus W.
The final verifier checks all 70 ideals, 1694 directed inclusion differences,
512 growth comparisons, 16 packet patterns and 340 path-coordinate sequences.
The original 93 rows are already closed under these maps.

## Single-pair and genuinely two-pair certificates are different

The single-pair certificate uses `1247 -> 1258`, with cells (1,4) or (2,2).
Each branch unit-refutes a 52-clause occupation core. Its proof has three
additions: reject the first cell, reject the second, then the empty clause.

The genuinely joint certificate uses two different actual pairs:

```
P: 1268 -> 1468, cells (3,1) or (3,2)
Q: 1457 -> 2467, cells (2,3) or (4,1).
```

Both P-only branches remain unresolved by unit propagation. Q's first branch
also remains unresolved; its second refutes. All four P/Q choices unit-refute
the same 53-clause occupation core. Seven checked RUP additions comprise four
binary rejections `not(P_i and Q_j)`, then `not P_1`, `not P_2`, and the empty
clause. The standalone verifier recomputes the exact cell domains, every unit
reason and these seven proof lines, and invokes the real checker again.

The jointness claim is exactly this UP criterion. It does not say the individual
branches are logically satisfiable or that the proof is globally minimum.
The completed scan tested 462 pair-pairs from 23 exported cores. The original
single-pair proof and the full 1694-pair model retain their separate meanings.

## Dictionary scope and observed transport limits

A bounded 25-second census enumerated 200 transpose orbits / 400 physical
nine-hole vectors satisfying the earlier 123-row matrix. It did not exhaust
the domain, so 400 is a lower bound, not its total size. Search blockers were
never mathematical rows. Filtering the complete sample by 139 rows left
86 orbits / 172 vectors; filtering by the frozen 215 rows leaves 12 orbits /
24 vectors. This is a concrete sampled remainder, not a complete classification.

The first five uniform-cell-force/transpose orbits were fully enumerated and
each contained only two images. Both tested 13-state cores were rigid even
when restricting to used comparisons and shrinking only used pair domains.
More general pair-cell maps were developed separately by the transport worker.

## Final transport merge and stopping point

The other worker froze 15 four-image orbit representatives, including the
first row already present in 215. Their 56 genuinely new image supports were
merged in `appendix9plus/transport-merge/`, without changing either prior package.
All 271 rows have the following nine-hole survivor:

```
1268 1358 1378 1478 1567 2345 2456 2457 3467
```

Ten- and eleven-hole survivors are also retained. Thus the last merge still
cannot force ten holes. Its standalone delivery replays all source target-CNFs
directly in the same semantic variable ledger, all source proofs and four-image
identities, the inherited <=8 proof and every final vector. This supplies a
reproducible hard remainder and closes the authorized finite run.

The merged delivery is `appendix9plus/transport-merge/delivery/`. Its actual
Linux verification returned PASS in 7.67 seconds over 47 source proofs.
`merge271.tgz` SHA256 is
`2b3687e073d3755b55d9477d49db62c95725e7fac87bdb75d151c9169d5ed663`;
its 158-file manifest SHA256 is
`25e9eac67c1fd8f18fd0626fd37a122156bc06a2113cef284bc17b65a36746b6`.
The same 12 sampled orbits / 24 physical dictionary vectors still survive
the final 271 rows. This remains a sampled lower-count remainder.

On Linux with Python and an existing drat-trim, reproduce either delivery by:

```bash
python3 verify.py --directory . --checker /path/to/drat-trim
```

All scientific execution was Linux-only. Windows performed control-plane
edits, transfers, archive unpacking and byte hashes. Source proofs, timeout
prefixes and large formulas remain at the authoritative Linux root. A prototype
201-row bundle had an overwritten displayed single-pair field; its actual
checks were sound. The frozen final deliveries use explicit names and correctly
distinguish both small certificates. All predecessor artifacts are preserved.
