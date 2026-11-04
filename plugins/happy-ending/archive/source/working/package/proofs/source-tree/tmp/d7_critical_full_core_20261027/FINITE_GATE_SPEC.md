# One discriminating universal-minor gate (2026-10-27)

Status before execution: proposed mathematical test, not a theorem or acceptance.
The main session owns the mathematics. The only execution role is native
gpt-6.1-sol/high, on the authoritative Linux server. No existing run is restarted.

## Candidate and all-class entry

Candidate M6: no complete D7 contains the following fifteen-point restriction.
Order is P=(p1<...<p5)<a<Q=(q1<...<q4)<b<c<d<f<g.
Require actual R6 on P+a, a+Q+b, and (a,b,c,d,f,g), and require each of
a,b,c,d,f,g to be a right root on every later pair in this restriction.
All colors are otherwise free. Impose every packet, no B5, no weak7,
and no actual EndR5/SrcB4 intersection. R7 is also forbidden as a redundant
consequence of no weak7. All path quantifiers are actual and exhaustive.

Every D7 with exactly six actual R6 endpoints contains this ordered minor:
a=e1,b=e2,c=e3,d=e4,f=e5,g=e6; choose any R6 ending at e1 and any ending
at e2. The latter starts at e1 by R7's complete argument. Its four interior
points lie strictly between e1,e2, and the first path's five predecessors
lie before e1. The fifteen vertices are distinct (5+4+6=15). Every marked endpoint
is a right root in the parent, and remains so after restriction.
The restriction need not retain actual endpoint attainment at c,d,f.
Those identities are deliberately NOT inferred or imposed.

## Decision meanings and value

Bound/formula-checked UNSAT followed by a complete proof check would exclude
the entire E6 branch at every order. Raw UNSAT alone is only a candidate.
A complete SAT coloring checked directly against all mathematical conditions
refutes M6, showing that the first two endpoint witnesses plus all six root
identities cannot exclude E6. It need not refute D<=29 or uniform tau<=4.
Timeout gives neither conclusion. This targets a universal fifteen-vertex
minor proved above, unlike the previous n18 tau>=5 search (no size reduction)
or the previous unrestricted n30 decision. No favorable template is imposed
on a claimed full-class search: only this explicitly stated necessary minor
is tested.

## Authorized execution

One new run, external authoritative AE Kissat, wall/CPU budget <=60 seconds,
memory <=3GiB. Reuse the unchanged complete D7 base builder in a new directory
and append only the stated actual triple constraints for the three red sets
and six roots. Do not reuse auxiliary flags for positive path existence.
Preserve source hashes, formula/variable binding, command, full result, and
complete SAT assignment if any. On SAT recompute all packets, all actual
path and endpoint/source facts directly from colors; report all R6, actual E,
minimum tau, and alpha6. On UNSAT preserve proof and stop before claiming
checked exclusion unless the bound proof check is separately authorized.
No retries, fallback solver, increased budget, or follow-up search.
