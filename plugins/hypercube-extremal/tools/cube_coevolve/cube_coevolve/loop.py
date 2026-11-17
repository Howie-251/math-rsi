"""A small, inspectable co-evolution loop; conjecture discovery is not proof."""
import copy
import hashlib
import json
from pathlib import Path
import random
import sys
from .graphs import graph_id, greedy, read_edges, validate
from .metrics import Registry
from .inequalities import applicable, check_conditions, evaluate, exhaustive_oracle, normalize
from .providers import propose
from .runtime import execute
from .reward import freeze, score, select_parents


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def load_config(path):
    path = Path(path).resolve()
    config = json.loads(path.read_text())
    registry = Registry(config["n"], config.get("metrics", []))
    goal = config["goal"]
    if goal.get("metric", "edges") not in registry.names or type(goal["target"]) is not int:
        raise ValueError("goal needs a registered metric and integer target")
    if goal.get("sense", "max") not in ("max", "min"):
        raise ValueError("goal sense must be max/min")
    check_conditions(goal.get("conditions", []), registry.names)
    proof_goal = config.get("primary_proof_goal")
    if proof_goal is not None:
        if (not isinstance(proof_goal, dict) or set(proof_goal) != {"statement", "upper_bound"}
                or not isinstance(proof_goal["statement"], str) or not proof_goal["statement"].strip()
                or type(proof_goal["upper_bound"]) is not int
                or goal.get("metric", "edges") != "edges" or goal.get("sense", "max") != "max"
                or goal["target"] != proof_goal["upper_bound"] + 1):
            raise ValueError("primary_proof_goal needs statement/upper_bound and an edge counterexample target one higher")
    if config["provider"]["backend"] not in ("offline", "codex"):
        raise ValueError("provider backend must be offline/codex")
    for key, default in (("seed", 17), ("search_steps", 16), ("max_graphs", 4), ("program_timeout_seconds", 15), ("bootstrap_random", 2)):
        config.setdefault(key, default)
        if type(config[key]) is not int or config[key] < (0 if key in ("seed", "bootstrap_random") else 1):
            raise ValueError(f"invalid positive integer setting {key}")
    if config["max_graphs"] > 32:
        raise ValueError("max_graphs must be <=32")
    band = config.get("quality_band")
    if band is not None:
        if not isinstance(band, dict) or set(band) != {"min_edges"} or type(band["min_edges"]) is not int or not 0 <= band["min_edges"] <= config["n"] * 2**(config["n"]-1):
            raise ValueError("quality_band needs a valid integer min_edges")
        if goal.get("metric", "edges") != "edges" or goal.get("sense", "max") != "max":
            raise ValueError("quality_band currently applies only to edge-maximization tasks")
    schedule = config.get("focus_schedule", ["objective", "challenge", "novelty", "condition"])
    if not isinstance(schedule, list) or not schedule or any(s not in ("objective", "challenge", "novelty", "condition") for s in schedule):
        raise ValueError("focus_schedule must be a nonempty list of supported focus names")
    config["seed_files"] = [str((path.parent / p).resolve()) for p in config.get("seed_files", [])]
    config["config_source"] = str(path)
    return config


def add_graph(state, registry, edges, origin, output, program_id=None):
    normalized, verification = validate(registry.n, edges)
    identifier = graph_id(registry.n, normalized)
    existing = next((g for g in state["graphs"] if g["id"] == identifier), None)
    if existing:
        if program_id and program_id not in existing["program_ids"]:
            existing["program_ids"].append(program_id)
        return existing, False
    graph = {"id": identifier, "n": registry.n, "edges": [list(e) for e in normalized],
             "metrics": registry.compute(normalized), "origin": origin,
             "program_ids": [program_id] if program_id else [], "verification": verification}
    state["graphs"].append(graph)
    write_json(output / "graphs" / (identifier + ".json"), graph)
    edge_path = output / "graphs" / (identifier + ".edges")
    edge_path.write_text("".join(f"{u} {v}\n" for u, v in normalized))
    return graph, True


def initialize(config, output):
    registry = Registry(config["n"], config.get("metrics", []))
    state = {"schema_version": 1, "completed_rounds": 0, "config": config,
             "metric_definitions": registry.definitions, "graphs": [], "programs": [], "inequalities": [], "rounds": []}
    for path in config["seed_files"]:
        add_graph(state, registry, read_edges(Path(path)), {"kind": "imported_seed", "path": path}, output)
    add_graph(state, registry, [], {"kind": "empty_graph_exploration"}, output)
    for i in range(config["bootstrap_random"]):
        add_graph(state, registry, greedy(config["n"], random.Random(config["seed"] + i)), {"kind": "bootstrap_greedy", "seed": config["seed"] + i}, output)
    for raw in config.get("initial_inequalities", []):
        inequality = normalize(raw, registry)
        state["inequalities"].append(evaluate(inequality, state["graphs"]))
    return state


def training_view(graphs, registry, quality_band=None):
    # Deterministic discovery/challenge partition, NOT independent statistical validation.
    train = [g for g in graphs if int(g["id"][-2:], 16) % 4 != 0]
    if not train:
        train = graphs[:1]
    discovery_policy = "all densities"
    if quality_band:
        dense = [g for g in train if g["metrics"]["edges"] >= quality_band["min_edges"]]
        if dense:
            train = dense
            discovery_policy = f"near-extremal discovery: edges>={quality_band['min_edges']}; every archived graph still checked"
    train_ids = {g["id"] for g in train}
    heldout_ids = [g["id"] for g in graphs if g["id"] not in train_ids]
    clusters = {}
    for g in train:
        m = g["metrics"]
        key = f"odd={m['even_squares'] == 0};edge_bin={m['edges']//4};mindeg={m['min_degree']}"
        clusters.setdefault(key, []).append(g)
    cluster_rows = []
    for key, members in clusters.items():
        cluster_rows.append({"cell": key, "count": len(members),
                             "metric_ranges": {name: [min(g["metrics"][name] for g in members), max(g["metrics"][name] for g in members)] for name in sorted(registry.names)},
                             "representative": {"id": members[0]["id"], "metrics": members[0]["metrics"]}})
    # Max-edge ordering keeps dense extremes visible when the archive grows.
    rows = sorted(train, key=lambda g: g["metrics"]["edges"], reverse=True)[:48]
    return {"discovery_ids": [g["id"] for g in train], "challenge_ids_not_shown": heldout_ids,
            "discovery_policy": discovery_policy,
            "samples": [{"id": g["id"], "metrics": g["metrics"]} for g in rows], "clusters": cluster_rows,
            "assurance": "adaptive discovery sample; all archived graphs, including held-out ones, are checked by host"}, train


def challenge_turn_index(config, round_index):
    schedule = config.get("focus_schedule", ["objective", "challenge", "novelty", "condition"])
    periods, prefix = divmod(round_index, len(schedule))
    return periods * schedule.count("challenge") + schedule[:prefix].count("challenge")


def counterexample_view(state, limit=4):
    refutes = {}
    for inequality in reversed(state["inequalities"]):
        for identifier in inequality.get("counterexample_ids", []):
            refutes.setdefault(identifier, []).append(inequality["id"])
    selected = list(refutes)[:limit]
    by_id = {g["id"]: g for g in state["graphs"]}
    return [{"id": identifier, "n": by_id[identifier]["n"], "edges": by_id[identifier]["edges"],
             "metrics": by_id[identifier]["metrics"], "refutes": refutes[identifier]} for identifier in selected]


def run_round(state, output):
    config = state["config"]
    index = state["completed_rounds"]
    directory = output / "rounds" / f"{index:04d}"
    directory.mkdir(parents=True, exist_ok=True)
    registry = Registry(config["n"], state["metric_definitions"])
    snapshot = freeze(state["inequalities"], state["graphs"], config["goal"], challenge_turn_index(config, index), config.get("quality_band"))
    write_json(directory / "reward_before.json", snapshot)
    parents = select_parents(state["graphs"], snapshot, round_index=index)
    focus = config.get("focus_schedule", ["objective", "challenge", "novelty", "condition"])[index % len(config.get("focus_schedule", [0, 1, 2, 3]))]
    if focus not in ("objective", "challenge", "novelty", "condition"):
        raise ValueError("unknown focus")
    parent_program_ids = {pid for g in parents for pid in g["program_ids"]}
    source_programs = [{k: p[k] for k in ("id", "name", "source", "evaluation")} for p in state["programs"] if p["id"] in parent_program_ids][-4:]
    context = {"n": registry.n, "round": index, "seed": config["seed"] + index * 1009, "goal": config["goal"],
               "search_steps": config["search_steps"], "max_graphs": config["max_graphs"], "focus": focus,
               "metric_definitions": registry.definitions, "reward_snapshot": snapshot,
               "parents": [{k: g[k] for k in ("id", "edges", "metrics", "selection_channel", "reward")} for g in parents]}
    prompt_context = {**context, "registry": registry.describe(), "parent_programs": source_programs,
                      "recent_program_failures": [{k: p[k] for k in ("id", "source", "evaluation")} for p in state["programs"] if p["evaluation"]["status"] != "ok"][-4:],
                      "research_context": config.get("research_context", "")}
    if config.get("primary_proof_goal"):
        prompt_context.update(primary_proof_goal=config["primary_proof_goal"],
                              search_role="adversarial counterexamples and structural data; search failure is not an upper-bound proof")
    print(f"round {index}: lower/{config['provider']['backend']} focus={focus}", flush=True)
    lower, lower_receipt = propose("lower", prompt_context, config["provider"], directory / "lower")
    if not isinstance(lower, dict) or not isinstance(lower.get("programs"), list) or not 1 <= len(lower["programs"]) <= 4:
        raise ValueError("lower response must contain 1..4 programs")
    accepted = rejected = new_count = 0
    programs = []
    for offset, proposal in enumerate(lower["programs"]):
        source = proposal["source"]
        pid = f"r{index:04d}p{offset}_" + hashlib.sha256(source.encode()).hexdigest()[:10]
        program_dir = directory / pid
        execution_path = program_dir / "execution.json"
        execution = json.loads(execution_path.read_text()) if execution_path.exists() else execute(source, context, program_dir, config["program_timeout_seconds"])
        evaluations = []
        for candidate in execution["graphs"]:
            try:
                if not isinstance(candidate, dict) or "edges" not in candidate:
                    raise ValueError("candidate must have edges")
                if "n" in candidate and candidate["n"] != registry.n:
                    raise ValueError("candidate dimension differs from task")
                graph, fresh = add_graph(state, registry, candidate["edges"], {"kind": "generated", "round": index, "program": pid}, output, pid)
                reward = score(graph["metrics"], snapshot, graph["id"])
                evaluations.append({"status": "accepted", "graph_id": graph["id"], "new": fresh, "reward": reward})
                accepted += 1
                new_count += fresh
            except (ValueError, TypeError, KeyError) as exc:
                evaluations.append({"status": "rejected", "error": str(exc)})
                rejected += 1
        evaluation = {"status": execution["status"] if execution["status"] != "ok" else ("ok" if any(e["status"] == "accepted" for e in evaluations) else "no_valid_graphs"),
                      "execution": {k: v for k, v in execution.items() if k != "graphs"}, "outputs": evaluations}
        program = {"id": pid, "name": str(proposal.get("name", pid)), "source": source,
                   "parent_program_ids": [p["id"] for p in source_programs], "parent_graph_ids": [g["id"] for g in parents], "focus": focus, "round": index,
                   "rationale": proposal.get("rationale", ""), "evaluation": evaluation}
        state["programs"].append(program)
        programs.append(pid)
        write_json(program_dir / "evaluation.json", evaluation)
    # Retire older conjectures immediately if new lower-side outputs refute them.
    state["inequalities"] = [evaluate(i, state["graphs"]) for i in state["inequalities"]]
    view, discovery = training_view(state["graphs"], registry, config.get("quality_band"))
    upper_context = {"n": registry.n, "goal": config["goal"], "registry": registry.describe(), "graph_clusters": view,
                     "actual_counterexamples": counterexample_view(state),
                     "previous_inequalities": state["inequalities"], "new_program_ids": programs,
                     "research_context": config.get("research_context", "")}
    if config.get("primary_proof_goal"):
        upper_context.update(primary_proof_goal=config["primary_proof_goal"],
                             proof_role="lead with obligations covering the full counterexample domain; every conjecture remains unproved")
    print(f"round {index}: upper/{config['provider']['backend']} archive={len(state['graphs'])}", flush=True)
    upper, upper_receipt = propose("upper", upper_context, config["provider"], directory / "upper", registry, discovery)
    if not isinstance(upper, dict) or not isinstance(upper.get("inequalities"), list) or not 1 <= len(upper["inequalities"]) <= 8:
        raise ValueError("upper response must contain 1..8 inequality proposals")
    if not isinstance(upper.get("metrics", []), list) or len(upper.get("metrics", [])) > 2:
        raise ValueError("upper may request at most 2 declarative metrics")
    proposal_log = []
    for definition in upper.get("metrics", []):
        try:
            registry.add(definition)
            proposal_log.append({"kind": "metric", "status": "accepted", "definition": definition})
        except (ValueError, TypeError, KeyError) as exc:
            proposal_log.append({"kind": "metric", "status": "rejected", "definition": definition, "error": str(exc)})
    if registry.definitions != state["metric_definitions"]:
        state["metric_definitions"] = registry.definitions
        for graph in state["graphs"]:
            graph["metrics"] = registry.compute(graph["edges"])
    for raw in upper["inequalities"]:
        try:
            raw = dict(raw)
            if isinstance(raw.get("coefficients"), list):
                coefficients = {}
                for term in raw["coefficients"]:
                    if term["metric"] in coefficients:
                        raise ValueError("duplicate coefficient metric")
                    coefficients[term["metric"]] = term["coefficient"]
                raw["coefficients"] = coefficients
            candidate = normalize(raw, registry)
            if candidate["id"] not in {i["id"] for i in state["inequalities"]}:
                state["inequalities"].append(candidate)
            proposal_log.append({"kind": "inequality", "status": "accepted", "id": candidate["id"]})
        except (ValueError, TypeError, KeyError) as exc:
            proposal_log.append({"kind": "inequality", "status": "rejected", "raw": raw, "error": str(exc)})
    state["inequalities"] = [evaluate(i, state["graphs"]) for i in state["inequalities"]]
    oracle_report = {"status": "not_run", "reason": "oracle disabled by configuration"}
    if config.get("exhaustive_oracle", False):
        active = [i for i in state["inequalities"] if i["status"] != "refuted"]
        oracle_report, witnesses = exhaustive_oracle(registry, active)
        for edges in witnesses:
            add_graph(state, registry, edges, {"kind": "exhaustive_counterexample", "round": index}, output)
        if oracle_report["status"] == "complete":
            for inequality in active:
                row = oracle_report["inequalities"][inequality["id"]]
                if row["applicable"] and row["max_residual"] <= 0:
                    inequality["status"] = "exhaustive_verified"
                    inequality["evidence"] = str((directory / "oracle.json").relative_to(output))
                # Empty domains are explicitly reported rather than marketed as a useful theorem.
        state["inequalities"] = [evaluate(i, state["graphs"]) for i in state["inequalities"]]
    after = freeze(state["inequalities"], state["graphs"], config["goal"], challenge_turn_index(config, index + 1), config.get("quality_band"))
    write_json(directory / "registry.json", registry.describe())
    write_json(directory / "reward_after.json", after)
    write_json(directory / "proposal_checks.json", proposal_log)
    write_json(directory / "oracle.json", oracle_report)
    write_json(directory / "inequalities.json", state["inequalities"])
    # Export precisely scoped obligations, no solver success inferred from this file.
    write_json(directory / "proof_obligations.json", {"n": registry.n, "domain": "all simple C4-free subgraphs of Q_n satisfying each inequality's own conditions",
                "metric_registry": registry.describe(), "task_goal": config["goal"],
                "obligations": [i for i in state["inequalities"] if i["status"] in ("untested", "empirical")],
                "status": "not_proved; no automatic lift to original Q8 goal"})
    summary = {"round": index, "focus": focus, "accepted_outputs": accepted, "rejected_outputs": rejected,
               "new_lower_graphs": new_count, "archive_size": len(state["graphs"]), "program_ids": programs,
               "lower_provider": lower_receipt, "upper_provider": upper_receipt,
               "active_reward_inequalities": len(after["inequalities"]),
               "refuted_inequalities": sum(i["status"] == "refuted" for i in state["inequalities"]),
               "oracle_status": oracle_report["status"]}
    state["completed_rounds"] += 1
    state["rounds"].append(summary)
    write_json(directory / "summary.json", summary)
    return state


def report(state, output):
    config = state["config"]
    snapshot = freeze(state["inequalities"], state["graphs"], config["goal"], challenge_turn_index(config, state["completed_rounds"]), config.get("quality_band"))
    scores = [(g, score(g["metrics"], snapshot, g["id"])) for g in state["graphs"]]
    eligible = [(g, s) for g, s in scores if s["eligible"]]
    best = max(eligible, key=lambda row: row[1]["objective_utility"], default=None)
    summary = {"n": config["n"], "completed_rounds": state["completed_rounds"], "backend": config["provider"]["backend"],
               "requested_model": config["provider"].get("model"), "graphs": len(state["graphs"]), "programs": len(state["programs"]),
               "goal": config["goal"], "best_eligible_graph": best[0]["id"] if best else None,
               "best_objective": best[1]["objective"] if best else None,
               "goal_reached": any(s["goal_reached"] for _, s in scores),
               "inequality_statuses": {status: sum(i["status"] == status for i in state["inequalities"]) for status in ("untested", "empirical", "refuted", "exhaustive_verified")},
               "assurance": "host-validated witnesses; empirical conjectures are not theorems; small exhaustive claims only in recorded domain"}
    proof_goal = config.get("primary_proof_goal")
    if proof_goal:
        # Inspect every legal graph, even if it misses auxiliary search conditions.
        counterexamples = [g["id"] for g in state["graphs"] if g["metrics"]["edges"] > proof_goal["upper_bound"]]
        summary.update(primary_proof_goal=proof_goal,
                       primary_proof_status="counterexample_pending_independent_verification" if counterexamples else "open",
                       primary_counterexample_ids=counterexamples,
                       adversarial_search_target=config["goal"], adversarial_target_reached=summary["goal_reached"])
    write_json(output / "summary.json", summary)
    write_json(output / "registry.json", Registry(config["n"], state["metric_definitions"]).describe())
    for graph in state["graphs"]:
        write_json(output / "graphs" / (graph["id"] + ".json"), graph)
    lines = ["# Co-evolution run", "", f"Dimension: {config['n']}; completed rounds: {state['completed_rounds']}; provider: {summary['backend']}.",
             f"Valid archived graphs: {summary['graphs']}; programs: {summary['programs']}.",
             f"Best eligible objective: {summary['best_objective']}; target reached: {summary['goal_reached']}.", "",
             "## Inequality ledger", "", "| ID | Status | Samples | Maximum residual |", "|---|---|---:|---:|"]
    lines += [f"| {i['id']} | {i['status']} | {i.get('support_count', 0)} | {i.get('max_residual')} |" for i in state["inequalities"]]
    if proof_goal:
        lines += ["", "## Primary upper-bound proof", "", proof_goal["statement"],
                  f"Proof status: {summary['primary_proof_status']}.",
                  "The construction target is adversarial. Finding no counterexample does not prove the upper bound."]
    lines += ["", "Empirical support is not proof. Refuted inequalities are excluded from subsequent rewards.",
              "Programs use a frozen reward during each round; after upper updates, all archive selection scores are recomputed.",
              "`state.json` is the recovery entry. `rounds/` retains actual prompts, sources, evaluations, and proof obligations."]
    (output / "REPORT.md").write_text("\n".join(lines) + "\n")
    return summary


def run(config_path, output, rounds, resume=False):
    if rounds < 1:
        raise ValueError("rounds must be positive (additional rounds when resuming)")
    output = Path(output).resolve()
    state_path = output / "state.json"
    if resume:
        if not state_path.exists():
            raise ValueError("--resume requires an existing state.json")
        state = json.loads(state_path.read_text())
        if config_path and load_config(config_path) != state["config"]:
            raise ValueError("resume config differs from frozen run; start a new run for changed semantics")
    else:
        if output.exists() and any(output.iterdir()):
            raise ValueError("output is nonempty; use --resume or a new path")
        if not config_path:
            raise ValueError("new run requires --config")
        output.mkdir(parents=True, exist_ok=True)
        state = initialize(load_config(config_path), output)
        write_json(state_path, state)
        report(state, output)
    for _ in range(rounds):
        try:
            candidate = run_round(copy.deepcopy(state), output)
            write_json(state_path, candidate)
            state = candidate
            summary = report(state, output)
            print(json.dumps(summary, ensure_ascii=False), flush=True)
        except BaseException as exc:
            write_json(output / "last_error.json", {"type": type(exc).__name__, "error": str(exc), "completed_rounds": state["completed_rounds"],
                       "resume": "completed state preserved; cached completed calls reused; ambiguous/failed model calls require inspection"})
            raise
    return summary
