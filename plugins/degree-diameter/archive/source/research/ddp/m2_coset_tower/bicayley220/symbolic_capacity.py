"""Complete marked phase/symbolic <=3 word bound; no graph or S enumeration."""
import json
import math
import time
from collections import Counter
from itertools import combinations_with_replacement
from pathlib import Path

start = time.process_time()
out = Path(__file__).resolve().parent
P, M, D = 11, 10, 7
pw = [pow(2,j,P) for j in range(M)]
assert len(set(pw)) == M and pw[5] == P-1
component_count = 7  # a,b,t1,...,t5; t0 is fixed identity.
projective_count = sum(P**i for i in range(6))
assert projective_count == 177156

def basis(i):
    return tuple(int(k==i) for k in range(component_count))

def analyze(phases):
    # 0=a, 1=b; then paired forward/reverse letters for all six matchings.
    alphabet = [dict(phase=5, coeff=basis(0), inverse=0, source=0, target=0),
                dict(phase=5, coeff=basis(1), inverse=1, source=1, target=1)]
    for i,j in enumerate(phases):
        coeff = (0,)*component_count if i==0 else basis(i+1)
        forward = len(alphabet)
        alphabet.append(dict(phase=j,coeff=coeff,inverse=forward+1,source=0,target=1))
        alphabet.append(dict(phase=-j % M,coeff=tuple(-pw[-j % M]*x % P for x in coeff),
                             inverse=forward,source=1,target=0))
    allowed = [[i for i,a in enumerate(alphabet) if a['source']==side] for side in range(2)]
    assert list(map(len,allowed)) == [D,D]
    conjugation = (2,2)+tuple((1-pw[j]) % P for j in phases[1:])
    root_data = []
    all_words = []
    for root in range(2):
        raw = [[0]*M for _ in range(2)]
        forms = [[{} for _ in range(M)] for _ in range(2)]
        words = [((),root,0,(0,)*component_count)]
        level = words
        for length in range(1,4):
            new = []
            for word,side,j,coeff in level:
                for letter in allowed[side]:
                    if word and letter == alphabet[word[-1]]['inverse']:
                        continue
                    item = alphabet[letter]
                    new.append((word+(letter,),item['target'],(j+item['phase']) % M,
                                tuple((x+pw[j]*y) % P for x,y in zip(coeff,item['coeff']))))
            assert len(new) == D*(D-1)**(length-1)
            words += new
            level = new
        assert len(words) == 302
        for word,side,j,coeff in words:
            raw[side][j] += 1
            forms[side][j].setdefault(coeff,word)
        assert sum(raw[root]) == 128 and sum(raw[1-root]) == 174
        normalized = [[{} for _ in range(M)] for _ in range(2)]
        for side in range(2):
            for j in range(M):
                for coeff,word in forms[side][j].items():
                    assert sum(c*t for c,t in zip(coeff,conjugation)) % P == (1-pw[j]) % P
                    normalized[side][j][coeff[1:]] = word
                assert len(normalized[side][j]) == len(forms[side][j])
        root_data.append({'raw':raw,'forms':normalized,
                          'counts':[[len(row) for row in side] for side in normalized]})
        all_words.append(words)
    return root_data, alphabet, all_words

patterns = list(combinations_with_replacement(range(M),5))
assert len(patterns) == math.comb(14,5) == 2002
rows = []
calibrations = []
first_raw_pass_calibrated = False
first_symbolic_pass_calibrated = False
for index,tail in enumerate(patterns):
    phases = (0,)+tail
    roots,alphabet,words = analyze(phases)
    raw_pass = all(n >= P for root in roots for side in root['raw'] for n in side)
    symbolic_pass = all(n >= P for root in roots for side in root['counts'] for n in side)
    assert not symbolic_pass or raw_pass
    row = {'id':index,'cross_phases':list(phases),
           'root_raw_counts': [r['raw'] for r in roots],
           'root_distinct_form_counts':[r['counts'] for r in roots],
           'minimum_raw_capacity':min(n for r in roots for side in r['raw'] for n in side),
           'minimum_symbolic_capacity':min(n for r in roots for side in r['counts'] for n in side),
           'raw_pass':raw_pass,'symbolic_pass':symbolic_pass,
           'projective_input_bound':projective_count if symbolic_pass else 0}
    if not symbolic_pass:
        root,side,phase = min(((root,side,j) for root in range(2) for side in range(2) for j in range(M)),
                              key=lambda cell:(len(roots[cell[0]]['forms'][cell[1]][cell[2]]),cell))
        f = roots[root]['forms'][side][phase]
        row['symbolic_witness'] = {'root':root,'target_layer':side,'target_phase':phase,
            'raw_count':roots[root]['raw'][side][phase],'form_count':len(f),
            'normalized_forms':[list(c) for c in sorted(f)]}
    else:
        row['tight_cells'] = [{'root':root,'target_layer':side,'target_phase':j,
            'normalized_forms':[list(c) for c in sorted(roots[root]['forms'][side][j])]}
            for root in range(2) for side in range(2) for j in range(M)
            if len(roots[root]['forms'][side][j]) == P]
    rows.append(row)
    do_calibration = index==0 or (raw_pass and not first_raw_pass_calibrated) or (
        symbolic_pass and not first_symbolic_pass_calibrated)
    if do_calibration:
        # Zero and basis substitutions check recursive coefficients against direct
        # scalar semidirect multiplication. No legal candidate graph is built.
        substitutions = [(0,)*component_count]+[basis(i) for i in range(component_count)]
        checks = 0
        for values in substitutions:
            for root in range(2):
                for word,target,j,coeff in words[root]:
                    x,phase,side = 0,0,root
                    for letter in word:
                        item = alphabet[letter]
                        assert side == item['source']
                        y = sum(c*v for c,v in zip(item['coeff'],values)) % P
                        x = (x+pw[phase]*y) % P
                        phase = (phase+item['phase']) % M
                        side = item['target']
                    assert (x,phase,side) == (sum(c*v for c,v in zip(coeff,values)) % P,j,target)
                    checks += 1
        calibrations.append({'pattern_id':index,'basis_substitutions':len(substitutions),
                             'direct_short_word_checks':checks})
        first_raw_pass_calibrated |= raw_pass
        first_symbolic_pass_calibrated |= symbolic_pass
raw_survivors = [row for row in rows if row['raw_pass']]
symbolic_survivors = [row for row in rows if row['symbolic_pass']]
for row in raw_survivors:
    phases = set(row['cross_phases'])
    assert len(phases) == 6
    assert sum(j in phases and j+5 in phases for j in range(5)) == 2
    assert row['root_distinct_form_counts'][0][0][0] == 9
result = {
    'status':'COMPLETE_TWO_ROOT_PHASE_AND_SYMBOLIC_NECESSARY_FILTER',
    'group':'F11 semidirect_2 C10','vertices_if_legal':220,'degree':7,'target_diameter':3,
    'marked_scope':'T0=identity; other five cross phases nondecreasing, with independent field slots',
    'internal_phases':[5,5],'patterns_checked':len(rows),
    'words_per_root_by_length':[1,7,42,252],'words_per_root_total':302,
    'same_layer_word_total':128,'other_layer_word_total':174,
    'capacity_target_per_cell':11,'cells_per_pattern':40,
    'raw_capacity_survivors':len(raw_survivors),'symbolic_capacity_survivors':len(symbolic_survivors),
    'raw_survivor_structure':{'distinct_cross_phases':6,'opposite_phase_pairs':2,
        'root0_same_layer_phase0_form_count':9,
        'short_bound':'identity plus at most four values per opposite pair: 1+4*2=9<11'},
    'projective_inputs_per_phase_pattern':projective_count,
    'input_bound_before_capacity':len(rows)*projective_count,
    'input_bound_after_raw_capacity':len(raw_survivors)*projective_count,
    'input_bound_after_symbolic_capacity':len(symbolic_survivors)*projective_count,
    'raw_survivor_ids':[r['id'] for r in raw_survivors],
    'symbolic_survivor_ids':[r['id'] for r in symbolic_survivors],
    'minimum_raw_capacity_histogram':dict(sorted(Counter(r['minimum_raw_capacity'] for r in rows).items())),
    'minimum_symbolic_capacity_histogram':dict(sorted(Counter(r['minimum_symbolic_capacity'] for r in rows).items())),
    'normalized_field_variable_order':['b_x','T1_x','T2_x','T3_x','T4_x','T5_x'],
    'anchor_projection_preserves_all_form_counts':True,'rows':rows,
    'small_arithmetic_calibrations':calibrations,
    'actual_generator_assignments_enumerated':0,'graphs_built':0,'BFS_runs':0,
    'CPU_seconds':time.process_time()-start}
(out/'SYMBOLIC_CAPACITY.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'surviving_patterns.json').write_text(json.dumps(symbolic_survivors,indent=2)+'\n')
print(json.dumps({key:result[key] for key in ['status','patterns_checked','raw_capacity_survivors',
    'symbolic_capacity_survivors','input_bound_before_capacity','input_bound_after_raw_capacity',
    'input_bound_after_symbolic_capacity','symbolic_survivor_ids','CPU_seconds']},indent=2))
