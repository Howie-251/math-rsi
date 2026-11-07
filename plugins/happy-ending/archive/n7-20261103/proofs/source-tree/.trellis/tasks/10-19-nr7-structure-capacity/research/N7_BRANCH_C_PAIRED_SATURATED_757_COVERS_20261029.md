# Branch C: paired saturated 757 covers and the superseded strict entrance

Date: 2026-10-29. Mathematical generation and cross-challenge only; **unreviewed/unaccepted**. No scientific execution, enumeration, solver, proof checking, or independent/external review. No historical file, configuration, acceptance, binding, task status, or running job was changed.

## 1. Scope and verified cover interface

Use the complete ordered rank-3 packet model, vertex-count paths, and weak7 with the same actual endpoints and opposite-color lengths summing to 9. In the inherited hypothetical X80, write S=Src_R6(X), T=End_R6(X), H=X\S, H'=X\T, P=S\T, Q=T\S, D=X\(S∪T). The current inherited result gives U_D=Src_R5(D), V_D=End_R5(D), |U_D|=|V_D|=q and U_D∩V_D=∅. Let J=P∩Src_B5(X), J_T=Q∩End_B5(X).

This branch originally targeted both strict budgets. Given m,m'∈{9,10}, j,t∈{15,16}, strictness forces m=m'=9 and j=t=15.

R25 §7 really proves the following actual covers, rather than merely a cardinality decomposition. Put F=End_R5(H)=Q⊔V_D and K'=Src_R5(H')=P⊔U_D. When j=15, V_-=X\Src_B5(X)=F⊔(S\J) has size40. Every s∈S\J has an actual R6 with remaining five vertices in F: F+s has26 vertices, no B5, so the756 bound forces R6, whose source cannot lie in F⊆H.

The canonical747 side A'=V_-\End_B4(V_-) contains S\J: an incoming B4 at such s joined to its pure-F R6 gives B5 or R7. Hence |A'| is15 or16. If16, A'=(S\J)∪{f}. If15, the other canonical side is exactly F; no s can augment F because of its pure-F R6. R5's canonical augmentation therefore supplies f∈F with (S\J)∪{f}747. In either case this gives a16/b25 cover with intersection exactly {f}. Reversing order proves the counterpart (T\J_T)∪{g} with g∈K'.

Each assertion quantifies its own legal choice. Nothing proves uniqueness of f or g, or simultaneous admissibility of two choices on the same side. At size40 any legal747/756 cover has overlap at most1 by16+25−40, but arbitrary covers need not have positive overlap. R5 supplies positive overlap for an appropriate canonical augmentation; it does not confer canonical endpoint localization on arbitrary changed covers.

## 2. The a16 source does not supply a unique extremal catalog

Primary source inspected: Jineon Baek, *On the Erdős–Tuza–Valtr conjecture*, [arXiv:2206.04260v2](https://arxiv.org/pdf/2206.04260), §§2–5, especially Theorems2.7,3.6,5.10 and Lemmas5.1–5.7. Its model permits arbitrary complete triple colorings; thus its upper bound applies here. Theorem2.7 at n7 excludes size17 with no B4, R7, or same-endpoint B3/R6. Its proof uses slope labels, injective triangular-grid statistics, and interweaved laced red paths. It is not a classification of all16-point configurations. The grid for noB4/noR7 has21 cells, so16 does not mean a full grid. The published induction proving the forbidden configuration starts at17. No transfer of labels between the two actual covers follows.

One elementary useful interface is independent of any extremal classification: each actual747 side of size16 contains an internal R6, because the classical noB4/noR6 capacity is15. This does not locate its endpoints identically across the two covers or produce a common second overlap. The first obstruction to the original paired-cover attempt was precisely the absence of such a forced common actual support.

## 3. Stronger junction-deletion argument eliminates the entrance

During cross-challenge, generation branch B supplied a stronger candidate. The following records the complete check, not an independent review or an independent discovery claim.

Set W=S∪U_D and define internally

G=End_R5(W)∩Src_B4(W).

The previous neutral-through theorem supplies two facts with ambient quantifiers: S∪U_D has no ambient B5 terminal; every ambient B4 ending in S∪U_D extends to an ambient B5 preserving its source. Hence W has no B5, and every internal B4 source in W is an ambient B5 source. The R25 mixed-role exclusion S∩End_R5(X)∩Src_B5(X)=∅ therefore gives G⊆U_D.

Now delete the entire actual junction set: W0=W\G. Any R5 terminating and B4 starting at one point in W0 also constitute such paths in W, so their meeting point would belong to G and could not remain in W0. Consequently W0 has no internal red5-terminal/blue4-source junction. It also inherits no B5, no R7, and no weak7. This exactly matches the old residual D7 hypothesis. The residual theorem is not restricted to the canonical residual obtained from a global pair ordering; its proof only needs these induced path properties.

For completeness, that proof is independent of the desired budget equality. Let E=End_R6(W0). If e∈E started a B3, joining it to an incoming R6 gives either R7 or a B4 starting at the red5 predecessor, violating the junction condition. Thus every e is a right red root in W0. E is a red clique, so |E|≤6. When |E|≤5 delete E. When E={e1<…<e6}, every R6 ending e2 starts e1: a later source can be preceded by e1; an earlier source a makes the triple a,e1,e2 either blue, giving a same-endpoint B3/R6 weak7, or red, extending the red clique to R7. Thus E\{e2} hits every R6. In either case deleting at most5 points leaves an actual756, giving |W0|≤25+5=30.

Since |W|=30+q and |G|≤|U_D|=q,

30+q−|G|=|W0|≤30

forces G=U_D. This is the stronger actual internal statement: every u∈U_D simultaneously terminates an R5 and starts a B4 **inside S∪U_D**. It is not a conclusion about a chosen witness list. The proof includes every alternative path and is unaffected by witness sharing.

In particular U_D⊆End_R5(X)∩D=F'. In H', K'=P⊔U_D and K'⊔E'=L'⊔F'=H'. Also P∩L'=J. Therefore

K'\F'=J, and j=25−m'.

For the last equality of sets: U_D⊆F' removes its portion; on P, the partition L'⊔F' leaves exactly P∩L'=J. The order-reversed proof gives t=25−m. It uses W^rev=T∪V_D, internal junction Src_R5(W^rev)∩End_B4(W^rev), and forces that junction to equal V_D.

Thus BOTH budgets are equalities, and the initially assigned both-strict entrance is impossible. This conclusion does not need a16 classification, paired-cover uniqueness, or a second-overlap argument. It also does not use w0: W is the disjoint union of S and U_D regardless of U_D∩V_D, so it can be established before the previously derived w0 result.

## 4. Accurate outcome and remaining breakpoint

The paired saturated40 covers are valid interfaces, but they are no longer needed to exclude both-strictness. Under the inherited m,m'9/10 and j,t15/16 ranges, the possible pairs are now (m',j)=(9,16) or(10,15), and (m,t)=(9,16) or(10,15). Thus j=t15, if it remains, has m=m'10 rather than9.

The new internal supply does not by itself show that distinct u have distinct suppliers, that an R5 inside S∪U_D ends in D internally before its final vertex, or that the opposite-side paths can be joined at the same external endpoints. Those are unproved further steps. No X80 exclusion or new global numerical bound follows here;40/50/80/81 remains unchanged.

Dependencies: R5 §§2–8; R7 §§2–3.3; R20 root/terminal closure; R25 §§3–7; N7_NEUTRAL_THROUGH_RESIDUAL_AUGMENTATION_AND_MUS_SUPPORT_20261029 §§2–6. The stronger junction argument was received from branch B and checked here against the actual residual proof; this cross-challenge is generation work only.

## 5. Second pass: full-support Hall and five actual residual endpoints

The main session strengthened §3 by applying the same argument to each S∪{u}, of size31. It forces the junction u already in that singleton extension. Therefore every u∈U_D has pure incoming R5(S^4,u) and pure outgoing B4(u,S^3). This is actual induced supply, not a selected representation. The root, branch A, and this branch then obtained the following common extension during cross-challenge; it is one shared result, not several independent improvements.

Let E=End_R6(S), and retain W=S∪U_D. First E remains a right red root set in the enlarged W. Indeed, if B3(e,x,y) lies in W for e∈E, take an incoming R6 inside S with last predecessor r. The joining triple r,e,x is red only if there is R7. If blue, it yields B4(r,e,x,y), ending in W; the inherited ambient extension makes r an ambient B5 source. Yet r∈S∩End_R5(X), contradicting the mixed-role exclusion. Thus no such B3 exists. In this argument r<e<x<y, so all new vertices are distinct and the relevant path is genuinely ordered.

Define the full support graph between U_D and I\E as follows: u—i is an edge when an actual internal B4(u,i,x,y) exists in W. This graph keeps every path, including those with later vertices in U_D. Every second vertex i really lies in I\E. To see i∈I, extend B4 to an ambient B5 while preserving its first two vertices. Join it with the pure incoming R5(S^4,u). A blue join gives B6; a red join gives R6 ending at i. Thus i∈T, and since i∈W, i∈I. The lifted right-root fact rules out i∈E.

For A⊆U_D let N(A) be its entire neighbor set in this global support graph. Consider the actual induced set

W_A=(S∪A)\N(A).

It has no B5. Suppose an internal R5-terminal/B4-source junction z survives. If z∈S, extending its B4 to an ambient B5 contradicts the mixed-role exclusion. If z∈A, the second vertex of its B4 belongs to N(A), hence was removed. No junction remains, so the exact residual D7 bound applies. Because N(A)⊆I\E⊆S is disjoint from A,

30+|A|−|N(A)|=|W_A|≤30.

Consequently |N(A)|≥|A| for every A⊆U_D. Hall supplies a matching saturating all q vertices of U_D, with each matched pair u<i witnessed by an actual B4. No internally disjoint paths, exclusive suppliers, or pure-only support graph is claimed.

Now E⊆I, |I|=5+q, so the full-set Hall inequality gives

q≤|I\E|=5+q−|E|,

and |E|≤5. Conversely deleting all E from S kills every internal R6 and leaves a756, so 30−|E|≤25 and |E|≥5. Hence

**|End_R6(S)|=5, and the full support graph gives a perfect matching U_D→I\E.**

In particular the six-endpoint alternative in the old residual five-transversal proof is impossible for S in this common X80. Every actual R6 in S ends in those exact five points; no arbitrary canonical choice is needed. Matching also implies the usual order-cut dominance, since every matched u precedes its partner in I\E.

Reversing order gives exactly five actual sources E^rev=Src_R6(T), and a perfect matching from I\E^rev to V_D with increasing ordered edges, witnessed by the corresponding internal B4 paths in T∪V_D.

All of this remains unreviewed/unaccepted generation. It is a common-realization restriction, not an exclusion of X80. The note's original §4 breakpoint is refined: there is now a full-path matching into the precise q-point residual endpoint complement, but the matching does not transport all red and blue supplies into one common forbidden same-endpoint pair.

## 6. Third pass: every legal40-cover choice lies before the penultimate right root

The paired40 covers remain open in the budget-equality branch m=m'=10, j=t=15. Eliminating the original strict branch did not eliminate these covers. Fix this branch and write E={e1<e2<e3<e4<e5}=End_R6(S), and F0={f1<f2<f3<f4<f5}=Src_R6(T). F0 is distinct notation from the25-point core F=End_R5(H).

For **every** point f∈F such that A_f=(S\J)∪{f} is747, each e∈E is a right red root inside A_f. Take an incoming R6 inside S ending e with last predecessor r. Its first five vertices form R5 ending r, so r∈S∩End_R5(X), hence r∉J and r∈A_f. If B3(e,x,y) existed inside A_f, joining r,e,x red would yield ambient R7; joining blue would yield B4(r,e,x,y) inside A_f. Both are impossible. This proof uses all legal choices separately and does not assert a unique f.

The actual extended root chain R6(a,e1,e2,e3,e4,e5), a<e1, is available from the old R21 §2.4 mechanism. Here is its proof in the present five-root case. Since E is a size5 minimum transversal of R6 in S, there is an e2-private R6 in S avoiding E\{e2}; let its source be a. If a>e1, the right red root e1 could be prepended, giving R7, and a≠e1 by privacy. Thus a<e1. The triple a,e1,e2 cannot be blue because it would be a B3 sharing the endpoints of that private R6. It is red, and the rest of the displayed chain follows from E's root property.

Now if e4<f<e5, insert f into that actual chain. The new triples are e3,e4,f and e4,f,e5; both start at roots in E and belong to A_f, hence are red. This gives ambient R7. If f>e5, append f; the one new triple e4,e5,f is red, again giving R7. The point f lies in F⊆H and cannot coincide with any e_i∈S. Consequently

**Every legal cover point f satisfies f<e4.**

By reversing order, every legal g∈K' with (T\J_T)∪{g}747 satisfies **g>f2**. These are restrictions on every admissible augmentation, not assertions that every vertex in the indicated intervals is admissible. They also do not imply a second overlap or contradict existence of the actual saturated covers.

### Repaired failed strengthening and the exact first missing triple

The proposed stronger cutoff f<e2 was rejected during cross-challenge. Inserting f with e2<f<e3 into the displayed R6 introduces **three** new triples, including (f,e3,e4), whose first vertex is not an E root. Root lifting certifies (e1,e2,f) and (e2,f,e3), but not this third triple. The packet on e2<f<e3<e4 has its first three entries red and permits RRRB; it does not force (f,e3,e4) red. Similarly e3<f<e4 leaves (f,e4,e5) uncertified. This is a local permitted packet and a proof breakpoint, not a complete-model counterexample.

The a16 interface adds that each A_f contains some internal R6, but does not force that path to use f or to certify the missing triple. Paths avoiding f end in E; paths using f may acquire different internal endpoint roles. If f∈V_D, it cannot be the endpoint of an ambient R6, but may be an interior vertex of one. If f∈Q, it may be the endpoint. No selected witness can stand for all of these possibilities.

Finally, for every cut c, E_{≤c}∪(F0)_{>c} is an actual red clique: each mixed triple starts at an E right root, and triples entirely in F0 are red. Therefore |E_{≤c}|+|(F0)_{>c}|≤6. This is the old root-cut type of ordering restriction, not a new population saving or a contradiction by itself.

This completes the substantive third-pass attempt. The genuine new cover interface is universal root lifting and the f<e4 / g>f2 localization. The first unresolved step is the missing interior insertion triple, together with the lack of a16 classification forcing its color or alternative common forbidden endpoints. All critical full paths remain retained; no global bound is changed. This branch note is now frozen for parent integration.
