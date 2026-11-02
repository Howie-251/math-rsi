# Loz3243 has a recovered interface; the direct transfers are already closed

This is a read-only handoff, not a source or graph revalidation. All source
facts below are inherited from
`research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/`.
No network retrieval or mathematical experiment was needed.

## Actual local source and complete recipe

`source3243.raw_adj.txt` is the cached official3243-vertex,6486-edge adjacency,
with1-based labels in the original file. `SOURCE_FACTS.json` records degree
distribution{4:3243} and the prior exact12972-directed-edge recipe binding.
The official D8/girth10 and automorphism information are inherited from
`official_sage.txt`; no source BFS or group recovery is rerun.

The exact representation is three base points times a group of order1081,
not a guessed factorization and not a Cayley graph on all3243 vertices:

    G=F47 semidirect C23,
    (x,y)*(a,c)=(x+a mod23, y+6^x*c mod47),
    label=base*1081+x+23*y, base=0,1,2.

The base is K3 with identity voltages0-to1 and0-to2, cross voltage1-to2
(4,45), and one inverse-pair loop at each base point. Their positive
voltages are respectively(3,8),(11,2),(6,35). `SOURCE_FACTS.json` gives
all twelve directed darts and their actual inverses. Left group translation
acts on each1081-point fiber, yielding three source vertex orbits; the
public verifier describes Aut=C47:C23 and a non-vertex-transitive graph.

Equivalently, expand the phase into the controller. It has69 states
(base,x), x in C23, four ports per state, and a47-point scalar fiber. A
stored dart(from,to,a,c) becomes

    (base,x,y) -> (to,x+a,y+6^x*c).

This is a degree-preserving point-to-point translation chart. It has no
free per-edge scalar noise. In the successful D3 affine-line construction,
one controller edge yields q neighbors via a freely varying line parameter;
that operation would multiply the degree here and is not the same cap4
interface. The common transferable idea is that different controller words
must cover complementary endpoint translations. It is not an automatic
rank/pencil corollary of the D3 line charts.

## Inherited exact stops: do not run them again

1. **Retain every old edge and add vertices at cap4.** Every old source
   vertex already has degree4. A connected extension needs an old-new edge,
   but there is no old degree slot. This closes the specified monotone
   extension, independently of how the new vertices connect to each other.

2. **An ordinary nontrivial cover of the actual3243 source.** The official
   girth is10. A length-at-most9 source closed walk freely reduces to the
   empty walk: a nonempty reduced closed walk would contain a cycle of
   length at most9. In an ordinary cover, deleting an immediate backtrack
   from a projected walk also deletes an actual lifted backtrack, so an
   empty reduction returns to the initial sheet. Therefore two distinct
   vertices over the same old point cannot be joined in at most9 steps.
   A disconnected cover also fails finite diameter. This inherited proof
   excludes D<=9 ordinary covers, and in particular every ordinary small
   cover proposed at the current target D8. No fresh walk-count gate is
   needed for this already closed scope.

The existing REPORT and SOURCE_FACTS state both stops explicitly. They do
not exclude deleting old edges, another source or a different69-state
translation rule.

## A distinct field change was tried once; keep its failure narrow

`CONTROL_RECIPE.json` and `CONTROL_RESULT.json` freeze one change F47 to
F139 while keeping phase23, multiplier6 and centered translations8,2,-12,-2.
It has9591 vertices and was tested for D9, not accepted as a D8/D9 graph.
The saved first new-graph root has eccentricity10 and misses245 vertices
at R9; the other two deck-orbit roots were not tested, so the old result
does not establish an exact global diameter. This one control is terminal
and is not rerun. It is not an ordinary cover of the3243 source:139/47 is
not an integer. Its failure therefore comes from its actual endpoint
coverage, not the ordinary-cover girth argument above.

The saved phase-only length<=9 minimum word counts are533,510,528 for
the three base roots. Those older necessary counts permitted139, yet the
actual fixed translation control failed. They are not length<=8 counts,
and they say nothing sufficient about simultaneous field coverage.

## One concrete next question, deliberately not executed here

PRED.md isolates the actual69-state controller as a small diagnostic object:
hold the phase shifts/reverse ports fixed and count nonbacktracking words
of lengths0..8 to every target state. The falsifiable prediction is that a
slot has fewer than139 words, which would immediately reject every
F139-translation assignment in that fixed phase family at D8. Every word
has only one field endpoint, even if its affine parameters are changed.

If the count instead permits139 everywhere, the next obstacle would be
compatibility of the four shared translation parameters; neither the count
nor the already failed centered choice settles it. No parameter search,
field ladder, repeated9591 graph or additional scope is authorized by this
note. The direct source-cover and monotone rules stop immediately as
inherited exclusions, and root chooses whether this distinct necessary
controller diagnostic is worth a separate bounded task.

Public provenance remains Eyal Loz's July2006 contribution, with literal
input and generator evidence already cached. No existing graph is claimed
as this project's construction, and no new graph/parameter/Lean count follows.
