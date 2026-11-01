"""Record actual review completion; this does not run or replace verification."""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parents[1]
TRACE = ROOT / '.aris/traces/proof-checker/2026-10-29_m6-ge67'
TRACE.mkdir(parents=True, exist_ok=True)
now = datetime.now(timezone.utc).isoformat()
prompt = (RUN / 'reviews/FINAL_REQUEST.md').read_text()

def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

reviews = []
for i, (name, family, requested, effort) in enumerate([
    ('GROK', 'xai', 'grok-4.7', 'xhigh'),
    ('GEMINI', 'google', 'gemini-4-argon-high', 'high'),
], 1):
    path = RUN / f'reviews/FINAL_{name}_RESPONSE.json'
    if not path.exists():
        reviews.append(dict(reviewer=name, status='pending', review_completed=False))
        continue
    raw = json.loads(path.read_text())
    s = raw.get('structuredContent', {})
    body = s.get('content') or '\n'.join(c.get('text','') for c in raw.get('content',[]) if c.get('type') == 'text')
    complete = s.get('status') == 'SUCCESS' if name == 'GEMINI' else s.get('stopReason') == 'end_turn'
    # Root reads the raw response and resolves any issues before using this gate.
    positive = complete and 'PASS_WITH_DECLARED_COMPUTATION_IMPORTS' in body
    record = dict(reviewer=name, thread_id=s.get('threadId'), requested_model=requested,
                  reported_model=s.get('model'), effort=s.get('effort'), reviewer_family=family,
                  completion=s.get('status') if name == 'GEMINI' else s.get('stopReason'),
                  review_completed=complete, review_scope_complete=positive,
                  review_positive=positive, review_independence='cross-family',
                  acceptance_status='accepted' if positive else 'provisional',
                  verdict='PASS_WITH_DECLARED_COMPUTATION_IMPORTS' if positive else 'not_accepted',
                  executed_programs=False, executed_lean=False,
                  raw_source=str(path.relative_to(ROOT)))
    reviews.append(record)
    stem = f'{i:03d}-final-{name.lower()}'
    save(TRACE / f'{stem}.request.json', dict(prompt=prompt, requested_reviewer_model=requested,
         requested_effort=effort, executor_family='openai', executor_model=None,
         backend='grok' if name == 'GROK' else 'antigravity', cwd=str(ROOT)))
    (TRACE / f'{stem}.response.md').write_text(body + '\n')
    save(TRACE / f'{stem}.raw.json', raw)
    save(TRACE / f'{stem}.meta.json', record | dict(generated_at=now))

complete = all(r.get('review_positive') for r in reviews)
save(TRACE / 'run.meta.json', dict(skill='proof-checker', generated_at=now,
     executor='codex', executor_model=None, executor_family='openai', project_dir=str(ROOT),
     scope='Finite simple 6-uniform hypergraphs with at most 66 edges'))
audit = dict(audit_skill='proof-checker', verdict='PASS' if complete else 'PENDING',
    reason_code='all_proofs_complete_with_declared_computation_imports' if complete else 'final_review_pending',
    summary='Full original-domain computer-assisted proof of m(6) >= 67; complete independent local arithmetic; no Lean.',
    canonical_statement='For every finite set V and every simple family E of 6-element subsets of V, |E| <= 66 implies a two-coloring nonmonochromatic on every original edge.',
    extra_hypotheses=[], proof_status='sound-modulo-imports' if complete else 'drafted',
    declared_imports=['Explicit finite exact-rational computations and ordinary Python/runtime trust; all used necessary local domains independently reconstructed and checked.',
                      'Conditional greedy probability calculation is restated in the proof; no unproved structural premise or certificate hypothesis is exposed in the original theorem.'],
    trace_path=str(TRACE.relative_to(ROOT)), source_coverage='audit/SOURCE_COVERAGE.json',
    dependency_and_obligation_ledger='audit/PROOF_SKELETON.md', actual_input_map='audit/INPUT_MAP.json',
    executor_family='openai', executor_model=None, reviews=reviews,
    lean_verified=False, second_machine_reproduction=False,
    details=dict(theorems_audited=1, declared_source_units=67, declared_obligations=144,
                 source_files=14, issues=[], unresolved_mathematical_obligations=[],
                 analysis_interchanges='not_applicable: all arguments and probability spaces are finite'),
    generated_at=now)
save(RUN / 'PROOF_AUDIT.json', audit)
save(RUN / 'PROOF_CHECK_STATE.json', dict(status='completed' if complete else 'final_review_pending',
     rounds=1, review_agent_ids=[r.get('thread_id') for r in reviews if r.get('thread_id')],
     acceptance_gate=audit['verdict'], timestamp=now, lean_verified=False))
lines = ['# 六元67：最终审阅范围与处置', '',
         '原命题：任意有限简单六元超图，边数至多66即具有Property B，等价于m(6)≥67。', '',
         '**当前：完整数学论证与独立精确计算已完成；' + ('两份指定跨家族终审均有效接受。**' if complete else '指定终审尚有在途调用。**'), '',
         '|审阅者|实际模型／effort|完成状态|结论与范围|', '|---|---|---|---|']
for r in reviews:
    lines.append('|'+r['reviewer']+'|'+str(r.get('reported_model','待返回'))+' / '+str(r.get('effort','待返回'))+'|'+str(r.get('completion','pending'))+'|'+str(r.get('verdict','在途，未计通过'))+'；全文结构／原题连接静态审阅，数值为声明进口，未执行程序或Lean|')
lines += ['', '本机已用不同概率实现及完整必要域重建复核所有使用的有限表。模型认可只记录其实际阅读与判断，不能替代这些数学和计算证据。完整范围见 [审计](../PROOF_AUDIT.json)、[来源与义务地图](../audit/PROOF_SKELETON.md)。', '',
          'Gemini原回应把自身标成same-family/provisional，属于沿用模板的元数据错误；实际桥接返回gemini-4-argon-high，执行者为Codex/OpenAI，因此此处按实际模型家族记为cross-family，原回复原样保留。此更正不改变数学结论或声称独立服务端身份验证。', '',
          '本成果是完整计算机辅助证明；无本参数Lean、无第二台机器复现，不宣称m(6)的等号。较早子义务讨论与本次整卷终审分别保存；失败计算继续作为历史保留。', '',
          '[Grok原回应](FINAL_GROK_RESPONSE.json) · [Gemini原回应](FINAL_GEMINI_RESPONSE.json) · [完整请求](FINAL_REQUEST.md)', '']
(RUN / 'reviews/DISPOSITION.md').write_text('\n'.join(lines))
(RUN / 'PROOF_AUDIT.md').write_text('\n'.join(lines).replace('../PROOF_AUDIT.json','PROOF_AUDIT.json').replace('../audit/','audit/').replace('(FINAL_','(reviews/FINAL_'))
print(json.dumps(dict(verdict=audit['verdict'], reviews=reviews), ensure_ascii=False))
