# Independent paper and actual-code review

Paper result: the size-three K4 class has 15 incidences against 14
required outside helper classes. An internal old edge consumes two and
is impossible; 14 different classes require 14 distinct old endpoints.
Thus independence and neighbor union at least 14 are necessary. At most
one incidence may reach another class of the same K4 component, though
this last consequence is not separately encoded.

Actual-code read-only result: PASS. The triple filter enumerates all
unordered triples, rejects source-edge triples, and computes the union
of the three source neighbor masks correctly. The refinement appends
150*12=1,800 independence clauses and 6,840*12=82,080 forbidden-triple
clauses. The old CNF text is preserved except its header; the final
228,927 clauses and 44,460 variables agree. Repository/source paths and
the SAT-only verifier's additional path depth are correct. The reviewer
ran no solver or generation program.
