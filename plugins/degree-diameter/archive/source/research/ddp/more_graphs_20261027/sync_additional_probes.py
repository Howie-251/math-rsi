"""Upsert only the supplied completed probe notes through the existing ARIS helper."""
from pathlib import Path
import contextlib
import json
import runpy
import sys

ROOT=Path(__file__).resolve().parents[3]
WIKI=ROOT/'research-wiki'
source=Path(sys.argv[1]).resolve()
rawrows=json.loads(source.read_text())
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
ledger=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
existing={r['id']:r for r in ledger['rows']}
with source.with_suffix('.sync.log').open('w') as log,contextlib.redirect_stdout(log):
    for raw in rawrows:
        r=common['normalize'](raw)
        if raw.get('baseline_date'):
            r['goal']['baseline_date']=raw['baseline_date']
        assert r['evidence_paths'], r['id']
        common['write_node'](r)
        existing[r['id']]=r
    common['helper'].rebuild_index(str(WIKI))
    common['helper'].rebuild_query_pack(str(WIKI))
rows=list(existing.values())
hits={(r['goal']['Delta'],r['goal']['D']) for r in rows if r['other_metrics'].get('new_lower_bound_mathematically_verified')}
examples={(r['goal']['Delta'],r['goal']['D'],n) for r in rows if r['other_metrics'].get('new_lower_bound_mathematically_verified') for n in r['other_metrics'].get('example_orders',[])}
# Keep the historical confirmed-public-table counters backward compatible.
# A fully checked literal graph can have unresolved latest-global novelty; that
# is a separate mathematical-validity axis, never a fourth confirmed record cell.
validated_examples=examples|{(r['goal']['Delta'],r['goal']['D'],n)
    for r in rows if r['other_metrics'].get('mathematically_validated_complete_graph')
    for n in r['other_metrics'].get('validated_example_orders',[])}
# A single mechanism experiment can contain accepted terminal graphs at more
# than one parameter pair. Keep their explicit parameters instead of assigning
# every instance the aggregate row's (possibly None) degree.
validated_examples|={(g['Delta'],g['D'],g['n'])
    for r in rows for g in r['other_metrics'].get('validated_graph_instances',[])
    if g.get('mathematically_validated_complete_graph')}
validated_pairs={(d,D) for d,D,n in validated_examples}
# A valid graph already smaller than a checked public construction is a known
# nonrecord, rather than an unresolved novelty candidate.
nonrecord_examples={(g['Delta'],g['D'],g['n'])
    for r in rows for g in r['other_metrics'].get('validated_graph_instances',[])
    if g.get('known_nonrecord') and g.get('mathematically_validated_complete_graph')}
nonrecord_examples&=validated_examples
assert not (nonrecord_examples&examples)
nonrecord_pairs={(d,D) for d,D,n in nonrecord_examples}
# Current public comparison is a separate axis from the historical saved-table
# comparison. A graph can improve the saved table and already be dominated by
# a larger public graph; these two sets must therefore be allowed to overlap.
publicly_dominated_examples=nonrecord_examples|{(r['goal']['Delta'],r['goal']['D'],n)
    for r in rows for n in r['other_metrics'].get('known_publicly_dominated_example_orders',[])}
publicly_dominated_examples|={(g['Delta'],g['D'],g['n'])
    for r in rows for g in r['other_metrics'].get('validated_graph_instances',[])
    if g.get('known_publicly_dominated') and g.get('mathematically_validated_complete_graph')}
publicly_dominated_examples&=validated_examples
publicly_dominated_pairs={(d,D) for d,D,n in publicly_dominated_examples}
dominated_saved_table_examples=publicly_dominated_examples&examples
pending_examples=validated_examples-examples-nonrecord_examples
pending_pairs={(d,D) for d,D,n in pending_examples}
formal_examples={(r['goal']['Delta'],r['goal']['D'],n)
    for r in rows if r['other_metrics'].get('complete_Lean_graph_instance')
    for n in r['other_metrics'].get('validated_example_orders',[])}
formal_examples|={(g['Delta'],g['D'],g['n'])
    for r in rows for g in r['other_metrics'].get('validated_graph_instances',[])
    if g.get('complete_Lean_graph_instance')}
formal_confirmed_examples=formal_examples&examples
ledger.update(rows=rows,record_count=len(rows),updated_UTC=common['NOW'],
              new_lower_bounds=len(hits),mathematical_new_lower_bounds=len(hits),
              mathematically_improved_parameter_pairs=len(hits),valid_new_graph_examples=len(examples),
              confirmed_publictable_graph_examples=len(examples),
              confirmed_publictable_improved_parameter_pairs=len(hits),
              saved_main_table_improvement_graph_examples=len(examples),
              saved_main_table_improvement_parameter_pairs=len(hits),
              confirmed_publictable_scope='Comparison against preserved saved-main-table values at their recorded dates; not a certification of latest global records.',
              validated_graph_examples_including_novelty_pending=len(validated_examples),
              validated_parameter_pairs_including_novelty_pending=len(validated_pairs),
              validated_named_graph_examples=len(validated_examples),
              validated_named_parameter_pairs=len(validated_pairs),
              validated_nonrecord_graph_examples=len(nonrecord_examples),
              validated_nonrecord_parameter_pairs=len(nonrecord_pairs),
              validated_nonrecord_parameters=sorted([list(p) for p in nonrecord_pairs]),
              validated_nonrecord_instances=[dict(Delta=d,D=D,n=n) for d,D,n in sorted(nonrecord_examples)],
              validated_nonrecord_scope='Compatibility fields count explicitly classified nonrecord examples outside the saved-main-table-improvement set only; not all publicly dominated project examples. See known_publicly_dominated_* for the full currently established comparison set.',
              known_publicly_dominated_graph_examples=len(publicly_dominated_examples),
              known_publicly_dominated_parameter_pairs=len(publicly_dominated_pairs),
              known_publicly_dominated_parameters=sorted([list(p) for p in publicly_dominated_pairs]),
              known_publicly_dominated_instances=[dict(Delta=d,D=D,n=n) for d,D,n in sorted(publicly_dominated_examples)],
              known_publicly_dominated_also_saved_table_improvement_examples=len(dominated_saved_table_examples),
              known_publicly_dominated_scope='Accepted named graph instances with an explicitly checked larger public construction. May overlap confirmed saved-main-table improvements. This field does not certify global novelty of any other parameter or graph.',
              novelty_pending_valid_graph_examples=len(pending_examples),
              novelty_pending_parameter_pairs=len(pending_pairs),
              novelty_pending_parameters=sorted([list(p) for p in pending_pairs]),
              pending_outside_saved_table_graph_examples=len(pending_examples),
              pending_outside_saved_table_parameter_pairs=len(pending_pairs),
              pending_outside_saved_table_parameters=sorted([list(p) for p in pending_pairs]),
              novelty_pending_scope='Compatibility novelty_pending_* fields concern accepted named graphs outside the saved-main-table-improvement set only. Historical table-relative improvements are not thereby certified as global records.',
              complete_Lean_graph_instances=len(formal_examples),
              complete_deterministic_formula_Lean_graph_instances=len(formal_examples),
              confirmed_publictable_complete_Lean_graph_instances=len(formal_confirmed_examples),
              formally_completed_new_lower_bounds=len({(d,D) for d,D,n in formal_confirmed_examples}),
              formal_count_scope='Complete fixed deterministic-formula Lean graph witnesses; literal edge-text parsing equality and exact regularity are separate fields. Historical confirmed-public-table graph formal count remains separate.',
              graph_count_scope='Legacy valid_new_graph_examples/improved and confirmed_publictable_* counters track improvements over preserved saved-main-table baselines, not current global records. validated_named_* counts all accepted named graphs. Current publicly dominated examples form a separate, possibly overlapping set. Compatibility nonrecord/pending fields only classify examples outside the saved-table-improvement set; neither they nor the table counters certify current global novelty of the old11/12 families.')
ledger['input_counts'][str(source.relative_to(ROOT))]=len(rawrows)
(WIKI/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
page=common['render'](rows)
page=page.replace(f'本Goal已数学验证新下界{len(hits)}项；Lean与正式交付状态分列。',
    f'超过保存主表基线{len(hits)}参数／{len(examples)}例；数学合法共{len(validated_examples)}例／{len(validated_pairs)}参数。已知被更大公开构造超过{len(publicly_dominated_examples)}例（其中{len(dominated_saved_table_examples)}例同时超过保存主表）；保存主表外新颖性待核{len(pending_examples)}例／{len(pending_pairs)}参数。完整具体公式图Lean{len(formal_examples)}例。以上主表计数不是全球纪录认证，旧11/12参数的全球状态不由此推定。',1)
assert not common['capture'].screen(page)
(WIKI/'DDP_METHOD_LEDGER.md').write_text(page)
print(json.dumps(dict(record_count=len(rows),records_written=len(rawrows),
    valid_new_graph_examples=ledger['valid_new_graph_examples'],
    validated_graph_examples_including_novelty_pending=len(validated_examples),
    validated_parameter_pairs_including_novelty_pending=len(validated_pairs),
    complete_Lean_graph_instances=len(formal_examples),
    confirmed_publictable_improved_parameter_pairs=len(hits),experiments_rerun=0)))
