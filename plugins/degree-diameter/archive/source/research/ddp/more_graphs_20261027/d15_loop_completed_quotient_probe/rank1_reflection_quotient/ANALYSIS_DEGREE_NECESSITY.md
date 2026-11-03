# A nonloop channel also excludes non-automorphic reflection quotients

This strengthens the completed gate without another matrix test, solver or graph. The scope is still the same two intrinsic rank-one reflections at each controller, but the folding need no longer be assumed an automorphism. Its quotient must use **all projected source edges**, including the neighbors of both members of a two-point class. The earlier one-representative shortcut is valid only after an automorphism is established.

Consider a source controller a with no self arc and a nonfixed point x. Write x'=R_a*x. Its five channels have different target controllers, so their target-orbit neighbor counts add and none is removed as a source-class loop.

For the unique minus-input port, B annihilates x'-x, so its two old neighbor lines coincide. If the target noise is minus, that line is invariant and gives two target classes: one fixed point and one pair. If the target noise is plus, its three points represent three different classes, whether fixed or paired with points outside the line. Thus this channel contributes2 or3.

For each of the other four ports, x'-x is along the source minus axis, not that port's kernel. Their images in the target noise quotient differ, so the two parallel three-point lines are distinct. If the target noise is minus, each line is independently invariant under the target reflection; they give four classes in total. If the target noise is plus, the target reflection either exchanges the two lines, giving three classes, or gives no cross-line identifications, giving six. Any single cross-line identification would map the entire parallel line to the other because the noise direction is preserved.

The smallest possible sum is2+4*3=14. Requiring degree at most14 at every such source orbit forces the chosen minus port to have minus target noise, and every other channel to have plus target noise and exchanged neighbor lines. For a plus channel, exchange is exactly

    (Q_v*R_b*B - B*R_a)*x = 0.

It must hold for every nonfixed x. The complement of the source fixed hyperplane spans the entire vector space: it contains u and u+h for every fixed h, so their differences span that hyperplane as well. Therefore the displayed linear map is zero everywhere. On the minus channel the matching signs already make the identity automatic. Consequently maxdegree<=14 is possible at a nonloop controller only when all its outgoing arcs satisfy the same compatibility equations used in the original automorphism gate.

The saved table has a direct witness. Arc_id5 is controller1->4. Controller1's five outgoing targets in that existing table do not include1, so it is nonloop. All four state pairs(0,0),(0,1),(1,0),(1,1) are forbidden. Their complete saved matrices are copied unchanged to NONLOOP_ZERO_ALLOWED_ARC.json; no matrix was recomputed. Thus for every global choice assignment, some nonfixed class at controller1 has degree above14 in its true quotient. This excludes every quotient from this fixed two-choice reflection family at the required degree, even when it is not an automorphism.

The aggregate saved counts also imply many such obstructions:3840 choice pairs minus3648 forbidden leaves192 allowed pairs, so at least768 of960 arcs have no allowed pair. The24 loop controllers contribute at most120 outgoing arcs, leaving at least648 zero-allowed nonloop arcs. These are bounds derived from existing counts, not a new per-arc census. The single literal arc5 is already sufficient.

No quotient labels, actual quotient graph, new diameter, general degree-CSP or alternative reflection is produced. The hypothetical10368/max14 construction remains ungenerated. This does not exclude arbitrary partitions, other involutions or general(14,4) graphs. The original two-SAT UNSAT receipt and conditional automorphism quotient proof remain intact; the stronger degree conclusion is a separate paper consequence of their already saved compatibility data.
