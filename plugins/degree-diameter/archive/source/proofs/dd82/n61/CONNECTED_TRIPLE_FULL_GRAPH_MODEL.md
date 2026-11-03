# Complete original-graph test of the order61 triple-repeat branch

## Objective and current status

Decide the realizability of a61-vertex degree8 diameter2 graph with at
least one defect entry3, using the proved necessary triple-repeat
structure. This is a full adjacency completion task, not a feasibility
test of C alone. A SAT result must supply an actual graph; a complete
certified UNSAT result would exclude the whole triple-repeat branch.
UNKNOWN would decide neither. Subsequent actual execution: the baseline
returned UNKNOWN; the proved grid-normalized input returned UNSAT and
its LRAT certificate verified. See CONNECTED_TRIPLE_EXCLUSION.md for the
full proof chain and exact current scope. This file records the model.

The prior local and layer-interface proofs are explicit dependencies.
The local proof has a fresh same-family PASS, and its layer refinement
has a completed, explicitly reused same-family PASS. The complete original
degree/diameter constraints remain in the encoding even when necessary
layer constraints are added. No binary B, automorphism, CP02 H/no-O,
historical n62 data, or particular C/sigma is assumed.

## Exhaustive normalization of a hypothetical target

Choose any actual triple pair u,v. The local proof forces the shared
unit B endpoint w and the4 common neighbors S={a,b,c,d}, with w
A-adjacent precisely to a,b in S. Its exact full vertex partition is

```text
u=0, v=1, w=2, a=3, b=4, c=5, d=6;
U=7..10, V=11..14, Ta=15..19, Tb=20..24;
Tc=25..30, Td=31..36, Z=37..60.
```

All complete neighborhoods of the seven core vertices are fixed:

```text
N(u)={a,b,c,d} union U;    N(v)={a,b,c,d} union V;
N(a)={u,v,w} union Ta;    N(b)={u,v,w} union Tb;
N(c)={u,v} union Tc;      N(d)={u,v} union Td;
N(w)={a,b,Tc[0],Td[0],Z[0],Z[1],Z[2],Z[3]}.
```

The proofs give perfect A-matchings U↔V and Ta↔Tb. Label each second
side by its matched partner, making both matchings the identity. There
are also bijections from Ta to Tc minus its unique w-neighbor and to
Td minus its unique w-neighbor. Independently label those two five-point
sets so Ta[i] is adjacent to Tc[i+1] and Td[i+1]. These choices are
compatible: U/V, Ta/Tb, Tc and Td labels are separate, and gamma/delta
remain at index0. The four Z neighbors of w can independently be put
at Z[0..3]. No relabeling simultaneously fixes an unproved Tb-to-Tc or
Tb-to-Td permutation; both must remain variable.

This normalization applies to every actual triple pair. In particular,
the two r/s port-position cases in CONNECTED_TRIPLE_LAYER_INTERFACES.md
both remain included. Neither a specific C=B[U,V], its sigma, nor a
particular graph A[Z] is selected. If the implementation branches on the
two cases, both require actual terminal evidence; a one-case result is
not a whole-triple exclusion. A single model that leaves both cases
implicit is also complete and avoids unnecessary case splitting.

## Boolean graph variables and full original constraints

Use one Boolean A_ij=A_ji for each permitted unordered pair i<j,
with no self-loop variables. The core neighborhoods above fix their
incident pairs to0 or1. Additional zero entries and exact block degrees
may be imposed only where the source cites the proved layer table.
Every other edge remains variable. Each of the61 vertex degrees equals8.

For each distinct pair i,j require its actual edge or an actual common
neighbor:

`A_ij OR (OR_(k distinct i,j) (A_ik AND A_kj))`.

If auxiliary conjunction variables are introduced, encode their stated
semantics and do not allow a coverage witness without its two edges.
Constant propagation may simplify the clause but cannot discard an
uncovered pair. Thus any satisfying model expands directly to a simple
eight-regular graph on61 vertices with diameter at most2.

Conversely, every hypothetical triple-repeat target has the normalized
labeling above and satisfies all these Boolean conditions. The fixed
u/v neighborhoods themselves imply they are nonadjacent with exactly4
common neighbors, hence B_uv=3. This is a genuine original-graph
representation of the entire branch, not a relaxed quotient test.

## Result evidence and bounded execution

Reuse the installed solver and proven general CNF-building routines,
without running any old input or installing a backend. Generate and
inspect the actual new CNF after source review, then use a measured,
bounded single-core test (initial solver budget at most60CPU/90wall,
with explicit memory and proof-output limits). The exact launch command
and actual resource policy belong to the prepared runner; this note
does not claim a run occurred or that the finite space is easy.

SAT requires a saved complete model and expanded244-edge graph, then an
independent degree and all-pairs BFS from that edge list. UNSAT requires
the actual full trace/certificate and its successful independent checker,
as well as the coverage reduction above. A truncated proof, resource
termination or interrupted search is UNKNOWN, not a mathematical cut.
Do not silently restart after a tool observation timeout. The same
mechanism and Gemini thread will receive the actual result.

## What the completed small interface catalogue does and does not show

The separate source triple_interface_domain.py actually visited all
16^4=65,536 row assignments and completed in0.210814954CPU seconds.
It found968 labelled C,59 simultaneous-permutation C classes,4049
compatible labelled(C,sigma) pairs, and216 pair classes under the
matching-preserving simultaneous relabeling. Even under independent
row/column permutations, used only as a diagnostic, there are12 C
classes in the stated domain, not the reviewer's unsupported9.

C_ii=0 shows that the unit B port z_i is not A-adjacent to U_i or its
corresponding V endpoint. It does not place z_i outside Z; z_i could
lie in a different U/V incidence cell. The saved J-I/id partial example
demonstrates the logical gap in that proposed inference, without claiming
an actual graph realization. These two reviewer proposals are not used
as pruning conditions. The full-graph model keeps the actual choices.
