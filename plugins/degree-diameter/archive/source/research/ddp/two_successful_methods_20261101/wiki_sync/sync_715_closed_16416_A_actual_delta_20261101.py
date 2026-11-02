"""Two existing-node terminal updates; no source, graph, H, formal or review run."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync'
LABEL='715_COMPLETE_CLOSURE_16416_A_ACTUAL_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];records={r['id']:r for r in L['rows']}
pid='ddp-stale-d11d3-715-cross-oldclass-helper-min3-tight-route-tradeoff-20261101'
gid='ddp-d16d4-whole27-fulln-clone864-graph16416-20261101'
old715='ddp-stale-d11d3-715-fixed-induced-arbitrary-helpers-obstruction-20261101'
assert before==438 and tuple(L[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances'])==(153,43,47)
countkeys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs','pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs','known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k] for k in countkeys}
Q=S+'stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/'
closure,dispo=read(Q+'HIGHER_DEGREE_CLOSURE_RESULT.json'),read(Q+'ROOT_DISPOSITION.json')
assert closure['status']=='SUPPORTED_COMPLETE_NO_FIXED715_ALL_OLD_EDGES_RETAINED_ARBITRARY_FINITE_AUGMENTATION'
assert dispo['status']=='ROOT_ACCEPTED_PAPER_COMPLETE_NO_FIXED715_ALL_EDGE_PRESERVING_AUGMENTATIONS' and dispo['full_scope_closed']
assert closure['inherited_design_or_source_recomputed'] is False and closure['new_graphs']==closure['new_Lean']==0
p=copy.deepcopy(records[pid]['source_record']);history=copy.deepcopy(p)
p.update(title='11D3固定715全保边新增族严格NO：任意finite helpers及old-old/new-old/new-new边均排，须改旧边或换host',
    wiki_verdict='no',record_type='paper_complete_fixed_host_augmentation_exclusion',
    outcome_class=dispo['status'],
    scope='Actual fixed715 host,retain every oldedge,add a nonempty finite helper set H with arbitrary added simple old-old/new-old/new-new edges,maxdegree11,D<=3. All newold-old edges,including originalP3 leaf-leaf triangle completions,are included. The520 oldcore is saturated. Inherit source/core/design/moment inputs without revalidation. This is the complete edge-preserving augmentation family of this host,not generalN(11,3),oldedge deletions/replacements or anotherhost.',
    actual_D_scope='Complete paper exclusion for the stated fixed-host preserved-oldedge family;no candidate graph/H enumeration/sourceBFS',
    distance_text='原minHdegree3及8distinctleafpins/(b,c,s)20/8/0或21/7/1要求其3邻居H度数和13或12。新论证不要求helper是min点：任意d=4..7，ownclasses q≤11−d≤7，badowner≥65−q≥54+d；全H最低度3故neighbor spokes b≤8d，owncross c≤11−d。必要54+d≤b+c≤7d+11即43≤6d，逐排4..7（deficits19/13/7/1）。所有Hdegree只能3或≥8；min3点的3邻居度数和只能9或≥14，不能12/13，矛盾。一般mixedmin3在此固定保边scope也已关闭；原开放状态仅历史。累计小算式.022627260/5CPU，新增.000391260，0source/design/H枚举/BFS/solver/Lean重跑。',
    lesson_and_restart_condition='STOP every nonempty finite edge-preserving augmentation of this exact715host,including mixedmin3H and internalP3 triangle completion. A next construction must delete/replace oldedges or changehost;neither alternative is excluded or automatically authorized by this proof. Do not restart a preserved-edge Hsearch or label generalN11D3 impossible.',
    restart_condition='A genuinely changed oldedge-deletion/replacement rule or differenthost under a bounded research decision.',
    unclosed_gap='GeneralN(11,3),oldedge deletion/replacement and otherhosts remain open;no new graph/parameter/Lean or method count.')
pm=p['other_metrics'];pm.update(historical_min3_checkpoint=dict(status=history['outcome_class'],distance_text=history['distance_text'],metrics=history['other_metrics']),
    minimum3_open_checkpoint_is_historical=True,general_mixed_min3_H_excluded=True,
    complete_fixed715_all_oldedges_retained_nonempty_augmentation_family_excluded=True,
    arbitrary_added_oldold_newold_newnew_edges_included=True,intraP3_leafleaf_completions_included=True,
    excluded_nonminimum_helper_degrees=[4,5,6,7],remaining_helper_degrees=[3,8,9,10,11],
    required_min3_neighbor_degree_sums=[12,13],actual_possible_min3_neighbor_degree_sums='9 or>=14',
    core_inequality='54+d<=b+c<=8d+(11-d)=7d+11 implies43<=6d,impossible4..7',
    full_scope_closed=True,new_scalar_closure_CPU_seconds=closure['new_CPU_measured_process_seconds'],
    cumulative_small_scalar_CPU_seconds=dispo['measured_small_scalar_CPU_seconds'],CPU_budget_seconds=5,
    H_graphs_generated=0,H_searches=0,source_core_design_BFS_rechecks=0,new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0)
extra=[Q+n for n in ['HIGHER_DEGREE_CLOSURE_PRED.md','HIGHER_DEGREE_CLOSURE_NOTE.md','HIGHER_DEGREE_CLOSURE_RESULT.json','ROOT_DISPOSITION.json']]
assert all((R/x).is_file() for x in extra)
p['evidence_paths'].extend(x for x in extra if x not in p['evidence_paths'])

A=S+'reviews/D16_D4_16416_A_DISPOSITION.json';a=read(A)
assert a['status']=='ROOT_READ_FULLTEXT_ACCEPTED_NEW_EXACT_SCOPE_WITH_CLARIFICATIONS'
assert a['root_read_entire_text'] and set(a['facets'].values())=={'PASS'} and not a['old16389_verdict_reused']
g=copy.deepcopy(records[gid]['source_record'])
g['title']='16D4/16416：数学＋新concreteLean＋新A三facet实际PASS；B在途、freshC未派'
g['outcome_class']='ROOT_ACCEPTED_16416_MATH_LEAN_NEW_A_THREE_FACETS_PASS_B_INFLIGHT_C_UNDISPATCHED'
g['distance_text']+=' 新scope A实际完整16270字已root全文处置：math/formal-original-target/literal-binding三facet PASS，独立thread af23d117-58eb-43ba-a699-d4f683640eaa；不是旧16389 verdict。保留reviewer原文并澄清planeinjectivity需imB∩span(v)=0及kerB∩W=0或compiled recover_plane，不能只据某方向坐标非零；32非optimum与globalpriorityUNKNOWN各自有独立理由。B仍同exec1064在途，freshC未派。'
g['lesson_and_restart_condition']='Production/BFS and newconcreteLean are terminal;newscope AactualthreefacetPASS rootaccepted with recorded prose clarifications. B remains in flight in originalexec1064,C not dispatched. No newreview retry,old16389PASS reuse,33+packing or extra graph/formal checks. Keep latest715preservededgeclosure and15oldcells recovery scope.'
g['unclosed_gap']='Latest global priority/originality UNKNOWN;newB in flight and distinctfreshC not dispatched;no B/C PASS asserted.'
workflow=dict(A='ROOT_ACCEPTED_NEW_EXACT_SCOPE_THREE_FACETS_PASS_WITH_CLARIFICATIONS',A_thread=a['threadId'],A_disposition=A,
    B='IN_FLIGHT_ORIGINAL_EXEC1064',C='NOT_DISPATCHED',actual_new_verdicts=1,old16389_verdict_reused=False)
gm=g['other_metrics'];gm.update(new_scope_ARIS=workflow,external_A_thread=a['threadId'],external_A_facets=a['facets'],
    external_A_root_fulltext_characters=a['full_text_characters'],external_A_clarifications=a['clarifications'],
    external_A_actual_one_call=True,external_A_retried=False)
gm['validated_graph_instances'][0].update(external_ARIS_AB_freshC=workflow,external_A_thread=a['threadId'])
ap=[A,S+'reviews/'+a['raw']];assert all((R/x).is_file() for x in ap)
g['evidence_paths'].extend(x for x in ap if x not in g['evidence_paths'])
raws=[p,g];rawpath=OUT/f'{LABEL}_ROWS.json';rawpath.write_text(json.dumps(raws,ensure_ascii=False,indent=2)+'\n')
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
    txt=(W/fn).read_text();assert txt.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and LABEL not in txt
    prefix[fn]=txt[:txt.index(END)+len(END)]
oldpaper=(W/'experiments'/f'{pid}.md').read_text()
assert LABEL not in oldpaper
# Canonical updater preserves existing verdict metadata,so set the now-closed verdict before its upsert.
(W/'experiments'/f'{pid}.md').write_text(re.sub(r'^verdict: partial$', 'verdict: no',oldpaper,count=1,flags=re.M))
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
norm=[]
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):
    for r in raws:
        n=c['normalize'](r);n['goal']['baseline_date']=r['baseline_date'];c['write_node'](n);records[n['id']]=n;norm.append(n)
# Keep the previously open checkpoint explicitly historical inside the same node.
historical=re.sub(r'^---\n.*?\n---\n','',oldpaper,count=1,flags=re.S)
pp=W/'experiments'/f'{pid}.md';pp.write_text(pp.read_text()+'\n\n<!-- '+LABEL+' -->\n<details>\n<summary>历史中间检查点：mixedmin3当时仍开放，已被上面的完整闭合覆盖</summary>\n\n'+historical+'\n</details>\n')
op=W/'experiments'/f'{old715}.md';op.write_text(op.read_text()+'\n\n<!-- '+LABEL+' -->\n## 后续全部保边新增族已完整关闭\n\n此前“跨class后一般mixedmin3仍开放”现为历史。新非minimum-helper度数4..7路线容量矛盾与min3邻居度数和12/13冲突，root已接受固定715保留全部旧边、任意old-old/new-old/new-new新增及非空finiteH/max11/D3全NO，含原P3内leafleaf补三角。见[完整闭合]('+pid+'.md)。0旧源/H枚举重跑；下一需删改旧边或换host，不外推一般N11D3。\n')
u=dict(path='research-wiki/experiments/'+pid+'.md',date='2026-11-01',note='Now completeNO allfixed715 edge-preserving nonemptyfiniteaugmentations;oldmixedmin3open is historical;delete/replace oldedge orchangehost needed.')
for d in [records[old715]['other_metrics'],records[old715]['source_record']['other_metrics']]:d.setdefault('later_scope_updates',[]).append(copy.deepcopy(u))
L.update(rows=list(records.values()),updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=2
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
def table(n):
    safe=c['safe'];return '| ['+safe(n['title'])+'](experiments/'+n['id']+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+n['evidence_paths'][0]+') |'
mp=W/'DDP_METHOD_LEDGER.md';lines=mp.read_text().splitlines()
for n in norm:
    matches=[i for i,line in enumerate(lines) if line.startswith('| [') and '(experiments/'+n['id']+'.md)' in line];assert len(matches)==1
    lines[matches[0]]=table(n)
md='\n'.join(lines)+'\n';h=re.search(r'^更新：[^\n]+',md,re.M);assert h
summary='更新：'+NOW+'。数学合法153例／43参数、完整具体Lean47；savedmain105/4，outside45/38，known43（overlap40），全球确认0。715固定源全部保边非空新增族现完整NO；16416新A三facet实际PASS，B在途、freshC未派。'
md=md[:h.start()]+summary+md[h.end():]
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 原715节点完整闭合；16416新A实际返回\n\n不新增记录或方法。715从min3必要条件推进到全部固定host保边新增族严格NO：54+d≤7d+11排非minhelperdegree4..7，余3或≥8与min3邻居度数和12/13矛盾。旧mixedmin3OPEN明确仅历史，STOP保边Hsearch，下一必须删改旧边或换host。总.022627260/5CPU，新增.000391260，0原数据/H枚举重跑。16416新Athread'+a['threadId']+'已root全文处置三facetPASS且澄清原文保留；B原exec1064在途、freshC未派。438条/153/43/47均不变。\n';mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 最新终态：715所有保边新增族NO；16416新A已实际PASS\n\n715固定actual715、保留全部oldedges、任意新增simple old-old/new-old/new-new边及非空finiteH、cap11/D≤3现完整NO，含原P3内leafleaf补三角。先有minH3及min3点邻居Hdegreesum12/13；新对任意helper d4..7由ownclasses≤11−d、bad≥54+d、b≤8d、c≤11−d得43≤6d矛盾。故Hdegrees只能3或≥8，min3点邻居sum只能9或≥14，终矛盾。此前mixedmin3OPEN是已被覆盖的历史；.022627260/5CPU总、仅新增.000391260，0source/design/H枚举/BFS重跑。STOP该host所有保边新增搜索；下一需删旧边/换host，不排一般N11D3。\n\n16416新scope A已actual返回并root全文处置math/formal-original-target/literal-binding三facetPASS，thread'+a['threadId']+'，reviewer少量表述澄清与原文保留；不继承旧16389。B原exec1064仍在途，freshC未派，不记B/C通过。153图／43参数／Lean47、savedmain105/4、outside45/38、known43(overlap40)、global0，438条不增。15老题人工顶部、sameGoal ACTIVE、旧N8/n61暂停保留；不自动33+。\n\n'+ '；'.join('['+n['title']+'](experiments/'+n['id']+'.md)' for n in norm)+'\n\n'
preserved={}
for fn,pre in prefix.items():
    path=W/fn;txt=path.read_text();assert txt.startswith(pre);at=len(pre);txt=txt[:at]+'\n\n'+nav+txt[at:]
    if fn=='index.md':
        for n in norm:txt=re.sub(r'^- `exp:'+re.escape(n['id'])+r'`[^\n]*','- `exp:'+n['id']+'` — '+n['title']+(' [no]' if n['id']==pid else ' [yes]'),txt,flags=re.M)
    assert txt[:at]==pre;path.write_text(txt);preserved[fn]=True
helper.append_log(str(W),LABEL+': twoexistingcanonicalnodes updated,no rows/countincrements. Fixed715full edge-preservingnonemptyfiniteaugmentationfamily completepaperNO,oldmixedmin3openpreservedashistory,requiresoldedgechangeornewhost. New16416AactualfulltextrootacceptedthreefacetPASSwithclarifications,thread'+a['threadId']+';Bexec1064inflight,Cnotdispatched,noB/Cverdict. Human15oldcells top/counts438,153/43/47unchanged;no graph/source/H/formal/paidreview/hashrun.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==before and {k:after[k] for k in countkeys}==counts
for n in norm:assert all((R/x).exists() for x in n['evidence_paths'])
receipt=dict(status='PASS_EXISTING715_COMPLETE_CLOSURE_AND_NEW16416_A_ACTUAL_DELTA',updated_UTC=NOW,
    records_before=before,records_after=before,records_added=0,updated_experiment_ids=[pid,gid],
    graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
    fixed715_preserved_alloldedges_nonempty_augmentation_family_complete_NO=True,
    original_P3_triangle_completions_included=True,general_N11D3_or_oldedge_changes_excluded=False,
    min3_open_checkpoint_preserved_as_history=True,source_design_H_graph_enumeration_rechecks=0,
    new16416_A_actual_root_disposition=A,new16416_A_thread=a['threadId'],A_three_facets=a['facets'],
    B='IN_FLIGHT_ORIGINAL_EXEC1064',freshC='NOT_DISPATCHED',old16389_verdict_reused=False,
    human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,
    graph_BFS_Lean_solver_paidreview_remote_hash_runs=0,root_STATE_docs_HTML_REPORT_modified=False,
    writes_limited_to_Wiki_and_stage_wiki_sync=True,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
