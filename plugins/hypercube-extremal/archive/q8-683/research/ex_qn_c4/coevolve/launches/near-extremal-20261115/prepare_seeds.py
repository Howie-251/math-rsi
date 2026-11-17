"""Reproducible indicator-calibration samples, not new extremal records."""
from pathlib import Path
import json
import random
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from cube_coevolve.graphs import graph_id, read_edges, validate

out = Path(__file__).resolve().parent
(out / "seeds").mkdir(exist_ok=True)
rng = random.Random(20261115)
rows = []
for source_index in range(1, 5):
    source = ROOT.parent / f"proofs/q8_seed_isometries_cycle011/seed{source_index}.edges"
    original, _ = validate(8, read_edges(source))
    seen = set()
    for deletions in (1, 2):
        for sample in range(3):
            while True:
                removed = set(rng.sample(original, deletions))
                graph, verification = validate(8, [e for e in original if e not in removed])
                identifier = graph_id(8, graph)
                if identifier not in seen:
                    seen.add(identifier)
                    break
            path = out / "seeds" / f"seed{source_index}_delete{deletions}_{sample}.edges"
            path.write_text("".join(f"{u} {v}\n" for u, v in graph))
            rows.append({"path": str(path.relative_to(ROOT)), "source": str(source), "removed": sorted(removed),
                         "id": identifier, "verification": verification})
(out / "SEED_INVENTORY.json").write_text(json.dumps({"scope": "24 derived calibration samples, not new records or a full extremal classification", "samples": rows}, indent=2) + "\n")
config = json.loads((ROOT / "configs/q8.json").read_text())
config["quality_band"] = {"min_edges": 680}
config["focus_schedule"] = ["objective", "challenge", "objective", "novelty"]
config["seed_files"].extend("../" + r["path"] for r in rows)
config["search_steps"] = 80
config["program_timeout_seconds"] = 60
config["research_context"] += " Near-extremal campaign: focus on 680..682 edges and target 683. 680 is a heuristic QUALITY threshold, not a theorem premise. Derived 680/681 samples obtained by deleting one/two edges are calibration data, not novel constructions. Do not restrict future searches to that deletion family or restart its proved-small repair exclusions. Intermediate states may lose more edges before repairing. Upper discovery prioritizes dense samples, but every archived graph still checks every applicable inequality. Conditional conjectures edges>=680 are relevant to every 683+ graph; unrelated conditions require their own coverage proof. Show actual mathematics connecting learned correlations to the Q8 goal."
(ROOT / "configs/q8_near_extremal.json").write_text(json.dumps(config, indent=2) + "\n")
print(json.dumps({"derived_samples": len(rows), "edge_counts": sorted({r['verification']['edges'] for r in rows}), "config": "configs/q8_near_extremal.json"}))
