import json
import os
from datetime import datetime, timezone
from pathlib import Path

try:
    import fire
except ImportError:
    fire = None
import lib.erdos as erdos
import itertools
from lib.util import binom
from pipeline_utils import manifest_case_identity

def subsets(n, k):
    return itertools.combinations(list(range(n)), k)

def parse_truth_token(tok: str) -> bool:
    tok = tok.strip().upper()
    if tok in {"1", "T", "TRUE", "+", "POS", "YES"}:
        return True
    if tok in {"0", "F", "FALSE", "-", "NEG", "NO"}:
        return False
    raise ValueError(f"Unknown truth token: {tok}")


def parse_assumption_literals(inst, assume_file):
    """
    Supported assumption file formats:

    1) Old triple-color format:
         i j k R
         i j k B

    2) New symbolic format:
         split_end r T/F
         cap i j d T/F
         cup i j d T/F

    All indices in files are 1-based.
    Blank lines and lines starting with '#' are ignored.
    """
    lits = []

    with open(assume_file, "r") as f:
        lines = f.readlines()

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split()

        # --------------------------------------------------
        # Old format: i j k R/B
        # --------------------------------------------------
        if (
            len(parts) == 4
            and parts[0].isdigit()
            and parts[1].isdigit()
            and parts[2].isdigit()
            and parts[3].upper() in {"R", "B"}
        ):
            i, j, k = int(parts[0]) - 1, int(parts[1]) - 1, int(parts[2]) - 1
            color = parts[3].upper()
            var = inst.v[(i, j, k)]
            lits.append(var._lit if color == "R" else -var._lit)
            continue

        # --------------------------------------------------
        # split_end r T/F
        # --------------------------------------------------
        if parts[0].lower() == "split_end":
            if len(parts) != 3:
                raise ValueError(f"Bad split_end assumption line: {line}")
            if not hasattr(inst, "split_end"):
                raise ValueError(
                    "This instance has no split_end variables. "
                    "Use order=signotope_split or signotope_knuth_split."
                )
            r = int(parts[1]) - 1
            val = parse_truth_token(parts[2])
            var = inst.split_end[r]
            lits.append(var._lit if val else -var._lit)
            continue

        # --------------------------------------------------
        # cap i j d T/F
        # --------------------------------------------------
        if parts[0].lower() == "cap":
            if len(parts) != 5:
                raise ValueError(f"Bad cap assumption line: {line}")
            i = int(parts[1]) - 1
            j = int(parts[2]) - 1
            d = int(parts[3])
            val = parse_truth_token(parts[4])
            var = inst.cap[(i, j, d)]
            lits.append(var._lit if val else -var._lit)
            continue

        # --------------------------------------------------
        # cup i j d T/F
        # --------------------------------------------------
        if parts[0].lower() == "cup":
            if len(parts) != 5:
                raise ValueError(f"Bad cup assumption line: {line}")
            i = int(parts[1]) - 1
            j = int(parts[2]) - 1
            d = int(parts[3])
            val = parse_truth_token(parts[4])
            var = inst.cup[(i, j, d)]
            lits.append(var._lit if val else -var._lit)
            continue

        if parts[0].lower() == "split_pair":
            if len(parts) != 5:
                raise ValueError(f"Bad split_pair assumption line: {line}")
            if not hasattr(inst, "split_pair"):
                raise ValueError(
                    "This instance has no split_pair variables. "
                    "Use order=signotope_split or signotope_knuth_split."
                )
            r = int(parts[1]) - 1
            d = int(parts[2])
            e = int(parts[3])
            val = parse_truth_token(parts[4])
            var = inst.split_pair[(r, d, e)]
            lits.append(var._lit if val else -var._lit)
            continue

        if parts[0].lower() == "split_cap_exists":
            if len(parts) != 4:
                raise ValueError(f"Bad split_cap_exists assumption line: {line}")
            if not hasattr(inst, "split_cap_exists"):
                raise ValueError(
                    "This instance has no split_cap_exists variables. "
                    "Use order=signotope_split or signotope_knuth_split."
                )
            r = int(parts[1]) - 1
            d = int(parts[2])
            val = parse_truth_token(parts[3])
            var = inst.split_cap_exists[(r, d)]
            lits.append(var._lit if val else -var._lit)
            continue

        if parts[0].lower() == "split_cup_exists":
            if len(parts) != 4:
                raise ValueError(f"Bad split_cup_exists assumption line: {line}")
            if not hasattr(inst, "split_cup_exists"):
                raise ValueError(
                    "This instance has no split_cup_exists variables. "
                    "Use order=signotope_split or signotope_knuth_split."
                )
            r = int(parts[1]) - 1
            e = int(parts[2])
            val = parse_truth_token(parts[3])
            var = inst.split_cup_exists[(r, e)]
            lits.append(var._lit if val else -var._lit)
            continue

        raise ValueError(f"Unrecognized assumption line: {line}")

    return lits


def parse_assumption_metadata(assume_file):
    records = []
    split_info = {
        "type": "coarse",
        "does_not_fix_internal_vertices": True,
        "right_endpoint": None,
        "cap_size": None,
        "cup_size": None,
        "cap_min_left_position": None,
        "cup_min_left_position": None,
        "cap_path": None,
        "cup_path": None,
        "cap_triple_color": None,
        "cup_triple_color": None,
        "notes": "Only right endpoint and minimum left endpoint positions are constrained.",
    }

    with open(assume_file, "r") as f:
        lines = f.readlines()

    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            comment = line[1:].strip()
            parts = comment.split()
            if parts and parts[0] in {"exact_cap_path", "exact_cup_path"}:
                path = []
                color = None
                for part in parts[1:]:
                    if part.startswith("color="):
                        color = part.split("=", 1)[1].lower()
                    else:
                        path.append(int(part))
                atom = "exact_cap_path" if parts[0] == "exact_cap_path" else "exact_cup_path"
                records.append({"text": line, "semantic": {"atom": atom, "path": path, "color": color}})
                split_info["type"] = "exact_witness"
                split_info["does_not_fix_internal_vertices"] = False
                split_info["notes"] = "Concrete split witness path triples are fixed in the assumption file."
                if atom == "exact_cap_path":
                    split_info["cap_path"] = path
                    split_info["cap_triple_color"] = color
                    split_info["cap_size"] = len(path)
                    if path:
                        split_info["cap_min_left_position"] = path[0]
                        split_info["right_endpoint"] = path[-1]
                else:
                    split_info["cup_path"] = path
                    split_info["cup_triple_color"] = color
                    split_info["cup_size"] = len(path)
                    if path:
                        split_info["cup_min_left_position"] = path[0]
                        split_info["right_endpoint"] = path[-1]
            continue
        parts = line.split()
        head = parts[0].lower()

        if len(parts) == 4 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit() and parts[3].upper() in {"R", "B"}:
            triple = [int(parts[0]), int(parts[1]), int(parts[2])]
            color = "red" if parts[3].upper() == "R" else "blue"
            records.append({"text": line, "semantic": {"atom": "triple", "triple": triple, "color": color}})
            continue

        if head == "split_end":
            r = int(parts[1])
            value = parse_truth_token(parts[2])
            semantic = {"atom": "split_end", "right_endpoint": r, "value": value}
            records.append({"text": line, "semantic": semantic})
            if value:
                split_info["right_endpoint"] = r
            continue

        if head == "split_pair":
            r = int(parts[1])
            d = int(parts[2])
            e = int(parts[3])
            value = parse_truth_token(parts[4])
            semantic = {"atom": "split_pair", "right_endpoint": r, "cap_size": d, "cup_size": e, "value": value}
            records.append({"text": line, "semantic": semantic})
            if value:
                split_info["right_endpoint"] = r
                split_info["cap_size"] = d
                split_info["cup_size"] = e
            continue

        if head == "cap":
            i = int(parts[1])
            j = int(parts[2])
            d = int(parts[3])
            value = parse_truth_token(parts[4])
            semantic = {"atom": "cap", "left_endpoint": i, "right_endpoint": j, "cap_size": d, "value": value}
            records.append({"text": line, "semantic": semantic})
            if value:
                split_info["right_endpoint"] = j
                split_info["cap_size"] = d
                split_info["cap_min_left_position"] = i
            continue

        if head == "cup":
            i = int(parts[1])
            j = int(parts[2])
            d = int(parts[3])
            value = parse_truth_token(parts[4])
            semantic = {"atom": "cup", "left_endpoint": i, "right_endpoint": j, "cup_size": d, "value": value}
            records.append({"text": line, "semantic": semantic})
            if value:
                split_info["right_endpoint"] = j
                split_info["cup_size"] = d
                split_info["cup_min_left_position"] = i
            continue

        if head == "split_cap_exists":
            r = int(parts[1])
            d = int(parts[2])
            value = parse_truth_token(parts[3])
            records.append({"text": line, "semantic": {"atom": "split_cap_exists", "right_endpoint": r, "cap_size": d, "value": value}})
            continue

        if head == "split_cup_exists":
            r = int(parts[1])
            e = int(parts[2])
            value = parse_truth_token(parts[3])
            records.append({"text": line, "semantic": {"atom": "split_cup_exists", "right_endpoint": r, "cup_size": e, "value": value}})
            continue

        records.append({"text": line, "semantic": {"atom": "raw", "tokens": parts}})

    return {"cube_assumptions": records, "split_partition": split_info}


def apply_assumptions(inst, assume_file, group="cube_assumption"):
    for lit in parse_assumption_literals(inst, assume_file):
        inst.add_clause([lit], group=group)

etv = {
    "": erdos.etv,
    "signotope": erdos.etv_signotope,
    "ax4": erdos.etv_ax4,
    "ax4_interior": erdos.etv_ax4_interior,
    "ax5": erdos.etv_ax5,
    "semisimple": erdos.etv_semisimple,
    "restrict": erdos.etv_signotope,
    "endpoint_query_a": erdos.etv_signotope_extension,
    "endpoint_query_b": erdos.etv_signotope_extension_desync,
    "signotope_split": erdos.etv_signotope_split,
    "signotope_knuth_split": erdos.etv_signotope_knuth_split,
    "signotope_knuth": erdos.etv_signotope_knuth,
}

def main(
    n,
    a,
    b,
    N,
    filename=None,
    order="",
    assume_file=None,
    solver="kissat",
    lemma_dir=None,
    random_seed=None,
    generate_only=False,
):
    inst = etv[order](n, a, b, N)
    if not filename:
        filename = f"res/etv_{n}_{a}_{b}_{N}_{order}"
    assumption_meta = {"cube_assumptions": [], "split_partition": None}
    if order == "restrict":
        v = inst.v
        for i, j, k, l in subsets(N, 4):
            p = v[(i, j, k)]
            q = v[(i, j, l)]
            r = v[(i, k, l)]
            s = v[(j, k, l)]
            inst.add_implies(p & q & ~s, r)
    if lemma_dir:
        from lib.lemma import add_lifted_lemmas, load_verified_lemmas_from_dir

        wrappers = load_verified_lemmas_from_dir(lemma_dir)
        inst.set_clause_group("lemma")
        stats = add_lifted_lemmas(inst, N, wrappers, verbose=True, global_order=order)
        print(
            f"[LEMMA] added {stats['clauses_added']} lifted lemma clauses "
            f"from {stats['lemmas']} verified lemmas"
        )
    if assume_file:
        assumption_meta = parse_assumption_metadata(assume_file)
        assumption_group = (
            "fixed_base_model"
            if order in {"endpoint_query_a", "endpoint_query_b"}
            else "cube_assumption"
        )
        apply_assumptions(inst, assume_file, group=assumption_group)

    run_identity = manifest_case_identity(
        assume_file,
        n=n,
        a=a,
        b=b,
        N=N,
        order=order,
        lemma_dir=lemma_dir,
    )

    base_formula_sha256 = None
    inst.set_metadata(
        generator_version="ai-pipeline-mvp-1",
        order=order,
        solver=solver,
        filename=filename,
        assume_file=assume_file,
        lemma_dir=lemma_dir,
        random_seed=random_seed,
        generate_only=bool(generate_only),
        run_identity=run_identity,
        created_at=datetime.now(timezone.utc).isoformat(),
        problem={"n": n, "a": a, "b": b, "N": N, "order": order},
    )

    cnf_path = Path(f"{filename}.cnf")
    meta_path = Path(f"{filename}.meta.json")
    out_path = Path(f"{filename}.out")
    extra_meta = {
        "cube_assumptions": assumption_meta["cube_assumptions"],
        "split_partition": assumption_meta["split_partition"],
        "solver_command": None,
        "output_paths": {
            "cnf": str(cnf_path),
            "out": str(out_path),
            "meta": str(meta_path),
        },
    }

    inst.write(str(cnf_path))
    if cnf_path.exists():
        import hashlib

        base_formula_sha256 = hashlib.sha256(cnf_path.read_bytes()).hexdigest()
        extra_meta["base_formula_sha256"] = base_formula_sha256
    inst.write_metadata(str(meta_path), cnf_path=str(cnf_path), extra=extra_meta)

    if generate_only:
        print(f"CNF and metadata generated: {cnf_path}, {meta_path}")
        return

    status_path = Path(f"{filename}.status.json")
    if status_path.exists():
        status_path.unlink()
    try:
        successful = inst.solve(filename, solver=solver)
    except Exception as exc:
        status_payload = {
            "schema": "solver_status_v1",
            "status": "ERROR",
            "solver": solver,
            "run_identity": run_identity,
            "error": f"{type(exc).__name__}: {exc}",
            "output_paths": {
                "cnf": str(cnf_path),
                "meta": str(meta_path),
                "status": str(status_path),
            },
        }
        with open(status_path, "w", encoding="utf-8") as f:
            json.dump(status_payload, f, indent=2, sort_keys=True)
            f.write("\n")
        raise

    solver_result_getter = getattr(inst, "last_solver_result", None)
    solver_result = solver_result_getter() if callable(solver_result_getter) else None
    if not isinstance(solver_result, dict):
        solver_result = {
            "schema": "solver_status_v1",
            "status": "SAT" if successful else "UNSAT",
            "solver": solver,
            "legacy_status_fallback": True,
        }
    status = solver_result.get("status")
    solver_result["run_identity"] = run_identity
    solver_result["output_paths"] = {
        "cnf": str(cnf_path),
        "meta": str(meta_path),
        "status": str(status_path),
        "color": f"{filename}.color" if status == "SAT" else None,
    }

    if status == "SAT" and successful:
        print("Solution found")
        sol_filename = filename + ".color"
        with open(sol_filename, "w") as f:
            for triple, var in inst.v.items():
                color = 'R' if var.solution() else 'B'
                line = f"{triple[0]+1} {triple[1]+1} {triple[2]+1} {color}"
                f.write(line + "\n")
        print("Solution stored in " + sol_filename)
    elif status == "UNSAT":
        print("Solution not found")
    else:
        print(f"Solver failed with status {status or 'ERROR'}")

    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(solver_result, f, indent=2, sort_keys=True)
        f.write("\n")

    if status not in {"SAT", "UNSAT"}:
        raise SystemExit(2)

if __name__ == '__main__':
    if fire is not None:
        fire.Fire(main)
    else:
        import argparse

        parser = argparse.ArgumentParser()
        parser.add_argument("n", type=int)
        parser.add_argument("a", type=int)
        parser.add_argument("b", type=int)
        parser.add_argument("N", type=int)
        parser.add_argument("--filename")
        parser.add_argument("--order", default="")
        parser.add_argument("--assume_file")
        parser.add_argument("--solver", default="kissat")
        parser.add_argument("--lemma_dir")
        parser.add_argument("--random_seed")
        parser.add_argument(
            "--generate_only",
            action="store_true",
            help="Write CNF and metadata, then exit without running the SAT solver.",
        )
        args = parser.parse_args()
        main(
            args.n,
            args.a,
            args.b,
            args.N,
            filename=args.filename,
            order=args.order,
            assume_file=args.assume_file,
            solver=args.solver,
            lemma_dir=args.lemma_dir,
            random_seed=args.random_seed,
            generate_only=args.generate_only,
        )
