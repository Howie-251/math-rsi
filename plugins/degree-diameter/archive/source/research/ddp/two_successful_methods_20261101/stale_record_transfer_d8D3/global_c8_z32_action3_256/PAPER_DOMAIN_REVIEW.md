# Fixed C8 acting on Z32 by3: complete parameter domain and interpretation

This paper performs no word generation, parameter enumeration, group/field validation, cover computation, graph, BFS, solver, Lean or external review. The actual finite result belongs to the separate numeric owner. Z32 is an additive cyclic group/ring here, not a finite field, and no field-transfer theorem is invoked.

## Fixed group and inverse generators

Use the RIGHT law

(x,y)*(a,b)=(x+a mod8,y*3^a+b mod32).

The action is well-defined because3 has order8 modulo32. The four positive phases are fixed at1,2,3,4, with normal parameters b0,b1,b2,b3. Each named inverse has phase−a and normal−b*3^(-a), not merely negated normal. The eight named generator codes are the four positives and these literal inverses.

Only the phase-four positive and inverse can coincide: its square has phase0 and normal(3^4+1)*b3=18*b3. Since gcd(18,32)=2, it is an involution exactly when b3=0 or16. Those cases have actual simple degree7, all others degree8. No generator is the identity because all positive phases are nonzero. Degree7 cases are valid at a maximum-degree8 target and must not be discarded.

The457 named reduced words of length≤3 may include additional actual backtracks when the phase-four pair coincides, but their endpoint union remains the exact radius-three set. Every listed word is a genuine walk. Conversely any walk can be written in the named generator codes and adjacent named inverse pairs can be erased to enter the list. Extra aliases only duplicate already reachable elements; they do not create false endpoints. Hence named-code reduction is sound for degree7 as well as degree8.

## Complete common-unit normalization

For every odd unit u modulo32, (x,y)↦(x,u*y) is a group automorphism and sends all four normals to u*b_i. It commutes with the fixed action and the true inverse formulas, and gives an isomorphism of the corresponding undirected Cayley graphs.

If all normals were even, every generated normal coordinate would remain even, so the graph would be disconnected. Every connected tuple therefore has a first odd coordinate b_k. There is a unique odd unit b_k^(-1) making it1; earlier coordinates remain even. This is an exact orbit representative for the common-unit action, whose stabilizer is trivial when an odd coordinate exists.

The four first-odd positions give respectively

32^3, 16*32^2, 16^2*32, 16^3

representatives, totaling61440. This covers all connected tuples without claiming to remove all possible graph isomorphisms.

## Connectivity: parity mismatch is necessary and sufficient

Let g0 have phase1 and normal b0, and let K be the generated subgroup. Its phase projection is already all of C8. The parity character

chi(x,y)=y−(x mod2)*(b0 mod2) in C2

is a homomorphism because3 is odd and the phase wrap8 is even. If every b_i has parity a_i*b0, all generators lie in its proper kernel, so K is not the whole group.

Conversely, if b_i−a_i*b0 is odd for some i, the element g_i*g0^(-a_i) lies in K, has phase0 and odd normal parity. Any odd element generates the full additive Z32 subgroup. Thus K contains that normal subgroup and has full phase projection, so K is the entire semidirect product. This proves the claimed iff, not just a necessary quotient condition.

Among normalized non-all-even tuples, the only aligned pattern is b0 odd,b1 even,b2 odd,b3 even. Its first coordinate is already1 and the other three parity-restricted coordinates each have16 choices, giving4096 disconnected representatives. Therefore57344 normalized representatives are connected. Representatives whose first odd index is later are automatically mismatched and connected.

## Degree counts within the complete connected domain

For b3 in{0,16}, the first odd coordinate cannot be index3. The normalized degree-seven count before the parity exclusion is

2*32^2 +16*2*32 +16^2*2=3584.

Of these,16*16*2=512 have the aligned disconnected pattern. Thus connected degree-seven representatives number3072, and the other54272 of57344 have degree8. Common odd-unit scaling preserves b3=0/16, so this degree split is consistent with normalization. These are paper counts, not a second enumeration.

## Actual finite closure and what failed

The owner's `RESULT.json` reports457 raw named words and distinct coefficient-form counts per phase

[63,58,58,58,46,58,58,58].

Every phase passes the raw/form capacity bound32. The complete actual evaluation covers all57344 connected normalized tuples, including3072 degree7 and54272 degree8 cases, with no time-cap stop and no full hit. Unnormalized connected tuples are transported to this complete domain by the proved common-unit automorphism; disconnected tuples cannot satisfy a finite diameter target.

Crucially, every individual phase can cover all32 normal values for some actual tuple. The numbers of such tuples are[320,448,1344,672,256,672,1344,448]. Thus neither raw shortage, distinct-form shortage nor an impossible isolated phase explains the negative result. The same four normal parameters must satisfy all phase endpoint images simultaneously, and none does.

The owner's later read-only `COMPATIBILITY.json` sharpens this interpretation without new parameter evaluations: phases0 and2 already have empty simultaneous-full set, while each has individual witnesses. Its first phase0-full tuple is[1,1,2,23] and its first phase2-full tuple is[1,0,2,10]. This is a concrete shared-parameter incompatibility, not a claim that either tuple is globally viable. The main complete gate cost is2.080238239/20CPU seconds; the recorded postprocess brings the case to2.274279767/20. This paper does not recompute either result.

## Short return words and shared actual forms

For a fixed tuple, reversing a word and taking inverse generators carries phase j endpoints y to phase−j endpoints−3^(-j)*y. This is a bijection of the normal residues, so opposite phases have equal actual cover sizes for that same tuple. It does not permit choosing independent parameter values for the two phases. In particular the numerical negative is a compatibility statement among the self-inverse phases0/4 and phases1/2/3 with their inverse partners.

Phase0 consists of short closed phase words and its image is closed under negation. The empty word supplies0; covering all Z32 also requires a nonempty short-return form to evaluate to16. Phase4 is fixed by phase inversion with normal map y↦−3^(-4)*y=15*y and must cover its two involutory residues0 and16 as well as the other values. These are real constraints on the same saved linear forms and the same b tuple. They are not independent per-phase choices or a field rank condition; Z32 has zero divisors.

The actual phase0/phase2 incompatibility is already enough for this fixed-family negative. If a shorter human explanation is desired, the precise remaining paper question is whether identities among their saved short-word forms force a missing phase2 residue whenever phase0 covers32. That question is not executed here, does not change the accepted finite NO and authorizes no second phase/action/group, parameter seed, graph, Lean or paid review.

## Exact scope

The complete NO is for this fixed group C8 semidirect Z32 with action3, fixed four positive phases1/2/3/4, arbitrary four normal residues, common true inverse edges and maximum degree≤8. It includes connected degree7 cases. It is not an exclusion of arbitrary generators, another phase pattern/action/group, general256-vertex Cayley graphs or general(8,3) graphs. No new graph, parameter or Lean instance is counted. This line stops at the actual finite closure and its shared-parameter explanation.


## Actual enumerator read (no execution)

The reviewer read `gate.cpp` after the paper was saved. Named darts are paired by `last^1`; each inverse uses phase−a and coefficient−3^(−a) on the same normal parameter. Appending a RIGHT dart multiplies the current four coefficient entries by3^a and adds that dart coefficient, exactly matching the group law. The recursion emits the empty word and every named-inverse-reduced word through length3. For degree7 tuples the coincident phase-four codes may add redundant walks but cannot add a false endpoint or omit a reachable one, as proved above.

All eight phase images are evaluated for every retained tuple even after recording its first failure. Therefore the saved per-phase columns and the subsequent compatibility intersection are complete, not censored by an early-failure shortcut. Identity reachability of every one of the256 group elements within3 is equivalent to global D≤3 by left Cayley translation. The first-odd loops and parity exclusion match the proved domain. This was a source read only; no word, parameter or array was re-evaluated.
