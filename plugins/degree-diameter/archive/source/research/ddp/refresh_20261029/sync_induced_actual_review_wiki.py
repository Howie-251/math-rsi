"""Record the actual static review, separating the later3600 strengthening."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import importlib.util
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
WIKI=ROOT/'research-wiki'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
prefix=ROOT/'reviews/ddp/f5_induced_geodesic_20261029'
review=json.loads(prefix.with_suffix('.response.json').read_text())['structuredContent']
assert (review['status'],review['model'],review['effort'],review['threadId'])==(
    'SUCCESS','gemini-3.8-flash-high','high','12c1d715-0369-4a25-9755-3fb41033c3bd')
trans=json.loads((HERE/'f5_induced_transversal_deletion/RESULT.json').read_text())
assert trans['theoretical_bad_unordered_pairs_between_fibers0and5_exact']==3600
assert trans['retained_source_counterexamples_per_retained_target_exact']==36
ledger=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert ledger['record_count']==len(ledger['rows'])==374
identifier='ddp-f5-literal3750-induced-retention-max16-d3-20261029'
row=copy.deepcopy(next(r for r in ledger['rows'] if r['id']==identifier)['source_record'])
meta=dict(status='SUCCESS_STATIC_MATH_PASS',actual_model=review['model'],effort=review['effort'],
    thread_id=review['threadId'],original_call_only=True,
    reviewed_transversal_bad_pair_lower_bound=2000,
    reviewed_compressed_closure_specification=True,
    later3600_strengthening_external_reviewed=False,
    complete_CNF_or_solver_or_Lean_or_novelty_certified=False,
    response=str(prefix.with_suffix('.response.json').relative_to(ROOT)),
    disposition=str(prefix.with_suffix('.DISPOSITION.md').relative_to(ROOT)))
for v in row['variants']:
    if v['label']=='full_four_direction_transversal_vertex_deletion_paper_obstruction_20261029':
        v['cross_model_review_status']='SUCCESS_STATIC_MATH_PASS'
        v['actual_static_review']=meta
        v['earlier_bad_pair_lower_bound_reviewed']=2000
        v['theoretical_bad_unordered_pairs_lower_bound']=3600
        v['exact_cross_fiber0_to5_bad_unordered_pairs']=3600
        v['exact_bad_partners_per_retained_target']=36
        v['inclusion_exclusion_parts']=[20,20,4]
        v['later_strengthening_local_independent_static_review']='PASS_PARENT_REPORTED'
        v['later_strengthening_external_reviewed']=False
        v['all3600_pairs_enumerated']=False
    elif v['label']=='all3750_keep_variables_conditional_degree16_unique_geodesic_closure_20261029':
        v['compressed_closure_specification_review']=meta
        v['whole_CNF_independently_certified']=False
    elif v['label']=='one_literal_four_direction_hyperplane_3000_control_20261029':
        v['actual_saved_root_missing_in_fiber5']=36
        v['latest_paper_exact_cross_fiber_bad_pairs']=3600
        v['latest3600_is_global_measurement']=False
row['other_metrics'].update(cross_model_transversal_review_status='SUCCESS_STATIC_MATH_PASS',
    actual_induced_review_thread=review['threadId'],
    transversal_original_reviewed_bad_pair_lower_bound=2000,
    transversal_exact_cross_fiber_bad_pairs=3600,
    transversal_exact_bad_partners_per_retained_target=36,
    transversal_3600_external_reviewed=False,
    transversal_3600_local_independent_static_attack='PASS_PARENT_REPORTED',
    closure_CNF_independently_certified=False)
row['unclosed_gap']='一般>=1921点max16/D3诱导子图仍开放；完整retention必要模型单轮UNKNOWN、0候选，本批停止不续。transversal整域排除与压缩closure规范已实际GeminiPASS；后续跨fiber恰3600加强仅本地独立静态及既有单根fiber5缺36一致，未外审/枚举全部3600。无新合法图或下界。'
if '；实际Gemini静态PASS' not in row['failure_or_result']:
    row['failure_or_result']+='；实际Gemini静态PASS支持原2000下界与压缩closure规范，thread12c1d715-0369-4a25-9755-3fb41033c3bd；后续20+20−4=36给跨fiber恰3600坏对，只是本地加强，不称外审认证全部3600或完整CNF。'
paths=[str(prefix.with_suffix(s).relative_to(ROOT)) for s in ['.prompt.md','.response.json','.DISPOSITION.md']]
row['report_paths']=list(dict.fromkeys(row['report_paths']+paths))
spec=importlib.util.spec_from_file_location('capture_filter',ROOT/'aris_repo/tools/capture_filter.py')
capture=importlib.util.module_from_spec(spec);spec.loader.exec_module(capture)
assert not capture.screen(json.dumps(row,ensure_ascii=False))
pending=HERE/'INDUCED_ACTUAL_REVIEW_WIKI_ROWS.json'
pending.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==374
for k in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
          'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert ledger[k]==after[k]
receipt=dict(status='PASS_INDUCED_ACTUAL_STATIC_REVIEW_AND_LOCAL3600_SCOPE_RECORDED',
    updated_UTC=NOW,existing_id=identifier,record_count=374,actual_review=meta,
    local_exact_cross_fiber_bad_pairs=3600,local_3600_external_reviewed=False,
    new_experiments=0,new_methods=0,new_graphs=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    K2_resume_terminal_not_presumed=True,final_query_rebuild_after_root_update_pending=True,
    helper_stdout=run.stdout.strip())
out=HERE/'INDUCED_ACTUAL_REVIEW_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),record_count=374),ensure_ascii=False))
