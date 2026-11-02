#!/usr/bin/env python3
"""Exact necessary quotient-word counts; no field assignments or graph search."""
from collections import Counter
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import json
import time


def formal_words(pair_count):
    inverse = [j ^ 1 if j < 2 * pair_count else j for j in range(8)]
    layers = [[()]]
    for length in range(1, 4):
        layers.append([
            word + (letter,)
            for word in layers[-1]
            for letter in range(8)
            if not word or letter != inverse[word[-1]]
        ])
    assert [len(layer) for layer in layers] == [1, 8, 56, 392]
    return [word for layer in layers for word in layer]


def main():
    start = time.process_time()
    records, survivors, grouped = [], [], []
    global_minimum_histogram = Counter()
    for pairs in range(5):
        involutions = 8 - 2 * pairs
        words = formal_words(pairs)
        minima = Counter()
        passed = 0
        count = 0
        for phases in combinations_with_replacement(range(15), pairs):
            letters = [v for phase in phases for v in (phase, (-phase) % 30)]
            letters += [15] * involutions
            capacity = [0] * 30
            for word in words:
                capacity[sum(letters[j] for j in word) % 30] += 1
            assert sum(capacity) == 457
            assert all(capacity[z] == capacity[-z % 30] for z in range(30))
            minimum = min(capacity)
            deficient = [z for z, n in enumerate(capacity) if n < 11]
            row = {
                'id': len(records),
                'pair_count': pairs,
                'involution_count': involutions,
                'pair_phase_classes': list(phases),
                'capacity_by_phase_0_to_29': capacity,
                'minimum_capacity': minimum,
                'deficient_phases': deficient,
                'passes_necessary_capacity': not deficient,
            }
            records.append(row)
            if not deficient:
                survivors.append(row)
                passed += 1
            minima[minimum] += 1
            global_minimum_histogram[minimum] += 1
            count += 1
        assert count == comb(pairs + 14, pairs)
        grouped.append({
            'pair_count': pairs,
            'involution_count': involutions,
            'patterns': count,
            'survivors': passed,
            'maximum_of_minimum_capacity': max(minima),
            'minimum_capacity_histogram': dict(sorted(minima.items())),
        })
    assert len(records) == comb(19, 4) == 3876
    result = {
        'status': 'COMPLETE_QUOTIENT_CAPACITY_ONLY',
        'group': '(F11 semidirect_2 C10) x C3',
        'group_order': 330,
        'degree': 8,
        'target_diameter': 3,
        'quotient': 'C30, phase z: j=z mod10, w=z mod3',
        'kernel_size': 11,
        'pair_phase_classes': '0 and {z,-z} for z=1..14',
        'involution_phase': 15,
        'formal_words_by_length': [1, 8, 56, 392],
        'formal_words_total': 457,
        'patterns_checked': len(records),
        'survivor_count': len(survivors),
        'all_patterns_excluded': not survivors,
        'maximum_of_minimum_capacity': max(global_minimum_histogram),
        'minimum_capacity_histogram': dict(sorted(global_minimum_histogram.items())),
        'by_component_count': grouped,
        'survivors': survivors,
        'survivors_with_phase_zero': sum(0 in row['pair_phase_classes'] for row in survivors),
        'survivors_with_repeated_pair_phase': sum(len(set(row['pair_phase_classes'])) < row['pair_count'] for row in survivors),
        'all_pattern_results_file': 'quotient_word_capacity_patterns.json',
        'field_assignments_enumerated': 0,
        'graphs_generated': 0,
        'CPU_seconds': time.process_time() - start,
    }
    out = Path(__file__).resolve().parent
    (out / 'quotient_word_capacity_patterns.json').write_text(json.dumps(records, separators=(',', ':')) + '\n')
    (out / 'QUOTIENT_WORD_CAPACITY.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('survivors', 'minimum_capacity_histogram')}, indent=2))


if __name__ == '__main__':
    main()
