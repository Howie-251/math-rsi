"""Export saved unit-family catalogues with explicit checked permutations.

This replays only local block extensions; it never searches layouts or whole
hypergraphs. The Lean coverage theorem independently follows actual traces.
"""
from pathlib import Path
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "context/propertyb34/round01/high-math"
sys.path.insert(0, str(SOURCE))
from unit_catalogue import canonical, fullblocks

OUT = Path(__file__).resolve().parent
FORMAL = ROOT / "formal/Aris4Math/ThirtyFour"
SIX = [[], [7], [25, 14], [49, 14], [25, 14, 50], [11, 49, 22, 44],
       [39], [57, 14], [47]]

def sets(xs):
    return "∅" if not xs else "{" + ",".join(map(str, xs)) + "}"

def trace(t, n):
    return sets([i for i in range(n) if t >> i & 1])

def family(ts, n):
    return "∅" if not ts else "{" + ",".join(trace(t, n) for t in ts) + "}"

def choices(candidates, chosen=()):
    if not candidates:
        yield chosen
        return
    first, *rest = candidates
    yield from choices(rest, chosen)
    if all(not first & t for t in chosen):
        yield from choices(rest, chosen + (first,))

def main(level):
    n = level - 1
    old = SIX if n == 6 else json.loads((SOURCE / f"UNIT_CATALOGUE_{n}.json").read_text())["orbits"]
    new = json.loads((SOURCE / f"UNIT_CATALOGUE_{level}.json").read_text())["orbits"]
    targets = {tuple(x): j for j, x in enumerate(new)}
    records = []
    start = time.monotonic()
    for parent, big in enumerate(old):
        candidates = [t for t in fullblocks(big, n) if t.bit_count() <= 4]
        certificates = []
        for chosen in choices(candidates):
            ext = [t for t in big if t not in chosen] + [t | (1 << n) for t in chosen]
            normal, permutation = canonical(ext, level, with_perm=True)
            certificates.append(dict(target=targets[normal], permutation=permutation))
        records.append(dict(parent=parent, candidates=candidates, certificates=certificates))
    result = dict(level=level, parents=len(old), targets=len(new),
                  extensions=sum(len(r["certificates"]) for r in records),
                  elapsed=time.monotonic()-start, records=records)
    (OUT / f"UNIT_EXTENSION_{level}_CERTIFICATES.json").write_text(json.dumps(result, indent=2)+"\n")
    namespace = f"TwentyFiveUnit{level}Data"
    old_expr = "Aris4Math.K6Classification.representative" if n == 6 else f"TwentyFiveUnit{n}Data.catalogue"
    imports = "import Aris4Math.ThirtyFour.TwentyFiveUnitCatalogue\n"
    if n != 6:
        imports += f"import Aris4Math.ThirtyFour.TwentyFiveUnit{n}Data\n"
    lines = [imports, f"namespace Aris4Math.ThirtyFour.{namespace}",
             "open TwentyFiveUnitExtension TwentyFiveUnitCatalogue",
             "set_option maxRecDepth 100000", "set_option maxHeartbeats 0",
             f"def catalogue : Fin {len(new)} → Finset (Finset (Fin {level})) := ![" + ",\n".join(family(z, level) for z in new)+"]",
             f"def candidates : Fin {len(old)} → List (Finset (Fin {n})) := ![" + ",\n".join("["+",".join(trace(t,n) for t in r["candidates"])+"]" for r in records)+"]"]
    for r in records:
        entries = ["⟨"+str(w["target"])+",!["+",".join(map(str,w["permutation"]))+"]⟩" for w in r["certificates"]]
        lines.append(f"def witnesses{r['parent']} : List (Witness {level} {len(new)}) := ["+",\n".join(entries)+"]")
    lines += [f"end Aris4Math.ThirtyFour.{namespace}", ""]
    (FORMAL/f"{namespace}.lean").write_text("\n".join(lines))
    # Individual checks make ordinary compilation schedulable and diagnose the
    # specific old representative if a source witness was wrong.
    checks = [f"import Aris4Math.ThirtyFour.{namespace}",
              f"namespace Aris4Math.ThirtyFour.TwentyFiveUnit{level}Checked",
              f"open TwentyFiveUnitExtension TwentyFiveUnitCatalogue {namespace}",
              "set_option maxRecDepth 100000", "set_option maxHeartbeats 0"]
    for r in records:
        i = r["parent"]
        checks.append(f"theorem checked{i} : List.Forall₂ (Checks catalogue ({old_expr} {i}))\n  (choices (candidates {i}) ∅) witnesses{i} := by decide +kernel")
    checks += [f"end Aris4Math.ThirtyFour.TwentyFiveUnit{level}Checked", ""]
    (FORMAL/f"TwentyFiveUnit{level}Checked.lean").write_text("\n".join(checks))
    actual = [f"import Aris4Math.ThirtyFour.TwentyFiveUnit{level}Checked"]
    if n != 6:
        actual += [f"import Aris4Math.ThirtyFour.TwentyFiveUnit{n}Actual"]
    actual += [f"namespace Aris4Math.ThirtyFour.TwentyFiveUnit{level}Actual",
               f"open TwentyFiveUnitExtension TwentyFiveUnitCatalogue {namespace} TwentyFiveUnit{level}Checked",
               "set_option maxRecDepth 100000", "set_option maxHeartbeats 0",
               f"theorem candidates_eq : ∀ c, (candidates c).toFinset =\n  (Aris4Math.K6Classification.pairCompletion ({old_expr} c)).filter (fun T => T.card≤4) := by decide +kernel",
               f"theorem candidates_complete (c : Fin {len(old)}) (T : Finset (Fin {n}))\n    (mem : T ∈ Aris4Math.K6Classification.pairCompletion ({old_expr} c)) (small : T.card≤4) :\n    T∈candidates c := by\n  apply List.mem_toFinset.mp\n  rw [candidates_eq]\n  exact Finset.mem_filter.mpr ⟨mem,small⟩",
               f"theorem local_coverage (c : Fin {len(old)}) (chosen : Finset (Finset (Fin {n})))\n  (mem : chosen ∈ choices (candidates c) ∅) :\n  ∃ d : Fin {len(new)}, ∃ σ : Equiv.Perm (Fin {level}),\n    (extend ({old_expr} c) chosen).image (fun T => T.map σ.toEmbedding)=catalogue d := by\n  fin_cases c"]
    for r in records:
        i = r["parent"]
        actual += [f"  · exact checked_choice catalogue ({old_expr} {i}) _ witnesses{i} checked{i} chosen mem"]
    previous = "six_covers" if n == 6 else f"TwentyFiveUnit{n}Actual.actual"
    actual += [f"theorem actual : Covers catalogue :=\n  covers_succ {old_expr} catalogue candidates {previous} candidates_complete local_coverage",
               f"end Aris4Math.ThirtyFour.TwentyFiveUnit{level}Actual",
               f"#print axioms Aris4Math.ThirtyFour.TwentyFiveUnit{level}Actual.actual", ""]
    (FORMAL/f"TwentyFiveUnit{level}Actual.lean").write_text("\n".join(actual))
    print(json.dumps({k: v for k, v in result.items() if k != "records"}))

if __name__ == "__main__":
    main(int(sys.argv[1]))
