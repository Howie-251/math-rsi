> Current closure: the higher-helper-degree argument in `HIGHER_DEGREE_CLOSURE_NOTE.md` closes the full fixed-host all-old-edges-retained family, including arbitrary additional old–old edges. The min3-open checkpoint below is historical and is preserved verbatim.

# Cross-class old-edge tradeoff: independent paper review

This note enlarges the previously accepted fixed-old-induced 715 scope. All old edges stay; new old–old edges may join different eligible P3 classes; the 520 old core vertices remain saturated. Arbitrary finite helper graphs and helper–old spokes are allowed, with maximum degree 11 and required diameter at most 3. The direct literal-715 class/core and Steiner moment inputs are inherited from `../CORE_SUPPORT_RESULT.json` and the accepted arbitrary-helper note. No old source or core check was repeated.

## Exhaustive route accounting

Choose a helper h of minimum helper-graph degree r and put a=11-r. Let b be the total number of old spokes incident to its r helper neighbors. Thus b≤ra. Write d for the number of distinct classes among h's own pins and c for incidences of new old–old edges at those pins. Core targets can be reached only through an own pin and at most two old steps, or through a helper neighbor and its pin followed by a core edge. A core vertex cannot receive a new edge. Therefore the inherited number K(d) of core-missed owner classes must satisfy K(d)≤b+c.

For d≤7, K(d)≥65-d; K(8)≥28 and K(9)≥23 are the inherited moment bounds. The same identity gives K(10)≥22 and K(11)≥15: outside-owner moment sums are at least 195 and 220 respectively. An eight-entry multiplicity partition of total 10 has value sum(C2-C3)≤6 and a fully covered owner has value≤2; at total 11 these bounds are 7 and 3. Hence 195≤2·55+4K(10) and 220≤3·54+4K(11). These are paper consequences of the existing design, not new source computations.

They exclude r=0,1 and r≥4 immediately: their available b+c is at most 11, 20, and (r+1)(11-r)≤36 respectively. For r=2,3 they force exactly a distinct own-class pins: a=9 or 8.

The potential missed route is h–ownpin–original P3 neighbor–new old–old edge. It must be included. Let z count own center pins, s count additional helper incidences at own pins, and u count unused leaf slots. A center pin has no residual slot; a leaf has one after its h spoke, so c+s+u=a-z. The following upper bound covers every eligible old endpoint of every walk of length≤3:

- own old-only class routes: 3a;
- first helper neighbor, then a pin and at most one old edge: 3b;
- two helper edges, then a pin: a(10r-b), omitting the return to h;
- an own-pin cross edge followed by at most one old edge: 3c;
- reentry through an own pin into another helper: (a-1)s, as its shared pin is already counted;
- an original P3 edge followed by a cross edge: a+3z.

The closed eligible neighborhood of a pin already incident to a helper is at most three, even after cross edges: a center has its two leaves and no spare slot; a leaf has its center and at most one extra old neighbor. Likewise a cross-edge endpoint has at most two other old eligible neighbors. This includes F–F–F, shared-pin helper reentry and center-to-two-leaf cross routes; no single-owner assumption is used.

The resulting capacity is

E≤3a+3b+a(10r-b)+3c+(a-1)s+a+3z.

For r=2, with δ=b+c-23≥0, this is at most 159-6δ-6z-s-9u≤159<195. Thus minimum helper degree two is strictly impossible in the enlarged scope.

For r=3, with δ=b+c-28≥0, it is at most 196-5δ-5z-s-8u. Covering all 195 eligible vertices requires δ=z=u=0 and s≤1. The only scalar possibilities are (b,c,s)=(20,8,0) or (21,7,1). All eight own pins must be leaves in distinct classes; all their spare slots are used. The first case permits at most one unit of total overlap in all counted routes; the second permits none. In particular the neighbors' helper degrees must total 13 or 12: otherwise the two-helper-step bound loses at least eight units. A purely cubic helper graph or a cycle cannot realize these necessary cases.

## Result and boundary

The proposed broad route bound is supported, with the original-P3-neighbor cross-edge routes explicitly charged. Any surviving construction in this fixed-old-edge cross-class scope must have minimum helper degree three and the extreme local parameters above. This is not an impossibility proof for minimum degree three, not an existence claim, and not a prohibition on deleting/replacing old edges or changing source. No helper graph was enumerated and no graph was generated.

`RESULT.json` records only the small integer budget check (0.022236 CPU seconds); all graph/design inputs were inherited. The 5 CPU budget was not approached. The paper review stops here so the new 16416 concrete Lean task can proceed.


## Same-node final closure

See [HIGHER_DEGREE_CLOSURE_NOTE.md](HIGHER_DEGREE_CLOSURE_NOTE.md). The new argument excludes all helper degrees4..7, while min degree3 would require neighbor-degree sum12 or13; the remaining degrees{3,8,9,10,11} cannot supply that sum. Thus arbitrary new old–old, new–old and new–new edges do not permit a nonempty finite augmentation if all edges of the fixed715 source are retained. This supersedes only the earlier open boundary, not its intermediate calculations.
