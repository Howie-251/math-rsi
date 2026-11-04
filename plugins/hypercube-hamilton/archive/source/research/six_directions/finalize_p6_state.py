"""Publish P6 only after the final independent assembly gates are accepted.

This is a ledger publisher, not a replacement mathematical proof checker.
Run without --publish to inspect the release prerequisites without mutation.
"""
from pathlib import Path
import argparse
import hashlib
import json

R = Path(__file__).resolve().parent
GATES = {
    'FOURTEEN_HOLE_FULL_REVIEW.json': ('full_fourteen_hole_proved',),
    'SIXTEEN_EIGHTEEN_FULL_REVIEW.json': (
        'full_sixteen_hole_proved', 'full_eighteen_hole_proved'),
    'P6_FULL_REVIEW.json': ('full_P6_proved',),
}
MAPS = ('audited_input_hashes', 'imported_dependency_hashes',
        'checker_artifact_hashes', 'audit_artifact_hashes',
        'producer_comparison_hashes', 'accepted_import_source_bindings',
        'evidence_hashes')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    cache = {}
    checked = {}

    def sha(name):
        p = (R / name).resolve()
        stat = p.stat()
        key = (str(p), stat.st_size, stat.st_mtime_ns)
        if key not in cache:
            h = hashlib.sha256()
            with p.open('rb') as stream:
                for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b''):
                    h.update(chunk)
            cache[key] = h.hexdigest()
        return cache[key]

    def bind(owner, name, expected):
        actual = sha(name)
        if actual != expected.removeprefix('sha256:'):
            raise ValueError(f'Stale binding: {owner} -> {name}')
        checked[name] = actual

    reports = {}
    for name, claims in GATES.items():
        p = R / name
        if not p.exists():
            raise SystemExit(f'Pending independent gate: {name}; no state changed.')
        report = json.loads(p.read_text(encoding='utf-8-sig'))
        assert report['verdict'] == 'PASS', name
        assert report['audited_input_hashes'], name
        for claim in claims:
            assert report['details'].get(claim) is True, (name, claim)
        for field in MAPS:
            for item, value in report.get(field, {}).items():
                bind(name, item, value)
        for imp in report.get('formal_imports', []):
            bind(name, imp['file'], imp['sha256'])
        report_hash = report.get('report_hash', report.get('report_sha256'))
        assert report_hash, (name, 'missing human-readable review hash')
        bind(name, report.get('trace_path', name.replace('.json', '.md')), report_hash)
        reports[name] = report

    final = reports['P6_FULL_REVIEW.json']
    assert final['details']['all_original_short_matchings'] is True
    assert final['details']['every_free_root'] is True
    assert final['details']['every_opposite_parity_target_including_covered'] is True
    assert final['details']['all_predecessor_conditions_discharged'] is True
    assert final['details']['dependency_DAG_acyclic'] is True
    assert final['details']['remaining_full_p6_hole_levels'] == []
    # The final gate must itself import both newly accepted complete layers.
    final_bindings = {}
    for field in MAPS:
        final_bindings.update(final.get(field, {}))
    for gate in tuple(GATES)[:2]:
        assert final_bindings.get(gate, '').removeprefix('sha256:') == sha(gate)
    assert final_bindings.get('P6_FULL_CLOSURE.md', '').removeprefix('sha256:') == sha('P6_FULL_CLOSURE.md')
    gate_hashes = {name: sha(name) for name in GATES}
    result = {
        'status': 'PASS_RELATIVE_TO_EXPLICIT_IMPORTS',
        'full_p6_proved': True,
        'review_independence': 'same-family',
        'acceptance_status': 'provisional',
        'proof_assistant_verified': False,
        'gate_hashes': gate_hashes,
        'live_direct_bindings_checked': len(checked),
        'published': args.publish,
    }
    if args.publish:
        # Prepare both documents before changing either ledger.
        updates = {}
        for name in ('RUN_STATE.json', 'PROOF_CHECK_STATE.json'):
            p = R / name
            d = json.loads(p.read_text(encoding='utf-8'))
            if name == 'RUN_STATE.json':
                d.setdefault('historical_original_target', d.get('target'))
                d['target'] = 'P6: arbitrary Q6 edge matching, every free root and opposite-parity target'
                d['status'] = 'PROVABLE AS STATED'
                d['active_research_priority'] = 'Complete P6 accepted; no remaining P6 proof obligations.'
                d['latest_proof_package'] = 'P6_FULL_CLOSURE.md'
                d['remaining_structure'] = 'All complete layers 2,4,6,8,10,12,14,16,18 and rooted reduction accepted.'
                d['last_goal_turn_classification'] = 'progress'
                d['remaining_cnf_is_current_obligation'] = False
            else:
                d['status'] = 'completed_full_p6_review'
                d['acceptance_gate'] = 'P6_FULL_REVIEW.json'
                d['latest_package'] = 'Complete P6 with all prescribed-endpoint quantifiers'
                d['latest_review_files'] = list(GATES)
            d.update(full_fourteen_hole_proved=True, full_sixteen_hole_proved=True,
                     full_eighteen_hole_proved=True, full_p6_proved=True,
                     fourteen_hole_covered_targets_proved=True,
                     remaining_full_p6_hole_levels=[],
                     remaining_p6_proof_obligations=[],
                     final_p6_acceptance=result)
            if 'fourteen_hole_geometry_residual' in d:
                d['fourteen_hole_geometry_residual'].update(
                    review='FOURTEEN_HOLE_FULL_REVIEW.json', covered_remaining=0,
                    covered_by_target={'1': 0, '7': 0, '31': 0}, free_remaining=0,
                    status='Complete fourteen-hole assembly accepted')
            if 'sixteen_hole_conditional_geometry_residual' in d:
                d['sixteen_hole_conditional_geometry_residual'].update(
                    review='SIXTEEN_EIGHTEEN_FULL_REVIEW.json', covered_remaining=0,
                    covered_by_target={'1': 0, '7': 0, '31': 0}, free_remaining=0,
                    predecessor_discharged=True,
                    status='Full14 predecessor discharged; complete sixteen/eighteen-hole assembly accepted')
            if 'eighteen_hole_conditional_closure' in d:
                d['eighteen_hole_conditional_closure'].update(
                    review='SIXTEEN_EIGHTEEN_FULL_REVIEW.json',
                    predecessor_discharged=True,
                    status='Full16 predecessor discharged; complete eighteen-hole theorem accepted')
            updates[p] = json.dumps(d, ensure_ascii=False, indent=2) + '\n'
        for p, content in updates.items():
            tmp = p.with_suffix('.publish.tmp')
            tmp.write_text(content, encoding='utf-8')
            tmp.replace(p)
        (R / 'P6_RELEASE_CHECK.json').write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
