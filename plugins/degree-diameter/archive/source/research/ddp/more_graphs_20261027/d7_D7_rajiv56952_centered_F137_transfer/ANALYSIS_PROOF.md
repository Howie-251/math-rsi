# Arithmetic and route-scope audit: the single F137 transfer

This note independently checks the small group arithmetic. It does not rerun a graph construction, capacity enumeration, or BFS. The sole producer's terminal result is a simple connected 7-regular Cayley graph on 69048 vertices of exact diameter 8. Thus the frozen prediction of diameter at most 7 is refuted for this one control; no larger parameter family is excluded.

## Published source and right multiplication

`SOURCE_RECEIPT.json` records the primary description [Rajiv's degree-7 diameter-7 construction](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g7.html#77). Its seven generator IDs exactly equal the retrieved first adjacency row; this is a source-recipe/first-row binding, not a new verification of all source edges or source diameter.

Write elements as `(x,v)`, where `x` is modulo 24 and `v` modulo M. The law is

`(x,v)(u,w) = (x+u, v*a^u+w)`.

It is associative whenever `a^24=1 mod M`. Identity is `(0,0)` and

`(x,v)^-1 = (-x, -v*a^(-x))`.

For the source, `M=2373=21*113`, `a=44`, with residues `a=2 mod21` of order 6 and `a=44 mod113` of order 8. Hence the action has order 24. Under ID encoding `2373*x+v`, the seven IDs decode to

- `(1,709)`, `(2,831)`, `(7,1272)`;
- their inverses `(23,685)`, `(22,1278)`, `(17,645)`;
- the involution `(12,1428)`.

These inverse identities were checked directly in the stated right law. In particular the source's group convention is not silently replaced by the opposite semidirect-product convention.

## Field-only centering is an actual conjugation

On the field-113 component set

`v' = v + 36*(44^x-1)`.

For any action alpha, the correction satisfies

`(alpha^x-1)*alpha^u + (alpha^u-1) = alpha^(x+u)-1`,

so this is a homomorphism; the negative correction is its inverse. More precisely, under this right law it is conjugation `h*g*h^-1`. To leave the module-21 coordinate unchanged, the full old normal coordinate of h is **714**, characterized by `714=0 mod21`, `714=36 mod113`. Using 36 in the full modulus would not preserve the module-21 coordinates.

Conjugation by `h=(0,714)` gives the three positive source elements

`(1,562), (2,1335), (7,1545)`

and sends the involution to `(12,0)`. Their CRT normal residues are respectively

`(16,-3), (12,-21), (12,-37)` in `Z21 x F113`.

This is an isomorphism of the old group, not an assertion that a field replacement preserves its diameter.

## The single target law and generators

The next prime greater than 113 congruent to 1 modulo 8 is 137: the preceding such integers are 121 and 129, both composite. Trial division through 11 proves primality of 137. The primitive eighth roots in F137, in ascending integer order, are `10,41,96,127`; thus 10 is the specified smallest root. In particular `10^4=-1` and `10^8=1`.

Set `M=2877=21*137` and `a=695`, the CRT solution of `a=2 mod21`, `a=10 mod137`. Again the action has exact order 24, so the same displayed law defines a group of order `24*2877=69048`.

Keeping the centered integers and the module-21 residues gives

`g1=(1,2326), g2=(2,390), g3=(7,1881), h=(12,0)`.

Their three true inverses are

`(23,2617), (22,2832), (17,918)`.

The seven phases `1,2,7,12,17,22,23` are distinct and nonzero. Therefore these seven elements form an inverse-closed nonidentity set with no repetitions; their undirected Cayley graph is simple and exactly 7-regular. The positive-element orders are `24,12,24`, while h has order 2. These orders follow from the phase orders and the vanishing geometric normal sums; they were also checked by at most 24 small group multiplications per element.

Connectivity can be proved without a graph search. With multiplication and commutators in the displayed convention,

`k = h*g1*h^-1*g1^-1 = (0,987)`.

Its CRT normal residues are `(0,28)`, so it generates the full pure C137 normal factor. Also

`r = g3*g1^-7 = (0,586)`

has CRT residues `(19,38)`, and

`r*k^28 = (0,2329)`

has CRT residues `(19,0)`. Since 19 is a unit modulo 21, this generates the pure C21 factor. Thus all of the normal C2877 is generated. Removing the normal part of g1 then gives phase 1, proving generation of the whole target group.

## Capacity and exact diameter have different roles

The producer projects onto the unchanged 504-state quotient `C24 semidirect C21`. Its saved `CAPACITY.json` counts all 391910 reduced words of lengths zero through seven, with minimum raw count 663, at slot 135 `(phase6, normal9)`. Since 663 is at least 137, this necessary path-count test allows the target. It is not a certificate that those words attain all 137 field values.

`RESULT.json` and `NATIVE_RESULT.json` record the actual complete identity-root BFS of the one target Cayley graph: all 69048 vertices reached, maximum distance 8, and 187 vertices outside radius 7, first ID 26. No new BFS was run for this note.

For a right Cayley graph, every left translation `g -> k*g` preserves every generator edge `g -- g*s`. Left translations act transitively. Consequently distances from the identity already determine the global diameter: the producer's complete identity BFS proves **global D=8**, rather than merely the eccentricity of a sample root. This conclusion does not use vertex transitivity of the published source, and no source BFS was repeated. The 187 count is a root-specific missing-state count, not an ordinary unordered bad-pair count.

The implementation's initial inverse-table initialization error is separately retained in `INITIALIZATION_ERROR.json`; its corrected run tested this same single candidate. This audit neither treats that routine fix as another parameter experiment nor requests another run.

## Scope and disposition

The source first-row match, centering conjugation, CRT transfer, inverse binding, degree, connectivity, and Cayley root-to-global inference are valid. The necessary quotient capacity passes, but the sole target's actual diameter is 8. This closes only the frozen `q=137, alpha=10, centered(-3,-21,-37), module21 fixed` control for target `(7,7)`. It does not exclude other actions, offsets, primes, or the entire published-source mechanism. No such variants are proposed or executed here.
