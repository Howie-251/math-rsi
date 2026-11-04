# A8: final residual orbit, complete finite-completion obligation

2026-11-01. ARIS proof-writer. Proposed complete assembly; the positive
certificate run and fresh independent review must finish before acceptance.
Full A8 and P6 are not declared proved by this draft.

## Exact claim

Every arbitrary matching F of K(Q5) with holes exactly

$$H=\{0,2,4,8,15,23,27,29\}$$

has an extending cycle on exactly Q5 minus {0}, with only short new edges.
The twelve required edges may be long or join equal parities. The fifth
row of A8_PARTIAL_PROOF_PACKAGE.md has20 coordinate-permutation images
of this marked geometry. No other residual orbit is claimed here.

## 1. Imported constructions and four actual cuts

Import the accepted GQ4-avoid, Q4 T15/T63, and bridge criteria from
A8_BRIDGE_INPUTS_REVIEW.md/.json. For each cut bit b take A's bit zero
face, containing forbidden0, and B's bit one face. Select the bridge holes
in A that mirror to Y below.

| b | Y in B | fixed obstruction edge pq | B theorem |
|---:|---|---|---|
|2|6,10|3--18|T15|
|4|6,12|5--20|T15|
|8|10,12|9--24|T15|
|16|18,20,24|16--17|T63|

Each of the first three A faces has two minority and two majority holes.
The two bridges consume its minority holes; the A completion has two
majority holes and the compressed B input has1:5 holes, omitting Y.
The last A face has three minority and two majority holes; three bridges
leave its two majority holes, and B has six same-parity holes omitting Y.
Every bridge mirror is covered. Deleting the cut coordinate and normalizing
the singleton where required gives precisely the displayed local OB edges.

## 2. Exhaustive sufficient-condition partition

For any row let S=Y union {p,q}. If pq is absent from F and either a
crossing edge enters B outside S, or an internally matched bridge vertex
has its original mate outside S, the accepted bridge criterion succeeds.
Here is the complete reason, independent of any A-cycle search.

In G=F_B union C union the short bridges, all A vertices are degree-one
endpoints T. Let P pair T-to-T components and let e indicate whether
both p,q are B terminals of components rooted at T. The violated restriction
produces another B terminal outside {p,q}. The number |T|-2|P| of rooted
terminals is even and exceeds2e. Hence |T|/2>|P|+e. Prescribe P and the
OB-root pair when present as a proper subset of D, apply GQ4-avoid in A,
and use the audited bridge criterion. It guarantees an acyclic transfer,
no compressed OB, and a positive T15/T63 B completion. Expansion gives
the required31-cycle preserving all of F.

Thus every input not already solved must, for each row, either contain pq
or obey both restricted-edge conditions. Partition such inputs by the
four-bit mask of which actual fixed edges occur, in table order. For an
unset bit explicitly exclude its fixed edge and impose its restrictions.
This partitions all remaining matchings into16 disjoint finite graph
matching domains. The original graph is the complete graph on the24
covered vertices; no restriction to short original matching edges is made.

## 3. Exact finite domains

Require the set-bit fixed edges, delete their covered vertices, and
intersect the allowed-edge graphs for the unset bits. In a restricted
graph, crossings may enter B only at S, and internal B edges meeting Y
must remain in S. Enumerate all perfect matchings of the remaining graph.
The counts computed by A8_orbit5_joint_bad_enumerate.py are:

| fixed-edge mask | matching count |
|---:|---:|
|7|176400|
|11|176400|
|13|176400|
|14|176400|
|15|2027025|

All other masks have zero inputs. Total:2732625. These counts and the
empty branches require independent reconstruction; the producer's dynamic
programming alone is not the final acceptance gate. The input file stores
each original matching as24 endpoint bytes, with both endpoints within
each edge sorted and the twelve edges lexicographically sorted.

## 4. Positive finite completion and mandatory acceptance gate

The running producer a8_full_cycle_certifier.cpp seeks one31-cycle for
each complete input and writes55-byte records:24 original-matching bytes
followed by31 cycle vertices. Acceptance requires all2732625 inputs to
have such a record, with no missing or duplicate input. Every record must
independently satisfy:

* its required matching is exactly the corresponding complete-domain input;
* its cycle lists each vertex1,...,31 exactly once and never lists0;
* all twelve original required edges occur;
* every other cycle edge, including the closing edge, is a cube short edge.

These positive checks suffice regardless of the search algorithm. A timeout
or exhausted search would leave an explicit open obligation, not establish
a counterexample. The cycle order supplies connectedness as well as degrees.

## 5. Conclusion conditional on the gate, and scope

Once the independent domain reconstruction and all positive certificate
checks pass, every F either has a constructed cycle from Section2 or is one
of the certified finite inputs. This proves the exact claim and its20
coordinate images. A separate whole-A8 assembly audit must combine this
orbit with the other accepted cases before full A8 is marked closed.
No Q6 covered-target layer or full P6 conclusion follows solely from this file.
