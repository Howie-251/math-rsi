# Four-pair tight-fiber branch: preserved finite scope

The scope is exactly the twelve capacity-surviving degree-12 modes with four non-involution inverse pairs and four reflections in `F17 semidirect_3 C48`. Multiplication is `(x,j)(y,k)=(x+3^j*y mod17,j+k mod48)`. The action has order 16, so nonzero phase is not by itself a valid translation anchor: phases 0,16,32 have trivial action. The code selects a component with `3^j != 1`. In all twelve actual modes this is the first pair component.

The four reflection components have phase 24, where the action is −1. Every pair representative and every reflection has its own field variable, for eight variables before gauge. Common affine automorphisms are

`F_(lambda,t)(x,j)=(lambda*x+(1−3^j)*t,j)`.

Translate the selected nontrivial-action component to field zero. The remaining vector has seven coordinates. No legal possible solution is lost by this gauge. For coefficient vectors of a word ending at phase J, the identity `sum_i c_i(1−3^j_i)=1−3^J` also shows that dropping this anchor coordinate cannot merge two different forms with the same endpoint phase.

## Iterated necessary equations

At the current parameter subspace, first deduplicate all coefficient forms separately in each of the 48 endpoint fibers. A fiber with fewer than 17 distinct forms is insufficient for any field assignment. A fiber with exactly 17 forms can cover F17 only when their seventeen actual values are a permutation of F17. Therefore their sum equals `sum_{a in F17}a=0`, and the sum of the seventeen coefficient vectors gives a homogeneous linear equation.

This argument uses the entire set of exactly seventeen distinct forms. It does not choose an arbitrary seventeen-element subset of a larger fiber. All such tight fibers supply equations simultaneously.

Row-reduce their coefficient-sum matrix over F17. Let K be a basis of its kernel in the current coordinates. Restrict every fiber form to K, deduplicate again, and compose K with the previous basis to retain an exact map to the original seven anchored field coordinates. New fibers of size exactly seventeen are treated at the next iteration. A positive-rank step strictly lowers dimension; at most seven such steps are possible. Stop only when a deficient fiber appears or all tight-fiber sum equations have rank zero.

Every restriction is necessary for D3, so this iteration preserves all possible solutions. `patterns.json` saves each current-coordinate matrix, RREF, pivots, kernel basis, composed basis, counts before/after, and deficient-fiber witnesses.

## Actual closure result and normalized enumeration

All twelve first steps have rank one, dropping dimension from seven to six. Ten modes are then stable: all remaining tight-fiber sum equations vanish identically on their six-dimensional subspaces. Modes `[1,9,11,15]` and `[5,9,15,17]` acquire new tight fibers 21 and 27; a second rank-one step drops them to dimension five, after which the minimum fiber capacity is 12. They are rejected without field production.

For every surviving mode, the saved 6x7 basis B reconstructs the original anchored fields by `X=sum_k z_k*B_k`. The zero z cannot generate translations and lies in the 48-element complement, so it cannot give a connected 816-vertex Cayley graph. All equations are homogeneous and common nonzero scaling is an automorphism. Normalize **only the first nonzero z-coordinate to one** and enumerate all later coordinates in F17. Thus each surviving mode has

`(17^6−1)/16 = 1,508,598`

marked inputs, and the ten-mode actual range is **15,085,980**. The original twelve-mode range before these necessary restrictions was `12*(17^7−1)/16=307,754,004`; that number is not the count of assignments actually enumerated.

There is no second leading-one requirement on restored X. The explicit saved calibration has z=`[1,2,3,4,5,6]` and restores fields `[0,14,1,2,3,4,5,6]`, whose first nonzero original coordinate is fourteen. It is retained. Its actual twelve group elements are legal, and direct group multiplication through length three gives exactly the same value sets as the restored forms in all 48 fibers. This is one arithmetic calibration, not a graph or BFS. The C++ engine checks the restoration tuple without repeating the word experiment.

## Exact finite acceptance condition

Every enumerated assignment reconstructs all eight original fields and generates the four genuine inverse pairs plus four phase-24 reflections. The twelve actual group elements must be nonidentity and pairwise distinct. This includes reflection distinctness and, generically, repeated-phase pair collisions; legality is not inferred from dimension counts.

For each legal assignment, the program evaluates the saved restricted linear forms and tests whether every endpoint phase attains all seventeen field values. This is an exact distance-at-most-three coverage test, not the symbolic form-count necessary bound. Fibers are ordered by form count and then phase; no approximate score is used. The first failed fiber proves the candidate is not D3.

Only a candidate passing all 48 exact fibers receives a complete identity-root BFS and a full edge table. Cayley left translation then gives the full graph diameter. In the actual batch no assignment passes even the first tight fiber, so there is no BFS and no diagnostic failure graph. All 15,085,980 inputs are counted, including illegal generator sets.

## Limits

This closes the twelve specified four-pair capacity survivors when combined with the saved necessary restrictions and full actual remainder. It does not assert that other compositions in the 816-element group were processed here. The previously searched maximin modes and the concurrently assigned six-pair remainder were not touched.
