# F11 seven-port local interface: actual result

This is a finite local interface, not a produced controller or a complete diameter-three graph. The experiment uses prime-field integer arithmetic modulo 11. It does not reuse the old characteristic-three GF9 operations.

The original prediction in `PRED.md` is partly false. Enumerating all 1320 distinct PGL2(F11) permutations on the 12 projective points gives four six-subset orbits of sizes **110, 220, 264, 330**, each invariant under complementation. The complete 924 rows are in `SIX_SUBSETS.csv`. The 792 seven-subsets have the following puncture profiles, ordered by those four orbits:

| Puncture counts | Number of seven-subsets |
| --- | ---: |
| (0,0,2,5) | 132 |
| (1,2,2,2) | 660 |

Thus every seven-subset has exactly two 264-type punctures, but its other five punctures need not have a common orbit. There is no single 660-size six-subset orbit. The complete profiles are in `SEVEN_SUBSET_PROFILES.csv`.

The first usable set in the fixed projective-point order is S={infinity,0,1,2,3,4,5}. Its final role order is

```
port       0   1    2     3   4   5   6
point      1   4   inf    0   2   3   5
role       a+  a-  b+     b-  s   t   r
orbit      264 264 330    330 330 330 330
reverse    1   0    3     2   4   5   6
```

The initial run placed the two cross-port pairs in the other order. `canonicalize_roles.py` merely exchanges those already checked pairs using the port permutation [2,3,0,1,4,5,6], which commutes with the reverse permutation. `initial_role_order/` preserves the original outputs. No group or subset classification was repeated and no extra chart was introduced. The 360 transported determinants and ten literal inverses were checked directly after relabeling.

## Quotient and exact transport

Write ell(z)=(1,z,z²) for finite z and ell(infinity)=(0,0,1). For a finite port point p, use

```
H_p(x0,x1,x2) = (x0,x1-p*x0,x2-p*x1),
H_inf(x0,x1,x2) = (x2,x0,x1).
```

Both take ell(p) to e0 exactly. For z different from p, the last two coordinates of H_p ell(z) are (z-p)(1,z); the infinity case gives quotient slope infinity. H_inf ell(z) has quotient (1,z). Hence the six quotient slopes at port p are exactly B_p=S\{p}, in the same projective coordinates for every p.

For f(z)=(a*z+b)/(c*z+d), the matrix Q_f=[[d,c],[b,a]] acts on the quotient vector (1,z) with projective slope f(z). A chart from source p to target q is chosen with f(B_p)=PG1(F11)\B_q, then transported as

```
T = H_q^-1 * diag(1,Q_f) * H_p.
```

Consequently T ell(p)=ell(q) with coefficient **one**, not only projectively. A compatible f exists precisely when B_p and B_q have the same orbit, because every orbit is complement-invariant. For this selected S there are 2²+5²=29 compatible ordered port pairs: the four pairs among ports 0,1 have five PGL maps each; the 25 pairs among ports 2,...,6 have four maps each. This records compatibility only. Actual matrices and rank/pencil checks are supplied only for the fixed reverse pairing below.

## Ten actual charts

All entries below are residues modulo 11. The full forward PGL coefficients, permutations, H matrices, exact literal inverses, port directions and allowed pairs are in `PARAMETERS.json`.

| Chart | Actual 3 by 3 matrix, rows separated by semicolons |
| --- | --- |
| 0 to 1 | (1,0,0; 10,8,8; 6,10,0) |
| 1 to 0 | (1,0,0; 6,0,10; 1,7,1) |
| 2 to 3 | (0,0,1; 10,0,0; 0,1,0) |
| 3 to 2 | (0,10,0; 0,0,1; 1,0,0) |
| self 4 plus | (1,0,0; 10,2,8; 7,3,6) |
| self 4 minus | (1,0,0; 4,5,8; 6,3,9) |
| self 5 plus | (1,0,0; 10,1,5; 7,4,5) |
| self 5 minus | (1,0,0; 1,7,4; 0,1,8) |
| self 6 plus | (1,0,0; 2,10,10; 0,3,7) |
| self 6 minus | (1,0,0; 9,1,8; 4,9,3) |

Each reverse or minus chart is the actual inverse of its forward or plus 3 by 3 matrix, with both products checked to equal I. A normalized projective inverse is insufficient: rescaling its quotient block need not give the inverse of diag(1,Q_f). The complementary mechanism agent records a concrete counterexample separately.

For an edge step y=T*x+t*ell(q), the reverse step is

```
x=T^-1*y-t*ell(p).
```

The minus sign is in F11, of characteristic 11. The exact coefficient-one port identity makes this equality literal.

## Actual rank and pencil checks

For each of the ten charts p to q, and each s!=p and t!=q, the determinant of columns

```
ell(q), T*ell(s), ell(t)
```

is nonzero. All **10*6*6=360** determinants are recorded in `CHART_CHECKS.json`. For each chart, the six planes span(ell(q),T*ell(s)) and the six planes span(ell(q),ell(t)) have 12 distinct normalized normals. Direct vector enumeration gives union size **1331=11³** for each of the ten charts. These are all planes of the pencil through ell(q).

The local finite experiment used 0.128829424 CPU seconds; the role transport and its small checks used 0.002573764, for measured finite-check CPU **0.131403188**, with one worker and a 20-second budget. There were no failed finite checks. `RESULT.json` retains the false original-prediction flags and `TERMINAL.json` records no active process.

## Scope of the returned interface

The fixed reverse-port map is [1,0,3,2,4,5,6]. A future controller must bind its darts to this map and preserve puncture type. Its special edges at ports 0,1 must form a spanning two-factor. Ports 4,5,6 are self-reverse port labels, but their matrices are used with an orientation and the actual inverse on the reverse dart; no involutivity of a plus matrix is assumed. Arbitrary sorted-neighbor port labels are not supported by these ten charts.

The rank and pencil data can be reused for any controller satisfying that precise interface. Actual controller route coverage, a triangle at every controller vertex for same-fiber routes, graph construction, public comparison, diameter validation and Lean remain separate obligations. This batch performs no controller search, full graph generation, BFS, Lean, solver call, extra cross-chart construction, or test at another field.
