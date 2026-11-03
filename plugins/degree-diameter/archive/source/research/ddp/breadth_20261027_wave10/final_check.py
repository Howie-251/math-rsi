"""Root independent check from the saved explicit edge list; one BFS per root."""
from pathlib import Path
from collections import deque, Counter
import json
import sys
import time

def check(directory, target, expected_bad):
    p = Path(directory)
    output = p/'best.independent_check.json'
    if output.exists():
        raise RuntimeError('Final check exists; reuse it rather than repeating BFS')
    started = time.process_time()
    lines = (p/'best.edges').read_text().splitlines()
    n, m = map(int, lines[0].split())
    edges = {tuple(sorted(map(int, line.split()))) for line in lines[1:] if line.strip()}
    assert len(edges)==m==len(lines)-1
    adj = [[] for _ in range(n)]
    for u,v in edges:
        assert 0<=u<v<n
        adj[u].append(v)
        adj[v].append(u)
    assert all(len(ns)==8 for ns in adj)
    parameter_check = None
    if (p/'best_parameters.json').exists() and 'binary1152' in p.name:
        parameters = json.loads((p/'best_parameters.json').read_text())
        generated = set()
        def action(cols, x):
            y = 0
            for i, column in enumerate(cols):
                if x & (1<<i):
                    y ^= column
            return y
        for e in parameters['edges']:
            T, Ti = e['T_columns'], e['Tinv_columns']
            assert 0<e['b']<16 and len({action(T,x) for x in range(16)})==16
            assert all(action(Ti,action(T,x))==x for x in range(16))
            assert action(Ti,e['b'])==e['reverse_b'] and action(Ti,e['c'])==e['reverse_c']
            for x in range(16):
                for lam in range(2):
                    y = action(T,x)^e['c']^(lam*e['b'])
                    generated.add(tuple(sorted((16*e['u']+x,16*e['v']+y))))
        assert generated==edges
        parameter_check = dict(all_144_inverse_maps_valid=True, all_parameters_reconstruct_saved_edges=True)
    if (p/'geometry.json').exists():
        geometry = json.loads((p/'geometry.json').read_text())
        points, lines_geo = geometry['points'], geometry['lines']
        assert len(points)==len(lines_geo)==156
        point_ids = {tuple(x):i for i,x in enumerate(points)}
        assert len(point_ids)==156
        for line in lines_geo:
            assert len(set(line))==6
            a,b = points[line[0]],points[line[1]]
            assert (a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2])%5==0
            generated_line = set()
            for i in range(5):
                for j in range(5):
                    if i==j==0:
                        continue
                    vector = [(i*x+j*y)%5 for x,y in zip(a,b)]
                    leading = next(x for x in vector if x)
                    normalized = tuple(x*pow(leading,-1,5)%5 for x in vector)
                    generated_line.add(point_ids[normalized])
            assert generated_line==set(line)
        incidence = {(point,156+line_id) for line_id,line in enumerate(lines_geo) for point in line}
        assert len(incidence)==936
        assert incidence<=edges
        remaining = edges-incidence
        assert len(remaining)==312
        assert all((u<156)==(v<156) for u,v in remaining)
        count = Counter(x for e in remaining for x in e)
        assert all(count[u]==2 for u in range(n))
        parameter_check = dict(all936_incidence_edges_retained=True,
            exactly156_edges_in_each_internal_factor=True, all_vertices_internal_degree2=True)
    if (p/'best_parameters.json').exists():
        params = json.loads((p/'best_parameters.json').read_text())
        if 'global_label_parameters' in params:
            global_params = params['global_label_parameters']
            matrices, b = global_params['matrix_columns'], global_params['b_codes']
            inv, controller = params['inverse_labels'], params['controller_out']
            def apply(cols,x):
                value = 0
                for i in range(4):
                    if x&(1<<i):
                        value ^= cols[i]
                return value
            generated = set()
            for t in range(4):
                assert all(apply(matrices[inv[t]],apply(matrices[t],x))==x for x in range(16))
                assert apply(matrices[inv[t]],b[t])==b[inv[t]]
            for u,neighbors in enumerate(controller):
                for t,v in enumerate(neighbors):
                    assert controller[v][inv[t]]==u
                    for x in range(16):
                        for lam in range(2):
                            y = apply(matrices[t],x)^(lam*b[t])
                            generated.add(tuple(sorted((16*u+x,16*v+y))))
            assert generated==edges
            parameter_check = dict(all_four_global_maps_and_inverse_vectors_valid=True,
                all_controller_labels_inverse_consistent=True, all4608_parameter_edges_exact=True)
    histogram = Counter()
    eccentricity = Counter()
    for root in range(n):
        distance = [-1]*n
        distance[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if distance[v]<0:
                    distance[v] = distance[u]+1
                    queue.append(v)
        assert -1 not in distance
        histogram.update(distance[root+1:])
        eccentricity[max(distance)] += 1
    bad = sum(count for d,count in histogram.items() if d>target)
    assert bad==expected_bad
    result = dict(status='INDEPENDENT_ALL_ROOT_BFS_MATCH', n=n, m=m, max_degree=8,
        simple=True, connected=True, degree_histogram={8:n}, diameter=max(histogram),
        target_D=target, ordinary_bad_unordered_pairs=bad,
        unordered_distance_histogram=dict(sorted(histogram.items())),
        eccentricity_histogram=dict(sorted(eccentricity.items())),
        roots_checked=n, producer_score_match=True, parameter_check=parameter_check,
        source='best.edges only for BFS; parameters checked separately',
        CPU_seconds=time.process_time()-started, new_lower_bound=False)
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':
    check(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
