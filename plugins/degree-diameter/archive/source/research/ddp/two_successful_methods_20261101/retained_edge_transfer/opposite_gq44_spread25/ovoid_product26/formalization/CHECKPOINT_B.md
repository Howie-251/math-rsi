#7531 key actual connections

Original source25graph and general FullNeighborhoodClones proof remain unchanged.
New scope is the ovoid×spread center encoding, capacity reduction and actual
finite hO supply; not an independent-center special case.

OvoidSpreadCloneCapacity.lean is compiled PASS2.161900CPU. Its source graph is
OppositeGQSpread.graph e Inc spread, centers are old(ovoid_i,spread_j).
For w=old(v), two adjacent centers give ovoid_i and ovoid_i' on line(v), and
spread_j/spread_j' through point(v); hO/hS identify both coordinates.
For w=bonus(k), each adjacent center is a flag with its spread j=k by hS;
hO on spread k identifies i. Thus adjacent center INDEX subtype has card≤1.
This proves actual full-neighborhood load≤1 without assuming center independence
or injectivity. The actual centers are allowed to induce136K2+17 isolated points.

OvoidProduct26Definitions.lean PASS2.259311CPU: exact17 ovoid IDs, original
source graph constant, original product ordering, product Fin289 and total
Fin7531 label equivalences. Old source labels unchanged; new7242+17*i+j.
Graph is FullNeighborhoodClones.graph acceptedSource center, never a graph of
current(center). New-new remains False even for adjacent centers.

OvoidProduct26Inputs.lean PASS10.249949CPU: owner_of_ovoid checks17 lookup facts;
line_index_certificate checks425 positive actual line positions, each none or
the same original85-line ovoid index. Inc membership gives that index, hence
actual hO. hS uses the previously-proved source spread_unique theorem. Actual
load_le_one supplies all generic hypotheses. No7242×289 adjacency enumeration,
Q algebra or graph-distance computation was performed. ovoid_unique uses only
propext; actual load result uses the standard3 axioms.

INPUT_BINDING_CHECK: all289 owners match at the same index in ORDERED_CENTERS,
IMMUTABLE_SOURCE_PINS and EXTENSION_STEPS. Every one of7225 pins equals the
sorted ORIGINAL7242source adjacency of that owner and is below7242; current
neighborhoods are never used. The source's existing formula-to90525edge binding
is reused unchanged. Clone formula equals all97750 literal edges, retaining all
90525source edges and0newnew. This is external input binding, not an ASCII
parser theorem or independent acceptance. It uses0BFS/solver calls.

Highest remaining compiled connection at this checkpoint: Exact must derive
source_no_isolated from actual source WalkD3 and explicit distinct source0/1,
then apply FullNeighborhoodClones.degree_le,diameterAtMost and old-Walk collapse
(nonD2). Intended Exact source contains the closed assembly; it has not yet
been counted as final PASS. Separate actual import/type/axiom audit follows.
Global novelty/priority remain unconfirmed. Root coordinates newscope reviews;
previous source or generic-clone reviews do not silently cover this new encoding.

Terminal update: Exact and independent Audit subsequently both PASSed; actual
closed final scope, type and axioms are in CHECKPOINT_C.md and FINAL_COMPILE_RESULT.json.
