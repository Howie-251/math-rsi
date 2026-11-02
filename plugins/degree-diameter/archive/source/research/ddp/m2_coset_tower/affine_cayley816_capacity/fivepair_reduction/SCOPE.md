# Five-pair reduction in F17 semidirect C48

This preprocessing covers exactly the 16,375 saved symbolic survivors with five inverse pairs and two reflections for degree 12, diameter 3, order 816. It reads the saved complete maximin inputs and per-pattern terminal: 28 of these modes have already had all their marked field assignments excluded. No four-pair or six-pair mode was reprocessed. This is a necessary-condition reduction, not an existence result.

## Group and component coordinates

Write `(x,j)(y,k)=(x+3^j y,j+k)` in F17 × C48. The action has order 16. Each pair slot has representative phase `j` in 0..23 and its true inverse `(-3^(-j)x,-j)`. Two additional slots have phase 24 and are reflections. Repeated phases retain independent coordinates. Thus there are seven field coordinates, not seven necessarily distinct group elements; actual element legality is deferred to production.

Common conjugation and scaling have the form

`F_(lambda,t)(x,j)=(lambda*x+(1-3^j)t,j)`.

The anchor is the first component whose action is nontrivial. In particular, phases 0 and 16 cannot be translation anchors. Choosing `t=-x_anchor/(1-3^j_anchor)` sets that coordinate to zero; six coordinates remain. The all-zero anchored vector lies in the order-48 complement and cannot generate an order-816 Cayley graph. Overall nonzero scaling therefore gives `(17^6-1)/16 = 1,508,598` marked projective representatives per mode. We do not quotient by slot permutations, residual stabilizers, or accidental graph isomorphisms.

## The phase-17 automorphism

Define `Phi(x,j)=(x,17j mod48)`. We have `gcd(17,48)=1`, `17^2=1 mod48`, and `3^(17j)=3^j mod17`. Consequently Phi preserves the product and is an involutive group automorphism. It fixes phase 24 and both reflection field coordinates.

For a pair representative `(x,j)`, put `J=17j mod48`. If `J<=23`, the new canonical pair representative is `(x,J)`. If `J>=25`, use its inverse instead: the canonical representative is `(-3^(-j)x,48-J)`. In particular, phase 16 maps to phase 32 and is inverted back to phase 16 with field factor -1. Sort the resulting five canonical phases, retaining stable original-slot indices for repeated phases. This is an invertible monomial transformation of the five pair coordinates; it preserves actual inverse pairs and element legality.

`phase17_mappings.json` records this map for every one of the 16,375 source modes, including target mode, original-to-new slot order, inverse flag, and field factor. Every target exists in the saved survivor list. The program checked the involution on all modes and the full equality

`target_capacity[17*j mod48] = source_capacity[j]`

for all 48 fibers of every mode. `orbits.json` gives the lexicographically least phase tuple in each orbit and identifies every previously checked member. A completed mode excludes its whole orbit. Fixed modes retain their complete field scope; they are not divided by two. The 28 checked modes consist of four fixed modes and twelve two-element orbits, so this automorphism does not transfer closure to any further previously unchecked mode.

## Exact-17 constraints and iteration

For each unsearched orbit representative with an exact-17 fiber, generate all freely reduced words of length at most three with distinct component labels. Their field coordinates are linear forms in the seven original variables. Set only the chosen anchor to zero. Removing that coordinate does not merge forms: under common translation, every form in endpoint phase `h` changes by the same `(1-3^h)t`; the saved original and anchored form counts are also checked to agree.

If a fiber consists of exactly 17 distinct restricted forms and covers F17 at a candidate assignment, its 17 values must be a permutation of F17. Their sum is zero. Thus the sum of **all** 17 coefficient vectors gives a necessary homogeneous linear equation. No 17-element subset of a larger fiber is used.

Stack the equations from every currently exact-17 fiber and compute their kernel by modular Gaussian elimination. Compose this kernel basis with the existing basis, restrict every fiber, and deduplicate all restricted forms. If any fiber has fewer than 17 forms, reject the entire mode. Otherwise repeat on all newly exact-17 fibers until no new nonzero equation occurs. Each nontrivial iteration decreases the dimension, so there are at most six strict decreases. `tight_results.jsonl` preserves each actual matrix, RREF, rank, kernel basis, composed basis, counts, and any deficient-fiber witness. The implementation also checks that iterative projection agrees with direct projection from the original anchored forms.

This closure is invariant under Phi and reanchoring. Phi gives an invertible coordinate map and a fiber permutation. Reanchoring adds a common endpoint-dependent linear shift to every form in a fiber; summing 17 forms annihilates that shift in characteristic 17. Hence processing one representative supplies a valid necessary reduction for its entire explicitly listed orbit.

For a surviving basis B with d rows and six columns, restore the anchored coordinates by `X_j=sum_k z_k B[k][j] mod17`, then insert zero at the saved anchor. Normalize **only z** by setting its first nonzero entry to 1. Original field coordinates need not have first nonzero entry 1. The remaining marked scope is `(17^d-1)/16`. Full original generator distinctness remains mandatory in subsequent production.

## Read and write scope

Inputs read: `../survivors.jsonl`, `../maximin_production/inputs.json`, and `../maximin_production/terminal.json`. Arithmetic helpers reused: `../../axis_cayley272/symbolic_affine_words.py` and the pure kernel/projection functions in `../fourpair_tight/linear.py`; importing the latter does not execute its old run. New results are confined to this directory. Preprocessing enumerates no field assignments, constructs no graphs, and runs no BFS. Subsequent separately authorized production is recorded in `reduced_production/`.
