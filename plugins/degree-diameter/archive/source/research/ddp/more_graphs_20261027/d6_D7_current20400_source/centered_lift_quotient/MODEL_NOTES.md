# Centered cyclic-factor transfer: conditional model check

This note precedes the actual recovered48-base recipe. No coordinates are assumed.

Suppose its six directed ports at each basevertex are translations delta=(a,b,c) inF5²×C17, with explicitly paired inverse ports. Choose the unique centered c-hat in{−8,...,8}. Odd modulus17 ensures center(−c)=−center(c), including0. Retain a,b and the base target, and reduce c-hat modulo18 or19.

This defines an undirected regular voltage graph because every reverse dart still has exactly the negative translation. If two old ports at one basevertex have the same target and same a,b, their centeredc difference has magnitude at most16. A collision modulo18 or19 therefore forces that integer difference0 and would already have been an old collision. Other targets or a,b cannot collide. A new loop would require equalbase,a=b=0,c-hat=0 and thus an old loop. A nontrivial same-base port cannot become its own inverse: a or b nonzero has oddorder5, and witha=b=0, modulus18 would require c-hat=9 while|c-hat|≤8; modulus19 has no nonzero2torsion. Consequently a genuinely simple six-port source remains simple degree6 after either replacement.

The deck translations F5²×Cm remain graph automorphisms, acting transitively within each of48 fibers. No action of the old order16 complement on Cm is required: other old automorphisms may be lost. This is a regular voltage-cover parameter replacement, not a Cayley-graph claim or preserved fullautomorphism-group claim. Connectedness must be checked separately. Complete eccentricity≤7 at the48 identity-deck roots would certify diameter≤7 everywhere.

For route capacity, forgetc and retain Q=48base×F5², with1200 states. Keep all six named darts even if this projected graph has loops or parallel edges, and forbid only the explicitly inverse previous dart. The total number of reduced words oflength0..7 is117187 per root. Each such word gives exactly onec endpoint, so every projectedtarget must have at leastm words in a diameter7 lift. A small count is a true necessary obstruction; enough words do not prove coverage. SourceD7 would imply the inheritedm17 projection has at least17 such routes, which is a useful consistency check on actual recovered coordinates.

The assigned task waits for the literal recovered recipe. It does not generate either new graph or run BFS, reconstruct another automorphism, or expand the modulus list. The separate producer owns any actual21600/22800 graph tests.
