#!/usr/bin/env python3
"""Independent short-walk phase tuples; no graph BFS and no C++ expression tables."""
import json
from pathlib import Path
import resource
import time

OUT = Path(__file__).resolve().parent


def emit(handle, obj):
    handle.write(json.dumps(obj, separators=(',', ':')) + '\n')


def forms_for_quotient(edges):
    variables = []
    arcs = [[] for _ in range(8)]
    loops = []
    extra_degrees = [0] * 8
    for edge_id, (u, v, half) in enumerate(edges):
        assert 0 <= u < 8 and 0 <= v < 8 and half in (0, 1)
        if half:
            assert u == v
            arcs[u].append((u, None, 4))
            extra_degrees[u] += 1
        else:
            j = len(variables)
            variables.append({'symbol': j, 'edge_index': edge_id, 'u': u, 'v': v})
            arcs[u].append((v, j, 1))
            arcs[v].append((u, j, -1))
            extra_degrees[u] += 1
            extra_degrees[v] += 1
            if u == v:
                loops.append(j)
    assert extra_degrees == [2] * 8
    for u in range(8):
        for b in (1, 2, 4):
            arcs[u].append((u ^ b, None, 0))
    k = len(variables)
    assert k <= 8
    zero = (0,) * (k + 1)
    pairs = []
    for root in range(8):
        reached = [set() for _ in range(8)]
        stack = [(root, 0, zero)]
        while stack:
            at, depth, expression = stack.pop()
            reached[at].add(expression)
            if depth == 3:
                continue
            for to, symbol, increment in arcs[at]:
                if symbol is None:
                    if increment == 0:
                        updated = expression
                    else:
                        updated = expression[:-1] + (4 - expression[-1],)
                else:
                    updated = (expression[:symbol] + (expression[symbol] + increment,)
                               + expression[symbol+1:])
                stack.append((to, depth + 1, updated))
        for target in range(root, 8):
            expressions = sorted(reached[target])
            assert len(expressions) >= 8
            assert all(sum(abs(c) for c in x[:-1]) <= 3 and x[-1] in (0, 4)
                       for x in expressions)
            pairs.append((root, target, expressions))
    # Ordering only accelerates the first failed necessary condition.
    pairs.sort(key=lambda item: (len(item[2]), item[0], item[1]))
    return variables, loops, pairs


def residue_counts(expressions, values, modulus):
    counts = [0] * modulus
    for expression in expressions:
        # Direct evaluation of signed tuple coefficients; no bit-dot table.
        phase = expression[-1]
        for j, value in enumerate(values):
            phase += expression[j] * value
        counts[phase % modulus] += 1
    return counts


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (15, 15))
    start = time.process_time()
    prediction = json.loads((OUT / 'PREDICTION.json').read_text())
    quotients = json.loads((OUT.parent / 'CANONICAL_QUOTIENTS.json').read_text())
    assert len(quotients) == 110
    totals = {'parity_domain': 0, 'parity_pass': 0, 'mod4_domain': 0,
              'mod4_pass': 0, 'mod8_domain': 0}
    case_rows = []
    parity_positive_cases = []
    complete = True
    positive_inputs = []
    with ((OUT / 'FORMAL_WALK_FORMS.jsonl').open('w') as formfile,
          (OUT / 'PARITY_REJECTIONS.jsonl').open('w') as parityfile,
          (OUT / 'MOD4_REJECTIONS.jsonl').open('w') as mod4file,
          (OUT / 'MOD4_PASS_INPUTS.jsonl').open('w') as passfile):
        for case_id, quotient in enumerate(quotients):
            if time.process_time() - start > prediction['soft_stop_CPU_seconds']:
                complete = False
                break
            variables, loops, pairs = forms_for_quotient(quotient['edges'])
            k = len(variables)
            emit(formfile, {'case': case_id, 'variables': variables, 'loop_symbols': loops,
                            'expression_encoding': 'signed coefficients then constant0or4',
                            'pairs': [{'labels': [u, v], 'forms': expressions}
                                      for u, v, expressions in pairs]})
            counts = {'parity_domain': 0, 'parity_pass': 0, 'mod4_domain': 0, 'mod4_pass': 0}
            for parity_mask in range(1, 1 << k):
                counts['parity_domain'] += 1
                lowbits = [(parity_mask >> j) & 1 for j in range(k)]
                parity_receipts = []
                for u, v, expressions in pairs:
                    counts2 = residue_counts(expressions, lowbits, 2)
                    if min(counts2) < 4:
                        emit(parityfile, {'case': case_id, 'parity_mask': parity_mask,
                                          'failure_pair': [u, v], 'residue_form_counts': counts2,
                                          'formal_phase_count': len(expressions)})
                        break
                    parity_receipts.append([u, v, *counts2])
                else:
                    counts['parity_pass'] += 1
                    positive_inputs.append({'case': case_id, 'parity_mask': parity_mask,
                                            'ordinary_edge_parities': lowbits,
                                            'variables': variables,
                                            'all_label_pair_parity_counts': parity_receipts})
                    firstodd = next(j for j, bit in enumerate(lowbits) if bit)
                    for next_mask in range(1 << k):
                        nextbits = [(next_mask >> j) & 1 for j in range(k)]
                        if nextbits[firstodd]:
                            continue
                        values = [a + 2*b for a, b in zip(lowbits, nextbits)]
                        if any(values[j] == 0 for j in loops):
                            continue
                        counts['mod4_domain'] += 1
                        for u, v, expressions in pairs:
                            counts4 = residue_counts(expressions, values, 4)
                            if min(counts4) < 2:
                                emit(mod4file, {'case': case_id, 'parity_mask': parity_mask,
                                               'second_bit_mask': next_mask,
                                               'mod4_voltages': values,
                                               'firstodd_symbol': firstodd,
                                               'failure_pair': [u, v],
                                               'residue_form_counts': counts4,
                                               'formal_phase_count': len(expressions)})
                                break
                        else:
                            counts['mod4_pass'] += 1
                            emit(passfile, {'case': case_id, 'parity_mask': parity_mask,
                                            'second_bit_mask': next_mask, 'mod4_voltages': values})
            if counts['parity_pass']:
                parity_positive_cases.append(case_id)
            for key, value in counts.items():
                totals[key] += value
            case_rows.append({'case': case_id, 'labelled_quotients': quotient['labelled_count'],
                              'symbols': k, 'counts': counts, 'complete': True})
    elapsed = time.process_time() - start
    (OUT / 'PARITY_POSITIVE_INPUTS.json').write_text(json.dumps(positive_inputs, indent=2) + '\n')
    (OUT / 'CASE_RECEIPTS.json').write_text(json.dumps(case_rows, indent=2) + '\n')
    expected = {'parity_domain': 20050, 'parity_pass': 28, 'mod4_domain': 3104,
                'mod4_pass': 0, 'mod8_domain': 0}
    result = {'status': ('COMPLETE_COUNTS_MATCH' if totals == expected else 'COMPLETE_COUNT_DISAGREEMENT')
                        if complete else 'PARTIAL_SCOPE_CPU_STOP',
              'input_quotients': len(quotients), 'completed_quotients': len(case_rows),
              'completed_case_ids': [r['case'] for r in case_rows],
              'parity_positive_case_ids': parity_positive_cases,
              'parity_positive_quotient_count': len(parity_positive_cases),
              'counts': totals, 'expected_counts': expected,
              'prediction_matches': complete and totals == expected and len(parity_positive_cases) == 17,
              'CPU_seconds': elapsed, 'CPU_budget_seconds': 15, 'workers': 1,
              'original213798_quotients_reenumerated': False,
              'full_graph_BFS': 0, 'SAT_calls': 0, 'mod8_enumerations': 0, 'new_graphs': 0,
              'pending': [], 'main_Wiki_changed': False}
    (OUT / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
