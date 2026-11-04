"""Integrate explicit full-core PASS reports, retaining the full eight/P6 goal.

No theorem is inferred from a certificate count. The extra-core registry maps
each exact full theorem to its dedicated independent semantic review.
"""
import json,hashlib,collections
from pathlib import Path
R=Path(__file__).resolve().parent
EXTRA={0:'T15_CORE0_FULL_REVIEW.json',5:'T15_CORE5_FULL_REVIEW.json',
       1:'T15_CORE1_FULL_REVIEW.json',4:'T15_CORE4_FULL_REVIEW.json',
       24:'T15_CORE24_FULL_REVIEW.json',
       8:'T15_CORE8_FULL_REVIEW.json',27:'T15_CORE27_FULL_REVIEW.json',
       15:'T15_CORE15_FULL_REVIEW.json',23:'T15_CORE23_FULL_REVIEW.json',
       18:'T15_ALTERNATIVE_GROUP_REVIEW.json',21:'T15_ALTERNATIVE_GROUP_REVIEW.json',
       25:'T15_ALTERNATIVE_GROUP_REVIEW.json'}
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as stream:
        for block in iter(lambda:stream.read(8*1024*1024),b''):h.update(block)
    return h.hexdigest()
def put(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
    base=json.loads((R/'eight_after_balanced_bridge_candidates.json').read_text())
    accepted={};verified={}
    for core,name in EXTRA.items():
        if not (R/name).exists():continue
        review=json.loads((R/name).read_text(encoding='utf-8'))
        if review.get('verdict')!='PASS':continue
        assert review.get('audited_input_hashes') or review.get('protected_core_hashes'),name
        for field in ('audited_input_hashes','audit_artifact_hashes','protected_core_hashes'):
            for rel,h in review.get(field,{}).items():
                assert digest(R/rel)==h.removeprefix('sha256:'),(name,rel)
                verified[rel]=h.removeprefix('sha256:')
        accepted[core]=name
    extra=set(accepted);closed=set(base['proved_T15_core_orbits'])|extra
    remaining=[r for r in base['rows'] if not set(r['core_choices'])&extra]
    ep0_review=None;ep0_closed=set()
    ep0_name='EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.json'
    if not ({1,4}<=extra and (R/ep0_name).exists()):ep0_name='EIGHT_EP0_CORE4_CONSEQUENCES_REVIEW.json'
    if 4 in extra and (R/ep0_name).exists():
        report=json.loads((R/ep0_name).read_text(encoding='utf-8'))
        if report.get('verdict')=='PASS':
            for field in ('audited_input_hashes','audit_artifact_hashes'):
                for rel,h in report.get(field,{}).items():
                    assert digest(R/rel)==h.removeprefix('sha256:'),(ep0_name,rel)
                    verified[rel]=h.removeprefix('sha256:')
            ep0_closed={(r['target'],tuple(r['Z']),tuple(r['W'])) for r in report['closed_geometries']}
            original_no21={(r['target'],tuple(r['Z']),tuple(r['W'])) for r in base['rows'] if not r['core_choices']}
            expected_ep0=50 if ep0_name=='EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.json' else 11
            assert len(ep0_closed)==expected_ep0 and ep0_closed<=original_no21
            remaining=[r for r in remaining if (r['target'],tuple(r['Z']),tuple(r['W'])) not in ep0_closed]
            ep0_review=ep0_name
    counts=dict(collections.Counter(r['target'] for r in remaining))
    patterns={tuple(r['core_choices']) for r in remaining if r['core_choices']}
    best=None
    def cover(selected,todo):
        nonlocal best
        if best is not None and len(selected)>=len(best):return
        if not todo:best=set(selected);return
        p=min(todo,key=lambda p:(len(p),p))
        for c in p:cover(selected|{c},{q for q in todo if c not in q})
    cover(set(),patterns)
    for v in (1,7,31):
        (R/f'remaining_eight_current_{v}.bin').write_bytes(b''.join(bytes(r['Z']+r['W']) for r in remaining if r['target']==v))
    no21=sum(not r['core_choices'] for r in remaining);assert no21==50-len(ep0_closed)
    full_eight=False;full_review='EIGHT_HOLE_FULL_REVIEW.json'
    if (R/full_review).exists():
        report=json.loads((R/full_review).read_text(encoding='utf-8'))
        if report.get('verdict')=='PASS':
            assert not remaining and len(ep0_closed)==50
            assert report.get('audited_input_hashes')
            for field in ('audited_input_hashes','audit_artifact_hashes'):
                for rel,h in report.get(field,{}).items():
                    assert digest(R/rel)==h.removeprefix('sha256:'),(full_review,rel)
                    verified[rel]=h.removeprefix('sha256:')
            full_eight=True
    ledger=dict(status='PASS_RELATIVE_TO_EXPLICIT_IMPORTS',closed_t15_orbits=sorted(closed),
        extra_review_files=accepted,extra_review_hashes={n:digest(R/n) for n in accepted.values()},verified_input_hashes=verified,
        base_geometry_file='eight_after_balanced_bridge_candidates.json',base_geometry_sha256=digest(R/'eight_after_balanced_bridge_candidates.json'),
        remaining=len(remaining),by_target=counts,with_a2b1=len(remaining)-no21,without_a2b1=no21,
        closed_ep0_geometries=len(ep0_closed),ep0_consequence_review=ep0_review,
        ep0_consequence_review_sha256=digest(R/ep0_review) if ep0_review else None,
        full_eight_review=full_review if full_eight else None,
        full_eight_review_sha256=digest(R/full_review) if full_eight else None,
        additional_sufficient_cores=sorted(best),minimum_additional_whole_orbit_cover=len(best),
        review_independence='same-family',acceptance_status='provisional',full_t15_proved=False,full_eight_hole_proved=full_eight,full_p6_proved=False)
    put(R/'eight_current_core_ledger.json',ledger)
    state=json.loads((R/'RUN_STATE.json').read_text(encoding='utf-8'))
    state.update(latest_proof_package='EIGHT_CURRENT_PROGRESS.md',q5_t15_closed_core_orbits=sorted(closed),
        latest_core_ledger='eight_current_core_ledger.json',full_eight_hole_proved=full_eight,
        remaining_structure=('Eight-hole layer fully closed; higher10/12/14/16/18 layers remain in full P6 goal' if full_eight else f'Eight-hole covered targets: {len(remaining)} normalized geometries; whole-layer review pending' if not remaining else f'Eight-hole covered targets: {len(remaining)} normalized geometries; higher layers remain in full P6 goal'))
    state['covered_eight_geometry_residual'].update(configurations=len(remaining),by_normal_target=counts,
        with_a2b1=len(remaining)-no21,without_a2b1=no21,records='remaining_eight_current_{1,7,31}.bin',review='eight_current_core_ledger.json')
    state['t15_core_cover'].update(remaining_parent_geometries=len(remaining)-no21,
        forced_singleton_cores=sorted({p[0] for p in patterns if len(p)==1}),
        minimum_additional_whole_orbit_cover_within_a2b1_scheme=len(best),selected_additional_cores=sorted(best),
        already_proved_core_orbits=sorted(closed),source='eight_current_core_ledger.json')
    if full_eight:
        state.update(remaining_full_p6_hole_levels=[10,12,14,16,18],
            remaining_candidate_hole_counts=[10,12,14,16,18],
            active_research_priority='Unify and prove the remaining10/12/14/16/18-hole layers, reusing the completed eight-hole lemmas',
            q5_neighbor_abundance_proved=True,eight_hole_ep0_proved=True,
            last_goal_turn_classification='Complete eight-hole P6 proved relative to explicit imports and finite certificates; independent whole-layer audit PASS; full P6 remains open',
            latest_independent_witness_check='Complete eight-hole whole-layer audit plus24 marked T15 cores and all50 EP0 geometries; see EIGHT_HOLE_FULL_REVIEW.json')
    assert not state['full_p6_proved'];put(R/'RUN_STATE.json',state)
    audit=json.loads((R/'PROOF_CHECK_STATE.json').read_text(encoding='utf-8'))
    audit.update(latest_package='Current audited full T15 cores and retained eight-hole obligations',
        latest_review_files=list(accepted.values()),latest_review_report_hashes=ledger['extra_review_hashes'],
        latest_input_hashes_checked=len(verified),q5_t15_closed_core_orbits=sorted(closed),
        full_eight_hole_proved=full_eight,full_p6_proved=False,
        full_eight_review=full_review if full_eight else None,
        remaining_eight_hole_geometries=len(remaining),remaining_eight_hole_domain=f'R8-covered current {len(remaining)} normalized geometries')
    if full_eight:
        audit.update(remaining_full_p6_hole_levels=[10,12,14,16,18],
            q5_neighbor_abundance_proved=True,eight_hole_ep0_proved=True,
            eight_hole_final_review=dict(file=full_review,sha256=digest(R/full_review),verdict='PASS',review_independence='same-family',acceptance_status='provisional'))
    for name in accepted.values():
        r=json.loads((R/name).read_text());agent=r.get('reviewer_agent_id') or r.get('reviewer_task')
        if agent and agent not in audit['review_agent_ids']:audit['review_agent_ids'].append(agent)
    put(R/'PROOF_CHECK_STATE.json',audit)
    exception_status=('全部50个例外已由Q5自由孔邻点丰度、严格EP0换元和core1/core4关闭；234个可选边投影及50个规范几何均经独立审计核对。' if len(ep0_closed)==50 else '50个例外中，11个已由完整核心4和已审EP0证明关闭，并经后果审计精确核对；另39个尚未证明。' if ep0_closed else '50个例外中，11个的EP0辅助条件已审通过；完整后果尚未计入账本，另39个EP0仍未证。')
    scope_status=('完整八孔已关闭；完整T15及完整P6仍未证。' if full_eight else '所有八孔局部义务已关闭，完整八孔汇总审计尚待通过；完整T15及完整P6仍未证。' if not remaining else '完整八孔、完整T15、完整P6仍未证。')
    doc=f'''# 八孔当前状态

2026-11-01。用户要求优先尽快完整关闭八孔。**{scope_status}**

当前已由独立GPT-6.1-sol high审计通过的完整T15硬轨道有{len(closed)}个：
`{sorted(closed)}`。保证等级为相对于显式导入定理和有限证书的same-family/provisional。

当前剩余{len(remaining)}个规范八孔配置，其中{len(remaining)-no21}个有(2,1)投影，
{no21}个是原七轨道例外中的未关闭项。按规范目标1、7、31，剩余分别{counts.get(1,0)}、{counts.get(7,0)}、{counts.get(31,0)}。
这些是孔配置数，不是匹配数；每个已关闭轨道的量词覆盖其全部实现匹配。

当前整轨道(2,1)方案还需{len(best)}个核心，剩余充分集为`{sorted(best)}`；空集表示这一分支已全部关闭。
最少轨道数未必代表最快证明路线：18、21、25三个核心可以替代困难核心26，
这条替代路线已在三个核心完整独立审计PASS后计入。任何候选核心只在其完整独立审计PASS后计入。

{exception_status}
完整自由终点分支早已关闭，当前剩余是被覆盖终点。

当前纳入的完整核心审计：`{sorted(set(accepted.values()))}`。
EP0后果审计：`{ep0_review}`；完整八孔汇总审计：`{full_review if full_eight else '尚未最终接受'}`。
此前十二核心基础见`T15_TWELVE_CORES_PROGRESS.md`。
复核账本、输入哈希和剩余记录见`eight_current_core_ledger.json`及
`remaining_eight_current_{{1,7,31}}.bin`。

完整八孔的精确陈述与依赖见`EIGHT_HOLE_FULL_CLOSURE.md`。
10、12、14、16、18孔仍保留于完整P6目标；只证明恰好18孔并不蕴含八孔。
'''
    (R/'EIGHT_CURRENT_PROGRESS.md').write_text(doc,encoding='utf-8')
    print(json.dumps({k:ledger[k] for k in ['closed_t15_orbits','remaining','with_a2b1','without_a2b1','additional_sufficient_cores']}))
if __name__=='__main__':main()
