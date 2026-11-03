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
INTERFACE = HERE.parent
CAP = INTERFACE / 'phase69_capacity_gate'
PREP = 0.1
PRIOR_INTERFACE = json.loads((INTERFACE / 'TERMINAL.json').read_text())['charged_case_CPU_seconds']
PRIOR_CAPACITY = json.loads((CAP / 'TERMINAL.json').read_text())['charged_gate_CPU_seconds']
PRIOR = PRIOR_INTERFACE + PRIOR_CAPACITY
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
Q = 139
ZERO = (0, 0, 0, 0)


def used():
    return time.process_time() - START


def charged():
    return PRIOR + PREP + used()


def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def finish(result, note):
    (HERE / 'NOTE.md').write_text(note + '\n')
    result.update(actual_process_CPU_seconds=used(),
        conservative_new_preparation_charge_seconds=PREP,
        prior_interface_charged_CPU_seconds=PRIOR_INTERFACE,
        prior_raw_capacity_charged_CPU_seconds=PRIOR_CAPACITY,
        cumulative_charged_CPU_seconds=charged(), cumulative_CPU_budget_seconds=10,
        single_worker=True, graph_BFS_source_or_old_field_validation=0,
        new_full_graph_solver_Lean_external_review_or_web=0,
        graph_parameter_Lean_count_increment=[0, 0, 0],
        root_STATE_HTML_Wiki_modified=False)
    save('RESULT.json', result)
    terminal = dict(status=result['status'], running=False,
        all_processes_terminal=True, actual_process_CPU_seconds=used(),
        conservative_new_preparation_charge_seconds=PREP,
        prior_charged_CPU_seconds=PRIOR,
        cumulative_charged_CPU_seconds=charged(), cumulative_CPU_budget_seconds=10,
        no_timer_reset=True, no_automatic_continuation=True)
    save('TERMINAL.json', terminal)
    save('HANDLE.json', dict(actual_PID=os.getpid(), stage='TERMINAL', **terminal))
    print(json.dumps(dict(status=result['status'], prediction=result.get('prediction'),
        raw_tight_word_count=result.get('raw_tight_word_count'),
        tight_distinct_forms=result.get('tight_distinct_form_count'),
        minimum_distinct_forms=result.get('minimum_distinct_form_count'),
        cumulative_charged_CPU_seconds=terminal['cumulative_charged_CPU_seconds'])), flush=True)


try:
    save('HANDLE.json', dict(actual_PID=os.getpid(), stage='ACTUAL_SAVED_TIGHT_WORD_FORM_BINDING',
        prior_charged_CPU_seconds=PRIOR, cumulative_CPU_budget_seconds=10, single_worker=True))
    source = json.loads((CAP / 'CONTROLLER_INPUT.json').read_text())
    darts = source['directed_port_types']
    transitions = source['outgoing_transitions']
    reverse = [d['reverse'] for d in darts]
    parameter_name = ['c0', 'c1', 'c2', 'c12']
    positive = {0:(0,3), 2:(1,11), 4:(2,6), 10:(3,4)}
    negative = {1:(0,3), 3:(1,11), 5:(2,6), 11:(3,4)}
    pow23 = pow(6,23,Q)
    action_defined = pow23 == 1 and 6 % Q != 1
    save('FORM_MODEL.json', dict(field_modulus=Q, multiplier=6,
        multiplier_power23=pow23, multiplier_not_one=6 % Q != 1,
        cyclic_phase_action_model_defined=action_defined,
        parameter_order=parameter_name,
        positive_darts={p:dict(parameter=j,phase=a) for p,(j,a) in positive.items()},
        inverse_darts={p:dict(parameter=j,positive_phase=a) for p,(j,a) in negative.items()},
        zero_translation_darts=[6,7,8,9],
        equation='final_y=initial_y+coefficient_vector dot(c0,c1,c2,c12)',
        positive_step='6^current_phase times c_j',
        inverse_step='-6^(current_phase-positive_phase) times c_j',
        prior_centered_control_used=False, old_field_laws_reverified=False))
    if not action_defined:
        raise RuntimeError('fixedr6/C23 model is not defined; no alias exclusion is valid')
    powers = [pow(6,x,Q) for x in range(23)]

    def step(u, p):
        base, x = divmod(u,23)
        d = darts[p]
        if d['from'] != base:
            raise RuntimeError('savedword has a dart outside its current base')
        v = 23*d['to'] + (x+d['phase']) % 23
        if p in positive:
            j, a = positive[p]
            coefficient = powers[x]
        elif p in negative:
            j, a = negative[p]
            coefficient = -powers[(x-a) % 23] % Q
        else:
            return v, ZERO
        c = [0,0,0,0]
        c[j] = coefficient
        return v, tuple(c)

    def plus(a,b):
        return tuple((a[i]+b[i]) % Q for i in range(4))

    tight = json.loads((CAP / 'TIGHT_PAIR_WORDS.json').read_text())
    groups = collections.defaultdict(list)
    for index, word in enumerate(tight['words']):
        u = tight['source_state']
        path = [u]
        form = ZERO
        for p in word['ports']:
            u, c = step(u,p)
            form = plus(form,c)
            path.append(u)
        if path != word['states'] or u != tight['target_state']:
            raise RuntimeError('saved tightword/controller path binding failed')
        groups[form].append(index)
    literal_classes = [dict(coefficient_vector=list(form),
        word_indices=indices, words=[tight['words'][i] for i in indices])
        for form,indices in sorted(groups.items())]
    raw_count = len(tight['words'])
    form_count = len(groups)
    save('TIGHT_WORD_FORM_CLASSES.json', dict(source_state=tight['source_state'],
        target_state=tight['target_state'], raw_word_count=raw_count,
        distinct_coefficient_form_count=form_count, parameter_order=parameter_name,
        all_saved_words_phase_bound=True, class_size_histogram=dict(sorted(collections.Counter(map(len,groups.values())).items())),
        classes=literal_classes))
    minimum = form_count
    pair = [tight['source_state'],tight['target_state']]
    allslots = False
    first_obstruction = form_count < Q
    if not first_obstruction:
        # Exact form-set DP at the three phase-zero starts. Equal forms in
        # equal(state,lastport) have identical future contributions, so merging
        # retains every distinct endpoint form without recounting raw walks.
        representatives = []
        form_rows = []
        for base in range(3):
            start_state = 23*base
            totals = [dict() for _ in range(69)]
            totals[start_state][ZERO] = ()
            state = {(start_state,-1):{ZERO:()}}
            for length in range(1,9):
                nxt = {}
                for (u,last), forms in state.items():
                    for p,v in transitions[u]:
                        if last >= 0 and p == reverse[last]:
                            continue
                        actual_v,c = step(u,p)
                        if actual_v != v:
                            raise RuntimeError('controller transition/form binding disagreement')
                        image = nxt.setdefault((v,p),{})
                        for form,word in forms.items():
                            form2 = plus(form,c)
                            image.setdefault(form2, word+(p,))
                state = nxt
                for (u,last), forms in state.items():
                    for form,word in forms.items():
                        totals[u].setdefault(form,word)
                if charged() > 9.4:
                    raise RuntimeError('original cumulative tenCPU budget reached; no reset')
            representatives.append(totals)
            form_rows.append([len(forms) for forms in totals])
        all_counts = [[form_rows[s//23][23*(t//23)+(t%23-s%23)%23]
                       for t in range(69)] for s in range(69)]
        minimum = min(x for row in all_counts for x in row)
        pair = next([s,t] for s in range(69) for t in range(69) if all_counts[s][t] == minimum)
        allslots = True
        with (HERE/'ALL_SLOT_DISTINCT_FORM_COUNTS.csv').open('w') as f:
            writer=csv.writer(f)
            writer.writerow(['source_state','target_state','distinct_F139_four_parameter_forms'])
            for s,row in enumerate(all_counts):
                for t,n in enumerate(row):
                    writer.writerow([s,t,n])
        save('ALL_PHASEZERO_FORM_CLASSES.json', dict(
            phase_transport='sourcephase+k,targetphase+k maps every form to6^k times itself;6^k nonzero gives a bijection',
            root_rows=[dict(source_state=23*b,targets=[dict(target_state=t,
                distinct_forms=[dict(coefficient_vector=list(form),representative_ports=list(word))
                    for form,word in sorted(forms.items())]) for t,forms in enumerate(totals)])
                for b,totals in enumerate(representatives)],
            all4761_count_matrix=all_counts))
        # Lex-first minimum always has source phase0, by phase transport.
        sb,sx=divmod(pair[0],23)
        tb,tx=divmod(pair[1],23)
        target0=23*tb+(tx-sx)%23
        save('MINIMUM_SLOT_FORM_CLASSES.json',dict(source_state=pair[0],target_state=pair[1],
            equivalent_source_phasezero_state=23*sb, equivalent_target_phasezero_state=target0,
            distinct_form_count=minimum,
            classes=[dict(coefficient_vector=list(form),representative_ports=list(word))
                     for form,word in sorted(representatives[sb][target0].items())]))
    excluded = minimum < Q
    result = dict(status=('EXACT_NO_FIXED_PHASE69_R6_F139_FOUR_SHARED_TRANSLATIONS_D8' if excluded else
        'NECESSARY_DISTINCT_FORM_CAPACITY_PASS_PARAMETERS_UNSOLVED'),
        prediction='SUPPORTED_UNAVOIDABLE_COEFFICIENT_ALIAS_CAPACITY_DEFICIT' if excluded else
            'REFUTED_ALL_DISTINCT_FORM_CAPACITIES_AT_LEAST139',
        target_degree=4,target_D=8,hypothetical_order=9591,
        coefficient_field_modulus=139,multiplier=6,multiplier_power23=pow23,
        parameters=parameter_name,gauge_zero_cross_links=[[0,1],[0,2]],
        raw_tight_word_count=raw_count,tight_distinct_form_count=form_count,
        tight_word_alias_classes=len(groups),minimum_distinct_form_count=minimum,
        witness_pair=pair, required_fiber_endpoints=139,
        all4761_coefficient_slots_computed=allslots,
        early_stop_after_saved_tight_slot=first_obstruction,
        saved_tight_word_phase_formula_bindings=raw_count,
        reused_prior_raw_word_count_without_rerunning_NB_counts=True,
        exact_exclusion_scope='Only the fixed69phase controller, r6 overF139, four shared normal translations(c0,c1,c2,c12), two identitycross translations gauged0, true inverse relations. No assumption on the previously failed centered assignment.',
        not_excluded=['arbitrary permutation covers if four-parameter form restriction is removed',
            'other phase/controller structures','general4D8 graphs'],
        next='STOP_THIS_FOUR_PARAMETER_FAMILY_NO_FIELD_OR_TIMER_EXPANSION' if excluded else
            'REPORT_NECESSARY_PASS_TO_ROOT_NO_AUTOMATIC_PARAMETER_SEARCH')
    aliases = [row for row in literal_classes if len(row['word_indices'])>1]
    sample = aliases[0] if aliases else None
    note = f'''# Shared-parameter endpoint forms: actual result

The fixed model uses F139, r=6 and four shared translations(c0,c1,c2,c12).
The two necessary new model checks gave6^23 mod139={pow23} and6!=1.
These are not a repeat of old field laws or original source verification.

The saved tight slot has{raw_count} nonbacktracking port words of lengths
at most8, all inherited from the preceding raw-capacity certificate. Their
actual controller-state paths were bound while deriving each endpoint form.
They give only{form_count} distinct F139^4 coefficient vectors.
TIGHT_WORD_FORM_CLASSES.json contains every vector class, its complete
member-word indices and all literal port/state paths. No old9591 centered
control or field endpoint evaluation was used.

For a positive dart of phase a at current phase x, its contribution is
6^x*c_j. The inverse group dart has translation-6^(-a)*c_j and phase-a,
so its contribution is-6^(x-a)*c_j. For a forward step followed by its
reverse, the two terms cancel symbolically. The two gauged identity cross
links have zero contribution. Hence every saved word w has final coordinate

    initial_y + L_w dot(c0,c1,c2,c12).

Equal coefficient vectors therefore give identical endpoints for every
parameter choice and every initial normal coordinate. Each word has one
endpoint; after grouping, at most the number of distinct vectors can occur.
Nonbacktracking projection of a shortest lifted route ensures that the
complete saved at-most8 word list is an upper bound for every possible
length-at-most8 route to this target phase fiber.

The actual minimum distinct-form count used by the verdict is{minimum},
at pair{pair}. {'It is less than139, so no choice of the four translations can cover all139 points in that target fiber. This strictly excludes the entire stated fixedphase/r6/four-parameter family at D8.' if excluded else 'It is at least139 everywhere; this is only a necessary pass. Distinct vectors can evaluate equally at chosen parameters and the shared parameters must satisfy every slot simultaneously.'}

{'The saved tight slot already gives the obstruction. No other coefficient slots or raw words were regenerated, and no field/parameter search follows.' if first_obstruction else 'Three phase-zero start rows were computed as exact form-set unions, then transported to all69starts: shifting every phase by k multiplies every form by nonzero6^k. This preserves distinct-form cardinality and gives all4761slot counts. These are coefficient images, not a repeated raw-NB count or a graph BFS.'}

The scope is a four-parameter affine-translation subfamily, narrower than
the earlier raw word gate for arbitrary fiber permutations. Thus a raw160
capacity pass and a possible coefficient deficit are compatible statements.
No conclusion excludes changed phases, arbitrary permutation voltage maps,
another controller, general4D8 graphs, or other sources. No9591-point graph,
BFS, solver, Lean or external review was generated. The original two prior
charges remain in the cumulative tenCPU ledger, and the batch stops.
'''
    finish(result,note)
except Exception as error:
    finish(dict(status='UNKNOWN_FORM_MODEL_BINDING_OR_CPU_FAILURE_NO_RETRY',
        prediction='UNRESOLVED',exception=repr(error),
        scope='Only this fixedr6/F139 four-parameter coefficient-image gate',
        next='REPORT_WITHOUT_TIMER_RESET_OR_NEW_SEARCH'),
        '# One coefficient gate stopped\nThe error and spent cumulative CPU are retained. No mathematical family exclusion or automatic retry follows.')
