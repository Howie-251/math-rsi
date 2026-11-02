# F4 controller enlargement: a capacity bound and one closed lift domain

2026-11-01. No new fiber graph was produced in this batch. The accepted3840 graph is unchanged.

## What was not known

Could the successful C60/F4 construction be enlarged simply by increasing its cyclic deck, while retaining the five-conic full-pencil/rank-route mechanism? The bound and exact experiment below make this a small, testable question rather than a modulus ladder.

## Certificate bound: at most68 control vertices

At a central dart the four projected incoming and four projected outgoing directions lie in the five-point projective line PG(1,4). A full adjacent pencil forces their union to contain all five points, hence exactly three of the sixteen central turns have rank below three and thirteen have rank three. A simple5regular controller of order c therefore provides exactly65c rank-three three-words.

The current sufficient certificate requires one rank-three word for each of c(c-5) nonadjacent/equal ordered controller pairs. An equal pair actually consumes at least two: reversing a full-rank triangle word gives a distinct full-rank word with the same endpoint pair. Thus c(c-4)<=65c, giving c<=69; five-regularity makes c even, so **c<=68**.

This is a paper bound on the specific certificate used for3840. It does not exclude graphs that cover a layer collectively by lower-rank route images, other frames, or other mechanisms. It is not a new Lean theorem.

## Prediction and direct test

The actual controller is a three-state Schreier organization over Z20. Within the same three-state/even-deck form,66 is the only larger order allowed by the bound. The frozen prediction tested deck22 with unchanged a-voltages(6,3,12), zero b-voltages, and matching shift adjusted from10 to11 in the third state.

First, the deck20 formula was checked literally against the saved60x5 controller; it matched exactly. No source graph or source controller distance was revalidated. For deck22, all <=3 words from the three deck-translation root classes reach only53,58,55 of66 states. In particular0 cannot reach2. Every fiber edge projects to a controller edge, so no choice of fiber matrices can repair this controller gap. Cost0.00115458CPU seconds.

## Changed rule and complete voltage gate

To distinguish bad fixed constants from a structural problem, the next prediction released the four actual voltage variables(alpha,beta,gamma,tau), retaining the base permutations, b's zero-voltage triangle, and the third-state matching half-shift11. Simple inverse-port controllers require alpha!=0,11; beta,gamma,tau!=0; beta+gamma!=0 mod22. The complete176400 assignments were tested once; **none even covers all66 states from root0**. C++ gate0.045885CPU; measured whole child0.046904CPU, within30CPU budget. No SAT call or fiber graph followed. The originally failed fixed tuple appears once inside this full enumeration; this overlap is explicit, not another independent method.

## Why the routes cannot all fit

At the same base state as root0, all <=3 words provide just22 formal residues:

    0,11, +/-alpha, +/-2alpha, +/-3alpha, +/-tau,
    +/-(alpha-tau), +/-(alpha+tau), +/-beta, +/-(beta+tau),
    +/-gamma, +/-(gamma-tau).

To cover a22-element deck, these must all be different. Parity of the ten inverse pairs forces tau odd, and tau=11 collides with the halfdeck. All remaining odd tau are units, so rescale to tau=1. The alpha-dependent residues must leave room for the beta and gamma pairs, which occupy symmetric adjacent pairs of residues. A preliminary odd-run condition is useful but **not sufficient**: six alpha values survive, rather than the initially hoped universal domino obstruction.

The actual saturated same-base condition leaves exactly48 normalized(alpha,beta,gamma) tuples, with alpha in{5,6,9,13,16,17}. Every one has an explicit missing residue in a different base layer; all are saved in NORMALIZED_RESIDUE_EXPLANATION.json. This explains the complete gate: saturating the original layer spends the voltage freedom needed to cover the other layers. A single-plane or total bad-pair improvement would not address this conflict.

## Decision and exact exclusion boundary

Stop this full C3 x Z22 domain. Increasing the cyclic modulus is already blocked by the current certificate bound, and changing only these voltages has been exhausted. Further enlargement must change controller organization, obtain a different controller with adequate route multiplicity, or deliberately change the coverage certificate. No such next search is automatically dispatched. Other66-point controllers, nonzero b-cycle voltage, other lift groups, affine shifts or collective lower-rank coverage remain open.

Evidence: PREDICTION.md, check_once.py, RESULT.json, voltage_gate.cpp, VOLTAGE_RESULT.json, VOLTAGE_RUN_RECEIPT.json, FORMAL_RESIDUE_CAPACITY.json, DOMINO_OBSTRUCTION.json (records the insufficient intermediate test), explain_once.py and NORMALIZED_RESIDUE_EXPLANATION.json. All counts describe controller routes, not missing pairs in a generated4224-point graph. No4224-point graph exists from this batch.
