import argparse
import json
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="command", required=True)
    s = sub.add_parser("spine")
    s.add_argument("--output", required=True)
    r = sub.add_parser("run")
    r.add_argument("--config")
    r.add_argument("--output", required=True)
    r.add_argument("--rounds", type=int, default=1)
    r.add_argument("--resume", action="store_true")
    a = p.parse_args()
    if a.command == "run":
        from .loop import run
        run(a.config, a.output, a.rounds, a.resume)
        return
    out = Path(a.output)
    out.mkdir(parents=True, exist_ok=True)
    graph = {"n": 2, "edges": [[0, 1], [0, 2], [1, 3]]}
    # F0 is an actual three-edge C4-free graph. Evolution arrives in F2.
    result = {"stage": "F0_spine_only", "graph": graph, "edge_count": 3}
    (out / "spine_smoke.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
