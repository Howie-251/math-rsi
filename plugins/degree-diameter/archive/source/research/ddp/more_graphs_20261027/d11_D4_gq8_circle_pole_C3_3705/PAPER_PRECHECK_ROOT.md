# Pre-numeric refinement for the two standard spread lines

Root supplied this derivation before receiving any numerical q8 phase result. It retains the initially suggested [3,3,3] histogram as an earlier prediction and refines it to [2,3,4] for the specified orientation. The candidate rule is unchanged.

Let S0={(x,0)} and S∞={(0,y)}. The nine four-incidence geodesics between their base lines are indexed by x∈F64*/F8*, with the intermediate line through (x,0) and (0,1/x). Its spread-label circle is C=hF8∪{∞}, h=x^-2. On this circle the specified lexicographic outside point is t0=1 unless hF8=F8; for the latter it is the primitive element2.

After t'=1/(t+t0), its finite-circle centre is c=1/(h*Tr(t0/h)). Pulling the pole back gives label t0+1/c =h*(t0/h)^8. The four-incidence phase is chi(pole), because the endpoint spread phases cancel the scalar x and1/x factors.

For the eight hF8≠F8 classes, t0=1 and pole=h^-7. Thus chi(pole)=−7chi(h)=2chi(h) mod3. Among all9 projective h classes each character has multiplicity3; removing the F8 class removes a0, leaving [2,3,3]. The exceptional class takes t0=2 and pole=2^8, contributing character2. This predicts [2,3,4]. Reversing path orientation gives [2,4,3].

The stronger equal-multiplicity prediction is therefore expected to fail; the weaker necessary all-three-colours test is still expected to pass. A missing colour stops the candidate before constructing3705 vertices. A passing histogram is only this one line-pair test, not a complete graph certificate.
