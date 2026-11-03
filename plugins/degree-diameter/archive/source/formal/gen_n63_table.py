"""Emit explicit Lean polynomial identities from the project finite table.
The emitted statements are proved by Lean; this generator is not trusted.
"""
import json
from pathlib import Path
import importlib.util
root = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('table', root/'computations/dd82/construction/n63_cyclotomic_norms.py')
table = importlib.util.module_from_spec(spec)
spec.loader.exec_module(table)
rows = json.loads((root/'computations/dd82/construction/n63_cyclotomic_norms.json').read_text())['rows']
phi = {}
for n in range(1,64):
    p = [-1]+[0]*(n-1)+[1]
    for k in range(1,n):
        if n%k==0: p=table.divide_monic(p,phi[k])
    phi[n]=p

def poly(cs):
    return ' + '.join(f'C ({a} : ℚ) * X ^ {i}' for i,a in reversed(list(enumerate(cs))) if a)
selected=[1,2,3,4,5,6,61]
s=['import DegreeDiameter.N63Compose','import Mathlib.Tactic.ComputeDegree','import Mathlib.Data.Rat.Lemmas','',
'namespace DegreeDiameter.N63Table','open Polynomial','open scoped BigOperators','noncomputable section',
'set_option maxRecDepth 10000','set_option maxHeartbeats 4000000','',
'''theorem not_isSquare_rat_of_mod (z : ℤ) (p : ℕ) [NeZero p]
    (h : ¬ IsSquare (z : ZMod p)) : ¬ IsSquare (z : ℚ) := by
  intro hz
  exact h ((Rat.isSquare_intCast_iff.mp hz).map (Int.castRingHom (ZMod p)))''','']
for n in selected:
    pd=[k for k in range(1,n) if n%k==0]
    s += [f'theorem phi_{n} : cyclotomic {n} ℚ = {poly(phi[n])} := by',
    '  symm',f'  apply (eq_cyclotomic_iff (by decide : 0 < {n}) _).2',
    f'  have hd : Nat.properDivisors {n} = '+ ('{' + ', '.join(map(str,pd)) + '}' if pd else '∅') +' := by decide',
    '  rw [hd]', '  norm_num [' + ', '.join(f'phi_{k}' for k in pd) + '] <;> ring','']
    row=rows[n-1]; d=row['degree']
    s += [f'def c{n} : ℚ[X] := {poly(row["real_cyclotomic_coefficients"])}','',
    f'theorem degree_c{n} : (c{n}).natDegree = {d} := by', f'  unfold c{n}', '  compute_degree!','',
    f'theorem monic_c{n} : (c{n}).Monic := by',f'  unfold c{n}','  monicity!','']
    if n>=3:
        s += [f'theorem lift_c{n} : cyclotomicLift c{n} = cyclotomic {n} ℚ := by',
        f'  rw [phi_{n}]','  unfold cyclotomicLift', f'  rw [degree_c{n}]',
        f'  norm_num [c{n}, homogenize_add, homogenize_C_mul, homogenize_X_pow, MvPolynomial.aeval_def] <;> ring','',f'theorem irreducible_c{n} : Irreducible c{n} :=',
        f'  irreducible_of_cyclotomic_lift (by decide : 0 < {n}) lift_c{n}','']
    else:
        s += [f'theorem irreducible_c{n} : Irreducible c{n} := by',
              '  apply Polynomial.irreducible_of_degree_eq_one', f'  unfold c{n}', '  compute_degree!', '']
    norm=row['discriminant_norm']
    s += [f'theorem norm_c{n} : (-4 : ℚ) ^ (c{n}).natDegree * (c{n}).eval (-29 / 4) = {norm} := by',
    f'  rw [degree_c{n}]',f'  norm_num [c{n}]','']
    if n!=3:
        m=row['modulus']
        s += [f'theorem nonsquare_c{n} : ¬ IsSquare ((-4 : ℚ) ^ (c{n}).natDegree * (c{n}).eval (-29 / 4)) := by',
        f'  rw [norm_c{n}]',f'  exact not_isSquare_rat_of_mod {norm} {m} (by unfold IsSquare; decide)','',
        f'theorem irreducible_comp_c{n} : Irreducible ((c{n}).comp n63Quadratic) :=',
        f'  n63_composition_irreducible monic_c{n} irreducible_c{n} nonsquare_c{n}','']
s += ['end','end DegreeDiameter.N63Table','']
(root/'formal/DegreeDiameter/N63Table.lean').write_text('\n'.join(s))
