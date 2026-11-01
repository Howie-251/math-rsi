"""Render static profiles as Lean data; Lean recomputes every asserted number.

No executable Python output is assumed as a theorem. The emitted equality
proofs use `decide +kernel`, reducing the independent Lean formulas directly.
This generator neither imports multilock.py nor copies its probability code.
"""
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'formal/Aris4Math/Numeric.lean'
START = '-- BEGIN GENERATED CLOSED CERTIFICATES'
END = '-- END GENERATED CLOSED CERTIFICATES'

def rat(value):
    q = Fraction(value)
    return f'({q.numerator} / {q.denominator} : Rat)'

def ns(values):
    return '[' + ', '.join(map(str, values)) + ']'

def run():
    cases = json.loads((ROOT / 'results/reproduced_bounds.json').read_text())['cases']
    lines = [START, '/- Static inputs correspond to results/reproduced_bounds.json.\n'
             'Expected fractions are conclusions proved by kernel reduction,\n'
             'never hypotheses. Both unused diagnostic profiles are retained. -/']
    successes = []
    diagnostics = []
    for case in cases:
        name = case['name'].replace('-', '_')
        pos = case['positions']
        records = []
        for mask, count in case['counts'].items():
            locks = [p for i, p in enumerate(pos) if int(mask) & (1 << i)]
            records.append('⟨' + ns(locks) + f', {count}⟩')
        centers = [cert['position'] for cert in case['certificates']]
        cap = 'some 948' if name == 'v20' else 'none'
        lines += [f'\n-- {case["name"]}: masks/counts {case["counts"]}',
                  f'def {name} : Profile :=',
                  f'  ⟨{case["v"]}, {ns(pos)}, [{", ".join(records)}], {cap}, {ns(centers)}⟩',
                  f'theorem {name}_valid : validProfile {name} := by unfold validProfile; decide +kernel',
                  f'theorem {name}_value : totalBound {name} = {rat(case["corrected_bound"])} := by',
                  '  decide +kernel',
                  f'#print axioms {name}_value']
        if centers:
            lines += [f'theorem {name}_base_value : totalBound {{ {name} with correctionCenters := [] }} = {rat(case["base_bound"])} := by',
                      '  decide +kernel']
        for cert in case['certificates']:
            k, q = cert['position'], cert['q_lower']
            lines += [f'theorem {name}_link_{k} :',
                      f'    linkQLower {name} {k} = {q} ∧',
                      f'    {q} ≤ (linkSlots {name} {k}).length ∧',
                      f'    deduction {name} {k} = {rat(cert["deduction"])} ∧',
                      f'    0 ≤ deduction {name} {k} ∧ deduction {name} {k} ≤ boundC {name} {k} := by',
                      '  decide +kernel']
        successful = Fraction(case['corrected_bound']) < 1
        suffix = 'lt_one' if successful else 'gt_one'
        relation = '<' if successful else '>'
        lines += [f'theorem {name}_{suffix} : totalBound {name} {relation} 1 := by',
                  f'  rw [{name}_value]', '  norm_num']
        (successes if successful else diagnostics).append(name)
    # A single aggregate proposition records exactly what is certified.
    lines += ['\n/-- The twenty-one profiles actually used by the proof. -/',
              'def successfulProfiles : List Profile := [' + ', '.join(successes) + ']',
              'theorem all_successful_values : ∀ p ∈ successfulProfiles, totalBound p < 1 := by',
              '  intro p hp',
              '  simp only [successfulProfiles, List.mem_cons, List.not_mem_nil, or_false] at hp',
              '  rcases hp with ' + ' | '.join(['rfl'] * len(successes))]
    lines += ['  · exact ' + name + '_lt_one' for name in successes]
    lines += ['#print axioms all_successful_values',
              '#print axioms binom_eq_choose', END]
    before, rest = TARGET.read_text().split(START, 1)
    _, after = rest.split(END, 1)
    TARGET.write_text(before + '\n'.join(lines) + after)
    print(f'Generated {len(cases)} profiles: {len(successes)} successful, {len(diagnostics)} diagnostic; '
          f'{sum(len(c["certificates"]) for c in cases)} link centers.')

if __name__ == '__main__':
    run()
