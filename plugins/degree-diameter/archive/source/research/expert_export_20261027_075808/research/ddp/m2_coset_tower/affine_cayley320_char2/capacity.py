#!/usr/bin/env python3
"""GF16 affine Cayley capacity only: no field assignments, graphs, or BFS."""
from collections import Counter
from itertools import combinations_with_replacement
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent

def field_mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 16:
            a ^= 0x13
    return result

MUL = [[field_mul(a, b) for b in range(16)] for a in range(16)]

def power(a, n):
    result = 1
    for unused in range(n):
        result = MUL[result][a]
    return result

def main():
    start = time.process_time()
    # Polynomial t^4+t+1 is irreducible over F2: no linear factor; the only
    # irreducible quadratic is t^2+t+1, and reduction gives remainder 1.
    assert 0x13 & 1 and (0x13.bit_count() % 2) == 1
    remainder = 0x13
    while remainder.bit_length() >= 3:
        remainder ^= 0b111 << (remainder.bit_length() - 3)
    assert remainder == 1
    g = 2
    assert len({power(g, i) for i in range(15)}) == 15 and power(g, 15) == 1
    inverse = [0] + [next(y for y in range(1, 16) if MUL[x][y] == 1)
                     for x in range(1, 16)]
    assert all(MUL[a][b] == MUL[b][a] for a in range(16) for b in range(16))
    assert all(MUL[a][b ^ c] == (MUL[a][b] ^ MUL[a][c])
               for a in range(16) for b in range(16) for c in range(16))
    r = power(g, 3)
    scalar = [power(r, i) for i in range(20)]
    assert r == 8 and len(set(scalar)) == 5 and power(r, 5) == 1
    arithmetic = {'field': 'F2[t]/(t^4+t+1)', 'encoding': '4-bit polynomial',
                  'addition': 'bitwise XOR', 'multiplication': MUL, 'inverse': inverse,
                  'g': g, 'g_order': 15, 'r': r, 'r_order': 5, 'phase_scalar': scalar,
                  'irreducibility_checked': True,
                  'all_nonzero_inverses_and_distributivity_checked': True}
    (HERE / 'FIELD_TABLES.json').write_text(json.dumps(arithmetic, indent=2) + '\n')
    records, ordinary_survivors, symbolic_records, survivors, branches = [], [], [], [], []
    for pairs in range(5):
        involutions = 8 - 2 * pairs
        component_count = pairs + involutions
        inverse_letter = [i ^ 1 if i < 2 * pairs else i for i in range(8)]
        layers = [[()]]
        for unused in range(3):
            layers.append([w + (s,) for w in layers[-1] for s in range(8)
                           if not w or s != inverse_letter[w[-1]]])
        assert list(map(len, layers)) == [1, 8, 56, 392]
        words = [w for layer in layers for w in layer]
        branch = {'pairs': pairs, 'involutions': involutions, 'patterns': 0,
                  'ordinary_pass': 0, 'symbolic_pass': 0,
                  'ordinary_projective_marked_inputs': 0,
                  'symbolic_projective_marked_inputs': 0}
        for phases in combinations_with_replacement(range(1, 10), pairs):
            for zero_count in range(involutions + 1):
                components = list(phases) + [0] * zero_count + [10] * (involutions - zero_count)
                letter_phases = [k for phase in phases for k in (phase, -phase % 20)] + components[pairs:]
                ordinary = [0] * 20
                for word in words:
                    ordinary[sum(letter_phases[s] for s in word) % 20] += 1
                deficient = [k for k, count in enumerate(ordinary) if count < 16]
                row = {'id': len(records), 'pair_count': pairs, 'involution_count': involutions,
                       'pair_phases': list(phases), 'phase0_involutions': zero_count,
                       'phase10_involutions': involutions - zero_count,
                       'component_phases': components, 'ordinary_capacity': ordinary,
                       'ordinary_deficient_phases': deficient, 'ordinary_pass': not deficient,
                       'field_variable_count': component_count}
                records.append(row)
                branch['patterns'] += 1
                if deficient:
                    continue
                ordinary_survivors.append(row)
                branch['ordinary_pass'] += 1
                anchor = next((i for i, k in enumerate(components) if scalar[k] != 1), None)
                # All trivial-action phases are multiples of 5; their quotient
                # words stay in <5>, so they cannot pass coverage of all C20.
                assert anchor is not None
                marked = (16 ** (component_count - 1) - 1) // 15
                branch['ordinary_projective_marked_inputs'] += marked
                letters = []
                for i, phase in enumerate(components):
                    coeff = [0] * component_count
                    coeff[i] = 1
                    letters.append((phase, tuple(coeff)))
                    if i < pairs:
                        letters.append((-phase % 20,
                                        tuple(MUL[inverse[scalar[phase]]][x] for x in coeff)))
                assert len(letters) == 8
                symbolic = [{(0,) * component_count: ()}] + [{} for unused in range(19)]
                level = [((), 0, (0,) * component_count)]
                for unused in range(3):
                    new = []
                    for word, phase, coeff in level:
                        for letter, (target_phase, target_coeff) in enumerate(letters):
                            if word and letter == inverse_letter[word[-1]]:
                                continue
                            new_phase = (phase + target_phase) % 20
                            new_coeff = tuple(a ^ MUL[scalar[phase]][b]
                                              for a, b in zip(coeff, target_coeff))
                            new_word = word + (letter,)
                            symbolic[new_phase].setdefault(new_coeff, new_word)
                            new.append((new_word, new_phase, new_coeff))
                    level = new
                form_counts = [len(forms) for forms in symbolic]
                symbolic_deficient = [k for k, count in enumerate(form_counts) if count < 16]
                direction = [1 ^ scalar[k] for k in components]
                for phase, forms in enumerate(symbolic):
                    for coeff in forms:
                        dot = 0
                        for a, b in zip(coeff, direction):
                            dot ^= MUL[a][b]
                        assert dot == (1 ^ scalar[phase])
                    dropped = {coeff[:anchor] + coeff[anchor + 1:] for coeff in forms}
                    assert len(dropped) == len(forms)
                critical = min(range(20), key=lambda k: form_counts[k])
                extended = {**row, 'anchor_component': anchor,
                            'projective_marked_inputs': marked,
                            'symbolic_capacity': form_counts,
                            'symbolic_deficient_phases': symbolic_deficient,
                            'symbolic_pass': not symbolic_deficient,
                            'minimum_symbolic_capacity': form_counts[critical],
                            'critical_phase': critical,
                            'critical_phase_forms': [list(c) for c in sorted(symbolic[critical])],
                            'anchor_drop_injective_checked': True}
                symbolic_records.append(extended)
                if not symbolic_deficient:
                    survivors.append(extended)
                    branch['symbolic_pass'] += 1
                    branch['symbolic_projective_marked_inputs'] += marked
        branches.append(branch)
    assert [b['patterns'] for b in branches] == [9, 63, 225, 495, 495]
    assert len(records) == 1287
    (HERE / 'phase_patterns.json').write_text(json.dumps(records, indent=2) + '\n')
    (HERE / 'ordinary_survivors.json').write_text(json.dumps(ordinary_survivors, indent=2) + '\n')
    (HERE / 'symbolic_patterns.json').write_text(json.dumps(symbolic_records, indent=2) + '\n')
    (HERE / 'symbolic_survivors.json').write_text(json.dumps(survivors, indent=2) + '\n')
    elapsed = time.process_time() - start
    result = {'status': 'COMPLETE_CAPACITY_ONLY_NO_GRAPH_SEARCH',
              'group': 'F16 additive semidirect C20, generator action t^3 order5',
              'n': 320, 'degree': 8, 'target_diameter': 3,
              'field_definition': 'F2[t]/(t^4+t+1)', 'r_encoding': r,
              'nonidentity_involutions': 31, 'inverse_pairs': 144,
              'phase_patterns': len(records), 'ordinary_pass': len(ordinary_survivors),
              'symbolic_pass': len(survivors),
              'ordinary_projective_marked_inputs': sum(b['ordinary_projective_marked_inputs'] for b in branches),
              'symbolic_projective_marked_inputs': sum(b['symbolic_projective_marked_inputs'] for b in branches),
              'branches': branches, 'CPU_seconds': elapsed, 'CPU_budget_seconds': 30,
              'worker_count': 1, 'field_assignments_tested': 0, 'graphs_generated': 0,
              'BFS_runs': 0, 'running': False}
    assert 2 * 144 + 31 + 1 == 320 and elapsed < 30
    (HERE / 'CAPACITY_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    (HERE / 'terminal.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
