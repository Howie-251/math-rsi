"""One family/eight accepted graph instances; consume receipts without rerunning checks."""
from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[2];W=ROOT/'research-wiki'
S='research/ddp/two_successful_methods_20261101/'
B=S+'retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/'
F=B+'multiplicity65_72_family/';I=F+'independent_acceptance/'
PUB=S+'public_baseline_audit/'
STEM='P33_EIGHT_ACCEPTED_ONE_FAMILY_133_26_LEAN19_20261101'
ID='ddp-gq77-published-p33-immutable-fulln64-clone-eight-degree65-72-family-20261101'
PUBLICID='ddp-public-w3f7-partial-ovoid33-primary-table5-corrects-65-70-77-comparison-20261101'
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
read=lambda p:json.loads((ROOT/p).read_text())
result=read(I+'RESULT.json');summary=read(I+'SUMMARY.json');terminal=read(I+'TERMINAL.json')
production=read(F+'RESULT.json');coords=read(B+'RESULT.json');interface=read(B+'INTERFACE_RESULT.json')
window=read(PUB+'P33_CLONE_DEGREE65_72_WINDOW_20261101.json')
assert result['status']=='PASS_ALL_EIGHT_P33_ENDPOINT_GRAPHS'
assert terminal['status']=='PASS' and summary['all_eight_have_own_complete_literal_binding']
assert len(result['cases'])==8 and result['all_new_literal_N_bindings']==59400
assert result['actual_new_literal_R3_BFS_roots']==13200
formal_state=read(F+'formalization/STAGE_STATE.json')
instances=[]
for case,pub in zip(result['cases'],window['endpoints']):
    assert case['degree_cap']==pub['Delta'] and case['n']==pub['candidate_n']
    instances.append(dict(Delta=case['degree_cap'],D=3,n=case['n'],m=case['m'],actual_diameter=3,
        mathematically_validated_complete_graph=True,complete_Lean_graph_instance=False,
        known_nonrecord=False,known_publicly_dominated=False,latest_global_record_confirmed=False,
        confirmed_publictable_improvement=False,best_located_public_lower_bound=pub['current_published_method_guarantee'],
        bounded_gain=50,copy_count=case['k'],graph_path=F+f'graphs/d{case["degree_cap"]}_D3_n{case["n"]}.edges',
        degree_histogram={'64':case['degree64_count'],str(case['degree_cap']):case['high_degree_count']},
        independent_literal_fullN64_rows=case['new_vertices'],actual_new_root_BFS=case['actual_new_literal_R3_BFS_roots'],
        proof_derived_histogram_distribution=case['proof_derived_histogram_distribution'],
        actual_BFS_histogram_distribution=case['actual_BFS_histogram_distribution'],
        all_pair_prefix_proof_independent_of_max_BFS=True,max_BFS_used_to_infer_smaller_diameter=False,
        formal_status='Kernel queue staged PASS, external binding/final acceptance pending; not counted complete',
        external_A='encoding checkpoint423 in flight',external_B='not requested',external_distinctfreshC='not requested'))
evidence=[B+x for x in ['PRED.md','RESULT.json','TERMINAL.json','ACTUAL_POINTS.json','PROOF.md','INTERFACE_NEW_SET_PRED.md','INTERFACE_RESULT.json','INTERFACE_NOTE.md']]
evidence += [F+x for x in ['PRED.md','PROOF.md','RESULT.json','TERMINAL.json','ORDERED_CLONE_RECIPE.tsv','PREFIX_LOADS.csv','produce.cpp','run_once.py']]
evidence += [I+x for x in ['PRED.md','SUMMARY.json','RESULT.json','TERMINAL.json','PROOF.md','verify.cpp','run_once.py','SOURCE_R2_ONLY_PREDICTIONS.csv','cases/d72_n173250/NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv']]
evidence += [F+'formalization/'+x for x in ['PRED.md','STAGE_STATE.json','TARGETS.json','GQ77Published33CloneFamilyExact_RESULT.json','GQ77Published33CloneFamilyAudit_RESULT.json']]
evidence += [PUB+x for x in ['W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md','W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.json','P33_CLONE_DEGREE65_72_WINDOW_20261101.md','P33_CLONE_DEGREE65_72_WINDOW_20261101.json']]
evidence += [g['graph_path'] for g in instances]
family=dict(id=ID,title='公开P33复现＋filled160050不可变N64复制：65..72八完整图已独验，具体Lean/新外审未结',
    family='Prototype-neighborhood extension',idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',
    target_Delta=None,target_D=3,savedL=None,baseline_date='2026-11-01 current published-method guarantee160000+1650k from primary W(7)33, global/priority unconfirmed',
    record_type='complete_literal_graph_family_global_novelty_pending',n=dict(actual=None,hypothetical=None),actual_graph_Delta=None,actual_D=3,
    actual_D_scope='八图各自完整字面旧边/全部新点N64/degree绑定＋独立old-only-interior全点对/每prefix证明；仅max k8全部13200新根BFS补充，各小端点0BFS。未由大图BFS推出小图直径。',
    ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=3,wiki_verdict='yes',
    outcome_class='EIGHT_COMPLETE_LITERAL_GRAPHS_FRESH_INDEPENDENT_ACCEPTED_CONCRETE_LEAN_AND_NEW_REVIEWS_PENDING',
    distance_text='同一P33×50=1650原N64，k1..8给65/161700、66/163350、67/165000、68/166650、69/168300、70/169950、71/171600、72/173250，全fresh独验PASS，各比已核公开保证多50。全部保原5121600边、0newnew；105600原pins负载k，degree64点54450+1650k、degree64+k点105600。59400是八图新点完整N绑定，不是BFS数；independent sourceparse1/R2only1650一次（33根3185、1617根3248），0旧R3/field重验。仅k8实际13200新根BFS，264×(1,64,3193,169992)+12936×(1,64,3256,169929)全部逐根符合；其余七图靠各自binding及独立prefix路由证明。独验21.419453053CPU、生产2.152313735CPU。',
    scope='固定已接受filled160050/64regular源＋本轮实际33点坐标复现/原50spread序，按q=1650copy+50i+j复制不可变完整原N；只k1..8终点。同family8实例非8方法。新68n166650/m5544000与旧70同阶同边数但degreehist不同，不合并为同实例。',
    positive_guarantees=['33点大小归功Cimráková–Fack2007 §4.3/Table5；本次在原400点顺序找到实际新坐标，528新pair非零、400line交数136/264，无新partial-ovoid纪录或framework。',
        'fresh接口1650个原N64两两不交：105567原productpins＋33原fillpins，共105600；center诱导528K2＋594isolates，不要求独立center。',
        '所有prefix只用原160050内部点作短路；等center、相邻center和非邻分别有明确路由，源collapseHom保nonD2，因此八图各自恰D3。',
        '每新根准确预测(1,64,R+k,159985−R+1649k)，R从sourceR2-only一次实测。只有k8实际BFS，k1..7为证明导出的histogram，不冒直接测量。',
        '公开源仍160000，原P33存在性/一般复制只给160000+1650k；本地160050没有冒作公开。Payne特定packing最有利包络至72仍低329，非公开构造下界。'],
    unclosed_gap='root已接受八完整数学图；具体Lean的20chunks/Exact/Audit已阶段编译PASS，但最终外部binding/完整回执未结，本次新增Lean0。新scope仅一次共享Gemini A423编码checkpoint在途，B与distinctfreshC尚未派，不继承旧O22/source的外审PASS。全球最高/优先权未认证；旧冻结包不含本family。',
    lesson_and_restart_condition='明确33公开例推翻旧O22竞争优势后，先实际复现公开大小，再核filled源33个fillpin替换和N64不交，立刻改变规则到1650中心。公开65..72窗口全+50后统一生产八端点；一次源R2预测＋max BFS和各prefix证明避免重复验证，未扩73+或把每clone前缀记新结果。先闭合当前八具体原目标及独立Audit/新scope外审，不自动degree梯子。',
    other_metrics=dict(validated_graph_instances=instances,mathematically_validated_complete_graph=True,
        new_lower_bound_mathematically_verified=False,new_named_complete_graphs=8,new_Lean_instances=0,new_frameworks=0,
        rules=1,accepted_endpoint_instances=8,new_parameter_pairs=[[d,3] for d in [66,67,68,69,71,72]],
        replacement_local_representatives={'65,3':161700,'70,3':169950},old_O22_graphs_remain_legal_and_publicly_dominated=True,
        public_partial_ovoid_credit='Cimrakova-Fack2007 Table5 W(7)33 computational example; local coordinates reproduction only',
        published_object_coordinate_reproduction_CPU_seconds=coords['accounted_CPU_seconds'],
        fresh_interface_CPU_seconds=interface['CPU_seconds'],public_object_reproduction_counted_as_new_graph=False,
        source_n=160050,source_m=5121600,base_centers=1650,immutable_N_size=64,base_pins=105600,
        old_product_pins=105567,source_fill_pins=33,base_source_load_zero=54450,base_source_load_one=105600,
        center_induced_edges=528,center_induced_isolates=594,selected_k=list(range(1,9)),
        producer_CPU_seconds=production['accounted_CPU_seconds'],producer_source_parses=1,
        independent_CPU_seconds=21.419453053,independent_source_parses=1,
        independent_new_literal_N64_rows=59400,source_R2_only_centers=1650,source_R2_prediction_batches=1,
        source_R2_only_CPU_seconds=0.022353,source_R2_classes=result['source_R2_count_distribution'],
        actual_new_root_BFS=13200,actual_BFS_k=8,other_seven_endpoint_BFS=0,old_R3_BFS=0,
        source_field_geometry_checks_repeated=False,all_pairs_prefix_proof_independent_of_max_BFS=True,
        max_BFS_used_to_infer_smaller_diameter=False,max_CSR_separate_from_source=True,
        formal_stage_status=formal_state['status'],formal_finite_chunks_compiled=formal_state['finite_chunks_compiled'],
        concrete_Lean_complete=False,formal_final_binding_acceptance_pending=True,
        external_review_A='IN_FLIGHT_ENCODING_CHECKPOINT_ONLY',external_review_A_cell='423',
        external_review_B='NOT_YET_REQUESTED',external_review_distinctfreshC='NOT_YET_REQUESTED',
        public_window_all_gains50=True,global_record_or_priority_certified=False),
    evidence_paths=evidence)

ledger=read('research-wiki/DDP_METHOD_LEDGER.json');old={r['id']:r for r in ledger['rows']}
public=copy.deepcopy(old[PUBLICID]['source_record'])
public['unclosed_gap']='公开33大小现已实际复现：原400点标签下33坐标、528新pair非零，fresh1650N64接口PASS。此复现本身不记图/新纪录；其filled160050上的k1..8八完整图已fresh独验并由root接受，单独family记8实例，具体Lean/新外审未结。公开推论及旧O22两图支配状态保留，全球/优先权未认证。'
public['other_metrics'].update(coordinate_reproduction_status='ACTUAL_REPRODUCED33_AND_FRESH_FILLED_SOURCE_FULLN_INTERFACE_PASS',coordinate_reproduction_CPU_seconds=coords['accounted_CPU_seconds'],interface_CPU_seconds=interface['CPU_seconds'],reproduction_counted_as_new_record=False,subsequent_accepted_family_id=ID,subsequent_accepted_graphs=8,named_legal_total=133,legal_pairs=26,phase_graphs=29,phase_pairs=23,complete_Lean_total=19,pending_outside_saved_table_graphs=27,pending_outside_saved_table_pairs=22)
public['evidence_paths']=list(dict.fromkeys(public['evidence_paths']+[B+'RESULT.json',B+'ACTUAL_POINTS.json',B+'INTERFACE_RESULT.json',B+'INTERFACE_NOTE.md',I+'SUMMARY.json',I+'PROOF.md']))
rows=[family,public]
assert all((ROOT/p).exists() for r in rows for p in r['evidence_paths'])
raw=W/'updates'/f'{STEM}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
cmd=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(raw)]
x=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True);assert x.returncode==0,(x.stdout,x.stderr)
sync=json.loads(x.stdout)

erratum='expert_review_current/AFFINE_CLONE_ADDENDUM_20261101_PUBLIC_COMPARISON_ERRATUM'
assert all((ROOT/(erratum+ext)).exists() for ext in ['.html','.html.txt','.docx'])
intro=f'''<!-- {STEM} -->
# 当前：P33同一family八完整图已独验，133例／26参数；具体Lean仍19

同Goal ACTIVE：133合法图／26参数、阶段29图／23参数，ledger416，具体Lean19。旧known-publicly-dominated43（含旧65/70）不变，savedoverlap40；outsidepending27例／22参数，全球认证0。

[P33八图](experiments/{ID}.md)：65..72阶161700／163350／165000／166650／168300／169950／171600／173250，当前已核公开保证各+50。65/70更新代表，66/67/68/69/71/72六新参数；一family非八方法。公开33大小复现credit2007，不当新partial-ovoid纪录。

独验59400新点完整N64绑定；sourceparse1、1650sourceR2only一次(3185:33/3248:1617)。仅k8全部13200新根BFS逐根命中264×(1,64,3193,169992)+12936×(1,64,3256,169929)，其余七图0BFS靠各自完整binding＋old-only内部路线证明，非由大图BFS外推。独验21.419453CPU，0旧R3/field重验。

20finitechunks/Exact/Audit阶段编译PASS，但完整binding／终回执未结，新增Lean0；新scope仅A423编码审阅在途，B/C未派。旧冻结包不改，[四图公开比较勘误](../{erratum}.html)已另写，不替代历史包。不扩73+，先闭合八原目标。以下保留历史。

'''
gap=W/'gap_map.md';text=gap.read_text()
if not text.startswith(f'<!-- {STEM} -->'):gap.write_text(intro+text)
h=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
if f'<!-- {STEM} -->' not in h.read_text():
    with h.open('a') as f:f.write(f'''\n\n<!-- {STEM} -->
## 2026-11-01 公开P33复现改变实际连接，统一八端点已验收

延续既有人工要求及时保存直觉→预测→实测及精确范围，不新增Goal或第二计划。公开33点表推翻旧O22竞争判断后，实际找到原400点序下33坐标：528pair非零／line交数0:136、1:264；复现1.185446749CPU，归功Cimráková–Fack2007大小结果，不计新纪录。fresh接口.071535943CPU确认P33×50=1650个filled160050原N64互不交，共105600pins=105567oldproducts+33原fill，诱导528K2+594isolates；未重验旧field或大图。

公开65..72固定窗口全+50后，同一个immutable-N64规则统一生成[八完整图](experiments/{ID}.md)。root已实际接受：65/161700、66/163350、67/165000、68/166650、69/168300、70/169950、71/171600、72/173250。新68与旧70同n166650/m5544000但cap和degreehist不同，按(Delta,D,n)区分。旧161150/166650两图继续合法且已知公开支配；新65/70更新本地代表，其余六参数新。133合法/26参数、stage29/23，Lean19、main103/3、knownpublicdominated43/overlap40、outsidepending27/22、global0。

fresh独验对八图各自完整旧边、全部59400新行N64、degree逐项绑定；independent sourceparse1，1650center R2-only一次实际3185:33/3248:1617。只有maxk8实际13200新根BFS，264×(1,64,3193,169992)+12936×(1,64,3256,169929)逐根匹配；其余七图实际0BFS，来自各自binding与独立old-only-interior全点对/每prefix证明，不能称用大图BFS推小图。生产2.152313735CPU、独验21.419453053CPU，0旧R3/field重验。SUMMARY/RESULT/TERMINAL/完整PROOF现都已落盘。

本次不增Lean：20finitechunks及8具体原目标/独立Audit已阶段编译PASS，最终外部binding/完整终回执待结。新scope只有一次共享Gemini A423 encoding在途，B与distinctfreshC未派，不继承旧O22审阅。先完成这些原目标，不自动73+。root另写[公开比较勘误](../{erratum}.html)及[原生Word](../{erratum}.docx)，旧四图冻结包和更早包保持不动。
''')

helper=ROOT/'aris_repo/tools/research_wiki.py';calls=[]
def call(*args):
    c=[sys.executable,str(helper),*args];r=subprocess.run(c,cwd=ROOT,text=True,capture_output=True)
    calls.append(dict(command=c,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr));assert r.returncode==0,calls[-1]
for target,evidence in [(PUBLICID,'Published33 size reproduction credit; only filled-source clone family counts eight graphs, not newpartialovoid/framework.'),('ddp-gq77-classical-opposite-spread-fill-160050-d64-d3-20261101','Inherited accepted160050 source/old-only routes; no sourcegraphBFS/field revalidation.')]:
    # Use the actual existing source ID rather than assuming a new one.
    if target not in old:
        if target==PUBLICID:raise AssertionError(target)
        matches=[r['id'] for r in ledger['rows'] if r.get('actual_order')==160050 and r.get('actual_degree')==64]
        assert len(matches)==1,matches
        target=matches[0]
    call('add_edge',str(W),'--from','exp:'+ID,'--to','exp:'+target,'--type','uses','--evidence',evidence)
call('log',str(W),'2026-11-01 P33onefamilyeightactualfullgraphs65..72freshaccepted133legal26pairsstage29_23Lean19;59400literalnewNrowsnotBFS,onlyk8all13200newrootsBFS,1650sourceR2onlyonce,0oldR3/fieldrerun. Onefamilynewnodeledger416 pluspublic33existingreproductionstatusupdate;kernelstagePASSexternalbindingpending,A423encodinginflightB/Cnotrequested;publicdominated43overlap40outsidepending27/22global0,frozenpackunchanged.')
call('rebuild_index',str(W));call('rebuild_query_pack',str(W))
cp=W/'updates'/f'{STEM}_HELPER_CALLS.json';cp.write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
current=read('research-wiki/DDP_METHOD_LEDGER.json')
expect={'record_count':416,'validated_named_graph_examples':133,'validated_named_parameter_pairs':26,'complete_Lean_graph_instances':19,'known_publicly_dominated_graph_examples':43,'known_publicly_dominated_also_saved_table_improvement_examples':40,'pending_outside_saved_table_graph_examples':27,'pending_outside_saved_table_parameter_pairs':22}
for k,v in expect.items():assert current[k]==v,(k,current[k],v)
stored=next(r for r in current['rows'] if r['id']==ID)
assert len(stored['other_metrics']['validated_graph_instances'])==8
assert not any(g['complete_Lean_graph_instance'] for g in stored['other_metrics']['validated_graph_instances'])
resolved=set(p for r in rows for p in r['evidence_paths']);assert all((ROOT/p).exists() for p in resolved)
checked=0
for p in [W/'experiments'/f'{r["id"]}.md' for r in rows]:
    for t in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        t=unquote(t.strip('<>').split('#',1)[0])
        if not t or re.match(r'\w+://',t):continue
        assert (p.parent/t).exists(),(p,t);checked+=1
q=(W/'query_pack.md').read_text();assert 'ledger416' in q and '133' in q and '13200' in q
receipt=dict(updated_UTC=now,status='PASS_UNIQUE_WIKI_EIGHT_P33_LITERAL_GRAPHS_ACCEPTED_LEAN19_PENDING',ledger_records=416,records_added=1,records_updated=1,new_family_rules=1,accepted_graph_instances_in_family=8,new_parameter_pairs=6,named_legal_graphs=133,legal_parameter_pairs=26,stage_graphs=29,stage_pairs=23,complete_formula_Lean=19,new_concrete_Lean_count=0,known_publicly_dominated=43,saved_table_dominated_overlap=40,pending_outside_saved_table_graphs=27,pending_outside_saved_table_pairs=22,certified_global_records=0,all_new_N64_binding_rows=59400,actual_new_root_BFS=13200,actual_BFS_scope='k8 only; k1..7 zeroBFS and separate literalbinding+old-only proof',source_R2_only_centers=1650,independent_CPU_seconds=21.419453053,formal_stage_status=formal_state['status'],external_A='encoding423inflight',external_B='notrequested',external_freshC='notrequested',canonical_upsert_command=cmd,canonical_upsert_stdout=sync,actual_helper_calls=str(cp.relative_to(ROOT)),resolved_evidence_paths=len(resolved),checked_markdown_links=checked,query_current=True,experiments_rerun=0,root_owned_files_modified=False,frozen_expert_packets_modified=False)
rp=W/'updates'/f'{STEM}_RECEIPT.json';rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
