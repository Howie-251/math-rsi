# All source-preserving action lifts on Z275

This paper adds to the completed literal-r2 analysis; it does not alter the earlier r2 files or their execution times. The source remains the known Loz1100 graph with RIGHT law `(j,n)(k,m)=(j+k,n*2^k+m)` modulo phase20/normal55 and positives `(1,0),(12,33),(11,1),(16,19)`.

## Exactly five legal action lifts

An action lift inducing the same source projection must satisfy `r=2mod55`. The five residues modulo275 are exactly

`r in {2,57,112,167,222}`.

Each is a unit because it is2mod5 and2mod11. Its order modulo11 is10. Its order modulo25 divides20 and is a multiple of4, since its reduction modulo5 is2 of order4; hence that order is4 or20. The full order modulo275 is therefore `lcm(10,4)=20` or `lcm(10,20)=20`. All five define a legal C20 action, and there is no sixth action residue with the same source reduction. In particular this statement includes an action whose25-component has order4; requiring order20 on that component would incorrectly omit it.

For each r the group law is RIGHT:

`(j,n)(k,m)=(j+k,n*r^k+m)` modulo20/275.

Reduction modulo55 is the fixed source-group homomorphism because r=2mod55.

## The same625-to25 normalization is complete for every r

All source-preserving positive lifts still have normals `55k1,33+55k2,1+55k3,19+55k4`, with all ki modulo5. Kernel conjugation by `(0,55t)` adds `(r^j-1)*55t` to a normal coordinate. For the first phase j=1, `r-1=1mod5`, so its shift is exactly55t modulo275. The unique t=-k1 kills the first normal coordinate for every r.

The normal scalings `u=1+55s` are all units, preserve the source projection, and commute with multiplication by r. They keep the zero first normal coordinate and send `1+55k` to `1+55(k+s)`. Thus the unique s=-k kills the third shift. The third lift is always a unit, independently of r. The remaining two shifts are arbitrary, so the full canonical list for each action is

`(1,0),(12,33+55s),(11,1),(16,19+55t)`, `s,t in F5`.

Consequently there are25 covering representatives per r:125 overall, comprising the already completed25 at r2 and100 additional representatives. This is a completeness statement for all3125 source-preserving raw lifts across the five actions. No arbitrary generating-set or arbitrary edge-local-cover classification is claimed. No isomorphic redundancy between actions has been proved or used to omit a case.

## Inverses, connectivity and own-fibre guarantee are uniform

True inverses must be recomputed for the current r using `(-j,-n*r^(-j))`. In canonical order they are

`(19,0)`, `(8,-r^8*(33+55s))`, `(9,-r^9)`, `(4,-r^4*(19+55t))`,

with normals modulo275. The earlier r2 numerical inverse constants are not universal. The eight phases remain distinct, so every recipe is simple8regular. For all r, `g1^-11*g3=(0,1)`, giving the whole cyclic normal group, and g1 generates the phase group. Thus every canonical case is connected.

The two source-five-cycle geometric sums are still55 modulo275. Modulo11, r=2 makes `r^12` and `r^16` primitive fifth roots, so each sum is0. Modulo25, each ratio is1mod5, say1+5c. Its five-term sum is `5+5c*(0+1+2+3+4)=5mod25`. CRT therefore gives55 in both cases. It follows uniformly that

`g2^5=(0,165)`, `g4^5=(0,220)`.

The inverse fifth powers give110 and55, so all five elements of the cover kernel are within five steps. This supported local guarantee does not imply coverage of other source fibres or global diameter5.

Only paper completeness and group arguments were performed here: zero new target cases, word enumerations, graphs, BFS or solvers. The producer's combined result may inherit the old r2 cases and add the100 remaining cases once, retaining their separate numerical history. No other action reduction, source phase, base graph or normal modulus is added.
