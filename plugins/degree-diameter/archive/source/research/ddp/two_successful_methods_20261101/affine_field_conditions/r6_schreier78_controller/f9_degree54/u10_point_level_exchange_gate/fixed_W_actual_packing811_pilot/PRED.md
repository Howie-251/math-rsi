# P3 before the only actual packing solver call

P3: Does the fixed W={(a,b,4*a)} candidate pool contain at least811 centers with pairwise disjoint genuine complete source N54, while retaining all81centers in each of controllers31,59,60,72?

Exactly one fixed pool: retained324centers, all15admissible othercontrollers [16,17,30,32,35,42,43,44,45,58,61,64,71,73,74] times81Wpoints, total1539candidatecenters and1215binaryselectionvariables. Controllers64 and71 remain included even though absent from the earlier positive capacity support. No eta/phase/seed/retained change, old wholelayeropt search, edgefile read, field/rank revalidation, BFS, Lean, newparameter or follow-on family.

Reuse the accepted GF9 multiplication table, actual eight matrices/trueinverse dart indices, controller table and inverseport directions. Generate every candidate's complete54pins by y=M*x+t*ell_inverseport for all sixports/allt inF9, label729*v+y0+9y1+81y2. Addition is coordinatewise mod3 under a+3b fieldencoding, not integer mod9. Fixed pins must be disjoint. Every actual sourcepin gives a setpacking inequality; variable cardinality>=487, hence total>=811.

The prior811countvector and fixed-support837LP are necessarycapacity evidence only. In particular837 is not the P3 target or a constructed packing. Threeactualnoise directions at target48 from17,35,74 are independent (inherited determinant6). Disjoint axisparallel line families have sizes A<=bc, B<=a(9-c), C<=(9-a)(9-b), so ABC<=20^3. Therefore at least one count is<=20, including zero-family cases. Root's independently proved cut min(w17,w35,w74)<=20 is valid. Add threebinaryswitches z_u with w_u<=20+61z_u and sumz<=2; no unproved support restriction. A single small determinant may bind this actual target, with no whole-chart checks.

One scipy.milp feasibility call, objective0, exact integer pin constraints and cardinality>=487. One worker, total60CPU including imports/preparation/model/solver/aggregation. Use threads1 and time_limit44wallseconds, reserving room below the solver45CPU ceiling; no LP before or solver after. The zero objective's dualbound is not a maximum-center bound.

If an integer solution appears, verify all selected54pin lists using a separate dictionary, including the324retainedcenters, and save literal orderedcoordinates andpins. Only this directcheck permits a packingPASS. INFEASIBLE closes only this retained4/fixedW finitepool at solver evidence scale; a timelimit or unsupported prediction is UNKNOWN, not a family exclusion. No automatic timer extension, differentseed or newgraph/Leanproduction.
