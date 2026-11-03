# All local edge repairs after an adjacent-pair deletion from Exoo72 fail D3

## Exact domain and actual counts

Fix the previously saved Exoo72 controller. Delete an adjacent pair u,v and
retain every other source edge, obtaining H on70 vertices. This experiment
allows arbitrary added old-old edges under maximum degree5, including A-A
and B-B edges on A=N(u)\{v}, B=N(v)\{u}. It therefore genuinely enlarges the
earlier pure-crossmatching operation.

The full operation is strictly excluded for each of the180 source edges:

- the earlier24 pure-cross perfect matchings per edge,4320 assignments,
  are inherited as completed failures and were not rerun;
- this batch checks all81 remaining perfect matchings per edge,14580 new
  assignments. Every one fails an exact necessary boundary route condition;
- the combined disjoint partition has18900 parameter assignments,
 180×105. These counts are not counts of distinct isomorphism classes.

The new batch has no boundary survivor, so it generates no70controller,
runs no new-controller full R3 check or unique-map gate, and starts no SAT
or fiber graph. The guarded single worker measured0.25110093CPU under its
15CPU hard limit. Existing pure-cross results keep their original terminal
state and budget.

## Why perfect matchings cover all allowed old-old edge repairs

The source has girth5. Its boundary A∪B consists of8 distinct vertices with
no H edge among them. Each has degree4 in H; every other retained vertex
has degree5. Therefore any additional old-old edge under maxdegree5 must
join two boundary vertices, and each boundary vertex can be used at most
once: every allowed repair is a partial matching on those8 points.

Every partial matching can be extended to a perfect matching on the
remaining even number of boundary vertices. These extra edges are allowed
because the boundary is independent, and cannot increase any distance.
Thus if any partial repair had diameter≤3, some complete matching would
also have diameter≤3. Excluding all105 complete matchings excludes every
old-old edge repair in this exact retained-H/max5 operation.

The105 matchings split as24 all-cross,72 with one A-A pair and one B-B pair,
and9 with two A-A pairs and two B-B pairs. Only the latter81 types were new.

## Correct exact boundary route condition

Let mate(s) be the boundary vertex matched to s. For any distinct boundary
vertices s,t, a shortest path in H+M of length≤3 has the following forms.

It may use no matching edge, which is exactly an existing H path of length
at most3. If it uses one matching edge, that edge must be first or last:
placing it in the middle would require an H edge between two boundary
vertices. Two matching edges cannot be consecutive on a simple path because
a matching has degree1, and separating two of them within3 steps would
again require an H edge within the boundary. Three matching edges add only
backtracking. Thus the exact condition is

    d_H(s,t)≤3
      OR d_H(mate(s),t)≤2
      OR d_H(s,mate(t))≤2.

Distance0 is included in the last two terms, so direct matching is covered.
The existing-H term is retained, including all alternatives that existed
before any new edge. This is a derived equivalence for boundary pairs,
not an unsupported heuristic cut.

## Actual cache binding

The source controller is compared literally to the one embedded in the
earlier BOUNDARY_CERTIFICATE.json. Same-side H≤3 matrices and cross-side
H≤2/common-neighbor matrices are reused from that actual evidence.
Distinct same-side vertices have no H common neighbor by the source's
girth5, while H≤2 includes the diagonal distance0.

For a cross pair A_i,B_j, the old path A_i-u-v-B_j always has length3.
Any old path of length≤3 that uses u or v must be exactly this one: an
alternative through only u would need an old A-B edge, and likewise for
only v; those edges do not exist by girth5. Consequently

    d_H(A_i,B_j)>3
      iff A_i-u-v-B_j is the unique old path of length≤3.

The source's saved unique-distance3 ledger gives precisely these entries,
so it supplies the previously unstored cross H≤3 matrix without a new
source BFS or shortword enumeration. H_BOUNDARY_CACHE.json records all
180 complete8×8 distance≤2 and distance≤3 Boolean matrices and this bridge.

## Why the old pure-cross argument cannot be reused

The prior proof relied on every new matching edge going between A and B.
That condition is now false, and same-side matching really can repair a
previous unique cross pair without directly joining its endpoints.

For example, delete source vertices0,45. The boundary is

    A=[51,59,62,71], B=[15,18,56,58].

Take the new matching

    {51--59,62--71,15--18,56--58}.

The old unique cross route51--0--45--18 is destroyed, but the same pair now
has the three-step route51--59--36--18, using one new A-A edge. Vertices51
and18 are not directly matched. This explicitly disproves extending the
old must-directly-match argument to the new rule.

The same matching nevertheless loses another boundary obligation:51 and62
have no length≤3 path. All three terms of the exact boundary condition are
false for that pair. OLD_CROSS_ARGUMENT_ESCAPE_EXAMPLE.json saves the
repaired path, actual matching and separate remaining failure. The outcome
is an incompatibility between simultaneous route requirements, rather than
a denial that the relaxed rule adds useful routes.

## Complete new finite result

For each of180 deleted edges, all81 new matchings were evaluated on the28
unordered boundary pairs. BOUNDARY_ATTEMPTS.json records the first failed
pair and the three false route terms for every one of14580 assignments;
BOUNDARY_SURVIVORS.json is empty. The first-failure categories are

    A-A:7190, A-B:7318, B-B:72.

The source controller, matching generation and exact cached matrices make
this a finite proof certificate. It is not an unknown solver result or a
failure inferred from a partial total bad-pair score. With no surviving
boundary assignment there is no need to check all70 roots of a new graph.

Combined with the inherited24 pure-cross failures, this closes **every
old-old edge repair under maxdegree5 after deleting an adjacent pair from
this Exoo72 source while retaining all other source edges**.

Stop this local surgery family. Nonadjacent2point deletions,4point
deletions, other source graphs, further deletions of retained edges and
general70vertex controllers are outside the proof. The potential4480vertex
fiber graph remains ungenerated; no new degree-diameter example, Lean
theorem or SAT result is claimed.
