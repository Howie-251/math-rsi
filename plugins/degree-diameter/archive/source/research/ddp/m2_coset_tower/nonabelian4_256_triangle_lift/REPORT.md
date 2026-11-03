# Two prescribed central triangles: completed finite profile

The authorized16-start profile finished without a diameter3 graph. Its best projection has `L=6`, no empty quotient target slots, and six singleton-affine-form slots. No evaluated projection had L=0, so this batch examined no center assignments and saved no new full graph. This closes the specified finite profile only, not the constrained voltage family.

The mathematical change is imposed exactly: `h12=inv(h2)*c*h7` and `h15=inv(h9)*c*h11`. Both named triangle products equal the nonidentity center c. Together they guarantee three-step coverage of every vertex's central mate. The remaining short routes are still insufficient in every projection visited here. `TRIANGLE_LIFT_MATH.md` proves the parameterization and coverage criterion; `SCOPE.md` states the search scope.

## Actual execution

| Quantity | Actual result |
|---|---:|
| Starts completed |16: saved source plus15 fresh |
| Segments completed |144 |
| Complete341-neighbor neighborhoods |599 |
| Accepted strict moves |455 |
| Raw neighbor proposals |204,259 |
| GF2-illegal neighbor projections |19 |
| Legal projection evaluations |204,384 |
| Two-coordinate kick proposals / accepted |128 /128 |
| L=0 projections |0 |
| Center assignments examined |0 |
| New graph expansions / BFS runs |0 /0 |

Legal projection evaluations include16 initial states and128 accepted kicks, as well as204,240 legal neighbors; they are evaluations, not a distinct-projection count. All fresh starts were accepted in15 independent-coordinate draws. Both deterministic random streams used seed20261027091. No phase filter, extra start, restart, or other group was used.

The saved best projection, in the established16-edge order, is

```
[0,29,20,0,23,21,0,18,1,18,14,12,2,8,9,22]
```

It first appeared at evaluation23,632, start1, segment7, step4. `best_projection.json` preserves its score and position. The statement `L=6` means every legal central lift of this projection misses at least six vertices across the four representative roots, hence at least192 unordered pairs in the256-vertex graph. Neither bound was asserted to be attained: no actual center minimum was computed.

## Implementation and source calibration

The copied descent core now has eleven independent projection/center coordinates. Every neighbor and kick recomputes the two dependent projections. Full baseline voltages on the dependent edges are computed in Q64, retaining their high bits. The dependent coefficient masks are18 and320. Equal projected parallel edges use the general affine GF2 legality equation, including both baseline high bits; correlated or inconsistent equations are not treated as independent free-bit choices.

The old832-bad-pair source was exactly restored with eleven-bit center mask198. Its dependent baselines are38=(6,1) and63=(31,1), explicitly exercising the nonzero baseline high bit. All1,024 radius3 distances from its four representative roots matched the saved independent distance matrix. This introduced no BFS and no source-center enumeration. The source projection has L=18, with two empty and14 singleton slots. Every scored projection was also checked to have the constant0 and1 forms in all four self/quotient-identity slots, as required by the prescribed triangles.

`source_parameter_check.json`, `source_calibration.json`, and `first.formal_center.json` preserve these checks. The executable uses the exact short-walk affine route criterion. Center optimization would be performed only at L=0, over the2,048 assignments subject to legality; that branch was never entered in this run.

## Budget and terminal state

The single production process was PID4045620, launched by driver PID4044488 under session48158. It exited normally after all16 starts. Measured production CPU was8.708898 seconds; preparation/compilation CPU was1.675062 seconds; measured driver total was10.386599 CPU seconds and10.400899 wall seconds, within the180-second budget. No process is running and no continuation cursor remains.

`terminal.json` has status `COMPLETE_16_START_PROFILE_NO_D3`, `scope_exhausted=true`, `entire_family_exhausted=false`, and `pending=[]`. No independent final graph check is needed because no new graph was saved. The best artifact is explicitly a projection and lower bound.
