# Fixed 1344 source: C3 scope and the unique-route obstruction

## Source and conventions

The primary diameter7 description assigns W1,W2 as the two semi-edges at base0, W3,W4 at base1, and W5,W6 as links from0 to1 with inverse reverse darts. W1..W4 are involutions. W5 has order8 and W6 order6; neither is identity. Only the C3 coordinate of W5 is gauged to zero.

Permutation images use GAP right action: multiplication gW has images W[g[j]]. The earlier opposite-convention run is preserved as PROVISIONAL_WRONG_SOURCE and supplies no obstruction. SOURCE_BINDING_CHECK.json records the corrected source convention and its targeted root0 radius7 calibration. No whole-source all-root BFS was requested or repeated for this proof.

## Restricted central-cover classification and two-root criterion

For the restricted direct-product deck G x C3 rule, a semi-edge voltage (Wi,t) must square to identity. Since Wi^2=identity, 2t=0 in C3 forces t=0. Let the two forward link shifts be t5,t6. Relabeling each base fiber by a constant sheet shift sets t5=0 and leaves delta=t6-t5. Thus delta0 is three disconnected source copies; delta+1 and-1 are isomorphic under sheet negation. There is exactly one nontrivial class in this restricted rule, not a classification of all ordinary covers. Nonzero delta alone is not used as a general connectedness proof.

For any correctly constructed product-deck lift, left multiplication by G x C3 is an automorphism transitive on each base fiber. Complete radius8 coverage from the two identity base representatives therefore proves global diameter at most8, including connectedness. An eccentricity computed only in a component without checking full coverage is insufficient.

## Stronger obstruction, independent of the sheet rule

UNIQUE_ROUTE_CHECK.json independently confirms that, in the corrected source, every nonbacktracking word of length at most8 from (base0,identity) to (base0,g200) is the single word

    W6 W4 W6^-1.

Its base/group-index path is (0,0),(1,6),(1,35),(0,200). The check joins all reduced prefixes of length at most4 from each endpoint, with a fixed split for each total length0..8 and inverse-boundary rejection. Each side has levels1,4,12,36,108. It is a targeted word check, not BFS or another candidate; CPU0.003214067 seconds. It agrees with the complete cached raw count1.

Let pi be any ordinary three-sheet graph cover of this fixed source and fix a vertex above (0,identity). Every walk of length at most8 to the target fiber projects to a source walk of that length. Deleting immediate source backtracks leaves the lifted endpoint unchanged, because local bijectivity forces the lifted inverse edge to return to the preceding vertex. The reduced source walk must therefore be the unique word above. Unique path lifting gives only one possible endpoint in the three-vertex target fiber. The other two vertices cannot be reached within8. Consequently no ordinary three-sheet cover of this fixed source has diameter at most8, whether or not it is connected.

This excludes the central product rule and any proposed sign-twisted C3 rule that is an ordinary cover. It does not exclude branched covers, altered source edges, different sources or arbitrary 4032-vertex graphs. The proposed character recovery and729 coefficient search were stopped before execution; no actual chi values or twisted candidate result are claimed. Numerical global diameter and ordinary unordered bad-pair counts remain uncomputed.
