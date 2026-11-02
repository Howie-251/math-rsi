# Paper-only normalization attack: supported for the fixed four-parameter model

2026-11-01. Independent paper check only: no field powers, coefficient forms, controller words, graph, solver, Lean or external review were recomputed. Actual conventions were read from the sibling `coefficient_alias_gate/FORM_MODEL.json`, its route formula and the saved twelve darts.

The phase coordinate is x∈Z/23, notZ/69:69 is the number of three-base phase states. Inherit r=6, r^23=1 andr≠1. Thus r has order23 and v_2=r^6−1≠0. No new numerical power check is needed.

For a positive dart (b,x,y)→(b′,x+a_j,y+r^x c_j), conjugate by the same bijection on all bases

    Φ_d(b,x,y)=(b,x,y+r^x d).

Comparing its endpoints gives c′_j=c_j+(r^{a_j}−1)d. Both fixed cross01/02 darts have a0 and translation0, so they stay fixed. The inverse dart, whose translation is−r^(x−a_j)c_j, transforms into the true inverse with parameterc′_j; no independently normalized inverse is substituted. The shared parameters stay shared. Reversing the convention forΦ merely replacesd by−d and gives the same orbit reduction.

Writev_j=r^{a_j}−1. Setd=−c_2/v_2. Each four-vector therefore has exactly one representative in the hyperplanec_2=0 under this additive gauge. Global scalingΨ_s(b,x,y)=(b,x,sy), s≠0, preservesr, the phases, the zero cross darts andc_2=0, and multiplies all remaining parameters bys. Hence every nonzero remaining triple(c_0,c_1,c_12) has exactly one representative whose first nonzero entry is1. These are P²(F139), with139²+139+1=19461 representatives, plus the zero triple:19462 total. The zero case includes originalc parallel tov and must be tested separately. Any additional graph isomorphisms would only create harmless overcounting, not missing parameters.

Coverage cardinality is preserved slot by slot. For each saved wordw, the gauge increment of its endpoint form telescopes to(r^x_end−r^x_start)d, the same constant for all words in that ordered phase slot. Scaling multiplies every endpoint by the same nonzero scalar. Thus the complete tight image receives a common affine bijection and has unchanged cardinality.Φ_d need not fix the particular normal-coordinate0 root; the telescoping identity itself proves the image-cardinality assertion for the fixed-root coefficient evaluation. No false pointwise-root-fixing premise is required.

Therefore, **if every one of these19462 representatives fails to cover all139 normal coordinates in the saved tight slot**, the whole fixed four-parameter/r6/F139 family fails diameter≤8. If one passes, it is only a necessary-slot pass; no all-slot or graph claim follows. The normalization does not cover other phases, multipliers, extra independent edge parameters, nonzero fixed cross translations outside the stated gauge family, or arbitrary permutation lifts.

No invalid gauge, phase-component leak or omitted normalization orbit was found under these exact input conventions. This note reviews the reduction, not the actual159-form data or the pending finite enumeration.
