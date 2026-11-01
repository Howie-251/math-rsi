# Eight matching locks at 24 vertices

Let H be a pair-covering simple 5-uniform hypergraph on 24 vertices with
34 edges, minimum degree at least six, and r vertices of degree six. Let t
be the number of vertices of degree seven. Then

\[
170=\sum_v d(v)\ge6r+7t+8(24-r-t),\qquad t+2r\ge22.
\]

For a degree-seven vertex x, the weighted degree in the nonunit codegree
graph is exactly

\[
\sum_{y\ne x}(\lambda(x,y)-1)=4\cdot7-23=5.
\]

Partition the degree-seven vertices into three classes minimizing the total
weight of edges internal to a class. Each vertex has internal weighted degree
at most one: otherwise minimality forces weighted degree at least two to each
of the other two classes, contradicting its total weighted degree at most five.
Thus every class induces a matching whose edges have weight one (codegree two).

A degree-six vertex has total nonunit weighted degree exactly one. Its unique
exceptional partner may be another low vertex, a seven-degree vertex, or a
higher-degree vertex. It can be appended to at least two of the three classes
without creating any nonunit low/high pair: exclude the partner's class if that
partner has degree seven; otherwise all three classes are available.

For i=1,2,3 let S_i consist of class i together with **all** low vertices
available to it. Each S_i induces a nonunit matching: high/high edges form the
class matching, low/low edges form a matching because every low has a unique
partner, and low/high pairs are unit. Moreover

\[
\sum_i|S_i|\ge t+2r\ge22.
\]

Therefore one S_i has at least eight vertices. Any eight of them have degrees
six or seven and all codegrees one except for a codegree-two matching. No
matching edge joins a six-degree lock to a seven-degree lock.

In the currently open cases r=1,2,3,4, any seven of these eight locks have at
most four degree-six vertices. An eighth actual lock remains available for
residual local types. This is a selection lemma only; the associated complete
probability classification is still being checked.
