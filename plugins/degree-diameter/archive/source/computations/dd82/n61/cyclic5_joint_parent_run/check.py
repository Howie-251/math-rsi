"""Ordinary adjacency-matrix/set verification; no C++ masks or score shortcuts."""
from collections import Counter
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parent / 'cyclic5_h35_run'
DS = ([0, 0, 0, 1, 2, 3, 4], [0, 0, 1, 1, 2, 3, 4])
OLD_P = [0, 2, 3, 4, 5, 6, 1]
OLD_Q = [2, 0, 6, 1, 3, 4, 5]


def inherited_prefix():
    result = json.loads((OLD / 'result.json').read_text())
    packing = json.loads((OLD / 'packing_result.json').read_text())
    candidate = result['candidate']
    assert result['status'] == 'FRONTEND_FOUND'
    assert result['types'][0]['compatible_pairs_checked'] == 116
    assert result['types'][0]['pointwise_pass'] == 1
    assert result['types'][1]['compatible_pairs_checked'] == 0
    assert candidate['type'] == 0 and candidate['d'] == DS[0]
    assert candidate['p'] == OLD_P and candidate['q'] == OLD_Q
    assert packing['status'] == 'EXHAUSTED_NO_PACKING' and packing['complete']
    assert packing['six_packings_checked'] == 70 and packing['color_pass'] == 0
    return dict(type=0, skipped_compatible_prefix=116,
                first_115='pointwise rho failed in saved original run',
                item_116='saved fixed H has all 70 six-packings, zero colors_21111',
                result_source='../cyclic5_h35_run/result.json',
                packing_source='../cyclic5_h35_run/packing_result.json')


def graph_check(candidate, supplied_edges=None):
    d, p, q = candidate['d'], candidate['p'], candidate['q']
    assert d == DS[candidate['type']]
    assert sorted(p) == sorted(q) == list(range(7))
    expected = set()
    for r in range(7):
        for i in range(5):
            for perm, step in ((p, 1), (q, 2)):
                expected.add(tuple(sorted((5*r+i, 5*perm[r]+(i+step) % 5))))
    edges = list(expected) if supplied_edges is None else [tuple(e) for e in supplied_edges]
    assert len(edges) == len(set(edges)) == 70 and set(edges) == expected
    matrix = [[0]*35 for _ in range(35)]
    for x, y in edges:
        assert 0 <= x < y < 35
        matrix[x][y] = matrix[y][x] = 1
    assert all(sum(row) == 4 for row in matrix)
    neighbors = [{v for v in range(35) if matrix[z][v]} for z in range(35)]
    closed = [neighbors[z] | {z} for z in range(35)]
    f = [z % 5 for z in range(35)]
    g = [(z % 5 + d[z//5]) % 5 for z in range(35)]
    local = all(sorted(c[v] for v in closed[z]) == list(range(5))
                for c in (f, g) for z in range(35))
    intersection = [[sum(f[z] == i and g[z] == j for z in range(35))
                     for j in range(5)] for i in range(5)]
    expected_intersection = [[1 + (i == j) + (j == (i + candidate['type']) % 5)
                              for j in range(5)] for i in range(5)]
    assert intersection == expected_intersection
    h2 = [[sum(matrix[z][h]*matrix[h][v] for h in range(35))
           for v in range(35)] for z in range(35)]
    covered, rho, geometric = [], [], []
    for z in range(35):
        routes = [matrix[z][v] + h2[z][v] + int(f[z] == f[v]) + int(g[z] == g[v])
                  for v in range(35)]
        covered.append({v for v in range(35) if v != z and routes[v] > 0})
        rho.append(sum(max(routes[v]-1, 0) for v in range(35) if v != z))
        geometric.append(16 - sum(matrix[z][v] + h2[z][v] > 0 for v in range(35) if v != z)
                         + intersection[f[z]][g[z]] - 1)
    assert geometric == [r for r in candidate['rho_orbit'] for _ in range(5)]
    assert max(geometric) == candidate['max_rho'] and sum(geometric) == candidate['sum_rho']
    if local:
        assert rho == geometric
        assert all(rho[z] == 28-len(covered[z]) for z in range(35))
    holes = [set(range(35)) - {z} - covered[z] for z in range(35)]
    report = dict(edges=70, degrees=[4]*35, f=f, g=g, intersection=intersection,
                  two_local_colorings=local, rho=rho, max_rho=max(rho), sum_rho=sum(rho),
                  rho_frontend_pass=local and max(rho) <= 4 and sum(rho) <= 130)
    data = dict(neighbors=neighbors, closed=closed, f=f, g=g, rho=rho,
                covered=covered, holes=holes)
    return data, report


def independent(data, vertices):
    return all(not (data['neighbors'][v] & vertices) for v in vertices)


def root_parent(data, z, parent):
    outside = data['holes'][z] - parent
    return len(outside) <= 5 and independent(data, outside), outside


def parent_check(data, a, supplied_p=None):
    A = set(a)
    assert len(A) == len(a)
    balls = [data['closed'][v] for v in A]
    packing = len(A) == 6 and all(not (x & y) for k, x in enumerate(balls) for y in balls[k+1:])
    occupied = set().union(*balls) if balls else set()
    P = set(range(35)) - occupied
    if supplied_p is not None:
        assert len(set(supplied_p)) == len(supplied_p) and P == set(supplied_p)
    colors = all(sorted(Counter(data[c][v] for v in A).values()) == [1,1,1,1,2]
                 for c in ('f', 'g'))
    ap_missing = [[a, p] for a in sorted(A) for p in sorted(P) if p not in data['covered'][a]]
    a_out = {a: root_parent(data, a, A) for a in sorted(A)}
    p_out = {p: root_parent(data, p, P) for p in sorted(P)}
    checks = dict(packing=packing, colors_21111=colors,
                  P_independent=len(P) == 5 and independent(data, P),
                  P_rho_at_most3=len(P) == 5 and all(data['rho'][p] <= 3 for p in P),
                  AP_covered=not ap_missing,
                  A_Rout=all(ok for ok, outside in a_out.values()),
                  P_Rout=all(ok for ok, outside in p_out.values()))
    checks['pass'] = all(checks.values())
    if packing and data.get('local', True):
        assert all(sorted(data[c][p] for p in P) == list(range(5)) for c in ('f', 'g'))
    report = dict(A=sorted(A), P=sorted(P), checks=checks, AP_uncovered=ap_missing,
                  A_Rout={str(z): sorted(outside) for z, (ok, outside) in a_out.items()},
                  P_Rout={str(z): sorted(outside) for z, (ok, outside) in p_out.items()})
    return report


def ordinary_set_packings(data):
    """Independent small regression enumeration using disjoint closed sets."""
    leaves = []
    def dfs(chosen, candidates):
        if len(chosen) == 6:
            leaves.append(tuple(chosen))
            return
        for k, v in enumerate(candidates):
            if len(candidates)-k < 6-len(chosen):
                break
            after = [w for w in candidates[k+1:] if not (data['closed'][v] & data['closed'][w])]
            dfs(chosen+[v], after)
    dfs([], list(range(35)))
    return leaves


def check_sanity():
    raw = json.loads((ROOT/'sanity_cpp.json').read_text())
    reports = []
    old_data = None
    for case in raw['graph_cases']:
        data, report = graph_check(case['candidate'], case['edges'])
        assert report['two_local_colorings'] == case['signature_accept']
        reports.append(report)
        if case['candidate']['p'] == OLD_P and case['candidate']['q'] == OLD_Q:
            old_data = data
    assert old_data is not None
    assert [r['two_local_colorings'] for r in reports] == [True, True, False, True]
    saved_edges = [list(map(int, line.split())) for line in (OLD/'candidate.edges').read_text().splitlines()]
    assert sorted(saved_edges) == sorted(raw['graph_cases'][-1]['edges'])
    old = raw['old_packing']
    assert old['complete'] and old['stats']['six_packings'] == 70 and old['stats']['color_pass'] == 0
    direct_leaves = ordinary_set_packings(old_data)
    assert len(direct_leaves) == 70
    assert {tuple(x['A']) for x in old['leaves']} == set(direct_leaves)
    for leaf in old['leaves']:
        assert parent_check(old_data, leaf['A'], leaf['P'])['checks'] == leaf['checks']
    ap_results = []
    for probe in raw['AP_probes']:
        ok = all(p in old_data['covered'][a] for a in probe['A'] for p in probe['P'])
        assert ok == probe['pass']
        ap_results.append(ok)
    assert ap_results == [True, False]
    rout_results = []
    for probe in raw['Rout_probes']:
        ok, outside = root_parent(old_data, probe['root'], set(probe['parent']))
        assert ok == probe['pass'] and outside == set(probe['outside'])
        rout_results.append(dict(pass_=ok, outside=sorted(outside)))
    assert [x['pass_'] for x in rout_results] == [True, False, False]
    interrupted = raw['interrupted_packing']
    assert interrupted['limited'] and not interrupted['complete'] and not interrupted['found']
    assert interrupted['stats']['nodes'] == 2 and interrupted['stats']['six_packings'] == 0
    return dict(status='PASS', inherited_prefix=inherited_prefix(), graph_cases=reports,
                old_six_packings=70, old_color_pass=0, all_70_parent_evaluations_agree=True,
                AP_operator_probes=ap_results, Rout_operator_probes=rout_results,
                interrupted_packing=interrupted,
                scope='Small semantics only; AP/Rout probes test individual predicates, not complete frontends.')


def check_result():
    result = json.loads((ROOT/'result.json').read_text())
    status = result['status']
    if result.get('partial_counters_unavailable'):
        assert not result['complete'] and status in ('INCOMPLETE_RESOURCE_LIMIT', 'PROCESS_ERROR')
        return dict(status='NO_FRONTEND_TO_VERIFY', production_status=status, complete=False)
    assert result['type_order'] == [1, 0]
    for stats in result['types']:
        assert stats['compatible_pairs_seen'] == stats['skipped_inherited'] + stats['checked_this_run']
        assert stats['skipped_inherited'] == (min(116, stats['compatible_pairs_seen']) if stats['type'] == 0 else 0)
        assert stats['packing_exhausted'] <= stats['packing_started'] <= stats['rho_pass_this_run']
        if stats['complete']:
            assert stats['started'] and stats['packing_exhausted'] == stats['packing_started']
    assert result['complete'] == all(s['complete'] for s in result['types'])
    if status != 'JOINT_PARENT_FRONTEND_FOUND':
        assert status in ('EXHAUSTED_NO_JOINT_PARENT_FRONTEND', 'INCOMPLETE_RESOURCE_LIMIT')
        assert (status == 'EXHAUSTED_NO_JOINT_PARENT_FRONTEND') == result['complete']
        assert result['candidate'] is None and not result['A'] and not result['P']
        return dict(status='NO_FRONTEND_TO_VERIFY', production_status=status, complete=result['complete'])
    assert not result['complete']
    edges = [list(map(int, line.split())) for line in (ROOT/'candidate.edges').read_text().splitlines()]
    data, graph_report = graph_check(result['candidate'], edges)
    assert graph_report['rho_frontend_pass']
    parents = parent_check(data, result['A'], result['P'])
    assert parents['checks']['pass']
    saved = json.loads((ROOT/'candidate_parent.json').read_text())
    assert saved['A'] == result['A'] and saved['P'] == result['P']
    assert saved['checks'] == parents['checks']
    return dict(status='PASS', graph=graph_report, parents=parents,
                scope='Necessary H/f/g/A/P frontend only; not a 61-vertex graph.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('sanity', 'result'))
    args = parser.parse_args()
    print(json.dumps(check_sanity() if args.mode == 'sanity' else check_result(), indent=2))
