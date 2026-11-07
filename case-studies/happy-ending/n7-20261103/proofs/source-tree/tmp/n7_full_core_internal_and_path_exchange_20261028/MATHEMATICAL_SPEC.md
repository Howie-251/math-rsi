# Frozen mathematical specification — fixed full-core/internal insertion and path exchange

Date: 2026-10-28. Supplied by the parent mathematical planner before implementation.
This authorizes finite consistency checks of exactly two supplied complete colorings.
It does not authorize SAT, parameter search, proof replay, external review, new global
bounds, acceptance changes, modification of existing artifacts, or scientific retry.

## Runtime and change boundary

Only this fresh directory is owned. Existing research, synthesis, task state,
acceptance, traces, proofs and running jobs remain outside the write boundary.
All scientific Python execution and py_compile must occur on authoritative Linux:
/data/ktqiu_hdd/math_agent, using /opt/anaconda3/envs/forktqiu3/bin/python3.12.
Windows is for file preparation and transport only; Windows Python is prohibited
unless the parent/user explicitly grants a transport-only exception.

One scientific process, external wall 180 seconds with TERM then KILL after 2 seconds;
internal deadline 150 seconds, CPU 175 seconds, address space 512 MiB.
Timeout is UNDECIDED; no retry, continuation, extra budget or scope expansion.

## Common exact semantics

Vertices are totally ordered and every increasing triple has exactly one R/B color.
For a<b<c<d, the packet word is abc,abd,acd,bcd and must change color at most once.
A monochromatic path counts vertices; compare consecutive triples against every
triple within the selected vertex subset. Length-two paths are vacuous in both colors.
Weak7 is forbidden when same actual first/last endpoints have red and blue path
lengths summing at least 9. No disjoint-interior assumption is introduced.

Recompute endpoint paths by a pair-state dynamic program independently of subset
enumeration, retaining reachable lengths and witnesses for every endpoint pair and
color. Check all reachable lengths, not just maxima. The DP covers all lengths up
to the order; complete subset comparison for 26/25/21-point objects covers lengths
2 through 6. DP must also certify no omitted longer monochromatic paths there.
Every induced object recomputes colors, packets and endpoint states internally.

Export all triple colors (CSV acceptable), every packet check, actual endpoint
maxima and reachable lengths/witnesses, complete relevant path families, exact
operation results, source/input/spec hashes, command/environment/exit receipts,
and a short engineering report. A finite pass is
FINITE_CONSISTENCY_PASS_UNREVIEWED_UNACCEPTED, never independent mathematical review.
If an assertion fails, retain concrete failure data; do not repair and rerun.

## Fixed object 1: 26 vertices U<T<V

F(a,b) has blue maximum a, red maximum b. Base F(2,b) is b all-red
vertices; F(a,2) is a all-blue vertices. Recursively
F(a,b)=F(a-1,b) plus F(a,b-1), in consecutive order, with left-left-right
triples B and left-right-right triples R.

U=F(3,5), 15 vertices numbered 0..14.
T=(t1,t2,t3,t4,t5), vertices 15..19, all blue.
V=F(3,3), 6 vertices numbered 20..25.
The base is U plus V with the same left-left-right B / left-right-right R rule.
Pure-base triples inherit this base color. Pure-T triples are B.
Any mixed base/T triple is B iff its middle vertex is in base, and R iff
its middle vertex is in T.

Expected:
- All packets legal; no blue6, red6 or weak7.
- The complete blue5 family consists exactly of T.
- Every red5 is inside U.
- x=t3=17; A=X minus x is a 25-point 756 object (no blue5, red6, weak7).
- P is the first F(2,5) block, vertices 0..4.
- Red role Urole=P; blue role Vrole={17}; B=X minus P is the 21-point
  dual756 object (no blue6, red5, weak7).
- Enumerate all 2^15 subsets of U to establish the red5 minimum transversal
  size 5; export the minimum and all minimizers, or every mask's validity.
- Red5 and blue5 supports are disjoint. Thus total used minimum is 5+1=6;
  the given legal pair has rho=26-6=20.
- Inversion I=#{(u,v):u in Urole,v in Vrole,u>v}=0, so the legal pair is
  lex optimal without enumerating all 3^26 role assignments.
- All blue5 insertion witnesses for x=t3 into A are exactly T, with x
  strictly internal and zero endpoint witnesses.
- Endpoint controls x=t1=15 and x=t5=19 each have an endpoint witness.
  Recompute their respective 25-point induced cores internally.
- b=25 gives delta=50-26=24, d_A=0, d_B=4 and rho=20.
  This is not delta0, not two full cores, and not a counterexample to C<=49.

## Fixed object 2: 10 vertices a<A4<B4<b

Number a=0, A={1,2,3,4}, B={5,6,7,8}, b=9.
Any triple containing a or b is R. An internal triple wholly in A or
wholly in B is R; every other internal triple is B.

Expected:
- Legal 767, red maximum 6, blue maximum 4, no weak7.
- The entire red6 family is exactly (a,A,b) and (a,B,b).
- Keep a,b fixed; replace k points of the A path by k points of B.
  Enumerate all C(4,k)^2 choices for k=1,2,3: 16+36+16=68 failures.
  Save each selected path and a violating triple. At k=4 the single
  complete replacement succeeds.
- K={a}, Y=the remaining nine vertices, Z=empty is a valid 766/756/empty
  partition. Recompute both induced objects internally.
- Consequently this is not a minimally unsatisfiable partition obstruction.

## Explicit non-results

No near48/78 construction, no simultaneous full756 kernels, no universal
endpoint reduction, no new C/Q/F upper bound, no new independent review, and
no acceptance or proof binding change follows from these two finite checks.
