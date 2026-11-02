# Specified finite-field representations

The exported tables validate the four prescribed degree-6/D7 representations over F7, F8, and F9, together with the single initial F11/D8 control representation. This is a finite specified set, not a classification of representations.

Let H have normal form beta^u alpha^v, with multiplication (u,v)(U,V)=(u+(-1)^v U,v+V) modulo (3,16). Its action is rho(u,v)=B^u A^v. For every exported representation, B^3=I, A^16=I, and ABA^-1=B^-1. The independent C17 action is chi(alpha)=5, chi(beta)=1. Consequently

    (V,c,h)(W,d,k)=(V+rho(h)W,c+chi(h)d,hk)

and the inverse is (-rho(h^-1)V,-chi(h)^-1 c,h^-1). These formulas use the actual recovered source H/C17 components, not a proposed replacement quotient.

The three positive quotient components are A:(c,u,v)=(0,0,1), B:(1,1,12), and C:(5,2,11). Their exact quotient orders are 16,12,16. The finite-field geometric sums of their action matrices at those orders are zero, as saved in generator_norm_checks. Their orders remain exactly 16,12,16 for every choice of the two free normal vectors. All six positive/inverse quotient elements are distinct, so the resulting Cayley graphs are simple and degree 6; connectedness remains a separate condition.

The four D7 cases have orders 39984, 52224, 66096, 66096 and respectively 400,585,820,820 projective vector assignments. Simultaneous nonzero field scaling of the two vectors commutes with rho and is a group automorphism. Thus first-nonzero-coordinate=1 is an exact normalization; the all-zero setting is disconnected. Total: 2625 assignments.

F8 has no common invariant F8 line, but its prescribed matrices have entries in F2. A control whose four field coordinates lie in a proper F2 subspace need not generate the full additive normal group. Both F9 representations preserve the line spanned by (1,2). Irreducibility or connectedness was never inferred merely from the field size. The producer's complete finite tests are in ../RESULT.json.

The F11 initial control uses A=[[7,5],[1,4]], B=[[0,10],[1,10]] and normal tuple (0,1,0,2). Its representation is valid, but its actual graph has diameter 9 and 986 vertices outside the identity R8 ball; see ../q11_D8_control/RESULT.json. The subsequent, separately authorized complete F11 projective family is in ../q11_D8_projective/RESULT.json.

All field/action tables were exported and checked in 0.038012277 CPU seconds. This table task performed no parameter search, graph generation, or BFS. The original source graph was not revalidated.
