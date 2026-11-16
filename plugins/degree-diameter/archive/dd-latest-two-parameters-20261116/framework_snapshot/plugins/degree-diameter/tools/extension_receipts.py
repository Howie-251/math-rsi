"""Consume already-reviewed extension receipts into the existing parent state.

No graph search, BFS, Lean or new mathematical acceptance is performed here.
This adapter supports the current D5 prefix-checker receipt format.
"""
import argparse
import copy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "base/tools"))
from current_context import read_state, write_current


def require(condition, message):
    if not condition:
        raise ValueError(message)


def consume(current, author, independent, *, family_key, evidence, acceptance_basis):
    require(bool(acceptance_basis.strip()), "parent must state the previously accepted evidence")
    require(independent["status"] == "PASS", "independent receipt is not PASS")
    require(author["running"] is False, "batch still running")
    family = current["families"][family_key]
    degree, diameter = family["degree"], family["diameter"]
    source = independent["source"]
    prefixes = independent["prefixes"]
    require(source["n"] == author["source_n"], "source order mismatch")
    known = {family["phase_start_order"], *family["accepted_orders"]}
    require(source["n"] in known, "source has not been accepted in this family")
    require(source["previously_independently_accepted_diameter_upper_bound"] <= diameter,
            "source diameter premise mismatch")
    require(len(prefixes) == author["accepted_new_graphs"]
            == independent["independently_accepted_prefix_count"], "missing prefix checks")
    n, m = source["n"], source["m"]
    for row in prefixes:
        n += 1
        bfs = row["bfs_in_this_prefix"]
        require(row["status"] == "PASS" and row["n"] == n and row["simple"] is True,
                "invalid prefix sequence")
        require(row["maximum_degree"] <= degree and row["all_vertex_degrees_checked"] == n,
                "degree check incomplete")
        require(row["retained_previous_edge_count"] == m and row["removed_edge_count"] == 0
                and row["other_added_edge_count"] == 0, "old-edge inheritance broken")
        require(row["new_vertex"] == n - 1 and row["m"] == m + row["added_edge_count"],
                "extension binding mismatch")
        require(bfs["root"] == n - 1 and bfs["graph_order_at_bfs"] == n
                and bfs["visited_count"] == n and bfs["unreachable_count"] == 0
                and bfs["maximum_distance"] <= diameter, "new-root check incomplete or wrong prefix")
        require(row["prior_prefix_diameter_upper_bound"] <= diameter
                and row["diameter_upper_bound"] <= diameter, "diameter induction mismatch")
        m = row["m"]
    final = independent["final_graph"]
    require((n, m) == (author["final_n"], author["final_m"])
            == (final["n"], final["m"]), "final graph mismatch")
    comparison = independent["author_final_graph_comparison"]
    require(comparison["status"] == "MATCH", "author/independent graph mismatch")
    require(Path(comparison["path"]).name == author["final_edgefile"]
            and (comparison["author_n"], comparison["author_m"]) == (n, m)
            and comparison["missing_edge_count"] == comparison["extra_edge_count"] == 0,
            "graph comparison does not bind the reported final graph")
    require(final["simple"] is True and final["maximum_degree"] <= degree
            and final["diameter_upper_bound"] <= diameter, "final graph not verified")
    result = copy.deepcopy(current)
    updated = result["families"][family_key]
    # Re-consuming the same receipt is idempotent, not another eight graphs.
    received_orders = {p["n"] for p in prefixes}
    new_orders = received_orders - set(family["accepted_orders"])
    # Batch evidence paths identify immutable, previously consumed receipts.
    # A zero-prefix replay must not erase a newer stop on the same graph.
    consumed = updated.setdefault("consumed_receipts", [])
    replay = evidence in consumed
    require(not (replay and new_orders),
            "consumed receipt paths were reused for new prefixes; use new batch evidence paths")
    if not replay:
        consumed.append(copy.deepcopy(evidence))
    updated["accepted_orders"] = sorted(set(family["accepted_orders"]) | received_orders)
    # An old successful receipt may be read again after a later zero-prefix
    # limit/No result on the same graph. It must not rewind that current stop.
    if new_orders and n >= family["latest_graph"]["n"]:
        updated["latest_graph"] = dict(n=n, m=m, maximum_degree=final["maximum_degree"],
                                       diameter_upper_bound=final["diameter_upper_bound"],
                                       edge_file=comparison["path"], evidence=evidence)
    if not replay and n >= family["latest_graph"]["n"] and (not prefixes or new_orders):
        updated["last_batch"] = dict(
            stop_reason=author["status"], accepted_count=len(prefixes),
            whole_CPU=author.get("whole_CPU"), evidence=evidence,
            acceptance_basis=acceptance_basis,
            next_batch="Parent decides a bounded successor within current authorization; none launched.",
            exhausted=author["status"] == "COMPLETE_NO_IN_CURRENT754_SUFFICIENT_PLANE_DOMAIN",
            exhaustion_scope="Only the stated current-graph sufficient plane domain, never all graphs.")
    # Shared formal gaps, review clock, route stops and Goal status are not changed by receipt ingestion.
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--state", type=Path, required=True)
    p.add_argument("--author", type=Path, required=True)
    p.add_argument("--independent", type=Path, required=True)
    p.add_argument("--family", required=True)
    p.add_argument("--acceptance-basis", required=True)
    a = p.parse_args()
    state = read_state(a.state)
    current = consume(state["current_context"], read_state(a.author), read_state(a.independent),
                      family_key=a.family, evidence={"author": str(a.author.resolve()),
                      "independent": str(a.independent.resolve())}, acceptance_basis=a.acceptance_basis)
    write_current(a.state, current)
    print(json.dumps(current["families"][a.family]["latest_graph"], ensure_ascii=False))


if __name__ == "__main__":
    main()
