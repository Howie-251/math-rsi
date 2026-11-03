# Exact source-specific clone-and-cut obstruction

Let G be the existing252-vertex5regular diameter4 source. Choose a prototype x and an edge set F containing no edge incident with x. Write H=G-F. Add one new vertex y adjacent to every vertex of the unchanged five-element neighborhood N_G(x)=N_H(x). Call the extended graph K.

## Full-neighborhood cloning preserves all old-pair distances exactly

The map fixing every old vertex and sending y to x is a graph homomorphism from K to H: each new edge yv maps to the retained edge xv of H. Therefore every K-walk between old vertices maps to an H-walk of the same length. Conversely H is a subgraph of K. Hence for all old p,q,

    d_K(p,q)=d_H(p,q).

In particular, the clone cannot repair any old-old distance that was spoiled by deleting F. Conversely, if H has diameter at most4, then all new-old distances are at most4: for t!=x, take a shortest H-path from x to t and replace its initial x by y; for t=x, use y-v-x of length2 through any retained neighbor v. Thus, under the unchanged-star hypothesis, K has D<=4 exactly when H has D<=4.

Since every neighbor of x had degree5 in G and gains a new incident edge, a legal maximumdegree5 K requires at least one deleted incidence at each of these neighbors. In particular F cannot be empty.

## Critical-edge certificate from complete short-word intersections

Assign one edge ID to both directions of each of G's630 edges. For each root p, enumerate every nonbacktracking walk of length0 through4, including the empty walk. There are exactly

    1+5+20+80+320=426

prefixes per root. For each endpoint q, intersect the edge sets of all such walks ending at q. An edge e lies in this intersection if and only if G-e has no p-to-q path of length at most4. For necessity, any such path would itself be nonbacktracking and avoid e. For sufficiency, a surviving nonbacktracking route is already a path/walk of the required length; arbitrary immediate reversals can also be removed without creating use of e. The empty diagonal route contributes the empty mask, correctly preventing a spurious p=p obstruction.

The producer performed the full252-root route enumeration, totaling107352 prefixes. It did not run source BFS or generate modified graphs. All630 edges occur in at least one endpoint intersection. CRITICAL_WITNESSES.json records, for each edge, the first root and endpoint, the number of enumerated routes to that endpoint, one route, and all common edge IDs. NONZERO_ROUTE_INTERSECTIONS.jsonl preserves the complete40110 ordered root/endpoint records having a nonempty intersection. These ordered records are not a count of ordinary bad pairs in a generated graph.

Now take any nonempty F. It contains some critical edge e. Its saved witness p,q has no length<=4 route in G-e, and deleting further edges cannot restore one, so H=G-F also has d_H(p,q)>4. The clone-fold identity then gives d_K(p,q)>4. Therefore no prototype and no legal deletion set in the stated unchanged-star/full-neighborhood-clone rule can give a253-vertex maximumdegree5/D4 graph.

The result is confined to this fixed source and full-neighborhood clone with its entire prototype star retained. It does not exclude arbitrary253-point graphs, clones with different anchors, deletion of prototype-star edges, other source surgery, or the earlier252-to254 finite four-matching/two-hub experiment. No cut-set search or candidate graph is needed after the complete critical-edge obstruction.
