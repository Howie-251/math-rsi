"""Render downstream inputs from the coordinator's existing project state.

This is not a scheduler, a mathematical verifier, or a second state store.
Only the designated parent writes current_context; workers return evidence.
"""
import argparse
import json
import os
from pathlib import Path
import tempfile
from datetime import datetime, timezone


def resolve_path(path, state_dir=None):
    """Resolve declared paths relative to the existing state directory."""
    path = Path(path)
    if not path.is_absolute() and state_dir is not None:
        path = Path(state_dir) / path
    return path.resolve()


def read_state(path):
    return json.loads(Path(path).read_text())


def write_current(path, current):
    """Replace current facts and refresh an existing configured reading view.

    current_context_view is optional and relative to STATE.json when not absolute.
    The reading view is generated output, never a second source of facts.
    """
    path = Path(path)
    state = read_state(path)
    state["current_context"] = current
    state["current_context_updated_at"] = datetime.now(timezone.utc).isoformat()
    with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
        f.write("\n")
        name = f.name
    os.replace(name, path)
    view = state.get("current_context_view")
    if view:
        view = Path(view)
        if not view.is_absolute():
            view = path.parent / view
        view.write_text(render(state))
    return state


def snapshot(state, routes=None):
    current = dict(state["current_context"])
    stops = current.get("route_stops", {})
    if routes:
        # A typo must not silently drop the relevant negative history.
        current["route_stops"] = {key: stops[key] for key in routes}
    return {**current, "goal_status": state["status"],
            "as_of": state.get("current_context_updated_at")}


def render(state, routes=None):
    return ("Current facts from the existing project STATE.json; historical logs "
            "do not override this view. This snapshot is not authorization to run.\n"
            + json.dumps(snapshot(state, routes), ensure_ascii=False, indent=2) + "\n")


def require_consumed_results(state, state_dir=None):
    """Catch returned jobs still advertised as pending before issuing new input.

    terminal_result is an optional, explicitly registered final JSON output,
    not a progress file. Its presence requires parent consumption, not acceptance
    of its mathematical claims. Rendering a reading view remains unrestricted.
    """
    jobs = state["current_context"].get("current_work", {}).get("in_flight", {})
    for name, job in jobs.items():
        result = job.get("terminal_result")
        if not result:
            continue
        result = Path(result)
        if not result.is_absolute():
            if state_dir is None:
                raise ValueError("relative terminal_result requires state_dir")
            result = Path(state_dir) / result
        if result.exists():
            raise ValueError(
                f"Returned result for {name} must be consumed by the parent before "
                f"new input: {result}. Update current facts and remove the returned "
                "job from in_flight; author claims may remain pending verification."
            )


def request_text(state, request, *, state_dir=None):
    """Caller chooses reuse/delta/new after comparing mathematical scope.

    We check the declared action, not mathematical equivalence of two claims.
    A reusable review does not certify a later graph or waive final review.
    """
    require_consumed_results(state, state_dir)
    mode = request["review_mode"]
    changes = request.get("changes", [])
    prior = request.get("prior_reviews", [])
    if mode not in {"reuse", "delta", "new", "task"}:
        raise ValueError("review_mode must be reuse, delta, new or task")
    if mode == "reuse" and (changes or not prior or not request.get("reuse_scope", "").strip()):
        raise ValueError("reuse requires prior evidence, explicit unchanged scope, and no changes")
    if mode == "delta" and not changes:
        raise ValueError("delta review requires the actual changed assumption/domain/code/claim")
    for review in prior:
        if not resolve_path(review["path"], state_dir).is_file() or not review.get("scope", "").strip():
            raise ValueError("prior review needs an existing original and its applicable scope")
    intent = {
        "reuse": "Consume the cited review; no new model call for that unchanged obligation.",
        "delta": "Review the stated changes and their consequences; reuse unaffected evidence.",
        "new": "New review question; no prior acceptance is implied.",
        "task": "Task input for the caller's authorized scope; return evidence to the parent.",
    }[mode]
    if mode == "delta" and not prior:
        intent = "Review the stated changes and their consequences; no prior review is supplied or claimed reusable."
    path_context = ("All relative paths declared in this state snapshot and request "
                    "(including review and terminal-result paths) resolve against "
                    f"the STATE directory: {Path(state_dir).resolve()}\n"
                    if state_dir is not None else "")
    return (path_context + render(state, request.get("routes")) + "\n" + intent + "\n"
            + json.dumps(request, ensure_ascii=False, indent=2)
            + "\nPer-instance validation and the original final-review contract remain in force.\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--request", type=Path, help="optional task/review description JSON")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    state = read_state(args.state)
    text = (request_text(state, read_state(args.request), state_dir=args.state.parent)
            if args.request else render(state))
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
