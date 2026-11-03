import json,pathlib,sys
P=pathlib.Path(__file__).resolve().parent;ROOT=pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
r=json.loads((P/'RESULT.json').read_text());assert len(r['sources'])==2 and all(s['status']=='SOLVER_UNSAT_COMPLETE_AT_MOST_FIVE_LINE_DOMAIN_UNCERTIFIED' and len(s['rounds'])==1 for s in r['sources'])
r.update(actual_n=None,actual_D=None,ordinary_bad_unordered_pairs=None,new_lower_bounds=0,raw_line_columns_preserved=True,old_blockmask_dedup_used=False,prior_invariant_UNSAT_dependency=False,CEG_new_point_cuts=0,complete_domain_status='Raw solverUNSAT for all <=5 selected originalaffinelines on eachsource; no independentlycheckedprooflog',unrestricted_15_pin_domain_status='OPEN: earlier full-independent/asymmetric SAT calls were UNKNOWN',capture_screen='clean')
report='''# Joint affine-line point cover: both necessary models UNSAT

This batch asked whether at most five free affine3-lines can jointly cover the source by their complete cached point balls. It preserved every original line:2808 for the15552/D4 source and3510 for the102060/D5 source. It did not use the earlier312/390 whole-fiber representatives and did not discard lines with an empty whole-fiber column. Different lines sharing a whole-fiber mask can still cover different points; the saved fixed offset counterexample demonstrates why these distinctions matter.

The exact clause for a target t is the OR of every line incident to any free pin whose cached R3/R4 contains t. Thus partial images from several selected lines can complement each other inside a fiber. At most five line selectors are allowed. Selected lines may overlap or share a controller; their literal pin union has at most15 distinct points. There is no lex restriction or negative cut from the previous inversion models, so these decisions do not depend on the earlier invariantUNSAT results.

Initial targets were every controller's zero and plus/minus coordinate-basis points:1728 for D4 and4620 for D5. These are necessary constraints only. The planned CEG loop would decode every SAT set, check the full original n-point cached-ball OR, and for each missing fiber add its first missing target and negative. Every such point clause would be valid and would exclude the current assignment; no missing-count objective or best-score choice was used.

In the actual run both initial necessary formulas were already UNSAT. D4 used2808 line selectors,19656 total variables,35414 clauses and1594416 covering literals; one requested49second call returned code20 after11.707798 childCPU seconds. D5 used3510 selectors,24570 variables,46730 clauses and7455870 cover literals; its one49second call returned code20 after8.833548 seconds. All lines were represented in both counters and point supports.

UNSAT of a necessary subset rules out a cover of all source targets in this complete at-most-five-line domain, subject to the raw solver result; no independently checked UNSAT proof log was produced. It also excludes a proposed pin set contained in such a five-line union, since adding the remaining free points of the union preserves both coverage and the15-spoke bound. This does not exclude arbitrary independent sets of at most15 free pins; their earlier full-SAT questions remain UNKNOWN.

There were zero SAT candidates, zero full-point OR candidate checks, zero learned CEG cuts, zero graph exports, new balls, source-diameter BFS or solver retries. Both sources ended in round0, so no ninth-round or budget question arose. Source1 PID1706030, source2 PID1711425 and session85493 are terminal. Recorded aggregateCPU25.794664232seconds, including the carried interface cost, is below130; parent preparation remained below15 and each source solver used less than50.

All original target lists, exact CNFs, stdout, model statistics and round outcomes remain in source15552/ and source102060/. The loader reads the actual complete free-cache row order and all raw line metadata; it does not compute balls. SourceD was inherited, and no existing delivery/example was modified. Stop this five-line batch without another seed, source, timer or line-budget expansion.
'''
proof='''# Why the joint CEG reduction is exact for its stated domain

For line L, define its point-cover set as the union of the cached radius-(D-1) balls of its three actual pins. A selected line covers t iff at least one pin of L covers t. Taking the OR of the incident-line masks of all pin coverers of t therefore produces the exact selector clause for that target. No complete-fiber condition is involved.

A union of at most five three-point free lines has at most15 distinct free pins. Retain all source edges and join the new vertex exactly to that union. Its distance to old t is one plus the distance from the union to t, so full point coverage plus actual degree legality proves the new diameter bound. SAT is accepted only after the full n-point cache OR and eventual actual-degree/edge checks.

Every initial test point is a necessary target. If a SAT assignment misses t in the authoritative full point OR, its current selectors have no intersection with t's exact support clause. Adding that clause excludes the assignment while preserving every possible complete cover. The negative point is another ordinary valid target clause. Monotone additions change constraints rather than select an improved-score candidate or retry a seed.

Consequently a completed UNSAT result at any round rules out the complete stated five-line domain even though only a subset of all targets was present. A SAT result at a partial round is only a candidate. UNKNOWN, time budget or the fixed round bound leaves the family unresolved. In this run both initial formulas returned rawUNSAT; no CEG candidate or extra clause was generated. This note does not certify the solver's UNSAT proof and does not exclude unrestricted15-pin sets.
'''
fields={'status':'TWO_COMPLETE_RAW_FIVE_LINE_DOMAINS_SOLVER_UNSAT','record_type':'joint-point-cover-variant-of-existing-source-port-cover-rows','sources':r['sources'],'raw_lines_complete':{'15552':2808,'102060':3510},'old_fullfiber_columns_used_as_joint_equivalence':False,'lines_with_empty_fullfiber_masks_preserved':True,'selected_line_budget':5,'joint_partial_fiber_complements_allowed':True,'prior_negative_cut_used':False,'lex_used':False,'initial_target_rows':{'15552':1728,'102060':4620},'solver_calls':2,'raw_UNSAT_sources':2,'UNKNOWN_sources':0,'SAT_candidates':0,'fullpoint_OR_candidate_checks':0,'CEG_added_constraints':0,'new_graphs':0,'new_balls':0,'source_D_BFS':0,'aggregate_CPU_seconds':r['aggregate_CPU_seconds'],'negative_scope':'All <=5 originalaffinefreelines, including overlap/multiplelinespercontroller, on each fixedsource. Raw solver decision without independentlycheckedprooflog.','open_scope':'Unrestricted <=15freepin neighborhoods remain UNKNOWN, othergeometry/connectionrules notexcluded.','report_paths':[],'capture_screen':'clean'}
for name,obj in [('RESULT.json',r),('RAW_ANALYSIS_FIELDS.json',fields),('CEG_CURSOR.json',{'status':'TERMINAL_BOTH_SOURCE_ROUND0_UNSAT','next_round':None,'learned_point_cuts':0,'pending':[]})]:
 (P/name).write_text(json.dumps(obj,indent=2)+'\n')
for name,text in [('REPORT.md',report),('MODEL_SCOPE.md',proof)]:
 assert not screen(text);(P/name).write_text(text)
fields['report_paths']=[str((P/name).relative_to(ROOT)) for name in ['PREDICTION.json','RESULT.json','REPORT.md','MODEL_SCOPE.md','RAW_ANALYSIS_FIELDS.json','TERMINAL.json','CEG_CURSOR.json','run.py','support_loader.py','ANALYSIS_JOINT_CEG.md','ANALYSIS_JOINT_CEG.json'] if (P/name).exists()]
for n in [15552,102060]:
 for name in ['INITIAL_TARGETS.json','round00_MODEL.json','round00_TARGETS.json','round00_RESULT.json','round00.cnf','round00.stdout','RESULT.json']:
  fields['report_paths'].append(str((P/f'source{n}'/name).relative_to(ROOT)))
(P/'RAW_ANALYSIS_FIELDS.json').write_text(json.dumps(fields,indent=2)+'\n')
print(json.dumps({'status':'FINAL_RAW_ANALYSIS_READY','file':str(P/'RAW_ANALYSIS_FIELDS.json'),'solver_calls':2,'new_graphs':0,'unrestricted_pin_domain_excluded':False}))
