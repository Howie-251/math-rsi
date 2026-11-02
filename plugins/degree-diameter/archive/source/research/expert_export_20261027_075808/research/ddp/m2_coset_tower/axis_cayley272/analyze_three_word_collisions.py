"""Saved 272 root data and 312 symbolic phase patterns; no graph or BFS."""
import json
import time
from collections import Counter
from pathlib import Path
from symbolic_affine_words import affine_word_forms

start = time.process_time()
here = Path(__file__).resolve().parent
other = here.parent/'affine_cayley312'

def phase_tables(modulus, central_order):
    count = modulus*central_order
    mul = [[(a % modulus+b % modulus) % modulus
            +modulus*((a//modulus+b//modulus) % central_order)
            for b in range(count)] for a in range(count)]
    inv = [-a % modulus+modulus*(-(a//modulus) % central_order) for a in range(count)]
    return mul, inv

def direct_word(p,mul,scalar,alphabet,word,values):
    x,phase = 0,0
    for letter in word:
        a = alphabet[letter]
        y = sum(c*v for c,v in zip(a['coeff'],values)) % p
        x = (x+scalar[phase]*y) % p
        phase = mul[phase][a['phase']]
    return x,phase

saved = json.loads((here/'production.best.json').read_text())
checked = json.loads((here/'production.best.independent_check.json').read_text())
p,modulus = 17,16
mul,inv = phase_tables(modulus,1)
scalar = [pow(3,j,p) for j in range(modulus)]
components = [{'phase':j,'kind':'pair' if c < 3 else 'involution'}
              for c,j in enumerate(saved['component_phases'])]
symbolic = affine_word_forms(p,mul,inv,scalar,components)
values = saved['fields']
phase_rows = []
covered = set()
for phase,forms in enumerate(symbolic['forms']):
    evaluations = {}
    for coeff,words in forms.items():
        value = sum(c*x for c,x in zip(coeff,values)) % p
        evaluations.setdefault(value, []).append({'coeff':list(coeff),
                                                   'words':[list(w) for w in words]})
        for word in words:
            assert direct_word(p,mul,scalar,symbolic['alphabet'],word,values) == (value,phase)
        covered.add(value+p*phase)
    phase_rows.append({'phase':phase,'raw_words':symbolic['raw_counts'][phase],
        'distinct_forms':len(forms),'actual_values':len(evaluations),
        'missing_fields':sorted(set(range(p))-set(evaluations)),
        'constant_form_collisions':symbolic['raw_counts'][phase]-len(forms),
        'evaluation_collision_excess':len(forms)-len(evaluations),
        'evaluated_collision_groups':{str(x):items for x,items in evaluations.items() if len(items)>1}})
missing = sorted(set(range(272))-covered)
assert missing == [g for g,d in enumerate(checked['root_0_distances']) if d > 3]
assert len(missing) == 9 and len(covered) == 263
inverse_classes = []
for g in missing:
    x,j = g % p,g//p
    h = -pow(3,-j,p)*x % p + p*(-j % modulus)
    assert h in missing
    if g <= h:
        inverse_classes.append([[x,j],[h % p,h//p]] if g != h else [[x,j]])
g = (10,1)
assert ((g[0]+pow(3,g[1],p)*g[0]) % p,2*g[1] % modulus) == (6,2)
analysis272 = {
    'status':'COMPLETE_SAVED_ROOT_AND_SYMBOLIC_WORD_ANALYSIS_NO_BFS',
    'group':'F17 semidirect_3 C16','input':'production.best.independent_check.json',
    'component_phases':saved['component_phases'],'field_values':values,
    'letter_names':['A','a','B','b','C','c','I','J'],
    'alphabet':symbolic['alphabet'],'formal_words':len(symbolic['words']),
    'distinct_form_phase_pairs':sum(symbolic['form_counts']),
    'actual_reachable_elements':len(covered),'missing_codes':missing,
    'missing_coordinates':[[x % p,x//p] for x in missing],
    'missing_inverse_classes':inverse_classes,
    'missing_structure':'{g^+/-1,g^+/-2,h^+/-1,k^+/-1,t}; g=(10,1),h=(12,5),k=(12,6),t=(0,8)',
    'phase_rows':phase_rows,'root_distance_recomputed_by_BFS':False,
    'direct_word_checks':len(symbolic['words'])}

capacity = json.loads((other/'QUOTIENT_CAPACITY.json').read_text())
p,modulus = 13,12
mul,inv = phase_tables(modulus,2)
scalar = [pow(2,j % modulus,p) for j in range(24)]
rows = []
calibration = []
for pattern in capacity['survivors']:
    components = [{'phase':j+modulus*w,'kind':'pair'} for j,w in pattern['pair_phases']]
    components += [{'phase':6,'kind':'involution'}]*pattern['reflection_6_0_count']
    components += [{'phase':18,'kind':'involution'}]*pattern['reflection_6_1_count']
    components += [{'phase':12,'kind':'involution','free_coordinate':False}]*pattern['central_involution_count']
    data = affine_word_forms(p,mul,inv,scalar,components)
    assert data['raw_counts'] == pattern['capacity_by_j_plus12w']
    assert data['variable_count'] == pattern['free_component_coordinates']
    free_phases = [c['phase'] for c in components if c.get('free_coordinate',True)]
    conjugation_direction = [(1-scalar[j]) % p for j in free_phases]
    anchor = next(i for i,x in enumerate(conjugation_direction) if x)
    # Same-phase differences annihilate the common conjugation direction.
    # Thus deleting this anchor coordinate cannot merge distinct forms.
    for phase,forms in enumerate(data['forms']):
        assert all(sum(c*t for c,t in zip(coeff,conjugation_direction)) % p
                   == (1-scalar[phase]) % p for coeff in forms)
        assert len({coeff[:anchor]+coeff[anchor+1:] for coeff in forms}) == len(forms)
    failing = [j for j,count in enumerate(data['form_counts']) if count < p]
    tight = [j for j,count in enumerate(data['form_counts']) if count == p]
    row = {'pattern_id':pattern['id'],'components':components,
           'component_variables':data['component_variables'],
           'raw_counts':data['raw_counts'],'distinct_form_counts':data['form_counts'],
           'minimum_distinct_forms':min(data['form_counts']),
           'excluded':bool(failing),'failing_phases_j_plus12w':failing,
           'projective_input_bound':pattern['projective_input_bound'],
           'anchor_component_variable':anchor,'anchor_projection_preserves_form_counts':True}
    if failing:
        phase = min(failing,key=lambda j:(len(data['forms'][j]),j))
        row['witness'] = {'phase':phase,'phase_coordinates':[phase % 12,phase//12],
            'raw_words':data['raw_counts'][phase],'distinct_forms':len(data['forms'][phase]),
            'forms':[list(c) for c in sorted(data['forms'][phase])]}
    else:
        row['tight_phases'] = [{'phase':j,'forms':[list(c) for c in sorted(data['forms'][j])],
            'necessary_condition':'all 13 form evaluations pairwise distinct'} for j in tight]
    rows.append(row)
    if pattern['id'] in (414,1650):
        # A few basis substitutions calibrate the symbolic coefficients against
        # direct group multiplication. These are not legal-S candidates or a search.
        vcount = data['variable_count']
        assignments = [[0]*vcount]+[[int(i==j) for i in range(vcount)] for j in range(vcount)]
        checks = 0
        for value in assignments:
            for word,phase,coeff in data['words']:
                assert direct_word(p,mul,scalar,data['alphabet'],word,value) == (
                    sum(c*v for c,v in zip(coeff,value)) % p,phase)
                checks += 1
        calibration.append({'pattern_id':pattern['id'],'basis_substitutions':len(assignments),
                            'direct_group_word_checks':checks})
excluded = [row for row in rows if row['excluded']]
survivors = [row for row in rows if not row['excluded']]
assert len(rows) == 370 and len(excluded) == 358 and len(survivors) == 12
assert sum(row['projective_input_bound'] for row in rows) == 252258
assert sum(row['projective_input_bound'] for row in survivors) == 28560
result312 = {
    'status':'COMPLETE_SYMBOLIC_NECESSARY_BOUND_ONLY',
    'source_patterns':'QUOTIENT_CAPACITY.json survivors only; original phase-capacity program not rerun',
    'field':13,'phase_group':'C12 x C2','action':'2^j, fixes second factor',
    'patterns_checked':len(rows),'symbolically_excluded':len(excluded),'surviving_patterns':len(survivors),
    'projective_input_bound_before':252258,'projective_input_bound_after':28560,
    'projective_input_bound_excluded':223698,
    'surviving_pattern_ids':[row['pattern_id'] for row in survivors],
    'minimum_form_count_histogram':dict(sorted(Counter(row['minimum_distinct_forms'] for row in rows).items())),
    'rows':rows,'small_arithmetic_calibration':calibration,
    'actual_candidate_sets_enumerated':0,'graphs_built':0,'BFS_runs':0,
    'changes_to_completed_actual_production':False,
    'note':'An independent mathematical filter; all 12 surviving modes still require actual evaluation.',
    'cpu_seconds_including_272_analysis':time.process_time()-start}
analysis272['cpu_seconds_including_312_symbolic_filter'] = result312['cpu_seconds_including_272_analysis']
(here/'THREE_WORD_COLLISIONS.json').write_text(json.dumps(analysis272,indent=2)+'\n')
(other/'SYMBOLIC_WORD_BOUND.json').write_text(json.dumps(result312,indent=2)+'\n')
print(json.dumps({key:result312[key] for key in ['patterns_checked','symbolically_excluded',
    'surviving_patterns','projective_input_bound_before','projective_input_bound_after',
    'surviving_pattern_ids','cpu_seconds_including_272_analysis']},indent=2))
