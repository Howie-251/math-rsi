"""Exact finite verification of saved exterior-moment separating inequalities.

Standard library only; neither calls an LP solver nor regards a floating
feasible vector as a graph. The original-graph moment lemma is a separate
mathematical dependency.
"""
from pathlib import Path
import itertools
import json

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "computations/dd82/n62/component_exterior_moments.json"


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def main():
    data = json.loads(SOURCE.read_text())
    actual = {(c["k"], c["a"], c["b"], c["s"], c["t"]): c for c in data["cases"]}
    assert len(actual) == len(data["cases"])
    expected, excluded, remaining, checked_points = set(), [], [], 0
    h = 12
    for k,a,b in [(12,4,4),(16,4,3),(20,5,3),(24,6,3),(28,7,3)]:
        for s,t in itertools.product(range(9-a),range(9-b)):
            rhs = [62-h-k,h*(8-s-a),k*(8-t-b),
                   h*(h+2-s*s-a*(b-1)),k*(k+2-t*t-b*(a-1)),
                   h*(k-a*(s+t+1))]
            if any(v < 0 for v in rhs):
                continue
            key = k,a,b,s,t
            expected.add(key)
            entry = actual[key]
            assert entry["h"] == h and entry["rhs"] == rhs
            domain = [(x,y) for x in range(9) for y in range(9-x)
                      if (s+1)*x+b*y<=h and a*x+(t+1)*y<=k]
            assert entry["domain"] == list(map(list,domain))
            if entry["status_label"] == "EXACT_SEPARATOR_FOR_MOMENT_SYSTEM":
                z = entry["separator"]
                assert len(z)==6 and all(type(v) is int for v in z)
                values = [dot(z,[1,x,y,x*(x-1),y*(y-1),x*y]) for x,y in domain]
                assert min(values)>=0
                target = dot(z,rhs)
                assert target<0 and target==entry["rhs_value"]
                assert min(values)==entry["domain_min"]
                excluded.append(key)
                checked_points += len(domain)
            else:
                remaining.append(key)
    assert set(actual)==expected
    print(json.dumps(dict(status="EXACT_INTEGER_SEPARATORS_CHECKED",
                          total_cases=len(expected), excluded_moment_cases=len(excluded),
                          remaining_cases=remaining, checked_domain_points=checked_points,
                          scope="conditional finite moment systems only; no Lean graph bridge"),indent=2))


if __name__=="__main__":
    main()
