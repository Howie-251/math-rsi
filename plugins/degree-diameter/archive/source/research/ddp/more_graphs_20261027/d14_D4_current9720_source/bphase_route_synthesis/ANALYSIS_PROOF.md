# Coarse phase formula, parity lifts and unit-a normalization

This note checks the new fixed-m9 synthesis model only. The SL2(3) matrix parts Xa=(0,1;2,2), Xb=(0,1;2,1), the four line charts and gamma(x)=-x+c remain fixed. The numerical producer tests a-phase1, b-phase B in0..8, and two distinct projected central inverse pairs chosen from classes1..4. No fiber graph or BFS was produced for this analysis.

## A proposed stronger capacity was tested and refuted

ANALYSIS_PREDICTION.json froze the possibility of a distance4 element in the SL2 projection with fewer than9 wide words. Exact enumeration of341 wide words of lengths0..4 instead gives SL2 distance histogram1,4,10,9: its diameter is3, with no distance4 element. Thus that particular capacity obstruction is inapplicable. ANALYSIS_SL2_CAPACITY.json records this negative test, using0.003784042 CPU seconds. No absence theorem is claimed from it.

## Exact minus-identity phase constraint

The cached complete wide-word list shows no -I endpoint with fewer than3 wide letters. At length3 the only words are bbb and BBB, with phases +/-3B. At length4 the words are abab,baba,ABAB,BABA, with phases +/-2(1+B). Central plain steps do not change the SL2 component. Therefore with two projected central inverse pairs S={+/-r,+/-s}, the complete phases at -I within4 total steps are

    T(B,S)={+/-3B,+/-2(1+B)} union ({+/-3B}+S) modulo9.

This includes all word orders and all immediate inverse-letter occurrences. It is a controller statement; it does not assume that affine fiber maps commute.

The small necessary-phase check agrees with the prediction frozen before seeing the new producer results. Exactly six of the54 frames have T(B,S)=all of C9:

    B1: {3,4}; B4: {1,3}; B7: {2,3};
    B8: {1,2}, {1,4}, {2,4}.

For B divisible by3, +/-3B collapses to0 and capacity is insufficient. For the other B values, phase0 must come from class3 unless B8 makes the four-wide phase0; this gives the listed cases. These six pass only the -I necessary test, not the full controller test. The producer's complete coarse checks reject all54 frames at some controller target. No parity lift can repair an absent controller route.

Replacing a projected pair by the within-cell matching P9 and retaining only one projected pair cannot help: at -I the phases are among +/-3B, +/-3B+/-r, and +/-2(1+B), at most8 distinct phases. That paper rejection is not counted as one of the54 numerical frames.

## Exactly four fiber parity lifts

The global plain operator is P(g,x)=(gp,gamma x), of order18 on this m9 graph, not order9. Gamma is an affine involution, so P^e has fiber gamma for odd e and identity for even e. For any projected inverse class k in1..4, the global inverse-power pairs represented by k and9-k have the same projected controller pair and opposite fiber parity. They are the two possibilities in this rule. Two distinct projected classes therefore have exactly four independent parity lifts; inverse darts use P^-e with the same parity as e. Nothing requires gamma^9=identity.

## Coverage of the unit-a subfamily

Let a's central phase A be any unit modulo9. Put u=A^-1 modulo9 and let U be its unique odd lift modulo18. Then U is a unit modulo18. The controller automorphism

    (X,i) maps to (X,u*i)

sends a=(Xa,A) to (Xa,1), b=(Xb,B) to (Xb,uB), and central p^e to p^(u*e). On the lifted graph leave the fiber coordinate unchanged. A plain edge with global power e is sent to the edge with global power Ue: its projected phase agrees modulo9, and its affine fiber map agrees because U is odd and gamma^(Ue)=gamma^e. The wide charts are unchanged by this relabeling.

Multiplication by U permutes all eight nonidentity, noninvolution global inverse-power pairs represented by1..8; it preserves distinct projected classes and the available parity lifts. Thus the a1 numerical family covers every unit-A member of this same fixed rule by isomorphism. This is an exact equivalence, not additional numerical tests. A0,A3,A6 are nonunits and are outside this argument, as are other moduli, changed SL2 projections, different shortcuts or arbitrary degree16/D4 graphs.

The necessary-phase/parity arithmetic check used0.000330854 CPU seconds. Actual producer scope remains54 coarse frames, zero fiber graphs and zero BFS; logical unit-A extension does not inflate those counts. The fixed unit-A family is stopped after the producer's complete coarse rejection.
