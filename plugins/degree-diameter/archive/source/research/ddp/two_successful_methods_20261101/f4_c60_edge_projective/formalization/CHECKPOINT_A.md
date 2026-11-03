# Checkpoint A — actual encoding and original target

Review pending: the root's configured Gemini A call returned an output-token-limit ERROR, without a substantive verdict. No automatic repeat was made.

Original mathematical object: the fixed graph in ../PARAMETERS.json, ../generate.py and ../PROOF.md, on 60 controller vertices times the 64-element GF(4)^3 fiber. Labels are 64*a+x0+4*x1+16*x2. GF(4) uses polynomial encoding 0,1,w,w+1 and w²=w+1; it is not ZMod4.

Actual source bodies to back-translate independently:

- formal/DegreeDiameter/Portfolio/F4Graph3840Field.lean: F, F.add, F.mul, F.ofCode, F.code, act.
- formal/DegreeDiameter/Portfolio/F4Graph3840.lean: controllerData, matrixData, directionData, controller, inversePort, matrix, direction, encodeVec, decodeVec, stepVec, fiberStep, controllerOf, fiberOf, liftAt, forward, graph.
- formal/DegreeDiameter/Portfolio/SingleExtension.lean:15: DiameterAtMost G D := ∀ u v, ∃ p : G.Walk u v, p.length ≤ D.

The generator formalization/generate_lean.py reads every controller, dart matrix and direction literal from PARAMETERS.json. The field tables are handwritten exact GF4 operations; numeric parameter codes are fed through F.ofCode so that ring numeral 2=0 cannot silently replace the encoded element w.

Intended unconditional exported declarations in namespace DegreeDiameter.Portfolio.F4Graph3840:

```
concrete_order_degree_and_D3 :
  Fintype.card (Fin 3840) = 3840 ∧
    (∀ u, graph.degree u ≤ 20) ∧ DegreeDiameter.Portfolio.DiameterAtMost graph 3

diameter_exact_three_in_project_definition :
  DegreeDiameter.Portfolio.DiameterAtMost graph 3 ∧
    ¬ DegreeDiameter.Portfolio.DiameterAtMost graph 2
```

These declarations are targets and are not yet claimed proved. No certificate assumption may survive on either exported theorem.

Proof connection interfaces:

1. The concrete reverse controller and matrix binding gives forward_reverse for all u,p,t. Its caller will discharge matrix inverse/transport by kernel checks of the literal table, not by asking the final user for hypotheses.
2. adj_iff_forward then makes every neighborhood the image of Fin5 × F, proving degree≤20.
3. Three actual forward steps construct a genuine graph.Walk of length3. Controller and vector endpoint equations will be supplied from the 3300 fixed rank routes, and the 300 fixed adjacent-pencil routes, using symbolic affine linearity plus finite kernel-checked local decoders.
4. A concrete pair with no forward word of length≤2 will imply ¬DiameterAtMost graph2 using Walk decomposition, following the already proved generic walk interface of the old F5 module without changing it.

Scope: fixed deterministic formula graph. No ASCII parser theorem, exact20 regularity theorem, literal edge-text identity theorem, or public novelty claim is intended. The existing independent all3840-root acceptance is reused and not rerun.

Reviewer request: independently translate the source bodies and proposed final types, compare them with the original graph and genuine-walk target, identify any weakened claim or unbound parameter. Do not rate a plan as a checked final proof.
