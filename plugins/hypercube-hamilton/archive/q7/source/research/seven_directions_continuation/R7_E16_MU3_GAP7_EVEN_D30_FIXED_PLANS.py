"""One all-axis plan pass on the fixed five-branch gap-seven D=30 basis."""

from collections import Counter
import json
from pathlib import Path
from time import process_time
from unittest.mock import patch

import R7_E16_MU3_GAP7_EVEN_MINIMAL_FIXED_PLANS as gates


BASE = Path(__file__).with_name("R7_E16_MU3_GAP7_EVEN_D30_BASE.json")
BASE_SHA256 = "aadd47734210dedab65ef09f9390407c2e99ff7de14fcf7e58a4dc8a948eb253"
EXPECTED = 27936
CPU_LIMIT = 180
K3_AUDITED_DONORS = frozenset({
    "Q6_balanced_complement_avoid_two", "Q6_same_side_majority_root",
    "Q6_same_side_two_minority_roots", "T26_separated_two_root_choice",
    "Q6_T26_paired_S1", "T26_two_majority_roots", "T15_same_face",
    "T15_isolated_mark", "Q6_T15_D4", "T15_exact_core",
})


def run(start):
    data = json.loads(BASE.read_bytes())
    assert data["status"] == "complete" and data["record_count"] == EXPECTED
    previous_supplier = gates.supplier

    def audited_supplier(outer, minor, retained, marks, lookup, t26):
        plan = previous_supplier(outer, minor, retained, marks, lookup, t26)
        return plan if plan and plan["kind"] in K3_AUDITED_DONORS else None

    with (
        patch.object(gates, "BASE", BASE),
        patch.object(gates, "BASE_SHA256", BASE_SHA256),
        patch.object(gates, "EXPECTED", EXPECTED),
        patch.object(gates, "CPU_LIMIT", CPU_LIMIT),
        patch.object(gates, "supplier", audited_supplier),
        patch.object(gates, "t26_registry", dict),
    ):
        result = gates.run(start)
    result["audited_k3_donor_kinds"] = sorted(K3_AUDITED_DONORS)
    result["case_plan_counts"] = {
        case: dict(Counter(item["plan"]["gate"] for item in result["positives"]
                           if data["records"][item["index"]]["case"] == case))
        for case in data["counts"]
    }
    return result


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as file:
        json.dump(result, file, separators=(",", ":"))
        file.write("\n")
    print(json.dumps({key: value for key, value in result.items() if key != "positives"}, indent=2))
