# Source-neighbourhood seeded cover: final bounded Ccase batch

**Positive prediction:** at least one unselected original center with exactly4 zero-residual neighbours has a full-sourceN design whose available subset can be supplemented by currentavailablepins to total≤16 while covering all16416 current targets.

Take allactual savedprofile rows satisfying unselected andzero_residual_neighbours=4 (expected162, do not forcecount). For eachv deriveoriginalNv bycurrentadj filtered<15552, fourblocked=currentdegree16, fixedseedFv=Nvminusblocked. Reuse all4050currentpin R3 and fulloldsourceR3 saved in cooperativecase; compute no new balls. Check fullNv R3 union equalsallcurrenttargets, and seedpins arecurrentavailable.

For eachv run one max-uncovered-gain/actuallex greedy addingallavailableextras and one redundancydeletionpass on extras only. Save initialholes, categories indexedbywhichof4blockedR3balls covertarget, and everyextra'sactualrepairedholemask/categorycounts. Firsttotal≤16 validateswholecurrentunion then produces16417 graph, preservingall129240currentedges,degree/PIN_SET/newZroutes;stop.

If alltemplates need>16, freeze unique minimumtotalcount/tieactualv template. Run one warmHiGHS minextras residualcover usingonlyitsinitialholes asrows andallavailableextras, preservingactualmapping through empty/duplicatecolumn pruning. Window≤20seconds, thread1, onepassModel/setSolution/run. Onlybestextras<=16−seedsize plusactualwholeunion producesgraph. No-hit/time/rawsolver claim remainsUNKNOWN, notoptimal orfullfamilyNO. No secondtemplate/seed/solve.

CumulativeC cap120 inherits37.985870069 includingvisibleK5preexecutionfailure. Newprep reserve0.5, childhard65/soft60 plusparentactualCPU;nonewball/sourceD4/field/oldallrootBFS/Lean/ARIS. Newroot routeBFS onlyafterpositivehit. This lastC batch stops regardlessoutcome.
