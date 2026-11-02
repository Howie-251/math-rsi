"""One exact30-controller open-neighborhood packing; no lifted graph checks."""
import json
from pathlib import Path
import signal
import time


def main():
    start = time.process_time()
    here = Path(__file__).resolve().parent
    root = next(p for p in here.parents if (p / 'formal').is_dir())
    source = root / 'research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json'
    data = json.loads(source.read_text())
    controller = data['controller']
    assert len(controller) == 30
    neighborhoods = [sum(1 << v for v in row) for row in controller]
    assert all(n.bit_count() == 4 for n in neighborhoods)
    compatible = [sum(1 << v for v in range(30)
                      if v != u and not (neighborhoods[u] & neighborhoods[v]))
                  for u in range(30)]
    incumbent = []
    nodes = 0

    def timeout(_signum, _frame):
        raise TimeoutError

    signal.signal(signal.SIGPROF, timeout)
    signal.setitimer(signal.ITIMER_PROF, max(0.001, 10 - (time.process_time() - start)))

    def search(candidates, chosen):
        nonlocal incumbent, nodes
        nodes += 1
        if len(chosen) > len(incumbent):
            incumbent = chosen[:]
        if len(incumbent) == 7:
            return
        while candidates:
            if len(chosen) + candidates.bit_count() <= len(incumbent):
                return
            bit = candidates & -candidates
            candidates ^= bit
            v = bit.bit_length() - 1
            search(candidates & compatible[v], chosen + [v])
            if len(incumbent) == 7:
                return

    status = 'EXACT_OPTIMUM'
    try:
        search((1 << 30) - 1, [])
    except TimeoutError:
        status = 'UNKNOWN_WITH_RETAINED_INCUMBENT'
    finally:
        signal.setitimer(signal.ITIMER_PROF, 0)
    union = 0
    for v in incumbent:
        assert not union & neighborhoods[v]
        union |= neighborhoods[v]
    selected_edges = [[u, v] for i, u in enumerate(incumbent)
                      for v in incumbent[i + 1:] if v in controller[u]]
    result = {
        'status': status,
        'source': str(source.relative_to(root)),
        'controller_vertices': 30,
        'routine_capacity_upper': 7,
        'packing_size': len(incumbent),
        'controller_centers': incumbent,
        'literal_neighborhoods': {str(v): controller[v] for v in incumbent},
        'covered_controller_vertices': [v for v in range(30) if union >> v & 1],
        'selected_induced_edges': selected_edges,
        'search_nodes': nodes,
        'prediction': 'exact_maximum6',
        'prediction_result': ('SUPPORTED' if status == 'EXACT_OPTIMUM' and len(incumbent) == 6
                              else 'REFUTED' if status == 'EXACT_OPTIMUM' else 'UNKNOWN'),
        'conditional_lifted_center_count': 16 * len(incumbent),
        'conditional_degree17_order': 1920 + 16 * len(incumbent),
        'new_accepted_graphs': 0,
        'old_source_BFS_field_rank_Lean_runs': 0,
    }
    elapsed = time.process_time() - start
    result['actual_CPU_seconds'] = elapsed
    (here / 'CONTROLLER_PACKING_RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    terminal = {'status': status, 'actual_CPU_seconds': time.process_time() - start,
                'CPU_budget_seconds': 10, 'workers': 1, 'automatic_continuation': False}
    (here / 'CONTROLLER_PACKING_TERMINAL.json').write_text(json.dumps(terminal, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
