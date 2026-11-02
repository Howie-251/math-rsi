# Encoding and return-object review

Prepared model:150 undirected edges,7200 selectors,7050 sequential-counter
auxiliaries,14250 total variables,24450 clauses. Preparation PID2258128,
measured function CPU0.848586814 seconds. The old global model is not reused
as a solver state.

1. Each edge is oriented by lower controller label to higher label. Its
   source port p and target reverse port inv(p) are read from the literal
   controller; every opposite dart is assigned this same edge and reverse
   flag. No port4 self-involution restriction survives this change.
2. All60 projectivities are considered. Exactly48 have a full projected
   pencil, forward iff reverse. Each surviving map has one selector.
3. Each edge has one at-least-one clause and a standard existential Sinz
   at-most-one chain. Together these choose exactly one map. Counter
   variables have no mathematical interpretation beyond this constraint.
4. Every one of3300 nonadjacent/equal ordered pairs gets one positive clause.
   For each of its actual NB3 words, include every selector on that word's
   central edge that makes the correct forward/reverse turn full rank.
   Multiple witnesses or repeated selectors in a clause are safely deduped.
   The OR imposes no choice of a predetermined path.
5. SAT parsing checks the full literal CNF assignment, then reconstructs
   each chosen forward matrix as H_target^-1 diag(1,Q) H_source and uses its
   actual inverse on the reverse dart. It checks all300 inverse/line/pencil
   conditions and chooses one actually rank3 word for each required pair.
6. Only after these checks are all3840 adjacency sets built and checked for
   exact degree20, no loops and reverse edges. Full-rank/pencil certificates
   prove D≤3 for every source coordinate. Since3840>401=Moore(20,2), D=3.
   This is followed by root-arranged independent graph validation, not a
   producer claim of independent acceptance.

One solver call only. `-t48` is a wall-clock window according to local
CaDiCaL help; RLIMIT_CPU49 is the CPU hard bound. Observation timeouts keep
polling the same PID. No seed/configuration ladder, no proof logging, no
automatic repeat. Code20 records RAW_UNSAT for this sufficient domain;
other non-SAT returns record UNKNOWN and stop. The wider edge-dependent
construction with triangle-route assistance or affine offsets is not
excluded by a negative solver result here.
