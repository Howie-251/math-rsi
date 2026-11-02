"""One finite raw NB-word capacity on the actual quotient; no graph BFS."""
from collections import Counter
from pathlib import Path
import json
import resource
import time

START=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(1,1))
OUT=Path(__file__).resolve().parent
recipe=json.loads((OUT.parent/'normal425_cover/COVER_RECIPE.json').read_text())
assert recipe['status']=='READY_ACTUAL_SOURCE_48_BASE_ABELIAN_VOLTAGE_RECIPE'
assert recipe['base_count']==48 and recipe['moduli']==[5,5,17]
ports=[b['darts'] for b in recipe['base_ports']]
assert recipe['base_ports'][0]['representative']==0
counts=[0]*816;bydepth=[[0]*816 for _ in range(8)]
word_count_by_depth=[0]*8

def visit(base,c,forbidden,depth):
    state=17*base+c
    counts[state]+=1;bydepth[depth][state]+=1;word_count_by_depth[depth]+=1
    if depth==7:return
    for p in ports[base]:
        if p['port']!=forbidden:
            visit(p['to'],(c+p['c17'])%17,p['reverse_port'],depth+1)

visit(0,0,-1,0)
assert word_count_by_depth==[1,6,30,150,750,3750,18750,93750]
assert sum(counts)==117187
minimum=min(counts)
witnesses=[{'state':s,'target_base':s//17,'c17':s%17,
            'raw_routes':counts[s],'routes_by_depth':[bydepth[d][s] for d in range(8)]}
           for s in range(816) if counts[s]==minimum]
result={'status':'COMPLETE_ONE_ROOT_RAW_NB_QUOTIENT_CAPACITY','source_recipe':str(OUT.parent/'normal425_cover/COVER_RECIPE.json'),
        'quotient_states':816,'quotient_encoding':'17*base+c17',
        'identityroot':{'base':0,'c17':0,'actual_base_representative':0},
        'normal_module_forgotten':'actualC5^2 order25','retained_coordinate':'c17',
        'NB_words_by_length':word_count_by_depth,'NB_words_total':117187,
        'count_histogram':dict(sorted(Counter(counts).items())),
        'minimum_K':minimum,'minimum_witnesses':witnesses,
        'original_fiber25_capacity_check':minimum>=25,
        'hypothetical_normal_F7_squared_fiber_size':49,
        'hypothetical_order':816*49,'q7_capacity_allowed':minimum>=49,
        'prediction_disposition':'SUPPORTED_NECESSARY_CAPACITY_ONLY' if minimum>=49 else 'REFUTED_Q7_CAPACITY_IMPOSSIBLE',
        'interpretation':'Every inverse-consistent six-step quotientcover endpoint has a nonbacktracking representativeword oflength<=7. Each suchword reaches atmostonefiberpoint fromafixedsource; hencefiberorder<=minimumK is necessary, regardlessofhowthemoduleliftsarechosen.',
        'scope_if_negative':'Any49pointfiber retaining these exactsixquotientsteps, includingF7^2; not arbitrarydegree6D7graphs, otherquotients, changedsteps or largergrouprepresentations.',
        'sufficient_for_cover':False,'actual_candidate_n':None,'actual_candidate_D':None,
        'ordinary_bad_unordered_pairs':None,'source_graph_parses':0,'graph_BFS':0,
        'group_or_module_search':False,'candidate_graphs':0,
        'CPU_seconds':time.process_time()-START,'running':False,'pending':[]}
(OUT/'COUNTS.json').write_text(json.dumps({'encoding':'17*base+c17','counts':counts,'by_depth':bydepth},indent=2)+'\n')
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
