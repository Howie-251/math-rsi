"""Emit fixed-scope independent audit after semantic review; hashes are byte hashes."""
from pathlib import Path
import datetime
import hashlib
import json
import re

B = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
read = lambda p: json.loads(Path(p).read_text(encoding='utf-8'))
manifest = read(B/'R7_NEAR_BALANCED_BLOCKS_INPUTS.json')
assert sha(B/'R7_NEAR_BALANCED_BLOCKS.md') == 'f14078566876269bfd0c4f6d64a016b720872129e612307037c07571f8ab0e89'
assert sha(B/'R7_NEAR_BALANCED_BLOCKS_INPUTS.json') == '3a94390fb6a2db67659d18faa08ea00c57dfcc9361222739dded3ebed382e510'
for group in ('author_artifacts','direct_imports_and_comparisons','reference_state_only'):
    for name, expected in manifest[group].items():
        assert sha(B/name) == expected.removeprefix('sha256:'), (group, name)
checks = []
for report, section, source in (
    ('../six_directions/Q5_A10_FULL_REVIEW.json','audited_input_hashes','Q5_A10_FULL_CLOSURE.md'),
    ('../six_directions/P6_FULL_REVIEW.json','audited_input_hashes','P6_FULL_CLOSURE.md'),
    ('R7_BALANCED_Q5_BLOCKS_REVIEW.json','audited_input_hashes','R7_BALANCED_Q5_BLOCKS.md'),
    ('Q7_EIGHT_NINE_CUTS_REVIEW.json','audited_input_hashes','Q7_EIGHT_NINE_CUTS.md'),
    ('Q7_EIGHT_NINE_CUTS_REVIEW.json','imported_dependency_hashes','PROOF_PACKAGE.md')):
    p = B/report
    d = read(p)
    assert d['verdict'] == 'PASS'
    expected = d[section][source].removeprefix('sha256:')
    assert sha(p.parent/source) == expected
    checks.append(dict(report=report, source=source, expected=expected, status='PASS'))
extra = ['R7_TWO_CROSS_SEPARATING_FACE.md','R7_TWO_CROSS_SINGLE_INTERNAL.md',
         'R7_SINGLE_I_FLEXIBLE_EAR.md','R7_SINGLE_I_SOURCE_CUT.md']
md = (B/'R7_NEAR_BALANCED_BLOCKS_REVIEW.md').read_text(encoding='utf-8')
obligations = []
for line in md.splitlines():
    if re.match(r'\| [CQSWG][0-9]{2} \|', line):
        _, ident, location, discharge, _ = line.split('|')
        obligations.append(dict(id=ident.strip(),status='PASS',location=location.strip(),discharge=discharge.strip()))
assert len(obligations) == 31
arithmetic = read(B/'R7_NEAR_BALANCED_BLOCKS_REVIEW_check.json')
assert arithmetic['status'] == 'PASS'
assert arithmetic['source_sha256'] == sha(B/'R7_NEAR_BALANCED_FIXED_WITNESS.json')
inputs = {name: sha(B/name) for name in (
    'R7_NEAR_BALANCED_BLOCKS.md','R7_NEAR_BALANCED_BLOCKS_INPUTS.json',
    'R7_NEAR_BALANCED_FIXED_WITNESS.md','R7_NEAR_BALANCED_FIXED_WITNESS.json')}
artifacts = {name:sha(B/name) for name in (
    'R7_NEAR_BALANCED_BLOCKS_REVIEW_check.py','R7_NEAR_BALANCED_BLOCKS_REVIEW_check.json',
    'R7_NEAR_BALANCED_BLOCKS_REVIEW_emit.py')}
result = dict(audit_skill='ARIS proof-checker local adaptation under Q7_WORKFLOW',
    verdict='PASS', reason_code='all_scoped_obligations_complete_modulo_explicit_imports',
    summary='C6+, Q+, residual necessary structure and one strictly new fixed input pass modulo explicit accepted imports; full m2/R7/P7 remain open.',
    caller='/root', reviewer_agent='/root/r7_nearbalanced_audit',
    reviewer_model='gpt-6.1-sol', reviewer_reasoning='high',
    model_configuration_source='Explicit workspace instruction and caller request; served backend not independently attested',
    backend_identity_independently_certified=False, reviewer_family='openai',
    review_independence='same-family',acceptance_status='provisional',proof_status='sound-modulo-imports',
    generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    audited_input_hashes=inputs,
    imported_dependency_hashes=manifest['direct_imports_and_comparisons'],
    additional_comparison_hashes={name:sha(B/name) for name in extra},
    author_checker_artifact_hashes={'r7_near_balanced_fixed_probe.py':sha(B/'r7_near_balanced_fixed_probe.py')},
    author_manifest_bindings_checked=30, direct_accepted_source_bindings_checked=checks,
    checker_artifact_hashes=artifacts,
    trace_path='R7_NEAR_BALANCED_BLOCKS_REVIEW.md',
    audit_report_sha256=sha(B/'R7_NEAR_BALANCED_BLOCKS_REVIEW.md'),
    skill_sha256=sha('F:/c4free-hypercube-main/ARIS/skills/skills-codex/proof-checker/SKILL.md'),
    external_imports=manifest['external_imports'],
    details=dict(obligations=obligations,issues=[],revisions_required=0,no_open_scoped_obligations=True),
    scope=dict(C6plus=True,Qplus=True,old_Q_included=True,residual_necessary_condition=True,
        all_short_realizations_of_fixed_hole_set=True,
        strict_new_coverage_over_listed_old_rules=True,
        full_two_cross_edge_family=False,full_m2=False,full_R7=False,full_P7=False,
        seven_direction_lift=False,historical4228_reduced=False),
    independent_fixed_arithmetic=arithmetic, solver_calls=0,
    producer_script_executed=False,matching_family_enumeration=False,
    high_hole_family_enumeration=False,large_certificates_replayed=False,
    all_transitive_reports_rehashed=False,transitive_imports_reproved=False,
    run_state_reference_sha256=sha(B/'RUN_STATE.json'),mathematical_closure_state_updated=False)
out = B/'R7_NEAR_BALANCED_BLOCKS_REVIEW.json'
out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(verdict=result['verdict'],obligations=len(obligations),
    author_manifest_bindings_checked=30,direct_accepted_source_bindings_checked=len(checks),
    main_sha256=inputs['R7_NEAR_BALANCED_BLOCKS.md'],
    report_md_sha256=result['audit_report_sha256'],report_json_sha256=sha(out))))
