from pathlib import Path
from datetime import datetime,timezone
import json,re,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';B='Q8_THREE_ACCEPTED143_36_AND_EXACT_LINE_INTERFACE_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
rows=json.loads((W/f'updates/{B}_ROWS.json').read_text());ids=[r['id'] for r in rows];l=json.loads((W/'DDP_METHOD_LEDGER.json').read_text())
assert (l['record_count'],l['validated_named_graph_examples'],l['validated_named_parameter_pairs'],l['complete_Lean_graph_instances'])==(420,143,36,34)
block=f'''<!-- {B} -->
# 当前：q8第三图82度346515已验，143／36／Lean34；B局部iff给生成规则

同Goal ACTIVE，ledger420(本轮4existingrows复用/0新增行)。143合法／36参数、stage39／33、具体Lean34；known43/main103_3/outside37_32/global0。没有把832或局部line witness计图。

[q8三终图](experiments/{ids[0]}.md)：80/327744、81/342290、82/346515均数学接受。新82保81源13862745边，4225immutableN81实际不交，4225新根freshBFS两类全部命中，old-only/prefix/collapse proof齐，独验12.395600852CPU，公开346450多65。三新Lean仍0；源fullproof在跑，82四module codeonly/300CPU待parent。sourceA2实际PASS/A82cell494在途/B/C未发，专家三图仅DRAFT准备，0ZIP。

[A饱和局部门](experiments/{ids[1]}.md)现在balanced onecopy前提已有实际82图，但只排其固定oldadjacency/cap82追加任意helperbatch，不是N82上界；k2/offdiagholes/改边仍未排。

[B同节点](experiments/{ids[2]}.md)：fixedW/ret4全19池≥811单次MIP数值INFEASIBLE，非formal UNSAT；837分数sanity却可行。新count832也被projection拒。两独立方向iff ceil(A/q)+ceil(B/q)≤q(含0)；三正族iff存在a,b,c三矩形不等式。50/31不可、27/54实际分区；12/50/3实际65lines。以后先选支持/slabs，再同S_i全6dart运输兼容；不续旧timer或只调counts。

public gains64/65/65仅对已核保证；exactfill/JGTpriorityUNKNOWN，若同fill已公开可归0。旧十五图冻结包不含q8且不改。以下保留历史。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
comment=f'''\n\n## {NOW} 同一q8节点接受第三图；B同一local节点补精确构造接口

本次canonical upsert真实复用4节点，ledger420无新增方法行，数学143合法／36参数、stage39／33、具体Lean34；known43/main103_3/outside37_32/global0。root-owned状态/报告/HTML/恢复由root管理，本次没有重跑数学。

[q8同机制记录](experiments/{ids[0]}.md)增加唯一82完整实例346515/14204970。原source是balanced81/342290/13862745，不是Payne或current克隆图；4225中心immutableN81逐项绑定，342225pins两两不交且source减D65，degree81:4290/82:342225，0newnew/全部旧body保留。fresh所有4225新根逐项65×(1,81,5249,341184)+4160×(1,81,5329,341104)，sourceR2只是事前公式、0旧根/旧R2枚举；独立old-only全点对/prefix证明及clone→center同态保nonD2，独验12.395600852CPU。已核public346450优势65，priorityUNKNOWN，不冒world record。

源80/81的具体Lean原目标仍未闭合，1104module队列实际在途，Derived327680projection及4个hline/howner全域已PASS；不按partial模块计图Lean。82四module只codeprepared，300CPU授权待parent/实际编译门；没有预记Exact/Audit完成。source2共享A编码PASS，A82cell494在途，B/C尚未发。新专家Q8_THREE_RESULTS_20261101只准备DRAFT HTML/源码/Word/SOURCES/复现计划，0ZIP/冻结直到root另授权且freshC实际齐；旧P33十五归档包不改。

[A局部门](experiments/{ids[1]}.md)balanced onecopy的结构前提现在由真实82图支持，原同cap82/不改oldadjacency的任意helperbatch路线障碍可直接应用，不是全部N82图上界；Payne onecopy仍未生产，k≥2/offdiagonal holes/改变code旧边高cap未排。

[B同一local节点](experiments/{ids[2]}.md)补完实际反馈：固定ret4/W平面、全19层1539候选/1215点变量的唯一MIP数值INFEASIBLE，原810负对照仅违反新cardinality；837均匀1/3或2/3权重精确满足全部逐pin行，因此障碍是整数完整线同时互补，非连续负载已经关掉。没有独立UNSAT树/Lean，不能外推其他W/retained或任意F9族。

放开W后的另一单次45变量count模型max832仍不是实际packing，targets9/19/48没有projection profile。精确局部补全给直接生成法：两独立方向iff ceil(A/q)+ceil(B/q)≤q，含零；三独立方向正族iff有a,b,c∈1..q−1使A≤bc,B≤a(q−c),C≤(q−a)(q−b)，互补投影矩形内任取所需条数即可。50/31虽sum81仍不行；27/54实际729pins分区；target19真实det2，12/50/11不行而12/50/3唯一8/6/2 profile给65条不交线585pins。这个认识要求先选projection支持/slabs，再检查同一个S_i经全6dart的运输耦合，不再只优化837/832 counts，也不自动开新timer/大池。局部iff不是其他77targets同时可实现的证明。
'''
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+comment)
helper=R/'aris_repo/tools/research_wiki.py';calls=[]
def call(*args):
 cmd=[sys.executable,str(helper),*map(str,args)];p=subprocess.run(cmd,cwd=R,text=True,capture_output=True);calls.append({'command':cmd,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0,(cmd,p.stdout,p.stderr)
call('log',W,'2026-11-01 oneincrement ledger420 unchanged4existingrows,accepted143legal36pairsstage39_33Lean34:addeduniqueq8degree82n346515m14204970/all4225newrootBFSactualmatchedoldOnlyprefixcollapseproof,+65scopedpublic346450/priorityUNKNOWN. SourceLeanpartialactualrunning/new82codeonly300CPUpendingparent,sourceA2PASS/A82cell494inflight/B_Cnotstarted. fixedWret4all19poolnumericalINFEASnoformalUNSAT,837fractionalsanityfeasible;one45varcount832failsprofiles;two_directionceiliff+three_positiveprojectioniffexplicitlocalwitnesses/shared6dartcoupling. Noexperimentrerun/rootfile/oldpackageedit,newexpert3DRAFTpreparingnoZIP.')
call('rebuild_index',W);call('rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
paths=set()
for row in rows:
 for x in row['evidence_paths']:
  p=R/x;assert p.exists(),p;paths.add(str(p))
texts=[(W/'experiments'/f'{i}.md',(W/'experiments'/f'{i}.md').read_text()) for i in ids]+[(W/'gap_map.md',block),(W/'DD82_PROGRESS_AND_COMMENTS_20261018.md',comment),(W/'query_pack.md',(W/'query_pack.md').read_text())]
n=0
for origin,text in texts:
 for target in re.findall(r'\]\(([^)]+)\)',text):
  target=target.strip().strip('<>')
  if target.startswith(('https:','http:','mailto:','#')):continue
  target=target.split('#')[0]
  if target:assert (origin.parent/target).resolve().exists(),(origin,target);n+=1
l=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (l['pending_outside_saved_table_graph_examples'],l['pending_outside_saved_table_parameter_pairs'])==(37,32)
receipt={'status':'PASS_EXISTING_FOUR_ROWS_Q8_THREE_ACCEPTED_AND_EXACT_LOCAL_LINE_INTERFACE','updated_UTC':NOW,'ledger_records':420,'records_added':0,'records_updated':4,'accepted_graphs_added':1,'new_parameter_pairs':1,'new_concrete_Lean':0,'new_frameworks':0,'named_legal_graphs':143,'legal_parameter_pairs':36,'stage_graphs':39,'stage_pairs':33,'complete_formula_Lean':34,'known_publicly_dominated':43,'main_table_graphs':103,'main_table_pairs':3,'pending_outside_graphs':37,'pending_outside_pairs':32,'global_records':0,'new82_BFS_actual_roots':4225,'new82_independent_CPU':12.395600852,'new82_exact_sourcefill_priority':'UNKNOWN','q8_three_original_Lean_complete':False,'q8_new82_formal_status':'FOUR_MODULES_PREPARED_COMPILATION_GATED','q8_new82_formal_CPU_budget':300,'source2_A_actual':'PASS','A82':'CELL494_INFLIGHT','new_B_C_started':False,'B_fixedW_finite_pool':'NUMERICAL_INFEASIBLE_NOT_FORMAL_UNSAT','B837_fractional_sanity':'EXACT_FEASIBLE','B832_counts':'PROFILE_COUNTEREXAMPLES_NOT_ACTUAL_PACKING','B_exact_local_iff_constructive':True,'B_all6dart_coupling_open':True,'resolved_evidence_paths':len(paths),'checked_local_links':n,'actual_helper_calls':f'research-wiki/updates/{B}_HELPER_CALLS.json','query_current':True,'experiments_rerun':0,'root_owned_files_modified':False,'frozen_expert_packets_modified':False,'expert_three_status':'DRAFT_PREPARING_NO_ZIP'}
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
