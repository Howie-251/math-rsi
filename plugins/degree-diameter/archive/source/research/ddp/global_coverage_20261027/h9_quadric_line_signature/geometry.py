"""Deterministic Q(6,9)-line attachment API; no graph adjacency or source lookup.

Field entries 0..8 encode x+3*y for x+y*t, with t^2=-1 over F3.
The fold argument maps normalized coordinate tuples to core vertex labels.
"""
from array import array
from pathlib import Path

ADD = [[(a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3) for b in range(9)] for a in range(9)]
MUL = [[((a % 3) * (b % 3) - (a // 3) * (b // 3)) % 3 +
        3 * (((a % 3) * (b // 3) + (a // 3) * (b % 3)) % 3) for b in range(9)] for a in range(9)]
INV = [0] + [next(b for b in range(1, 9) if MUL[a][b] == 1) for a in range(1, 9)]


def normalize(v):
    scale = INV[next(x for x in v if x)]
    return tuple(MUL[scale][x] for x in v)


def on_quadric(v):
    """X0*X4+X1*X5+X2*X6 == X3^2 in F9."""
    return ADD[ADD[MUL[v[0]][v[4]]][MUL[v[1]][v[5]]]][MUL[v[2]][v[6]]] == MUL[v[3]][v[3]]


def line_points(p, q):
    """Return all10 normalized points on a Q-singular line spanned by p,q.

    Input contract: p,q are distinct normalized 7-coordinate projective points.
    Raises ValueError when their projective line is not contained in Q(6,9).
    """
    p, q = tuple(p), tuple(q)
    assert len(p) == len(q) == 7 and p != q
    assert normalize(p) == p and normalize(q) == q
    line = [normalize(tuple(ADD[p[j]][MUL[t][q[j]]] for j in range(7))) for t in range(9)] + [q]
    if not all(on_quadric(v) for v in line):
        raise ValueError('the projective line is not contained in Q(6,9)')
    assert len(set(line)) == 10
    return sorted(line)


def line_attachment(p, q, fold):
    """Generate an attachment solely from two points and a coordinate->core fold.

    Returns the10 original projective points and their distinct core pins.
    It does not select extra anchors or promise a new-new distance bound.
    """
    points = line_points(p, q)
    return {'point_coordinates': [list(v) for v in points],
            'pins': sorted({fold[v] for v in points})}


def read_cached_fold(point_coords_path, point_to_core_path):
    """Read the small coordinate/fold caches written by identify.py."""
    coordinates = Path(point_coords_path).read_bytes()
    vertices = array('H')
    vertices.frombytes(Path(point_to_core_path).read_bytes())
    assert len(coordinates) == 7 * len(vertices)
    return {tuple(coordinates[7*i:7*i+7]): v for i, v in enumerate(vertices)}
