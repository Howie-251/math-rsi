"""In-place paper scope strengthening of existing451; zero new numeric experiments."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,runpy,time
ROOT=Path(__file__).resolve().parents[4];W=ROOT/'research-wiki';S=Path(__file__).resolve().parent
D=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/threecut_fourhelper_star1254'
start=time.process_time();now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
slug='ddp-stale-d3d10-conder1250-three-matching-cuts-fourhelper-star-global-no-20261101'
marker='<!-- SOURCE1250_STAR_CENTRE_PAIRING_SCOPE_20261102 -->'
ledger=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert ledger['record_count']==len(ledger['rows'])==452
pos=next(i for i,r in enumerate(ledger['rows']) if r['id']==slug);old=ledger['rows'][pos];raw=copy.deepcopy(old['source_record'])
otherrows={r['id']:copy.deepcopy(r) for r in ledger['rows'] if r['id']!=slug};counts={k:v for k,v in ledger.items() if k not in {'rows','record_count','updated_UTC','input_counts'}}
assert 'negative_pairing_scope_extension_20261102' not in raw['other_metrics']
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
files=['index.md','query_pack.md','gap_map.md'];original={p:(W/p).read_text() for p in files};end='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';human={p:t[:t.index(end)+len(end)] for p,t in original.items()}
addendum=str((D/'GLOBAL_CENTRE_PAIRING_SCOPE_ADDENDUM.md').relative_to(ROOT));assert (ROOT/addendum).exists()
raw['title']='3D10 Conder1250三matching-cut四helper星：全1743779均centre失败，六端点任意15配对亦NO'
raw['scope']='FixedactualConder1250source. Deleteany3vertex-disjoint originaledges; useallsixfreedendpoints exactlyonce,partitionarbitrarilyinto3unordered2pointgroups,eachattachedtooneleaf; newcentreconnectsonlythesethreeleaves(K1,3); noothermodification/oldrepair. Actualnumericvisited1743779anchoredmatching-cuttriples,allfailcentreR8six-endpointunion. Thecentreexactdistance2+dG(all6pins,t)isindependentofthe15pairings,sothesamecountertargetexcludeseverypairingbypaperdeduction,notnewenumeration. SourceedgeVTanchorsallcuttriples; no candidateVT. Previouswholecut-to-leafdomainisnumericgenerator/leafweighted-formuladomainhistory,notcurrentnegativeboundary. Excludesnootherhelper topology/sharedcuts/morecuts/repair/otherhost/general3D10.'
raw['actual_D_scope']=raw['actual_D_scope']+' Paperfollowup20261102extendsnegativefromwholecutpairingtoall15six-pinpairingsbycentreindependence; visitedremains1743779cuts,not15timesgraphs.'
raw['distance_text']+=' 2026-11-02纸面范围补强：centre距离2+dG(全部六端点,t)与六端点如何配三对无关，同一1743779cuttriple数据已排每组全部15种unordered2+2+2配对。未另枚图/跑BFS。leaf weighted-G正向公式仍只限wholecutpairs，不能套给跨cut配对。'
raw['lesson_and_restart_condition']+=' STOPalsocoversall15pairingsforeachcuttriple:donotre-runwithcross-cutpairingasnewgenerator,becausethecentreobstructionisunchanged. Thisispaperscopeclosure,notnewnumericprogress.'
raw['restart_condition']='Anewauthorizedboundedquestionmustchangehelper topology/routecost,cutcontract,hostorothermeaningfulrule; changingonlythepairingofsixpinsintheleafK1,3isalreadyclosed. Noautomaticfourthcut/newsource/anchor/seed.'
raw['unclosed_gap']='Otherfourhelper topologies(P4etc),shared/nonmatchingcuts,extraoldoldrepair,morecuts,otherhosts/morehelpers/general3D10remainunexcluded. Arbitrarysix-pin2+2+2pairingwithsameK1,3isnowexcluded,notopen. Leafweighted-Gpositiveformularemainsprovedonlyforwholecutpairs;donotapplyittoarbitrarypairings. Leafgatesnotentered;individualleaffailureunmeasured. No newLean graph/theorem orrecord; GoalACTIVE/oldN8n61PAUSED.'
raw['positive_guarantees'].append('Centreexactdistance2+dT(all6pins,t)=2+dG(all6pins,t)holdsforany2+2+2leafpairing; thesameall-centreNOexcludesall15unorderedpairingsbypaperalone. Do notextendwholecutleafweighted-Gformulatocross-cutpairings.')
raw['other_metrics']['negative_pairing_scope_extension_20261102']={
'kind':'PAPER_DEDUCTION_FROM_EXISTING_ALL_CENTRE_FAILURE_DATA','actual_visited_cuttriples_unchanged':1743779,'unordered_pairings_per_sixpins':15,'extra_pairings_enumerated':0,'extra_candidate_graphs_or_BFS':0,
'centre_formula':'d_final(C,t)=2+dT(all6pins,t)=2+dG(all6pins,t)','centre_independent_of_leaf_pairing':True,'negative_scope':'all15unordered2+2+2pairingsforeachsource3matchingcuttriple/K1,3/noothermodification',
'positive_leaf_weighted_G_formula_scope':'wholeoriginalcutendpointpairtooneleafonly','arbitrary_pairing_leaf_formula_not_claimed':True,'old_RESULT_scope_retained_as_numeric_history':True,'new_method_graph_parameter_Lean':[0,0,0,0]}
raw['other_metrics']['global_gate']['current_negative_pairing_scope']='all15unorderedpairings_by_centre_paper_deduction_not_new_scan'
raw['other_metrics']['negative_Lean_requirement']['paper_scope']='inheritedconcretesource+3matchingcuts+allsixpinsarbitrary2+2+2partition+K1,3 centreformula;leafpositiveformulaseparatelywholecutpairsonly'
raw['evidence_paths']=list(dict.fromkeys(raw['evidence_paths']+[addendum]));assert all((ROOT/p).exists() for p in raw['evidence_paths'])
row=common['normalize'](raw);row['goal']['baseline_date']=raw['baseline_date'];assert not common['capture'].screen(json.dumps(raw,ensure_ascii=False))
rowfile=S/'SOURCE1250_STAR_CENTRE_PAIRING_SCOPE_20261102_ROW.json';rowfile.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
helper=common['helper'];helper.rebuild_index=lambda *_a,**_kw:None;helper.rebuild_query_pack=lambda *_a,**_kw:None
with (S/'SOURCE1250_STAR_CENTRE_PAIRING_SCOPE_20261102_NODE_CALLS.log').open('w') as out,contextlib.redirect_stdout(out):common['write_node'](row)
ledger['rows'][pos]=row;ledger['updated_UTC']=now;ledger['input_counts'][str(rowfile.relative_to(ROOT))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
node='experiments/'+slug+'.md'
summary=f'''\n\n{marker}
### {now} 原451星节点补强：同一centre反例排全部15种六端点配对

centre精确距离2+dG(全部六端点,t)与分成哪三对leaf无关。因此已完成的1743779 matching-cuttriples全部centre fail，按paper同时排每triple任意15种unordered2+2+2配对/K1,3；跨cut配对不是待重跑的新方向。visited仍1743779 cuts，没有追加15倍图/数值/BFS。

leaf weighted-G正向公式仍只在原wholecutpairs范围成立，不能随negative扩scope套到其他配对；leaf门仍NOT_ENTERED。其它helper拓扑/sharedcuts/repair/host/一般3D10未排。仅原451节点原位纸面范围更正，452→452/add0，starline3.611239973/30不变，0新图/参数/Lean/方法。153/43/47与人工15格top原文保持；Goal ACTIVE/旧N8n61暂停。

[{raw['title']}]({node})

'''
for name in files:
 text=original[name];assert marker not in text;cut=len(human[name]);(W/name).write_text(text[:cut]+summary+text[cut:]);assert (W/name).read_text().startswith(human[name])
md=(W/'DDP_METHOD_LEDGER.md').read_text();assert marker not in md
md+=f'''\n\n{marker}
## {now} 原451负范围加强：任意六端点配三对也NO

[原451同一星实验]({node})：centre2+dG(六端点,t)不看leaf配对，既有1743779cuttriples全centre失败已纸面排每triple全部15种unordered2+2+2配对。没有再枚图/新BFS；visited仍1743779，不乘15计工作量。leaf weighted-G正向公式仍只限wholecutpairs，其他配对的leaf公式未声称。一般P4/其他helper拓扑、sharedcuts/repair/host不排。

[新增纸面范围论证](../{addendum})；原RESULT的wholecut scope留作执行历史，不限制当前negative。ledger452→452/add0，图/参数/Lean/方法均0新增，原starline3.611239973/30与153/43/47不变。
'''
(W/'DDP_METHOD_LEDGER.md').write_text(md)
after=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert after['record_count']==len(after['rows'])==452;assert all(after[k]==v for k,v in counts.items());assert all(r==otherrows[r['id']] for r in after['rows'] if r['id']!=slug)
receipt={'status':'PASS_EXISTING451_CENTRE_PAIRING_SCOPE_PAPER_EXTENSION','updated_UTC':now,'records_before':452,'records_after':452,'records_added':0,'updated_id':slug,'canonical_node':str((W/node).relative_to(ROOT)),'row_path':str(rowfile.relative_to(ROOT)),'negative_scope':'fixedConder1250/3disjointsourcecuts/allsixpinsonce/any15unordered2+2+2pairings/K1,3/noothermodification','actual_numeric_visited_cuttriples_unchanged':1743779,'new_pairings_enumerated':0,'new_candidate_graph_BFS_Lean_paid_runs':0,'positive_leaf_weighted_G_scope':'wholecutpairsonly_not_extended','old_RESULT_scope_preserved_as_history':True,'other452row_and_all_other_rows_preserved_exact':True,'graph_parameter_Lean_method_increments':[0,0,0,0],'counts_unchanged':{k:after[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs']},'starline_CPU_unchanged':3.611239973,'starline_CPU_cap':30,'human_top_blocks_preserved_exact':{p:True for p in files},'index_experiment_count_unchanged':539,'full_rebuild_reimport':False,'root_STATE_ROUND_pages_recovery_modified':False,'sameGoal':'ACTIVE','old_N8_n61':'PAUSED','sync_CPU_seconds':time.process_time()-start,'stop':True}
(S/'SOURCE1250_STAR_CENTRE_PAIRING_SCOPE_20261102_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
