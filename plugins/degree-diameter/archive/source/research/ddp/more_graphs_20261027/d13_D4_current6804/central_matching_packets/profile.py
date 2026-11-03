"""Actual 36 central-insertion packets and a phase-only capacity bound."""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import resource
import time

began = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (3, 3))
out = Path(__file__).resolve().parent
recipe = json.loads((out.parent/'construction.json').read_text())['construction']
charts = recipe['charts']
symbols = 'aAbBz'
inverse = [1,0,3,2,4]
vectors = [tuple(x//3**j%3 for j in range(4)) for x in range(81)]
relations = []
for chart in charts:
    rows = []
    for x in vectors:
        center = [sum(a*b for a,b in zip(row,x))%3 for row in chart['M']]
        if chart['kind'] == 'plain':
            rows.append({sum(((a+b)%3)*3**j for j,(a,b) in enumerate(zip(center,chart['d'])))})
        else:
            rows.append({sum(((a+k*b)%3)*3**j for j,(a,b) in enumerate(zip(center,chart['d']))) for k in range(3)})
    relations.append(rows)

words=[()] + [w for length in range(1,5) for w in product(range(5),repeat=length)]
images = {():{0}}
for word in words[1:]:
    table = relations[word[-1]]
    images[word] = set().union(*(table[y] for y in images[word[:-1]]))

def normal_and_residue(points):
    first = vectors[min(points)]
    choices = [n for n in vectors[1:] if all(sum(a*(b-c) for a,b,c in zip(n,vectors[y],first))%3==0 for y in points)]
    if len(choices)!=2:
        return None, None
    n = choices[0]
    scale = pow(next(x for x in n if x),-1,3)
    n = tuple(x*scale%3 for x in n)
    return n, sum(a*b for a,b in zip(n,first))%3

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4))%3 for j in range(4)] for i in range(4)]

def linear_part(word):
    result = [[int(i==j) for j in range(4)] for i in range(4)]
    for symbol in word:
        result = matmul(charts[symbol]['M'],result)
    return result

packets=[]
for word in product(range(4),repeat=3):
    if any(word[i]==inverse[word[i-1]] for i in range(1,3)):
        continue
    inserted = [word[:j]+(4,)+word[j:] for j in range(4)]
    reached = set().union(*(images[w] for w in inserted))
    normals_residues = [normal_and_residue(images[w]) for w in inserted]
    normals = [a for a,b in normals_residues]
    residues = [b for a,b in normals_residues]
    linear_parts = [linear_part(w) for w in inserted]
    common_linear = all(A==linear_parts[0] for A in linear_parts)
    assert common_linear
    packets.append({'line_word':''.join(symbols[s] for s in word),
                    'inserted_words':[''.join(symbols[s] for s in w) for w in inserted],
                    'image_sizes':[len(images[w]) for w in inserted],
                    'normal':normals[0] if all(n==normals[0] for n in normals) else None,
                    'normals':normals,'residues':residues,
                    'distinct_residue_count':len(set(residues)),
                    'zero_source_union_size':len(reached),
                    'all_sources_same_union_size_by_common_linear_part':common_linear,
                    'common_linear_part':linear_parts[0],
                    'all_sources_union_full':len(reached)==81})

phase_steps = [1,-1,4,-4,6]
phase_upper = [0]*12
phase_word_count = [0]*12
for word in words:
    phase = sum(phase_steps[s] for s in word)%12
    phase_upper[phase] += len(images[word])
    phase_word_count[phase] += 1

result = {
 'status':'COMPLETE_PACKET_PROFILE_AND_MOD8_OBSTRUCTION',
 'packets':packets,'packet_count':len(packets),
 'packet_union_size_histogram':dict(Counter(p['zero_source_union_size'] for p in packets)),
 'full_packets':[p['line_word'] for p in packets if p['all_sources_union_full']],
 'full_packet_count':sum(p['all_sources_union_full'] for p in packets),
 'prediction_disposition':'SUPPORTED' if any(p['all_sources_union_full'] for p in packets) else 'REFUTED',
 'tiling_principle_status':'Inherited explicitly from primary author search README; not a new theorem.',
 'all_source_extension':'Insertion of scalar linear part -I at any position gives the same total linear matrix -M_word; therefore every zero-source union is translated by a common vector for any source.',
 'capacity_word_scope':'All781 words of length0..4 including backtracking over a,A,b,B,z. Each term is exact individual route image cardinality; their sum is a safe upper bound, not an assertion of distinct endpoints.',
 'phase_steps':phase_steps,'phase_word_counts':phase_word_count,
 'phase_image_cardinality_sum_upper_bound':phase_upper,
 'minimum_phase_capacity_upper_bound':min(phase_upper),
 'module8_required_points_per_phase':648,
 'phase_bound_excludes_module8':min(phase_upper)<648,
 'mod8_uniform_obstruction':{'character':'chi(i,j)=i-j mod2','reason':'Every unit r modulo8 is odd; (i,j)(k,l)=(i+r^j k,j+l) preserves chi additively. Fixed a=(1,1),b=(0,4),z=(0,6) all havechi0.','at_most_controller_vertices_in_generated_component':48,'controller_order':96,'unreachable_condition':'i not congruent j modulo2','applies_to':'All valid odd-unit actions on C8 retaining these literal generator coordinates, including3,5,7.','graph_consequence':'Disconnected; no7776-point D4 graph can arise from this unchanged recipe.'},
 'CPU_seconds':time.process_time()-began,
 'graph_generated':False,'BFS':0,'action_sweep_executed':False,'running':False,'pending':[]}
assert len(packets)==36 and len(words)==781
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps({k:v for k,v in result.items() if k!='packets'},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='packets'},indent=2))
