"""Emit this audit's input manifest and machine-readable obligation ledger."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
names = [
    'FOUR_HOLE_FULL.md', 'SINGLE_ODD_HOLE_COMPLETION.md',
    'MIXED_TWO_HOLE_TRANSFER.md', 'THREE_ODD_HOLES_TRANSFER.md',
    'TWO_ODD_HOLES_TRANSFER.md', 'AVOIDED_VERTEX_TRANSFER.md',
    'DISTANCE_TWO_ALL_TARGETS.md', 'GENERAL_NEAR_PERFECT.md',
    'BIPARTITE_NEAR_PERFECT.md', 'paper.txt',
    'verify_recut.py', 'verify_two_odd_holes.py', 'verify_conflict_cycles.py',
    'recut_results.json', 'two_odd_holes_results.json',
    'conflict_cycle_results.json', 'HOLE_RANGE_AND_COMPLETION.md',
]
hashes = {name: 'sha256:' + hashlib.sha256((root / name).read_bytes()).hexdigest()
          for name in names}
for path in [root.parent.parent / '2501.19029v1.pdf',
             Path('F:/c4free-hypercube-main/ARIS/skills/skills-codex/proof-writer/SKILL.md'),
             Path('F:/c4free-hypercube-main/ARIS/skills/skills-codex/proof-checker/SKILL.md')]:
    hashes[path.as_posix()] = 'sha256:' + hashlib.sha256(path.read_bytes()).hexdigest()

report = root / 'FOUR_HOLE_SOL_HIGH_REVIEW.md'
obligations = []
for lineno, line in enumerate(report.read_text(encoding='utf-8').splitlines(), 1):
    if re.match(r'^\| (?:[GH]\d+|[NZE]\d+(?:\.\d+)?) \|', line):
        parts = line[2:-2].split(' | ', 2)
        obligations.append(dict(id=parts[0].strip(),
                                assumptions_and_goal=parts[1].strip(),
                                derivation=parts[2].strip(),
                                status='closed_modulo_declared_imports',
                                location=f'{report.name}:L{lineno}'))

data = dict(
    audit_skill='proof-checker', writer_skill='proof-writer',
    verdict='PASS', reason_code='all_proofs_complete_modulo_declared_imports',
    summary='Z18 four-hole short-matching claim survives unchanged; no substantive gap found. Same-family provisional semantic review, not a formal proof or full P6.',
    proof_status='PROVABLE AS STATED',
    requested_model='gpt-6.1-sol', requested_effort='high',
    executor_model='runtime-not-attested', executor_family='openai',
    reviewer_model='gpt-6.1-sol', reviewer_family='openai', reviewer_reasoning='high',
    reviewer_configuration_source='Parent spawn_agent request; not reviewer self-attestation of served backend model.',
    reviewer_task='/root/four_hole_sol_high_audit',
    review_independence='same-family', acceptance_status='provisional',
    independent_context=True, cross_family_review=False, formalized=False,
    user_configuration_overrides_skill_defaults=True,
    subagents_spawned=0, review_rounds=1,
    prior_audit_verdicts_used_as_evidence=False, main_proofs_modified=False,
    full_p6_proved=False, exhaustive_q6=False,
    audited_input_hashes=hashes,
    report_sha256='sha256:' + hashlib.sha256(report.read_bytes()).hexdigest(),
    trace_path=report.as_posix(), generated_at=datetime.now(timezone.utc).isoformat(),
    external_sources=[dict(url='https://tmuetze.de/papers/match.pdf',
                          inspected_pages=[1,3,4], theorems=[2,8,9,12],
                          access='web PDF text', raw_pdf_sha256=None,
                          hash_limitation='Direct byte download blocked by local network sandbox; source text read successfully through web tool.'),
                      dict(local_input=(root / 'paper.txt').as_posix(), theorem=8,
                           prohibitions_checked=['C1','C2','C3'])],
    details=dict(theorems_audited=14, obligations=obligations,
                 open_obligations=[], issues=[],
                 fatal=0, critical=0, major=0, minor=0,
                 supplements=['parity-count forcing of the second same-parity hole',
                              'no isolated vertices after deleting auxiliary matching',
                              'double compression half-layer identity, including candidates u/h',
                              'E2 applied to the same actual global matching with long hu',
                              'exhaustive second-coordinate elimination in Z18'],
                 counterexample_pass='Executed structural attacks listed in report; no verified counterexample. This is not exhaustive enumeration.',
                 supplementary_hole_bound=dict(graph_edges=186, max_degree=6,
                                                max_edges_dominated_by_one_matching_edge=11,
                                                minimum_maximal_matching_size=17,
                                                maximum_holes_after_root_preserving_maximal_completion=30,
                                                tightness_claimed=False)),
    certificate_checks=[dict(script='verify_recut.py',status='PASS',verified=9),
                        dict(script='verify_two_odd_holes.py',status='PASS',verified=81,
                             root_sides=dict(A=53,B=28),artificial_cross=32),
                        dict(script='verify_conflict_cycles.py',status='PASS',verified=12,
                             modes=dict(Z15=3,Z16=9),conflict_edge_is_hu=1)],
    evidence_boundary='Certificate checks cover only the saved witnesses. The universal claim rests on the analytic obligation ledger and declared external theorems.',
)
assert len(obligations) >= 40
target = root / 'FOUR_HOLE_SOL_HIGH_REVIEW.json'
target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(verdict=data['verdict'],obligations=len(obligations),
                      input_files=len(hashes),full_p6_proved=False)))
