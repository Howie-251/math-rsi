import time
START = time.process_time()
WALL = time.time()
import resource
resource.setrlimit(resource.RLIMIT_CPU, (5, 6))
import csv
import itertools
import json
from collections import Counter
from pathlib import Path

D = Path(__file__).resolve().parent
BASE = D.parents[1]
P = json.loads((BASE / 'PARAMETERS.json').read_text())
I = json.loads((D.parent / 'fixed_support_max_capacity_lp/ALL_ADMISSIBLE_AFFINE_INTERFACE.json').read_text())
RET = [31, 59, 60, 72]
ALLOW = [16, 17, 30, 32, 35, 42, 43, 44, 45, 58, 61, 64, 71, 73, 74]
assert I['retained'] == RET and I['all_admissible'] == ALLOW
C, MU = P['controller'], P['field']['multiplication']
INV = P['field']['inverses']
ADD = [[(a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3) for b in range(9)] for a in range(9)]
NEG = [(-a % 3) + 3 * (-(a // 3) % 3) for a in range(9)]

def add(a, b):
    return ADD[a][b]

def sub(a, b):
    return ADD[a][NEG[b]]

def dot(a, b):
    out = 0
    for x, y in zip(a, b):
        out = ADD[out][MU[x][y]]
    return out

def scale(c, v):
    return [MU[c][x] for x in v]

def norm(v):
    c = next((x for x in v if x), None)
    return None if c is None else scale(INV[c], v)

def cross(a, b):
    return [sub(MU[a[1]][b[2]], MU[a[2]][b[1]]),
            sub(MU[a[2]][b[0]], MU[a[0]][b[2]]),
            sub(MU[a[0]][b[1]], MU[a[1]][b[0]])]

def mv(m, v):
    return [dot(row, v) for row in m]

def rowmat(v, m):
    return [dot(v, [m[r][c] for r in range(3)]) for c in range(3)]

def rank(rows):
    rows = [list(r) for r in rows]
    if not rows:
        return 0
    n, r = len(rows[0]), 0
    for c in range(n):
        pivot = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        rows[r] = scale(INV[rows[r][c]], rows[r])
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                coeff = rows[i][c]
                rows[i] = [sub(x, MU[coeff][y]) for x, y in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r

def plane_basis(a):
    k = next(i for i, x in enumerate(a) if x)
    out = []
    for j in range(3):
        if j == k:
            continue
        v = [0, 0, 0]
        v[j] = 1
        v[k] = NEG[MU[INV[a[k]]][a[j]]]
        assert dot(a, v) == 0
        out.append(v)
    return out

def dart(u, p):
    chart = P['dart_chart_index'][u][p]
    return dict(source=u, target=C[u][p], source_port=p,
                source_port_name=P['ports'][p], target_port=P['inverse_ports'][p],
                chart=chart, chart_name=P['chart_ids'][chart],
                matrix=P['matrices'][chart],
                direction=P['directions'][P['inverse_ports'][p]])

phase = 'extract_actual_shared_target_pairs'
try:
    pairs = []
    for p17, v in enumerate(C[17]):
        for w in ALLOW:
            if w == 17 or v not in C[w]:
                continue
            pw = C[w].index(v)
            a, b = dart(17, p17), dart(w, pw)
            n = norm(cross(a['direction'], b['direction']))
            assert n is not None
            assert dot(n, a['direction']) == dot(n, b['direction']) == 0
            fa, fb = rowmat(n, a['matrix']), rowmat(n, b['matrix'])
            c = next(x for x in fa if x)
            canon_fa, canon_fb = scale(INV[c], fa), scale(INV[c], fb)
            pairs.append(dict(pair_id=len(pairs), source17=17, target=v, other_source=w,
                              dart17=a, dart_other=b, target_cross_normal=n,
                              f17=fa, f_other=fb,
                              normalized_f17=canon_fa,
                              normalized_f_other_same_scale=canon_fb,
                              normalized_f_other_projective=norm(fb),
                              intersection_equation='dot(f17,x17)=dot(f_other,x_other)',
                              image_disjointness_equivalent_to_line_family_disjointness=True))
    assert pairs
    fs = [p['f17'] for p in pairs]
    pull_rank = rank(fs)
    directions = sorted({tuple(norm(f)) for f in fs})
    witness = []
    for p in pairs:
        if rank([q['f17'] for q in witness] + [p['f17']]) > len(witness):
            witness.append(p)
    (D / 'SHARED_TARGET_TRANSPORT.json').write_text(json.dumps(pairs, indent=2) + '\n')
    with (D / 'SHARED_TARGET_PAIR_COEFFICIENTS.tsv').open('w') as stream:
        wr = csv.writer(stream, delimiter='\t')
        wr.writerow(['pair_id', 'source17', 'target', 'other_source', 'port17', 'port_other',
                     'chart17', 'chart_other', 'direction17', 'direction_other',
                     'target_normal', 'f17', 'f_other', 'normalized_f17', 'normalized_f_other_same_scale'])
        for p in pairs:
            a, b = p['dart17'], p['dart_other']
            wr.writerow([p['pair_id'], 17, p['target'], p['other_source'], a['source_port'], b['source_port'],
                         a['chart'], b['chart'], a['direction'], b['direction'],
                         p['target_cross_normal'], p['f17'], p['f_other'],
                         p['normalized_f17'], p['normalized_f_other_same_scale']])

    phase = 'source17_six_dart_noise_pullbacks'
    trans = []
    for p in range(6):
        a = dart(17, p)
        # Use the accepted literal true-inverse chart, not a projective renormalization.
        mi = P['matrices'][P['inverse_charts'][a['chart']]]
        pull = mv(mi, a['direction'])
        trans.append(dict(**a, inverse_chart=P['inverse_charts'][a['chart']],
                          source_noise_pullback=pull, projective_pullback=norm(pull)))
    (D / 'SOURCE17_SIX_DART_TRANSVERSALS.json').write_text(json.dumps(trans, indent=2) + '\n')

    phase = 'enumerate_91_source17_plane_normals'
    normals = [list(a) for a in itertools.product(range(9), repeat=3)
               if any(a) and next(x for x in a if x) == 1]
    assert len(normals) == 91
    planes = []
    for index, a in enumerate(normals):
        basis = plane_basis(a)
        noise_evals = [dot(a, d['source_noise_pullback']) for d in trans]
        rs = [[dot(f, b) for b in basis] for f in fs]
        unique = sorted({tuple(norm(r)) for r in rs if any(r)})
        planes.append(dict(plane_index=index, normal=a, basis=basis,
                           six_noise_evaluations=noise_evals,
                           source17_all_six_dart_transversal=all(noise_evals),
                           zero_restrictions=sum(not any(r) for r in rs),
                           restricted_functionals=rs,
                           restricted_projective_directions=[list(r) for r in unique],
                           restricted_direction_count=len(unique), restricted_span_rank=rank(rs)))
    (D / 'ALL_91_SOURCE17_PLANES.json').write_text(json.dumps(planes, indent=2) + '\n')
    with (D / 'ALL_91_SOURCE17_PLANES.tsv').open('w') as stream:
        wr = csv.writer(stream, delimiter='\t')
        wr.writerow(['plane_index', 'normal', 'basis', 'six_noise_evaluations', 'all_six_transversal',
                     'zero_restrictions', 'projective_direction_count', 'restricted_span_rank',
                     'restricted_projective_directions', 'restricted_functionals_by_pair_id'])
        for p in planes:
            wr.writerow([p['plane_index'], p['normal'], p['basis'], p['six_noise_evaluations'],
                         p['source17_all_six_dart_transversal'], p['zero_restrictions'],
                         p['restricted_direction_count'], p['restricted_span_rank'],
                         p['restricted_projective_directions'], p['restricted_functionals']])
    eligible = [p for p in planes if p['source17_all_six_dart_transversal']]
    assert eligible
    minimum = min(p['restricted_direction_count'] for p in eligible)
    bests = [p for p in eligible if p['restricted_direction_count'] == minimum]
    best = bests[0]
    original_normal = norm([NEG[4], 0, 1])
    original = next(p for p in planes if p['normal'] == original_normal)
    # Explicit typed basis (a,b,4a) facilitates comparison independent of canonical basis.
    original_typed_basis = [[1, 0, 4], [0, 1, 0]]
    original_typed_restrictions = [[dot(f, b) for b in original_typed_basis] for f in fs]
    result = dict(status='PASS_PREDICTION_SUPPORTED' if pull_rank == 3 and minimum > 1 else 'PREDICTION_REFUTED',
                  scope='source17 transport against the fixed retained4 all15 admissible pool only',
                  retained=RET, all_admissible_sources=ALLOW,
                  source17_targets=C[17], shared_pair_count=len(pairs),
                  shared_targets=sorted(set(p['target'] for p in pairs)),
                  shared_other_sources=sorted(set(p['other_source'] for p in pairs)),
                  ambient_pullback_rank=pull_rank,
                  ambient_distinct_projective_functionals=[list(f) for f in directions],
                  rank_witness_pair_ids=[p['pair_id'] for p in witness],
                  rank_witness_f17=[p['f17'] for p in witness],
                  enumerated_plane_normals=len(planes), all_six_transversal_planes=len(eligible),
                  eligible_direction_count_histogram=dict(sorted(Counter(p['restricted_direction_count'] for p in eligible).items())),
                  all_plane_restricted_span_rank_histogram=dict(sorted(Counter(p['restricted_span_rank'] for p in planes).items())),
                  minimum_eligible_direction_count=minimum, best_plane_count=len(bests),
                  best_plane_normals=[p['normal'] for p in bests], best_plane=best,
                  original_W_equation='x2=4*x0 over F9 codes a+3b', original_W=original,
                  original_typed_basis=original_typed_basis,
                  original_typed_restrictions_by_pair_id=original_typed_restrictions,
                  common_single_slab_direction_possible=any(p['restricted_direction_count'] <= 1 for p in eligible),
                  original_W_is_optimal_within_91_plane_diagnostic=(original['source17_all_six_dart_transversal'] and original['restricted_direction_count'] == minimum),
                  new_graphs=0, old_edgefiles_read=0, source_BFS=0, field_law_retests=0,
                  old_all_rank_retests=0, Lean_runs=0, solver_calls=0,
                  other_source_plane_enumerations=0, packing_searches=0,
                  total_CPU_seconds=time.process_time() - START)
    (D / 'BEST_PLANE.json').write_text(json.dumps(dict(plane=best, source=17, by_pair=[
        dict(pair_id=p['pair_id'], target=p['target'], other_source=p['other_source'],
             restricted_f17_raw=best['restricted_functionals'][p['pair_id']],
             f_other_raw=p['f_other'],
             normalized_restricted_f17=[dot(p['normalized_f17'], b) for b in best['basis']],
             normalized_f_other_same_scale=p['normalized_f_other_same_scale']) for p in pairs]), indent=2) + '\n')
    (D / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    terminal = dict(status=result['status'], total_CPU_seconds=time.process_time()-START,
                    wall_seconds=time.time()-WALL, CPU_budget_seconds=5,
                    single_worker=True, all_processes_terminal=True,
                    no_automatic_continuation=True,
                    measured_scope='Python imports, accepted table input, all shared pairs, rank, 91 planes, aggregation')
    (D / 'TERMINAL.json').write_text(json.dumps(terminal, indent=2) + '\n')
    print(json.dumps(dict(result=result, terminal=terminal), indent=2))
except Exception as exc:
    failure = dict(status='FAILED_OR_UNKNOWN_NO_CONTINUATION', phase=phase, error=str(exc),
                   total_CPU_seconds=time.process_time()-START, all_processes_terminal=True)
    (D / 'RESULT.json').write_text(json.dumps(failure, indent=2) + '\n')
    (D / 'TERMINAL.json').write_text(json.dumps(failure, indent=2) + '\n')
    raise
