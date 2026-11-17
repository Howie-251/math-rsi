"""One authorized fixed geometry and one 30-second single-worker CP-SAT call.

No Hamilton constraint, objective, geometry loop, matching enumeration or retry.
Use --verify-only to check saved edges with pure integer arithmetic, no solver.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'R7_NEAR_BALANCED_FIXED_WITNESS.json'
HA = {0, 3, 5, 9, 61, 59, 55, 47}
HB = {x ^ 63 for x in HA}
H = HA | {x + 64 for x in HB}


def verify(edges):
    """Pure arithmetic; takes concrete edges, not solver variables."""
    ends = [x for e in edges for x in e]
    assert len(edges) == 56 and len(ends) == len(set(ends)) == 112
    assert set(range(128)) - set(ends) == H
    assert all(0 <= u < v < 128 and (u ^ v).bit_count() == 1 for u, v in edges)
    counts = [sum(u ^ v == 1 << k for u, v in edges) for k in range(7)]
    assert min(counts) >= 3 and counts[6] == 4
    hole_edges = [[u, v] for u in sorted(H) for v in sorted(H)
                  if u < v and (u ^ v).bit_count() == 1]
    assert not hole_edges
    # Every block count uses actual global colors; a face may swap color names.
    def colors(vertices):
        return [sum(v.bit_count() % 2 == c for v in vertices) for c in (0, 1)]
    faces = []
    for i in range(7):
        fs = []
        for side in range(2):
            hs = [v for v in sorted(H) if (v >> i & 1) == side]
            cuts = []
            for k in range(7):
                if k == i:
                    continue
                cs = [colors([v for v in hs if (v >> k & 1) == t]) for t in (0, 1)]
                cuts.append({'k': k, 'block_color_counts': cs,
                             'balanced': all(a == b for a, b in cs),
                             'nearbalanced': all(abs(a-b) <= 1 for a, b in cs)})
            fs.append({'side': side, 'hole_color_counts': colors(hs), 'internal_cuts': cuts})
        faces.append({'outer_coordinate': i, 'faces': fs})
    q_conditions = []
    for row in faces:
        a, b = row['faces']
        for ca in a['internal_cuts']:
            for cb in b['internal_cuts']:
                q_conditions.append({'outer': row['outer_coordinate'],
                                     'k_A': ca['k'], 'k_B': cb['k'],
                                     'pass': ca['balanced'] and cb['balanced']})
    assert len(q_conditions) == 7*6*6 and not any(t['pass'] for t in q_conditions)
    qplus = faces[6]
    assert all(f['hole_color_counts'] == [4, 4] for f in qplus['faces'])
    assert all(next(c for c in f['internal_cuts'] if c['k'] == 0)['nearbalanced']
               for f in qplus['faces'])
    local_signed = [sum((v >> k & 1) for v in (0, 3, 5, 9))
                    - sum((v >> k & 1) for v in (61, 59, 55, 47)) for k in range(6)]
    assert local_signed == [-1, -2, -2, -2, -3, -4]
    return {'status': 'PASS', 'edge_count': 56, 'holes': sorted(H),
            'direction_counts': counts, 'hole_color_counts': colors(H),
            'hole_adjacent_pairs': hole_edges, 'inclusion_maximal': True,
            'A_local_bit1_signed_margins': local_signed,
            'all_outer_faces_and_internal_cuts': faces,
            'old_Q_all_252_candidates': q_conditions,
            'old_Q_passing_candidates': 0,
            'Qplus_gate': {'outer': 6, 'k_A': 0, 'k_B': 0,
                          'outer_face_hole_color_counts': [f['hole_color_counts'] for f in qplus['faces']],
                          'four_block_color_counts': [c for f in qplus['faces']
                              for c in next(t for t in f['internal_cuts'] if t['k'] == 0)['block_color_counts']]},
            'exclusions': {'T_U_V_W_M_N_F7_F14': 'No direction has exactly two prescribed edges.',
                           'B': '16 holes exceeds the maximum 12 in that rule.',
                           'E8_completion': 'Independent holes make this 56-edge matching inclusion-maximal, so no containing 60-edge matching.',
                           'Q': 'All 252 outer/inner coordinate choices fail.'},
            'scope_limit': 'No unlisted rule is excluded; not an R7 counterexample or a universal source theorem.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    if args.verify_only:
        data = json.loads(OUT.read_text(encoding='utf-8'))
        result = verify(data['edges'])
        assert result == data['arithmetic_verification']
        print(json.dumps({'status': 'PURE_ARITHMETIC_PASS', 'direction_counts': result['direction_counts'],
                          'Qplus_gate': result['Qplus_gate'], 'old_Q_choices': 252}))
        return
    # Accidental re-execution is prevented; a second solver call is unauthorized.
    if OUT.exists():
        raise SystemExit('STOP: output exists; use --verify-only; no second solver call allowed.')
    from ortools.sat.python import cp_model
    import ortools
    model = cp_model.CpModel()
    allowed = [(u, u ^ (1 << k), k) for u in range(128) if u not in H
               for k in range(7) if u < (u ^ (1 << k)) and (u ^ (1 << k)) not in H]
    xs = [model.new_bool_var(f'e_{u}_{v}') for u, v, k in allowed]
    for v in range(128):
        if v not in H:
            model.add_exactly_one(x for x, (a, b, k) in zip(xs, allowed) if v in (a, b))
    for k in range(7):
        total = sum(x for x, (a, b, d) in zip(xs, allowed) if d == k)
        model.add(total >= 3)
        if k == 6:
            model.add(total == 4)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 30.0
    solver.parameters.num_search_workers = 1
    solver.parameters.random_seed = 0
    status = solver.solve(model)  # The only solver invocation.
    result = {'caller': '/root', 'worker': '/root/r7_nearbalanced_fixed_probe',
              'gap': 'R7-2X-SAME', 'scope': 'One fixed hole geometry; one matching witness only.',
              'ortools_version': ortools.__version__, 'solver_calls': 1,
              'solver_parameters': {'max_time_in_seconds': 30, 'num_search_workers': 1, 'random_seed': 0},
              'solver_status': solver.status_name(status), 'solver_wall_time': solver.wall_time,
              'has_hamilton_constraint': False, 'has_objective': False,
              'A_local_holes': sorted(HA), 'B_local_holes': sorted(HB)}
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        edges = [[u, v] for x, (u, v, k) in zip(xs, allowed) if solver.value(x)]
        result['edges'] = edges
        result['arithmetic_verification'] = verify(edges)
    else:
        result['scope_limit'] = 'No witness obtained; stop without retry or changed geometry.'
    result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('edges', 'arithmetic_verification')}, ensure_ascii=False))
    if 'arithmetic_verification' in result:
        print(json.dumps({'direction_counts': result['arithmetic_verification']['direction_counts'],
                          'Qplus_gate': result['arithmetic_verification']['Qplus_gate']}))


if __name__ == '__main__':
    main()
