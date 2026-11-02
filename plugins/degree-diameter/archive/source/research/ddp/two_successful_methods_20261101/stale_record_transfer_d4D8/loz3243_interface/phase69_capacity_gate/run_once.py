#!/usr/bin/env python3
import time
START = time.process_time()
import collections
import csv
import json
import os
import resource
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'research-wiki').is_dir())
SOURCE = ROOT / 'research/ddp/more_graphs_20261027/d4_D8_current3243_transfer/SOURCE_FACTS.json'
PREP = 0.1
resource.setrlimit(resource.RLIMIT_CPU, (5, 5))


def used():
    return time.process_time() - START


def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def finish(result, note):
    (HERE / 'NOTE.md').write_text(note + '\n')
    result.update(actual_process_CPU_seconds=used(),
        conservative_preparation_charge_seconds=PREP,
        charged_gate_CPU_seconds=used() + PREP, gate_CPU_budget_seconds=5,
        single_worker=True, original3243_or9591_BFS=0,
        original_source_graph_field_inverse_or_legality_rechecks=0,
        new_full_graphs_solver_Lean_web_or_review=0,
        graph_parameter_Lean_count_increment=[0, 0, 0],
        root_STATE_HTML_Wiki_modified=False)
    save('RESULT.json', result)
    terminal = dict(status=result['status'], running=False,
        all_processes_terminal=True, actual_process_CPU_seconds=used(),
        conservative_preparation_charge_seconds=PREP,
        charged_gate_CPU_seconds=used() + PREP, gate_CPU_budget_seconds=5,
        no_automatic_continuation=True)
    save('TERMINAL.json', terminal)
    save('HANDLE.json', dict(actual_PID=os.getpid(), stage='TERMINAL', **terminal))
    print(json.dumps(dict(status=result['status'], minimum=result.get('minimum_words'),
        tight_pair=result.get('tight_pair'), prediction=result.get('prediction'),
        charged_gate_CPU_seconds=terminal['charged_gate_CPU_seconds'])), flush=True)


try:
    save('HANDLE.json', dict(actual_PID=os.getpid(),
        stage='ACTUAL_69_STATE_LENGTH8_NB_CAPACITY', gate_CPU_budget_seconds=5,
        single_worker=True, no_field_or_large_graph_input=True))
    facts = json.loads(SOURCE.read_text())
    darts = facts['darts']
    bybase = [[d['id'] for d in darts if d['from'] == b] for b in range(3)]
    reverse = [d['reverse'] for d in darts]
    transitions = [[(p, 23 * darts[p]['to'] + (phase + darts[p]['phase']) % 23)
                    for p in bybase[base]] for base in range(3) for phase in range(23)]
    save('CONTROLLER_INPUT.json', dict(state_encoding='23*base+phase', states=69,
        source_recipe=str(SOURCE.relative_to(ROOT)),
        directed_port_types=[{k:d[k] for k in ['id', 'from', 'to', 'phase', 'reverse']} for d in darts],
        outgoing_transitions=transitions,
        actual_field_translations_used=False, fiber_permutations_assumed=False,
        source_47_D8_inherited_only=True))
    counts = []
    length_totals = []
    minimum = None
    tight = None
    for source in range(69):
        totals = [0] * 69
        totals[source] = 1
        state = {(source, -1): 1}
        lengths = [1]
        for length in range(1, 9):
            nxt = collections.defaultdict(int)
            for (u, last), number in state.items():
                for port, v in transitions[u]:
                    if last >= 0 and port == reverse[last]:
                        continue
                    nxt[v, port] += number
            state = nxt
            lengths.append(sum(state.values()))
            for (u, last), number in state.items():
                totals[u] += number
        counts.append(totals)
        length_totals.append(lengths)
        for target, n in enumerate(totals):
            if minimum is None or n < minimum:
                minimum = n
                tight = [source, target]
        if used() + PREP > 4.5:
            raise RuntimeError('original five-CPU cap reached before complete count; no continuation')

    source, target = tight
    words = []
    def collect(u, last, word, path):
        if u == target:
            words.append(dict(ports=word, states=path, length=len(word)))
        if len(word) == 8:
            return
        for port, v in transitions[u]:
            if last < 0 or port != reverse[last]:
                collect(v, port, word + [port], path + [v])
    collect(source, -1, [], [source])
    assert len(words) == minimum
    assert len({tuple(w['ports']) for w in words}) == minimum
    save('TIGHT_PAIR_WORDS.json', dict(source_state=source, target_state=target,
        source_base_phase=list(divmod(source, 23)), target_base_phase=list(divmod(target, 23)),
        minimum_word_count=minimum, required_fiber_endpoints=139,
        words_are_distinct_directed_port_sequences=True,
        complete_nonbacktracking_lengths=[0, 8], words=words))
    with (HERE / 'ALL_ORDERED_PHASE_PAIR_COUNTS.csv').open('w') as f:
        writer = csv.writer(f)
        writer.writerow(['source_state', 'source_base', 'source_phase',
                         'target_state', 'target_base', 'target_phase', 'NB_words_length0_to8'])
        for s, row in enumerate(counts):
            for t, n in enumerate(row):
                writer.writerow([s, *divmod(s, 23), t, *divmod(t, 23), n])
    passed = minimum >= 139
    consistency = minimum >= 47
    status = ('UNKNOWN_INPUT_PROJECTION_CONFLICT_WITH_INHERITED47_SOURCE' if not consistency else
              'NECESSARY_CAPACITY_PASS_NO_GRAPH_OR_FIELD_CONSTRUCTION' if passed else
              'EXACT_NO_FIXED_PHASE69_ANY_139SHEET_COVER_D8')
    result = dict(status=status,
        prediction='REFUTED_MINIMUM_AT_LEAST139' if passed else 'SUPPORTED_RAW_ROUTE_DEFICIT_BELOW139',
        controller_states=69, source_base_count=3, phase_modulus=23,
        directed_port_types=12, actual_ordered_pairs_counted=69 * 69,
        nonbacktracking_lengths=[0, 8], zero_length_word_included=True,
        ordinary_cover_sheet_target=139, hypothetical_order=9591,
        minimum_words=minimum, tight_pair=tight,
        tight_source_base_phase=list(divmod(source, 23)),
        tight_target_base_phase=list(divmod(target, 23)),
        minimum_slots=[[s, t] for s in range(69) for t in range(69) if counts[s][t] == minimum],
        all_slot_count_histogram=dict(sorted(collections.Counter(n for row in counts for n in row).items())),
        count_matrix=counts, word_totals_by_exact_length_each_source=length_totals,
        tight_literal_word_certificate_count=len(words), capacity_pass=passed,
        inherited47_source_consistency_lower_bound=47,
        inherited47_source_consistency_comparison=consistency,
        inverse_dart_mapping_inherited_without_recheck=True,
        multiplier6_mod139_order_checked=False, finite_field_assumption_used=False,
        scope='Any ordinary139sheet permutation cover of this fixed69phase controller. No affine field specialization is required; not all4D8 graphs or changedphase graphs.',
        next='REPORT_NECESSARY_PASS_TO_ROOT_NO_AUTOMATIC_VOLTAGE_SEARCH' if passed else
             'STOP_FIXED_PHASE69_139SHEET_FAMILY_NO_Q_SCREEN_OR_TIMER')
    note = f'''# Fixed69-phase controller capacity: actual terminal result

All4761 ordered controller pairs were counted for nonbacktracking port
words of lengths0..8, including the empty word. The actual minimum is
{minimum}, at state pair{tight}; base/phase labels are
{list(divmod(source,23))} to{list(divmod(target,23))}. Every slot count is in
ALL_ORDERED_PHASE_PAIR_COUNTS.csv and RESULT.json. TIGHT_PAIR_WORDS.json lists
all{minimum} distinct directed port words in this tight slot, with their
complete controller paths. The word count is independent of any field or
choice of fiber permutations. No original3243 source or9591 graph was built
or searched by BFS.

The input is the actual twelve directed port types/reverse involution from
the recovered source recipe, expanded to69 states23*base+phase. Its old
valid47-sheet realization is inherited. Comparing the new minimum against
47 is a consistency check of this necessary projection bound, not a new
legality or diameter test of the old source.

A shortest lifted route projects without an immediate inverse-port pair,
because the locally unique reverse lifted edge would otherwise immediately
retrace. Each remaining directed base word has one lifted endpoint from a
fixed root. Therefore a count less than139 leaves some vertices of a target
fiber out of range8 for every ordinary139sheet cover of this controller,
even with arbitrary inverse-consistent permutation voltages. This argument
does not assume that6 has order23 modulo139 or even use a finite field.

The actual verdict is {'a necessary capacity PASS only; the stated deficit prediction is refuted' if passed else 'a capacity deficit; the stated prediction is supported'}.
{'Different words can still have equal lift endpoints, and shared edge permutations can be incompatible across slots. Thus no9591 graph, diameter theorem, field model or record is obtained from this count. Root must choose any later voltage question.' if passed else 'The fixed69phase139sheet family stops at this raw route deficit. No other q, phase profile, source, field or offset is tested.'}

The earlier original3243 ordinary-cover girth exclusion and unique centered
F139/D9 control remain separate records and were not rerun. This is one
new, bounded small-controller route count, not a template screen or a new
full graph. Root documents, HTML, Wiki and graph/Lean counts are unchanged.
'''
    finish(result, note)
except Exception as error:
    finish(dict(status='UNKNOWN_IMPLEMENTATION_OR_CPU_STOP_NO_RETRY',
        prediction='UNRESOLVED', exception=repr(error),
        scope='Only the one fixed69phase length8 NB capacity calculation',
        next='REPORT_UNFINISHED_SCOPE_NO_TIMER_RESET'),
        '# One bounded phase-capacity attempt stopped\nThe exception and spent CPU remain recorded. No retry or mathematical exclusion follows.')
