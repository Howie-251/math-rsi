"""Final technical-review state and one fixed-source exhaustive edit experiment."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync'
LABEL='FINAL16416_TECHNICAL_REVIEWS_N1_TWO_CUT_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
def evidence(p,names):
    paths=[p+n for n in names];assert all((R/x).is_file() for x in paths);return paths
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];records={r['id']:r for r in L['rows']}
gid='ddp-d16d4-whole27-fulln-clone864-graph16416-20261101'
sourceid='ddp-stale-d4d5-messieres-three41-any-ninecover-capacity-20261101'
assert before==438 and gid in records and sourceid in records
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs','pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs','known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k] for k in keys};assert tuple(counts[k] for k in keys[:5])==(153,43,47,105,4)
V=S+'reviews/';a=read(V+'D16_D4_16416_A_DISPOSITION.json');b=read(V+'D16_D4_16416_B_DISPOSITION.json');f=read(V+'D16_D4_16416_FINAL_C_DISPOSITION.json')
assert all(x['root_read_entire_text'] and set(x['facets'].values())=={'PASS'} and not x['old16389_verdict_reused'] for x in [a,b,f])
assert len({x['threadId'] for x in [a,b,f]})==3 and f['distinct_from_both_actual']
assert f['full_text_characters']==20170
g=copy.deepcopy(records[gid]['source_record']);gm=g['other_metrics']
gm['historical_review_progress_checkpoint']=dict(status=g['outcome_class'],review_state=copy.deepcopy(gm['new_scope_ARIS']),distance_text=g['distance_text'])
workflow=dict(status='COMPLETE_ACTUAL_NEW_SCOPE_A_B_DISTINCT_FRESH_C_ALL3_FACETS_ROOT_ACCEPTED',
    A='PASS',B='PASS',distinct_fresh_C='PASS',A_thread=a['threadId'],B_thread=b['threadId'],C_thread=f['threadId'],
    all_threads_distinct=True,fulltext_chars=[a['full_text_characters'],b['full_text_characters'],f['full_text_characters']],
    root_read_all_three_fulltexts=True,actual_new_verdicts=3,active_remote_waits=0,
    old16389_verdict_reused=False,technical_review_complete=True,global_priority='UNKNOWN')
g.update(title='16D4/16416完整技术验收：fresh全根exactD4、新concreteLean及A/B/distinctfreshC三facet全实际PASS；priorityUNKNOWN',
    outcome_class='COMPLETE_NEW16416_MATH_CONCRETE_LEAN_A_B_DISTINCT_FRESH_C_ROOT_ACCEPTED_PRIORITY_UNKNOWN',
    distance_text='新图16416/129240/max16/exactD4：864实际fullN、12924新边/12924distinct pins/maxload1、116316旧边全保/newnew0；hist14:126/15:3924/16:12366。唯一fresh全16416roots/269485056orderedpairs≤4，每root ecc4，oldR4实测13066..13242支持≥6966，11.414157660/120CPU；source/candidate各parse1/sourceonlyBFS0。新原具体kernel、Fin15552⊕Fin864≃Fin16416、真Walk4/nonD3、160owner/864roles/12924pins及typedI32外部绑定root接受，14.020610885/200CPU含prep/失败。新scope A/B及distinctfreshC均实际三facetPASS、root各全文读取16270/16153/20170字，三thread不同，0remote等待，不继承旧16389 verdict。比已核main/URSA描述16384+32、旧本地16389+27；报告LA-UR-26-28353正文未定位/未读，globalpriority及methodoriginality仍UNKNOWN。',
    lesson_and_restart_condition='This exact newversion has completed mathematical,concreteLean and independent A/B/distinctfreshC technical review. Stop all graph/BFS/formal/review work for this closed suite;no remote waiting or newpaidcall. Technical completion does not certify globalSOTA or method originality. Keep URSA report gap and packingmaxUNKNOWN separate;no automatic33+ or oldsource restart.',
    restart_condition='Only a genuinely new research question or concrete new public comparison evidence;the exact technical suite is terminal.',
    unclosed_gap='Global priority/method originality UNKNOWN;URSA LA-UR-26-28353 fulltext remains unlocated/unread. Packing32 maximality is separately unproved;not a missing technical-review step.')
gm.update(new_scope_ARIS=workflow,complete_exact_scope_technical_reviews=True,remote_waits=0,
    external_A_thread=a['threadId'],external_B_thread=b['threadId'],external_fresh_C_thread=f['threadId'],
    external_A='ACTUAL_NEW_SCOPE_ALL3_FACETS_ROOT_ACCEPTED',external_B='ACTUAL_NEW_SCOPE_ALL3_FACETS_ROOT_ACCEPTED',
    external_fresh_C='ACTUAL_DISTINCT_NEW_SCOPE_ALL3_FACETS_ROOT_ACCEPTED',
    final_C_root_clarifications=f['root_clarifications'],external_B_root_clarifications=b['root_clarifications'],
    global_priority='UNKNOWN',method_originality='UNKNOWN',URSA_full_report_gap_closed=False,
    packing32_maximality='UNKNOWN_SEPARATE_FROM_GLOBAL_PRIORITY',exact_technical_suite_terminal=True)
gm['validated_graph_instances'][0].update(external_ARIS_AB_freshC=workflow,external_A_thread=a['threadId'],
    external_B_thread=b['threadId'],external_fresh_C_thread=f['threadId'],
    technical_review_complete=True,global_priority='UNKNOWN',latest_global_record_confirmed=False)
newpaths=evidence(V,['D16_D4_16416_B_DISPOSITION.json','D16_D4_16416_B_GEMINI_RAW.json','D16_D4_16416_FINAL_C_DISPOSITION.json','D16_D4_16416_FINAL_C_GEMINI_RAW.json'])
newpaths+=evidence(S+'public_baseline_audit/',['D16_D4_URSA_REPORT_FOLLOWUP_20261101.json','D16_D4_URSA_REPORT_FOLLOWUP_20261101.md'])
g['evidence_paths'].extend(x for x in newpaths if x not in g['evidence_paths'])

P=S+'stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/'
r,t,root=read(P+'RESULT.json'),read(P+'TERMINAL.json'),read(P+'ROOT_DISPOSITION.json')
assert root['status']=='ROOT_ACCEPTED_COMPLETE_NO_MESSIERES_N1_TWO_CUT4STAR42'
assert r['configurations_finished']==r['exact_domain']==3075 and not r['remaining_unvisited_pairs']
assert r['pair_stage_counts']=={'NEWROOT_R3_FAIL':3072,'OLDOLD_R3_FAIL':3}
assert r['newroot_R3_passed']==3 and r['final_candidate_old_label_BFS_checks']==4
assert r['original_source_single_pair_diagnostic_checks']==1 and r['source_D3_allroot_BFS_or_geodesic_enumeration']==0
assert t['all_processes_terminal'] and not t['running']
nid='ddp-stale-d4d3-messieres-n1-all3075-two-cut-fourstar42-no-20261101'
assert nid not in records and not(W/'experiments'/f'{nid}.md').exists()
paths=evidence(P,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json','ROOT_DISPOSITION.json','run_once.py','INPUT_BINDING.json','ALL3075_PAIR_PARAMETERS.tsv','ALL3075_PAIR_STAGES.tsv','ONE_OLDPAIR_ROUTE_DIAGNOSTIC.json'])
paths+=evidence(S+'stale_record_transfer_d4D3/two_corecut_star42/source_interface/',['PRED.md','NOTE.md','RESULT.json','PAPER_SCOPE_REVIEW.md'])
n=dict(id=nid,title='4D3 cached MessieresN1→42：全3075两不交删边四星严格NO；3案修新根却均伤oldold，非其他源排除',
    family='Existing graph old-edge repair and helper completion',idea_family=records[sourceid]['idea_id'],date='2026-11-01',
    wiki_verdict='no',record_type='complete_fixed_source_two_edge_cut_helper_experiment',
    target_Delta=4,target_D=3,savedL=41,baseline_date='2026-11-01 current main41;cached MessieresN1 source facts inherited',
    n=dict(actual=None,hypothetical=42),actual_graph_Delta=None,actual_D=None,
    actual_D_scope='All3075 actual edited42/84 candidates rejected by finalcandidate ordinaryBFS;no accepted finalgraph/globalD per failed candidate claimed',
    ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=3,
    scope='Only cached literal MessieresN1,41vertices/82edges/4regular. For each unordered pair of vertex-disjoint oldedges,delete exactly2 oldedges and add newvertex41 joined to their4 endpoints. Exactly3075 configurations,each42/84 and4regular. NewrootR3 gate first,oldlabel ordinaryBFS only for passers. This is not the older ordinaryninecover/D5 model,notN2/N3,otherN1rewirings or general4D3.',
    outcome_class='ROOT_ACCEPTED_COMPLETE_NO_N1_ALL3075_TWO_DISJOINT_EDGECUT_ONE4STAR',new_lower_bound=False,
    distance_text='预测存在newrootR3通过案得到支持3次，但没有完整D3图。3075unordereddisjointedgepairs全完成：3072案newrootR3失败，3案过门却全oldold失败，仅4个candidate旧labelBFS。首oldpair(1,33)两端均非pin：旧源一次针对pair诊断给3路1–17–22–33，删边17–22后实际新最短4路1–17–41–22–33；没有枚举所有旧最短路或声称旧路线unique。缓存JSON输入parse1，0sourceD3allroot/field/solver/Lean。累计.350856972/20CPU含接口.121139383；无未访问配置，只排该fixedsource/rule。',
    lesson_and_restart_condition='STOP this exact N1 two-disjoint-cut plusone4star family. Newroot coverage can be repaired while nonpin oldpairs lose their distance3 routes;do not infer complete success from newrootR3 or focus only on pins. Do not continue source/cut/seed/model budget automatically. The canonical alternative41_ninecover node supplies the same cachedN1 input,not a reused exclusion for this different edit scope.',
    restart_condition='A separately justified different rewiring or source;N2/N3 and otherN1edits remain outside this strictNO.',
    unclosed_gap='N2/N3 sources,otherN1rewirings and generalN(4,3) remain open;0new acceptedgraph/parameter/Lean.',
    other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
        related_cached_source_node=sourceid,same_as_old_ninecover_scope=False,new_source_gate_node=False,
        source_id='MessieresN1',source_n=41,source_m=82,source_degree=4,
        target_n=42,target_m=84,target_degree=4,Moore_bound=53,Moore_space_from_baseline=12,
        Moore_space_is_not_constructibility=True,unordered_disjoint_edgepair_domain=3075,
        configurations_finished=3075,newroot_R3_fail=3072,newroot_R3_pass=3,oldold_fail_after_pass=3,
        prediction_newroot_supported=True,prediction_complete_graph_success=False,
        candidate_newroot_ordinary_BFS=3075,candidate_old_label_BFS=4,
        source_single_pair_diagnostic=1,source_D3_allroot_BFS=0,
        first_oldold_failure=r['first_oldold_failure'],one_oldpair_route_diagnostic=r['one_oldpair_diagnostic'],
        old_route_uniqueness_claimed=False,source_cached_JSON_parses=1,
        remaining_unvisited_pairs=0,complete_fixed_rule_exclusion=True,
        cumulative_charged_CPU_seconds=t['cumulative_charged_CPU_seconds'],CPU_budget_seconds=20,
        inherited_interface_CPU_seconds=t['prior_case_CPU_seconds'],no_timer_reset=True,terminal=True),evidence_paths=paths)
rawpath=OUT/f'{LABEL}_ROWS.json';rawpath.write_text(json.dumps([g,n],ensure_ascii=False,indent=2)+'\n')
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
    text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and LABEL not in text
    prefix[fn]=text[:text.index(END)+len(END)]
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
norm=[]
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):
    for raw in [g,n]:
        v=c['normalize'](raw);v['goal']['baseline_date']=raw['baseline_date'];c['write_node'](v);records[v['id']]=v;norm.append(v)
# Source reuse pointer only;the old source/ninecover experiment is neither rerun nor recounted.
sp=W/'experiments'/f'{sourceid}.md';old=sp.read_text();assert LABEL not in old
sp.write_text(old+'\n\n<!-- '+LABEL+' -->\n## cachedN1在另一改边问题中的新终态（旧ninecover范围不变）\n\nN1同一41/82源被用于4D3/42目标的两不交oldedgecut＋新4star；完整3075配置全排，3newrootpass均oldoldfail。不是复跑本页9cover/D5，也不把本页N2/N3的coverNO搬给新rewire。见[固定N1新实验]('+nid+'.md)。0新source验收或独立方法；其他source/改边仍未排，不自动续算。\n')
up=dict(path='research-wiki/experiments/'+nid+'.md',date='2026-11-01',note='SamecachedN1 reused for different4D3two-cut4star42scope,all3075NO;not an ordinaryninecover rerun or N2/N3 exclusion.')
for container in [records[sourceid]['other_metrics'],records[sourceid]['source_record']['other_metrics']]:container.setdefault('later_source_reuse_updates',[]).append(copy.deepcopy(up))
L.update(rows=list(records.values()),record_count=before+1,updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=2
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
def table(v):
    safe=c['safe'];return '| ['+safe(v['title'])+'](experiments/'+v['id']+'.md) | '+safe(c['goal_text'](v))+' | '+safe(c['gap_text'](v))+' | '+safe(v['exact_scope'])+'；'+safe(v['lesson'])+'；[原始证据](../'+v['evidence_paths'][0]+') |'
mp=W/'DDP_METHOD_LEDGER.md';md=mp.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{before+1}条记录；不以此宣称{before+1}种独立方法。',1)
lines=md.splitlines();matches=[i for i,line in enumerate(lines) if line.startswith('| [') and '(experiments/'+gid+'.md)' in line];assert len(matches)==1;lines[matches[0]]=table(norm[0]);md='\n'.join(lines)+'\n'
h=re.search(r'^更新：[^\n]+',md,re.M);assert h
summary='更新：'+NOW+'。数学合法153图／43参数／完整具体Lean47；savedmain105/4，outside45/38，known43(overlap40)，全球确认0。16416新A/B/distinctfreshC三facet均实际PASS，技术审阅终态无remote等待，globalpriority/URSA报告缺口仍UNKNOWN。'
md=md[:h.start()]+summary+md[h.end():]
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 16416技术审阅完整终态；cachedN1固定改边全域失败\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+table(norm[1])+'\n\n新16416原节点A/B/distinctfreshC全部实际三facetPASS，kernel与互审均terminal，不重BFS/Lean/付费。URSA报告正文未定位，globalpriority/methodoriginality仍UNKNOWN；32未证最大是另一问题。新N1只一实验节点，非另计sourcegate/方法，0图/参数/Lean；记录438→439不等于439种方法。15老格、同Goal ACTIVE、旧N8/n61暂停保留。\n';mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 最新actual：16416完整技术审阅终态；N1/42两cut四星全3075NO\n\n16416 freshC已实际三facetPASS并root全文20170字接受，thread'+f['threadId']+'，与A'+a['threadId']+'及B'+b['threadId']+'均不同。数学/fresh全根BFS、完整新kernel、A/B/distinctfreshC均terminal，0remote等待，不重图/Lean/付费。不声称globalSOTA：main/URSA描述16384已直接读，但LA-UR-26-28353报告正文仍未定位/未读，globalpriority及methodoriginalityUNKNOWN，packing32maxUNKNOWN独立保留。\n\ncachedMessieresN1(41/82/4regular)两不交oldedgecut＋新4star42/84全3075配置完成：3072newrootR3fail、3newrootpass却全oldoldfail，4candidate旧根BFS/1旧sourcepair诊断，0sourceD3allroot重验。存在newrootpass的预测支持3次，不是新图成功；首nonpinpair1,33旧3路1–17–22–33在cut17–22后新最短4路1–17–41–22–33，不称旧routeunique。严格NO仅该N1/rule，不排N2/N3/其他改边/general4D3；.350856972/20CPU含接口，STOP不续source/cuts。\n\n439条（记录非方法）、153图／43参数／Lean47、savedmain105/4、outside45/38、known43(overlap40)、global0均按原计数；0新增图/参数/Lean。715已闭全部保边新增范围；15老格人工主线、sameGoal ACTIVE、旧N8/n61暂停保留，不自动33+。\n\n'+ '；'.join('['+v['title']+'](experiments/'+v['id']+'.md)' for v in norm)+'\n\n'
preserved={}
for fn,pre in prefix.items():
    path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
    if fn=='index.md':
        text=re.sub(r'^- `exp:'+re.escape(gid)+r'`[^\n]*','- `exp:'+gid+'` — '+norm[0]['title']+' [yes]',text,flags=re.M)
        m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m
        text=text[:m.start()]+f'## Experiments ({int(m[1])+1})'+text[m.end():];pos=text.index('\n',m.start())+1
        text=text[:pos]+'- `exp:'+nid+'` — '+norm[1]['title']+' [no]\n'+text[pos:]
    assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': existing16416node exacttechnicalreviews complete(A/B/distinctfreshCactualallthreefacetsROOTfulltextaccepted),0remotewaits,globalpriority/URSAreportgapstillUNKNOWN. One newN1twocut4star42experiment(all3075completeNO,3newrootpassalloldoldfail),notnewsourcegateormethod. Records438to439;153/43/47,savedmain105/4,global0unchanged;human15oldcells top preserved,no computation/review/reimport.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==before+1 and {k:after[k] for k in keys}==counts
for v in norm:assert all((R/x).exists() for x in v['evidence_paths'])
receipt=dict(status='PASS_FINAL16416_TECHNICAL_REVIEWS_AND_ONE_FIXED_N1_EXPERIMENT',updated_UTC=NOW,
    records_before=before,records_after=before+1,records_added=1,new_experiment_id=nid,
    updated_graph_node=gid,new_source_gate_nodes=0,graph_parameter_Lean_method_increments=[0,0,0,0],
    counts_unchanged=counts,new16416_A_B_distinctfreshC_actual_all3_facets_rootaccepted=True,
    review_threads=[a['threadId'],b['threadId'],f['threadId']],active_remote_waits=0,
    global_priority='UNKNOWN',URSA_report_gap_closed=False,packing32_maximality='UNKNOWN_SEPARATE_QUESTION',
    N1_exact_all3075_NO=True,N1_newroot_prediction_supported_3=True,N1_complete_graph_hits=0,
    N2_N3_other_rewiring_or_general4D3_excluded=False,N1_oldroute_uniqueness_claimed=False,
    human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,
    source_graph_BFS_Lean_solver_paidreview_remote_hash_runs=0,root_STATE_HTML_progress_REPORT_modified=False,
    writes_limited_to_Wiki_and_stage_wiki_sync=True,sameGoal='ACTIVE',old_N8_n61='PAUSED',
    CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
