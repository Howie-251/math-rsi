# Paper obstruction for an invariant pin set, with arbitrary internal rewiring

This independently checks the stronger pin-set prediction. No numerical
enumeration, solver, graph or distance check was run. In particular this note
does not report the outcome of the separately proposed1764-set necessary gate.
Earlier symmetry-preserving exclusions and experimental RESULT files remain
unchanged.

## Fixed model and inherited source facts

The accepted source G has106 vertices, diameter at most2 and maximum degree11.
Its verified order-seven automorphism has eight fixed points

    F={7,17,23,34,46,54,59,105}

and fourteen orbits of size7. Every nonfixed vertex has degree11. Fixed
vertices34 and54 have degree10 and all other fixed vertices have degree11.

Select a pin set S of size10 or11 which is invariant under this source C7.
Add z adjacent precisely to S. Change old edges only inside G[S]; every
cross edge and every edge outside S stays unchanged. The final internal
rewiring is arbitrary and need not preserve any automorphism. Require the
final graph to have order107, maximum degree11, and diameter at most2.

Every vertex of such a final graph must have degree at least10: a degree-d
root can reach at most1+11d vertices in two steps under maximum degree11,
which is at most100 if d<=9.

Applied to z, this also shows that the sizes10 and11 exhaust all possible
pin-set sizes under this cap and target order.

Since there are only eight fixed points, invariance forces

    S=O union K,
    |O|=7, K subset F, q=|K| in{3,4}.

There is exactly one free orbit O. This orbit decomposition is only a
property of the selected set and the source; it imposes no symmetry on the
final edges.

Write:

* r for the source internal degree of G[O];
* k for the number of fixed neighbors of a point of O;
* h for the number of those k fixed neighbors that lie in K.

The source action makes these numbers constant on O. Its induced graph on
O is a union of undirected cyclic-difference rings, so r belongs to{0,2,4,6}.
Also0<=h<=k. A fixed source vertex has neighbors in at most one free orbit:
two such orbits would require at least14 neighbors, exceeding11.

## A necessary degree condition without any final symmetry

Each u in O has exactly r+h source neighbors inside S, hence11-r-h
unchanged cross neighbors. After adding z its final degree is

    12-r-h + d_final_inside_S(u).

The final internal degree is nonnegative. The cap11 therefore requires

    r+h>=1.                                             (1)

This step does not assume an even final internal degree or an invariant
final graph.

## Source domination bound with the selected fixed stars separated

For an old point outside S, a length-at-most-two route to z must use an
unchanged cross edge to a point in S. Thus a necessary condition is

    N_G[S]=V(G).                                        (2)

Selected old points are included by the closed neighborhood; no extra open
domination condition is introduced for them.

The source fixed neighbors of O are precisely k fixed vertices, each joined
to all seven points of O. Counting incidences to outside free points gives

    |N_G[O]| <= 7 + 7(11-r-k) + k
              = 84-7r-6k.                              (3)

Each of the h fixed points in K adjacent to O has all its free neighbors
inside O, since it cannot meet a second seven-orbit. Those free points are
already in N_G[O]. Each of the other q-h points in K contributes at most
seven free points. Finally at most8-k fixed points are not already covered
by N_G[O]. Hence

    |N_G[S]| <= 84-7r-6k + 7(q-h) + (8-k)
              = 92+7q-7(r+k+h).                        (4)

All overlaps only decrease this upper bound. In particular the subtraction
of h is valid because it concerns entire source fixed stars, not their final
possibly asymmetric internal edges.

## Size10 is impossible

For q=3, (2) and (4) require

    r+k+h<=1.

If r>=2 this is impossible. If r=0, (1) forces h>=1; since k>=h, we instead
have r+k+h>=2. This excludes all invariant size10 pin sets, regardless of
how their internal edges are rewired.

## Size11 has exactly two possible boundary forms, both impossible

For q=4, (2) and (4) require

    r+k+h<=2.

Together with (1), h<=k and the even source degree r, this leaves only:

    (A) r=2, k=h=0;
    (B) r=0, k=h=1.

Values r>=4 are excluded directly by the bound.

### Boundary A: the source seven-cycle forces a duplicated outside endpoint

When r=2, the source G[O] is a seven-cycle, since any nonzero difference
generates the cyclic group of prime order7. Two points at cycle-distance3
are nonadjacent and have no common neighbor inside O. The source has
diameter2, so they share a neighbor outside O. Since k=0 this common neighbor
is not fixed. At least two of the7*9 outside incidences therefore have the
same endpoint. Thus (3) is strict:

    |N_G[O]|<=69,
    |N_G[S]|<=69+28+8=105<106.

This contradicts (2), using only the source cycle and source diameter. The
final internal graph need not be cyclic or symmetric.

### Boundary B: all seven orbit pins are forced internally isolated

There is a unique fixed source neighbor f of O, and f is selected in K.
Each point u in O has source internal degree r+h=1, namely its edge to f,
and has10 frozen cross neighbors. After adding z it already has degree11.
Consequently every final internal degree d_final_inside_S(u) is zero.

All seven edges from f to O must therefore be deleted, and no new edge from
an O point to any other selected pin can be added. The only new old
neighbors f can obtain are among the other three fixed points of K. Even
giving f all three such new edges, and allowing its original degree to be11,
its final degree is at most

    11-7+1+3=8.

This contradicts the necessary minimum degree10. No symmetry assumption
was used to force the final degree of an O point: its10 frozen cross edges
and its edge to z already fill the cap.

## Disposition and consequence for generation

The stronger paper prediction is supported. For this source and this
actual C7 action, no invariant pin set S of size10 or11 can support the
order107/max-degree11/diameter2 augmentation when only old G[S] is modified.
The final internal rewiring may be completely asymmetric.

Thus replacing an internal circulant by a noninvariant internal graph while
keeping the same orbit-invariant pin set does not evade the obstruction.
Within the current edge-edit model, a viable next generation rule must use
a pin set not invariant under this particular C7. Alternatively it must
change the frozen-cross-edge model. Neither alternative is tested here.

This does not rule out noninvariant pin sets, changing edges outside G[S],
other sources, different degree caps or larger augmentation models. It is
also separate from the earlier numerical internal-S MILP UNKNOWN; that
run's status is not rewritten as a completed solve.
