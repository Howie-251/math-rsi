# Directprimary LCF source and C7/radius4 model inputs

The localtriad-to-LCF isomorphism attempt is genuinely UNKNOWN: the sole GraphMatcher process reached its8CPU hardlimit, exit-9, at7.997978 workerCPU plus0.002022506 driverCPU. BINDING_RESULT.json and binding_terminal.json preserve it, and no map or successful189-edge isomorphism is asserted. It was not retried.

The parent subsequently selected a different evidence route: the official Maple LCFGraph documentation directly lists generalizedhexagon126/189 with exactly the saved18offset sequence repeated7; Sage's official Tutte12Cage description supplies126/189/girth12/D6. SOURCE_LCF_PRIMARY.json uses that primaryrecipe directly. This does not resolve the old local-label mapping and does not rely on it.

The actual standalone source is source126.edges with126vertices/189edges/all3regular. Adding18 modulo126 sends all189 edges to sourceedges. AUTOMORPHISM.json saves this actualpermutation, its18 cycles of length7, and9even/9odd cycles. No completeAutgroup was computed.

One source-radius cache pass traversed each126root only throughdepth4. All layers are1,3,6,12,24, giving closedR4 size46. RADIUS_CACHE.json saves the exact closed balls; old_distance_to4.u8.bin is a126x126 row-major uint8 array, with0..4 exactdistances and255 meaningbeyond4. OLD_FAR_PAIRS.json lists5040 unorderedpairs outsideR4:3024oppositeparity and2016sameparity. KnownD6 plusbipartition can identify their olddistances as5/6, but no newD5/D6 BFS was performed.

The cache preparation body used0.028389041 CPU seconds. These126 bounded source traversals are actualwork, not hidden behind an oldsourceBFS0 shorthand. They are model-input preparation rather than another completeD6 sourceacceptance. Sourcegeometry/LCF graph construction, one explicitC7 edgepermcheck and this cache are the entire newactualwork. There are no matchingatoms, perfectmatchings, augmentedgraphs, SAT/MIP/SA calls or targetdistancechecks.

An olddistance>4 domain for a newmatchingedge avoids a shortcycle containing thatone newedge; it does not by itself exclude4/5cycles withtwo newmatchingedges. Further augmentedgirth claims require their own exactconstraints. The parent will specify the remaining model, rather than this source-preparation task silently imposing or claiming them.
