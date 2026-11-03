# Actual tower-prefix signature passes; K6 free-port gate fails

The one frozen prefix [0,132860,172076,179888,182618,186033] was tested once against the already cached actual186033 CSR and currentdegree bytes. No alternative offset, vertex permutation, source or helper count was tried.

The structural prediction is SUPPORTED. All original182618 vertices have the expected internaldegree in their fixed interval: H9-like layer132860 vertices of internaldegree10; H7-like39216 of degree8; H5-like7812 of degree6; H4-like2730 of degree5. Exactly one connectivity/two-color traversal was performed perlayer. Each layer is connected and bipartite, with colorclass sizes66430/66430,19608/19608,3906/3906,1365/1365. Color0 is the class containing the least oldlabel of that layer, not an independently bound geometric point-versus-line orientation.

Every later originalvertex has exactly2 neighbors in every earlierlevel and those anchors have oppositecolors. All63030 such two-anchor conditions passed. The oldlater-neighbor multiplicities at every earliervertex are0or1, as recorded in RESULT.json. These are source-label/part signatures, not a proof of generalizedhexagon isomorphism or internal diameter6.

The separate six-half-class capacity prediction is REFUTED. The first three classcounts were:

- H9 color0:12353 currentdegree<11 ports.
- H9 color1:12280 currentdegree<11 ports.
- H7 color0:0 currentdegree<11 ports, below the required6.

The two H9 counts total24633. This is not the24643 total of oldfree vertices derived across allupperlevels in the earlier paper note. H7 color1 and the two H5 colors were not counted after the decisive failure; their values remain unknown here. No full six-class free pool or label-color binary was exported.

Each helper in the fixedK6 rule requires a free port in each of these six classes. A class containing no such port blocks the rule outright on the current source. Thus no cooperative R5/R4 mask generation, solver,186039graph or source-diameter recheck is warranted for this rule. Other connectionrules are not adjudicated.

Successful worker PID2395092; session29980 completed with processCPU1.214964867s and wall1.286615629s under the20CPU hard bound. An initial project-root path calculation exited before opening any source and is preserved in PRESTART_FAILURE.json with0source reads/traversals; its separateCPU was not measured. It was a launch correction, not another prefix trial. The successful mathematical run read the existing CSR once and used its degree cache.

The executed writer mislabeled the structural prediction REFUTED when its later capacity check failed. RESULT_METADATA_ERRATUM.json records the metadata-only correction toSUPPORTED; all numeric fields and the capacity failure are unchanged. The executedscript is retained as run_executed_v1.py; run.py has the future writer fix and was not rerun.

Counts: four layerconnectivity/two-color traversals, zero sourceD6 distanceBFS, zero newradiusballs, zero solvercalls, zero candidategraphs, zero alternatepartitions. Everything is terminal. This is a newlabel-binding and resourcegate, not source recovery or a new independent graph method.
