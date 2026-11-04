"""Integrate the jointly audited eight-core theorem and geometry consequences.

This is bookkeeping, not a proof checker. It requires the existing independent
PASS reports and verifies all declared source hashes before updating state.
"""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
    names=['T15_SINGLE_AVOIDED_FACE_REVIEW.json','T15_NEW_CONSEQUENCES_REVIEW.json','T15_SAMEFACE_ZERO_CROSSING_REVIEW.json']
    verified={}
    for name in names:
        report=json.loads((R/name).read_text(encoding='utf-8'));assert report['verdict']=='PASS'
        for field in ('audited_input_hashes','audit_artifact_hashes'):
            for rel,h in report.get(field,{}).items():
                assert digest(R/rel)==h.removeprefix('sha256:'),(name,rel)
                verified[rel]=h.removeprefix('sha256:')
    cores=[13,14,19,31,32,35,37,38]
    con=json.loads((R/'T15_NEW_CONSEQUENCES_REVIEW.json').read_text())['details']['geometry_consequences']
    assert con['newly_covered']==7820 and con['remaining']==33638 and con['minimum_additional_core_cover']==14
    manifest=dict(status='PASS_RELATIVE_TO_EXPLICIT_IMPORTS',closed_t15_orbits=cores,
        review_independence='same-family',acceptance_status='provisional',
        reports={n:digest(R/n) for n in names},verified_input_hashes=verified,
        full_t15_proved=False,full_eight_hole_proved=False,full_p6_proved=False,
        newly_covered_eight_geometries=7820,remaining_eight_geometries=33638)
    write(R/'t15_eight_cores_manifest.json',manifest)
    state=json.loads((R/'RUN_STATE.json').read_text(encoding='utf-8'))
    state.update(latest_proof_package='T15_EIGHT_CORES_PROGRESS.md',last_update='2026-11-01',
        q5_t15_closed_core_orbits=cores,q5_t15_sameface_zero_crossing_proved=True,
        full_p6_proved=False,full_eight_hole_proved=False,q5_t15_proved=False,
        remaining_structure='Eight-hole covered targets after eight T15 cores; 10--18 layers remain in full goal but are deferred by user priority',
        active_research_priority='Complete the entire eight-hole layer as quickly as rigorous proofs and independent audits allow',
        t15_eight_cores_closure=manifest)
    g=state['covered_eight_geometry_residual']
    g.update(closed_by_eight_t15_cores=7820,configurations=33638,by_normal_target=con['remaining_by_target'],
        with_a2b1=33588,without_a2b1=50,without_a2b1_orbits=7,
        records='remaining_eight_after_single_face_{1,7,31}.bin',review='T15_NEW_CONSEQUENCES_REVIEW.json')
    state['t15_core_cover']=dict(remaining_parent_geometries=33588,
        minimum_additional_whole_orbit_cover_within_a2b1_scheme=14,
        forced_singleton_cores=11,disjoint_additional_groups=3,
        selected_additional_cores=con['selected_additional_cores'],already_proved_core_orbits=cores,
        source='eight_after_single_face_cores.json',review='T15_NEW_CONSEQUENCES_REVIEW.json',
        geometry_accounting_itself_proves_no_T15_theorem=True)
    write(R/'RUN_STATE.json',state)
    check=json.loads((R/'PROOF_CHECK_STATE.json').read_text(encoding='utf-8'))
    for a in ['/root/t15_sameface_zero_audit','/root/t15_single_face_full_audit','/root/t15_new_consequences_audit']:
        if a not in check['review_agent_ids']:check['review_agent_ids'].append(a)
    check.update(acceptance_gate='EIGHT_T15_ORBITS_AND_SCOPED_CONSEQUENCES_PASS_RELATIVE_TO_IMPORTS',
        latest_package='Eight T15 singleton-avoided-face orbits, sameface zero crossing, and exact Q6 geometry consequences',
        latest_review_files=names,latest_review_report_hashes=manifest['reports'],
        latest_input_hashes_checked=len(verified),latest_micro_obligations='25 core proof obligations plus scoped consequence ledger',
        deterministic_check='2027025 root states; 15135120 forward targets; 34514 witnesses; 396900 actual 30-cycle joins; 112199 coordinate projections',
        q5_t15_closed_core_orbits=cores,q5_t15_sameface_zero_crossing_proved=True,
        remaining_eight_hole_domain='R8-covered after a1b4 and eight T15 orbit cores:33638 normalized geometries',
        remaining_eight_hole_geometries=33638,full_p6_proved=False,full_eight_hole_proved=False,q5_t15_proved=False)
    check['audited_packages']=max(check.get('audited_packages',0),29)
    write(R/'PROOF_CHECK_STATE.json',check)
    package=R.parent.parent/'PROOF_PACKAGE.md';text=package.read_text(encoding='utf-8')
    marker='2026-11-01 最新八孔推进：**八个 T15 核心轨道已关闭**'
    if marker not in text:
        entry=marker+'（13、14、19、31、32、35、37、38），并关闭六孔同面零跨边的T15分支。详见 [T15_EIGHT_CORES_PROGRESS.md](research/six_directions/T15_EIGHT_CORES_PROGRESS.md)。GPT-6.1-sol high 新上下文审计通过，保证等级same-family/provisional；独立核验2027025根态及396900次实际合圈。八孔新增覆盖7820个规范孔配置，剩33638=33588个有(2,1)切分+50个七轨道例外；当前整轨道方案最少还需14个T15核心。**完整T15、完整八孔及P6仍未证**。用户要求优先尽快完整八孔，10—18孔暂缓研究但保留于完整目标。以下冲突状态为历史记录。\n\n'
        first,rest=text.split('\n',1);package.write_text(first+'\n\n'+entry+rest.lstrip('\n'),encoding='utf-8')
    nxt=R/'NEXT_OBLIGATIONS.md';text=nxt.read_text(encoding='utf-8');head,history=text.split('## 历史研究记录',1)
    head='''# 完整P6的剩余义务

## 当前优先级（覆盖下面旧条目）

**用户要求：先把八孔完整证完，尽可能快速封闭。** 10—18孔暂缓研究，仍属于完整P6目标。

已关闭A4、完整六孔、A6/K6、完整八孔自由终点、T44_5、八孔已覆盖目标(1,4)分支，以及T15硬轨道13、14、19、31、32、35、37、38。当前总览 `T15_EIGHT_CORES_PROGRESS.md`；所有新增全称结论均经GPT-6.1-sol high独立审计，same-family/provisional。

八孔被覆盖目标当前剩33638个规范孔配置。其中33588个有(2,1)切分，可由尚未证明的T15核心充分覆盖；另50个、七轨道仍需EP0或替代路径构造。数字为孔几何数，不是匹配数。

当前最小额外整轨道充分集为 `[0,1,2,4,5,7,8,10,15,23,24,26,27,44]`。14的最小性仅针对当前(2,1)整轨道方案，独立检查确认11个单项强制核心加3组互不交约束。优先寻求同时处理多轨道的引理，不能把这个覆盖规划当成14个核心已证明。

推进路线：`T15_CORE0_THREE_AVOID_NEXT.md` 记录新双桥方案和完整四维三避点例外表，零跨边B面仍有18个简单方案障碍，未宣称core0关闭。`T15_PRESCRIPTION_ANALYSIS.md`证明指定边的圈因子普遍存在，连接成单圈仍未证。`T15_SAMEFACE_ZERO_CROSSING.md`已关闭同面零跨边；正跨边三角障碍继续研究。

必须对剩余全部匹配、自由根和异奇偶目标闭合后才可宣布完整八孔。完整P6始终未证。

'''
    nxt.write_text(head+'## 历史研究记录'+history,encoding='utf-8')
    print('Integrated audited eight-core theorem; verified unique hashes',len(verified),'; full P6 remains false')
if __name__=='__main__':main()
