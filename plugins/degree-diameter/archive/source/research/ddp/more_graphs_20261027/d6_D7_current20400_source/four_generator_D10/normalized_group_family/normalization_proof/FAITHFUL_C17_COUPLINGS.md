# Two faithful scalar couplings for the fixed normal action

This is a classification only of the faithful C17 scalar couplings with the fixed source action on F5^2 and the fixed H48. It is not a classification of all groups of order 20400, or of all two-dimensional H representations.

Let A=[[4,2],[1,1]], B=[[0,4],[1,4]]. Then A^2=3I and A beta A^-1=beta^-1 in this representation. An H automorphism sends alpha to beta^u alpha^k, k odd, and beta to beta or beta^-1. Since k is odd, the square of the new alpha acts on F5^2 as A^(2k)=3^k I. Linear conjugacy preserves scalar matrices, so equivalence of the fixed normal action forces 3^k=3, namely k=1 modulo 4.

This condition is sufficient. A beta conjugation removes the beta^u factor. For k in {1,5,9,13}, A^k is either A or -A. The invertible matrix S=B-B^2 satisfies S^2=2I, SBS^-1=B and SAS^-1=-A, so it realizes the required sign change without changing beta. Conjugation by A additionally realizes beta inversion. Thus the allowable exponent subgroup is exactly {1,5,9,13} modulo 16.

Every primitive C17 scalar can be written chi(alpha)=5^e, with e odd modulo 16. Composition with the allowable H automorphisms multiplies e by an exponent congruent to 1 modulo 4. There are exactly two orbits, distinguished by e modulo 4. Representatives are chi(alpha)=5 and chi(alpha)=5^3=6. Rescaling C17 does not identify them: all automorphisms of its one-dimensional additive group commute with the scalar action.

For chi=6, 6^2=2 and 6^8=-1 modulo 17, hence its order is 16. All steps of PROOF.md remain valid: odd alpha phases have invertible I-A^a and 1-chi(alpha)^a; all involutions have zero F5^2 coordinate; the independent normal scalings remain automorphisms. The 216 normalized four-generator sets therefore cover every connected degree-four Cayley graph for this new fixed group as well. Their connectedness proof uses the unchanged beta action and A^2=3I, so all 216 are connected.

The three old diameter-11 controls belong to chi=5. Their diameter results cannot be inherited for chi=6. The new producer must evaluate all 216 representatives. This note performed only the displayed finite-field matrix identities, with no generating-set enumeration, graph generation, or BFS.
