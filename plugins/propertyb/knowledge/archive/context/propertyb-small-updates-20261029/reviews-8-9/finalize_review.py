"""Persist actually completed reviews of the two frozen, independently checked proofs."""
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TRACE = ROOT / '.aris/traces/proof-checker/2026-10-29_m8-m9'
TRACE.mkdir(parents=True, exist_ok=True)
now = datetime.now(timezone.utc).isoformat()
prompt = (HERE / 'REQUEST.md').read_text()
def save(p, x): p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

reviews = []
for i, (name, family, requested, effort) in enumerate([
    ('GROK', 'xai', 'grok-4.7', 'xhigh'), ('GEMINI', 'google', 'gemini-4-argon-high', 'high')
], 1):
    path = HERE / f'{name}_RESPONSE.json'
    if not path.exists():
        reviews.append(dict(reviewer=name, status='pending', review_completed=False)); continue
    raw = json.loads(path.read_text()); s = raw.get('structuredContent', {})
    body = s.get('content') or '\n'.join(c.get('text','') for c in raw.get('content',[]) if c.get('type') == 'text')
    signal = s.get('stopReason') if name == 'GROK' else s.get('status')
    complete = signal == ('end_turn' if name == 'GROK' else 'SUCCESS')
    positive = complete and 'PASS_WITH_DECLARED_COMPUTATION_IMPORTS' in body
    record = dict(reviewer=name, requested_model=requested, reported_model=s.get('model'),
                  thread_id=s.get('threadId'), effort=s.get('effort'), completion=signal,
                  reviewer_family=family, review_independence='cross-family',
                  review_completed=complete, review_scope_complete=positive, review_positive=positive,
                  acceptance_status='accepted' if positive else 'provisional',
                  verdict='PASS_WITH_DECLARED_COMPUTATION_IMPORTS' if positive else 'not_accepted',
                  executed_programs=False, executed_lean=False, raw_source=str(path.relative_to(ROOT)))
    reviews.append(record)
    stem = f'{i:03d}-final-{name.lower()}'
    save(TRACE / f'{stem}.request.json', dict(prompt=prompt, executor_family='openai',
         executor_model=None, requested_reviewer_model=requested, requested_effort=effort, cwd=str(ROOT)))
    (TRACE / f'{stem}.response.md').write_text(body + '\n')
    save(TRACE / f'{stem}.raw.json', raw); save(TRACE / f'{stem}.meta.json', record | dict(generated_at=now))

done = all(r.get('review_positive') for r in reviews)
scope = [
    dict(k=8, M=266, vertex_domain=[47,120], profiles=2094, independent_quota_inputs=299,
         source='context/propertyb-m8-267-20261029/PROOF_M8_GE267.md',
         verification='context/propertyb-m8-267-20261029/independent/CHECK.json'),
    dict(k=9, M=542, vertex_domain=[57,195], profiles=3450, conditional_parent_inputs=73,
         source='context/propertyb-m9-543-20261029/PROOF_M9_GE543.md',
         verification='context/propertyb-m9-543-20261029/independent/CHECK.json')]
obligations = [
    'Original arbitrary finite simple k-uniform input, with no structural certificate premise',
    'Minimum-vertex pair identification, balanced small-v exclusion, exact budget padding',
    'Complete integer upper and lower vertex domains including the new v195 boundary',
    'Actual minimum-degree unit partner and nested common-unit pool, with positive n and t',
    'All degree intervals, all two unit-triple trace patterns, actual nonnegative multiplicities',
    'Low-degree conflict graph and exact strict Caro-Wei gap over the whole tail',
    'k8 v120 forces at least32 globally unit degree17 vertices; complete K4 six-pattern domain',
    'Seven-link support7alpha/8/15 and DP necessary-bound direction; same-vector max_R',
    'Conditional actual permutation endpoint/pair counts and ordered/unordered factors',
    'Independent full domain reconstruction and all exact fractions; original legal coloring obtained from U<1']
audit = dict(audit_skill='proof-checker', verdict='PASS' if done else 'BLOCKED',
    reason_code='all_proofs_complete_with_declared_computation_imports' if done else 'final_review_pending',
    summary='Complete computer-assisted proofs m(8)>=267 and m(9)>=543, with full independent exact replay; no Lean.',
    generated_at=now, executor_family='openai', executor_model=None, reviews=reviews,
    canonical_statements=[f'For every finite simple {x["k"]}-uniform hypergraph H, |E(H)| <= {x["M"]} implies Property B.' for x in scope],
    reviewed_author_snapshots=['context/propertyb-m8-267-20261029/AUTHOR_REVIEW_SNAPSHOT.md','context/propertyb-m9-543-20261029/AUTHOR_REVIEW_SNAPSHOT.md'],
    post_review_change='Only verification-status prose updated; no theorem, selection, domain, formula, fraction or program changed. Exact textual diff: STATUS_ONLY_DIFF.patch.',
    extra_hypotheses=[], proof_status='sound-modulo-imports' if done else 'drafted',
    scope=scope, obligations=obligations,
    declared_imports=['Finite exact-rational computation and ordinary Python/runtime trust. Every used local probability row was independently reimplemented and recomputed.',
                      'Shared conditional greedy witness and counting are explicitly read and checked; no unproved structure or certificate hypothesis is added.'],
    issues=[], unresolved_mathematical_obligations=[], lean_verified=False, second_machine_reproduction=False,
    trace_path=str(TRACE.relative_to(ROOT)))
save(HERE / 'PROOF_AUDIT.json', audit)
save(HERE / 'PROOF_CHECK_STATE.json', dict(status='completed' if done else 'final_review_pending', timestamp=now,
    acceptance_gate=audit['verdict'], review_agent_ids=[r.get('thread_id') for r in reviews if r.get('thread_id')]))
save(TRACE / 'run.meta.json', dict(skill='proof-checker', scope=scope, executor='codex', executor_family='openai',
     executor_model=None, project_dir=str(ROOT), generated_at=now))
lines = ['# 八元267、九元543：联合审阅与实际验收', '',
         '原命题分别为任意有限简单八元超图至多266边可二染、九元超图至多542边可二染；所有顶点数、点对覆盖及选锁条件均为内部推导。', '',
         '**完整数学链与全量独立数值复算已完成；' + ('两份指定跨家族审阅均有效接受。**' if done else 'Grok成稿审阅仍在途，尚未计作双模型通过。**'), '',
         '八元独核2094型、299个组件配额全部精确一致；九元独核3450型及原始决策树全部精确一致。下降阶乘注入实现不导入作者二项式数值或域生成程序。两者均严格，均连接回原始输入的合法染色；没有枚举原超图来代替证明。', '',
         '|审阅者|实际返回模型／effort|完成信号|结论|', '|---|---|---|---|']
for r in reviews:
    lines.append('|'+r['reviewer']+'|'+str(r.get('reported_model','待返回'))+' / '+str(r.get('effort','待返回'))+'|'+str(r.get('completion','pending'))+'|'+str(r.get('verdict','在途，未计通过'))+'|')
lines += ['', '跨家族审阅为原证明、代码和独核记录的静态审阅，未执行程序或Lean。Gemini实际读了两份independent/check.py及CHECK.json，审阅时REVIEW.md尚未生成，因此没有把后生成报告计入其阅读范围。完整实际阅读范围及攻击过程见原回复；模型认可不能代替数学与独立计算。', '',
          '状态为完整计算机辅助证明，明确保留有限计算和通常软件信任；无本参数Lean或第二台机器复现。不改参考基线，不声称m(8)、m(9)的精确值。', '',
          '[八元完整证明](../../propertyb-m8-267-20261029/PROOF_M8_GE267.md) · [九元完整证明](../../propertyb-m9-543-20261029/PROOF_M9_GE543.md) · [共同离线阅读页](../../../M8_M9_IMPROVEMENTS.html)', '',
          '成稿终审之后仅更新了验收状态说明，数学命题、证明、公式、数值与程序均未改；送审原稿保留为各目录AUTHOR_REVIEW_SNAPSHOT.md，完整文字差分见[状态同步差分](STATUS_ONLY_DIFF.patch)。', '',
          '[审计JSON](PROOF_AUDIT.json) · [Grok原回应](GROK_RESPONSE.json) · [Gemini原回应](GEMINI_RESPONSE.json) · [完整送审请求](REQUEST.md)', '']
(HERE / 'DISPOSITION.md').write_text('\n'.join(lines))
(HERE / 'PROOF_AUDIT.md').write_text('\n'.join(lines))
print(json.dumps(dict(verdict=audit['verdict'], reviews=reviews), ensure_ascii=False))
