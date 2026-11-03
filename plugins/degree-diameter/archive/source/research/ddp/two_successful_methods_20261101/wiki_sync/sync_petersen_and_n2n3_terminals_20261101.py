"""Two canonical mechanism nodes; preserve exact finite/paper scopes and human top."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync'
LABEL='PETERSEN_AND_N2N3_TERMINALS_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
def evidence(p,names):
    a=[p+x for x in names];assert all((R/x).is_file() for x in a);return a
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];records={r['id']:r for r in L['rows']}
assert len(records)==before
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs','pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs','known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k] for k in keys};assert tuple(counts[k] for k in keys[:5])==(153,43,47,105,4)
P=S+'stale_record_transfer_d3D6/petersen_c14_140_route_gate/'
root=read(P+'ROOT_DISPOSITION.json');gate=read(P+'RESULT.json');structure=read(P+'STRUCTURE_RESULT.json');rank=read(P+'AFFINE_F16_RANK_RESULT.json')
assert root['status']=='ROOT_ACCEPTED_COMPLETE_NO_FIXED_PETERSEN_REGULAR_GROUP14_AND_SCALAR_AFFINE_F16_MODELS'
assert root['all_processes_terminal'] and not root['running']
assert gate['raw_word_capacity_survivors']==gate['distinct_mod7_form_capacity_survivors']==[21,62]
assert gate['all_directed_NB_words_generated_once']==1900 and gate['parity_signatures_tested']==64
assert rank['prediction_supported'] and rank['status']=='ALL_SCALAR_AFFINE_F16_PETERSEN_COVERS_DIAMETER6_IMPOSSIBLE'
assert all(x['integer_minor_determinant']==-1 for x in structure['results'])
pid='ddp-stale-d3d6-petersen-route-group14-h20-affine7-scalar-affine16-complete-no-20261101'
scopeP='Fixed literal Petersen10/15 and literal inverse edge maps,gauge9treeedges/6cotreeparameters,targetD<=6. CompleteNO:alltranslationC14covers and allregularorder14group-voltagecovers of this base;allscalar-affineF7edgecovers of the two actual20/30 bases from signatures21/62;allscalar-affineF16edgecovers of literalPetersen,includingtranslationF2^4. NotarbitraryS14/S16/S7permutationcovers,semilinear/higher-dimensionalotherlineargroups,otherbasecontrollers or allcubicD6graphs.'
pathsP=evidence(P,['PRED.md','HISTORY_SCOPE.json','NOTE.md','INPUT_AND_TREE_GAUGE.json','ALL_NB_WORDS_AND_INTEGER_FORMS.json','SLOT_RAW_FORM_COUNTS.csv','ALL64_SIGNATURE_RESULTS.json','ALL64_SIGNATURE_SUMMARY.csv','RESULT.json','TERMINAL.json','run_once.py','SURVIVOR_SIGNATURE_DETAILS.json','CANONICAL_BIPARTITE_DOUBLECOVER_CAPACITY.json','CANONICAL_NONADJACENT_SIX_WORD_WITNESS.json','PAPER_DOMAIN.md','STRUCTURE_PRED.md','STRUCTURE_RESULT.json','STRUCTURE_TERMINAL.json','STRUCTURE_NOTE.md','structure_once.py','PAPER_ODD_WHEEL_CONDITIONAL.md','PAPER_STRUCTURE_BINDING_REVIEW.json','C14_AND_ORDER14_NO_PROOF.md','AFFINE_F16_PRED.md','AFFINE_F16_RANK_RESULT.json','affine16_rank_once.py','PAPER_AFFINE16_COLLISION.md','PAPER_AFFINE16_BINDING_REVIEW.json','PAPER_AFFINE16_NO_PROOF.md','FINAL_NOTE.md','ROOT_DISPOSITION.json'])
for sig in [21,62]:pathsP+=evidence(P+f'signature{sig}/',['H20.edges','FACES_AND_RETURNS.json','ODD_WHEEL.json','FACE_CYCLE_MINOR.json'])
rowP=dict(id=pid,title='3D6 Petersen路线机制完整NO：order14正则群cover、两H20的affine7与Petersen scalar-affine16，各范围分别闭合',
    family='Petersen voltage-cover route compatibility',idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',wiki_verdict='no',
    record_type='complete_model_specific_route_compatibility_obstruction',target_Delta=3,target_D=6,savedL=132,
    baseline_date='Inherited cached primary132/1998;no newpublic/sourcequery',n=dict(actual=None,hypothetical=140),actual_graph_Delta=None,actual_D=None,
    actual_D_scope='No140/160targetcandidate orBFS;one small-base word/parity gate plus exact small certificates and complete scoped paper proofs',ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=6,
    scope=scopeP,outcome_class=root['status'],new_lower_bound=False,
    distance_text='先预测并实际支持Petersen≤6NB槽25/21/17，1900words一次生成；64parity全部测，raw与distinctmod7形式各仅21/62存活。canonical43的非邻槽6预测支持，实际全局更紧adj槽5，原flag检查globalmin6的错误已更正且不改结论。两个实际H20各12pentagon、每根七returnwords=empty+三face双向；wheel center0/rim1,6,8,10,2迫三faceclass不兼容。两11×11整face-cycle minor均−1，使scalar-affine7线性holonomy全可gauge掉，归translation7矛盾；order14正规C7商用raw容量同样归两H20。另scalar-affineF16：17words覆盖16输出迫去一outlier后16slopes相同；17个15×6矩阵mod3/mod5均rank6，CRT迫六乘子为1，translationF2⁴闭路逆对重复仅≤13<16。无C7/C14电压赋值搜索、140/160图/BFS/solver/Lean/付费，整个case3.688288616/5CPU。',
    lesson_and_restart_condition='Stop these exact model families,not generalcubicD6. Initialrawcapacitysurvivors were necessary only;the new lesson is globalface compatibility and inverse-route aliasing,not slowly improvingbadpairs. Do not rerun1900words/64signatures,enumerateC7assignments or startC14/F16/fieldladder. A nextmodel must change routegeneration and state a concrete newquestion. AFY70ordinary2cover/132edge-repair/715Petersenhelper oldNO was not applied to this scope.',
    restart_condition='A genuinely changedbase or connection-mapclass outside the four proved domains,with a separate bounded question;not a second parameter scan of the closed domains.',
    unclosed_gap='GeneralS14/S16permutations,semilinear/otherlineargroups,othercontrollers and generalN(3,6) remain open;paper/certificates are not Lean or newgraph results.',
    other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
        auxiliary_base_Petersen=[10,15],auxiliary_H20_bases=[20,30],auxiliary_bases_counted_as_newgraphs=False,
        hypothetical_target_orders=[140,160],Moore_bound=190,baseline=132,Moore_space=58,Moore_space_is_not_constructibility=True,
        history_same_scope_NO_or_UNKNOWN_not_located_before_work=True,not_derived_from_old_AFY70_or715_scope=True,
        raw_NB_words_generated_once=1900,raw_slot_counts=[25,21,17],raw_count_prediction_supported=True,
        parity_signatures_complete=64,raw_capacity_survivors=[21,62],distinct_mod7_form_survivors=[21,62],
        canonical_allodd_signature=43,canonical_global_min_raw=5,canonical_nonadjacent_six_prediction_supported=True,
        canonical_flag_correction_preserved=True,intermediate_survivors_not_acceptedgraphs=True,
        actual_H20_faces_each=12,return_words_each_root=7,nonempty_returns='threepentagons,bothorientations',
        oddwheel=dict(center=0,rim=[1,6,8,10,2]),integral_cycle_minor_determinants=[-1,-1],
        complete_NO_scopes=root['complete_NO_scopes'],affineF16_outlier_deletion_cases=17,
        affineF16_integer_difference_shape=[15,6],affineF16_all_rank_mod3_mod5=6,
        affineF16_exponent_modulus=15,translationF2power4_return_upper=13,required_return_fiber_size=16,
        C7_C14_assignments_evaluated=0,target_graph_BFS_solver_Lean_paidreviews=0,
        wholecase_CPU_seconds=root['wholecase_CPU_seconds'],CPU_budget_seconds=5,
        Lean_status='PAPER_AND_EXACT_SMALL_CERTIFICATES_NOT_LEAN',all_processes_terminal=True),evidence_paths=pathsP)

Q=S+'stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/'
nr=read(Q+'ROOT_DISPOSITION.json');a=read(Q+'RESULT.json');at=read(Q+'TERMINAL.json')
assert nr['status']=='ROOT_ACCEPTED_COMPLETE_NO_N2_N3_TWO_CUT4STAR42' and at['all_processes_terminal']
assert a['configurations_finished']==6150 and a['complete_fixed_N2_N3_rule_exclusion'] and a['hit']is None
assert [s['newroot_R3_passed']for s in a['source_results']]==[6,0]
nid='ddp-stale-d4d3-messieres-n2n3-two-cut4star-source-comparison-20261101'
oldN1='ddp-stale-d4d3-messieres-n1-all3075-two-cut-fourstar42-no-20261101'
sourceid='ddp-stale-d4d5-messieres-three41-any-ninecover-capacity-20261101'
assert oldN1 in records and sourceid in records
changed=dict(status='ROOT_AUTHORIZED_SEPARATE_BOUNDED_CHANGED_RULE_BATCH',terminal_result_received=False,
    source='N2only,sixactualnewrootPASSbasecases',rule='choosep in4pins andthirdoriginaledge(a,b)outsidepins withp-aoldnonedge;deletea-b andstar-p,addp-a andstar-b',
    meaning='threeoriginalcutsplusoldoldrepair,maintains4regularity;nottheruled-outtwocut4starfamily',
    prediction='AtleastonevariantrepairsitsfirstoldpairandkeepsnewrootR3;complete42unknown',
    maximum_variants=3936,CPU_budget_seconds=5,owner='/root/f9_56862_independent',
    root_reported_in_progress=True,no_result_claimed=True,no_N4_or_blindcut_ladder=True)
pathsN=evidence(Q,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json','ROOT_DISPOSITION.json','run_once.py','N2_RESULT.json','N3_RESULT.json','N2_ALL_PAIR_PARAMETERS.tsv','N3_ALL_PAIR_PARAMETERS.tsv','N2_ALL_PAIR_STAGES.tsv','N3_ALL_PAIR_STAGES.tsv','ONE_OLDPAIR_ROUTE_DIAGNOSTIC.json'])
C=S+'stale_record_transfer_d4D5/alternative41_ninecover_gate/'
pathsN+=evidence(C,['source_N2.NORMALIZED_ADJ.json','source_N3.NORMALIZED_ADJ.json'])
rowN=dict(id=nid,title='4D3 N2/N3两cut4star对照6150案全NO：N2六次新根通过却全旧点失败；新三cut修补批独立待终态',
    family='Existing graph old-edge repair and helper completion',idea_family=records[sourceid]['idea_id'],date='2026-11-01',wiki_verdict='no',
    record_type='complete_fixed_source_comparison_and_changed_rule_followup',target_Delta=4,target_D=3,savedL=41,
    baseline_date='Inherited cached MessieresN2/N3 41/82/4regular/D3;no source revalidation',n=dict(actual=None,hypothetical=42),actual_graph_Delta=None,actual_D=None,
    actual_D_scope='All6150actual42/84edited candidates rejected;newrootfirst thenoldlabelsuntilfirstfailure,noaccepted42/globalDclaim',ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=3,
    scope='OnlycachedliteralMessieresN2andN3,eachall3075unorderedpairsofdisjointoldedges;delete2oldedges,newvertex41joinedtoall4endpoints. CompleteNOforbothfixedtwocut4starfamilies. The separate now-authorized N2 thirdcut+oldoldrepair batch changes the generationrule,doesnotinherit this NO,and has no receivedterminal yet. Nototherhosts/rewirings/general4D3 or oldordinaryninecoverD5.',
    outcome_class='ROOT_ACCEPTED_COMPLETE_NO_N2_N3_TWO_CUT4STAR42_SEPARATE_REPAIR_SCOPE_PENDING',new_lower_bound=False,
    distance_text='预测至少N2/N3一源也有newrootR3pass得到支持：N2实际3075案中3069newrootfail、6pass却全oldoldfail，14candidate旧根BFS；N3实际3075全newrootfail、0旧根。共6150全访，每sourcecacheparse1。全批仅N2首pair(0,1)一次旧源诊断，pins1/2/4/35为ONE_PIN：旧3路0–37–4–1包含cut1–4，实际新最短4路0–18–8–13–1。N1首反例BOTH_NONPIN、N2首ONE_PIN，换source改变覆盖数却没有使新旧覆盖同时实现；不称旧routeunique。无sourceD3allroot/非同构/field/solver/Lean重验，1.503331119/5CPU含readgate1.125664745。',
    lesson_and_restart_condition='Stop the exacttwo-cut4star rule forN1/N2/N3;more newrootpasses alone is not fullgraphprogress. Root has separately authorized the genuinechangedN2rule:one extra oldedgecut plusoldoldrepair,conditioned on the sixactualnewrootPASSbasecases,atmost3936variants/5CPU. Its test is to repairthefirstoldpairwhilekeepingnewrootcoverage,thenfull42;it is pending,not a rerunof6150 or automaticN4/cutladder. Await actualterminal and rootdisposition before updating this same node,no independentnewmethod count.',
    restart_condition='Onlythealreadyroot-authorized boundedchangedN2thirdcut/oldoldrepair scope may proceed;no repeatofclosedtwo-cut domains or newsource/seed extension.',
    unclosed_gap='SeparateN2thirdcut+oldoldrepair result notyetreceived;otherhosts/rewirings/generalN4D3 remain open.0new acceptedgraph/parameter/Lean.',
    other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
        related_N1_experiment=oldN1,related_cached_source_node=sourceid,ordinaryninecover_same_scope=False,
        actual_source_domains=[3075,3075],all_configurations_finished=6150,newroot_passes=[6,0],newroot_fails=[3069,3075],
        oldold_fails_after_newrootpass=[6,0],candidate_oldroot_BFS=[14,0],prediction_newroot_supported=True,complete42hits=0,
        source_cached_JSON_parses=[1,1],source_single_pair_diagnostic=1,source_D3_allroot_nonisomorphism_rechecks=0,
        diagnostic=nr['one_original_source_pair_diagnostic'],old_route_unique_claimed=False,
        contrast_to_N1=nr['contrast_to_N1'],complete_NO_scope=nr['strict_scope'],
        cumulative_charged_CPU_seconds=at['cumulative_charged_CPU_seconds'],CPU_budget_seconds=5,
        prior_readgate_CPU_seconds=at['prior_readgate_CPU_seconds'],no_timer_reset=True,
        original_two_cut_batch_all_processes_terminal=True,separate_changed_generation_scope=changed),evidence_paths=pathsN)
rows=[rowP,rowN];ids=[x['id']for x in rows];assert all(i not in records and not(W/'experiments'/f'{i}.md').exists()for i in ids)
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
    text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->')and LABEL not in text
    prefix[fn]=text[:text.index(END)+len(END)]
rawpath=OUT/f'{LABEL}_ROWS.json';rawpath.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
norm=[]
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w')as log,contextlib.redirect_stdout(log):
    for raw in rows:
        n=c['normalize'](raw);n['goal']['baseline_date']=raw['baseline_date'];c['write_node'](n);records[n['id']]=n;norm.append(n)
# Preserve originalN1 proof scope,adding only the actual later-source comparison pointer.
oldpath=W/'experiments'/f'{oldN1}.md';text=oldpath.read_text();assert LABEL not in text
oldpath.write_text(text+'\n\n<!-- '+LABEL+' -->\n## 后续N2/N3同架构对照终态\n\n本页N1旧3075案NO仍有效且不重跑。N2/N3各3075案后来也完整NO：N2六次newrootpass却全oldoldfail，N3无pass；首N2旧pair0→1为ONE_PIN、3→4，区别于N1首BOTH_NONPIN。见[同机制sourcecomparison]('+nid+'.md)。现root另批N2第三cut＋oldoldrepair改变生成规则、尚待终态；不可拿上述two-cutNO外推，不新增独立方法。\n')
u=dict(path='research-wiki/experiments/'+nid+'.md',date='2026-11-01',note='N2/N3samearchitectureeach3075completeNO;distinctthirdcut+oldoldrepairscopepending,notcoveredbyoldNO.')
for d in [records[oldN1]['other_metrics'],records[oldN1]['source_record']['other_metrics']]:d.setdefault('later_source_comparison_updates',[]).append(copy.deepcopy(u))
L.update(rows=list(records.values()),record_count=before+2,updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=2
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
def table(n):
    safe=c['safe'];return '| ['+safe(n['title'])+'](experiments/'+n['id']+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+n['evidence_paths'][0]+') |'
mp=W/'DDP_METHOD_LEDGER.md';md=mp.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{before+2}条记录；不以此宣称{before+2}种独立方法。',1)
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' Petersen兼容性闭合与N2/N3 sourcecomparison终态\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+'\n'.join(table(n)for n in norm)+'\n\n两个机制实验节点，不计新图/参数/Lean/独立方法。Petersen的初步21/62必要门幸存并非最终开放：后续face/oddwheel及rank证明已在各exactscope闭合。N2/N3旧two-cut域终态NO；新第三cut＋oldoldrepair是root已授权的独立改变规则小批，尚未收到终态，后续原位更新同N2节点而不加方法。153/43/47、savedmain105/4、global0不变，15老格、sameGoal ACTIVE/N8n61暂停继承。\n';mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 最新两scope终态：Petersen四固定模型NO；N2/N3 two-cut全6150NO\n\nPetersen1900≤6NBwords一次/槽25,21,17；64parity仅21/62幸存。两H20实际七returnwords/12faces与oddwheel使face三类不能同时实现；minor−1归scalar-affine7为translation7。结合raw商门排Petersen所有regularorder14groupcovers（含C14和order14dihedral）。另17word碰撞迫16同斜率，全部17outlier差矩阵mod3/5rank6消去F16乘子，return逆对仅13<16，排固定Petersen全部scalar-affineF16（含F2⁴translation）。各域严格NO，不排任意S14/S16/semilinear/其他base/general3D6；3.688288616/5CPU，0targetgraph/BFS/solver/Lean/付费，不续C7assignments/field梯。\n\nN2/N3各3075全访：N2六次newrootpass全部oldoldfail、14候选旧根；N3无pass。唯一旧源pair诊断N2的0→1 ONE_PIN，旧0–37–4–1长3，新0–18–8–13–1最短4，不称unique；1.503331119/5CPU，0sourceD3allroot重验。two-cut4star规则在N1/N2/N3都终态关闭。root现另批N2六个pass基例的第三cut＋oldoldrepair，≤3936variants/5CPU，测试修首旧pair兼保newroot；这是实际改变规则的独立有界scope，正在执行/终态未收，不冒成功或NO、不另计方法。\n\n'+str(before+2)+'条记录（非方法），153图／43参数／Lean47、savedmain105/4、global0不变。保留15老格人工顶块、sameGoal ACTIVE及旧N8/n61暂停；16416既有全技术交付继承不重验。\n\n'+'；'.join('['+n['title']+'](experiments/'+n['id']+'.md)'for n in norm)+'\n\n'
preserved={}
for fn,pre in prefix.items():
    path=W/fn;txt=path.read_text();assert txt.startswith(pre);at=len(pre);txt=txt[:at]+'\n\n'+nav+txt[at:]
    if fn=='index.md':
        m=re.search(r'^## Experiments \((\d+)\)$',txt,re.M);assert m
        txt=txt[:m.start()]+f'## Experiments ({int(m[1])+2})'+txt[m.end():];pos=txt.index('\n',m.start())+1
        txt=txt[:pos]+''.join('- `exp:'+n['id']+'` — '+n['title']+' [no]\n'for n in norm)+txt[pos:]
    assert txt[:at]==pre;path.write_text(txt);preserved[fn]=True
helper.append_log(str(W),LABEL+': two canonical mechanismexperimentnodes only;Petersenraw64gate21/62survivors followedbyactualH20oddwheel/unimodularfacebasisandF16all17mod3mod5rankcompleteNOinexplicit4modelscopes;N2/N3all6150twocut4starNO,onepinoldpair3to4. RootseparatechangedN2thirdcut+oldoldrepairbatchpending/notcoveredbyoldNO/notanothermethod. No graph/parameter/Lean/methodincrements,no reimport/rebuild/rerun/paidreview;human15oldcells top preserved,153/43/47 unchanged.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==before+2 and {k:after[k]for k in keys}==counts
receipt=dict(status='PASS_TWO_CANONICAL_TERMINALS_WITH_SEPARATE_CHANGED_RULE_PENDING',updated_UTC=NOW,
    records_before=before,records_after=before+2,records_added=2,new_experiment_ids=ids,
    graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
    Petersen_model_specific_complete_NO_scopes=root['complete_NO_scopes'],Petersen_not_general_cubicD6_NO=True,
    N2_N3_all6150_two_cut_NO=True,newroot_prediction_supported_6=True,
    N2_thirdcut_oldoldrepair_separate_scope=changed,changed_scope_terminal_result_received=False,
    old_N1_scope_original_preserved=True,human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,
    numeric_source_graph_BFS_Lean_solver_paidreview_hash_runs=0,
    root_STATE_HTML_REPORT_recovery_builder_modified=False,writes_limited_to_Wiki_and_stage_wiki_sync=True,
    sameGoal='ACTIVE',old_N8_n61='PAUSED',CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
