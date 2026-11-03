"""Coefficient forms for words of length <=3 in F_p semidirect a finite phase group.

Pure symbolic routine: no field assignments, graph generation, or BFS.
phase 0 must be the identity. The caller supplies an already valid scalar action.
Each component has a distinct variable unless free_coordinate=False (fixed x=0).
"""


def affine_word_forms(p, phase_product, phase_inverse, scalar, components, length=3):
    """Return formal reduced words and coefficients, grouped by phase.

    components: [{phase: int, kind: 'pair'|'involution', free_coordinate: bool}].
    A pair adds its representative and actual inverse. An involution adds one
    self-inverse letter. Keep repeated phases as distinct components/variables.
    Fixed central involutions use free_coordinate=False, not a free variable.
    This implementation is for prime fields with coefficients reduced modulo p.
    """
    phase_count = len(scalar)
    assert scalar[0] == 1 and len(phase_product) == phase_count
    variable_count = sum(c.get('free_coordinate', True) for c in components)
    alphabet, component_variables = [], []
    variable = 0
    for component_index, component in enumerate(components):
        phase = component['phase']
        coeff = [0]*variable_count
        if component.get('free_coordinate', True):
            coeff[variable] = 1
            component_variables.append(variable)
            variable += 1
        else:
            component_variables.append(None)
        letter = len(alphabet)
        if component['kind'] == 'pair':
            inverse_phase = phase_inverse[phase]
            inverse_scalar = pow(scalar[phase], -1, p)
            alphabet.append({'phase':phase, 'coeff':tuple(coeff), 'inverse':letter+1,
                             'component':component_index, 'inverse_direction':False})
            alphabet.append({'phase':inverse_phase,
                             'coeff':tuple(-inverse_scalar*x % p for x in coeff),
                             'inverse':letter, 'component':component_index,
                             'inverse_direction':True})
        else:
            assert component['kind'] == 'involution'
            assert phase_inverse[phase] == phase
            assert all((1+scalar[phase])*x % p == 0 for x in coeff)
            alphabet.append({'phase':phase, 'coeff':tuple(coeff), 'inverse':letter,
                             'component':component_index, 'inverse_direction':False})
    words = [((), 0, (0,)*variable_count)]
    level = words
    for _ in range(length):
        new = []
        for word, phase, coeff in level:
            for letter, item in enumerate(alphabet):
                if word and letter == alphabet[word[-1]]['inverse']:
                    continue
                new.append((word+(letter,), phase_product[phase][item['phase']],
                            tuple((x+scalar[phase]*y) % p
                                  for x,y in zip(coeff,item['coeff']))))
        words += new
        level = new
    forms = [{} for _ in range(phase_count)]
    raw_counts = [0]*phase_count
    for word, phase, coeff in words:
        raw_counts[phase] += 1
        forms[phase].setdefault(coeff, []).append(word)
    return {'alphabet':alphabet, 'component_variables':component_variables,
            'variable_count':variable_count, 'words':words,
            'forms':forms, 'raw_counts':raw_counts,
            'form_counts':[len(row) for row in forms]}
