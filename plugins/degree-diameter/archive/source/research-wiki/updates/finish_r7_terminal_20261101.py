"""Finish the existing Wiki recovery pointers and record actual helper receipts."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
W = ROOT/'research-wiki'
STEM = 'R7_F11_LOCAL_PUBLIC77_FIXEDM50_M33_TERMINAL_20261101'
rows = json.loads((W/'updates'/f'{STEM}_ROWS.json').read_text())
ids = [r['id'] for r in rows[:4]]
links = [f'experiments/{i}.md' for i in ids]
header = f'''<!-- {STEM} -->
# 当前：六新图审阅完成；F11从局部接口经严格门到四base有限UNKNOWN

同Goal ACTIVE：125合法例／20参数、阶段21图／17参数，具体Lean19，ledger414。U6＋U10六目标A/B/freshC实际齐。新数学终态：三base m50严格失败；四base m33两百万合法样本UNKNOWN、0controller/图、不自动续。全球／首创未认证；冻结四图包119/16/Lean13不改。

[F11局部]({links[0]})：两轨预测被实际四轨110/220/264/330推翻；选132类的264×2+330×5，finalports=[1,4,∞,0,2,3,5]。10真逆chart/360turn/12plane覆盖1331全PASS，.131403188CPU；归一PGL逆反例.000518CPU，不替代真逆。

[公开77门]({links[1]})169750=160000+13×750，仅公开Tallini15×spread及一般复制，非本地160050/O22；F11³需H≥128。[固定三base m50]({links[2]})4802outer全域、32tiling全缺0→1，.919086CPU严格失败；旧mod10 OPEN已覆盖，smaller≤48开放但不自动降模数。

[四base m33]({links[3]})1372词16类min51、B三角；条件H132/175692不计图。一次200万合法global样本终态UNKNOWN，含编译1.822286CPU，0controller/大图/BFS/Lean。首同层失败1962566；代表缺路线已存，非family排除，不自动第二seed/hillclimb。下一机制由root据此决定。

以下为保留历史；恢复时以本段、所链实际TERMINAL及根STAGE_STATE为准。

'''
gap = W/'gap_map.md'
text = gap.read_text()
if not text.startswith(f'<!-- {STEM} -->'):
    gap.write_text(header+text)

human = W/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker = f'<!-- {STEM}_POST_NOTE -->'
if marker not in human.read_text():
    with human.open('a') as f:
        f.write(f'''\n\n{marker}
## 2026-11-01 本轮实测恢复记录：F11预测、严格门与一次有界UNKNOWN

延续用户“先直觉、后构造；有依据扩大样本而不无限坏对微调；及时保存避免重复”的既有意见。本段为执行记录，不新增人工原话或冲突计划。当前仍125合法图／20参数、阶段21／17、具体Lean19；U6＋U10六target实际A/B/freshC均完成，一次联合C逐目标PASS，不算六次外审。四图冻结包仍119／16／13，全球／优先权未认证。

1. 此前不知F11六子集能否像预想264+660两轨。实际四轨110/220/264/330推翻该预测，只有132-profile七子集适用264×2+330×5；因此限定finalports和10真逆chart。360秩/12平面覆盖全PASS(.131403188CPU)。独立反例(.000518141CPU)确认PGL归一逆会错误往返，producer真实逆正确；不重分类。[局部证据]({links[0]})。
2. [公开77门]({links[1]})在一次4primary查询及.020526023CPU标量下，best-located推论169750；只用公开Tallini15/GQ7/spread/一般§7复制。中心含105K2，非独立中心特例。本地160050/O22不充当公开，全球未穷尽；1331纤维需H≥128。
3. [固定三base]({links[2]})symbolic最小50使最高m50成为有限门。26+三8块拆解使4802归一outer完整，32同层tiling全部缺0→1，.919086454CPU。缺pair非邻且继承两步上界847<1331，故该m50 fullfiber严格失败；旧mod10 OPEN只是被覆盖的历史。原smaller evenm≤48和其他七port拓扑开放，但未自动续。
4. 因32个同层可行对象不能同时补跨层路线，实际改为[四base B三角规则]({links[3]})，1372词/16类min51。首competitive m33/H132的175692仅条件目标。一批2000000合法global候选、五单位轨各400000、seed2026110107，全部实际记录；终态UNKNOWN_SAMPLE_CAP_REACHED，含编译1.822285705CPU。首(3,3)失败1962566，37434过首门，最后3止于03。实际代表16类signature和缺residue保存，不能称整族无望/最优坏对；未产controller、17424word证书或大图，0BFS/Lean。

本轮没有新增完整图、Lean或framework。余CPU不自动授权续批，root依据同层首门与跨层缺路线再决定机制；不自动第二seed/hillclimb/模数梯子。保存的是“原预测→反例或实测→改变生成规则→有限返回”的证据链，不以整理文档充当数学成果。
''')

helper = ROOT/'aris_repo/tools/research_wiki.py'
calls = []
def call(*args):
    cmd = [sys.executable, str(helper), *args]
    r = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    calls.append(dict(command=cmd,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr))
    assert r.returncode == 0, calls[-1]

edges = [
    (ids[0], 'ddp-r6-schreier3base-z26-sixport-controller78-complete-a3-20261101', 'extends', 'F11 fixed typed seven-port interface extends inherited successful controller/lift mechanism; no new complete graph.'),
    (ids[1], ids[0], 'uses', 'F11 cube1331 and conditional degree77 determine public threshold; public Tallini15 only.'),
    (ids[2], ids[0], 'uses', 'Fixed actual ten-chart inverse-port interface, missing-threewalk full-fiber obstruction; m50 only.'),
    (ids[2], ids[1], 'uses', 'Public169750 justified finite highest m50 target199650; target was never a graph.'),
    (ids[3], ids[2], 'extends', 'Change three-base to four-base triangle topology after strictm50failure, not automatic lower-modulus ladder.'),
    (ids[3], ids[0], 'uses', 'Retains exact typed inverse-port chart interface and B triangles.'),
    (ids[3], ids[1], 'uses', 'Competitive firstm33/H132 conditional175692; actual bounded2000000UNKNOWN, notfamilyexclusion.'),
]
for source,target,kind,evidence in edges:
    call('add_edge',str(W),'--from','exp:'+source,'--to','exp:'+target,'--type',kind,'--evidence',evidence)
call('log',str(W),'2026-11-01 actualr7local4orbitsrefutes2orbitprediction/10trueinversechartsPASS;public77derived169750Hmin128;fixedthreebasem50all4802outer32tilingsfail01strictclosed;fourbasem33actual2000000legalglobalUNKNOWNcapreached1.822285705CPU,noautomaticretry. Fourlocal/public/gatenodesadded,existingU10nextBupdated,ledger414/125legal20pairs/stage21_17/Lean19unchanged;0newgraph/BFS/Lean/framework,nohash,nooldcheckrerun,frozenpackuntouched.')
call('rebuild_index',str(W))
call('rebuild_query_pack',str(W))
calls_path = W/'updates'/f'{STEM}_HELPER_CALLS.json'
calls_path.write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')

ledger = json.loads((W/'DDP_METHOD_LEDGER.json').read_text())
assert ledger['record_count']==414
assert ledger['validated_named_graph_examples']==125
assert ledger['validated_named_parameter_pairs']==20
assert ledger['complete_Lean_graph_instances']==19
known = {r['id']:r for r in ledger['rows']}
for i in ids:
    assert i in known
    assert known[i]['other_metrics']['new_named_complete_graphs']==0
    assert known[i]['other_metrics']['new_Lean_instances']==0
    assert known[i]['actual_order'] is None

evidence = set(p for r in rows for p in r['evidence_paths'])
assert all((ROOT/p).exists() for p in evidence)
checked = 0
paths = [W/'experiments'/f'{r["id"]}.md' for r in rows]
for p in paths:
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        target = target.strip('<>').split('#',1)[0]
        if not target or re.match(r'\w+://',target):
            continue
        target = unquote(target)
        assert (p.parent/target).exists(), (p,target)
        checked += 1
query = (W/'query_pack.md').read_text()
assert 'ledger414' in query and 'UNKNOWN' in query
assert 'm50' in query and '169750' in query
receipt = dict(updated_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
               status='PASS_UNIQUE_WIKI_R7_ACTUAL_PREDICTION_PUBLIC_GATE_STRICT_M50_M33_UNKNOWN_SAVED',
               ledger_records=414,records_added=4,records_updated=1,named_legal_graphs=125,
               legal_parameter_pairs=20,phase_graphs=21,phase_pairs=17,complete_formula_Lean=19,
               new_complete_graphs=0,new_Lean_instances=0,new_frameworks=0,
               new_node_ids=ids,resolved_evidence_paths=len(evidence),checked_markdown_links=checked,
               actual_helper_calls=str(calls_path.relative_to(ROOT)),query_current=True,
               m50_status='STRICT_FIXED_TOPOLOGY_COMPLETE_DOMAIN_ALL32_FAIL01',
               m33_status='UNKNOWN_SAMPLE_CAP_REACHED_NOT_FAMILY_EXCLUSION',
               m33_legal_candidates=2000000,m33_accounted_CPU_seconds=1.8222857049999996,
               experiments_rerun=0,root_owned_files_modified=False,frozen_expert_packet_modified=False,
               global_record_or_priority_certified=False)
out = W/'updates'/f'{STEM}_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
