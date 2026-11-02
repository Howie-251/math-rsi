# Source non-D3: controllers0 and1

The bounded prediction is supported: the125 three-type words from controller0
have82 distinct endpoints and omit controller1. Type0 fixes controller0, so
these125 endpoints also contain every endpoint of a word of length0,1 or2.
The complete literal125-entry certificate is LOWER_D4_CONTROLLER_RESULT.json.
Selection cost0.013533367CPU seconds under2CPU; no graph body was read and
no BFS, field/rank computation, solver or Lean compilation was performed.

Let c(u)=floor(u/81). By the actual typed source definition, an edge u--v
has either v=forward(u,p,t) or u=forward(v,p,t). The first case gives
c(v)=controller(c(u),p). In the second case the already kernel-proved
controller_reverse_type identity rewrites this as

    c(v)=controller(c(u),inverseType(p)).

This argument uses only the controller inverse identity; it does not need
the pending five affine reverse identities or source degree theorem. An
edge whose endpoints share a controller still contributes a legitimate
controller transition. Do not remove such transitions merely because the
controller labels agree: the physical source vertices can differ.

Induction on a true source Walk converts any walk from controller0 with
length<=3 to a typeword of the same length with the same target controller.
Prefix it with enough type0 transitions at controller0 to obtain exactly
three types. Controller1 is not among the125 endpoints, a contradiction.
Therefore for arbitrary x,y in Fin81 there is no source Walk of length<=3
from liftAt(0,x) to liftAt(1,y). In particular the concrete labels0 and81
give non-D3. This is a lower-distance obstruction, not a proof of D<=4;
the latter remains the separate all-controller affine/coset construction.

For the837-clone graph, FullNeighborhoodClones.collapseHom maps any walk
between the old labels0 and81 to a source walk of the same length. The
same obstruction therefore yields non-D3 for the final graph, with no new
final-root enumeration. Its D<=4 follows separately once the complete
parent bound and non-isolation are instantiated.

Kernel work still required: the concrete125-case controller exclusion,
the source-edge projection lemma and Walk induction. This file does not
claim a new compiled theorem, complete source FinalClaim, or Lean46.
