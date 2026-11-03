# Fixed F5 fiber quotient: a valid750-point quotient and a five-sheet ceiling

This bounded transfer check found no improved degree/diameter lower bound. It did identify an exact common translation of the verified3750-point graph. Its quotient is explicitly750 vertices,20-regular, and diameter3. The original graph is a regular five-sheet cover of that quotient. A single cached controller route proves that every ordinary cover of this exact quotient with more than five sheets fails diameter3.

The frozen prediction that the compatible translation space was zero was **refuted**: its actual dimension is one. The new translation does not lower degree. No graph, whole-graph BFS, candidate sweep, new controller, or noise-set search was run. The current3750-point result and its pending global novelty status are unchanged.

## Source and exact quotient conditions

Use the literal source parameters in `../f5_full_d20_D3/PARAMETERS.json`. A vertex is `(a,x)` with a in the fixed30-controller and x in V=F5^3. At port p, with controller neighbor b, its five neighbors are

    (b, T_p x + t*d_p),     t in F5,

where d_p is the direction at the reverse port. The four controller neighbors are distinct. The source's order3750, degree20, and diameter3 are inherited from its existing independent and formal certificates, not recomputed here.

For any subspaces W_a, define the **full** quotient by identifying x modulo W_a in each controller fiber. The set of neighbors of `(a,x+W_a)` through port p is exactly

    pi_b(T_p x) + pi_b(T_p W_a + <d_p>).

Consequently

    N = sum_a 5^(3-dim W_a),
    degree(a) = sum_p 5^r_(a,p),
    r_(a,p) = dim(T_p W_a + <d_p> + W_b) - dim W_b.

The full quotient inherits diameter at most3: project a source path and remove repetitions. This is a distance upper bound, not an assertion that individual distances are unchanged. A port contributes1,5,or at least25 neighbors when its rank is0,1,or at least2. Thus degree at most20 requires every port rank at most1; maximum degree below20 additionally requires a rank-zero port at every controller vertex.

Using one representative of a fiber class reproduces the full quotient neighbor set exactly when

    T_p W_a subseteq W_b + <d_p>.

Descending every individual fixed-t affine map would require the stronger `T_p W_a subseteq W_b`. The weaker relation condition is sufficient here and is essential: the actual common translation below does not give a common invariant line for all four matrices.

The single frozen direction test W=<e0> produced ranks `[1,1,2,2]`, hence750 vertices and degree60. It refutes the tempting degree16/20 representative shortcut for that partition; no other direction templates were tested.

## Actual common translation and explicit750-point graph

A simultaneous fiber translation `(a,x) -> (a,x+h_a)` is an automorphism precisely when

    h_b - T_p h_a in <d_p>

on every controller edge. The single fixed homogeneous system has120 scalar equations in90 field variables. Its saved reduction has rank89 and one-dimensional nullspace. A basis has the same vector

    h = (0,3,1)

in all30 fibers. In particular,

    T0*h = h + 2*e1,
    T1*h = h + 3*e0,
    T2*h = T3*h = h.

Thus simultaneous translations by t*h form a free C5 action on the graph. The matrix and full row reduction are in `TRANSLATION_SYSTEM.json`. This establishes the compatible translation subgroup; no claim of a complete automorphism-group classification is made.

Choose quotient coordinates

    pi(x0,x1,x2) = (u,v) = (x0, x1-3*x2).

The vertex set is the fixed30-controller times F5^2. Through the four ports, the explicit relations are, with t ranging over all F5:

| Port | Neighbor fiber coordinate |
|---|---|
|0 | `(2v, u+2v+t)` |
|1 | `(v+t, 3u)` |
|2 | `(2u+3v+t, 2u+4v+3t)` |
|3 | `(2u+v, 4u+v+2t)` |

Every relation has five distinct targets, and different ports have different controller targets. The graph is therefore simple and20-regular on750 vertices. Its diameter is at most3 by projection. Since750 exceeds the degree20 diameter-two Moore bound401, its diameter is exactly3. This is a fully specified formula quotient, not an exported or newly BFS-checked edge list.

The line <h> meets none of the four noise lines nontrivially. Hence projection is bijective on each source vertex's20 neighbors. The source-to-quotient map is an ordinary graph covering with five sheets, and C5 acts transitively on each covering fiber. Its validity is stronger than just a surjective graph homomorphism.

This concrete parameter `(20,3,750)` is dominated by the already verified `(20,3,3750)` source. It supplies no new lower bound or new target parameter worth a graph-production batch.

## A cached short-route obstruction to larger covers

The existing `controller_structure.json` has `NB3_counts[0][3]=1`. The source neighbor lists give `C[0]=[18,20,2,9]`, `C[3]=[17,21,5,1]`: these controllers are distinct, nonadjacent, and have no common neighbor. Their unique length-three controller path is

    0 -> 2 -> 1 -> 3,     ports [2,0,2].

No new path enumeration was performed. For this one stored route the full source's three noise coefficients have matrix

    B = [[4,3,1],
         [3,4,1],
         [0,0,1]],

of rank3. Applying pi gives

    pi*B = [[4,3,1],
            [3,4,3]],

of rank2. Therefore, from any chosen starting source lift over controller0, the125 noise triples project onto all25 target points over controller3, exactly five triples per target point. The covering property ensures that different triples describe different quotient walks: a quotient walk has a unique lift from the chosen source vertex. Conversely there are no other quotient walks of length at most3 to that target controller because its controller route is unique and has no shorter alternative.

Thus each such quotient target has **exactly five** walks of length at most3 from the fixed quotient root. In any k-sheet ordinary cover of this exact750-point graph, these five walks have at most five endpoints over that target. Diameter at most3 would require reaching all k endpoints. Hence

    k <= 5.

The original3750-point graph attains k=5. This proof does not infer a quotient path count merely from a unique path upstairs: it uses the cached unique controller path, the explicit rank-two projected noise map, and the covering property. It applies to ordinary covers of this specific quotient only; changing the controller, its edges, or the base relations is outside the conclusion. It makes no diameter4-or-higher exclusion.

## Scalar orbit controls and scope

Homogeneity gives simultaneous scalar automorphisms. The two frozen local controls, checked on one125-point fiber, yielded:

| Scalar subgroup | Quotient order | Degrees per controller fiber | Maximum degree | Diameter |
|---|---:|---|---:|---:|
| `{1,-1}` |1890 | one degree12, eight degree18, fifty-four degree20 |20 |3 |
| F5* |960 | one degree8, four degree17, twenty-seven degree20 |20 |3 |

Projection gives D<=3; both orders exceed401, proving exactD3. These quotients also lose order without lowering maximum degree. No additional subgroup quotient, controller-permuting automorphism, or mixed-dimension partition was searched or classified. The general rank formula remains a checkable condition for a future independently justified proposal, not authorization for a template sweep.

The relevant inherited failures were read, not rerun: the fifteen-degree source's fixed two-choice reflection partition obstruction, and the two fixed F5 restricted-noise degree10/D4 domains. This task changes the operation to a full quotient and an ordinary-cover ceiling; it does not reinterpret those failures as new tests.

`RESULT.json` records0.044410258 CPU seconds for the fixed linear/local check. `QUOTIENT_AND_COVER_WITNESS.json` records0.002111506 CPU seconds for the unique translation and cached-route calculation. Total diagnostic CPU is0.046521764 seconds, one worker, under30 seconds. There are zero new graphs, BFS runs, or path enumerations. The bounded task is complete with no production proposal supported by these quotients.
