# Complete residual-phase reduction for the fixed M9 operator family

Keep G=SL2(3) x C9, the source SL2 matrices Xa,Xb and its four wide charts. Let a=(Xa,A), b=(Xb,B), A,B arbitrary modulo9. The plain operator is P(g,x)=(gp,gamma x), p=(I,1), gamma(x)=-x+c, c=(2,0,2,2). It has global order18. This proof concerns only these projections/charts and inverse-closed choices of powers of this plain operator. It does not concern another modulus, altered SL2 steps, noncentral shortcuts or arbitrary degree16/D4 graphs.

The complete341-word SL2 projection calculation establishes that -I cannot be reached by fewer than3 wide letters. Exactly bbb,BBB reach it at length3, with phases +/-3B. At length4 the words abab,baba,ABAB,BABA have phases +/-2(A+B), and there are no others. Any route of total length at most4 to -I has either3 wide steps and at most1 plain step, or4 wide steps and none. All claims below therefore concern complete projected route sets, not merely full-rank fiber certificates.

## Nonunit b phases are impossible

If B is0,3 or6, then3B=0 modulo9. For two distinct projected plain inverse pairs S={+/-r,+/-s}, all -I phases lie in

    {0,+/-r,+/-s} union {+/-2(A+B)}.

This has at most7 phases, fewer than9, for every A. Some whole controller fiber is therefore unreachable in4 steps, independently of the plain fiber parity or wide-route rank.

## Unit phases reduce without losing fiber maps

For any unit u modulo9, let U be its unique odd lift modulo18. The controller automorphism (X,i)->(X,u*i), with fiber coordinate unchanged, maps a-phase A to uA and b-phase B to uB. A plain edge P^e maps to P^(Ue): controller exponents agree modulo9 and gamma^(Ue)=gamma^e because U is odd. This preserves the full affine map, including its translation, rather than only the linear sign. Multiplication by U permutes all global inverse-power pairs represented by1..8, preserves projected distinctness and their two parity choices, and fixes P9.

If A is a unit, choose u=A^-1. These instances are isomorphic to the already tested a1 family, B0..8 and all six distinct projected-pair patterns. Every such coarse controller failed in that producer's54 tests. No new tests are asserted for this logical extension.

If A is not a unit but B is, choose u=B^-1. Then b-phase becomes1 and a-phase remains in{0,3,6}. Exactly3*6=18 coarse frames remain. The residual producer tested these18 once, and all18 failed its complete projected radius4 gate. Thus no parity-lift or fiber graph was generated. The unit maps cover these cases by isomorphism; they do not turn18 actual tests into a claimed exhaustive numerical run over all phase pairs.

The logical phase cases are complete: Bnonunit; Bunit/Aunit; Bunit/Anonunit. The result therefore covers all81 possible (A,B) phase pairs through paper reductions and the two actual batches54 and18. The raw actual counts remain54+18 coarse frames, zero new fiber graphs and zero BFS.

## Repeated projected pairs and the plain matching

Two global inverse-power pairs can have the same projected C9 pair and opposite fiber parities. Then their projected plain steps are only{+/-r}. The same phase argument gives at most2 phases from +/-3B, at most4 after adding +/-r, and at most2 four-wide phases: total at most8, for every A,B. They cannot supply all9 -I targets.

One global inverse-power pair together with P9 has projected steps{0,+/-r}. The zero step only repeats the no-plain phase, so the same at-most8 bound applies. These paper-excluded cases are not part of either numerical54 or18 batch. Families with still fewer plain edges are subcases and are likewise impossible.

For completeness under maxdegree16, the four source wide relations contribute12 neighbors in nonidentity-SL2 controller cells. At a fiber point not fixed by gamma, distinct global powers of P give distinct neighbors: equal projected powers differ by9 and have opposite gamma parity. Each inverse-power pair therefore contributes2 plain neighbors and P9 contributes1. Three pairs, or two pairs plus P9, exceed degree16 at such points. Since gamma has only one fixed point out of81, these are not maxdegree16 graphs. Hence all permitted inverse-closed power selections are exhausted by the two distinct projected-pair class, repeated-pair class, and one-pair-plus-matching class above.

This completes the fixed M9 operator/phase family exclusion. The actual negative coarse checks are inherited from ../bphase_route_synthesis/RESULT.json and this directory's producer RESULT.json. No additional controller search, graph construction, BFS, phase grid or field change was run for this proof.
