# Full independent free-port cover: both single calls UNKNOWN

This is the first SAT model on all648 individual free pins of the15552/D4 source and all810 individual free pins of the102060/D5 source. Every original target is constrained:15552 and102060 unique support rows respectively. No target-inversion folding was used. Each pin is independent and the only degree budget is at most15 selected pins.

Source inversion supplies a valid WLOG choice between S and its reflected set. Nonfixed pin pairs are ordered by their smaller label; at the first pair whose selections differ, the smaller-label pin is selected. Five-clause prefix equivalences track preceding equality. Zero/fixed pins are not tied or folded. The final equal-prefix variable is forced false to exclude the already tested invariant subdomain. This extra cut depends on the two previous full-inversion rawUNSAT results, which have no independently checked proof logs; it is not an unconditional mathematical axiom. The asymmetric subdomain itself is represented completely up to the proved source automorphism.

Degree15/D4 model:648 selector variables,312 reflected pairs,313 lex-prefix variables,11329 total variables and38132 clauses. It contains1496880 cover literals and all15552 target rows. One CaDiCaL call requested60seconds and returned UNKNOWN/code0 at59.902467 childCPU seconds, without a model.

Degree15/D5 model:810 selector variables,390 reflected pairs,391 lex-prefix variables,14161 total variables and130292 clauses. It contains19735110 cover literals and all102060 target rows. Its one60second call also returned UNKNOWN/code0 at60.032781 childCPU seconds, without a model.

The producer used the original cached R3/R4 balls, actual all-free cache labels and the scout's complete direction interface. It generated no new ball and performed no old-source diameter BFS. If SAT had returned, decoded pins would have had to pass all target clauses, explicit full-n cached-ball union, actual selected old degrees and complete retained-edge export. No candidate reached that stage, so there is no new graph or exact diameter/bad-pair measurement.

Aggregate producerCPU127.968020737seconds includes both solver children, preparation and the carried direction-interface cost0.063390872, within160. Parent preparation was below25CPU. PIDs1425008/1444069 and session27336 are terminal. Each source received exactly one new full-domain call; original MILPUNKNOWN and old72/90-pinSAT histories were not rerun or overwritten. No seed, timer continuation or third domain is appended here.

Both asymmetric questions remain unresolved. Combining invariantUNSAT with asymmetricUNKNOWN does not exclude the unrestricted single-vertex extension family. The separate bounded affine-line sufficient-certificate experiment can therefore remain meaningful; this producer did not stop it or run its models. Stop this batch without spending its remaining budget on a second call.
