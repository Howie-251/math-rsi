#!/usr/bin/env python3
"""Literal q2-square calibration; one prefix root and all 230 final roots."""
from collections import Counter, deque
import csv
import json
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
started = time.process_time()
usage_start = resource.getrusage(resource.RUSAGE_SELF)
base = Path(__file__).resolve().parent

A = [set() for _ in range(15)]
def put(x, y):
    A[x].add(y)
    A[y].add(x)
for i in range(5):
    put(i, i)
    put(i, 5+i)
    put(i, 10+i)
    put(5+i, 5+(i+1)%5)
    put(10+i, 10+(i+2)%5)

matrix = [[int(j in A[i]) for j in range(15)] for i in range(15)]
def matmul(B, C):
    return [[sum(B[i][k]*C[k][j] for k in range(15)) for j in range(15)] for i in range(15)]
cube = matmul(matmul(matrix, matrix), matrix)
cube_errors = [[i,j,cube[i][j],4*matrix[i][j]+1]
               for i in range(15) for j in range(15)
               if cube[i][j] != 4*matrix[i][j]+1]
absolute_pair_errors = [[i,j] for i in range(5) for j in range(i+1,5)
                        if j in A[i] or A[i] & A[j]]
closed_owners = [[i for i in range(5) if v in A[i]] for v in range(15)]

S = [set() for _ in range(225)]
for x in range(15):
    for y in range(15):
        u = 15*x+y
        for xx in A[x]:
            for yy in A[y]:
                v = 15*xx+yy
                if u != v:
                    S[u].add(v)
prefix = [set(row) for row in S] + [set()]
for j in range(5):
    c = j
    prefix[225].add(c)
    prefix[c].add(225)
final = [set(row) for row in S] + [set() for _ in range(5)]
for i in range(5):
    h = 225+i
    for j in range(5):
        c = 15*i+j
        final[h].add(c)
        final[c].add(h)
    for j in range(i+1,5):
        final[h].add(225+j)
        final[225+j].add(h)

def edges(G):
    return [(u,v) for u,row in enumerate(G) for v in sorted(row) if u < v]
def degree_hist(G):
    return dict(sorted(Counter(map(len,G)).items()))
def simple_symmetric(G):
    return all(u not in row and all(u in G[v] for v in row) for u,row in enumerate(G))
def write_edges(name,G):
    body = edges(G)
    with (base/name).open('w') as out:
        out.write(f'{len(G)} {len(body)}\n')
        out.writelines(f'{u} {v}\n' for u,v in body)
    return len(body)
def bfs(G,root,limit=None):
    dist = [-1]*len(G)
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        if limit is not None and dist[u] == limit:
            continue
        for v in G[u]:
            if dist[v] < 0:
                dist[v] = dist[u]+1
                queue.append(v)
    return dist

source_edges = write_edges('source_product_n225.edges',S)
prefix_edges = write_edges('prefix_one_helper_n226.edges',prefix)
final_edges = write_edges('graph_d9_D3_n230.edges',final)
predicted = {
    'helper': [1,9,60,160],
    'old_abs_abs_or_nonabs_nonabs': [1,9,48,172],
    'old_exactly_one_abs': [1,9,46,174],
}
per_root = []
mismatches = []
class_hist = {}
witness = None
for root in range(230):
    dist = bfs(final,root)
    hist = [dist.count(d) for d in range(4)]
    if root >= 225:
        cls = 'helper'
    else:
        x,y = divmod(root,15)
        cls = ('old_abs_abs_or_nonabs_nonabs' if (x<5)==(y<5)
               else 'old_exactly_one_abs')
    actual = {'root': root, 'class': cls, 'hist': hist,
              'unreachable': dist.count(-1), 'eccentricity': max(dist)}
    per_root.append(actual)
    class_hist.setdefault(cls,Counter())[tuple(hist)] += 1
    if hist != predicted[cls] or actual['unreachable'] or actual['eccentricity'] != 3:
        mismatches.append(actual)
    if witness is None and 3 in dist:
        witness = [root,dist.index(3)]

prefix_dist = bfs(prefix,225,3)
prefix_hist = [prefix_dist.count(d) for d in range(4)]
prefix_missed = [v for v,d in enumerate(prefix_dist) if d < 0]
with (base/'FINAL_ROOT_HISTOGRAMS.tsv').open('w',newline='') as out:
    writer = csv.writer(out,delimiter='\t')
    writer.writerow(['root','class','d0','d1','d2','d3','unreachable','eccentricity'])
    for row in per_root:
        writer.writerow([row['root'],row['class'],*row['hist'],row['unreachable'],row['eccentricity']])
with (base/'PREFIX_ROOT_DISTANCES.tsv').open('w',newline='') as out:
    writer = csv.writer(out,delimiter='\t')
    writer.writerow(['vertex','distance_from_225_within_radius3'])
    writer.writerows(enumerate(prefix_dist))
with (base/'HELPER_PIN_RECIPE.tsv').open('w',newline='') as out:
    writer = csv.writer(out,delimiter='\t')
    writer.writerow(['helper','absolute_A_index','absolute_B_index','old_product_label'])
    writer.writerows((225+i,i,j,15*i+j) for i in range(5) for j in range(5))

checks = {
    'factor_row_size3': all(len(row)==3 for row in A),
    'factor_symmetric': all(i in A[j] for i,row in enumerate(A) for j in row),
    'factor_loops_exactly_abs': [i for i,row in enumerate(A) if i in row]==list(range(5)),
    'factor_cube_identity_all225_pairs': not cube_errors,
    'factor_distinct_abs_no_edge_or_common_neighbor': not absolute_pair_errors,
    'factor_closed_absolute_neighborhoods_partition15': all(len(owners)==1 for owners in closed_owners),
    'source_simple_symmetric': simple_symmetric(S),
    'source_predicted_edge_count1000': source_edges==1000,
    'source_predicted_degree_hist': degree_hist(S)=={8:25,9:200},
    'source_all25_centers_degree8': all(len(S[15*i+j])==8 for i in range(5) for j in range(5)),
    'source_center_openN_partition_other200': all(sum(v in S[15*i+j] for i in range(5) for j in range(5))
         == (0 if v//15<5 and v%15<5 else 1) for v in range(225)),
    'prefix_predicted_radius3_hist': prefix_hist==[1,5,40,60],
    'prefix_predicted_miss120': len(prefix_missed)==120,
    'final_simple_symmetric': simple_symmetric(final),
    'final_n230_m1035': len(final)==230 and final_edges==1035,
    'final_regular9': degree_hist(final)=={9:230},
    'all230_final_BFS_predictions_match': not mismatches,
}
parameters = {
    'literal_factor_labels': {'absolute':'i (0<=i<5)', 'outer':'5+i', 'inner':'10+i'},
    'literal_factor_edges': ['absolute self-loops','a_i-u_i','a_i-v_i','u_i-u_(i+1 mod5)','v_i-v_(i+2 mod5)'],
    'factor_rows': [sorted(row) for row in A],
    'product_label': '15*x+y',
    'product_adjacency': 'u!=v and A[x][xx] and A[y][yy]',
    'helper_label': '225+i', 'helper_pins': '(a_i,a_j), j=0..4',
    'helper_internal_graph': 'K5',
    'predicted_final_histograms': predicted,
    'prediction_file': 'PREDICTION_AND_SCOPE.md',
    'geometry_isomorphism_claimed': False,
}
(base/'PARAMETERS.json').write_text(json.dumps(parameters,indent=2)+'\n')
usage = resource.getrusage(resource.RUSAGE_SELF)
cpu = (usage.ru_utime+usage.ru_stime)-(usage_start.ru_utime+usage_start.ru_stime)
result = {
    'status': 'ALL_PREDECLARED_CALIBRATION_PREDICTIONS_PASS' if all(checks.values()) else 'PREDICTION_MISMATCH_STOP',
    'checks': checks,
    'factor_cube_mismatches': cube_errors, 'factor_absolute_pair_errors': absolute_pair_errors,
    'source': {'n':225,'m':source_edges,'degree_histogram':degree_hist(S),'BFS_roots':0},
    'prefix': {'n':226,'m':prefix_edges,'degree_histogram':degree_hist(prefix),
        'BFS_root':225,'BFS_limit':3,'histogram_d0_to_d3':prefix_hist,
        'within_radius3':sum(prefix_hist),'missed_within_radius3':len(prefix_missed),
        'missing_within_radius3_is_not_disconnectedness_claim':True},
    'final': {'n':230,'m':final_edges,'degree_histogram':degree_hist(final),
        'BFS_roots':230,'all_roots_eccentricity3':not mismatches,
        'histogram_classes':{cls:[{'histogram':list(h),'root_count':n} for h,n in rows.items()] for cls,rows in class_hist.items()},
        'prediction_mismatches':mismatches,'actual_distance3_witness':witness},
    'CPU_seconds_rusage':cpu, 'CPU_seconds_process_time':time.process_time()-started,
    'CPU_limit_seconds':5,
    'operations': {'literal_factor_cube_check':1,'source_BFS':0,'prefix_root_BFS':1,
        'final_root_BFS':230,'field_or_geometry':0,'old_graph_parsing':0,
        'Lean':0,'solver':0,'web':0,'paid_review':0,'hash':0},
    'portfolio_graph_increment':0,'new_parameter_increment':0,'Lean_increment':0,
    'existing_three_graph_C_scope':False,
}
(base/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
terminal = {
    'state':result['status'],'active_processes':False,'new_parameter_queue_started':False,
    'CPU_seconds_rusage':cpu,'CPU_limit_seconds':5,
    'final_BFS_roots':230,'prefix_BFS_roots':1,
    'root_state_Wiki_frozen_packages_modified':False,
    'portfolio_increment':0,'new_parameter_increment':0,'Lean_increment':0,
    'cap31_enumeration_or_source_build_started':False,
}
(base/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps({'status':result['status'],'failed_checks':[k for k,v in checks.items() if not v],
    'final':result['final'],'prefix':result['prefix'],'CPU_seconds_rusage':cpu}))
