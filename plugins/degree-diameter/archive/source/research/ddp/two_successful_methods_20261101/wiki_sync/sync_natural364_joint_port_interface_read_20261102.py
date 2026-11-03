"""Existing natural364 sample node: read-only joint interface followup, no new row."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
ROOT=Path(__file__).resolve().parents[4];W=ROOT/'research-wiki';S=Path(__file__).resolve().parent
D=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/port_matching_core2_star365'
st=time.process_time();now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
slug='ddp-stale-d4d5-natural364-port-matching-two-core-cuts-star365-sample-20261101';marker='<!-- NATURAL364_JOINT_PORT_INTERFACE_READ_20261102 -->'
ledger=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert ledger['record_count']==len(ledger['rows'])==455
pos=next(i for i,r in enumerate(ledger['rows']) if r['id']==slug);old=copy.deepcopy(ledger['rows'][pos]);raw=copy.deepcopy(old['source_record']);others={r['id']:copy.deepcopy(r) for r in ledger['rows'] if r['id']!=slug};counts={k:v for k,v in ledger.items() if k not in {'rows','record_count','updated_UTC','input_counts'}}
read=json.loads((D/'JOINT_PORT_INTERFACE_READ.json').read_text());assert read['new_numeric_runs']==0 and read['conservative_read_preparation_CPU_charge']==.3
assert read['frozen_first_config']['P']==[43,58,151,314] and read['actual_previous_sample']['distinct_complete_configs']==10000
assert raw['outcome_class']=='UNKNOWN_10000_SAMPLE_NO_HIT' and raw['other_metrics']['cumulative_charged_CPU_seconds']==1.537876879
assert 'joint_port_interface_read_20261102' not in raw['other_metrics']
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
files=['index.md','query_pack.md','gap_map.md'];original={p:(W/p).read_text() for p in files};end='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';human={p:t[:t.index(end)+len(end)] for p,t in original.items()}
raw['scope']+=' 2026-11-02 followupisread/paperinterfaceonly:freezefirstcuts(43,58)/(151,314),P={43,58,151,314};jointdesignofall28portmatesbyexactnewrootcoveragecriterion. No new balls/matching/solver/samples orfamilyverdict;original10000sampleUNKNOWNandCPUretained.'
raw['distance_text']+=' 新只读接口：28port的R2类分割364且不同port距5，cut端点同在P给dT(P,t)=dG(P,t)。z≤5路线最多一条matching；sourceR4(P)外hole t的唯一owner b、beta<=2，精确要求dG(P,mate(b))+beta<=3。无向允许边必须同时a∈L_b、b∈L_a，其perfectmatching iff新根R5，仍不保证oldoldD5。固定P存在jointM仅预测未测。缓存给target0 owner=port2，beta仅知{1,2}未查；mate256不合格是旧反例+lemma的推论，非新距离数据。最小新数据四coreR4，余阈值复用port缓存，当前0新数值。'
raw['lesson_and_restart_condition']+=' Readfollowupchangesproposeddesignfromindependentshuffleofcuts/matchingtofixedfirstP+jointmutualallowed-mateobligations. Do notrepairjusttarget0andrandomizetherest. Perfectmatchingcriterioncoversnewrootonly;oldoldD5stillrequiresfutureactualcandidatevalidation. Thisisreadscope/papernotnumericalprogress.'
raw['restart_condition']+=' Onlyaseparatelyselectedandbudgetedfixed-firstPfour-coreR4/allowedgraphtestcouldtestthisprediction; currentreadSTOPdoesnotresumeold10000seed,allcutpairsearchoroldsolver.'
raw['unclosed_gap']+=' FixedfirstP joint-perfectmatchingexistenceisUNTESTED. FourcoreR4supports/holeclassesandbeta-labelthresholdlookupsnotexecutedhere. IndividualdG(P,256)orbeta(2,0)notmeasured;mate256violationisinferredfromsavedroot6counterexampleandexactcriterion. NewrootR5successwouldnotproveoldoldD5/full365.'
raw.setdefault('positive_guarantees',[]).extend([
'CutendpointsallinP implydT(P,t)=dG(P,t) byrestartingatanydownstreamcutendpoint; no new source distance query.',
'28cachedportR2classespartition364,portsmutualdistance5; anysimplez-rootpath<=5usesatmostonematchingedge. Aholeownertailbeta<=2avoidscuts,soexactmateinequalityusesoriginalsource distances.',
'Allowededge{a,b}requiresbothdirectedobligationsa∈L_b,b∈L_a. AnallowedperfectmatchingiffnewrootR5,notoldoldD5.',
'Owner0=port2comesfromcache;beta(2,0)∈{1,2}only,notlookedup. Currentmate256thresholdviolationanddG(P,0)=5arelogicalconsequencesofsavedroute/lemma,notfreshBFSresults.'
])
raw['other_metrics']['joint_port_interface_read_20261102']={
'status':read['status'],'read_CPU_charge':.3,'read_CPU_cap':1,'original_sample_CPU_unchanged':1.537876879,'original_sample_cap_unchanged':20,
'frozen_cuts':[[43,58],[151,314]],'P':[43,58,151,314],'newroot':364,'natural_source':[364,714],'ports':28,'core':336,'not_public_regular364_728':True,
'cached_R2_port_classes_partition_all364':True,'cached_distinct_port_distance':5,'distance_invariance':'dT(P,t)=dG(P,t)','z_path_max_matching_edges':1,
'exact_hole_condition':'dG(P,mate(owner(t)))+beta_owner(t)(t)<=3','beta_general_bound':'<=2','allowed_directed_mates':'L_b=allotherports if noholes in classb; else dG(P,a)<=3-maxholebeta','allowed_undirected_mates':'a in L_b AND b in L_a','allowedgraph_perfectmatching_iff_newroot_R5':True,'oldold_D5_not_guaranteed':True,
'saved_target0_owner':2,'target0_beta_values_not_queried':[1,2],'saved_mate_of_2':256,'mate256_violation_basis':'INFERRED_FROM_SAVED_BAD_ROUTE_AND_EXACT_LEMMA_NOT_NEW_NUMERIC','dG_P_to0_5_basis':'OLD_SAVED_ROOT6_AND_5EDGE_OLDTAIL_PLUS_INVARIANCE_NOT_NEW_BFS',
'prediction':'fixedfirstP admitsanotherjointportperfectmatchinggivingnewrootR5','prediction_verdict':'UNTESTED','minimum_new_data':'fourcoreclosedR4supports','reuse_other_thresholds':'cachedportR1/R2classes/R3bits; no28ballrecompute','new_BFS_ball_distance_queries':0,'matching_solver_new_samples_graph_runs':0,'allcutpair_seed_continuation':False,'read_terminal':True,'new_graph_parameter_Lean_method':[0,0,0,0]}
newpaths=[str((D/p).relative_to(ROOT)) for p in ['JOINT_PORT_INTERFACE_READ.md','JOINT_PORT_INTERFACE_READ.json','PAPER_SCOPE_REVIEW.md']]
raw['evidence_paths']=list(dict.fromkeys(raw['evidence_paths']+newpaths));assert all((ROOT/p).exists() for p in raw['evidence_paths'])
row=common['normalize'](raw);row['goal']['baseline_date']=raw['baseline_date'];assert row['status']==old['status'] and row['source_record']['outcome_class']==old['source_record']['outcome_class'];assert not common['capture'].screen(json.dumps(raw,ensure_ascii=False))
rowfile=S/'NATURAL364_JOINT_PORT_INTERFACE_READ_20261102_ROW.json';rowfile.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
helper=common['helper'];helper.rebuild_index=lambda *_a,**_kw:None;helper.rebuild_query_pack=lambda *_a,**_kw:None
with (S/'NATURAL364_JOINT_PORT_INTERFACE_READ_20261102_NODE_CALLS.log').open('w') as out,contextlib.redirect_stdout(out):common['write_node'](row)
ledger['rows'][pos]=row;ledger['updated_UTC']=now;ledger['input_counts'][str(rowfile.relative_to(ROOT))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n');node='experiments/'+slug+'.md'
summary=f'''\n\n{marker}
### {now} 原natural364样本节点只读追加：固定首P的联合port接口未测

保原10000样本UNKNOWN及1.537876879/20CPU历史；不续seed/allcutpairs。新接口冻结cuts(43,58)/(151,314)、P四端点。cached28port R2类分割364/port间距5，cutset端点不变式保dT(P,t)=dG(P,t)，z≤5至多一matching。R4(P)外hole由唯一owner b承担，精确要求dG(P,mate(b))+beta<=3；无向允许边要双向同时满足。允许图perfectmatching iff新根R5，不保证oldoldD5。

固定首P存在jointM只是未测预测。target0 owner=port2来自cache，beta仅知1或2未查；savedmate256违反是旧root6路径＋lemma推论，非新数值。最小需四coreR4新数据，其余阈值复用port缓存，本轮0新BFS/球/距离/matching/solver/样本，read.3/1另记不改原sample费用。

仅原canonical节点原位追加，455→455/add0，0新图/参数/Lean/方法，153/43/47保持；人工15格top与其他454rows原样。当前readSTOP，GoalACTIVE/旧N8n61暂停。

[原样本与新只读接口]({node})

'''
for name in files:
 text=original[name];assert marker not in text;cut=len(human[name]);(W/name).write_text(text[:cut]+summary+text[cut:]);assert (W/name).read_text().startswith(human[name])
md=(W/'DDP_METHOD_LEDGER.md').read_text();assert marker not in md
md+=f'''\n\n{marker}
## {now} 原natural364→365样本：新增联合mate纸面接口，不增加实验记录

[原canonical样本]({node})原10000UNKNOWN/CPU1.537876879/20保持。固定首P={43,58,151,314}的jointmatching预测未测；newrootR5 iff28port允许图perfectmatching，allowededge需a∈L_b且b∈L_a，hole精确阈值dG(P,mate(owner))+beta<=3，oldoldD5另验。owner(0)=port2及R2partition来自缓存；beta1/2未查，mate256违反/旧dG(P,0)=5仅逻辑推论，不冒新BFS。四coreR4是下一最小新数据，当前不计算、不续seed。

[JOINT接口与proof](../{newpaths[0]})；read.3/1单独记录，455→455/add0、0新图/参数/Lean/方法；其他454rows与人工top保持，GoalACTIVE/旧N8n61暂停。
'''
(W/'DDP_METHOD_LEDGER.md').write_text(md)
after=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert after['record_count']==len(after['rows'])==455;assert all(after[k]==v for k,v in counts.items());assert all(r==others[r['id']] for r in after['rows'] if r['id']!=slug)
updated=after['rows'][pos];assert updated['status']==old['status'] and updated['other_metrics']['cumulative_charged_CPU_seconds']==1.537876879
for k,v in old['other_metrics'].items():assert updated['other_metrics'][k]==v
assert re.search(r'^## Experiments \((\d+)\)',(W/'index.md').read_text(),re.M).group(1)=='542'
receipt={'status':'PASS_EXISTING_NATURAL364_SAMPLE_JOINT_PORT_READ_INTERFACE_UPSERT','updated_UTC':now,'records_before':455,'records_after':455,'records_added':0,'updated_id':slug,'canonical_node':str((W/node).relative_to(ROOT)),'row_path':str(rowfile.relative_to(ROOT)),'old_sample_UNKNOWN_preserved':True,'old_10000sample_metrics_CPU_preserved_exact':True,'original_sample_CPU':1.537876879,'original_sample_cap':20,'new_read_charge':.3,'new_read_cap':1,'fixedP_jointmatching_prediction':'UNTESTED','allowedmatching_iff_newroot_R5_only':True,'oldold_D5_not_guaranteed':True,'owner0_port2_from_cache':True,'beta1or2_not_queried':True,'mate256_violation_logical_not_new_numeric':True,'new_BFS_distance_ball_matching_solver_sample_runs':0,'graph_parameter_Lean_method_increments':[0,0,0,0],'other454rows_preserved_exact':True,'human_top_blocks_preserved_exact':{p:True for p in files},'index_experiments_count_unchanged':542,'counts_unchanged':{k:after[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs']},'full_rebuild_reimport':False,'root_STATE_pages_recovery_modified':False,'sameGoal':'ACTIVE','old_N8_n61':'PAUSED','sync_CPU_seconds':time.process_time()-st,'stop':True}
(S/'NATURAL364_JOINT_PORT_INTERFACE_READ_20261102_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
