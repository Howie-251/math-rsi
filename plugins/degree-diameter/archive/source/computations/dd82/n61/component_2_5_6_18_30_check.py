"""Check one explicitly derived abstract quotient; no graph realization asserted."""
from pathlib import Path
import json
import time


def main():
    start = time.process_time()
    sizes = [2, 5, 6, 18, 30]
    q = [[0, 5, 3, 0, 0], [2, 0, 0, 0, 6], [1, 0, 1, 6, 0],
         [0, 0, 2, 1, 5], [0, 1, 0, 3, 4]]
    c = len(sizes)
    assert sum(sizes) == 61
    assert all(sum(row) == 8 for row in q)
    assert sum(q[i][i] for i in range(c)) == 8-(c-1)//2
    for i in range(c):
        assert 0 <= q[i][i] < sizes[i] and sizes[i]*q[i][i] % 2 == 0
        for j in range(c):
            assert isinstance(q[i][j], int) and 0 <= q[i][j] <= sizes[j]
            assert sizes[i]*q[i][j] == sizes[j]*q[j][i]
            value = sum(q[i][k]*q[k][j] for k in range(c))+q[i][j]-11*(i == j)
            assert value == sizes[j], (i, j, value, sizes[j])
    i, j = 2, 3
    assert q[i][i] == q[j][j] == 1 and q[i][j] > 0
    assert all(q[i][k]*q[k][j] == 0 for k in range(c) if k not in (i, j))
    result = dict(status='EXACT_ABSTRACT_QUOTIENT_VERIFIED', sizes=sizes, Q=q,
                  complete_polynomial_entries=c*c, balanced_interfaces_checked=c*c,
                  matching_edge_obstruction_indices=[i, j],
                  graph_realized=False,
                  scope='One abstract quotient only; no coverage assertion about other quotients',
                  cpu_seconds=time.process_time()-start)
    Path(__file__).with_suffix('.result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
