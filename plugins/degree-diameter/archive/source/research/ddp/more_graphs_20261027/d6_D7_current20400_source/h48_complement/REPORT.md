# Actual H48 complement and the source's small semidirect recipe

The fixed recovery succeeded at candidate17of at most425N-twists.
No new graph, BFS, large-group enumeration or field assignment was
performed. Both dependent agents received the completed recipe before
this report was written.

Let alpha be the actual source generator A, of order16, and let
beta0=B^4, of order3. Using the previously verified N-basis a,b,z,
the first successful twist in index order i+5*j+25*k is

    beta = a^1 b^3 z^0 beta0.

The actual tests establish beta^3=1 and beta≠1, and
alpha*beta*alpha^(-1)=beta^(-1). These comparisons use0images of
actual group elements, sound because the source action is regular.
CANDIDATE_TESTS.json preserves all17tested records; it is not an
enumeration of all425possibilities.

The48normal forms beta^u alpha^v, u modulo3 and v modulo16, have
distinct N-cosets. The relation above bounds their generated group
by48normal forms, while these distinct cosets give48distinct elements.
Thus H=<beta,alpha> has order48and is a complement to N. Its law is

    (u,v)*(U,V) = (u+(-1)^v U mod3, v+V mod16).

Actual conjugation on N gives the following column-vector actions:

    M_alpha = [[4,2],[1,1]] mod5,
    M_beta  = [[0,4],[1,4]] mod5.

Equivalently the centered source matrices are [[-1,2],[1,1]] and
[[0,-1],[1,-1]]. On C17, chi_alpha=5 has order16and chi_beta=1.
The expected beta matrix, beta's cubic relation, alpha's16th relation
and the inversion relation were checked in the actual basis.

Every group element is uniquely n(x,y,c)*beta^u*alpha^v, with x,y
modulo5 and c modulo17. Its multiplication is

    (n,h)*(n2,h2) = (n + rho(h)*n2, h*h2),

where rho(beta^u alpha^v) has matrix M_beta^u*M_alpha^v on F5² and
scalar5^v on C17. The three positive source generators are:

| Source generator | Normal F5² vector | c17 | u | v |
|---|---|---:|---:|---:|
| A | (0,0) | 0 | 0 | 1 |
| B | (0,2) | 1 | 1 | 12 |
| C | (0,4) | 5 | 2 | 11 |

SOURCE_SEMIDIRECT_RECIPE.json contains these and the three actual
inverse generators, the48Hidentity images, their N-cosets, matrices,
scalar action and the full convention. Permutations act on the left;
source graph steps are right multiplication g*s. All20400source
vertices were assigned their group coordinates by the already known
N-coordinate offsets relative to the H-coset representative.

The resulting semidirect right-multiplication rule matched every
one of122400directed source adjacencies, equivalently61200undirected
edges. It is therefore an actual small algebraic source recipe,
not merely a guessed abstract group or a few sample products. This
does not rerun or prove the original D7through graph distances.

The binary vertex_group_coordinates.u32le.bin gives the uint32
quintuple(x,y,c,u,v) per old vertex, and beta.pi.u32le.bin preserves
the actual complement generator. Total recorded CPU was0.167127
seconds. The recovery is terminal; new field7/8/9representations and
graphs belong to the separately assigned agents and were not tried here.
