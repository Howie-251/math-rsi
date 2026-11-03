# q=5: exact partner-ball marginal closes every added matching

Status: **VALID, complete for the fixed polynomial source plus one arbitrary simple complement matching**. This analysis read `check_overlap.py` and `RESULT.json`; it performed no new numerical evaluation, graph construction, BFS, matching search or solver call. The general three-walk image and route classification are proved in `../small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.md`.

## Exact source endpoint data and the code interface

The source has vertex set F5^3 and formal neighbour rule

    (a,b,c) -> (s,a*s-b,a^2*s+a*s^2-c),

with self-loops omitted. Let p=(0,0,0) and O=B3_G(p). The algebraic image count gives |O|=55. Its closed radius-two ball has size 21: the formal two-step endpoints are

    (d, u*d, u*d*(u+d)).

For d=0 there is one endpoint, and for each nonzero d the q choices of u are distinct. This gives 1+q*(q-1)=q^2-q+1=21. All one-step points (d,0,0) are already included by u=0. Equivalently, there are q zero-second-coordinate points and (q-1)^2 others.

For a general starting point x=(a,b,c), the two-step endpoint used by `ball2` is

    (d, b+u*(d-a), c+(d-a)*(u^2+(a+d)*u)).

This follows by substituting the formal first step with first coordinate u into the neighbour rule. Including the zero-step and one-step endpoints makes the returned set exactly B2_G(x): any formal self-loop can be removed, and every actual path of length at most two is explicitly included. Thus this code is an algebraic endpoint enumeration, not a graph BFS or a candidate matching test.

The forbidden partner set {(u,0,0):u in F5} is precisely {p} union N_G(p). Hence the other 120 vertices are exactly all possible mates of p in a complement matching. The saved complete calculation proves

    max over eligible x of |B2_G(x) minus O| = 20.

There are 24 maximizing partners. The original conditional prediction was at most 24; the actual bound 20 is stronger. These values are inherited from `RESULT.json` and `PARTNER_BALL_MARGINALS.json`, not recomputed in this review.

## Deduplication valid for partial matchings

Let M be any simple partial complement matching, with partial mate map m and matched-vertex set D. Put k=|N_G(p) intersect D|, so k<=4. Use the five endpoint classes from the general proof:

    O=B3_G(p),
    F=B2_G(m(p)) if p is matched,
    U=union_{u in N_G(p) intersect D} B1_G(m(u)),
    L=m(B2_G(p) intersect D),
    V=m(N_G(m(p)) intersect D) if p is matched.

Suppose first that p is matched, to x=m(p). The k vertices m(u), for matched u in N_G(p), are distinct and all belong to L. None equals x, because m is injective and u!=p. Therefore remove these k centres from U, and remove x from L. Every removed vertex is still represented by another retained set: the k centres are in L minus {x}, and x is in F. Consequently the full endpoint union remains contained in

    O union F union (L minus {x}) union
    (U minus {m(u):u in N_G(p) intersect D}) union V.

Each closed B1_G(m(u)) contributes at most five vertices after deleting its own centre. The other three upper bounds are |L minus {x}|<=20, |V|<=5, and |F minus O|<=20. Thus

    |B3_(G union M)(p)| <= 55+20+20+5*k+5 <= 120.

There is no double subtraction: the proof explicitly replaces the endpoint union by covering sets with the removed vertices retained elsewhere. It also does not assume that all four old neighbours of p are matched. Using k rather than four keeps the argument valid for every partial matching.

If p is unmatched, F and V are absent. Remove the same k centres from U and retain them in L; then

    |B3_(G union M)(p)| <= |O|+|L|+5*k <= 55+21+20=96.

Hence every matching, whether or not it matches p, leaves at least five of the 125 vertices beyond radius three from p. This strictly excludes the whole stated single-matching augmentation family as a degree-six, diameter-three construction exceeding 120.

## Scope and state

No matching or augmented graph was instantiated. The numbers 120 and 96 are uniform upper bounds on one closed ball; five is a uniform missing-target lower bound, not an ordinary unordered bad-pair count. Actual graph order and global diameter fields remain null. The argument does not exclude arbitrary 125-vertex graphs, more than one added matching, edge deletions, rewiring, or a different base graph.

Evidence: `check_overlap.py`, `RESULT.json`, `PARTNER_BALL_MARGINALS.json`. The saved result records 125 partner endpoint evaluations, 120 eligible complement partners, zero graph generations, zero BFS, zero matching assignments and zero solver calls.
