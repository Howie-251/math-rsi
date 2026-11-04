"""Resolve only declared runtime paths inside a relocatable package."""
from pathlib import Path
if not __debug__: raise RuntimeError("Do not disable assertions with Python -O")
import json
ROOT = Path(__file__).resolve().parents[1]
def load_manifest(path):
    m = json.loads(Path(path).read_text())
    def resolve(value):
        rel = Path(value)
        if rel.is_absolute() or ".." in rel.parts:
            raise ValueError(f"Expected a package-relative path: {value}")
        p = (ROOT / rel).resolve()
        if not p.is_relative_to(ROOT) or not p.is_file():
            raise ValueError(f"Missing or escaping input: {value}")
        return str(p)
    m["actual_matrix_snapshot"] = resolve(m["actual_matrix_snapshot"])
    for rec in m["records"]:
        for part in ("original_scan", "independent_full_F", "pair_graph"):
            for key, value in rec[part].items():
                if key.endswith("_path"):
                    rec[part][key] = resolve(value)
    return m
