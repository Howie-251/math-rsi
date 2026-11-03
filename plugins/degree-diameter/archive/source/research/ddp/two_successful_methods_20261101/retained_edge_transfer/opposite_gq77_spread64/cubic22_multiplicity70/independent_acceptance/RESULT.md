# A70 independent acceptance: PASS

The complete literal `graph_d70_D3_n166650.edges` is independently accepted: **166650 vertices,5544000 edges, maximum degree70, exact diameter3**. The source is the original accepted160050/5121600/64-regular graph. The161150 graph was not read.

- All5121600 original old edges match the immutable source body entry for entry. The full candidate has proper endpoints, strict global edge order, and no repeated edge.
- All6600 new labels individually connect exactly to their specified base center's complete64-neighbor set, independently recovered from the original source edge file. Copy order is outermost: k=1100copy+50i+j, newlabel160050+k. All six repetitions per base center are bound literally. Added edges:422400; new-new edges:0.
- Every old pin load is checked individually:89650 old vertices have load0;70400 have load6. Actual degrees:64 at96250 vertices,70 at70400 vertices.
- All6600 new roots actually pass ordinary FIFO queue radius3 BFS;0 old roots were run. The prediction was written first and the actual per-root classes and aggregate counts agree exactly:132 roots have(1,64,3191,163394);6468 have(1,64,3254,163331). Every root reaches166650 vertices. See `NEW_ROOT_BFS.csv` for every root's copy, base index, center, predicted class, measured histogram, and match flag.
- Full all-pairs and every-prefix diameter-at-most3 follows from the inherited accepted source theorem plus the immutable-full-neighborhood clone lemma in `PLAIN_PROOF.md`. Same-center clones use2 steps; adjacent-center clones use3. Routes use only old source vertices and their endpoint clones, so no prefix borrows future clones. The source has231 actual edges among the distinct base centers. The degree70 diameter2 order bound4901 proves exact diameter3.

The10-root pilot cost0.035732 CPU seconds and predicted25.703978 CPU seconds for the complete validator. Actual measured acceptance-process total, including one compile, all BFS, driver preparation and result aggregation: **26.343279409 CPU seconds /90**, one worker. The validator's internal total is25.270636 CPU seconds, including23.094774 for BFS. Actual compile and validation child CPU receipts are1.028157 and25.278185 seconds. No timer or scope extension occurred.

The closed source concrete Lean theorem is inherited; no new Lean compilation was performed here. This task makes no public global-record or priority claim. `SUMMARY.json`, `RESULT.json`, `TERMINAL.json`, `PRED.json`, the independent inputs, validator source, and actual compile/run logs provide the machine-readable evidence.
