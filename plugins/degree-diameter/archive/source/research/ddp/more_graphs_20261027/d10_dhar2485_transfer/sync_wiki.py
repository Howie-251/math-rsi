"""Upsert this focused batch using the existing ARIS Wiki writer and ledger."""
from pathlib import Path
from datetime import datetime, timezone
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
COMMON = runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def row(slug, title, scope, result, lesson, evidence, **extra):
    data = dict(id=slug, title=title, family='metacyclic base voltage constructions',
                record_type='finite-cayley-route-coverage-no-accepted-graph',
                target_Delta=10, target_D=4, savedL=2485,
                n=dict(actual=None, hypothetical=None), actual_D=None,
                actual_graph_Delta=None, ordinary_bad_unordered_pairs=None,
                scope=scope, failure_or_result=result,
                lesson_and_restart_condition=lesson,
                unclosed_gap='未取得此参数的完整新纪录；其它作用、相位及一般图未由此排除。完整Lean实例仍0。',
                outcome_class='COMPLETE_FINITE_SCOPE_NO_NEW_GRAPH', wiki_verdict='no',
                report_paths=[str((HERE/p).relative_to(ROOT)) for p in evidence])
    data.update(extra)
    return data


def main():
    literal = json.loads((HERE/'LITERAL_RESULT.json').read_text())
    q25 = json.loads((HERE/'QUOTIENT25_RESULT.json').read_text())
    assert literal['new_graphs'] == q25['complete_hits'] == 0
    rows = [
        row('ddp-d10-dhar2485-route-intuition-20261027',
            'Dhar2485路线恢复与可推翻预测：原薄层、kernel重合及C25互补',
            'Existing2485 source plus controlledfree-form comparisons at actionorders5/7/35; oneD7to8counterfactual. No oldgraphBFS.',
            '源规范化为phases1/3/6/7/9与[0,r²−1,−r²−1,−r,1]。P1降阶容量直接挡101/113被反驳，实际最小182仍足够；D7强制5阶解释薄层215词/211形式。改C25使BD与ce两组独立变量对进入同一薄phase10。',
            '区分形式数量与数值碰撞；不以kernel重复排整个非faithful族。C25路线互补与余量支持一次固定r25完整参数决策，不支持多作用盲扫。',
            ['REPORT.md','source_analysis/SOURCE.json','source_analysis/SOURCE_PHASES.json',
             'source_analysis/M35_CONTROLS.json','source_analysis/M25_CAPACITY_ONLY.json',
             'counterexample_analysis/RESULT.json','counterexample_analysis/WITNESSES.json'],
            record_type='known-source-and-controlled-route-analysis',
            n=dict(actual=2485,hypothetical=None), actual_graph_Delta=10,
            actual_D=4, actual_D_scope='Inherited already verified public2485 source; no repeated source BFS.',
            wiki_verdict='partial', outcome_class='SOURCE_MECHANISM_RECOVERED_PREDICTION_PARTLY_REFUTED'),
        row('ddp-d10-dhar2485-literal127-20261027',
            'Dhar2485字面迁移：Moore范围唯一mod127对象未覆盖',
            'SameC35phases,sourcefiveintegertranslations,literalr2;all72<=modulus<=234 satisfying2^35=1. Exactlymod127.',
            '4445点对象代表根≤4缺644端点；未导出边表，实际D及普通无序坏对保持null。',
            '仅关闭字面r2及整数平移规则，不排其它平移、作用或商。',
            ['EXPERIMENT_PLAN.md','LITERAL_RESULT.json','literal_transfer.py'],
            n=dict(actual=None,hypothetical=4445), other_metrics=dict(
                complete_moduli=[127],representative_root_R4_missing=644,
                raw_words_by_length=[1,10,90,810,7290],
                CPU_seconds=literal['CPU_seconds'],old_source_BFS=0,new_graphs_generated=0)),
        row('ddp-d10-dhar-source25-quadratic101-20261027',
            'C25/F101源二次规则20作用：薄层预测支持，完整覆盖无命中',
            'ExactlyC25/F101,phases1/3/6/7/9,translations[0,r²−1,−r²−1,−r,1];all20primitive25actions.',
            'P2最薄路线数>215得到支持：实际308。20项全部检查25层，代表根R4遗漏52..192；0完整新图，未测普通全图坏对或实际D。',
            '词数余量确实改善，固定多项式同时绑住两组补位变量却仍失败；选maxminfreecapacity的最小r25，只作一个完整射影参数决策，不按最少遗漏选r80。',
            ['QUOTIENT25_PREDICTION.json','QUOTIENT25_RESULT.json','quotient25.py','EXPERIMENT_CODE_REVIEW.md'],
            n=dict(actual=None,hypothetical=2525), other_metrics=dict(
                complete_action_count=20,min_raw_word_count=308,
                route_count_prediction_supported=True,new_graphs_generated=0,
                representative_root_missing_min=52,representative_root_missing_max=192,
                CPU_seconds=q25['CPU_seconds'],old_source_BFS=0))]
    free_path = HERE/'free_translation_r25/RESULT.json'
    if free_path.exists():
        free = json.loads(free_path.read_text())
        # Only final decisions enter this batch ledger; the raw result is preserved verbatim.
        rows.append(row('ddp-d10-source25-free-r25-20261027',
            'C25/F101/r25固定作用的完整射影连接系数检验',
            'FixedC25/F101/r25andphases1/3/6/7/9;A0bycommonconjugation,nonzeroB/C/D/Eup-to-common-scalar. Exactscope/result in rawJSON.',
            f"全部{free['evaluated_candidates']}项结束，未试{free['untested_candidates']}，UNKNOWN0，完整命中{free['full_hits']}；{free['thin_phase_full']}项修好薄phase10却在其它层失败。总编译/运行4.083CPU秒。无新图，无普通坏对或实际D数值。",
            '按固定全范围终态重新评估；不自动扩其它作用/商/seed，也不把未知或有限未命中扩大为整个构造族不存在。',
            ['REPORT.md','free_translation_r25/RESULT.json','free_translation_r25/PREDICTION.json'],
            n=dict(actual=None,hypothetical=2525),other_metrics=free))
    assert not COMMON['capture'].screen(json.dumps(rows,ensure_ascii=False))
    normalized=[]
    for raw in rows:
        item=COMMON['normalize'](raw)
        item['goal']['baseline_date']='2026-10-27'
        COMMON['write_node'](item)
        normalized.append(item)
    path=ROOT/'research-wiki/DDP_METHOD_LEDGER.json'
    ledger=json.loads(path.read_text())
    replace={r['id']:r for r in normalized}
    allrows=[replace.pop(r['id'],r) for r in ledger['rows']]+list(replace.values())
    ledger.update(updated_UTC=NOW,rows=allrows,record_count=len(allrows))
    ledger['input_counts']['../more_graphs_20261027/d10_dhar2485_transfer/wiki_rows.json']=len(rows)
    path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
    page=COMMON['render'](allrows).replace('## 家族目录',
        '当前最强数学结果：N(11,5)≥37631，N(12,5)≥42398，共59个完整阶数例子、2个改进参数对；完整Lean实例0。Goal ACTIVE。\n\n## 家族目录',1)
    (ROOT/'research-wiki/DDP_METHOD_LEDGER.md').write_text(page)
    COMMON['helper'].rebuild_index(str(ROOT/'research-wiki'))
    COMMON['helper'].rebuild_query_pack(str(ROOT/'research-wiki'))
    (HERE/'wiki_rows.json').write_text(json.dumps(dict(updated_UTC=NOW,rows=rows),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(upserted=[r['id'] for r in normalized],ledger_records=len(allrows)),ensure_ascii=False))


if __name__=='__main__':
    main()
