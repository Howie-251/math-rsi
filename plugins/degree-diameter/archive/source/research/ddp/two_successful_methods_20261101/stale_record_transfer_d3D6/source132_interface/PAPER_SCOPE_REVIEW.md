# Cubic Exoo132 →134: paper interface only

2026-11-01. No source literal, adjacency, graph/BFS, field or numerical search was read/run for this note. The source owner located the official diameter6 entry Exoo132 (1998) and saved its upper-adjacency literal. This is the published cubic(3,6)132 source, **not** the unrelated(6,3)/PSL132 object. Retrieval/metadata alone is not a new source acceptance; the proposed construction is conditional on the primary source's cubic/D6 facts. No numerical batch is authorized by this note.

**Why target134 rather than133.** In any maximum-degree3 graph, a root ofdegree≤2 has at most

    1+2*(1+2+4+8+16+32)=127

vertices within6 steps. A diameter≤6 graph on133 vertices would therefore have everydegree3. Its degree sum399 is odd, impossible. Thus133 is excluded even without assuming regularity in advance.134 is the next possibleorder; this does not assert its existence. Every successful134-point maximum3/D6 graph would likewise be cubic and have201edges.

**Operation and degrees.** Assume the old132 graph is cubic with198edges. Delete three vertex-disjoint oldedges, giving six distinct free endpoints. Choose two for a permitted old-old nonedge repair; partition the otherfour into pairsA,B. Join a newx toA, a newy toB, and addxy. The repair must not duplicate an edge in the deleted host. Each oldendpoint loses then gains one edge, all other olddegrees stay3, and each newvertex has two oldpins and onepeer. Therefore

    n=134, m=198−3+1+4+1=201,

with everydegree3. These are degree/edge identities, not a diameter certificate.

**Exact cooperative new-old condition.** LetH be the old graph after the threecuts andrepair. A shortestx-to-oldtargett route that usesy can replace its entire prefix toy byxy; afterwards it stays inH. Hence

    d_J(x,t)=min(1+d_H(A,t), 2+d_H(B,t)),
    d_J(y,t)=min(1+d_H(B,t), 2+d_H(A,t)).

Both helpers reach everyoldvertex within6 exactly when

    R4_H(A) ∪ R4_H(B) ∪ (R5_H(A) ∩ R5_H(B)) = V(H).

If either pair is within4 oft, both helpers can use thatpair with at most onepeer step. Otherwise both pairs must be within5. The balls are closed and belong to the modifiedhostH, not an inherited original-source profile. Helper-helper distance is already1.

For the analogousD5 rule the condition isR3(A)∪R3(B)∪[R4(A)∩R4(B)]. TheD6 threshold adds one layer to each required ball. On a fixedhost this is a weaker cover condition, giving a concrete reason to consider a bounded trial. The source andorder here are different, so that extra layer does not guarantee a hit or overturn any actualAFY70/D5 failure.

**Old-old coverage remains separate.** Both helperconditions only control pairs involving newvertices. Forold u,v the shortest route may avoidhelpers, use one, or use thepeeredge; its distance is the minimum of

    d_H(u,v),
    d_H(u,A)+2+d_H(A,v), d_H(u,B)+2+d_H(B,v),
    d_H(u,A)+3+d_H(B,v), d_H(u,B)+3+d_H(A,v).

The helpercover condition does not bound this minimum by6. Deleting oldedges can damage a former source route, while the repair/peer shortcuts may or may not compensate. A genuine candidate therefore needs exact final newroot checks followed by complete final old-old coverage; a newrootpass cannot stand in for fullD6.

No earlier ordinarytwo-cover ofAFY70 or itsD5 cut/repair experiments are exclusions of this new132-source operation. No symmetry reduction, sourcegirth or bipartite premise is assumed. This paper/interface checkpoint adds no134graph, sample result, sourceBFS or newparameter/Lean. Any subsequent numerical work belongs to the root's separately authorized fixed sample/CPU scope and the sole numerical owner; it is neither executed nor certified by this note.
