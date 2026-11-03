"""Export the successful literal controller and check the saved witness interface.

This does not search, generate a fiber graph, or perform BFS.
"""
import csv
import json
from pathlib import Path
import time

scope = Path(__file__).resolve().parent
started = time.process_time()
result = json.loads((scope/'SEARCH_RESULT.json').read_text())
assert result['status'] == 'WITNESS_PASS'
a0,a1,a2,s,t,h = result['solution_parameters']
inverse = [1,0,3,2,4,5]
rows = list(csv.DictReader((scope/'controller78.porttable.tsv').open(), delimiter='\t'))
names = ['a_plus','a_minus','b_plus','b_minus','s','t']
table = [[int(row[key]) for key in names] for row in rows]
assert [int(row['vertex']) for row in rows] == list(range(78))

# Explicit equations independent of the searcher's coefficient-step implementation.
for v in range(78):
    c,g = divmod(v,26)
    if c == 0:
        expected = [(0,g+a0),(0,g-a0),(1,g),(2,g),(1,g+s),(2,g+t)]
    elif c == 1:
        expected = [(2,g+a1),(2,g-a2),(2,g),(0,g),(0,g-s),(1,g+h)]
    else:
        expected = [(1,g+a2),(1,g-a1),(0,g),(1,g),(2,g+h),(0,g-t)]
    assert table[v] == [26*d+k%26 for d,k in expected]
    assert len(set(table[v])) == 6 and v not in table[v]
    assert all(table[u][inverse[p]] == v for p,u in enumerate(table[v]))
    assert table[table[table[v][2]][2]][2] == v
edges = [tuple(map(int,line.split())) for line in (scope/'controller78.edges').read_text().splitlines()]
assert len(edges) == len(set(edges)) == 234
assert set(edges) == {(v,u) for v in range(78) for u in table[v] if v < u}
witnesses = list(csv.DictReader((scope/'THREE_PORT_WITNESSES.tsv').open(),delimiter='\t'))
assert len(witnesses) == 234
assert {(int(w['root_base']),int(w['target_vertex'])) for w in witnesses} == {(c,v) for c in range(3) for v in range(78)}
nb_count = 0
adj_count = 0
route_rows = []
for w in witnesses:
    c,v = int(w['root_base']),int(w['target_vertex'])
    word = [int(w[f'p{k}']) for k in range(3)]
    nb = word[1] != inverse[word[0]] and word[2] != inverse[word[1]]
    adjacent = v in table[26*c]
    assert adjacent or nb
    adj_count += adjacent
    nb_count += nb
    path = [26*c]
    for p in word: path.append(table[path[-1]][p])
    assert path[1:] == [int(w[f'v{k}']) for k in (1,2,3)]
    assert path[-1] == v
    for shift in range(26):
        u = 26*c+shift
        for p in word: u = table[u][p]
        assert u == 26*(v//26)+(v%26+shift)%26
    route_rows.append({'root_base':c,'target_vertex':v,'ports':word,'vertices':path,
                       'adjacent_layers':adjacent,'nonbacktracking':nb})
parameters = {
    'status':'ACTUAL_CONTROLLER_WITNESS_PASS',
    'controller_order':78,'controller_degree':6,'controller_edges':234,
    'deck_modulus':26,'base_vertices':3,'vertex_label':'26*c+g',
    'ports':names,'inverse_ports':inverse,
    'alpha0':a0,'alpha1':a1,'alpha2':a2,'sigma':s,'tau':t,'self_matching_shift':h,
    'controller':table,
    'controller_framework_author':'Bhakar, author repository f4t4nt/degree-diameter-graphs',
    'framework_source':'../../f7_c60_d35/PARAMETERS.json',
    'original_author_source':'research/ddp/more_graphs_20261027/d15_D3_current1620_source/construction.author.json',
    'inherited_framework':'Three-base Schreier (a,b,s), a base permutation [0,2,1], b base permutation [1,2,0] and zero voltages; not an invention of general Schreier lifts.',
    'current_change':'Fixed m26, new parameters (2,6,17,5), and explicit sixth matching t with tau10.',
    'edge_file':'controller78.edges','porttable_file':'controller78.porttable.tsv',
    'route_certificate_file':'CONTROLLER_ROUTE_CERTIFICATE.json',
    'route_witness_tsv':'THREE_PORT_WITNESSES.tsv',
    'route_interface':'A^3 positive on all6084 ordered pairs; 234 deck classes with literal three-port witnesses. Same/nonadjacent classes have NB3; adjacent classes use inherited F9 pencil.',
    'field_interface':'../r6_f9_projective_halves/cross_port_extension/PARAMETERS.json',
    'conditional_target':{'field':9,'fiber_dimension':3,'fiber_size':729,'order':56862,'degree':54,'expected_edges':1535274},
    'public_degree54_best_located':55350,
    'fiber_graphs_generated_here':0,'global_record_claim':False,'Lean_completed_here':False,
}
(scope/'PARAMETERS.json').write_text(json.dumps(parameters,ensure_ascii=False,indent=2)+'\n')
(scope/'CONTROLLER_ROUTE_CERTIFICATE.json').write_text(json.dumps({
    'controller_order':78,'base_roots':[0,26,52],'deck_modulus':26,
    'classes':234,'all_ordered_pairs':6084,'adjacent_classes':adj_count,
    'nonadjacent_including_diagonal_classes':234-adj_count,
    'saved_witnesses_nonbacktracking':nb_count,'witnesses':route_rows,
},ensure_ascii=False,indent=2)+'\n')
terminal = json.loads((scope/'TERMINAL.json').read_text())
export_cpu = time.process_time()-started
terminal['literal_export_equation_and_witness_check_cpu_seconds'] = export_cpu
terminal['total_cpu_seconds'] += export_cpu
terminal['total_cpu_includes'] = ['driver/preparation','C++ compile','exact lex search','C++ artifact export and actual checks','Python literal equation/edge/route export checks']
terminal['literal_checks'] = {'explicit_recipe_binding':True,'simple_6regular':True,'true_inverse_ports':True,
    'edge_count':234,'all_points_have_b_triangle':True,'actual_route_classes':234,
    'actual_translated_ordered_pairs':6084,'adjacent_classes':adj_count,
    'same_nonadjacent_NB3_classes':234-adj_count,'fiber_graphs':0,'BFS':0,'solver':0,'Lean':0}
assert terminal['total_cpu_seconds'] < 10
(scope/'TERMINAL.json').write_text(json.dumps(terminal,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'LITERAL_EXPORT_PASS','total_cpu_seconds':terminal['total_cpu_seconds'],
    'adjacent_classes':adj_count,'same_nonadjacent_NB3_classes':234-adj_count,
    'saved_NB_witnesses':nb_count},ensure_ascii=False))
