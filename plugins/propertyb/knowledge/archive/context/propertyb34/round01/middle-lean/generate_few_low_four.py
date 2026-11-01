"""Export the strict four-lock representatives with their actual-count callers.

The source representative labels and positions are retained. No permutation of
the mixed low/high degree classes is introduced by this exporter.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import argparse
import json
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
OUT = ROOT / "formal/Aris4Math/ThirtyFour"
sys.path[:0] = [str(ROOT / "computations"),
               str(ROOT / "computations/propertyb33/round01"),
               str(ROOT / "context/propertyb34/round01/twentyone-math")]
from multilock import Profile, pair_weight, rows, total_bound, json_value
from pure_quota import certificate
from independent_structure_bounds import independent_rows
from verify_joint import verify

vec = lambda xs: "![" + ",".join(map(str, xs)) + "]"
rat = lambda x: f"({F(x).numerator}/{F(x).denominator})"
fs = lambda m: "{" + ",".join(str(j) for j in range(4) if m >> j & 1) + "}" if m else "∅"


def write(name, text):
    (OUT / (name + ".lean")).write_text(text)


def mu(ns):
    return "fun T => " + "".join(f"if T={fs(t)} then {k} else " for t, k in sorted(ns.items())) + "0"


def computed(ns, pos):
    ts = ["⟨[" + ",".join(map(str, sorted(pos[j] for j in range(4) if t >> j & 1))) + f"],{k}⟩"
          for t, k in sorted(ns.items())]
    return "⟨23,[" + ",".join(map(str, sorted(pos))) + "],[" + ",".join(ts) + "],none,[" + ",".join(map(str, pos)) + "]⟩"


def labels():
    return f"""def labels : List (Finset (Fin 4)) := [{','.join(fs(t) for t in range(16))}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
"""


def pure_record(r, degrees):
    ns = {int(t): k for t, k in r["counts"].items() if k}
    pos = tuple(r["positions"])
    p = Profile(23, 5, pos, ns)
    cs = [certificate(p, i) for i in range(4)]
    raw_rows = rows(p, deductions={pos[i]: cs[i]["loss"] for i in range(4)})
    stubs = [frozenset(i + 1 for i in range(4) if t >> i & 1) for t, k in ns.items() for _ in range(k)]
    independent = independent_rows(23, pos, stubs)
    assert all(a[key] == b[key] for a, b in zip(raw_rows, independent) for key in ("A", "B", "C"))
    assert total_bound(raw_rows) == F(r["bound"]) < 1
    assert sum(ns.values()) == 34
    assert [sum(k for t, k in ns.items() if t >> i & 1) for i in range(4)] == degrees
    duals, losses = [], []
    for j, c in enumerate(cs):
        bit, k = 1 << j, pos[j]
        types = sorted(t for t in ns if t & bit)
        inv = []
        for ii, t in enumerate(types):
            for u in types[ii:]:
                cap = ns[t] * (ns[t] - 1) // 2 if t == u else ns[t] * ns[u]
                if cap:
                    inv.append((pair_weight(23, 5, pos, t, u, k) + pair_weight(23, 5, pos, u, t, k), cap, t, u))
        wp = 2 * pair_weight(23, 5, pos, bit, bit, k)
        best = None
        for a in sorted({F(0), wp, *(w for w, _, _, _ in inv)}):
            b = max(F(0), wp - a)
            value = c["q_total"] * a + c["q_pure"] * b - sum(
                cap * max(F(0), a + (b if t == u == bit else 0) - w) for w, cap, t, u in inv)
            if best is None or value > best[0]:
                best = value, a, b
        dual = [(0, best[1], c["q_total"]), (15 ^ bit, best[2], c["q_pure"])]
        value = sum(a * q for R, a, q in dual) - sum(
            cap * max(F(0), sum(a for R, a, q in dual if not (t | u) & R) - w)
            for w, cap, t, u in inv)
        assert value >= c["loss"]
        for R, a, q in dual:
            available = sum(k for t, k in ns.items() if t & bit and not t & R)
            assert a >= 0 and not R & bit and q <= max(0, (4 * available + 2 - (22 - R.bit_count())) // 3)
        duals.append(dual)
        losses.append(value)
    bound = total_bound(rows(p, deductions=dict(zip(pos, losses))))
    assert bound < 1
    return dict(source_group=r["group"], counts=ns, pos=pos, dual=duals, loss=losses,
                bound=bound, original_bound=F(r["bound"]), independent_ABC=True,
                co=[sum(k for t, k in ns.items() if t & mask == mask)
                    for mask in (sum(1 << i for i in pair) for pair in combinations(range(4), 2))],
                high=[ns.get(t, 0) for t in (7, 11, 13, 14, 15)])


def export_pure(name, source_rows, degrees):
    data = [pure_record(r, degrees) for r in source_rows]
    s = f"""import Aris4Math.ThirtyFour.SingleLayoutApplication
namespace Aris4Math.ThirtyFour.{name}Data
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles
open scoped BigOperators
set_option maxRecDepth 100000
abbrev Case := Fin {len(data)}
abbrev Quota := Fin 2
def degree : Fin 4 → ℕ := {vec(degrees)}
def sourceGroup : Case → ℕ := {vec(d['source_group'] for d in data)}
""" + labels()
    s += 'def μ : Case → Finset (Fin 4) → ℕ := ' + vec(mu(d['counts']) for d in data) + '\n'
    s += 'def co : Case → Fin 6 → ℕ := ' + vec(vec(d['co']) for d in data) + '\n'
    s += 'def high : Case → Fin 5 → ℕ := ' + vec(vec(d['high']) for d in data) + '\n'
    s += 'def positionFn : Case → Fin 4 → Fin 23 := ' + vec(vec(k - 1 for k in d['pos']) for d in data) + '\n'
    s += """theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel
def positions (i : Case) : Fin 4 ↪ Fin 23 := ⟨positionFn i,positionFn_injective i⟩
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨23,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i=profile labels (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
"""
    s += 'def computed : Case → Numeric.Profile := ' + vec(computed(d['counts'], d['pos']) for d in data) + '\n'
    s += 'set_option maxHeartbeats 0 in\ntheorem p_eq_computed (i : Case) : p i=computed i := by fin_cases i <;> rfl\n'
    s += 'def loss : Case → Fin 4 → ℚ := ' + vec(vec(rat(q) for q in d['loss']) for d in data) + '\n'
    for var, typ, index, fmt in [('R', 'Finset (Fin 4)', 0, fs), ('α', 'ℚ', 1, rat), ('quota', 'ℕ', 2, str)]:
        s += f'def {var} : Case → Fin 4 → Quota → {typ} := ' + vec(vec(vec(fmt(q[index]) for q in row) for row in d['dual']) for d in data) + '\n'
    s += f"""set_option maxHeartbeats 0 in
theorem μ_eq_recovered : ∀ i T, μ i T=Aris4Math.ThirtyThree.QuadProfiles.recovered 34 degree (co i) (high i) T := by decide +kernel
end Aris4Math.ThirtyFour.{name}Data
"""
    write(name + 'Data', s)
    write(name + 'Numeric', f"""import Aris4Math.ThirtyFour.{name}Data
namespace Aris4Math.ThirtyFour.{name}Numeric
open scoped BigOperators
open {name}Data
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option synthInstance.maxSize 2000
theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧ (p i).emptyPairCap=none ∧
    (∀ j, (positions i j).val+1∈(p i).correctionCenters) ∧
    (∀ j z, 0≤α i j z) ∧ (∀ j z, j∉R i j z) ∧
    (∀ j z, quota i j z ≤
      (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (R i j z))+2-
        (23-1-(R i j z).card))/3) ∧
    (∀ j, loss i j ≤ (∑ z, (quota i j z : ℚ)*α i j z)-
      penaltySum (p i) ((positions i j).val+1) (fun z => avoidedPositions (positions i) (R i j z)) (α i j)) ∧
    (∑ k : Fin 23, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))))<1 := by
  intro i
  fin_cases i <;> simp only [p_eq_computed] <;> unfold Numeric.validProfile <;> decide +kernel
end Aris4Math.ThirtyFour.{name}Numeric
#print axioms Aris4Math.ThirtyFour.{name}Numeric.certificates
""")
    write(name, f"""import Aris4Math.ThirtyFour.{name}Numeric
namespace Aris4Math.ThirtyFour.{name}
open {name}Data {name}Numeric
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 4 ↪ Fin 23)
    (i : Case) (counts : ∀ T, count H vertices T=μ i T) : PropertyB H := by
  obtain ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,strict⟩ := certificates i
  have real : Aris4Math.TypeCounting.RealizesProfile H vertices (positions i) (p i) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions i) labels labels_nodup mem_labels (μ i) counts
    rw [← p_eq]; exact valid
  exact SingleLayoutApplication.propertyB_of_single_layout H vertices (positions i) (p i) real
    nocap centers (R i) (α i) (quota i) (loss i) nonneg avoids quotas deduction strict
theorem propertyB_of_data (H : Simple5Hypergraph (Fin 23)) (size : H.edges.card=34)
    (vertices : Fin 4 ↪ Fin 23) (i : Case)
    (hd : ∀ j, H.degree (vertices j)=degree j)
    (hc : ∀ j, H.codegree (vertices (Aris4Math.ThirtyThree.QuadProfiles.first j))
      (vertices (Aris4Math.ThirtyThree.QuadProfiles.second j))=co i j)
    (ht : ∀ j, count H vertices (Aris4Math.ThirtyThree.QuadProfiles.highLabels j)=high i j) : PropertyB H := by
  apply propertyB_of_counts H vertices i
  intro T
  rw [μ_eq_recovered]
  change Aris4Math.ThirtyThree.QuadProfiles.count H vertices T=_
  rw [Aris4Math.ThirtyThree.QuadProfiles.actual_recovered,size]
  rw [show (fun j=>H.degree (vertices j))=degree from funext hd,
    show (fun j=>H.codegree (vertices (Aris4Math.ThirtyThree.QuadProfiles.first j))
      (vertices (Aris4Math.ThirtyThree.QuadProfiles.second j)))=co i from funext hc,
    show (fun j=>Aris4Math.ThirtyThree.QuadProfiles.count H vertices (Aris4Math.ThirtyThree.QuadProfiles.highLabels j))=high i from funext ht]
end Aris4Math.ThirtyFour.{name}
#print axioms Aris4Math.ThirtyFour.{name}.propertyB_of_counts
#print axioms Aris4Math.ThirtyFour.{name}.propertyB_of_data
""")
    return data


def export_joint(name, r, degrees):
    x = r['joint']
    assert x['group'] == r['group'] and x['counts'] == r['counts']
    checked = verify(x, v=23, ds=degrees)
    ns = {int(t): k for t, k in x['counts'].items() if k}
    layouts = x['layouts']
    Q = max(sum(q['center'] == i for q in x['quotas']) for i in range(4))
    quotas = []
    for i in range(4):
        qs = [q for q in x['quotas'] if q['center'] == i]
        assert all('kind' not in q for q in qs)
        quotas.append(qs + [dict(avoid=0, delta='0', q=0)] * (Q - len(qs)))
    s = f"""import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.{name}Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin {len(layouts)}
abbrev Quota := Fin {Q}
def sourceGroup : ℕ := {r['group']}
""" + labels()
    s += 'def μ : Finset (Fin 4) → ℕ := ' + mu(ns) + '\n'
    s += 'def support : Finset (Finset (Fin 4)) := {' + ','.join(fs(t) for t in sorted(ns)) + '}\n'
    s += 'def positionFn : Layout → Fin 4 → Fin 23 := ' + vec(vec(k - 1 for k in z['positions']) for z in layouts) + '\n'
    s += """theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 4 ↪ Fin 23 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨23,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
"""
    s += 'def computed : Layout → Numeric.Profile := ' + vec(computed(ns, z['positions']) for z in layouts) + '\n'
    s += 'theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl\n'
    s += 'def gamma : Layout → ℚ := ' + vec(rat(z['probability']) for z in layouts) + '\n'
    s += 'def beta : Layout → Fin 4 → ℚ := ' + vec(vec(rat(b) for b in z['betas']) for z in layouts) + '\n'
    s += 'def R : Fin 4 → Quota → Finset (Fin 4) := ' + vec(vec(fs(q['avoid']) for q in row) for row in quotas) + '\n'
    s += 'def delta : Fin 4 → Quota → ℚ := ' + vec(vec(rat(q['delta']) for q in row) for row in quotas) + '\n'
    s += 'def quota : Fin 4 → Quota → ℕ := ' + vec(vec(q['q'] for q in row) for row in quotas) + '\n'
    s += f'end Aris4Math.ThirtyFour.{name}Data\n'
    write(name + 'Data', s)
    write(name + 'Numeric', f"""import Aris4Math.ThirtyFour.{name}Data
namespace Aris4Math.ThirtyFour.{name}Numeric
open scoped BigOperators
open {name}Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option synthInstance.maxSize 2000
theorem data_valid :
    (∀ T, 0<μ T → T ∈ support) ∧
    (∀ l, Numeric.validProfile (p l) 34) ∧
    (∀ l, (p l).emptyPairCap=none) ∧
    (∀ l j, (positions l j).val+1 ∈ (p l).correctionCenters) ∧
    (∀ l, 0 ≤ gamma l) ∧ (∑ l, gamma l)=1 ∧
    (∀ l j, 0 ≤ beta l j) ∧ (∀ l j, beta l j ≤ gamma l) ∧
    (∀ j q, 0 ≤ delta j q) ∧ (∀ j q, j ∉ R j q) ∧
    (∀ j q, quota j q ≤ (4*available support μ j (R j q)+2-(23-1-(R j q).card))/3) := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem strict :
    (∑ l, gamma l*free (positions l) (p l)) +
    (∑ l, ∑ j, ((gamma l-beta l j)*a positions p l j+beta l j*c positions p l j)) -
    (∑ j, ((∑ q, (quota j q : ℚ)*delta j q)-
      penalty support μ beta (weights positions p) j (R j) (delta j))) < 1 := by
  simp only [LocalProfiles.weights_eq,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.{name}Numeric
#print axioms Aris4Math.ThirtyFour.{name}Numeric.strict
""")
    write(name, f"""import Aris4Math.ThirtyFour.{name}Numeric
namespace Aris4Math.ThirtyFour.{name}
open {name}Data {name}Numeric
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 4 ↪ Fin 23)
    (counts : ∀ T, count H vertices T=μ T) : PropertyB H := by
  obtain ⟨covers,valid,nocap,centers,gn,mass,bn,bg,dn,avoids,quota_valid⟩ := data_valid
  have real (l) : Aris4Math.TypeCounting.RealizesProfile H vertices (positions l) (p l) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions l) labels labels_nodup mem_labels μ counts
    rw [← p_eq]
    exact valid l
  exact MixedLayoutApplication.propertyB_of_mixed_layouts H vertices support μ counts covers
    positions p real nocap centers gamma beta R delta quota gn mass bn bg dn avoids quota_valid strict
end Aris4Math.ThirtyFour.{name}
#print axioms Aris4Math.ThirtyFour.{name}.propertyB_of_counts
""")
    return dict(module=name, **checked)


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--pilot', action='store_true')
    mode.add_argument('--all', action='store_true')
    args = parser.parse_args()
    summary = dict(mode='pilot' if args.pilot else 'all', pure=[], joint=[], residual=[])
    for suffix, source in [('OneLow', 'FEW_LOW23_1_3'), ('TwoLow', 'FEW_LOW23_2_2')]:
        raw = json.loads((ROOT / f'context/propertyb34/round01/middle-math/{source}.json').read_text())
        ps = [r for r in raw['results'] if F(r['bound']) < 1]
        js = [r for r in raw['results'] if F(r['bound']) >= 1 and F(r['final_bound']) < 1]
        residual = [r['group'] for r in raw['results'] if F(r['final_bound']) >= 1]
        assert len(ps) + len(js) + len(residual) == raw['groups']
        summary['residual'].append(dict(source=source, groups=residual))
        if args.pilot and suffix != 'OneLow':
            continue
        if args.pilot:
            ps, js = ps[:1], js[:1]
        name = f'TwentyThree{suffix}Four'
        data = export_pure(name, ps, raw['degrees'])
        summary['pure'].append(dict(module=name, cases=len(data), groups=[r['group'] for r in ps],
                                    maximum_bound=str(max(d['bound'] for d in data))))
        (HERE / f'{name}_REPLAY.json').write_text(json.dumps(json_value(data), indent=2) + '\n')
        print(name, len(data), 'pure', flush=True)
        for r in js:
            result = export_joint(f'{name}Joint{r["group"]}', r, raw['degrees'])
            summary['joint'].append(result)
            print(result, flush=True)
    (HERE / f'FEW_LOW_FOUR_{summary["mode"].upper()}_EXPORT.json').write_text(json.dumps(summary, indent=2) + '\n')


if __name__ == '__main__':
    main()
