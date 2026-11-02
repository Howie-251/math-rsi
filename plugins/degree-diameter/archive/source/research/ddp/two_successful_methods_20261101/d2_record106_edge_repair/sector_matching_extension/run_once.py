#!/usr/bin/env python3
import time
START = time.process_time()
import collections
import itertools
import json
import math
import os
import resource
from datetime import datetime, timezone
from pathlib import Path

D = Path(__file__).resolve().parent
C = D.parent
resource.setrlimit(resource.RLIMIT_CPU, (4, 4))
PRIOR = json.loads((C / 'core_route_discriminator/TERMINAL.json').read_text())['case_CPU_seconds']
FIXED = [7, 17, 23, 34, 46, 54, 59, 105]
PHASES = []


def dump(name, data):
    (D / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def mark(stage, **extra):
    PHASES.append(dict(stage=stage, batch_CPU_seconds=time.process_time() - START, **extra))
    dump('HANDLE.json', dict(pid=os.getpid(), actual_process_started=True,
        stage=stage, single_worker=True, batch_CPU_budget_seconds=4,
        prior_case_CPU_seconds=PRIOR, case_CPU_budget_seconds=20,
        updated_UTC=datetime.now(timezone.utc).isoformat()))
    dump('BUDGET_LEDGER.json', dict(prior_case_CPU_seconds=PRIOR,
        batch_CPU_budget_seconds=4, case_CPU_budget_seconds=20, stages=PHASES))


class PremiseFailure(Exception):
    def __init__(self, reason, witness):
        self.reason = reason
        self.witness = witness


def cycles(p):
    unseen = set(range(106))
    out = []
    while unseen:
        start = min(unseen)
        v = start
        row = []
        while v not in row:
            row.append(v)
            unseen.discard(v)
            v = p[v]
        assert v == start
        out.append(row)
    return out


def finish(result, note):
    (D / 'NOTE.md').write_text(note + '\n')
    result.update(prior_case_CPU_seconds=PRIOR,
        batch_CPU_seconds=time.process_time() - START,
        case_CPU_seconds=PRIOR + time.process_time() - START,
        batch_CPU_budget_seconds=4, case_CPU_budget_seconds=20,
        single_worker=True, pid=os.getpid(), graph_distance_BFS=0,
        source_D2_or_common_neighbor_revalidation=0, color_refinement_runs=0,
        generalized_graph_isomorphism_search=False, solver_Lean_field_rank_web=0,
        graph_or_parameter_or_Lean_count_increment=0,
        symmetric_rewiring_enumeration=0, rootdocs_Wiki_oldfiles_modified=False)
    dump('RESULT.json', result)
    mark('TERMINAL', outcome=result['status'])
    terminal = dict(status=result['status'], running=False,
        all_processes_terminal=True, prior_case_CPU_seconds=PRIOR,
        batch_CPU_seconds=time.process_time() - START,
        case_CPU_seconds=PRIOR + time.process_time() - START,
        batch_CPU_budget_seconds=4, case_CPU_budget_seconds=20,
        no_automatic_continuation=True)
    dump('TERMINAL.json', terminal)
    print(json.dumps(dict(status=result['status'],
        tested_sector_count=result.get('tested_sector_count', 0),
        matching_extensions_attempted=result.get('matching_extensions_attempted', 0),
        order=result.get('selected_generator_order'),
        orbit_length_histogram=result.get('orbit_length_histogram'),
        batch_CPU_seconds=terminal['batch_CPU_seconds'],
        case_CPU_seconds=terminal['case_CPU_seconds'])), flush=True)


def main():
    mark('READ_SAVED_CLASSES_AND_LITERAL_SOURCE')
    old = json.loads((C / 'structure_probe/RESULT.json').read_text())
    colors = sorted([sorted(row) for row in old['color_classes'] if len(row) == 7],
                    key=lambda row: row[0])
    core = set(next(row for row in old['color_classes'] if len(row) == 49))
    small = set().union(*map(set, colors))
    color = {v: i for i, row in enumerate(colors) for v in row}
    inherited = json.loads((C / 'core_route_discriminator/SIGNATURE_CLASSES.json').read_text())['classes']
    groups = [row['vertices'] for row in inherited]
    signatures = [tuple(row['small_neighbors']) for row in inherited]
    signature_index = {sig: i for i, sig in enumerate(signatures)}
    group_of = {v: i for i, row in enumerate(groups) for v in row}
    A = [set() for _ in range(106)]
    with (C / 'source106.author.adjlist.txt').open() as source:
        for line in source:
            row = list(map(int, line.split()))
            A[row[0]] = set(row[1:])
    edges = [(u, v) for u in range(106) for v in sorted(A[u]) if u < v]

    # Inherit the old one-to-one small-sector construction without refining colors.
    sectors = []
    assigned = {}
    for seed in colors[0]:
        todo = [seed]
        bycolor = {color[seed]: seed}
        for u in todo:
            for v in sorted(A[u] & small):
                ci = color[v]
                if ci in bycolor and bycolor[ci] != v:
                    raise PremiseFailure('small_sector_color_conflict', dict(seed=seed, u=u, v=v))
                if ci not in bycolor:
                    bycolor[ci] = v
                    todo.append(v)
        if len(bycolor) != 7:
            raise PremiseFailure('inherited_sector_not_seven_colors', dict(seed=seed, bycolor=bycolor))
        row = [bycolor[i] for i in range(7)]
        if any(v in assigned for v in row):
            raise PremiseFailure('small_sectors_overlap', dict(seed=seed, row=row))
        for v in row:
            assigned[v] = len(sectors)
        sectors.append(row)
    if set(assigned) != small:
        raise PremiseFailure('small_sector_union_changed', {})

    double = [i for i, row in enumerate(groups) if len(row) == 2]
    singleton = [i for i, row in enumerate(groups) if len(row) == 1]
    if len(double) != 7 or len(singleton) != 35:
        raise PremiseFailure('inherited_signature_size_profile_changed', dict(double=double, singleton=singleton))
    quotient = {i: set() for i in double}
    matching = {}
    for i in double:
        for u in groups[i]:
            for v in A[u] & core:
                j = group_of[v]
                if j not in quotient or j == i:
                    raise PremiseFailure('double_vertex_core_neighbor_outside_other_double_groups',
                                         dict(u=u, v=v, group_i=i, group_j=j))
                quotient[i].add(j)
        for j in quotient[i]:
            m = {}
            for u in groups[i]:
                targets = sorted(A[u] & set(groups[j]))
                if len(targets) != 1:
                    raise PremiseFailure('double_edge_block_not_matching', dict(i=i, j=j, u=u, targets=targets))
                m[u] = targets[0]
            if len(set(m.values())) != 2:
                raise PremiseFailure('double_edge_block_not_bijective', dict(i=i, j=j, matching=m))
            matching[i, j] = m
    reached = {double[0]}
    todo = [double[0]]
    for i in todo:
        for j in quotient[i]:
            if j not in reached:
                reached.add(j)
                todo.append(j)
    if reached != set(double) or any(len(quotient[i]) != 4 for i in double):
        raise PremiseFailure('double_quotient_not_connected_four_regular',
                             dict(reached=sorted(reached), quotient={i: sorted(js) for i, js in quotient.items()}))
    for (i, j), m in matching.items():
        if any(matching[j, i][v] != u for u, v in m.items()):
            raise PremiseFailure('matching_inverse_inconsistent', dict(i=i, j=j))

    def extend(p, gmap, flip):
        """One first-group flip, then matching constraints only, no 2^7 enumeration."""
        source_root = groups[double[0]][0]
        target_root = groups[gmap[double[0]]][flip]
        image = {source_root: target_root}
        other_source = groups[double[0]][1]
        image[other_source] = next(v for v in groups[gmap[double[0]]] if v != target_root)
        queue = [source_root, other_source]
        for u in queue:
            i = group_of[u]
            for j in sorted(quotient[i]):
                if gmap[j] not in quotient[gmap[i]]:
                    return None, 'quotient_edge_not_preserved'
                v = matching[i, j][u]
                forced = matching[gmap[i], gmap[j]][image[u]]
                if v in image:
                    if image[v] != forced:
                        return None, 'cycle_matching_disagreement'
                else:
                    image[v] = forced
                    queue.append(v)
        if len(image) != 14 or len(set(image.values())) != 14:
            return None, 'matching_propagation_not_bijection'
        q = p.copy()
        for u, v in image.items():
            q[u] = v
        return q, None

    identity_map = {i: i for i in range(len(groups))}
    consistency = []
    for flip in range(2):
        p, reason = extend(list(range(106)), identity_map, flip)
        consistency.append(dict(first_flip=flip, consistent=p is not None, reason=reason))
    if not all(row['consistent'] for row in consistency):
        raise PremiseFailure('identity_double_matching_propagation_inconsistent', dict(checks=consistency))
    dump('MATCHING_PREMISE.json', dict(
        double_group_indices=double, double_groups=[groups[i] for i in double],
        quotient={i: sorted(js) for i, js in quotient.items()},
        connected_components=1, degree_histogram={4: 7},
        identity_matching_propagations=consistency,
        directed_matching_maps=[dict(source_group=i, target_group=j,
            pairs=sorted(m.items())) for (i, j), m in sorted(matching.items())],
        fixed_labels=FIXED, sectors_by_color=sectors))
    mark('ENUMERATE_SECTOR_PERMUTATIONS_AND_MATCHING_EXTENSIONS')
    tested = 0
    extensions = 0
    full_bijections = 0
    edge_memberships = 0
    rejected = collections.Counter()
    accepted = []
    generator = None
    complete = True
    for perm7 in itertools.permutations(range(7)):
        if time.process_time() - START > 3.30:
            complete = False
            break
        tested += 1
        p = list(range(106))
        for i, row in enumerate(sectors):
            for ci, u in enumerate(row):
                p[u] = sectors[perm7[i]][ci]
        gmap = {}
        bad = False
        for i, sig in enumerate(signatures):
            j = signature_index.get(tuple(sorted(p[v] for v in sig)))
            if j is None or len(groups[j]) != len(groups[i]):
                rejected['transformed_signature_missing_or_wrong_size'] += 1
                bad = True
                break
            gmap[i] = j
            if len(groups[i]) == 1:
                p[groups[i][0]] = groups[j][0]
        if bad:
            continue
        for flip in range(2):
            extensions += 1
            q, reason = extend(p, gmap, flip)
            if q is None:
                rejected[reason] += 1
                continue
            if len(set(q)) != 106:
                raise PremiseFailure('forced_complete_map_not_bijective', dict(perm7=perm7, flip=flip))
            full_bijections += 1
            preserved = True
            for u, v in edges:
                edge_memberships += 1
                if q[v] not in A[q[u]]:
                    rejected['literal_edge_not_preserved'] += 1
                    preserved = False
                    break
            if not preserved:
                continue
            orbits = cycles(q)
            order = math.lcm(*(len(row) for row in orbits))
            rec = dict(sector_permutation=list(perm7), first_double_group_flip=flip,
                permutation=q, order=order, actual_source_edges_checked=len(edges),
                orbits=orbits)
            accepted.append(rec)
            if order == 7:
                generator = rec
                complete = False  # Deliberate first-witness stop, not full group enumeration.
                break
        if generator is not None:
            break
    dump('ACTUAL_ACCEPTED_AUTOMORPHISMS.json', dict(
        complete_sector_enumeration=complete, first_order7_stop=generator is not None,
        tested_sector_count=tested, accepted=accepted))
    result = dict(status=('ORDER7_AUTOMORPHISM_FOUND' if generator else
        'LIMITED_SECTOR_ACTION_EXHAUSTED_NO_ORDER7' if complete else
        'UNKNOWN_SECTOR_CPU_STOP'), matching_premise_supported=True,
        double_group_connected_components=1, double_quotient_four_regular=True,
        identity_matching_propagations_consistent=True, tested_sector_count=tested,
        matching_extensions_attempted=extensions, propagated_complete_bijections=full_bijections,
        actual_edge_membership_checks=edge_memberships,
        full_edges_per_accepted_permutation=len(edges), accepted_permutation_count=len(accepted),
        complete_sector_enumeration=complete, first_order7_stop=generator is not None,
        rejected_reason_counts=dict(rejected),
        accepted_order_histogram=dict(sorted(collections.Counter(row['order'] for row in accepted).items())),
        selected_generator_order=7 if generator else None)
    if generator is None:
        note = '''# Matching-extension batch stopped

The seven double groups form one connected four-regular matching quotient, so
each proposed sector action has at most two propagated extensions. Actual
tested counts and edge-verified maps are in RESULT.json and
ACTUAL_ACCEPTED_AUTOMORPHISMS.json. No order-seven map was returned by this
limited action/budget. This is not a full-graph no-C7 claim. No symmetric pin
selection or rewiring follows, and no automatic continuation is authorized.
'''
    else:
        dump('ORDER7_GENERATOR_AND_ORBITS.json', generator)
        hist = dict(sorted(collections.Counter(map(len, generator['orbits'])).items()))
        fixed_actual = [row[0] for row in generator['orbits'] if len(row) == 1]
        shape = hist == {1: 8, 7: 14} and fixed_actual == FIXED
        result.update(orbit_length_histogram=hist, actual_fixed_vertices=fixed_actual,
            invariant_pin_shape_7_plus_3_or_4_supported=shape,
            symmetric_internal_S10_Moore_bound=104 if shape else None,
            symmetric_internal_S10_impossible=shape,
            symmetric_internal_S11_not_excluded_by_this_bound=True)
        note = '''# An actual order-seven source automorphism

The inherited seven double signature groups form one connected four-regular
quotient. Each directed quotient edge is an actual two-vertex matching, its
reverse is its inverse, and the two identity-image propagations are consistent.
The small sectors determine all signature-group images. The thirty-five
singleton groups are forced; the double groups require only one initial flip,
after which matching propagation either forces all fourteen images or rejects
a cycle disagreement. No 2^7 enumeration or generic isomorphism procedure was
used.

The first order-seven permutation in ORDER7_GENERATOR_AND_ORBITS.json is a
106-vertex bijection checked against all 582 actual source edges. Its edge
images have the same finite cardinality as the original edge set, so this gives
adjacency equivalence and a genuine automorphism, not a sampled homomorphism.
The exact tested prefix, attempted extensions, accepted maps and CPU are saved
separately; the search stops at this first order-seven witness and does not
claim the full automorphism group. Earlier failed unique-signature and partial
propagation predictions remain unchanged historical results.

## Paper consequence for the current internal-pin rewiring rule

When the recorded cycle shape is fourteen seven-cycles and the eight fixed
labels {7,17,23,34,46,54,59,105}, an invariant S of size10 or11 must be one
seven-orbit and respectively three or four fixed vertices. This restricts only
solutions required to preserve this particular C7; arbitrary solutions need
not have invariant S.

For a graph of order107, maximum degree11 and diameter2, every vertex has
degree at least10: a root of degree d reaches at most1+11d vertices in two
steps. Suppose only old G[S] is changed, new z is adjacent to S, and the C7 is
preserved while fixing z. A selected fixed vertex is adjacent either to all
seven orbit vertices or to none. Changing that bundle adds or deletes seven
neighbors, while changing its other selected-fixed incidences changes at most
r-1<=3 neighbors, and z adds one. Starting from degree10 or11, adding the bundle
forces degree at least10+1-3+7=15>11; deleting forces degree at most
11+1+3-7=8<10. Thus every fixed/orbit bundle is unchanged.

Each of the seven selected orbit vertices originally has degree11. An
undirected C7-invariant graph on one seven-orbit has even degree (a union of
cyclic-difference rings). All its other old incidences are unchanged, and z
adds one, so its final degree is even; the allowed interval[10,11] forces
degree10. Equivalently its old orbit-internal degree decreases by two. This
also excludes selecting an originally independent orbit under this symmetric
rule.

For |S|=10, z has seven neighbors of final degree10 and at most three of degree11.
Therefore its two-ball has at most
1+10+7*(10-1)+3*(11-1)=104<107 vertices. This proves that the C7-preserving
internal-S size10 rule cannot yield the desired107 graph. For |S|=11, the same
bound is115 and does not exclude a candidate; old selected/outside route
obligations still matter. No S11 or other symmetric rewiring was enumerated,
and no new graph, solver, source-D2 validation, or distance BFS was run.
'''
        if not shape:
            note += '\nWARNING: actual cycles do not have the hypothesized shape; the stated pin-shape consequences are conditional only and not marked supported in RESULT.\n'
    finish(result, note)


try:
    main()
except PremiseFailure as error:
    finish(dict(status='MATCHING_EXTENSION_PREMISE_REFUTED', reason=error.reason,
        counterexample=error.witness, selected_generator_order=None),
        '# Matching-extension premise failed\nThe counterexample is saved in RESULT.json. No exponential extension fallback, generic isomorphism, or symmetric rewiring search follows.')
except Exception as error:
    finish(dict(status='UNKNOWN_IMPLEMENTATION_ERROR_NO_RETRY', exception=repr(error),
        selected_generator_order=None),
        '# One bounded implementation attempt stopped\nThe actual exception and spent CPU are saved. No retry or mathematical negative conclusion is claimed.')
