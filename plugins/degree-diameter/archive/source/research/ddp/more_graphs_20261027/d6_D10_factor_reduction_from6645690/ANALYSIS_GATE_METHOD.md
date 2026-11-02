# Core-route gates and the actual old seed

This is a paper-only analysis. It does not execute a core traversal, word enumeration, parameter evaluation, candidate graph, solver, or BFS. The original [NOT_EXECUTED proposal](ROOT_QUESTION_NOT_EXECUTED.md) is unchanged. In particular, the factorization of current6645690 is not a recovered group recipe.

## Source binding and the revised conditional question

The current6645690 recipe remains unbound. The actual available author recipe is the older6641680 graph, in [construction.json](../d7_D10_current6645690_source/old6641680_primary/construction.json), [README.md](../d7_D10_current6645690_source/old6641680_primary/README.md), and [verification.txt](../d7_D10_current6645690_source/old6641680_primary/verification.txt). Its primary JSON is https://raw.githubusercontent.com/f4t4nt/degree-diameter-graphs/main/graphs/deg7/dia10/construction.json . No large source edge file is needed for this analysis.

The actual source uses the LEFT law (n,I)(m,J)=(n+4400^I*m,I+J), with normal83021=61*1361 and phase80. Its three positive normal/phase pairs are (4907,38),(21040,3),(63695,58), and its involution is (74603,40). The source agent's [small arithmetic receipt](../d7_D10_current6645690_source/OLD6641680_ARITHMETIC.json) gives actor8 of order20 on F61 and actor317 of order80 on F1361; the positive CRT normals are (27,824),(56,625),(11,1089), and the involution CRT normal is (0,1109). These source constants are inherited, not recomputed here. Source D10 is author-reported and is not reverified.

The revised controlled model keeps the complete F1361 component and phase80, replaces only F61 by F13, and permits all small-component positive normals. Its order would be80*1361*13=1415440. The two separate questions are:

* Three inverse pairs, omit h: maximum degree6, target D10.
* The same three pairs plus the source-projected h: maximum degree7, target D9.

Their quotient connection rules and distance radii differ, so their gates and outcomes must remain separate. The parent has paused any225-setting graph batch in favor of smaller degree/diameter questions; the normalization below is saved as mathematics, not an executed or failed search.

## The unchanged core is an exact necessary gate

For the actual old seed, put Q=F1361 semidirect_317 C80, of order108880. Its positive normal/phase pairs are (824,38),(625,3),(1089,58), and h_Q=(1109,40). The latter must not be replaced by (0,40): only the small component is being changed.

Each proposed target G has a homomorphism pi:G->Q whose kernel is F13. The target connection letters project to these same literal core letters. Consequently, every target path of length at most D projects to a core path of length at most D. One absent core endpoint therefore rejects every13-fold target having this projection, regardless of small actor or small normals. Source D10 does not establish either the no-h core R10 condition or the with-h core R9 condition. At most it establishes the with-h core R10 condition.

The same statement would apply to an11-fold target of the initially proposed current source, if that source and its fixed core were actually recovered. Here the actual seed requires13 lifts, not11; the threshold must change with the kernel order.

## Exact short-word multiplicity gate

Use the six actual positive/negative letters, and optionally h, with an explicit true inverse-letter map. For a core endpoint q, let W_D(q) be all freely reduced words of lengths0 through D that evaluate to q in Q. Every shortest target path is represented in this set. A word has one target endpoint, so at most |W_D(q)| distinct vertices in the fibre pi^-1(q) are reachable within D steps. Hence

    |W_D(q)| < 13

strictly rejects all13-fold targets with this fixed projected connection rule. A count of zero is the preceding missing-core gate. A count at least13 is only a necessary condition and does not establish a full target fibre, much less the full graph diameter.

No new large graph is required to compute this bound. A possible exact implementation keeps counts indexed by (core endpoint,last letter), and advances only to letters other than the true inverse of the previous letter. Accumulate all lengths0..D. Counts may be saturated at13: this preserves exactly whether the final count is less than13. Such a single small-core computation simultaneously detects absent endpoints and thin fibres.

The count must concern labelled target letters. One must not merge projected letters or cancel additional projected relations merely because two words have the same core endpoint: their kernel translations can differ. In this actual seed, the six phases38,3,58,42,77,22 and optional40 are distinct, so immediate inverse labels are unambiguous. General projected loops or collisions would still require retaining their original labels.

In particular, do not divide the word count by two just because q is an involution in Q. All legal F13 actions here satisfy a^40=1. The lifts of h_Q with small normal t have square small normal2t; only t=0 is an involution. Word and inverse can therefore reach different small-component values. The involution-fibre collapse used for a different action with a^j=-1 does not transfer here.

If raw multiplicities do not reject the model, a stronger optional gate is still independent of graph generation: for a fixed small actor, express the small endpoint of each word as a linear form in the free positive normals, using true inverse normals. Equal coefficient forms necessarily alias for every parameter choice. Fewer than13 distinct coefficient forms for a core endpoint uniformly rejects that actor's complete normal family. A full set of at least13 forms remains insufficient. This is a proposed method only; no forms are generated or evaluated here.

## Complete small-normal normalization:225 representatives per rule

The new small actor must satisfy a^80=1 in F13*. Because F13* has order12, a has order dividing4. The four legal actors are1,-1,5,-5, of orders1,2,4,4. This deliberately changes the old F61 action of order20; it is not an embedding preserving the old small-coordinate routes.

Write target elements as (z,t,j), where z is in F1361, t is in F13, and j is modulo80. The LEFT law is

    (z,t,j)*(w,s,k) = (z+317^j*w, t+a^j*s, j+k).

The true inverse is (-317^(-j)z,-a^(-j)t,-j). In particular, old inverse normal numbers must not be transplanted into F13.

Since a^40=1, an order-two element above h_Q must have small normal t satisfying2t=0. Thus t=0 is forced. The actual source h already has small normal0, but its large normal1109 remains. Small-component conjugation does not change h.

For a nontrivial actor, choose the first positive phase j_l with a^j_l!=1. Conjugating by a pure small translation c changes b_i to b_i+(1-a^j_i)c, uniquely setting b_l=0. Small-component scaling by F13* then identifies the remaining two normals up to a common nonzero scalar. Their all-zero tuple cannot generate F13. The complete nonzero classes are P1(F13): (1,t) for all13 values t and (0,1), giving14 representatives. For a=-1, the pivot is phase3 (pair index1). For a=5 or-5, the pivot is phase38 (pair index0). No further phase or core automorphism reduction is assumed.

For a=1, conjugation has no effect on small normals. Common nonzero scaling of the three normals gives P2(F13): (1,s,t), (0,1,t), and (0,0,1), for169+13+1=183 representatives. Exclude only the all-zero tuple, which has no small-component generation.

Thus there are3*14+183=225 normal forms for each connection rule. They are complete for the explicitly fixed large projection and these four actors under small translation and scaling. This is not a claim about arbitrary Cayley sets, different large projections, phase sets, fields, or groups.

## Conditional connectivity proof

The remaining common condition is that the relevant core connection set generates Q. The core gate supplies this if it reaches every core vertex. Omitting h cannot inherit this condition merely from source connectedness; a retained phase3 generates the phase quotient but does not alone prove generation of the large normal subgroup.

Assume onto Q. For a nontrivial actor in the normalized family, the pivot has small normal0 and nontrivial actor, while some other positive normal is nonzero. Their commutator has phase0 and a nonzero small normal. Raising it to the1361st power kills its large normal and retains a nonzero F13 normal, since13 does not divide1361. It therefore generates all of the pure F13 kernel. Together with the onto core projection, this proves connectedness.

For a=1, choose a generator with nonzero small normal b. Its108880th power has identity core projection and small normal108880*b!=0, since13 does not divide108880. Again the full kernel and onto core prove connectedness. These arguments apply with or without h.

The six positive/negative phases and optional40 are distinct and nonzero. Hence every normalized setting is simple with the intended degree6 or7. Connectedness is conditional on its own core rule, as above. A finite Cayley graph then needs only a complete identity-root distance computation to establish its global diameter; a truncated radius failure does not supply an exact larger diameter or ordinary bad-pair count.

## Terminal scope of this paper task

The group, normalization, and gates above are paper-valid. The parent subsequently supplied the two completed small-core gates: [without h at radius10](core_from_old6641680/degree6_D10_remove_h.json) has core diameter9 and minimum raw multiplicity67; [with h at radius9](core_from_old6641680/degree7_D9_keep_h.json) has core diameter8 and minimum raw multiplicity81. Both reach all108880 core states and have zero slots below13. Thus these two particular necessary gates pass and do not refute the target family. These results were produced outside this paper task and are cited without rerunning them.

No225-parameter target family was run, and no positive or negative target-graph result is asserted. The target family remains NOT EXECUTED, rather than failed or UNKNOWN from an attempted batch. There is no new research row, source BFS, target graph, solver, embedding sweep, or external review from this analysis.
