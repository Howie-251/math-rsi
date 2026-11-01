"""Reuse the checked single-layout exporter on the frozen 22/23 witnesses.

Only 16 and 26 relabeling representatives are exported. The separate coverage
theorem transports every admissible labelled input to one of these rows.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent
sys.path.insert(0, str(ROOT / "computations"))
from multilock import Profile, pair_weight, rows, total_bound, json_value

frozen = json.loads((ROOT / "context/propertyb34-hour1-20261013/MIDDLE_THRESHOLDS_VERIFIED.json").read_text())["profiles"]
exporter = (HERE.parent / "twentyone-lean/generate_six_single.py").read_text()
exporter = exporter[exporter.index("G=defaultdict(dict)"):]
for vertex_count, prefix, expected in [(22, "TwentyTwoStrong", 16), (23, "TwentyThreeStrong", 26)]:
    raw = [dict(ds=[7, 7, 7], counts=r["counts"], pos=r["positions"],
                cs=r["certificates"]) for r in frozen
           if r["kind"] == "triple" and r["v"] == vertex_count]
    assert len(raw) == expected
    source = exporter.replace("TwentyOneSix", prefix)
    source = re.sub(r"(?<![0-9])21(?![0-9])", str(vertex_count), source)
    source = re.sub(r"(?<![0-9])20(?![0-9])", str(vertex_count - 1), source)
    env = dict(globals(), __file__=str(Path(__file__).resolve()), raw=raw)
    exec(compile(source, str(Path(__file__).resolve()), "exec"), env)
