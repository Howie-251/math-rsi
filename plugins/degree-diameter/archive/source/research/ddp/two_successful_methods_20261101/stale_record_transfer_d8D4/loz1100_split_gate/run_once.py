#!/usr/bin/env python3
import time
START = time.process_time()
import collections
import csv
import json
import os
import resource
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREPARATION_CHARGE = 0.1
BUDGET = 10
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))


def cpu():
    return time.process_time() - START


def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def finish(result, note):
    (HERE / 'NOTE.md').write_text(note + '\n')
    result.update(actual_process_CPU_seconds=cpu(),
        conservative_preparation_charge_seconds=PREPARATION_CHARGE,
        charged_case_CPU_seconds=cpu() + PREPARATION_CHARGE,
        CPU_budget_seconds=BUDGET, single_worker=True,
        old_source_validation_or_allroot_BFS=0,
        new_identity_R4_firsthop_support_calculations=1,
        source_split_candidate_graphs_generated=0,
        solver_Lean_field_rank_or_web_runs=0,
        graph_parameter_Lean_count_increment=0,
        rootdocs_Wiki_oldfiles_modified=False)
    save('RESULT.json', result)
    terminal = dict(status=result['status'], running=False,
        all_processes_terminal=True, actual_process_CPU_seconds=cpu(),
        conservative_preparation_charge_seconds=PREPARATION_CHARGE,
        charged_case_CPU_seconds=cpu() + PREPARATION_CHARGE,
        CPU_budget_seconds=BUDGET, no_automatic_continuation=True)
    save('TERMINAL.json', terminal)
    save('HANDLE.json', dict(actual_PID=os.getpid(), stage='TERMINAL', **terminal))
    print(json.dumps(dict(status=result['status'], prediction=result.get('prediction'),
        actual_N1=result.get('actual_N1'), actual_R4=result.get('actual_R4'),
        singleton_targets=result.get('singleton_target_count'),
        charged_case_CPU_seconds=terminal['charged_case_CPU_seconds'])), flush=True)


try:
    save('HANDLE.json', dict(actual_PID=os.getpid(), stage='ACTUAL_NEW_R4_SUPPORT_CALCULATION',
        CPU_budget_seconds=BUDGET, source_validity_inherited=True,
        no_source_allroot_BFS=True, single_worker=True))
    positive = [(1, 0), (12, 33), (11, 1), (16, 19)]
    inverse = [((-j) % 20, (-v * pow(2, (-j) % 20, 55)) % 55)
               for j, v in positive]
    darts = positive + inverse
    factors = [pow(2, j, 55) for j, _ in darts]

    # Recipe is evaluated only as input to this split-route question. No old
    # source degree/symmetry/diameter acceptance loop is run.
    adjacency = []
    for u in range(1100):
        j, x = divmod(u, 55)
        adjacency.append([55 * ((j + k) % 20) + (x * factor + v) % 55
                          for (k, v), factor in zip(darts, factors)])
    neighbors = adjacency[0]
    distance = [-1] * 1100
    support = [0] * 1100
    parent = [-1] * 1100
    distance[0] = 0
    layer = [0]
    for depth in range(1, 5):
        nxt = []
        for u in layer:
            for port, v in enumerate(adjacency[u]):
                bits = (1 << port) if u == 0 else support[u]
                if distance[v] < 0:
                    distance[v] = depth
                    parent[v] = u
                    nxt.append(v)
                if distance[v] == depth:
                    support[v] |= bits
        layer = nxt
    boundary = [u for u in range(1100) if distance[u] == 4]
    mask_hist = collections.Counter(support[u] for u in boundary)
    singletons = [u for u in boundary if support[u].bit_count() == 1]
    with (HERE / 'R4_BOUNDARY_SUPPORTS.csv').open('w') as f:
        writer = csv.writer(f)
        writer.writerow(['old_target', 'distance_from_source_root0', 'firsthop_support_mask',
                         'support_size', 'supported_neighbor_labels'])
        for u in boundary:
            writer.writerow([u, 4, support[u], support[u].bit_count(),
                             ' '.join(str(neighbors[p]) for p in range(8) if support[u] >> p & 1)])
    save('SOURCE_RECIPE_INPUT.json', dict(
        source_order=1100, source_degree=8, source_diameter=4,
        source_validity='INHERITED_ONLY', phase_modulus=20, normal_modulus=55,
        law='RIGHT(j,x)(k,v)=(j+k mod20,x*2^k+v mod55)',
        vertex_label='55*j+x', positive_generators=positive,
        inverse_generators=inverse, darts_in_support_bit_order=darts,
        actual_root0_neighbor_labels=neighbors,
        inherited_recipe='research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/run.py',
        old_exclusion_scope='25 normalized5500-point cyclic25 lifts, not the present split rule'))
    witness = None
    survivors = []
    tested = 0
    if singletons:
        v = singletons[0]
        path = [v]
        while path[-1] != 0:
            path.append(parent[path[-1]])
        path.reverse()
        port = (support[v] & -support[v]).bit_length() - 1
        witness = dict(target=v, singleton_support_mask=support[v],
            mandatory_firsthop_port=port, mandatory_first_neighbor=neighbors[port],
            actual_source_four_step_route=path,
            obstruction='The side without this mandatory neighbor has distance at least5 to the target after the split.')
        status = 'EXACT_NO_SINGLE_SPLIT_DUE_TO_SINGLETON_R4_SUPPORT'
        prediction = 'SUPPORTED_SINGLETON_BOUNDARY_OBSTRUCTION'
        excluded = 127
    else:
        # Label a/b exchange fixes bit0 in A. This is127 representatives,
        # not a source orbit or graph-isomorphism search.
        for amask in range(1, 255, 2):
            tested += 1
            bmask = 255 ^ amask
            if all(mask & amask and mask & bmask for mask in mask_hist):
                survivors.append(dict(A_mask=amask, B_mask=bmask,
                    A_neighbors=[neighbors[p] for p in range(8) if amask >> p & 1],
                    B_neighbors=[neighbors[p] for p in range(8) if bmask >> p & 1]))
        excluded = 127 - len(survivors)
        status = 'BOUNDARY_SPLIT_SURVIVORS_PENDING_OLD_OLD_ANALYSIS' if survivors else 'EXACT_NO_SINGLE_SPLIT_BY_BOUNDARY_TWO_COLORING'
        prediction = 'REFUTED_NO_SINGLETON_TARGET'
    result = dict(status=status, prediction=prediction,
        target_degree=8, target_D=4, target_order=1101,
        actual_N1=neighbors, actual_N1_count=len(neighbors),
        actual_R4=len(boundary), boundary_targets=boundary,
        source_root0_route_layer_histogram=dict(sorted(collections.Counter(distance).items())),
        firsthop_support_mask_histogram=dict(sorted(mask_hist.items())),
        firsthop_support_size_histogram=dict(sorted(collections.Counter(support[u].bit_count() for u in boundary).items())),
        singleton_target_count=len(singletons), singleton_target_labels=singletons,
        singleton_witness=witness,
        nontrivial_oriented_partitions_total=254,
        complement_partition_classes_total=127,
        partition_classes_actually_tested=tested,
        partition_classes_excluded=excluded,
        oriented_partitions_excluded=2 * excluded,
        surviving_partition_class_count=len(survivors), surviving_partitions=survivors,
        near_targets_distance_at_most3='BOTH_SPLIT_ROLES_HAVE_DISTANCE_AT_MOST4_BY_ONE_INSERTED_ROLE_EDGE',
        scope='One source vertex is replaced by two adjacent vertices whose nonempty neighbor sets partition the original8neighbors; no other edges changed. Cayley left translation reduces any source vertex to0.',
        next='STOP_THIS_SPLIT_RULE' if not survivors else 'REPORT_SURVIVORS_TO_ROOT_NO_AUTOMATIC_GRAPH_OR_ALLROOT_BFS')
    if not survivors:
        note = '''# The inherited1100 source cannot gain one point by this single split

The actual prediction result, all distance-four first-hop support masks and
the terminal CPU are saved separately. If RESULT gives a singleton witness,
every partition is rejected logically without enumerating partitions: that
single mandatory first neighbor belongs to only one side. If it instead
reports a two-coloring rejection, the127 complement representatives were
actually checked. This is a split-route calculation, not a rerun of source
graph validity or an all-root source BFS.

Take an old target x at source distance4 from root0. Any route of length at
most4 from either split role to x must begin with one of that role's assigned
old neighbors. A route starting across the new role-role edge has at least
one inserted step beyond a four-step source route. Projecting any putative
short route back onto the source gives a length-at-most4 source route; at
distance4 it must be a geodesic with first neighbor in that role's assigned
set. Therefore both parts of the partition must meet every recorded
first-hop support. A singleton, or failure of all127 two-colorings, excludes
the rule. The genuine source four-step path is a witness of the actual
boundary target, not a path in a newly generated graph.

Old targets at source distance at most3 cause no new-root exception: a source
geodesic can be followed from either role with at most one role-role step,
giving length at most4. No old-old pair was tested; if this necessary gate
had survived, old routes crossing the split root could still gain a step.
Here the failed new-root necessary condition already suffices to stop before
generating any1101 edge file or running full-target BFS.

The source is the inherited RIGHT-law C20 semidirect_2 Z55 Cayley recipe.
Left translations preserve its fixed generator graph and carry any chosen
source root to identity0, including its neighbor partitions. Thus the
identity obstruction excludes this same single-split rule at every source
vertex; no general automorphism enumeration is used. The previous failed
5500-point cyclic25 cover is a separate scope, not a premise that this split
must fail.

This does not exclude splitting multiple vertices, adding other edges,
moving other source edges, other sources or any general(8,4) construction.
No new graph, global record or Lean result is counted. The batch stops.
'''
    else:
        note = '''# First-hop boundary survivors, without a full candidate claim

RESULT.json lists the actual127-complement partition test and every survivor.
Both split roles can cover their distance-four boundary by the recorded
first-hop supports; targets of source distance at most3 are automatically
within4 after at most one role-role step. This is not an all-pair theorem:
old-old routes crossing the split root can lengthen, so no1101 graph or full
BFS is automatically generated. Return the survivors to root for the next
authorized question. Source validity is inherited, and old cyclic25-cover
exclusions were not rerun.
'''
    finish(result, note)
except Exception as error:
    finish(dict(status='UNKNOWN_IMPLEMENTATION_FAILURE_NO_RETRY', prediction='NOT_RESOLVED',
        exception=repr(error), scope='Only the one authorized Loz1100 split boundary gate',
        next='REPORT_TO_ROOT_WITHOUT_RETRY'),
        '# The one split-boundary attempt stopped\nThe actual exception and CPU are retained. No retry, source-invalidity conclusion or new graph follows.')
