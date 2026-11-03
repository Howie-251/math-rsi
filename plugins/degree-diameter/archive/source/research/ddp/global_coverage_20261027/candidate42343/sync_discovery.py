"""Record the one independently verified instance in the existing Wiki/Goal."""
from pathlib import Path
from datetime import datetime, timezone
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
check=json.loads((HERE/'independent_all_source_BFS.json').read_text())
assert check['valid'] and check['n']==42343 and check['max_degree']==12
assert check['diameter']==5 and check['roots_checked']==42343 and check['bad_unordered_pairs']==0
files=['README.md','parameters.json','generate.py','FINAL_MATH_PROOF.md',
       'graph_d12_D5_n42343.edges','independent_all_source_BFS.json',
       'verify_all.cpp','BASELINE_REFRESH.json','dry_run_structure_check.json']
assert all((HERE/f).exists() for f in files)
row=dict(
 id='ddp-h9-qline-42343', title='完整新图：(12,5)42343，超过实时公开42342门槛',
 family='H9 quadric-line extension',record_type='mathematically-verified-new-lower-bound',
 target_Delta=12,target_D=5,savedL=42342,n=dict(actual=42343,hypothetical=None),
 actual_graph_Delta=12,actual_D=5,
 actual_D_scope='Root independent full42343-source BFS from expanded edge list; all eccentricities5. Mathematical verification complete; Lean incomplete.',
 ordinary_bad_unordered_pairs=0,ordinary_bad_target_D=5,
 scope='Preserve every edge of public42342 graph; append one vertex42342 with a fixed12-neighbor set:10 mandatory pins of an ambientQ-line and2 exact-completion anchors. One generated graph and one independent all-source verification.',
 failure_or_result='n42343,m245229,maxdegree12,connected,simple,Dexact5,badunordered0；全部42343根独立BFS通过。2026-10-27实时官方主表与描述仍42342，数学新下界提高1。尚未Lean、尚未对外发布，Goal ACTIVE。',
 positive_guarantees=[
  'All245217 oldedges preserved plus12newedges; oldneighbors each had degree<=11.',
  'Root independently rebuilt the rawsource graph and checked all42342 oldvertices lie within radius4 of the12pins.',
  'Root rebuilt expanded edge list and ran all42343 ordinary BFS sources: maximum degree12, exactD5,0badpairs,0unreachable.',
  'Deterministic generator dry-run reproduces the exact validated edge set without modifying it.',
  'Official live table and linked description both still report42342; improvement1 and no exact-optimum claim.'],
 unclosed_gap='最终Lean尚未完成；Gemini同线程最终成果审阅在途，实际回执另存。公开投稿/作者联系未进行。已有新图不能据此标整个Goal完成。',
 lesson_and_restart_condition='停止固定7线的剩余搜索：首完整解已满足存在性目标。由675个成功对象恢复Q-line的统一旧覆盖，再做有限degree筛及至多2anchors精确完整补全；不以坏对下降驱动续算。当前优先该新成果的交付、审阅与形式化。',
 outcome_class='MATHEMATICAL_NEW_BOUND_LEAN_PENDING',wiki_verdict='yes',
 other_metrics=dict(new_lower_bound_mathematically_verified=True,
  new_graphs_generated=1,independent_full_BFS_graphs=1,roots_checked=42343,
  checked_n=42343,checked_m=245229,degree_cap=12,exact_D=5,
  all_source_check_CPU_seconds=check['CPU_seconds'],all_source_check_wall_seconds=check['wall_seconds'],
  mandatory_pins=[452,6195,10312,12353,13822,21068,24695,29805,36474,38101],
  anchors=[4633,20168],new_vertex=42342,
  saved_baseline_date='2026-10-26',baseline_refreshed_UTC='2026-10-27 10:39:09 UTC',
  current_public_baseline=42342,improvement=1,Lean_complete=False,
  public_submission=False,Goal_complete=False,
  source_author='Dharunish Yugeswardeenoo; underlying partial fold and duality Rishabh Rajiv',
  mechanism_evidence_node='exp:ddp-h9-global-coverage-20261027'),
 report_paths=[str((HERE/f).relative_to(ROOT)) for f in files])
assert not common['capture'].screen(json.dumps(row,ensure_ascii=False))
(HERE/'wiki_rows.json').write_text(json.dumps(dict(updated_UTC=NOW,row_count=1,rows=[row]),ensure_ascii=False,indent=2)+'\n')
r=common['normalize'](row)
common['write_node'](r)
ledger_path=ROOT/'research-wiki/DDP_METHOD_LEDGER.json'
ledger=json.loads(ledger_path.read_text())
rows=[old for old in ledger['rows'] if old['id']!=r['id']]+[r]
hits=sum(bool(old.get('other_metrics',{}).get('new_lower_bound_mathematically_verified')) for old in rows)
ledger.update(updated_UTC=NOW,record_count=len(rows),rows=rows,new_lower_bounds=hits,
 mathematical_new_lower_bounds=hits,formally_completed_new_lower_bounds=0)
ledger['input_counts']['../global_coverage_20261027/candidate42343/wiki_rows.json']=1
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
page=common['render'](rows)
page=page.replace('## 家族目录','已数学验证：[完整(12,5)42343图](experiments/ddp-h9-qline-42343.md)，超过实时官方42342门槛1点；Lean未完成。\n\n## 家族目录',1)
assert not common['capture'].screen(page)
(ROOT/'research-wiki/DDP_METHOD_LEDGER.md').write_text(page)

focus='''当前已取得第一个数学验收通过的新下界：N(12,5)≥42343。保存完整245229边图，root从展开边表独立全42343源BFS：simple/connected、max12、Dexact5、坏无序对0；2026-10-27实时官方主表与描述仍42342，提升1点。构造为保留Dhar42342全部旧边，加入vertex42342，10个Q-line mandatory pins加anchors4633/20168。675条成功附件的几何识别和统一旧核心覆盖推导实际导出649中心的52569线有限池，degree筛7项，精确≤2anchor补全首项成功；其余6不再搜索。不按坏对下降续轮、不扩中心或加第三anchor。当前优先完成这一新图的审阅、可复现交付和对应Lean；数学成功1、完整形式化0，Goal保持ACTIVE，不能提前标完成。原27格范围及旧D2暂停不变。证据research/ddp/global_coverage_20261027/candidate42343/README.md。'''
assert not common['capture'].screen(focus)
agents=(ROOT/'AGENTS.md').read_text()
oldfocus=next(line for line in agents.splitlines() if line.startswith('当前唯一主线是H9二次曲面直线'))
for rel in ['AGENTS.md','context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md',
            'RESEARCH_BRIEF.md','context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md',
            'research-wiki/gap_map.md']:
 p=ROOT/rel;s=p.read_text();assert oldfocus in s,rel;s=s.replace(oldfocus,focus)
 if rel.endswith('NEXT_SESSION.md'):
  lines=s.splitlines();lines[2]=f'Updated {NOW}. Goal ACTIVE; one mathematical new lower bound, Lean incomplete. Execute RESEARCH_GOAL.md. Old D2 remains paused.'
  s='\n'.join(lines)+'\n';s=s.replace('ledger160条记录','ledger161条记录')
 if rel=='RESEARCH_BRIEF.md':s=s.replace('已验证新下界仍为0。','数学验收新下界1项，完整Lean仍0项。',1)
 p.write_text(s)
goal=ROOT/'context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md'
text=goal.read_text()
text=text.replace('## 9. 最终交付与Lean顺序','## 9. 最终交付与Lean顺序\n\n2026-10-27首次命中：42343点图已通过全源数学验收及实时公开表比较。现在按本节推进该成果对应的形式化和最终审阅；旧公开图本身的合法性须真实绑定，不能用未证公理代替。数学命中不免除Lean要求，不恢复旧D2形式化。',1)
goal.write_text(text)
registry=ROOT/'context/DD_PORTFOLIO_START_20261026/registry/cases.json'
cases=json.loads(registry.read_text())
case=next(c for c in cases['cases'] if c['degree_cap']==12 and c['diameter_cap']==5)
case.update(research_status='MATHEMATICAL_NEW_BOUND_FORMAL_PENDING',
 mathematical_status='N12_5_GE42343_VERIFIED_NOT_EXACT',
 novelty_status='EXCEEDS_REFRESHED_OFFICIAL_TABLE_UNPUBLISHED',
 public_baseline_verified_here=True,baseline_refresh_UTC=NOW,
 refreshed_public_baseline_order=42342,
 local_result=dict(n=42343,m=245229,max_degree=12,diameter=5,
  independent_roots=42343,bad_unordered_pairs=0,Lean_complete=False,
  evidence=str(HERE.relative_to(ROOT))))
registry.write_text(json.dumps(cases,ensure_ascii=False,indent=2)+'\n')
with (ROOT/'research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md').open('a') as f:
 f.write('\n\n## '+NOW+' — 首个完整新图数学验收通过\n\n'+focus+'\n\n这次成果是合法新图，不是坏点对分数改善；用户纠偏实际改变了生成规则。Gemini承重几何审阅已SUCCESS，最终图同线程审阅待回执；Lean具体工作已派发，仅围绕新图，不恢复旧D2。\n')
common['helper'].rebuild_index(str(ROOT/'research-wiki'))
common['helper'].rebuild_query_pack(str(ROOT/'research-wiki'))
(HERE/'WIKI_SYNC_RESULT.json').write_text(json.dumps(dict(updated_UTC=NOW,
 record_count=len(rows),new_lower_bounds=hits,formally_completed_new_lower_bounds=0,
 nodes_upserted=[r['id']],historical_nodes_rewritten=0),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record_count=len(rows),mathematical_hits=hits,formal_hits=0,Goal='ACTIVE'),ensure_ascii=False))
