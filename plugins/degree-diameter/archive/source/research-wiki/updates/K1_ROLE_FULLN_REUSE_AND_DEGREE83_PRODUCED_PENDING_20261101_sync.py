from pathlib import Path
from datetime import datetime,timezone
import copy,json,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
B='K1_ROLE_FULLN_REUSE_AND_DEGREE83_PRODUCED_PENDING_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
I=S+'retained_edge_transfer/diagonal_fill_general_review/';G=S+'retained_edge_transfer/DIAGONAL_FILL_REALLOCATION_GENERAL_NOTE.md'
D=S+'retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/multiplicity2_degree83/'
P=S+'public_baseline_audit/DEGREE83_DIAGONAL_REALLOCATION_K2_TARGET_GATE_20261101'
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,145,36,37)
rid='ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101'
r=copy.deepcopy(next(x for x in L['rows']if x['id']==rid)['source_record']);m=r['other_metrics']
z=json.loads((R/D/'RESULT.json').read_text());t=json.loads((R/D/'TERMINAL.json').read_text());assert z['status']=='PRODUCER_PASS_PENDING_FRESH_ACCEPTANCE';assert z['n']==350742 and z['m']==14547195 and t['CPU_seconds']==3.493080617
reuse=json.loads((R/I/'RESULT.json').read_text())['k1_full_neighborhood_reuse_clarification'];assert reuse['status']=='SUPPORTED_EXACT_IDENTIFICATION_NO_GAP'
m['diagonal_fill_general_paper_review']['k1_role_fullN_reuse']=reuse
m['degree83_multiplicity2_single_target']=dict(status='COMPLETE_PRODUCER_TERMINAL_FRESH_INDEPENDENT_IN_PROGRESS_NOT_ACCEPTED',n=350742,m=14547195,Delta=83,D='predicted3_pendingfresh',
    source_n=346516,source_m=14204970,source_all_edges_retained=True,extra_vertices=4226,new_edges=342225,producer_CPU_seconds=3.493080617,producer_CPU_budget=30,
    producer_full_copy_bindings=4225,producer_BFS=0,producer_degree_histogram=z['degree_histogram'],copied_centers='first4225clonesandfirsthubofG1;notoldGQcenters',
    new_clone_label='346516+h',new_hub_label=350741,independent_status='ACTUAL_ROOT_DISPATCHED_IN_PROGRESS',independent_CPU_budget=40,planned_BFS_roots=68,
    independent_BFS_scope='65second-diag+2preselectedsecond-off+secondhub;notall4226',
    best_located_public_lower_bound=350675,bounded_candidate_gain=67,public_gate='PASS_WITHIN_SCOPED_PRIMARY_FORMULAS_NOT_GLOBAL_CERTIFICATE',public_gate_CPU=.034119546,
    public_priority='UNKNOWN',if_filled_H_and_standard_copy_public_gain=2,if_same_reallocation_public_gain=0,
    mathematically_validated_complete_graph=False,accepted_instances=0,complete_Lean_graph_instance=False,in_600CPU_k1_two_target_Lean_scope=False,in_A559_scope=False,
    external_A_B_freshC='NOT_DONE_NOT_INHERITED',no84plus_ladder=True,
    evidence=[D+'PREDICTION_AND_SCOPE.md',D+'RESULT.json',D+'TERMINAL.json',P+'.md'])
r['lesson_and_restart_condition']+=' 纸面简化已核：G1独立role集J=首批clones+hub，完整N分别为NU(c)及F、彼此不交且全在H；为J每点复制k−1次即Gk，应用既有FullNeighborhoodClones，以firstclone/hub为center而非oldGQcenter。源δ+1/loadk−1得δ+k，collapse目标是G1，不是H；label固定原源，q8k2新clone346516+h/hub350741。唯一degree83目标350742/14547195已生产3.493080617CPU，fresh40CPU/68roots在验未接受、不计146；不属k1两目标600CPU或A559scope。'
e=[G,I+'NOTE.md',I+'RESULT.json',I+'TERMINAL.json','formal/DegreeDiameter/Portfolio/FullNeighborhoodClones.lean',P+'.md',P+'.json',P+'.py']+[D+x for x in ['PREDICTION_AND_SCOPE.md','PARAMETERS.json','RESULT.json','TERMINAL.json','produce_once.py','produce_once.cpp','graph_d83_D3_n350742.edges','independent_acceptance/PRED.md','independent_acceptance/HANDLE.json','independent_acceptance/PRESELECTED_BFS_ROOTS.json']]
assert all((R/x).is_file()for x in e);r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+e))
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps([r],ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,145,36,37)
block=f'''<!-- {B} -->
# 当前：G1-role完整邻域复制接口获纸面支持；唯一83度图已生产待独验

同Goal ACTIVE，ledger420复用q8现节点/0新行；145／36／Lean37、stage41／33不变，旧冻结包不动。新简化不是新增理论计数：[q8节点](experiments/{rid}.md)中的G1首clone+hub独立role集，完整N为NU(c)/F且不交，复制这些first-role完整源邻域恰得Gk。source冻结、δ+1加loadk−1、保持源标签及G1collapse/nonD2均由纸面与既有generic源码接口支持，非新kernelPASS。

唯一degree83k2公开门bestlocated350675，条件目标350742多67、priorityUNKNOWN。物理350742/14547195图已生产3.493080617CPU/保全部346516源边，fresh≤40CPU/68预选新根在验；尚未root数学接受，0新计图/Lean、不计146。其83scope未含于k1两原目标600CPU或唯一A559（仍在途），不继承旧review，不派84+。以下保留历史。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} G1角色复制简化独立支持；degree83唯一物理候选在验不计图

本次[现q8节点](experiments/{rid}.md)只补有限接口与实际producer状态，ledger420/0新行，145合法／36参数／Lean37、stage41／33不变。独立generalreview原NOTE新增clarification，未新开理论成果行：J=G1首批pR clones+hub独立、全部source完整N分别为NU(c)与F且互不交，全pins在H。Gk等于以G1中firstclone/hub为center复制k−1份；固定这些源N，旧J load0/H load≤k−1，source degree≤δ+1，旧generic degree_le给δ+k。新copy的collapseHom目标是G1（有真实hub角色），不是错误地把hubcollapse回H；G1的D3/nonD2和无孤立一旦kernel闭合，旧generic可直接复用。只读graph/degree/D3/nonD2定义，0编译。

q8k2保持原G1全部label，center342290+h及346515分别对应newlabel346516+h及350741，实际producer完整350742/14547195、保14204970源边、加342225边，degree65:2/80:130/81:8385/83:342225，3.493080617CPU/30终态，producer0BFS。fresh独验≤40CPU、65second-diag+2预选second-off+secondhub共68根在途，0数学接受/0新图实例，未计146。该target独立于k1二目标600CPU与A559，不能继承PASS；A559仍在途。

实际83公门仅一个≤3primaryquerybatch/标量.034119546CPU，已核保证350675、候选多67；若publicfilledH+标准复制已发表仅剩2优势，若同reallocation已发表则归0。有限未命中不作全球或原创证据。新判据推动直接用first-role fullN框架，未启动84+/旧field/projection/solver/Lean。根STATE/REPORT/progress/恢复与旧冻结包未改。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'PaperclarificationGk=FullNeighborhoodClonesonG1firstclone_hubroles;frozenNU_Fpins/disjoint/oldJload0/Hloadkminus1/sourcebounddelta+1/labelskept/collapseG1notH;nonewtheoremcount. Degree83onlyproduceractual350742/14547195/all14204970sourceedgeskept/3.493080617CPU;fresh40CPU68rootinprogressNOTaccepted/no146/notk1Lean600CPUorA559scope.Publicbestlocated350675candidateplus67/priorityUNKNOWN. Ledger420oneexistingq8row145_36Lean37stage41_33unchanged/0newmathruns/rootedits/frozenpackchanges.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_K1_ROLE_FULLN_REUSE_PAPER_CLARIFICATION_AND_D83_PRODUCER_PENDING_WIKI_SYNC',updated_UTC=now,ledger_records=420,records_added=0,records_updated=1,named_legal_graphs=145,legal_parameter_pairs=36,stage_graphs=41,stage_pairs=33,complete_formula_Lean=37,new_graphs_counted=0,new_Lean=0,new_theorems_counted=0,new_frameworks=0,
    fullN_reuse_paper='SUPPORTED_SOURCEG1_FIRSTCLONE_HUB_CENTERS',degree83_status='PRODUCED_FRESH_IN_PROGRESS_NOT_ACCEPTED',producer_CPU=3.493080617,independent_CPU_budget=40,planned_BFS_roots=68,in_k1_600CPU_or_A559_scope=False,new_evidence_paths_checked=len(e),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_q8_packet_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
