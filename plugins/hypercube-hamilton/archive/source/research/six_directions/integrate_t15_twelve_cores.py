"""Bookkeeping after three new independent PASS packages; not a proof checker."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
    names=['T15_BALANCED_BRIDGE_REVIEW.json','T15_BALANCED_BRIDGE_CONSEQUENCES_REVIEW.json','EIGHT_NEW_PARTIAL_BRANCHES_REVIEW.json']
    verified={}
    for n in names:
        report=json.loads((R/n).read_text());assert report['verdict']=='PASS'
        for field in ('audited_input_hashes','audit_artifact_hashes','protected_core_hashes'):
            for p,h in report.get(field,{}).items():
                assert digest(R/p)==h.removeprefix('sha256:'),(n,p)
                verified[p]=h.removeprefix('sha256:')
    c=json.loads((R/'eight_after_balanced_bridge_check.json').read_text())
    assert c['remaining']==21350 and c['minimum_additional_whole_orbit_cover']==10
    manifest=dict(status='PASS_RELATIVE_TO_EXPLICIT_IMPORTS',review_independence='same-family',acceptance_status='provisional',
        report_hashes={n:digest(R/n) for n in names},verified_input_hashes=verified,
        closed_t15_orbits=c['proved_T15_core_orbits'],remaining_eight_geometries=21350,
        full_t15_proved=False,full_eight_hole_proved=False,full_p6_proved=False)
    write(R/'t15_twelve_cores_manifest.json',manifest)
    state=json.loads((R/'RUN_STATE.json').read_text(encoding='utf-8'))
    state.update(latest_proof_package='T15_TWELVE_CORES_PROGRESS.md',last_update='2026-11-01',
        q5_t15_closed_core_orbits=c['proved_T15_core_orbits'],t15_twelve_cores_closure=manifest,
        remaining_structure='Eight-hole covered targets after twelve T15 cores; full 10--18 layers deferred but remain in P6 goal')
    g=state['covered_eight_geometry_residual']
    g.update(closed_by_balanced_four_t15_cores=12288,configurations=21350,by_normal_target=c['remaining_by_target'],
        with_a2b1=21300,without_a2b1=50,records='remaining_eight_after_balanced_bridge_{1,7,31}.bin',review='T15_BALANCED_BRIDGE_CONSEQUENCES_REVIEW.json')
    state['t15_core_cover']=dict(remaining_parent_geometries=21300,minimum_additional_whole_orbit_cover_within_a2b1_scheme=10,
        forced_singleton_cores=9,disjoint_additional_groups=1,selected_additional_cores=c['additional_sufficient_cores'],
        already_proved_core_orbits=c['proved_T15_core_orbits'],source='eight_after_balanced_bridge_check.json',
        review='T15_BALANCED_BRIDGE_CONSEQUENCES_REVIEW.json',geometry_accounting_itself_proves_no_T15_theorem=True)
    state['new_scoped_eight_hole_obligations']=dict(ep0_geometries_closed=11,ep0_geometries_remaining=39,
        ep0_to_actual_q6_paths_still_requires_T15=True,core0_zero_crossing_cut0_proved=True,
        sameface_positive_safe_pairing_and_two_triangle_ports_proved=True,
        review='EIGHT_NEW_PARTIAL_BRANCHES_REVIEW.json',no_additional_q6_parent_removed_by_partial_branches=True)
    assert not state['full_p6_proved'] and not state['full_eight_hole_proved'] and not state['q5_t15_proved']
    write(R/'RUN_STATE.json',state)
    audit=json.loads((R/'PROOF_CHECK_STATE.json').read_text(encoding='utf-8'))
    for agent in ['/root/t15_balanced_four_core_audit','/root/eight_partial_branches_audit']:
        if agent not in audit['review_agent_ids']:audit['review_agent_ids'].append(agent)
    audit.update(latest_package='Twelve full T15 core orbits and scoped EP0/sameface/core0 branches',
        acceptance_gate='TWELVE_T15_ORBITS_AND_SCOPED_BRANCHES_PASS_RELATIVE_TO_IMPORTS',
        latest_review_files=names,latest_review_report_hashes=manifest['report_hashes'],latest_input_hashes_checked=len(verified),
        q5_t15_closed_core_orbits=c['proved_T15_core_orbits'],remaining_eight_hole_geometries=21350,
        remaining_eight_hole_domain='R8-covered after a1b4 and twelve T15 core orbits:21350 normalized geometries',
        latest_micro_obligations='Four-core full proof plus exact geometry appendix and three scoped partial branches',
        deterministic_check='135135 new Q4 records/84 negatives;270270 N14 positives;15 B exceptions;94779 projections;187110 core0 circles;12720 sameface full expansions')
    audit['audited_packages']=max(audit.get('audited_packages',0),32);write(R/'PROOF_CHECK_STATE.json',audit)
    p=R.parent.parent/'PROOF_PACKAGE.md';text=p.read_text(encoding='utf-8');marker='2026-11-01 最新：**十二个T15核心轨道已关闭**'
    if marker not in text:
        line=marker+'，新增2、7、10、44；八孔当前剩余21350=21300个(2,1)投影配置+50个七轨道例外。当前整轨道方案还需10个核心。详见 [T15_TWELVE_CORES_PROGRESS.md](research/six_directions/T15_TWELVE_CORES_PROGRESS.md)。新四核心、精确后果及三项局部分支均经GPT-6.1-sol high独立审计PASS，same-family/provisional。EP0已有11/50几何关闭，但仍依赖未证T15核心4，未从50项扣除。**完整八孔、T15及P6仍未证**；当前集中优先完成八孔。\n\n'
        first,rest=text.split('\n',1);p.write_text(first+'\n\n'+line+rest.lstrip('\n'),encoding='utf-8')
    p=R/'NEXT_OBLIGATIONS.md';text=p.read_text(encoding='utf-8');marker='**最新：十二个T15核心已关闭**'
    if marker not in text:
        text=text.replace('## 当前优先级（覆盖下面旧条目）\n','## 当前优先级（覆盖下面旧条目）\n\n'+marker+'。以 `T15_TWELVE_CORES_PROGRESS.md` 为准，以下八核心阶段数字为历史。八孔剩21350=21300+50，充分核心集现为 `[0,1,4,5,8,15,23,24,26,27]`，最小10仅指当前整轨道方案。EP0关闭11/50但仍需核心4，其余39的EP0未证。最新任务是core0两跨边谱、r3小跨边谱和core4双孔面方案；完整八孔仍未关闭。\n',1)
        p.write_text(text,encoding='utf-8')
    print('Integrated twelve audited T15 core orbits; remaining Q6 hole geometries 21350; full eight and P6 remain open; verified hashes',len(verified))
if __name__=='__main__':main()
