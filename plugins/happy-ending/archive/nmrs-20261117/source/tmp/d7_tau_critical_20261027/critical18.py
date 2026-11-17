"""One eager complete finite D7/tau>=5 decision; Linux only."""
from itertools import combinations
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import platform
import shutil
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from semantic_check import analyze, transversals
N = 18
SOLVER = Path('/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat')


def sha(path):
    with path.open('rb') as f: return hashlib.file_digest(f, 'sha256').hexdigest()


def save(name, data):
    with (HERE / name).open('x') as out: json.dump(data, out, indent=2)


def hclauses(gate, triple_ids):
    return [[-gate, value] for value in triple_ids] + [[gate] + [-v for v in triple_ids]]


def gate_controls():
    ids, gate = list(range(1, 21)), 21
    clauses = hclauses(gate, ids)
    records = []
    for blue in [None] + list(range(20)):
        colors = {i: (blue is None or i != blue + 1) for i in ids}
        for flag in (False, True):
            model = {**colors, gate: flag}
            satisfied = all(any(model[abs(v)] == (v > 0) for v in row) for row in clauses)
            expected = flag == all(colors.values())
            assert satisfied == expected, 'H6 definition control mismatch'
            records.append({'one_blue_triple': blue, 'flag': flag, 'satisfied': satisfied})
    known = json.loads((HERE / 'published_D26_calibration_result.json').read_text())
    colorsraw = json.loads((HERE / 'published_D26_colors.json').read_text())
    colors = {tuple(row['triple']): row['red'] for row in colorsraw['colors']}
    six = known['all_red6'][0]
    assert all(colors[t] for t in combinations(six, 3))
    assert known['red6_transversals']['tau'] == 1
    prior = HERE.parent / 'd7_global_critical_20261027/canonical_R11_counterreceipt.json'
    r11 = json.loads(prior.read_text())
    assert r11['semantic_check']['D7_valid'] and r11['transversals']['tau'] == 2
    save('H6_gate_controls.json', {'status': 'PASS', 'gate_assignments_checked': records,
        'known_actual_R6': six, 'published_D26_tau': 1, 'actual_R11_tau': 2,
        'fixture_meaning': 'domain-positive, tau>=5-negative',
        'old_R11_source_sha256': sha(prior), 'solver_invocations': 0})


def build(base):
    basedir = HERE / 'base_domain18'
    basedir.mkdir(exist_ok=False)
    for name in ('semantic_check.py', 'MATHEMATICAL_ENCODING_SPEC.md'):
        shutil.copyfile(HERE / name, basedir / name)
    base.N, base.HERE = N, basedir
    triples, base_binding = base.build()
    ledger = json.loads((basedir / 'variable_ledger.json').read_text())
    hflags = {}
    for six in combinations(range(N), 6):
        hflags[six] = len(ledger) + 1
        ledger.append({'id': len(ledger) + 1, 'key': ['exact_actual_red6', *six]})
    body = HERE / 'critical18.body'
    definitions, deletions, deletion_literals = 0, 0, 0
    with body.open('xb') as out, (basedir / 'decision.body').open('rb') as src:
        shutil.copyfileobj(src, out)
        for six, gate in hflags.items():
            values = [triples[t] for t in combinations(six, 3)]
            for row in hclauses(gate, values):
                out.write((' '.join(map(str, row)) + ' 0\n').encode())
                definitions += 1
        for deleted in combinations(range(N), 4):
            remaining = [v for v in range(N) if v not in deleted]
            values = [hflags[six] for six in combinations(remaining, 6)]
            assert len(values) == 3003
            out.write((' '.join(map(str, values)) + ' 0\n').encode())
            deletions += 1
            deletion_literals += len(values)
    clauses = base_binding['clauses'] + definitions + deletions
    with (HERE / 'critical18.cnf').open('xb') as out, body.open('rb') as src:
        out.write(f'p cnf {len(ledger)} {clauses}\n'.encode())
        shutil.copyfileobj(src, out)
    save('critical18_ledger.json', ledger)
    binding = {'schema': 'complete_D7_order18_exact_all_red6_all_four_deletions_v1',
        'n': N, 'triple_colors': 816, 'packets': 3060,
        'base_variables': base_binding['variables'], 'base_clauses': base_binding['clauses'],
        'base_groups': base_binding['groups'], 'H6_flags': len(hflags),
        'H6_definition_clauses': definitions, 'four_deletion_clauses': deletions,
        'deletion_clause_length': 3003, 'all_deletion_literals': deletion_literals,
        'variables': len(ledger), 'clauses': clauses,
        'cnf_sha256': sha(HERE / 'critical18.cnf'), 'ledger_sha256': sha(HERE / 'critical18_ledger.json'),
        'source_bindings': {str(p): sha(p) for p in [Path(__file__), HERE / 'base_D7_builder.py',
             HERE / 'semantic_check.py', HERE / 'MATHEMATICAL_ENCODING_SPEC.md', SOLVER,
             HERE / 'H6_gate_controls.json']},
        'base_metadata_note': 'Base copy preserves static order30 schema/packet label; authoritative finite binding here states actual n18/3060 packets and measured clause groups.',
        'no_endpoint_or_template_assumptions': True, 'all_positive_flags_exact': True,
        'theorem_credit': False, 'production_acceptance': False}
    assert len(hflags) == 18564 and definitions == 389844 and deletions == 3060 and deletion_literals == 9189180
    save('critical18_binding.json', binding)
    base.HERE = HERE
    return triples, binding


def sat_check(raw, triples, binding):
    model = {}
    for line in raw.splitlines():
        if line.startswith('v '):
            for token in line.split()[1:]:
                value = int(token)
                if value: model[abs(value)] = value > 0
    assert set(model) == set(range(1, binding['variables'] + 1)), 'partial SAT model'
    checked_clauses = 0
    with (HERE / 'critical18.cnf').open() as src:
        for line in src:
            if line.startswith('p'): continue
            row = [int(v) for v in line.split()[:-1]]
            assert any(model[abs(v)] == (v > 0) for v in row), 'CNF violation'
            checked_clauses += 1
    colors = {t: model[v] for t, v in triples.items()}
    save('critical18_sat_colors.json', {'n': N, 'colors': [{'triple': t, 'red': c} for t, c in colors.items()]})
    save('critical18_full_model.json', model)
    semantic = analyze(colors, N)
    semantic.pop('_endpoints')
    semantic['red6_transversals'] = transversals(colors, N)
    red6 = semantic['red6_transversals']['red6_masks']
    failed = []
    for deleted in combinations(range(N), 4):
        mask = sum(1 << v for v in deleted)
        if not any(not edge & mask for edge in red6): failed.append(deleted)
    semantic['four_deletions_directly_checked'] = 3060
    semantic['four_point_covers_found'] = failed
    semantic['clausewise_checked'] = checked_clauses
    valid = semantic['D7_valid'] and not failed and semantic['red6_transversals'].get('tau') == 5
    semantic['actual_tau5_counterexample'] = valid
    save('critical18_sat_semantics.json', semantic)
    return valid


def main():
    assert platform.system() == 'Linux'
    if (HERE / 'solver_launch.json').exists() or (HERE / 'critical18_result.json').exists():
        raise FileExistsError('one-shot decision already started')
    spec = importlib.util.spec_from_file_location('immutable_base', HERE / 'base_D7_builder.py')
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    gate_controls()
    triples, binding = build(base)
    save('critical18_prepared.json', {'status': 'PREPARED', 'binding': binding,
        'solver_invocations_so_far': 0, 'scope': 'exact order18 only'})
    run = base.controlled([str(SOLVER), '--time=180', str(HERE / 'critical18.cnf'),
                           str(HERE / 'critical18.drat')], 'solver', 180, 3)
    report = {'schema': 'one_shot_order18_D7_tau5_decision_v1', 'binding': binding,
              'solver': run, 'solver_invocations': 1, 'independent_review': False,
              'production_acceptance': False, 'scope': 'exact order18 target only; no other-order or global upper bound'}
    raw = (HERE / 'solver.stdout').read_text()
    if run['exit_code'] == 10 and 's SATISFIABLE' in raw:
        report['status'] = 'SAT_ACTUAL_TAU5_CHECKED' if sat_check(raw, triples, binding) else 'SAT_SEMANTIC_FAILURE'
    elif run['exit_code'] == 20 and 's UNSATISFIABLE' in raw:
        report['status'] = 'RAW_UNSAT_ORDER18_UNACCEPTED'
        proof = HERE / 'critical18.drat'
        report['proof'] = {'bytes': proof.stat().st_size if proof.exists() else 0,
                           'sha256': sha(proof) if proof.exists() else None}
        candidates = [Path('/data/ktqiu_hdd/math_agent/drat-trim/drat-trim'),
                      Path('/data/ktqiu_hdd/math_agent/cadical-sc2025/test/cnf/drat-trim'),
                      HERE.parent / 'balanced49_saturated_exchange_20261026/drat-trim']
        checker = next((p for p in candidates if p.is_file() and os.access(p, os.X_OK)), None)
        if checker and report['proof']['bytes']:
            report['checker_binding'] = {'path': str(checker), 'sha256': sha(checker)}
            outcome = base.controlled([str(checker), str(HERE / 'critical18.cnf'), str(proof), '-t', '60'], 'proof_check', 65, 3)
            report['proof_check'] = outcome
            if outcome['exit_code'] == 0 and 's VERIFIED' in (HERE / 'proof_check.stdout').read_text():
                report['status'] = 'UNSAT_ORDER18_PROOF_CHECKED_UNACCEPTED'
        else: report['proof_check'] = {'status': 'UNAVAILABLE'}
    else: report['status'] = 'TIMEOUT_UNDECIDED' if run['timed_out'] or run['exit_code'] in (0, -9, -15, -24) else 'EXECUTION_ERROR'
    report['final_cnf_sha256'] = sha(HERE / 'critical18.cnf')
    assert report['final_cnf_sha256'] == binding['cnf_sha256']
    save('critical18_result.json', report)
    print(json.dumps({'status': report['status'], 'solver': run,
                      'variables': binding['variables'], 'clauses': binding['clauses']}, indent=2))


if __name__ == '__main__': main()
