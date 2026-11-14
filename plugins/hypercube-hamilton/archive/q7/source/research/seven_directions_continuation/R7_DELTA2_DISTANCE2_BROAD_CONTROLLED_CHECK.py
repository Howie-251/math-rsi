"""Check controlled circle donors with four through six bridges on three fixed tails."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
from time import process_time

from R7_CONTROLLED_CYCLE_DONOR_EXTENDED_PROBE import geometry
from R7_CONTROLLED_CYCLE_DONOR_PROBE import PERMUTATIONS
from R7_MU3_COVERAGE_CIRCLE_T63_V3 import marked_ranks


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "R7_DELTA2_DISTANCE2_BROAD_PLANS.json"
NEW_RANK_PROOF = HERE / "R7_MU3_T63_NEW_RANK.md"


def new_ranks():
    rows = re.findall(r"^\| (\d+) \| ([\d,]+) \| ([\d,]+) \| [\d,]+ \|",
                      NEW_RANK_PROOF.read_text(encoding="utf-8"), re.M)
    assert len(rows) == 6
    return [(int(i), *(tuple(map(int, field.split(","))) for field in (h, u))) for i, h, u in rows]


def t63(face, old, new):
    h, u = (tuple(face[key]) for key in ("majority", "marks"))
    if (h, u) in old:
        rank, p, z = old[h, u]
        return dict(kind="T63_old", rank=rank, rank_to_local_permutation=p, rank_to_local_xor=z)
    for rank, target_h, target_u in new:
        for z in u:
            for image in PERMUTATIONS:
                if tuple(sorted(image[v ^ z] for v in u)) != target_u:
                    continue
                if tuple(sorted(image[v ^ z] for v in h)) == target_h:
                    permutation = tuple(image[1 << i].bit_length() - 1 for i in range(5))
                    return dict(kind="T63_new", rank=rank, local_to_rank_xor=z,
                                local_to_rank_permutation=permutation)
    used, kept = set(u), set(h) - set(u)
    for i in range(5):
        n, m = (sum(v >> i & 1 for v in group) for group in (used, kept))
        if n == m and n in (1, 2):
            return dict(kind="T63_split", local_inner=i)
    return None


def tool(face, old, new):
    shape = face["q"], len(face["minority"])
    if shape[0] == 1:
        return dict(kind="avoid_one")
    if shape == (2, 0):
        return dict(kind="T44")
    if shape == (2, 1):
        return dict(kind="T15")
    if shape == (3, 0):
        return t63(face, old, new)
    return None


def main():
    start = process_time()
    old, old_hashes = marked_ranks()
    new = new_ranks()
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    results = []
    for row in source["rows"]:
        if row["result"]:
            continue
        counts = Counter()
        missing = Counter()
        plans = []
        fixed_plan = None
        for k in (4, 5, 6):
            for plan in geometry(row["even"] + row["odd"], k, start):
                counts[k] += 1
                interfaces = [tool(face, old, new) for face in plan["faces"]]
                if all(interfaces):
                    witness = dict(plan, k=k, interfaces=interfaces)
                    plans.append(witness)
                    if (row["reference"]["pair"] == 1 and plan["outer"] == 5 and plan["inner"] == 4
                            and tuple(plan["sources"]) == (5, 9, 17, 77)):
                        fixed_plan = witness
                else:
                    missing.update((face["q"], len(face["minority"]))
                                   for face, interface in zip(plan["faces"], interfaces) if not interface)
        if row["reference"]["pair"] == 1:
            assert fixed_plan and fixed_plan["interfaces"][0]["kind"] == "T63_new"
            assert fixed_plan["interfaces"][0]["rank"] == 4
        result = dict(reference=row["reference"], raw_geometry=dict(counts),
                      unhandled_face_shapes={str(key): n for key, n in missing.items()},
                      accepted_plan_count=len(plans), witness=fixed_plan or (plans[0] if plans else None))
        if row["reference"]["pair"] == 13:
            receive = {v for v in row["odd"] if v & 1}
            result["rejected_trial"] = dict(outer=0, inner=2, donor_side=0,
                                            majority_by_inner_side=[
                                                sorted(v for v in receive if (v >> 2 & 1) == b) for b in (0, 1)
                                            ])
        results.append(result)
    assert len(results) == 3
    output = dict(source_sha256=sha256(SOURCE.read_bytes()).hexdigest(),
                  new_T63_proof_sha256=sha256(NEW_RANK_PROOF.read_bytes()).hexdigest(),
                  old_T63_source_sha256=old_hashes, rows=results,
                  matching_calls=0, hamilton_calls=0, rank_runs=0, cpu_seconds=process_time() - start)
    (HERE / "R7_DELTA2_DISTANCE2_BROAD_CONTROLLED_RESULT.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8",
    )
    print(json.dumps(results))


if __name__ == "__main__":
    main()
