"""One literal degree/fiber/saturation profile; no graph BFS or search."""
from collections import Counter,defaultdict
from datetime import datetime,timezone
from html import unescape
from pathlib import Path
import json,re,time

P=Path(__file__).resolve().parent
START=time.process_time()
recipe=json.loads((P/'construction.json').read_text())
N=recipe['order']
assert (N,recipe['degree'],recipe['diameter'])==(6156,12,4)
adj=[[]for _ in range(N)]
blocks=Counter()
edgecount=loops=0
for line in (P/'source6156.edges').read_text().splitlines():
    if not line.strip()or line.lstrip().startswith('#'):continue
    u,v=map(int,line.split())
    assert 0<=u<N and 0<=v<N
    adj[u].append(v);adj[v].append(u);edgecount+=1;loops+=u==v
    blocks[tuple(sorted((u//81,v//81)))]+=1
degree=[len(row)for row in adj]
free=[v for v,d in enumerate(degree)if d<12]
(P/'degree12.u8.bin').write_bytes(bytes(degree))
(P/'free_ports.json').write_text(json.dumps({'source_n':N,'source_m':edgecount,'delta':12,'ports':free,
      'degrees':[degree[v]for v in free],'free_slots':[12-degree[v]for v in free]},indent=2)+'\n')
sat=Counter(sum(degree[w]==12 for w in row)for row in adj)
local=Counter(tuple(sorted(Counter(w//81 for w in row).values()))for row in adj)
c=recipe['construction']['controller']
va=c['symbols'][0]['voltages'];vb=c['symbols'][1]['voltages']
pa=c['symbols'][0]['perm'];pb=c['symbols'][1]['perm']
alpha=[19*pa[b]+(g+va[b])%19 for b in range(4)for g in range(19)]
beta=[19*pb[b]+(g+vb[b])%19 for b in range(4)for g in range(19)]
expected={tuple(sorted((v,w)))for f in [alpha,beta]for v,w in enumerate(f)}
actual={b for b in blocks if b[0]!=b[1]}
def permutation_order(f):
    from math import lcm
    visited=set();order=1
    for v in range(len(f)):
        if v in visited:continue
        u=v;n=0
        while u not in visited:visited.add(u);u=f[u];n+=1
        order=lcm(order,n)
    return order
result={'status':'ACTUAL6156_SOURCE_PROFILE_COMPLETE','source_n':N,'source_m':edgecount,
        'maximum_degree':max(degree),'degree_histogram':dict(sorted(Counter(degree).items())),
        'free_vertices':len(free),'free_slots':sum(12-d for d in degree),
        'saturated_neighbor_count_histogram':dict(sorted(sat.items())),
        'number_of_81_fibers':76,'intrafiber_edges':sum(v for(k,l),v in blocks.items()if k==l),
        'interfiber_quotient_edges':len(actual),'edges_per_nonempty_fiberpair_histogram':dict(sorted(Counter(blocks.values()).items())),
        'pervertex_neighbor_multiplicities_by_fiber':{str(k):v for k,v in local.items()},
        'actual_quotient_equals_recipe':actual==expected,
        'quotient_missing_recipe_edges':len(expected-actual),'quotient_extra_edges':len(actual-expected),
        'controller':{'type':'Z19 lift of4vertex Schreier base','alpha_base_perm':pa,'beta_base_perm':pb,
                      'va':va,'vb':vb,'alpha_order':permutation_order(alpha),'beta_order':permutation_order(beta),
                      'inverse_label_pairs':[['a','a^-1'],['b','b^-1']],
                      'four_controller_maps_are_involutions':False},
        'structure_prediction_verdict':'SUPPORTED_81FIBERS_AND_INVERSE_PAIRS',
        'spare_prediction_verdict':'SUPPORTED'if free else'REFUTED',
        'monotone_extension_scope':'No source pin available atcap12 when all6156vertices degree12. This excludes preserving alloldedges and attaching any connected newvertex/block to this fixedsource, not arbitrary6157graphs.',
        'source_D4_scope':'Inherited primary author graph; no source BFS repeated.',
        'R3_cover_search_started':False,'source_BFS':0,'graphs_generated':0,
        'actual_candidate_n':None,'actual_candidate_D':None,'ordinary_bad_unordered_pairs':None,
        'CPU_seconds':time.process_time()-START,'pending':[]}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'terminal.json').write_text(json.dumps({**result,'running':False},indent=2)+'\n')
# Retain exact primary-cell evidence, distinct from the stale descriptive page.
html=(P/'official_main.html').read_text()
cells=re.findall(r'<td\b[^>]*>.*?</td>',html,re.I|re.S)
chosen=[x for x in cells if re.sub(r'\D','',unescape(re.sub(r'<[^>]+>','',x)))=='6156']
assert len(chosen)==1
cell=chosen[0]
facts={'checked_UTC':datetime.now(timezone.utc).isoformat(),'official_main_url':'https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html',
       'delta':12,'D':4,'current_lower_bound':6156,'cell_html':cell,
       'marked_optimal_by_bold':bool(re.search(r'<(?:b|strong)\b',cell,re.I)),
       'description_url':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html',
       'description_contains6156':bool(re.search(r'6\s*156',(P/'official_desc_g4.html').read_text())),
       'description_old_d12_value':5832,
       'author_primary':'https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg12/dia4',
       'author_attribution':'Nishant Bhakar; current primary-table update listing and linked author repository.',
       'literal_file':'source6156.edges','recipe_file':'construction.json','source_gap':None}
(P/'SOURCE_FACTS.json').write_text(json.dumps(facts,indent=2)+'\n')
indexfile=P/'AUTHOR_RELEVANT_PATHS.json'
indexdata=json.loads(indexfile.read_text())
indexdata['matched_paths']=[x for x in indexdata['matched_paths']if 'graphs/deg12/dia4/'in x['path']or'6156'in x['path']]
indexfile.write_text(json.dumps(indexdata,indent=2)+'\n')
print(json.dumps(result,indent=2))
