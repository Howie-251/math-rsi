# A genuine MUS support exclusion from a unique private red path

Date: 2026-10-29, subsequent authorized theoretical continuation. **Unreviewed / unaccepted.** This note proves a restricted actual MUS support exclusion. It does not prove a general MUS descent, a smaller deletion transversal, or a new global numerical bound. No scientific computation, enumeration, solver, external review, or export request was used. Only this fresh note is owned by this contribution; historical files, configuration, evidence, acceptance, and task pointers are preserved.

## 1. One chosen target and complete-constraint setting

The target is to exclude a specified support pattern in a genuine inclusion-minimal unsatisfiable path family, rather than repeat the earlier repair accounting.

Let X be an actual ordered rank-3 signotope with no blue six-path, red seven-path, or weak seven. Four-point packets, in abc, abd, acd, bcd order, change color at most once. Paths count vertices. Opposite-color paths of total length nine with the same actual endpoints give weak seven.

Let F be an inclusion-minimal unsatisfiable family of complete requirements: each actual red six-path in F must meet both roles K and Y, and each actual blue five-path in F must meet K. A red path's two conditions remain bundled. Write F_R for the red members. All transversals below hit **every** member of F_R, not merely selected witnesses.

## 2. Unsatisfiability forces every five-point red transversal to be a blue member

**Lemma 1.** F_R has no transversal of size at most four. Every five-point transversal S of F_R is itself an actual blue five-path belonging to F.

Proof. Assign Y=S and K=X minus S. Every red member meets Y by the transversal property and meets K because it has six vertices whereas |S|<=5. Thus all complete red requirements are satisfied. A blue member fails exactly when all five of its vertices lie in S. If |S|<=4 this is impossible, contradicting unsatisfiability. If |S|=5, failure is possible only for the member whose vertex set is exactly S. Unsatisfiability forces that member to exist. This proves both claims.

In particular every five-point red transversal is inclusion-minimal. For every s in S there is at least one private red path A with A intersect S={s}. The lemma is a general complete-constraint observation. The new actual support restriction will require packet closure, weak seven, and both monochromatic caps in Section 4.

For a pure-red F, the same assignment works for every |S|<=5, since no blue requirement remains to fail. Therefore its red transversal number is at least six. This does not exclude pure-red MUS families.

## 3. Unique private support forces a full family of six actual blue extensions

Fix S={s1<...<s5}, a red transversal of size five. Fix s in S and put D=S minus {s}. Let A be a private red member at s, so |A|=6 and A intersect S={s}.

**Lemma 2.** The following conditions are equivalent:

1. A is the unique complete red member of F meeting S only at s.
2. For every x in A minus {s}, the five-point set D union {x} hits every red member of F.

Proof of 1 implies 2. A is hit by x. Every other red member has a point in D, since otherwise it would be another private member at s. Hence each replacement hits the entire red family.

Proof of 2 implies 1. Any private red member B at s avoids D. Therefore all five x in A minus {s} must lie in B. Since B also contains s and has exactly six vertices, B=A.

Assume these equivalent conditions. Lemma 1 now gives six distinct actual blue members

\[
Q_x=D\cup\{x\}\in F\qquad(x\in A).
\tag{1}
\]

The x=s case is S itself; the other five are the replacements. All points of D are outside A. D is an actual blue four-path by heredity. This is a forced complete family of blue requirements, not the selection of a convenient pair of paths.

**Lemma 3 (critical traces).** For each x in A and every assignment sigma_x satisfying F minus {Q_x},

\[
D\cup\{x\}\subseteq Y_x,
\qquad A\setminus\{x\}\subseteq K_x.
\tag{2}
\]

Proof. Path-level inclusion-minimality provides such an assignment. It must violate Q_x, since satisfying Q_x would satisfy all F. Thus D and x are Y. Every other Q_y, y in A minus {x}, remains a requirement and is satisfied. As all D is Y, its only possible K-point is y, forcing y into K. In particular the complete red requirement A is satisfied, with x its unique Y-point.

The six assignments in (2) are separate. Nothing identifies their roles on X minus (D union A), and no proof below combines their outside assignments. The actual paths in (1) coexist in the same fixed X regardless of which critical assignment is considered.

## 4. Packet and weak constraints exclude three support arrangements

Write A=(a1<...<a6), with endpoints a=a1 and b=a6.

**Theorem.** Under the hypotheses of Section 3,

\[
|D\cap(a,b)|\le1,
\tag{3}
\]

and D cannot lie entirely to the left of a or entirely to the right of b.

Proof of (3). Suppose d<e are two points of D between a and b. The actual blue member Q_a gives chi(a,d,e)=B, and Q_b gives chi(d,e,b)=B. These are the first and last entries of the packet on a,d,e,b, so all four entries are blue. In particular (a,d,b) is a blue three-path with the same endpoints as the red six-path A. Their lengths sum to nine, contradicting no weak seven. This uses the actual endpoint extensions forced by all-constraint unsatisfiability.

Proof of the right-side exclusion. Suppose b<d1<d2<d3<d4 are all points of D. If chi(a5,b,d1)=R, appending d1 to A gives a red seven-path. Hence chi(a5,b,d1)=B. The actual blue Q_b gives chi(b,d1,d2)=B, and the remaining consecutive triples of D are blue. Consequently

\[
(a_5,b,d_1,d_2,d_3,d_4)
\]

is an actual blue six-path, a contradiction. Every consecutive triple has been supplied; this is an append operation, not an insertion with an omitted second gate.

For the left-side exclusion, write d1<d2<d3<d4<a. No red seven forces chi(d4,a,a2)=B. The blue Q_a supplies chi(d3,d4,a)=B, and the two preceding triples belong to D. Thus (d1,d2,d3,d4,a,a2) is blue six, again a contradiction.

The theorem excludes these signatures in a **genuine complete-path MUS**: a five-point red transversal with a unique private member whose endpoint interval contains two other transversal points, or places all four other transversal points on one side. The intermediate geometric argument uses actual paths; the reason all its blue extensions must coexist is Lemmas 1-2, and the exact critical role traces use MUS minimality in Lemma 3.

## 5. Explicit extreme-vertex localization

If s=s1, every point of D is later than s1, while a<=s1. Thus D has no point left of a. The right-side exclusion forces at least one D-point inside (a,b), and (3) permits at most one. Since A avoids D, its endpoint b cannot equal any s_i. Therefore

\[
\boxed{s_2<\max A<s_3}
\qquad\text{when }s=s_1\text{ has a unique private red member.}
\tag{4}
\]

By the same reasoning in reverse order,

\[
\boxed{s_3<\min A<s_4}
\qquad\text{when }s=s_5\text{ has a unique private red member.}
\tag{5}
\]

Thus an extreme transversal point with a private red path violating (4) or (5) cannot have that path as its only private member. This conclusion concerns the entire red family of F; choosing a single private witness does not satisfy the uniqueness premise.

## 6. Exact coverage and the remaining gap

The completed target is the support exclusion in Sections 4-5. It is not a support theorem for every MUS: there is no proof that every F has a red transversal of size five, or that a five-point transversal has a vertex with a unique private red member. If all relevant vertices have several private paths, the full replacement family (1) is not justified.

Even with uniqueness, the surviving configurations include D straddling the red endpoints with at most one internal point, and the one-interior-point arrangement forced at an extreme s. No contradiction for these remaining arrangements is proved. In particular one cannot conclude that every blue four-path extension family is red-six-free.

Pure-red families have red transversal number at least six by Lemma 1's assignment argument and remain unresolved. There is no decreasing potential, no new global support transversal, and no z<=4 conclusion. The old z<=5 baseline and the global 40/50/80/81 chain remain unchanged. No actual MUS or critical X was constructed.

Generation cross-challenge by the strict-branch collaborator and then by the root checked the complete-transversal equivalence, the six separate critical traces, the packet contradiction, and both cap-six arguments. This is collaboration in the generation task, not independent mathematical review or acceptance.

The preceding [simultaneous-repair note](N7_BRANCH_C_MUS_DESCENT_AND_SIMULTANEOUS_REPAIR_20261029.md), [critical-blocker note](N7_BRANCH_C_CRITICAL_BLOCKER_PROPAGATION_20261029.md), and [latest common-saturation synthesis](N7_H50_R30_COMMON_SATURATION_AND_FULL_SUPPORT_BARRIERS_20261029.md) provide the prior stopping points. Their rollback and full-violation formulas are not claimed as new results here. The present proof selects the distinct unique-private-support target and proves exactly its stated exclusion.
