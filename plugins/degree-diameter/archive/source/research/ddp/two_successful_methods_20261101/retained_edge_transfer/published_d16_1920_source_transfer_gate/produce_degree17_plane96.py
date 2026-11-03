"""Materialize one new clone graph using the inherited literal source recipe."""
import collections
import json
from pathlib import Path
import signal
import time


def main():
    start = time.process_time()
    def timeout(_signum, _frame):
        raise TimeoutError('single producer CPU budget15s exhausted')
    signal.signal(signal.SIGPROF, timeout)
    signal.setitimer(signal.ITIMER_PROF, 15)
    gate = Path(__file__).resolve().parent
    root = next(p for p in gate.parents if (p / 'formal').is_dir())
    output = gate / 'degree17_plane96'
    output.mkdir(exist_ok=True)
    source_path = root / 'research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json'
    source = json.loads(source_path.read_text())
    controller, matrices, directions = (source[k] for k in
        ['controller', 'matrices', 'outgoing_return_directions'])
    inverse_ports = [1, 0, 3, 2]

    def mul(a, b):
        answer = (a if b & 1 else 0) ^ (a << 1 if b & 2 else 0)
        return answer ^ 7 if answer & 4 else answer

    def apply(matrix, x):
        return [mul(row[0], x[0]) ^ mul(row[1], x[1]) ^ mul(row[2], x[2])
                for row in matrix]

    old_edges = set()
    for u in range(30):
        for code in range(64):
            x = [code % 4, code // 4 % 4, code // 16]
            vertex = 64 * u + code
            for p in range(4):
                y = apply(matrices[u][p], x)
                direction = directions[inverse_ports[p]]
                for t in range(4):
                    z = [y[k] ^ mul(t, direction[k]) for k in range(3)]
                    neighbor = 64 * controller[u][p] + z[0] + 4 * z[1] + 16 * z[2]
                    old_edges.add(tuple(sorted((vertex, neighbor))))
    assert len(old_edges) == 15360
    adjacency = [set() for _ in range(1920)]
    for u, v in old_edges:
        assert u < v
        adjacency[u].add(v)
        adjacency[v].add(u)
    assert all(len(row) == 16 for row in adjacency)
    packing = json.loads((gate / 'CONTROLLER_PACKING_RESULT.json').read_text())
    selected_layers = packing['controller_centers']
    assert packing['status'] == 'EXACT_OPTIMUM' and len(selected_layers) == 6
    roles, added_edges, pin_counts = [], set(), collections.Counter()
    for i, layer in enumerate(selected_layers):
        for a in range(4):
            for b in range(4):
                c = 64 * layer + a + 4 * b + 16 * (a ^ b)
                new = 1920 + 16 * i + 4 * a + b
                neighbors = sorted(adjacency[c])
                roles.append({'new': new, 'controller': layer, 'a': a, 'b': b,
                              'old_center': c, 'complete_neighbors': neighbors})
                for pin in neighbors:
                    pin_counts[pin] += 1
                    added_edges.add((pin, new))
    assert len(roles) == 96 and len(pin_counts) == 1536
    assert max(pin_counts.values()) == 1 and len(added_edges) == 1536
    degree_histogram = collections.Counter(16 + pin_counts[v] for v in range(1920))
    degree_histogram[16] += 96
    assert dict(degree_histogram) == {16: 480, 17: 1536}
    for name, n, edges in [('source_d16_D3_n1920.edges',1920,old_edges),
                            ('graph_d17_D3_n2016.edges',2016,old_edges | added_edges)]:
        (output / name).write_text(f'{n} {len(edges)}\n' +
                                  ''.join(f'{u} {v}\n' for u, v in sorted(edges)))
    (output / 'ALL_96_NEW_ROLE_NEIGHBORS.json').write_text(json.dumps(roles, indent=2)+'\n')
    parameters = {'Delta': 17, 'D': 3, 'n': 2016, 'm': 16896,
                  'source_recipe': str(source_path.relative_to(root)),
                  'source': {'Delta':16,'D':3,'n':1920,'m':15360,'published':True},
                  'mechanism':'full frozen-source neighborhood cloning of transverse-plane centers',
                  'selected_controller_layers':selected_layers,'normal':[1,1,1],
                  'new_label':'1920+16*i+4*a+b',
                  'old_center':'64*I[i]+a+4*b+16*(a XOR b)',
                  'source_label':'64*u+x0+4*x1+16*x2',
                  'all_original_edges_preserved':True,'new_new_edges':0,
                  'public_located_monotone_guarantee':1920,
                  'degree17_global_threshold':'UNKNOWN','priority':'UNKNOWN'}
    (output / 'PARAMETERS.json').write_text(json.dumps(parameters,indent=2)+'\n')
    elapsed = time.process_time() - start
    result = {'status':'PRODUCED_PENDING_INDEPENDENT_ACCEPTANCE',
              'n':2016,'m':16896,'source_edges':15360,'added_edges':1536,
              'degree_histogram':dict(sorted(degree_histogram.items())),
              'new_roles':96,'distinct_old_pins':1536,'maximum_old_load':1,
              'source_BFS':0,'new_BFS':0,'old_field_rank_certificate_reruns':0,
              'source_recipe_materializations':1,'actual_CPU_seconds':elapsed,
              'portfolio_increment':0,'Lean_increment':0}
    (output / 'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    (output / 'TERMINAL.json').write_text(json.dumps({
        'status':result['status'],'running':False,'CPU_budget_seconds':15,
        'actual_CPU_seconds':time.process_time()-start,'workers':1},indent=2)+'\n')
    signal.setitimer(signal.ITIMER_PROF, 0)
    print(json.dumps(result))


if __name__ == '__main__':
    main()
