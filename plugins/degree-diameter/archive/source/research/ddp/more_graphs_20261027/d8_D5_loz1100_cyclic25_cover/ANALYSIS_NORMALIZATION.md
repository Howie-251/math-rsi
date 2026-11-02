# Complete normalization of the fixed Loz1100 cyclic-normal lifts

The previously verified source is documented in `../d4_source_transfer/REPORT.md`. Its canonical RIGHT law is

`(j,n)(k,m)=(j+k,n*2^k+m)` on `C20 semidirect Z55`,

with four positive phase/normal pairs `(1,0),(12,33),(11,1),(16,19)`. The source diameter4 is inherited; its old field61 and CRT D4 transfer experiments are not rerun here.

Replace only the normal modulus by275=11*25 and keep literal action2. The identity `2^20-1=1048575=275*3813` makes this a valid C20 action. It has exact order20 (already modulo25), so the target group has order5500. The projection `(j,n mod275)->(j,n mod55)` is a surjective group homomorphism with kernel `{(0,55k):k in F5}` of order5. The kernel is not asserted central: the phase generator acts on it by multiplication2 modulo5. Thus this is a five-sheet ordinary cover with a cyclic25 normal factor, not a25-sheet cover.

## All source-preserving lifts and their gauge

Fix the four directed source representatives and their phases. Every lift is

`(1,55k1),(12,33+55k2),(11,1+55k3),(16,19+55k4)`,

where each ki is modulo5. This gives625 ordered lifts. All reverse darts are their true group inverses; they are not extra variables.

Under the RIGHT law, conjugation by `(0,c)` changes a normal coordinate to `n+(2^j-1)c`. Choose the kernel value `c=55t`. This induces the identity on the source modulo55. For j1=1 the first coordinate becomes `55(k1+t)`, so the unique choice `t=-k1` kills it.

Next multiply every normal coordinate by `u=1+55s`. All five such u are units modulo275, induce the identity modulo55, and commute with the action2. They therefore give source-preserving group automorphisms and keep the first normal coordinate zero. The third coordinate has the form `1+55k`; multiplying it gives `1+55(k+s)` because55^2 is divisible by275. The unique `s=-k` makes the third normal coordinate exactly1. There is no nonunit gap: every third lift is1 modulo55 and hence a unit modulo275.

The two remaining coordinates run freely through their original residue classes. Consequently the complete normalized list is

`(1,0),(12,33+55s),(11,1),(16,19+55t)`, `s,t in F5`,

with25 representatives. The normalization is exact for every one of the625 lifts. A source-preserving kernel conjugation/scaling that fixes both the normalized first and third coordinates is the identity, so no residual choice is missing. This is a covering list under the specified gauge, not a claim that all25 graphs are pairwise nonisomorphic under other automorphisms. It does not classify arbitrary degree-eight generating sets of the group or arbitrary five-sheet edge-local covers.

## True inverses, degree and connectivity

The true inverse is `(-j,-n*2^(-j))`. In the same generator order the normalized inverses are

`(19,0)`, `(8,77+220s mod275)`, `(9,38)`, `(4,246-55t mod275)`.

All eight phases `[1,12,11,16,19,8,9,4]` are distinct and nonzero. Thus every normalized recipe is simple and8regular, with5500 vertices and22000 edges if generated. Projection maps these eight darts bijectively to the eight source darts, proving the ordinary-cover claim.

Let g1=(1,0) and g3=(11,1). The word `g1^-11*g3=(0,1)` supplies the pure unit normal generator. Together with g1 it generates the full target group, so every case is connected without a BFS. This generation word is not a diameter-five certificate.

## Two complementary lifted five-cycles cover each own fibre

A useful source-specific consequence holds uniformly in all25 cases. The geometric sums for the phase12 and phase16 generators satisfy

`sum_{i=0}^4 2^(12i)=sum_{i=0}^4 2^(16i)=55 mod275`.

For either sum the residue modulo11 is zero; modulo25 the respective ratios are21=1+20 and11=1+10, each giving sum5. CRT gives55. Hence

`g2^5=(0,165)=(0,55*3)`, `g4^5=(0,220)=(0,55*4)`.

Their inverse fifth powers give `(0,55*2)` and `(0,55)`. Along with identity these are all five kernel elements, each reachable in at most five steps. Thus every source fibre is internally covered from each of its lifts within five steps, independently of s,t. This is genuine complementarity of two old source five-cycles after the cyclic25 enlargement. It does not bound distances between different fibres: neither source diameter4 nor this own-fibre fact proves full diameter5.

This note uses only symbolic group/gauge arguments and the cited existing source. No new word enumeration, target case, source/new graph, BFS or solver was run. The25-case numerical producer remains separate and must test complete target coverage. The closed older D4 prime/CRT scopes do not decide this new D5/mod275 family.
