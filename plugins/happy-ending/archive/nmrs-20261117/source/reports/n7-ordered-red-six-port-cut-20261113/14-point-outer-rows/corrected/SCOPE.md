# Fourteen-point safe outer-row extraction

Physical order: U=1..6, r=7, s=8, V=9..14. The six assigned left terminal
rows and six right source rows are pairwise distinct on each side, with r
the row of u6 and s the row of v1. Full 14-domain packet, no R7/B6, no weak7.
The original 12-point induced U union V has its previous exact predicates.
No mixed-B4 ban is applied to paths using r or s.

No ambient R5 goes from U to V, using any retained points. No R6 ends in U
or starts in V. In this 14-domain any R6 starting in U may only have
endpoints (u6,r), and any R6 ending in V may only have endpoints (s,v1).
These are SOURCE/TERMINAL endpoint restrictions, never penultimate/second
restrictions. Both exceptional pairs are adjacent in the extracted domain.
The source-row locks are provided by the caller's M0 three-chain lemma;
the present encoding does not re-prove that ambient import.

r cannot start B5; s cannot end B5; no B4 has endpoints (r,s).
For all retained x<u6 and z>r, impose chi(x,u6,r)=R and chi(u6,r,z)=B.
For all x<s and y>v1, impose chi(x,s,v1)=B and chi(s,v1,y)=R.
These derive from the real red-six terminal/source hats and the real
blue-five first/last pairs, respectively.

No ambient existence predicates are inferred from absence of an induced path.
SAT checks only this necessary projection; UNSAT requires full clause-set
reconstruction and a successful proof checker bound to the formula.
