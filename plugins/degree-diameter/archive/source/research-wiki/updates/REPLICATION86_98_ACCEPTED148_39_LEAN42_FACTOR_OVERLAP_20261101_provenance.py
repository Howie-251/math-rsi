from pathlib import Path
from datetime import datetime,timezone
import copy,json,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';B='REPLICATION86_98_ACCEPTED148_39_LEAN42_FACTOR_OVERLAP_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,148,39,42)
rid='ddp-full-ovoid-spread-fixed-cap-singlehelper-rsquare-conditional-saturation-barrier-20261101';r=copy.deepcopy(next(x for x in L['rows']if x['id']==rid)['source_record'])
oldids=['ddp-polarity585-port-steiner-local-premises-20261027','ddp-polarity585-all-preserved-edge-extensions-theorem-20261027'];data='research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/'
e=['research-wiki/experiments/'+i+'.md'for i in oldids]+[data+x for x in ['SOURCE.json','BLOCKS.json','PORT_R2.json','THEOREM.md']]+['research/ddp/polarity585_replication/source585.implicit_adj.txt'];assert all((R/x).is_file()for x in e)
m=r['other_metrics']['factor_radius2_overlap_paper_and_literal15_experiment'];m.update(status='OLD_ACTUAL585_STEINER_PREMISES_INHERITED_NEW_PRODUCT_ROUTE_APPLICATION_AND_NEW_LITERALQ2_CALIBRATION',
    support72_pair9_triple1_already_known_since='2026-10-27',not_first_discovery=True,new_theorem_or_method_count=0,inherited_Wiki_nodes=oldids,inherited_data=data,
    old_actual_source='research/ddp/polarity585_replication/source585.implicit_adj.txt',old_design='Steiner3-(65,9,1)',old_point_pair_triple_multiplicity=[72,9,1],
    generic_pair_only_q8_union_upper=513,generic_pair_only_bound_is_correct_but_weaker=True,
    actual_saved585_bound_scope='Bfactorfixedtosavedactual585witholdSteinertriplecertificate',actual_saved585_union_formula='U(a)=72a-9*binom(a,2)+binom(a,3)',
    q8_t8_union_at_most=380,q8_missed_at_least=140,actual_saved585_distinct_external_unowned_classes_at_least=18,targets_per_external_class=8,
    union380_attainment_claimed=False,universal_allGQ8_Steiner_claimed=False,old_source_or_BLOCKS_PORT_R2_tests_repeated=0,
    new_content_only='old585SteinerandBonferroniboundappliedtoproductcap31rowexternalobligation;newliteralq2supportsmallexperiment')
r['distance_text']+=' 继承修订：support72/pair9及triple1的实际585证据在20261027已验Steiner3-(65,9,1)，不是本轮新发现。对固定该actual585为B因子，旧THEOREM三阶Bonferroni U(a)=72a−9C(a,2)+C(a,3)给U8≤380，故漏≥140、每唯一owner类8点需≥18个未owned外援类；上述513只是一般pair-only弱界，在此actualsource应用中由旧强界取代。0旧data/585/BFS重跑，不新计理论/方法；本轮新处为product cap31义务应用与literalq2支持实验。'
r['lesson_and_restart_condition']+=' 优先继承旧premise/theorem可实际加强路线判断：实际585八own类row还需至少18distinct未owned类外援，不是只知≥1；并不据此单独排31或说每helper需9ownpins。matrix一般推导留作解释而非72/9发现成果，Steiner三阶只用于保存的actual585，不泛化所有假想GQ8。旧两Wiki节点只链接，不重导或重跑。'
r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+e))
raw=W/f'updates/{B}_PROVENANCE_ROWS.json';raw.write_text(json.dumps([r],ensure_ascii=False,indent=2)+'\n')
cp=W/f'updates/{B}_HELPER_CALLS.json';calls=json.loads(cp.read_text())
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
gap=W/'gap_map.md';s=gap.read_text();old='factor-overlap纸面SUPPORTED与rootliteral15的32subset/10pair全PASS另记0图/Lean；q8八类pin仍漏≥7点，需≥1外援类，非31排除。';new='factor72/9/triple1继承20261027实际585 Steiner3旧证据，非新发现；旧U8≤380使实际585八own类row漏≥140、需≥18未owned外援类，非31排除。一般matrix纸面复核与新literalq2的32subset/10pair全PASS另记0图/Lean，不重跑旧585数据。';assert old in s;gap.write_text(s.replace(old,new,1))
comment=f'''\n\n### {now} 同一增量的必要继承修订：旧585 Steiner证据，不新计72/9\n\n收到root针对性恢复的旧证据后，本轮[现barrier](experiments/{rid}.md)只链接继承[20261027实际585 Steiner premises](experiments/{oldids[0]}.md)及[同机制旧保边定理](experiments/{oldids[1]}.md)，未创建新实验或方法行。其SOURCE/BLOCKS/PORT_R2已实际验point72/pair9/triple1；本轮不能把72/9当新发现。一般matrix独立纸面推导仍正确，只是解释与fallback，不替代历史credit。\n\n固定B为保存actual585源时，旧THEOREM三阶Bonferroni U(a)=72a−9C(a,2)+C(a,3)在a8给≤380，不只一般pair-only≤513；520非abs至少漏140，每唯一owner类8targets，因此该row至少18个未ownedbasedclasses需外援。380是upper非每8-subset exactsize；这是旧强证据在product-cap31路线义务的新应用，非cap31排除/人人9pins/所有GQ8都有该Steiner证书。新literalq2支持小实验另记，旧585数据/图/BFS/枚举0重跑。148/39/Lean42、ledger420与86/98新A在途等状态完全不变。\n'''
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+comment)
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'Necessaryinheritancecorrectiononly:actual585support72_pair9_Steinertriple1alreadyknown20261027/oldtwoWikiNodeslinked/notnewdiscovery. OldBonferroniU8<=380=>miss>=140/atleast18unownedclassesforthesavedactual585Bfactor;genericpair513correctbutweaker/notuniversalGQ8Steiner/not31exclusion. Newcontentproductcap31routeapplicationandliteralq2smallexperimentonly.0olddata_BFS_tests/newtheoremcounts. Ledger420148_39Lean42unchanged;main86_98receiptamendedwithrealcanonicalprovenanceupsert.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W);cp.write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
rp=W/f'updates/{B}_RECEIPT.json';v=json.loads(rp.read_text());v.update(updated_UTC=now,status='PASS_NEW86_98_ACCEPTED148_39_LEAN42_WITH_OLD585_PROVENANCE_CORRECTION',
    unique_existing_records_updated=2,canonical_upsert_calls=2,provenance_correction_existing_barrier_only=True,old585_support72_pair9_triple1_inherited_not_new=True,
    inherited_old_Wiki_nodes=oldids,actual_saved585_union8_upper=380,actual_saved585_missed_lower=140,actual_saved585_external_class_lower=18,
    generic_pair513_bound_retained_as_weaker=True,new_discovery_or_theorem_count_from72_9=0,old585_data_or_graph_retests=0,
    additional_inherited_paths_checked=7,evidence_paths_checked=65,new_rows=0)
rp.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v[k]for k in ['status','ledger_records','named_legal_graphs','legal_parameter_pairs','complete_formula_Lean','actual_saved585_union8_upper','actual_saved585_missed_lower','actual_saved585_external_class_lower','old585_data_or_graph_retests']},ensure_ascii=False))
