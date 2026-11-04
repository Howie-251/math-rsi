# Expanded B inputs close two more fourteen-hole root-star orbits

2026-11-02. ARIS proof-writer candidate; independent review pending.

## Exact claim and source

From the exact2,527 covered-target residual accepted by
FOURTEEN_MAXIMAL_A_REVIEW, two disjoint60-record orbits are covered here.
The new remaining counts are240/702/1,465 for targets1/7/31, totaling2,407.
The free-target branch remains accepted. Full14 and P6 remain OPEN.

Both representatives have u=0,v=31, W={1,2,4,8,14,16,32}, all six Z in
the bit32 face B. Their projected sets T=Z xor32 are:

- orbit79: {7,11,13,19,21,31};
- orbit87: {7,11,13,22,26,31}.

The record orbits use every permutation of the first five coordinates,
fixing0,31 and the outer coordinate. Every actual transport, original source
index and exact remaining stream is supplied in FOURTEEN_STAR_EXPANDED_transport.json.

## Universal maximal-A reduction

Let A be the bit32-zero face, J={1,2,4,8,16,14}, E the15 nonzero even
vertices of A, and O the10 odd vertices outside J. The original internal
matching L=M_A lies in G=Q5[E union O]. Every t in T is internally matched
in A because its mirror is an original B hole. In particular v=31 is
internally matched. Extend L by adding short edges in G to an
inclusion-maximal matching Lstar, still covering T. This preserves all
original edges. It suffices to supply a compatible construction for every
such Lstar, with later-added edges treated as completion edges.

For each Lstar, the finite certificate chooses an unmatched even q,
t in T minus{31} adjacent to q, and distinct unit vertices w,b. Set
S=J minus{w,b}; it has four odd source holes, including14. Replace the
Lstar edge31-hstar by w-hstar to form Lstarprime. The selected short forest
P on A minus{0,31} has degree2 at q,b and degree1 at every other retained
vertex, contains q-t, and P+Lstarprime is acyclic as a labeled graph.
Its free endpoints form equal nonempty even/odd sets (at least8 in total).
An opposite-parity matching Dstar joins its path components into a30-cycle
CA. This is the same balanced-endpoint gluing lemma used in the accepted
maximal-A reduction: orient even-odd paths, and alternate even-even and
odd-odd paths; the endpoint count guarantees the required pairing.

Let h be the actual original mate of31, and Lprime=L minus31-h plus w-h.
Since31 was already matched in L, h=hstar, so Lprime subset Lstarprime.
Use D=Dstar union(Lstarprime minus Lprime). Every added edge has endpoints
originally unmatched internally in A, and therefore represents a completion
edge rather than an original requirement. D is a matching on the actual
A cross ports except q, together with the four sources S. In particular14
remains a source, never an edge endpoint of Lstar. The same CA retains every
edge of Lprime and every edge of D. These assertions are universal for
all original submatchings, not just maximal ones.

Delete D and the opening q-t from CA. Attach the actual original crossing
edges (including the crossing at q), the four bridges s--(s xor32), and
the opening bridge t--(t xor32). The latter consumes one original B hole.
Compress the transferred A paths. At each source mirror Y, the original
internal short edge has a mate outside Y; simultaneous pendant-mate
suppression yields the B required matching. Its marked holes are
minority{0}, majority(T minus{t}) union S, omissions S, in projected B labels.
This is a1:9 four-omission input. All translations and permutations apply
simultaneously to these sets and the forced pair below.

The two retained neighbors of the included minority hole0 are exactly
w,b: S removes three of the five unit neighbors and the nonunit14.
Thus the local forced pair is R={w,b}. Both original B vertices corresponding
to w,b are internally matched by original short edges, since their A mirrors
are original holes. They are neither cross ports nor source mirrors.
Their original mates have the opposite parity from Y, so suppression leaves
those short edges unchanged. Therefore the actual compressed matching
cannot contain the same-parity pair R. The accepted single-cherry
classification applies once the new marked local rank inputs are audited.

Expand the B avoiding-S cycle and all suppressed paths. This produces a
62-cycle on Q6 minus{u,v} containing F=M minus(vh) plus(wh). Delete its
auxiliary edge wh, prepend the short edge u-w and append h-v, restoring
the original matching edge hv. The result is a Hamilton u-v path containing
every edge of the original M. The construction and its boundary conditions
are the generic argument independently checked for orbit85; the two new
T sets change only the finite A and B premises checked here.

## Ten new positive B inputs

All200 ordered choices t,w,b in the two representatives were used only
to search for useful local inputs. The actual A certificates use ten
canonical B classes, indices0,1,7,8,17,24,25,26,30,35 in
FOURTEEN_STAR_B_EXPAND_profile.json. Only these ten are premises.

Each has22 covered vertices. Every selected short forest contains the
forced cherry through0 joining its two retained unit neighbors. Deleting
that fixed endpoint pair gives20 reduced terminals. The supplied512 by512
matrix has full GF2 rank512. For any F not containing the forced pair,
contracting its two incident edges across that pair gives a perfect matching
on20 terminals. The generic connectivity-rank theorem supplies a compatible
forest, and expanding restores the local cycle. If F contains the pair,
the forced cherry makes an isolated triangle, so no spanning cycle exists.

The reduced prefixes are FOURTEEN_STAR_B_REDUCED_orbit_iii. Each has512
forests of34 bytes, full endpoint pairs22 bytes, reduced pairs/columns20
bytes and matrix/pivot/combination rows64 bytes. Metadata pins source column
indices. Independent checking must reconstruct forests, full/reduced pairs,
every2,621,440 connectivity bit and all ten ranks. Candidate ranks for the
other32 classes are not imported.

## Complete positive A premises and actual partition

The A graph G has15 even and10 odd vertices. The complete maximal T-covered
domains have285,153 and289,791 elements respectively, total574,944:

| Orbit | Size10 | Size9 | Size8 | Total |
|---|---:|---:|---:|---:|
|79|274691|10462|0|285153|
|87|274691|15082|18|289791|

The two *_A_full_{79,87}_certificates.bin files use the previous32-byte
format: sorted Lstar edges padded255 to byte21; byte22 size; bytes23..27
q,t,w,b,forest-case; bytes28..29 source row; byte30 first-five permutation;
byte31 internal-target flag (always1). Source forests are the five
TWELVE_ROOT_STAR_OPENING_case_0c_forests.bin pools. Their deficient global
ranks are irrelevant: only individual positive forests are used.

Independent verification must establish a complete maximal domain (for
example independent enumeration or independent counting plus uniqueness),
every physical forest and modified matching union, every actual B marked
transport into one of the ten audited classes, and the exact120 source
records under the target stabilizer. The producer DP counts, compatibility
search and rank flags are not independent acceptance. The120 new records
are disjoint from the previously accepted orbit85, and the three remaining
streams preserve source order exactly. No global novelty or formalization
claim is made.
