# Twenty-seven actual single-cherry local classifications

2026-11-01. ARIS proof-writer candidate, independent verification pending.

## Exact conditional local theorem

For each of the27 rows in `TWELVE_NEW_FORCED_summary.json`, put
H=minority union majority, U=omitted, K=V(Q5) minus H. The row specifies
an included hole h and two covered vertices p,q. For every perfect
matching F of the COMPLETE graph on K, a cycle on exactly V(Q5) minus U
containing F and adding only cube edges exists if and only if pq is not
an edge of F. The statement transports under common cube automorphisms
of all marked data (H,U,h,{p,q}). It does not assert any unlisted input.

All rows have22 covered endpoints. Their types are T28 (2:8 holes,
three majority omissions) or T19 (1:9 holes, four majority omissions).
Every neighbor of h outside U is precisely p or q, and both are in K.
Thus any permitted cycle must contain p--h--q. If F contains pq this
forms an isolated triangle, while the retained graph has29 or28 vertices.
The forbidden pair is therefore a genuine necessary obstruction.

## Sufficiency by a reduced rank certificate

The certificate supplies512 short forests S. Each covers V(Q5) minus U,
has degree one at K, degree two at H minus U, and no cycle. These forests
have eighteen edges for T28, seventeen for T19. Each consists of eleven
paths, and the h path is exactly p--h--q. Its endpoint matching P(S)
contains pq. Delete that pair to obtain P'(S) on K'=K minus {p,q},
with twenty endpoints.

For any F not containing pq, write Fp=a and Fq=b. The four vertices
p,q,a,b are distinct. Delete pa,qb from F and replace them by ab,
obtaining a perfect matching F' on K'. The labelled graph F+P(S)
is connected if and only if F'+P'(S) is connected: contract its path
a--p--q--b. This equivalence is an exact graph operation, not an
assumption that the compressed matching remains short.

The complete matching-connectivity matrix on K' has GF(2) rank
2^(20/2-1)=512 by Cygan--Kratsch--Nederlof, Corollary3.5; the same
general primary-source import is recorded in
`A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md` (arXiv1211.1506,
DOI10.1145/3148227). For every claimed geometry the512 supplied reduced
forest pairings and512 supplied arbitrary matching columns give a
full-rank512 submatrix. Thus the selected complete rows span the full
matching-connectivity row space. Every column is nonzero, by cyclically
joining the ten edges of its perfect matching. Some selected P'(S)
is therefore connected with the arbitrary F'. Undo the contraction,
then expand P(S) to S. The result is the required simple cycle.
Common required/forest physical edges cannot occur in a successful
connected pairing union: they would be an isolated labelled two-edge
component; the particular common pair pq was excluded explicitly.

The finite checks of forest legality, the fixed cherry and exact binary
rank are the only computational hypotheses. No generator exhaustiveness,
deficient-rank negative inference or full-Q6 theorem is used.

## Certificate formats and independent obligations

Each summary row gives its prefix `TWELVE_NEW_FORCED_orbit_XXX`.
There are512 unsigned-byte records in each forest or pairing file:

- `_forests.bin`: 36 bytes per T28 record, 34 per T19 record.
- `_full_pairs.bin`: 22 bytes, the full eleven endpoint pairs.
- `_pairs.bin`: 20 bytes, the ten reduced pairs.
- `_columns.bin`: 20 bytes, arbitrary perfect matchings on K'.
- `_matrix.bin`, `_pivots.bin`, `_combos.bin`: 512 rows of64 bytes,
  little-bit-first; pivots use highest-bit positions and combos select
  original rows by XOR.
- `_config.txt` and `.json`: actual geometry and extraction metadata.

Independent verification must reconstruct every forest and its full
pairing, check exactly the available neighbors of h and its forced
physical cherry, delete pq and compare the reduced pairing, validate
every reduced column, reconstruct all512^2 connectivity bits, and check
rank512. The source full-matrix column indices in metadata explain
construction but need not be trusted; the resulting reduced certificates
stand on their own. Total:13824 forests and7077888 connectivity bits.

The author extraction uses independent columns of an already produced
512-by-1024 matrix and contracts the selected columns. It is merely a
producer; the target theorem does not rely on trusting those original
matrices or their rank metadata.

## Q6 application boundary

An actual cut may use this local theorem only after checking the marked
geometry, legal sources and the hypotheses of
`HIGHER_FORCED_CHERRY_TRANSFER.md` / `HIGHER_FORCED_CHERRY_REVIEW.json`,
including exclusion of the global root from the actual pair {p,q}.
Original shortness alone does not ensure the compressed F lacks pq;
the accepted safe-completion argument supplies that fact. No actual Q6
coverage count is claimed here. Full twelve-hole/P6 remain OPEN.
