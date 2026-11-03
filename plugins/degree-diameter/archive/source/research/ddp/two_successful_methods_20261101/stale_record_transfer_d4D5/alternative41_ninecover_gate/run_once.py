#!/usr/bin/env python3
import time
START = time.process_time()
import collections
import json
import os
import resource
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = next(p for p in HERE.parents if (p / 'research').is_dir())
PREP = 0.1
PRIOR_CHARGED = 0.14797470699999998
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
OFFICIAL = 'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html#43'
PREFIX = 'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/'


def save(name, x):
    (HERE / name).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')


def used():
    return time.process_time() - START


def finish(status, rows):
    result = dict(status=status,
        prediction=('SUPPORTED_AT_LEAST_ONE_CAPACITY_PASS' if any(r.get('capacity_pass') for r in rows)
                    else 'REFUTED_ALL_THREE_NEW_SOURCES_HAVE_ROUTE_DEFICIT' if len(rows) == 3 and all(r.get('capacity_pass') is False for r in rows)
                    else 'UNRESOLVED_INPUT_OR_CPU_SCOPE'),
        source_count_planned=3, source_count_returned=len(rows),
        sources_actually_counted=sum('minimum_count' in r for r in rows), sources=rows,
        ordinary_cover_sheets=9, target_order=369, target_degree=4, target_D=5,
        official_new_source_description=OFFICIAL,
        old_Allwright1a_capacity_and_triangle_gate_reused_not_rerun=True,
        source_BFS_or_source_allroot_validity_runs=0, nonbacktracking_max_length=5,
        graph369_generation=0, solver_Lean_field_rank_or_paid_review=0,
        graph_parameter_or_Lean_count_increment=0,
        actual_process_CPU_seconds=used(), conservative_preparation_charge_seconds=PREP,
        charged_case_CPU_seconds=PRIOR_CHARGED + used() + PREP, CPU_budget_seconds=10,
        previous_parser_failure_charged_CPU_seconds=PRIOR_CHARGED,
        previous_parser_failure_receipt='INITIAL_PARSE_FAILURE_TERMINAL.json',
        next=('REPORT_GATE_PASS_FOR_ROOT_VOLTAGE_DECISION' if any(r.get('capacity_pass') for r in rows)
              else 'STOP_TESTED_SOURCES_NO_TIMER_OR_SOURCE_EXPANSION'),
        rootdocs_Wiki_oldfiles_modified=False)
    save('RESULT.json', result)
    table = ['| Source | Input | minimum NB walks of length0..5 | tight ordered pair | disposition |',
             '| --- | --- | ---: | --- | --- |']
    for r in rows:
        table.append(f"| {r['source_id']} | {r['status']} | {r.get('minimum_count', 'not measured')} | {r.get('tight_pair', '')} | {'necessary gate passes only' if r.get('capacity_pass') else 'arbitrary nine-sheet cover excluded' if r.get('capacity_pass') is False else 'UNKNOWN input'} |")
    note = '''# Alternative41 sources: actual nine-cover capacity readout

The source change and falsifiable prediction were saved before this one
process. Only N1,N2,N3 from the official2026 additional-source description
were eligible. The older Allwright Graph1(a) C9 and affine-transfer exclusions
remain separate historical scopes and were not recalculated.

''' + '\n'.join(table) + '''

For an ordinary graph cover, a source walk has a unique lift from a fixed
lifted starting vertex. A shortest lifted route cannot project an immediate
edge reversal: local bijectivity would force the actual lifted edge to be
immediately reversed too. Hence every lifted endpoint within five steps
comes from a nonbacktracking source walk of length0..5. If one ordered base
pair has fewer than nine such walks, at most that many of the nine target
fiber vertices are reachable within five steps. This excludes any ordinary
nine-sheet cover, including arbitrary permutation voltages; it is stronger
than a cyclic-C9 voltage obstruction. The zero-length walk is included for
a diagonal ordered pair.

A passed count gate would only show that this simple capacity obstruction
is absent; endpoints from different walks can still coincide and all voltage
constraints may be incompatible. It would not produce a369-point graph or
prove diameter5. A failed input fetch or parse remains UNKNOWN, not a route
capacity failure. No unknown input is replaced by another Allwright variant.

The input is parsed as a NetworkX undirected adjacency representation,
symmetrizing its listed edges. Only input identity/cardinality and degree
contract binding needed for the route calculation are recorded; source
diameter and nonisomorphism are inherited from the primary description, not
rechecked. No source-distance BFS or all-root source-validity test was run.
Every counted source has its full41-by41 nonbacktracking count matrix and
the complete short-walk list for its tight witness pair, saved in the
source-specific ROUTE_CAPACITY.json. No cover graph, solver, Lean module,
field check, external review or portfolio update is generated here.
'''
    (HERE / 'NOTE.md').write_text(note + '\n')
    terminal = dict(status=status, running=False, all_processes_terminal=True,
        actual_process_CPU_seconds=used(), conservative_preparation_charge_seconds=PREP,
        charged_case_CPU_seconds=PRIOR_CHARGED + used() + PREP, CPU_budget_seconds=10,
        previous_parser_failure_charged_CPU_seconds=PRIOR_CHARGED,
        no_automatic_continuation=True)
    save('TERMINAL.json', terminal)
    save('HANDLE.json', dict(actual_PID=os.getpid(), stage='TERMINAL', **terminal))
    print(json.dumps(dict(status=status, prediction=result['prediction'],
        sources=[{k:r.get(k) for k in ['source_id','status','minimum_count','tight_pair']} for r in rows],
        charged_case_CPU_seconds=terminal['charged_case_CPU_seconds'])), flush=True)


rows = []
try:
    save('HANDLE.json', dict(actual_PID=os.getpid(), stage='ONE_NEW_THREE_SOURCE_BATCH',
        CPU_budget_seconds=10, single_worker=True))
    oldfile = PROJECT / 'research/ddp/breadth_20261027_wave6/cyclic_cover369/base41.edges'
    lines = [list(map(int, line.split())) for line in oldfile.read_text().splitlines() if line.strip()]
    if len(lines[0]) == 2 and lines[0] == [41, 82]:
        lines = lines[1:]
    oldedges = {tuple(sorted(pair)) for pair in lines}
    previous_inputs = []
    for name in ['N1', 'N2', 'N3']:
        if PRIOR_CHARGED + used() + PREP > 9.5:
            rows.append(dict(source_id=name, status='UNKNOWN_CPU_STOP_BEFORE_SOURCE'))
            continue
        url = PREFIX + f'41_Messieres_{name}.adjlist'
        row = dict(source_id=name, official_href=PREFIX + f'41_Messieres_{name}.adjlistt',
            official_href_observed_result='404', actual_fetch_URL=url,
            filename_correction='One obvious suffix correction:adjlistt to adjlist',
            source_author='Michel de Messieres', source_date='October2026',
            source_nonisomorphism_and_D3='INHERITED_PRIMARY_CLAIM_NOT_RETESTED')
        try:
            rawfile = HERE / f'source_{name}.author.adjlist'
            if rawfile.exists():
                raw = rawfile.read_bytes()
                row.update(HTTP=200, raw_bytes=len(raw), reused_actual_download=True)
            else:
                response = urllib.request.urlopen(url, timeout=12)
                raw = response.read()
                rawfile.write_bytes(raw)
                row.update(HTTP=response.status, raw_bytes=len(raw), reused_actual_download=False)
        except Exception as error:
            row.update(status='UNKNOWN_PRIMARY_INPUT_UNAVAILABLE', error=repr(error))
            rows.append(row)
            continue
        edges = set()
        labels = set()
        observed_metadata_headers = []
        for line in raw.decode('utf-8', errors='strict').splitlines():
            line = line.split('#', 1)[0].strip()
            if not line:
                continue
            if line.startswith(f'(4,3)=41 {name};'):
                observed_metadata_headers.append(line)
                continue
            ns = list(map(int, line.split()))
            labels.add(ns[0])
            for v in ns[1:]:
                labels.add(v)
                edges.add(tuple(sorted((ns[0], v))))
        ordered_labels = sorted(labels)
        relabel = {v:i for i,v in enumerate(ordered_labels)}
        E = {tuple(sorted((relabel[u], relabel[v]))) for u,v in edges}
        adjacency = [set() for _ in ordered_labels]
        for u,v in E:
            adjacency[u].add(v)
            adjacency[v].add(u)
        degree_hist = dict(sorted(collections.Counter(map(len, adjacency)).items()))
        row.update(input_vertices=len(adjacency), input_edges=len(E),
            observed_uncommented_metadata_headers=observed_metadata_headers,
            input_degree_histogram=degree_hist, original_labels_in_normalized_order=ordered_labels,
            literal_edge_set_equals_old_Allwright1a=E == oldedges)
        if E == oldedges:
            row['status'] = 'OLD_EXCLUDED_SOURCE_SKIP_NO_ROUTE_RECOMPUTATION'
            rows.append(row)
            continue
        if any(E == prior for prior in previous_inputs):
            row['status'] = 'UNKNOWN_DUPLICATE_LITERAL_INPUT_NO_RECOMPUTATION'
            rows.append(row)
            continue
        previous_inputs.append(E)
        if len(adjacency) != 41 or len(E) != 82 or degree_hist != {4:41} or any(u==v for u,v in E):
            row['status'] = 'UNKNOWN_INPUT_CONTRACT_MISMATCH_NO_ROUTE_COMPUTATION'
            rows.append(row)
            continue
        A = [sorted(ns) for ns in adjacency]
        save(f'source_{name}.NORMALIZED_ADJ.json', dict(original_labels=ordered_labels, adjacency=A))
        counts = []
        minimum = None
        witness_pair = None
        witness_walks = None
        total_walks = 0
        for source in range(41):
            endpoint_paths = [[] for _ in range(41)]
            def walk(u, prev, path):
                endpoint_paths[u].append(path)
                if len(path) == 6:
                    return
                for v in A[u]:
                    if v != prev:
                        walk(v, u, path + [v])
            walk(source, -1, [source])
            count = [len(ps) for ps in endpoint_paths]
            counts.append(count)
            total_walks += sum(count)
            for target, n in enumerate(count):
                if minimum is None or n < minimum:
                    minimum = n
                    witness_pair = [source, target]
                    witness_walks = endpoint_paths[target]
        passed = minimum >= 9
        row.update(status='CAPACITY_PASS_NO_CONSTRUCTION' if passed else 'EXACT_NO_ANY_NINE_SHEET_ORDINARY_COVER',
            capacity_pass=passed, ordered_pairs_counted=41*41,
            minimum_count=minimum, tight_pair=witness_pair,
            tight_pair_original_labels=[ordered_labels[u] for u in witness_pair],
            tight_pair_walks=witness_walks,
            tight_pair_walk_length_histogram=dict(sorted(collections.Counter(len(p)-1 for p in witness_walks).items())),
            all_count_histogram=dict(sorted(collections.Counter(x for rs in counts for x in rs).items())),
            nonbacktracking_walks_including_length0_total=total_walks)
        save(f'source_{name}.ROUTE_CAPACITY.json', dict(**row, count_matrix=counts,
            scope='Actual new source ordered-pair nonbacktracking route capacity only, lengths0..5'))
        rows.append(row)
        save('LIVE_RESULTS.json', rows)
    final = ('AT_LEAST_ONE_NEW_SOURCE_CAPACITY_PASS' if any(r.get('capacity_pass') for r in rows)
             else 'ALL_THREE_NEW_SOURCES_EXACT_NINECOVER_OBSTRUCTION' if len(rows)==3 and all(r.get('capacity_pass') is False for r in rows)
             else 'UNKNOWN_UNAVAILABLE_OR_UNRESOLVED_NEW_SOURCE_SCOPE')
    finish(final, rows)
except Exception as error:
    rows.append(dict(source_id='BATCH', status='UNKNOWN_IMPLEMENTATION_FAILURE_NO_RETRY', error=repr(error)))
    finish('UNKNOWN_IMPLEMENTATION_FAILURE_NO_RETRY', rows)
