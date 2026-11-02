"""The one predicted classical PG(2,4) augmentation. No BFS or search."""
from pathlib import Path
import json
import time
from collections import Counter

BASE = Path(__file__).resolve().parent


def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return out


def dot(x, y):
    return mul(x[0], y[0]) ^ mul(x[1], y[1]) ^ mul(x[2], y[2])


def write_edges(path, n, edges):
    with path.open("w") as f:
        f.write(f"{n} {len(edges)}\n")
        for a, b in edges:
            f.write(f"{a} {b}\n")


def main():
    start = time.process_time()
    pred = json.loads((BASE / "PRED.json").read_text())
    points = [(1,a,b) for a in range(4) for b in range(4)]
    points += [(0,1,a) for a in range(4)] + [(0,0,1)]
    edges = [(i,j) for i in range(21) for j in range(i+1,21)
             if dot(points[i],points[j]) == 0]
    adj = [set() for _ in points]
    for i,j in edges:
        adj[i].add(j)
        adj[j].add(i)
    pins = [i for i,x in enumerate(points) if x[0]^x[1]^x[2] == 0]
    absolute = [i for i,x in enumerate(points) if dot(x,x) == 0]
    assert pins == absolute
    pole = points.index((1,1,1))
    assert adj[pole] == set(pins)
    rows = []
    for i,x in enumerate(points):
        typ = "absolute" if i in pins else "pole" if i == pole else "other_nonabsolute"
        hit = sorted((adj[i] | {i}) & set(pins))
        expected = pred["prediction"]["old_point_types"][typ]
        assert len(adj[i]) == expected["degree"]
        assert len(hit) == expected["pins_in_closed_neighborhood"]
        rows.append({"id":i,"coordinates":list(x),"type":typ,
                     "source_degree":len(adj[i]),"spare_to_5":5-len(adj[i]),
                     "pins_in_closed_neighborhood":hit})
    assert Counter(r["type"] for r in rows) == Counter({"absolute":5,"pole":1,"other_nonabsolute":15})
    assert len(edges) == 50 and len(pins) == 5
    covered = set(pins)
    for s in pins:
        covered.update(adj[s])
    assert covered == set(range(21))
    assert all(len(adj[s]) == 4 for s in pins)
    final_edges = sorted(edges + [(s,21) for s in pins])
    final_degrees = [0]*22
    for a,b in final_edges:
        final_degrees[a] += 1
        final_degrees[b] += 1
    assert Counter(final_degrees) == Counter({5:22})
    write_edges(BASE/"source_d5_D2_n21.edges",21,edges)
    write_edges(BASE/"graph_d5_D2_n22.edges",22,final_edges)
    (BASE/"COORDINATES_AND_TYPES.json").write_text(json.dumps({
        "field":{"codes":{"0":"0","1":"1","2":"w","3":"w+1"},
                 "modulus":"w^2+w+1","addition":"bitwise xor"},
        "projective_representatives":"first nonzero coordinate normalized to 1",
        "old_vertices":rows,"new_vertex":{"id":21,"role":"false twin of pole", "pole_id":pole}
    },indent=2)+"\n")
    (BASE/"PINS.json").write_text(json.dumps({
        "pins":pins,"pole_id":pole,"new_id":21,"old_load":[int(i in pins) for i in range(21)],
        "covered_old_vertices":sorted(covered),"source_pin_degrees":[len(adj[i]) for i in pins]
    },indent=2)+"\n")
    result = {"status":"PASS","source_n":21,"source_m":50,
        "source_degree_histogram":dict(sorted(Counter(map(len,adj)).items())),
        "final_n":22,"final_m":55,"final_degree_histogram":{"5":22},
        "pins":pins,"pole_id":pole,"closed_pin_coverage":len(covered),
        "point_type_prediction":"all 21 rows match",
        "retained_old_edges":50,"added_edges":5,"final_spare_vertices":[],
        "BFS_runs":0,"searches":0,"process_CPU_seconds":time.process_time()-start}
    (BASE/"PRODUCTION_RESULT.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
