"""Split unchanged six-low extra-point row certificates into bounded kernel checks.

No mathematical domain or certificate is changed. The aggregate checks the
enumerator against the concatenation of all row inputs exactly once.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
OUT = ROOT / "formal/Aris4Math/ThirtyFour"
BASE = "TwentyThreeSixLowExtraCatalogue"
NS = "Aris4Math.ThirtyFour." + BASE
BLOCK = 8

def write(path, text):
    if not path.exists() or path.read_text() != text:
        path.write_text(text)

manifest = []
summary = []
for case in [0,6]:
    pattern = "none" if case==6 else f"(some {case})"
    source = OUT / f"{BASE}Coverage{case}.lean"
    snapshot = HERE / f"SixExtraCoverage{case}Unsplit.lean"
    raw = source.read_text()
    if f"def rows{case} : List" in raw and "\n([" in raw:
        write(snapshot, raw)
    else:
        raw = snapshot.read_text()
    entries = raw.split(f"def rows{case} : List (List ℕ × (Degree → Witness)) := [\n", 1)[1].split("\n]\n", 1)[0].splitlines()
    entries = [line.rstrip(",") for line in entries]
    blocks = [entries[i:i+BLOCK] for i in range(0, len(entries), BLOCK)]
    names = []
    for b, rows in enumerate(blocks):
        module = f"{BASE}Coverage{case}Block{b}"
        name = f"rows{case}_{b}"
        names.append(name)
        header = f"import Aris4Math.ThirtyFour.{BASE}Data\nnamespace {NS}\nset_option maxHeartbeats 0\nset_option maxRecDepth 100000\n"
        text = header + f"def {name} : List (List ℕ × (Degree → Witness)) := [\n" + ",\n".join(rows) + "\n]\n"
        text += f"theorem {name}_checked : {name}.all (fun row => decide (∀ d : Degree, Matched d {pattern} row.1 (row.2 d)))=true := by decide +kernel\nend {NS}\n"
        write(OUT / f"{module}.lean", text)
        manifest.append("Aris4Math.ThirtyFour." + module)
    text = "".join(f"import Aris4Math.ThirtyFour.{BASE}Coverage{case}Block{b}\n" for b in range(len(blocks)))
    text += f"namespace {NS}\nset_option maxHeartbeats 0\nset_option maxRecDepth 100000\n"
    text += f"def rows{case} : List (List ℕ × (Degree → Witness)) := " + " ++ ".join(names) + "\n"
    text += f"theorem catalogue_eq{case} : catalogue {pattern}=rows{case}.map Prod.fst := by decide +kernel\n"
    text += f"theorem rows_checked{case} : rows{case}.all (fun row => decide (∀ d : Degree, Matched d {pattern} row.1 (row.2 d)))=true := by\n"
    text += f"  simp only [rows{case},List.all_append," + ",".join(name+"_checked" for name in names) + ",Bool.true_and]\n"
    text += raw[raw.index(f"theorem coverage{case} ("):]
    write(source, text)
    manifest.append("Aris4Math.ThirtyFour." + BASE + f"Coverage{case}")
    summary.append(dict(case=case, rows=len(entries), block_size=BLOCK, blocks=len(blocks)))

manifest += ["Aris4Math.ThirtyFour." + s for s in [
    BASE+"Numeric", BASE, "TwentyThreeSixLowExtraChecked", "TwentyThreeExactlySixLowComplete"]]
write(HERE / "SIX_EXTRA_COVERAGE_SERIAL_MANIFEST.txt", "\n".join(manifest)+"\n")
write(HERE / "SIX_EXTRA_COVERAGE_BLOCKS.json", json.dumps(summary, indent=2)+"\n")
print(summary)
