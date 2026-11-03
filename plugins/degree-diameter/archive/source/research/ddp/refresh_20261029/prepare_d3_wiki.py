"""Prepare the completed D3 controls as one source update and one family record.

Reads saved results only. The actual source/controller/field experiments are never
executed by this persistence script.
"""
from pathlib import Path
import copy
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "aris_repo/tools"))
import capture_filter

WIKI = ROOT / "research-wiki"
ledger = json.loads((WIKI / "DDP_METHOD_LEDGER.json").read_text())
source_id = "ddp-wave4-mizuno-d3-source"
source = copy.deepcopy(next(r["source_record"] for r in ledger["rows"] if r["id"] == source_id))
f5dir = HERE / "f5_complementary_triples"
parallel = HERE / "controller33_parallel_triangle"
deranged = HERE / "controller33_deranged_attachment"
f5 = json.loads((f5dir / "RESULT.json").read_text())
nb3 = json.loads((f5dir / "ROOT_NB3_BINDING.json").read_text())
p = json.loads((parallel / "RAW_ANALYSIS_FIELDS.json").read_text())
d = json.loads((deranged / "RAW_ANALYSIS_FIELDS.json").read_text())
common_paths = [
    "research/ddp/refresh_20261029/DERIVATION_PACKAGE.md",
    "reviews/ddp/refresh_f5_complementary_20261029.prompt.md",
    "reviews/ddp/refresh_f5_complementary_20261029.response.json",
    "reviews/ddp/refresh_f5_complementary_20261029.DISPOSITION.md",
]
def pathstr(path):
    return str(path.relative_to(ROOT))

f5paths = [pathstr(f5dir / x) for x in [
    "PREDICTION.json", "RESULT.json", "MATRICES_AND_PENCILS.json", "PROOF_SCOPE.md",
    "REPORT.md", "ROOT_NB3_BINDING.json", "check_local.py", "TERMINAL.json"]] + common_paths

variant_label = "fixed_F5_complementary_triples_and_adjacent_pencils_20261029"
variant = dict(label=variant_label, target_Delta=20, target_D=3, target=[20,3],
    savedL=None, n=dict(actual=None, hypothetical=3750),
    actual_graph_Delta=None, actual_D=None, ordinary_bad_unordered_pairs=None,
    source_controller_n=30, controller_darts=120,
    local_prediction="SUPPORTED", central_turns=36, full_rank_turns=36,
    translated_pencil_checks=500, pencil_union=125,
    local_CPU_seconds=f5["cpu_seconds"],
    independent_saved_controller_NB3_binding=dict(
        status=nb3["status"], walks=1080, cached_cells_matched=900,
        required_nonadjacent_or_equal_pairs=780, required_minimum=1,
        diagonal_counts=[2], CPU_seconds=nb3["CPU_seconds"]),
    total_local_plus_binding_CPU_seconds=f5["cpu_seconds"]+nb3["CPU_seconds"],
    actual_field_graphs=0, graph_BFS=0, source_BFS=0, solver_calls=0,
    conditional_certificate="Specified source30 line relation would be simple20regular/3750/D<=3; no literal field graph exported or independently checked.",
    baseline_status="Degree20/D3 current public comparison not bound; not a record claim.",
    review="ACCEPT_WITH_QUALIFICATIONS; only F5 local/simultaneous-edge/conditional-certificate scope.",
    review_erratum="Suggested NB3 formula A(A^2-D+I) is incorrect and was not adopted. Root directly counted1080 walks; for d-regular simple graphs the correct count is A^3-(2d-1)A.",
    public_novelty="unresolved", complete_Lean_graph_instances=0,
    evidence_paths=f5paths)
source["id"] = source_id
source["matched_existing_id"] = source_id
source["title"] = "Mizuno D3 source: inherited F3 modes and a fixed F5 complementary-pencil control"
source["variants"] = [v for v in source.get("variants",[]) if v.get("label") != variant_label] + [variant]
source["other_metrics"]["F5_positive_control_20261029"] = variant
source["other_metrics"]["new_lower_bound_mathematically_verified"] = False
scope = " 2026-10-29在同一source30 controller/原inverse-port约定上追加唯一F5互补三方向控制；不重算原1920图，原q3/31scope保留。"
result = " 新F5固定四矩阵36/36中央转向rank3，4port×125=500平移pencil均union125；120dart真逆绑定，780所需controller对有NB3。local CPU0.059301383；root随后直接枚1080controller walks，与cached900计数全MATCH，另CPU0.001809612，非图BFS。条件3750/20reg/D3规则成立但无边表／当前20度公开比较，不报新纪录。"
lesson = " F5正对照说明局部转向与六平面可共同实现；不是F4约束消失，也不证明任何33控制器可用。实际外审ACCEPT_WITH_QUALIFICATIONS，建议的NB3矩阵公式错误未采用；以直接路线绑定处置。停止无公开门槛的F5纪录主线，不展开q／矩阵扫描。"
for key, extra in [("scope",scope),("failure_or_result",result),("lesson_and_restart_condition",lesson)]:
    if extra.strip() not in source.get(key,""):
        source[key] = source.get(key,"") + extra
source["positive_guarantees"] = list(dict.fromkeys(source.get("positive_guarantees",[]) + [
    "F5固定四port真逆及36转向共同满秩；相邻fiber六平面共同中心覆盖125，非邻／同controller依真实NB3路线。",
    "外审处置与1080条直接controller walk绑定单列，不将回执或条件图算实际新边表。"
]))
source["unclosed_gap"] = "原q3/31完整路线证书仍未得；F5条件规则缺degree20公开比较、literal导图／独验及Lean。一般其它controller／联合多路线并集未排。"
source["outcome_class"] = "source-recovery-and-positive-local-control-no-new-record"
source["report_paths"] = list(dict.fromkeys(source.get("report_paths",[]) + f5paths))

pr = p["result"]
pc = p["cut_pair_followup"]
dr = d["main_result"]
dc = d["saved_counterexample_diagnostic"]
assert pr["controller_candidates_generated"] == 80 and pr["pass_count"] == 0
assert pc["saved_cut_pairs_checked"] == 240
assert dr["controller_candidates_generated"] == 160 and dr["pass_count"] == 0
assert dr["cut_pair_actual_NB3_count_histogram"] == {"2":480}
assert dc["length2_path_count_histogram"] == {"0":134,"1":26}

parallel_variant = dict(label="parallel_subdivision_same_new_vertex_80", target_Delta=16,
    target_D=3, target=[16,3], savedL=1920,
    n=dict(actual=33,hypothetical=2112), object_level="controller",
    actual_controller_degree=4, actual_controller_m=66,
    controller_cases=80, raw_NB3_pass=0, failed=80, untested=0,
    structural_prediction="SUPPORTED", joint_prediction="REFUTED",
    first_missing_class_histogram=pr["first_missing_class_histogram"],
    all_missing_class_occurrences=pr["all_missing_class_occurrence_counts"],
    cutpairs_checked=240, cutpair_length2_length3_histogram={"1,0":240},
    raw_controller_CPU_seconds=pr["cpu_seconds"],
    cutpair_diagnostic_CPU_seconds=pc["cpu_seconds"],
    total_CPU_seconds=pr["cpu_seconds"]+pc["cpu_seconds"],
    strong_closed_scope=p["stronger_closed_scope"],
    target_field_graphs=0, actual_target_n=None, actual_target_D=None,
    ordinary_bad_unordered_pairs=None, source_or_controller_BFS=0, solver_calls=0)
deranged_variant = dict(label="two_deranged_threecycle_attachments_160", target_Delta=16,
    target_D=3, target=[16,3], savedL=1920,
    n=dict(actual=33,hypothetical=2112), object_level="controller",
    actual_controller_degree=4, actual_controller_m=66,
    controller_cases=160, raw_NB3_pass=0, failed=160, untested=0,
    local_cut_pair_repair_prediction="SUPPORTED480/480", joint_prediction="REFUTED",
    cutpair_actual_NB3_histogram={"2":480},
    first_missing_class_histogram=dr["first_missing_class_histogram"],
    all_missing_class_occurrences=dr["all_missing_class_occurrence_counts"],
    first_missing_no_three_walk=True, first_missing_two_walk_histogram={"0":134,"1":26},
    q4_endpoint_capacity_bounds=[0,16], target_fiber_size=64,
    raw_controller_CPU_seconds=dr["cpu_seconds"],
    saved_firstmissing_diagnostic_CPU_seconds=dc["cpu_seconds"],
    total_CPU_seconds=dr["cpu_seconds"]+dc["cpu_seconds"],
    strong_closed_scope=d["stronger_closed_scope"],
    unexecuted_other_transposition_settings=240,
    transposition_status="Paper fixed-point obstruction only; not generated or counted in the executed160.",
    target_field_graphs=0, actual_target_n=None, actual_target_D=None,
    ordinary_bad_unordered_pairs=None, source_or_controller_BFS=0, solver_calls=0)

new_id = "ddp-source30-triangle-attachment33-endpoint-capacity-20261029"
paths = list(dict.fromkeys(p["report_paths"] + p["followup_report_paths"] +
                         d["report_paths"] + [pathstr(parallel/"RAW_ANALYSIS_FIELDS.json"),
                         pathstr(deranged/"RAW_ANALYSIS_FIELDS.json"),
                         "research/ddp/refresh_20261029/DERIVATION_PACKAGE.md"]))
new = dict(id=new_id, title="Source30 triangle attachment to33: parallel80 and deranged160 both capacity-blocked",
    family="four-label affine route-chart lifts",
    idea_family="idea:ddp-q3-three-step-plane-pencil31",
    record_type="controller_necessary_and_strict_endpoint_capacity_gate",
    target_Delta=16, target_D=3, savedL=1920,
    n=dict(actual=33,hypothetical=2112), actual_graph_Delta=4,
    actual_D=None, actual_D_scope="controller-only stored edge lists and exact short-route counts; no exact global controller D or field graph",
    ordinary_bad_unordered_pairs=None, ordinary_bad_target_D=None,
    outcome_class="complete-fixed-controller-attachment-families-no-field-graph",
    date="2026-10-29", wiki_verdict="no",
    scope="同一实际30点/4度controller的十个triangle×各三external-cut选择8=80，identity附着与两个固定点自由3-cycle附着160。实际只生成80+160个33/66/4regular labelled controllers，不是240张2112图或240非同构图；F5正对照另沿旧source节点，不与这里混算。",
    failure_or_result="平行80项全raw门失败，240cutpairs全唯一2walk／0个3walk，因此任q>1、q^3纤维／每arc最多q分支／无内部纤维边的提升均D3失败，允许offset与任意关系。错位160项修480cutpairs且每对NB3=2，局部预测SUPPORTED；其余firstmissing均非邻且无3walk，134项无2walk、26项仅1个，在64纤维／每arc最多4分支下最多0/16<64，联合存在预测REFUTED。0未试、0targetgraph／BFS／solver；普通坏对与目标实际D均null。",
    positive_guarantees=[
        "两种attachment均保所有避开三cut的旧controller路线，所有实际controller简单4regular、十一指定三角。",
        "错位附着确实为全部480个cutpair补回三步路；此局部修复不冒完整共同覆盖。",
        "最终拒绝由无三步且两步容量不足给出，不再只依赖单路线满秩充分证书。"
    ],
    lesson_and_restart_condition="停止这两套固定attachment，不给已被controller容量阻断的设置续矩阵／offset／预算。下一规则须同时保被切边短路线和其它旧旧／新旧点对。原31/2760是另一已保存有限族，不改其统计；此处不排一般33controller、一般2112图或(16,3)。",
    unclosed_gap="一般controller生成、其它六端点配对、内部纤维边或不同宽度关系，以及一般(16,3)仍开放；本轮没有下一自动模板队列。",
    variants=[parallel_variant,deranged_variant],
    other_metrics=dict(controller_candidates_generated=240,
        actual_controller_counts_by_variant={"parallel":80,"deranged":160},
        actual_controller_n=33, actual_controller_m=66, actual_controller_degree=4,
        target_field_graphs=0, actual_target_n=None, actual_target_D=None,
        hypothetical_field_order=2112, hypothetical_field_degree=16,
        source_or_controller_BFS=0, new_field_matrix_search=0, solver_calls=0,
        passers=0, untested=0,
        aggregate_CPU_seconds=sum(v["total_CPU_seconds"] for v in [parallel_variant,deranged_variant]),
        no_nonisomorphism_claim=True, new_lower_bound_mathematically_verified=False,
        same_mechanism_two_variants_not_two_independent_methods=True),
    report_paths=paths)

for row in [source,new]:
    for path in row.get("report_paths",[]):
        assert (ROOT/path).exists(),path
    assert not capture_filter.screen(json.dumps(row,ensure_ascii=False))
(f5dir/"wiki_rows.json").write_text(json.dumps([source],ensure_ascii=False,indent=2)+"\n")
(HERE/"D3_ATTACHMENT_WIKI_ROWS.json").write_text(json.dumps([new],ensure_ascii=False,indent=2)+"\n")
print(json.dumps(dict(source_update_id=source_id,new_experiment_id=new_id,
    source_raw=pathstr(f5dir/"wiki_rows.json"), attachment_raw=pathstr(HERE/"D3_ATTACHMENT_WIKI_ROWS.json"),
    new_mathematical_method_claims=0, computations_rerun=0),ensure_ascii=False))
