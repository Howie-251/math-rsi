# Canonical labels for a bounded hard-D1 diagnostic

## Claim and status

**PROVABLE AS STATED.** Every actual hard-D1 graph can be relabeled to one of the three label representatives below, preserving the archived D1_MATCH parent template. The representative with $b=W_5$ is impossible by a further short argument, so only $b=W_4$ and $b=W_6$ need remain in a diagnostic.

This is a relabeling coverage theorem and a necessary-constraint specification. It is not a solver result or an exclusion of the remaining two representatives. No solver is run here. Historical D1 RAW results are not proof certificates.

## Assumptions and dependencies

Use the actual graph identities and the hard-D1 structure proved in `D1_MATCH_HARD_BRANCH_REDUCTION.md`, with its C4 refinement in `D1_MATCH_C4_TRANSPORT_REFINEMENT.md`. In particular,

$$r\in C_2,\quad p\in C_3,\quad q\in C_4,\quad c\in C_5\cup\cdots\cup C_8,$$

$$r\ne u_2,\quad p\ne u_3,\quad q\ne W_4,\quad U\cap W=\varnothing.$$

Here $W_i$ is the unique ordinary neighbor of $w$ in $C_i$ for $i=4,\ldots,8$, while $U=\{u_2,u_3,U_5,U_6,U_7,U_8\}$ is the ordinary neighborhood of $a$. The vertex $c$ is one of $U_5,\ldots,U_8$; $b$ is one of $W_4,\ldots,W_8$. The two vertices $b,c$ are distinct neighbors of $r$.

The literal source of vertex IDs is

`context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/theory/n62/n62_root_templates.json`,

entry `D1_MATCH`. It has $0$ as root, $w=9$, $a=10$, $P(w)=\{1,2,3\}$, $P(a)=\{1,4\}$, and the following ordinary classes:

| Class | Archived vertex IDs | Canonical distinguished vertices |
|---|---|---|
| $C_1$ | $11,\ldots,15$ | none fixed |
| $C_2$ | $16,\ldots,21$ | $r=16$, $u_2=17$ |
| $C_3$ | $22,\ldots,27$ | $p=22$, $u_3=23$ |
| $C_4$ | $28,\ldots,33$ | $W_4=28$, $q=29$ |
| $C_5$ | $34,\ldots,40$ | $W_5=34$, $c=U_5=35$ |
| $C_6$ | $41,\ldots,47$ | $W_6=41$, $U_6=42$ |
| $C_7$ | $48,\ldots,54$ | $W_7=48$, $U_7=49$ |
| $C_8$ | $55,\ldots,61$ | $W_8=55$, $U_8=56$ |

## 1. Complete relabeling proof

The original D1 parent pattern permits the interchange of labels 2 and 3. Use it to put the light mate $r$ of $w$ in $C_2$, as in the hard-branch reduction. This step fixes the resulting roles of labels 2 and 3.

The same parent pattern permits arbitrary permutations of labels $5,6,7,8$ and their entire ordinary classes. Send the parent of $c$ to label 5. This fixes $c$'s class but leaves all permutations of labels $6,7,8$ available.

Under this remaining label permutation group, the class of $b\in W$ has exactly three orbit representatives: 4, 5, and 6. In the last case, send whichever of 6,7,8 is its parent to 6. Thus the three representative labels are

$$b=W_4=28,\qquad b=W_5=34,\qquad b=W_6=41.$$

Finally apply independent permutations inside each ordinary class to place the distinguished points at the table's IDs. Every class contains either no distinguished point or two proved-distinct distinguished points. A permutation sending each ordered pair to its specified ordered pair therefore exists. These within-class permutations preserve every parent edge and nonedge. The remaining points can be mapped bijectively to the unused IDs in any order.

All facts above are transported under one graph isomorphism; none demands that an already labeled graph have a particular unproved automorphism. The ordering of the normalization steps avoids fixing $c$'s class or $b$'s class after the ordinary vertices have already been assigned IDs.

No choices have been imposed on $s,t$, the other unit endpoints of $r$, on $f,g$ in row 4, on matching permutations, or on the endpoints of the internal repeat edges. For example, $s=p$ remains allowed by the normalization.

## 2. The middle representative is already contradictory

The stable hard-branch proof gives $B_{ir}=0$ for every root-neighbor label $i\in X$. Since $r\in C_2$, its only original neighbor in $X$ is 2. It is adjacent to neither $w$ nor $a$.

In particular, for label 5 the nonadjacent pair $5,r$ has $B_{5r}=0$ and hence exactly one common neighbor. As $N(5)=\{0\}\cup C_5$ and $r\not\sim0$, this says

$$|N(r)\cap C_5|=1.$$

But $r$ is adjacent to both $b$ and $c$, which are distinct. Consequently they cannot both lie in $C_5$. After the normalization $c\in C_5$, this excludes $b=W_5$.

More generally, the same argument gives exactly one neighbor of $r$ in each $C_i$ with $i\ne2$: the exceptional vertices $w,a$ in the neighborhoods of labels 1,3,4 contribute none. Vertex $r$ has no neighbor inside $C_2$, since 2 is triangle-free. Thus $r$ has its parent 2 plus one neighbor in each of the other seven ordinary classes.

This is a direct graph argument, not a diagnostic non-hit. One may retain the $b=34$ specification as an explicitly known contradictory input check, but it is not a surviving mathematical branch.

## 3. Complete original adjacency rows

The word "complete" means that every unlisted off-diagonal entry in that row is zero. Symmetry also applies.

The base template fixes all rows of $0,1,\ldots,8$:

$$N(0)=\{1,\ldots,8\},$$
$$N(1)=\{0,9,10,11,12,13,14,15\},$$
$$N(2)=\{0,9,16,17,18,19,20,21\},$$
$$N(3)=\{0,9,22,23,24,25,26,27\},$$
$$N(4)=\{0,10,28,29,30,31,32,33\},$$
$$N(i)=\{0\}\cup C_i\quad(i=5,6,7,8).$$

The distinguished ordinary neighbors give two additional complete rows:

$$N(9)=\{1,2,3,28,34,41,48,55\},$$
$$N(10)=\{1,4,17,23,35,42,49,56\}.$$

Additional forced entries are

$$A_{16,b}=A_{16,35}=1,\qquad A_{b,35}=A_{16,10}=0.$$

The negative entry $A_{b,35}=0$ follows because both endpoints are neighbors of triangle-free $r=16$. Also

$$N(16)\cap U=\{35\},\qquad N(16)\cap W=\{b\}.$$

No complete adjacency row for 16 or 35 is specified.

## 4. Complete repeat rows

Every omitted entry in a listed complete row is zero:

$$B_0=2e_9+e_{10},\qquad B_9=2e_0+e_{16},$$
$$B_{10}=e_0+e_{22}+e_{29},$$
$$B_1=e_2+e_3+e_4,\qquad B_2=e_1+e_3+e_b,\qquad B_3=e_1+e_2+e_{35}.$$

These are constraints on the actual matrix $B=A^2+A-7I-J$; they do not introduce an independently realizable repeat matrix.

## 5. Partial rows and safe domains

The complete shape of row 4 is

$$B_4=e_1+e_f+e_g,$$

where

$$f\in\{17,42,49,56\},\qquad g\in\{34,41,48,55\}.$$

The C4 refinement gives $f=u_2$ if and only if $b=W_4$. Thus $f=17$ in the surviving $b=28$ representative, while $f\in\{42,49,56\}$ in the surviving $b=41$ representative. Its remaining endpoint $g$ is not assigned an ID.

The complete shape of row 16 is

$$B_{16}=e_9+e_s+e_t,$$

$$s\in C_3=\{22,\ldots,27\},\qquad t\in C_4\cup\cdots\cup C_8=\{28,\ldots,61\}.$$

These disjoint domains and the unit entry at 9 exhaust the row. This records $B_{X,16}=0$, but leaves all choices within the two domains unresolved. The $(4,r)$ entry of commutation gives $B_{C_4,r}=A_{fr}+A_{gr}$. Here $f\ne c$ and $N(r)\cap U=\{c\}$ force $A_{fr}=0$, while $N(r)\cap W=\{b\}$ gives $A_{gr}=[g=b]=B_{4b}$. In the $b=28$ representative, $B_{4b}=0$ because $b=W_4$ is an original neighbor of triangle-free label 4, so $t\notin C_4$. This refinement is optional and is not needed for relabeling coverage. No constraint fixes $s$ to 22 or 23, or $t$ to 29.

## 6. Machine-readable companion and boundary

The companion `d1_match_canonical_diagnostic_constraints_20261011.json` contains the class table, complete original rows, complete repeat rows, partial-row domains, and the three representative labels. The $b=34$ entry is marked `EXCLUDED_BY_PARENT_CLASS_ARGUMENT`; the other two are marked `NECESSARY_CONSTRAINTS_ONLY`.

Its complete-row fields mean that omitted entries are zero, while partial-row fields carry only their explicitly stated sums and support. No additional historical symmetry breaker may be combined automatically with these labels: any such combination needs its own common relabeling argument. In particular, the original and repeat matchings have not been identified or assigned matching permutations.

The specification supplies necessary conditions for an actual graph. A model of only these conditions would not by itself establish an order-62 graph, and a search non-hit would not by itself supply a proof of nonexistence.
