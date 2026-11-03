"""Project-specific Wiki backfill. No experiment or validation is rerun."""
from pathlib import Path
from datetime import datetime, timezone
import importlib.util
import contextlib
import io
import json
import re

ROOT = Path(__file__).resolve().parents[3]
WORK = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'

def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'aris_repo/tools' / (name+'.py'))
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

helper = module('research_wiki')
capture = module('capture_filter')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def load_rows(name):
    obj = json.loads((WORK / name).read_text())
    return obj['rows'] if isinstance(obj, dict) else obj

def evidence_paths(items):
    paths = []
    parent = None
    for item in items:
        expanded = [item]
        if '{' in item and '}' in item:
            before, rest = item.split('{', 1)
            middle, after = rest.split('}', 1)
            expanded = [before+x+after for x in middle.split(',')]
        for value in expanded:
            for piece in value.split(';'):
                piece = piece.strip()
                if not piece:
                    continue
                options = [piece]
                if '.md/json' in piece:
                    options += [piece.replace('.md/json', '.md'), piece.replace('.md/json', '.json')]
                for option in options:
                    path = Path(option)
                    if not (ROOT/path).exists() and parent is not None:
                        path = parent/path
                    if (ROOT/path).exists():
                        paths.append(str(path))
                        parent = path if (ROOT/path).is_dir() else path.parent
                        break
    return list(dict.fromkeys(paths))

def normalize(r):
    recent = isinstance(r.get('n'), dict)
    rid = r.get('matched_existing_id') or r.get('wiki', {}).get('matched_existing_id') or r['id']
    rid = re.sub(r'[^a-z0-9._-]+', '-', rid.removeprefix('exp:').lower()).strip('-')
    goal = dict(Delta=r.get('target_Delta') if recent else r.get('target', {}).get('Delta'),
                D=r.get('target_D') if recent else r.get('target', {}).get('D'),
                savedL=r.get('savedL'), baseline_date='2026-10-26')
    actual = r.get('n', {}).get('actual') if recent else r.get('n')
    hypothetical = r.get('n', {}).get('hypothetical') if recent else None
    kind = r.get('record_type') if recent else r.get('object_type', 'unspecified')
    if not recent and kind == 'necessary_or_symbolic_model':
        hypothetical, actual = actual, None
    scope = r.get('scope') if recent else r.get('scope_closed_or_remaining_raw', '')
    degree = r.get('actual_graph_Delta')
    diameter = r.get('actual_D') if recent else r.get('actualD')
    dscope = r.get('actual_D_scope') if recent else r.get('actualD_source', '')
    control = 'controller' in (kind or '').lower() or 'controller' in (dscope or '').lower() or '控制器' in (dscope or '')
    if control:
        level = 'controller'
    elif any(x in (kind or '').lower() for x in ['source', 'baseline']):
        level = 'known_source_or_recovery'
    elif actual is not None:
        level = 'candidate_graph_or_family'
    else:
        level = kind or 'no_final_graph'
    bad = r.get('ordinary_bad_unordered_pairs') if recent else r.get('bad_pair_count')
    badtype = 'ordinary_unordered_pairs' if recent and bad is not None else r.get('bad_pair_count_type')
    other = dict(r.get('other_metrics', {}))
    if r.get('intended_final_target'):
        other['intended_final_target'] = r['intended_final_target']
    if r.get('superseding_existing_wiki'):
        other['superseding_existing_wiki'] = r['superseding_existing_wiki']
    distance = r.get('distance_text') or r.get('failure_or_result') or r.get('metrics_raw', '')
    evidence = evidence_paths(r.get('report_paths', []) + r.get('evidence_paths', []) + r.get('evidence', []))
    if not evidence and r.get('primary_source_directory'):
        evidence = [r['primary_source_directory']]
    margin = actual-goal['savedL'] if level == 'candidate_graph_or_family' and isinstance(actual, int) and isinstance(goal['savedL'], int) else None
    return dict(id=rid, title=r['title'], method_family=r.get('family') or r.get('idea_family', 'DDP'),
                goal=goal, object_level=level, actual_order=actual, hypothetical_order=hypothetical,
                actual_degree=degree, actual_diameter=diameter, diameter_scope=dscope,
                order_margin=margin, diameter_excess=diameter-goal['D'] if level=='candidate_graph_or_family' and isinstance(diameter,int) and isinstance(goal['D'],int) else None,
                bad_pair_count=bad, bad_pair_count_type=badtype,
                ordinary_bad_target_D=r.get('ordinary_bad_target_D'), other_metrics=other,
                distance_text=distance, status=r.get('outcome_class') or r.get('status', 'recorded'),
                exact_scope=scope, positive_guarantees=r.get('positive_guarantees', []),
                remaining_gap=r.get('unclosed_gap', ''),
                lesson=r.get('lesson_and_restart_condition') or r.get('reuse_hint_raw') or r.get('reasoning_raw',''),
                restart_condition=r.get('restart_condition'), variants=r.get('variants', []),
                evidence_paths=evidence, wiki_path=f'research-wiki/experiments/{rid}.md',
                existing_wiki=r.get('existing_wiki_path'),
                idea_id=r.get('idea_family') or 'idea:ddp-breadth-20261027',
                source_record=r, updated_UTC=NOW)

def safe(s):
    return str(s).replace('|', '／').replace('\n', ' ')

def gap_text(r):
    parts = []
    if r['actual_diameter'] is not None:
        parts.append(f"实际D={r['actual_diameter']}" + (f"，目标D={r['goal']['D']}" if r['goal']['D'] else ''))
    if r['bad_pair_count'] is not None:
        label = '普通无序坏对' if r['bad_pair_count_type']=='ordinary_unordered_pairs' else '原报告bad（类型见详情）'
        parts.append(f"{label}={r['bad_pair_count']}")
    if r['other_metrics'].get('new_old_bad_pairs') is not None:
        parts.append(f"新旧坏对={r['other_metrics']['new_old_bad_pairs']}，只验新根")
    if r['diameter_scope']:
        parts.append(str(r['diameter_scope']))
    parts.append(r['distance_text'])
    for update in r['other_metrics'].get('superseding_existing_wiki', []):
        parts.append('后续结果优先：'+str(update.get('path'))+'；'+str(update.get('note')))
    return '；'.join(str(x) for x in parts if x)

def goal_text(r):
    g = r['goal']
    multi = r['source_record'].get('target_is_multivalued') or (g['Delta'] is None and any(v.get('target_Delta') is not None for v in r['variants']))
    if multi:
        items = [f"{v.get('label',v.get('id','变体'))}→{v.get('target') or [v.get('target_Delta'),v.get('target_D')]}／L={v.get('savedL')}" for v in r['variants'] if v.get('target') or v.get('target_Delta') is not None]
        target = '多目标：'+'；'.join(items)+'（逐变体，不合成一个距离）'
    else:
        target = f"({g['Delta'] or '?'},{g['D'] or '?'})；L={g['savedL'] if g['savedL'] is not None else '不适用／见变体'}"
    if r['actual_order'] is not None:
        target += f"；{r['object_level']} n={r['actual_order']}"
    if r['hypothetical_order'] is not None:
        target += f"；条件性n={r['hypothetical_order']}（未据此计纪录）"
    if r['other_metrics'].get('intended_final_target'):
        target += '；意图最终提升：'+str(r['other_metrics']['intended_final_target'])
    extra = []
    for v in r['variants']:
        if not isinstance(v, dict):
            continue
        item = v.get('target') or v.get('target_case')
        if item is None and ('target_degree_cap' in v or 'target_degree' in v):
            item = dict(Delta=v.get('target_degree_cap', v.get('target_degree')),
                        D=v.get('target_diameter', v.get('target_D')),
                        savedL=v.get('target_baseline', v.get('target_saved')))
        if item is not None and item not in extra:
            extra.append(item)
    if extra and not r['source_record'].get('target_is_multivalued'):
        target += '；从属目标：'+str(extra)
    if r['other_metrics'].get('targets'):
        target += '；多目标：'+str(r['other_metrics']['targets'])
    return target

def write_node(r):
    oldpath = ROOT / r['wiki_path']
    meta = helper._load_paper_frontmatter(oldpath) if oldpath.exists() else {}
    original = r['source_record']
    metrics = '\n\n'.join([
        '**对象层级：** '+r['object_level'], '**目标与阶数：** '+goal_text(r),
        '**距目标的证据：** '+gap_text(r),
        '**其他指标（保持原计数类型）：**\n```json\n'+json.dumps(r['other_metrics'], ensure_ascii=False, indent=2)+'\n```'
        if r['other_metrics'] else '',
        '**既有原文指标：** '+original.get('metrics_raw','') if original.get('metrics_raw') else '',
        '**从属变体：**\n```json\n'+json.dumps(r['variants'], ensure_ascii=False, indent=2)+'\n```' if r['variants'] else '',
        '**原始证据：** '+'；'.join(f'[{p}](../../{p})' for p in r['evidence_paths']),
        '**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。'
    ])
    reasoning = '\n\n'.join(x for x in [
        '**实际范围：** '+str(r['exact_scope']),
        '**正向保证：** '+'；'.join(r['positive_guarantees']) if r['positive_guarantees'] else '',
        '**仍未完成：** '+str(r['remaining_gap']) if r['remaining_gap'] else '',
        '**启发与重启依据：** '+str(r['lesson']),
        '**单独的重启条件：** '+str(r['restart_condition']) if r['restart_condition'] else '',
        '有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。'
    ] if x)
    assert not capture.screen(metrics), (r['id'], capture.screen(metrics))
    assert not capture.screen(reasoning), (r['id'], capture.screen(reasoning))
    partial = any(word in r['status'].lower() for word in ['positive-local', 'source-recovery', 'unknown', 'tool-ready', 'unexecuted-source'])
    verdict = meta.get('verdict') or original.get('wiki_verdict') or ('partial' if partial else 'no')
    idea = meta.get('idea_id') or r['idea_id']
    oldtags = json.loads(meta.get('tags', '[]'))
    helper.add_experiment(str(WIKI), slug=r['id'], title=r['title'], idea=idea,
        verdict=verdict, confidence=meta.get('confidence','high'),
        date=meta.get('date') or original.get('date') or '2026-10-27',
        hardware=meta.get('hardware') or original.get('hardware_raw',''),
        duration=meta.get('duration') or original.get('duration_raw',''),
        metrics=metrics, reasoning=reasoning,
        provenance='; '.join(r['evidence_paths']), tags=list(dict.fromkeys(oldtags+['ddp','method-ledger'])), update_on_exist=True)

def render(rows):
    mathematical_hits = len({(r['goal']['Delta'], r['goal']['D']) for r in rows
                             if r.get('other_metrics', {}).get('new_lower_bound_mathematically_verified')})
    lines = ['# 已尝试构造与目标差距', '', f'更新：{NOW}。本Goal已数学验证新下界{mathematical_hits}项；Lean与正式交付状态分列。', '',
        '本账本覆盖当前 Degree/Diameter Portfolio；旧 D2/DD82 实验保留在原节点，仅作为暂停历史。每条是实验、变体或工具/来源记录，不等于一种独立方法。', '',
        '先读本页说明和家族目录，再按机制、参数检索对应条目；不必把整页反复装入上下文。完整字段在 [机器账本](DDP_METHOD_LEDGER.json)，每项链接到独立实验节点和原始证据。', '',
        '## 怎样读“距离”', '',
        '- n超过基线但直径不达标，仍不是新下界；基线均标保存日期，正式纪录前重新核对公开来源。',
        '- 控制器、条件性大图、完整候选、部分状态和已知源分层记录。控制器阶数不能直接与最终图基线相减。',
        '- 普通无序坏对、NB有序缺项、代表状态缺项、容量不足分列；原文未标单位时保留“待核”，不猜成无序数。',
        '- 无图、UNKNOWN、局部满秩不填作目标图的实际直径；仅两新根BFS会明确写核验范围。',
        '- 严格排除范围不重跑；小样本、局部搜索及UNKNOWN不作整族无望。有具体预测、运行反馈或有效新规则时可在明确预算下深入，不以未成功或总坏对减少自动无限续算。', '',
        '## 从失败中保留的启发', '',
        '唯一短路/端点容量不足无法靠同一模板的标量调参补救；应先改变路线重数、内部边或生成结构。局部路由满秩仍需全局控制点覆盖；不同chart的pencil修补不能混用。', '',
        '方向类等不变量可在大图搜索前排除整族。加边能保留旧近端覆盖，但远端所有类别仍要核对；匹配路径可能用两条新边。R4/R3双点互助是不同于旧单点的覆盖条件。', '',
        '旧报告中的“8”指8个起始方案，旧单点已用满11/12邻居；不是发现一个尚未用满的度数预算。', '',
        '## 家族目录', '']
    families = sorted({r['method_family'] for r in rows})
    for i,family in enumerate(families,1):
        lines.append(f'- [{family}](#family-{i})')
    for i,family in enumerate(families,1):
        lines += ['',f'<a id="family-{i}"></a>',f'## {family}', '', '| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |', '|---|---|---|---|']
        for r in rows:
            if r['method_family'] != family: continue
            node = 'experiments/'+r['id']+'.md'
            evidence = next((x for x in r['evidence_paths'] if (ROOT/x).exists()), None)
            detail = f'[原始证据](../{evidence})' if evidence else '原始证据见节点'
            limits = str(r['exact_scope'])+'；'+str(r['lesson'])
            lines.append('| '+f'[{safe(r["title"])}]({node})'+ ' | '+safe(goal_text(r))+' | '+safe(gap_text(r))+' | '+safe(limits)+'；'+detail+' |')
    lines += ['', '## 计数与来源', '', f'本页有{len(rows)}条记录；不以此宣称{len(rows)}种独立方法。原有整轮聚合节点继续保留作历史索引，逐项结果以本账本和对应实验节点为准。', '']
    return '\n'.join(lines)

def main():
    inputs = ['legacy_rows.json', 'early_wave_rows.json', 'recent_rows.json', 'current_wave9_rows.json']
    inputs += ['../'+str(path.relative_to(WORK.parent)) for path in sorted(WORK.parent.glob('breadth_*/wiki_rows.json'))]
    merged = {}
    input_counts = {}
    for filename in inputs:
        source = load_rows(filename)
        input_counts[filename] = len(source)
        for original in source:
            row = normalize(original)
            if row['id'] in merged:
                previous = merged[row['id']]
                row['source_record']['previous_ledger_record'] = previous['source_record']
                row['evidence_paths'] = list(dict.fromkeys(row['evidence_paths']+previous['evidence_paths']))
                for key in ['metrics_raw', 'reasoning_raw', 'wiki_verdict', 'date', 'hardware_raw', 'duration_raw']:
                    if key not in row['source_record'] and key in previous['source_record']:
                        row['source_record'][key] = previous['source_record'][key]
            merged[row['id']] = row
    rows = list(merged.values())
    before = {p.stem for p in (WIKI/'experiments').glob('ddp-*.md')}
    for row in rows:
        assert row['id'] == re.sub(r'[^a-z0-9._-]+', '-', row['id'].lower()).strip('-')
        assert any((ROOT/p).exists() for p in row['evidence_paths']), row['id']
        assert not capture.screen(json.dumps(row, ensure_ascii=False)), row['id']
        if row['object_level'] == 'controller':
            assert row['order_margin'] is None
    with (WORK/'sync.log').open('w') as log, contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
        for row in rows:
            write_node(row)
    ledger = dict(updated_UTC=NOW, scope='DD Portfolio; paused DD82 retained separately in the same Wiki',
                  record_count=len(rows), new_lower_bounds=0,
                  counting_note='Records include experiments, subordinate variants, controllers, tools and source recovery; not independent method count.',
                  input_counts=input_counts, rows=rows)
    (WIKI/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+'\n')
    page = render(rows)
    assert not capture.screen(page)
    (WIKI/'DDP_METHOD_LEDGER.md').write_text(page)
    result = dict(updated_UTC=NOW, record_count=len(rows), input_counts=input_counts,
                  new_nodes=sum(r['id'] not in before for r in rows),
                  existing_nodes_updated=sum(r['id'] in before for r in rows),
                  all_nodes_exist=all((ROOT/r['wiki_path']).exists() for r in rows),
                  graph_experiments_rerun=0)
    (WORK/'SYNC_RESULT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    main()
