# Independent review: the 21-vertex degree-five candidate

2026-10-13, completed before 10:03 UTC. Reviewer: Codex Lean subagent. `review_independence: same-family`; `acceptance_status: provisional`.

**Result:** no mathematical gap found in the stated actual-input case split or the final incidence contradictions. Conditional on the retained strict probability witnesses, the argument covers every pair-covering simple five-uniform H with 21 vertices, 34 edges, and a degree-five vertex. This is a complete paper candidate for that branch, not a Lean result or a proof of all T34.

Read: `low-math/TWENTYONE_FIVE_COMPLETE.md`, the verification script and necessary generation functions in `probe.py`, `quad_general.py`, `twentyone_five_low.py`, `twentyone_five.py`, `twentyone_five_sevens.py`, plus the corresponding retained JSON records. I did not rerun the 169 numerical bounds or dual-certificate arithmetic.

## Actual selection and coverage

- Pair coverage gives a lower degree of five throughout. At the chosen degree-five x, the sum of the twenty positive codegrees is exactly twenty, so all are one. Hence the five actual x-edges partition the remaining twenty points into disjoint four-point blocks. This is the actual incidence fact used in all later choices; no independent or arbitrary partition is assumed.
- If a second degree-five/six point exists, choosing y of minimum degree off x and then z of minimum degree off x,y gives `d(y)≤d(z)≤8`. If z had degree at least nine, the nineteen points outside x,y would already contribute at least 171. When y has degree five, all its codegrees are also one by the same incidence identity. When y has degree six, `1≤λ(y,z)≤6` and `τ(x,y,z)≤1`; the stated triple domain covers exactly these possible local data after nonnegativity.
- After excluding that branch, x is the only degree-five point and every other degree is at least seven. Splitting on the exact number r of seven-degree points is exhaustive.
- For r≥3, the sole unsuccessful (5,7,7) triple gives **common** triple count one and seven-seven codegree two for every selected pair. Fixing one seven-point shows all seven-points belong to the same unique x-edge. Choosing three of them therefore gives actual common quadruple count one. The three exact traces involving x vanish, and the remaining exact three-seven trace is zero or one because its common count spends a pair inventory of two, one already spent by the common quadruple. These are precisely the two (5,7,7,7) records.
- For r=2, the degree budget gives at least eleven eight-points. The shared x/y/z edge contains at most two of them, so an eight-point outside it exists. Its common triples with x and either seven-point are zero by uniqueness of those x-pair edges. The remaining selected domain has eight records, all strict. No unproved choice of a specially correlated eight-point is required.
- For r=1, the degree budget gives at least thirteen eight-points. Removing the at most three in the x/y edge leaves S of size at least ten. Every point of S has common triple x/y/z zero. After the stated strict triples are excluded, the quadruple domain is exactly the one used in the table. Its single residue forces, for **every distinct z,w in S**, codegrees λ(y,z)=λ(y,w)=1 and common triple y/z/w zero. Since |S|≥2, each individual z can be paired with another w to derive the unit statement. More critically, no actual edge through y can contain two points of S. Seven y-edges therefore cover at most seven members of S, contradicting pair coverage and |S|≥10.
- For r=0, at least fifteen eight-points exist. After eliminating high pair codegrees, every selected triple of eight-points lies in the complete 62-record (5,8,8,8) domain. All five residues have exact quadruple count zero, which is also the common count of those four selected locks. Thus an x-edge cannot contain three eight-points: such a triple would give a selected quadruple with positive common count. Five x-edges cover at most ten eight-points, contradicting the at least fifteen required x-pairs. This uses a universal conclusion for every triple, not one fortunate selection.

## Independent domain and binding check

I added and executed `review_twentyone_domains.py`. It reconstructs the quadruple domains using **common triple variables** and Möbius inversion, independently of the original generator's exact-triple parametrization, then compares the entire sets of recovered multiplicity vectors with the saved data. It also checks that every strict selected source record has its full `(v, degrees, positions, actual type counts, bound)` bound to a record in the retained verified-witness JSON.

The check passed:

| Local domain | Complete records |
|---|---:|
| (5,5/6/7,d) triples | 67 |
| (5,8,8,8) quadruples | 62 |
| Seven-containing quadruples across the saved parameter range | 118 |
| Additional high-codegree (5,8,8) triples | 11 |

The 118 count includes saved (5,7,8,8) profiles with eight-eight codegree above two; those are correctly discarded from the required quadruple branch only after the separate strict (5,8,8) triple eliminates them. The required (5,7,8,8) domain has exactly one failed record, with the stated zero common traces; the (5,8,8,8) domain has exactly five, all with zero quadruple count. Output is `TWENTYONE_DOMAIN_REVIEW.json`, PASS within this scope.

This strengthens the local coverage/binding evidence but does not repeat the numerical probability or avoided-lock certificate verification. New Lean implementation still needs the actual selected vertices, recovered type multiplicities, real bad-pair deductions, and the two general edge-capacity contradictions. No existing Lean/source file was modified for this review.
