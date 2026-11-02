# PREDICTION — r6/F9 projective halves

Recorded before the finite classification. This is a new local finite gate, not a new complete graph claim.

## Inherited mathematics

Inherit in full `../general_ports/DERIVATION_PACKAGE.md`, especially its proof that simultaneous full rank of all (r−1)^2 central NB3 turns and coverage by the pure pre/post backtrack pencil forces q=2r−3. The derivation is inherited, not a new claim. Prior work explicitly did not verify r6/q9. The previous C120/F5 controller gate is trianglefree and stopped; this gate does not revive that controller.

## Exact question and falsifiable prediction

Use only PGL₂(F9), with F9=F3[w]/(w²+1), field code a+3b for a+bw. PG(1,9) has ten points. Enumerate the 720 projective linear permutations and their action on all C(10,5)=252 five-subsets. No Frobenius or other semilinear maps are allowed.

Prediction to test, not assumed: there are two orbits, of sizes 72 and 180, and each orbit is invariant under complementation. Consequently every five-subset is projectively equivalent to its complement. The classification must preserve all252 members and explicit linear witnesses, so failure is a concrete subset counterexample rather than a random sample.

For the one fixed port parameter set S=[∞,0,1,2,w,−w] (codes [inf,0,1,2,3,6]), define B_p=S\{p}. If all six B_p are projectively self-complementary, choose the lexicographically first normalized coefficient tuple (a,b,c,d) with f(z)=(az+b)/(cz+d) taking B_p to its complement. Normalize the first nonzero coefficient to1, and order coefficients by integer field code0..8. Construct Q=[[d,c],[b,a]], H_t(x)=(x0,x1−t*x0,x2−t*x1), H_inf(x)=(x2,x0,x1), T_p=H_p^-1 diag(1,Q)H_p.

Prediction: the six positive T_p and six exact negative inverses give300 nonzero central3×3 determinants (12×25), preserve their own port line, and each give ten distinct quotient/plane rays covering all729 vectors by the exact pencil. Positive and negative orientations of each matching use true inverse matrices; T_p²=I is not presumed.

## Execution boundary

One single-worker finite run, CPU hard limit20seconds. Read the saved field multiplication/inverse table in `../../d2_spare_dominating_fill/brown91_cap11_interface/pin_profiles/GEOMETRY.json` and check it against the stated field presentation. No controller search, fiber graph, graph BFS, SAT/solver, Lean, hash, installation, alternative S, field/seed ladder, or new family. On failure save a concrete counterexample and stop the chart gate. No target controller order has been selected and no54-degree D3 graph is claimed.
