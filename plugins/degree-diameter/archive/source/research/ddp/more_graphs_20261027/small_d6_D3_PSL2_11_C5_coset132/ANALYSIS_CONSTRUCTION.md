# PSL2(11)/C5: valid construction and complete ten-choice scope

Verdict: **VALID**. The ten selfpaired5-neighbor orbitals, each augmented by the unique normalizer matching, cover every simple undirected graph of maximum degree at most6 invariant under this fixed transitive PSL2(11) action that could have D<=3. This review uses paper algebra only: no matrix enumeration, coset generation, graph, solver, word enumeration, or BFS is run here. The original [question](ROOT_QUESTION_NOT_EXECUTED.md) remains historical proposal evidence; the producer owns the actual binding and numerical results.

## Matrix group, stabilizer, and normalizer

Let G=SL2(F11)/{I,-I}. There are(11^2-1)*11=1320 determinant-one matrices, hence |G|=660. Matrices and their negatives represent the same projective element.

Let h be the class of diag(3,4). Its determinant is1 modulo11, and3 has order5, so H=<h> has order5. The matrix t=[[0,1],[-1,0]] has square -I, hence its class is an involution. It swaps the two eigenlines and conjugates h to h^-1.

Every element normalizing H must preserve or swap H's two common eigenlines. Its matrix is therefore diagonal or antidiagonal. The projective diagonal determinant-one torus has order5, and there are five antidiagonal classes. Consequently N=N_G(H)=<H,t> is dihedral of order10 and contains exactly five involutions.

Use vertices xH. There are660/5=132 of them, and left multiplication by G is transitive. An H-fixed vertex xH satisfies x^-1 H x<=H and hence, by equal orders, x in N. Thus H has exactly two fixed vertices, H and tH. All remaining130 vertices have H-orbit length5, since H has prime order. There are26 such suborbits.

## Exactly ten selfpaired5-suborbits

For g outside N, the intersection H intersect gHg^-1 is trivial: a nontrivial intersection would equal H and make g normalize H. Thus the double coset HgH has25 elements and corresponds to five vertices in its root suborbit.

There are exactly55 projective involutions. A trace-zero determinant-one matrix has form [[a,b],[c,-a]], with bc=-1-a^2. Since -1 is not a square in F11, the right-hand side is always nonzero. There are11 choices for a and10 nonzero choices for b, with c determined. The110 matrices form55 distinct classes modulo sign, each squaring to -I. Conversely, a nontrivial projective involution has such a trace-zero representative: a determinant-one matrix squaring to I would be I or -I, whereas the nontrivial projective case squares to -I.

Exactly five of these involutions lie in N, leaving50 outside N. If g is an outside involution, HgH is inverse-closed. Its involutions are precisely the five H-conjugates of g. Indeed, the representation h1*g*h2 is unique because the intersection above is trivial. If it squares to1, put u=h2*h1 in H. Then g*u*g=u^-1. A nonidentity u generates H and would make g normalize H, a contradiction. Thus u=1, and h1*g*h2=h1*g*h1^-1. The five conjugates are distinct by the same normalizer argument.

Conversely, any inverse-closed outside double coset has odd size25. Inversion is an involution of that finite set, so it has a fixed element. The double coset does not contain identity, hence this fixed element is a nontrivial involution. Therefore the50 outside involutions partition into exactly50/5=10 inverse-closed double cosets. These are ten orbital choices in the fixed action, not a claim of ten nonisomorphic graphs. The remaining16 five-suborbits form eight inverse pairs.

## Adjacency, degree, and action

For one of those ten double cosets, take

    D = HtH union HgH,
    xH adjacent to yH iff x^-1*y belongs to D.

Equivalently the neighbors of xH are xD/H. Replacing representatives x by xh and y by yh' changes x^-1*y to h^-1*x^-1*y*h'; membership is unchanged because D is H-biinvariant. Thus the definition is independent of representatives.

D contains no element of H, so there are no loops. Its two parts are disjoint, and the neighbor count is(5+25)/5=6. Both parts are inverse-closed because t and g are involutions, giving an undirected simple6regular graph on132 vertices and396 edges. Left multiplication by any group element preserves adjacency, proving transitivity. The matching part alone sends xH to xtH and is a genuine perfect matching because t normalizes H and t^2=1 in G.

Connectedness does not follow merely from these counts or transitivity. The component of H is determined by <H,t,g>; if this is a proper subgroup the graph is disconnected. A candidate still requires complete actual radius3 coverage, and a first positive receives the parent's independent validation. No old660-vertex graph or diameter result is used in this proof.

## Why no other invariant maxdegree6 target is omitted

Every graph invariant under this G action has an H-invariant neighborhood at H, hence a union of H-suborbits. For an undirected graph, that union is closed under pairing each suborbit with its inverse. Excluding the loop at H, the only length-one suborbit is the matching neighbor tH. Every other suborbit has length5. A nonselfpaired one must be accompanied by its distinct inverse, costing valency10.

Thus a simple undirected invariant graph of valency at most6 can have valency0,1,5, or6. It has valency6 only by selecting the unique matching and one selfpaired5-suborbit. These are exactly the ten choices above. A graph of maximum degree at most5 and diameter at most3 has order at most1+5+20+80=106, below132. Since the G action is transitive, degree is constant; every invariant132-vertex candidate with maximum degree<=6 and D<=3 must therefore be one of the ten6regular graphs.

This completeness applies to this fixed PSL2(11)/H action. It does not classify all132-vertex graphs, all vertex-transitive132-vertex graphs, or all degree6/D3 constructions. A coset graph here might also admit a different regular group action; the construction alone does not prove it is non-Cayley. The earlier quartic Cayley census concerns another degree and does not exclude these graphs.

## A route-complementarity observation

Let K be the adjacency operator of the five-neighbor orbital, and T the matching permutation. Paths of length at most3 in K+T can use two separated matching edges: TKT is a real additional route type, and must not be dropped by assuming at most one matching step. Its five-neighbor orbital is HtgtH. When this differs from HgH, the matching opens an entire conjugate orbital within three steps, a global complementarity mechanism rather than a repair of a selected bad pair.

If instead TKT=K, then T commutes with K and every path can move matching steps together and cancel pairs. Its radius3 ball is contained in R3_K(H) union T(R2_K(H)). The degree5 Moore counts bound these two sets by106 and26, whose sum is exactly132. A D3 success in that commuting case would require both bounds to be attained and the two sets disjoint. In particular any K-cycle of length at most6 forces a strict loss in its radius3 tree bound and rules that case out, since K is vertex-transitive. This is a conditional paper gate, not a new computation of which actual orbitals commute or have short cycles.

The full coverage obligation is still all132 cosets, not just the additional five-neighbor class. Numerical outcomes remain the producer's evidence. This paper performs no additional experiment or independent-method count.
