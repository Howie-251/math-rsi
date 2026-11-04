# Rank reduction when an included hole forces a cherry

2026-11-01. A structural lemma for future marked multiple-omission inputs;
not an accepted new P6 branch.

Suppose an included free vertex $h$ has exactly two available short
neighbors $p,q$ after the specified omissions. Every short-complement
forest must contain $ph,hq$, hence its endpoint matching contains $pq$.
In the actual application $p,q$ are covered vertices; this assumption
must be checked, not inferred from the degree count alone.

If the required matching $F$ contains $pq$, the three edges $ph,hq,pq$
form an isolated triangle in every cycle extension: all three vertices
already have degree two. If other retained vertices exist, the desired
spanning cycle is impossible. This is an explicit obstruction.

If $pq\notin F$, put $a=F(p)$ and $b=F(q)$. The four endpoints are
distinct. Replace the two required edges $pa,qb$ by $ab$, giving a
perfect matching $F'$ on $K\setminus\{p,q\}$. For each admissible forest
with endpoint matching $P$, remove $pq$ to obtain $P'$ on that same set.
Then $F+P$ is one alternating cycle if and only if $F'+P'$ is one
alternating cycle: the path $a-p-q-b$ is suppressed or expanded.

Thus full rank $2^{(|K|-2)/2-1}$ for these shortened endpoint pairings
is a sufficient certificate for every required matching avoiding $pq$.
It need not be possible to attain the larger rank for the original
$|K|$ endpoints. A reduced-rank certificate plus the forced triangle
would yield an exact local classification.

For Q5 one-versus-seven holes with three majority holes omitted, a
minority free hole whose three neighbors are precisely the omissions
has this form if the other two neighbors are covered. In a Q6 transfer,
the original internal matching is short and cannot contain the
same-parity edge $pq$. The compressed matching may contain it, however;
one must still prove that the completion and transfer can avoid creating
it. A rank certificate alone does not discharge that transfer obligation.
