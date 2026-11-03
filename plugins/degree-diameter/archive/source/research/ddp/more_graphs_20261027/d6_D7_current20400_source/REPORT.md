# Current (6,7) 20400: Cayley source known, generator recipe still missing

The current official diameter-7 entry is Rithwik Gupta's20400graph,
dated September8,2026. It is not the former20319graph found by
Comellas, whose semidirect-product coordinates and generators are
explicitly given in the next, historical entry. The current entry
says its search details are forthcoming. The unique Wiki lookup found
no exact20400source recovery or previously closed transfer scope.

The current primary page is
[the official D7 description](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g7.html#67).
Its linked
[20400 Sage script](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD7/20400_d6D7_SageMath.txt)
reports order20400,size61200,6-regularity,diameter7,girth9, and
automorphism-group order20400 with a Cayley/vertex-transitive graph.
It reports automorphism structure

    (C5 x C5) : (C3 : (C17 : C16)), center order1.

The line's printed label is incorrectly hardcoded as deg16D4, but
the actual code defines Adeg6D7=deg6D7.automorphism_group() and prints
that variable's structure and center. Thus the label typo is recorded
rather than silently assigning this to a different graph. These are
the primary script's reported properties; they were not independently
recomputed in this source stage.

The factorization20400=5*4080 did not identify its group. In particular
PSL(2,16) x C5 has a central subgroup of order5, inconsistent with the
reported center1. That initial guess is refuted by the primary
reported group invariant. No generator list was invented from the
factorization or the abstract group structure.

The supposed small Sage file is actually170269bytes and embeds a
sparse6graph literal before generic property computations. It was
saved as 20400_d6D7_SageMath.author.txt, but the encoded graph was not
decoded, parsed, executed, or subjected to BFS/automorphism computation.
No separate20400vertex edge list was downloaded. Crucially, the script
does not specify a group presentation/action matrices with a bound
normal form, nor the three inverse-pair Cayley generators. Its
automorphism report alone is not a complete algebraic graph recipe.

The exact missing input is either a representation of the reported
group together with the six directed generators, or a regular
automorphism action with identity/neighbor binding from which those
generators can be recovered. Without that binding, replacing17,
changing the vector field, or preserving a generator phase pattern
would be speculation. Relations, valence and connectedness cannot
yet be transferred from an unspecified generator set.

This bounded source task stops at that concrete recipe gap. It does
not substitute the former20319recipe, scan other groups or parameters,
claim a failure of the20400family, or generate a candidate. Current
D7 is inherited, not reverified. PREDICTION.json preserves the initial
guess; RESULT.json separates primary reported facts from uncomputed
algebraic data. No shared Wiki, HTML, source graph or unrelated
4D9task was modified.
