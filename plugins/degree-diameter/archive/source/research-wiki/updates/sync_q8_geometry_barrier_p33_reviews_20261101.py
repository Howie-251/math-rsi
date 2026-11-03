"""Two local evidence nodes and the existing P33 review fields; no experiment reruns."""
from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[2];W=ROOT/'research-wiki'
S='research/ddp/two_successful_methods_20261101/';Q=S+'retained_edge_transfer/even_q8_gq_geometry_pilot/'
R=S+'reviews/';P=S+'public_baseline_audit/'
STEM='Q8_GEOMETRY_CONDITIONAL_SATURATION_P33_A_B_PASS_C445_INFLIGHT_20261101'
GID='ddp-even-q8-norm-ovoid65-spread65-payne-ovoid64-small-geometry-pilot-20261101'
TID='ddp-full-ovoid-spread-fixed-cap-singlehelper-rsquare-conditional-saturation-barrier-20261101'
FID='ddp-gq77-published-p33-immutable-fulln64-clone-eight-degree65-72-family-20261101'
read=lambda p:json.loads((ROOT/p).read_text())
geo=read(Q+'RESULT.json');gt=read(Q+'TERMINAL.json');sat=read(Q+'SATURATION_BARRIER_RESULT.json');st=read(Q+'SATURATION_BARRIER_TERMINAL.json')
assert gt['status']=='PASS' and st['status']=='PASS'
ledger=read('research-wiki/DDP_METHOD_LEDGER.json');old={r['id']:r for r in ledger['rows']}
zero=dict(new_named_complete_graphs=0,new_Lean_instances=0,new_frameworks=0,new_full_source_graphs=0,BFS_runs=0,Lean_runs=0,solver_runs=0)
common=dict(family='Prototype-neighborhood extension',idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',target_Delta=None,target_D=3,savedL=None,baseline_date='local q8 geometry or conditional saturation, no new complete diameter graph or public record',n=dict(actual=None,hypothetical=None),actual_graph_Delta=None,actual_D=None,ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=3)
g=copy.deepcopy(common);g.update(id=GID,title='q8小几何已完整复现：真F8/F64、O65/spread65及Payne O64/spread64全部PASS，0大图',
    record_type='local_finite_geometry_reproduction',wiki_verdict='yes',outcome_class='ACTUAL_FRESH_Q8_FIELD_AND_TWO_GQ_INTERFACES_PASS_NO_COMPLETE_GRAPH',
    actual_D_scope='新field/小GQ几何及全部非incident projection接口；不构造完整opposite/fill源，不宣D3图或Lean实例。',
    distance_text='2.285789276CPU/20预算，全新q8有限实验终态PASS。F8=F2[x]/(x³+x+1)、F64=F8[z]/(z²+z+1)是真域（非整数mod8/64）。原585PG点/585线全9度，336960非incident投影全唯一；65点ovoid的2080pair非零、每线恰一，65spread分割。Payne保512点，576旧线+64新H线共640线，线8点/点10线，全部322560非incident投影唯一，fullO64与spread64兼容。actualP pointid2/owner64；0完整sourcegraph/BFS/Lean。',
    scope='唯一q8特征2小几何实例，域编码与原Gram/trace/极化/实际共线逐项绑定；是已知几何与fullO大小的复现，不声称新ovoid/newrecord。balanced源342290/81和Payne327744/80都只条件未来fill数量，未生产/验收。',
    positive_guarantees=['具体预测B(X(u),X(v))=N(u+v)成立，N非零向量各向异性，X(a,b)=(1,a,b+N(a+bz),N(a+bz))及P=(0,0,1,1)给O65；2080pair和585line交点都实际检验，非仅计数代替。',
        'F64斜率v=lambda*u与infinity给65spread；Tr(uv′+u′v)等于实际Gram，无额外坐标变换。',
        '派生P使保留点x0=1；新H(a,b)={(1,a,b+t,t)}与范数图唯一交t=N(a+bz)，保住旧isotropic线覆盖并兼容64新增线。旧infinity删除后64spread仍partition512；不能只核原线忽略新线。'],
    unclosed_gap='完整opposite/fill源、current覆盖、具体Lean尚未生成或实例化；局部PASS不能记完整图。源fill同规则的公开优先权仍UNKNOWN，见专门审查；0新记录。',
    lesson_and_restart_condition='实际范数恒等式和新H线交点解释为何特征2的完整O可兼容，而非继续q7 partialO局部调点。下一步继承这套已核数据，不再搜O/spread或重验field；任何完整源须root另行决定及核公开竞争门。',
    variants=[{'label':'balanced_q8_small_geometry','target':[81,3],'actual_source_graph':None,'conditional_unfilled_order':342225,'conditional_fill_order':342290,'full_O':65,'spread':65},
              {'label':'Payne_q8_small_geometry','target':[80,3],'actual_source_graph':None,'conditional_unfilled_order':327680,'conditional_fill_order':327744,'full_O':64,'spread':64}],
    other_metrics={**zero,'CPU_seconds':gt['total_CPU_seconds_including_compile_all_new_field_geometry_checks_and_aggregation'],'F8_modulus':'x^3+x+1','F64_modulus':'z^2+z+1','original_points':585,'original_lines':585,'original_line_and_point_degree':9,'original_nonincident_projections':336960,'original_ovoid_size':65,'original_spread_size':65,'Payne_points':512,'Payne_lines':640,'Payne_points_per_line':8,'Payne_lines_per_point':10,'Payne_nonincident_projections':322560,'Payne_ovoid_size':64,'Payne_spread_size':64,'actual_P_point_id':2,'infinity_spread_owner':64,'known_geometry_reproduction_not_record':True,'conditional_source_D3_instantiated':False,'all_processes_terminal':True},
    evidence_paths=[Q+x for x in ['PRED.md','PARAMETERS.json','RESULT.json','SUMMARY.md','SUMMARY.json','TERMINAL.json','MECHANISM_NOTE.md','pilot.cpp','run_once.py','F8_FIELD_TABLE.csv','F64_FIELD_TABLE.csv','F64_TRACE_NORM.csv','PG3_POINTS.tsv','ORIGINAL_INCIDENCE.tsv','ORIGINAL_ALL_NONINCIDENT_PROJECTIONS.csv','OVOID65.tsv','SPREAD65.tsv','DERIVED_POINTS.tsv','DERIVED_LINES.tsv','DERIVED_INCIDENCE.tsv','DERIVED_ALL_NONINCIDENT_PROJECTIONS.csv','OVOID64.tsv','DERIVED_SPREAD64.tsv']])
t=copy.deepcopy(common);t.update(id=TID,title='条件饱和障碍：fullO×spread复制后，固定cap单helper至少R² pins，非仅fullN限制',
    record_type='conditional_local_singlehelper_theorem',wiki_verdict='partial',outcome_class='CONDITIONAL_ALL_PIN_SINGLE_HELPER_BOUND_R_SQUARED_SUPPORTED_BY_SELECTED_GEOMETRY',
    actual_D_scope='声明filledsource/fullO×spread/k≥1不可变N复制结构下的条件单helper下界；源D3实例未生成，无完整图或新Lean。',
    distance_text='事前只拟off-diagonal R(R−1)门，实际纸面分类加强为R²：pinunion=H\\D，复制k≥1后H\\D都饱和，合法freepins只能D与已有clones；每一freepin两步内只能服务自身clonebaseclass，覆盖全部R²类须|S|≥R²。balanced=4225、Payne=4096。小集合路线诊断0.145388401CPU全部PASS，0大sourcegraph/field/BFS/Lean。',
    scope='固定声明的filledsource、fullO×spread完整code及其k-copy图，保持旧边、固定capδ+k，只加一个helper并向现有free vertices连边。δ+k<R²时任何pin选择均不行，不局限复制完整N；不排jointhelper互连批次、改边、不同code或更高cap。',
    positive_guarantees=['fullO每线唯一点、spread每点唯一线给owner(p,L)；只D的raw selfloop被删除，fill替换后所有basecenters满Nδ、其并集恰H\\D，非只总负载计数。',
        '各D到其他basecenter无1/2步路线；不同baseclass clones也无1/2步路线，freepin只能服务一类，推出R²的任意单helper pin下界。没有短路的下界不依赖sourceD3上界。',
        'actual balanced4160offdiag×D=270400对、Payne4032×D=258048对的相邻/共同oldpair/共同fill全0；额外D对2080/2016也0，支持并加强原预测，不重验field/projection。',
        '当cap≥R²时条件纸面上每类选一个现有clone可达tight R²；因此不是任意巨大k都无扩张。整体D3与tight extension保持仍需sourceD3接口，当前未实例化。'],
    unclosed_gap='source342290/327744的完整D3实例未生产，本节点是条件结构定理。δ+k≥R²、jointbatch、改变旧边或code均未排；不能据此否定一般degree80/81图。',
    lesson_and_restart_condition='若未来fullO源和fullproduct复制实际完成，余下R个旧自由D点没有跨class补洞能力；在当前小cap范围直接停止逐单点调pins，不再仅把它当fullN模型受限。仍可由root选择jointbatch/改边/不同code/提高cap，但本次不派计算。',
    variants=[{'label':'balanced_q8_conditional','target':[81,3],'R':65,'delta':81,'pin_lower_bound':4225,'positive_k_excluded_up_to':4143,'full_source_D3_instantiated':False},
              {'label':'Payne_q8_conditional','target':[80,3],'R':64,'delta':80,'pin_lower_bound':4096,'positive_k_excluded_up_to':4015,'full_source_D3_instantiated':False}],
    other_metrics={**zero,'CPU_seconds':st['total_diagnostic_CPU_seconds'],'conditional':True,'k_min':1,'singlehelper_impossible_when':'delta+k<R^2','balanced_R':65,'balanced_pin_bound':4225,'balanced_max_k_excluded':4143,'Payne_R':64,'Payne_pin_bound':4096,'Payne_max_k_excluded':4015,'all_pin_sets_not_only_fullN':True,'pin_union':'H minus D','freepins':'D union existingclones','freepin_service_classes_max':1,'offdiagonal_D_tests':[270400,258048],'distinct_D_pair_tests':[2080,2016],'selected_route_counterexamples':0,'source_D3_instantiated':False,'not_excluded':['jointhelperbatches','oldedgechanges','differentcode','highercap','arbitrarilylargek'],'all_processes_terminal':True},
    evidence_paths=[Q+x for x in ['SATURATION_BARRIER_PRED.md','SATURATION_BARRIER_NOTE.md','SATURATION_BARRIER_RESULT.md','SATURATION_BARRIER_RESULT.json','SATURATION_BARRIER_TERMINAL.json','SATURATION_SELECTED_GEOMETRY_MATRICES.json','SATURATION_BALANCED_Q8_OFFDIAGONAL_TO_D.csv','SATURATION_PAYNE_Q8_OFFDIAGONAL_TO_D.csv','saturation_barrier_diagnostic.py','MECHANISM_NOTE.md']])

family=copy.deepcopy(old[FID]['source_record']);m=family['other_metrics']
family['title']='同一P33规则十五完整图／具体Lean-Audit及两scope A/B完成；distinctfresh15最终C445在途'
family['outcome_class']='FIFTEEN_LITERAL_AND_CONCRETE_LEAN_AUDIT_PASS_LOWER_UPPER_EXPLICIT_A_B_PASS_DISTINCT_FRESH_JOINT15_C445_IN_FLIGHT'
family['unclosed_gap']='十五图数学合法、fresh独验、十五无前提具体Lean/Audit/std3及lower8/upper7各自A/B均实际PASS。upper7 A438/B440是沿原A/B thread各一次明确追加scope，不继承下八PASS；B两处措辞已处置：Lean4.24.0下三个标准axioms，标准q7 Payne有343points/partialO upper42。唯一distinctfresh最终C15 cell445已发在途、storep33_15_C_review；非旧six-target C、非15calls，未冒完成。源fill优先权审查UNKNOWN，关键JGT1985正文缺口；若公开filled160050及接口已发表，十五图+50变0。当前公开数字不改，全球／首创未认证。专家15文档DRAFT，ZIP尚未生成，旧冻结包不变。'
family['lesson_and_restart_condition']='P33十五图和lower/upper各A/B已实际完成，当前只收一次distinctfresh15原目标最终C445；不重跑图/field/Lean或加外审。q8小几何范数/Payne接口现freshPASS，但其fullsource未产；新条件R²单helper障碍让未来fullO饱和后的逐点续造应在小cap范围停止。源fill同规则优先权给专家精确JGT正文问题，不把未命中当全球纪录；不自动新参数梯子。'
for instance in m['validated_graph_instances']:
    upper_instance=instance['copy_count']>=9
    instance.update(external_A='ACTUAL_PASS_EXPLICIT_UPPER7_ENCODING_SCOPE' if upper_instance else 'ACTUAL_ENCODING_CHECKPOINT_PASS_NOT_FINAL_KERNEL_VERDICT',
        external_B='ACTUAL_PASS_EACH_UPPER7_ORIGINAL_TARGET' if upper_instance else 'ACTUAL_PASS_EACH_LOWER8_ORIGINAL_TARGET',
        external_distinctfreshC='IN_FLIGHT_ONE_DISTINCTFRESH_JOINT15_ORIGINAL_SCOPE_CELL445_PENDING',
        external_final_C_cell='445',external_final_C_calls_shared=1,external_final_C_actual_complete=False)
m.update(lower8_review_scope={'A':'ACTUAL_ENCODING_CHECKPOINT_PASS','A_cell':'423','B':'ACTUAL_EACH_ORIGINAL_TARGET_PASS','B_cell':'428'},
    upper7_review_scope={'A':'ACTUAL_EXPLICIT_ADDITIONAL7_ENCODING_PASS','A_cell':'438','B':'ACTUAL_EXPLICIT_EACH_UPPER7_ORIGINAL_TARGET_PASS','B_cell':'440','lower8_PASS_inherited':False},
    external_review_A='ACTUAL_PASS_LOWER8_AND_EXPLICIT_UPPER7_SCOPES_TWO_CALLS',external_review_B='ACTUAL_PASS_LOWER8_AND_EXPLICIT_UPPER7_ORIGINAL_SCOPES_TWO_CALLS',
    external_review_distinctfreshC='IN_FLIGHT_ONE_DISTINCT_FRESH_NEWTHREAD_JOINT15_ORIGINAL_C445',external_final_fresh_C_scope='One distinctfresh call445,15 explicit original verdicts requested, pending; not15calls/notoldsixC',
    external_final_C_cell='445',external_final_C_store_key='p33_15_C_review',external_final_C_calls=1,external_final_C_actual_complete=False,
    external_all_A_B_actual_scopes_pass=True,external_all_A_B_freshC_complete=False,
    upper_B_disposition_corrections=['Lean4.24.0 with THREE standardaxioms, notLean3 language','standardPayneW3F7 has343derivedpoints andpartialovoidupper42, not42points'],
    source_fill_priority_status='UNKNOWN_EXACT_SAME_FILL_RECIPE_ORIGINAL_JGT1985_BODY_NOT_OBTAINED',source_fill_priority_report=P+'SPREAD_FILL_SOURCE_PRIORITY_20261101.md',
    current_scoped_public_margin=50,conditional_margin_if_exactfilledsource_publicly_confirmed=0,
    expert15_delivery_status='DRAFT_NO_ZIP_GENERATED',q8_geometry_status='SMALLGEOMETRY_ACTUAL_PASS_NO_COMPLETE_SOURCEGRAPH',q8_saturation_status='CONDITIONAL_SINGLEHELPER_BOUND_NOT_GRAPH')
family['evidence_paths']=list(dict.fromkeys(family['evidence_paths']+[R+'P33_SEVEN_UPPER_TARGETS_'+x for x in ['A_GEMINI_RAW.json','A_DISPOSITION.md','B_GEMINI_RAW.json','B_DISPOSITION.md']]+[P+'SPREAD_FILL_SOURCE_PRIORITY_20261101.md',P+'SPREAD_FILL_SOURCE_PRIORITY_20261101.json']))
rows=[g,t,family]
for row in rows:assert all((ROOT/p).exists() for p in row['evidence_paths']),row['id']
raw=W/'updates'/f'{STEM}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
cmd=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(raw)]
x=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True);assert x.returncode==0,(x.stdout,x.stderr)
sync=json.loads(x.stdout);now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
intro=f'''<!-- {STEM} -->
# 当前：十五图A/B实际齐，fresh最终C445在途；q8几何PASS及条件单helper障碍已保存

同Goal ACTIVE：140合法图／33参数、stage36／30、具体Lean34，ledger418；known43/overlap40/main103_3/outsidepending34_29/global0不变。本轮0完整图／Lean／framework新增。

[P33十五图](experiments/{FID}.md)lower8 A423/B428和upper7追加A438/B440现均actualPASS，各scope分别审原目标，不继承。唯一distinctfresh最终C15 cell445在途/storep33_15_C_review，未完成、非旧六C、非15calls。专家15仍DRAFT、ZIP未产，旧包不动。[fill优先权审查](../{P}SPREAD_FILL_SOURCE_PRIORITY_20261101.md)仍UNKNOWN/JGT正文缺口；若公开filled160050同规则确证，十五+50归0，当前数字未改。

[q8几何](experiments/{GID}.md)2.285789CPU全PASS：真F8/F64、585/585全9度/O65+spread65、Payne512/640线8点10度/O64+spread64，全部336960+322560投影。仅已知几何复现，0完整源图/BFS/Lean。

[条件饱和障碍](experiments/{TID}.md)：fullO×spread复制后pinunion=H减D，freeD/clone各仅服务自身类；任意单helper需R²pins=4225/4096，固定capδ+k<R²时停止逐单点，不只fullN。0.145388CPU；源D3未实例化，jointbatch/改边/不同code/高cap未排。以下保留历史。

'''
gap=W/'gap_map.md';oldtext=gap.read_text()
if not oldtext.startswith(f'<!-- {STEM} -->'):gap.write_text(intro+oldtext)
h=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
if f'<!-- {STEM} -->' not in h.read_text():
    with h.open('a') as f:f.write(f'''\n\n<!-- {STEM} -->
## 2026-11-01 q8机制检验、条件饱和障碍与十五图外审恢复

本段只记录新的实际研究证据与状态，不新Goal/Wiki。140合法/33参数、stage36/30、Lean34、known43/overlap40/main103_3/pending34_29/global0不变。两新节点是[小几何](experiments/{GID}.md)和[条件局部理论](experiments/{TID}.md)，0完整图/Lean/framework。

q8事前问的是具体域坐标/原isotropic覆盖能否同时兼容派生新H线，而非抽象ovoids是否存在。实际F8用x³+x+1、F64用z²+z+1，范数N=a²+ab+b²，各向异性及B(Xu,Xv)=N(u+v)支持O65；F64 slope加infinity给spread65。新H(a,b)交点t=N(a+bz)保证同一O64覆盖派生新增64线，也保576旧线。全部新field-law及原336960/派生322560非incident投影实际PASS，2.285789276CPU，585PG点/585线全9度，Payne512点/640线（8点每线/10线每点），P实际pointid2，0fullsourcegraphs/BFS/Lean。这是已知几何/大小复现，不新纪录，后续应直接读其表而不重做field或再搜O/spread。

条件饱和预测原仅R(R−1) off-diagonal类，实际owner/pinunion分类加强为R²。fullO×spread所有R² baseN并集=filledsource H减diagonal D；k≥1复制后H减D饱和，freeD及已有clone每个只能在两步内服务自身clonebaseclass，故任意单helper需至少R²pins。balanced4225、Payne4096；固定capδ+k<R²时逐单点扩张严格不行，范围超出fullN模型。诊断0.145388401CPU，balanced270400/Payne258048 offdiag×D路线全0，额外Dpair2080/2016亦0，无field/大graph/BFS/Lean重跑。source D3实例尚未生成，完整D3结论仍条件；大cap可tight，jointbatch/改边/不同code/提高cap未排。下一步不再盯“剩R个自由旧点”调单helper。

P33 lower8 A/B和upper7 A438/B440均actualPASS，raw/处置已保存。upperB两处文字已纠正为Lean4.24.0下三个标准axioms，以及q7派生343points、partialO upper42。上七是各线程明确追加一次scope，下八PASS没有被继承。唯一distinctfresh15原目标finalC cell445现已发在途（storep33_15_C_review），不当旧sixC/15calls或已完成。

专家必须注意[fill同规则优先权UNKNOWN](../{P}SPREAD_FILL_SOURCE_PRIORITY_20261101.md)：已读一般lemma/spread不自动等于相同fill pins/覆盖，关键原JGT1985正文仍未取得；若公开filled160050及接口确证，十五图当前+50将归0。未命中不是新纪录证，当前公开数字未改。专家15文档保持DRAFT、ZIP尚未生成，旧冻结包不改。root接续计算决定，不在此派源图、外审或新查询。
''')
helper=ROOT/'aris_repo/tools/research_wiki.py';calls=[]
def call(*args):
    c=[sys.executable,str(helper),*args];r=subprocess.run(c,cwd=ROOT,text=True,capture_output=True)
    calls.append(dict(command=c,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr));assert r.returncode==0,calls[-1]
for a,b,k,e in [(GID,FID,'extends','Knownq8smallgeometryreproductioninheritedprototypeidea; no completegraph ornewrecord.'),(TID,GID,'uses','ActualfullO/spread/ownerconditions support conditionalR2singlehelperbarrier; sourceD3notinstantiated.'),(TID,FID,'extends','StrengthensfullN-only obstruction to anyfreepin singlehelper in fixedfullO×spreadcopies; notjointbatch/highcap/generalgraph.')]:
    call('add_edge',str(W),'--from','exp:'+a,'--to','exp:'+b,'--type',k,'--evidence',e)
call('log',str(W),'2026-11-01 q8freshsmallfieldsandtwoGQgeometriesPASS2.285789276CPU/0sourcegraphs; conditionalfullOspreadsinglehelperbarrierR²4225/4096fixedcap0.145388401CPU,noD3sourceinstantiated. Two localnodesaddedledger418,no graph/Lean/frameworkcountincrease140/33stage36_30Lean34. ExistingP33lower8+upper7explicitA/BactualPASS,freshjoint15C445inflightnotcomplete,priorityfillauditUNKNOWNJGTbodygapconditional+50to0,expert15DRAFTnoZIP/frozenpackuntouched.')
call('rebuild_index',str(W));call('rebuild_query_pack',str(W))
cp=W/'updates'/f'{STEM}_HELPER_CALLS.json';cp.write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
current=read('research-wiki/DDP_METHOD_LEDGER.json');expected={'record_count':418,'validated_named_graph_examples':140,'validated_named_parameter_pairs':33,'complete_Lean_graph_instances':34,'known_publicly_dominated_graph_examples':43,'known_publicly_dominated_also_saved_table_improvement_examples':40,'pending_outside_saved_table_graph_examples':34,'pending_outside_saved_table_parameter_pairs':29}
for k,v in expected.items():assert current[k]==v,(k,current[k],v)
checked=0
for p in [W/'experiments'/f'{r["id"]}.md' for r in rows]:
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        target=unquote(target.strip('<>').split('#',1)[0])
        if not target or re.match(r'\w+://',target):continue
        assert (p.parent/target).exists(),target;checked+=1
q=(W/'query_pack.md').read_text();assert 'ledger418' in q and 'C445' in q and 'UNKNOWN' in q
paths=set(p for r in rows for p in r['evidence_paths'])
receipt=dict(updated_UTC=now,status='PASS_Q8_LOCAL_GEOMETRY_CONDITIONAL_BARRIER_P33_AB_PASS_C445_PENDING_SYNC',ledger_records=418,records_added=2,records_updated=1,new_graphs=0,new_Lean_instances=0,new_frameworks=0,named_legal_graphs=140,legal_parameter_pairs=33,stage_graphs=36,stage_pairs=30,complete_formula_Lean=34,known_publicly_dominated=43,saved_table_dominated_overlap=40,pending_outside_saved_table_graphs=34,pending_outside_saved_table_pairs=29,certified_global_records=0,q8_geometry_CPU_seconds=2.285789276,q8_full_source_graphs=0,conditional_saturation_CPU_seconds=0.145388401,conditional_pin_bounds=[4225,4096],conditional_source_D3_instantiated=False,P33_lower_upper_A_B='ALL_ACTUAL_PASS_EXPLICIT_SCOPE',P33_finalC='ONE_DISTINCTFRESH_JOINT15_CELL445_IN_FLIGHT_NOT_COMPLETE',source_fill_priority='UNKNOWN_EXACT_RECIPE_AND_JGT_BODY_GAP',conditional_gain_if_sourcefill_publicly_confirmed=0,expert15='DRAFT_NO_ZIP',canonical_upsert_command=cmd,canonical_upsert_stdout=sync,actual_helper_calls=str(cp.relative_to(ROOT)),resolved_evidence_paths=len(paths),checked_local_links=checked,query_current=True,experiments_rerun=0,root_owned_files_modified=False,frozen_expert_packets_modified=False)
rp=W/'updates'/f'{STEM}_RECEIPT.json';rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
