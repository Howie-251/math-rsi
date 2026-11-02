# The six-point longside can be the six non-F3 points

Use the existing encoding F9=F3[u], u²=-1, with u=3 and u^-1=6. On the standard Rédei15 infinity line, its six selected slopes are D={1,2,4,5,7,8}. The four omitted projective points are {infinity,0,u,2u}=u·PG1(F3). They are a Baer subline.

The line projectivity m -> u^-1 m sends this omitted subline to PG1(F3), hence sends D to PG1(F9)\PG1(F3), exactly the six nonfixed points. In the saved coordinates [Z,X,Y], the explicit plane projectivity is diag(1,1,6). Thus the proposed intersection-line footprint has no cross-ratio obstruction.

Let ell have an F3 basis e0,e1, and choose w in the nonstable singular plane outside ell. Every projectivity of the required type can be written

    [Z,X,Y] -> Z*w
        + (aZ+r(A00 X+A01 6Y))*e0
        + (bZ+r(A10 X+A11 6Y))*e1,

where A runs through24 canonical PGL2(F3) matrices, r runs through F9* and a,b through F9. The PGL2(F9) stabilizer of PG1(F3) is exactly PGL2(F3): normalize the images of a projective frame of three F3 points, after which a projectivity fixing that frame is identity. Normalizing the transverse coefficient to1 leaves the relative nonzero scalar r and the81 translations. Therefore each fixed plane has24·8·81=15552 projectivity parameters. Duplicate Rédei pointsets are permitted and are subsequently removed exactly.

For a nonstable plane with intersection ell, its nine selected off-line points have Frobenius partners outside the plane. Its six on-line points form three complete Frobenius pairs. Thus the whole-class raw preimage has24 points. If all selected classes are unsplit, its actual mandatory set has12 pins. Each split class adds one pin. This justifies the cap3 line gate for degree12 and cap4 for degree13, reserving at least nine pins for the off-line classes. Degree legality and full current-graph R4 remain separate obligations. No graph is produced by this proof.
