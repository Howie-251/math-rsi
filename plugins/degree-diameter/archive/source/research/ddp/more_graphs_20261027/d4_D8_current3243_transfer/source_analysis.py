from pathlib import Path
from collections import Counter
import json,time
P=Path(__file__).resolve().parent
start=time.process_time()
m,p,r=23,47,6
rows=[[int(x)-1 for x in line.split()] for line in (P/'source3243.raw_adj.txt').read_text().splitlines() if line.strip()]
adj=[line[1:] for line in rows]
r139=next(a for a in range(2,139) if pow(a,23,139)==1)
proposal={'status':'PROPOSAL_FROZEN_BEFORE_SOURCE_PHASE_COUNT','target_Delta':4,'target_D':9,'savedL':7884,
 'hypothetical_n':9591,'source_n':3243,'rule':'3-base identical voltage topology; change F47 to F139, keep quotient23, least primitive23 root, retain centered literal offsets.',
 'p':139,'r':r139,'loops':[[3,8],[11,2],[6,-12]],'cross_1_to_2':[4,-2],
 'identity_links':[[0,1],[0,2]],'prediction':'Provided raw phase capacity is at least139, this one controlled literal lift will cover all9591 vertices within9 steps from each of the three base identity roots.',
 'why':'Every nonidentity voltage retains order23; only one extra diameter step while field grows47 to139, less than branching factor3. This is a proposed falsifiable control, not an author-established general formula.',
 'state':'NOT_GENERATED_OR_NUMERICALLY_EVALUATED; parent decision required before any candidate run'}
(P/'PREDICTION_PROPOSAL.json').write_text(json.dumps(proposal,indent=2)+'\n')
def inv(g):
 a,b=g
 return (-a)%m,(-pow(r,(-a)%m,p)*b)%p
darts=[(0,0,(3,8)),(0,0,inv((3,8))),(1,1,(11,2)),(1,1,inv((11,2))),(2,2,(6,35)),(2,2,inv((6,35))),(0,1,(0,0)),(1,0,(0,0)),(0,2,(0,0)),(2,0,(0,0)),(1,2,(4,45)),(2,1,inv((4,45)))]
reverse=[1,0,3,2,5,4,7,6,9,8,11,10]
ports=[[i for i,d in enumerate(darts) if d[0]==b] for b in range(3)]
assert [len(x) for x in ports]==[4]*3
checked=0
for b in range(3):
 for y in range(p):
  for x in range(m):
   u=b*m*p+x+m*y
   expected=[]
   for di in ports[b]:
    _,to,(a,c)=darts[di]
    expected.append(to*m*p+(x+a)%m+m*((y+pow(r,x,p)*c)%p))
   assert sorted(expected)==sorted(adj[u]),(u,expected,adj[u])
   checked+=4
assert checked==12972
assert pow(r,m,p)==1 and r!=1
counts=[];witness=None
for root in range(3):
 totals=Counter({(root,0):1});state={(root,0,-1):1}
 for depth in range(1,10):
  nxt=Counter()
  for (b,phase,last),c in state.items():
   for di in ports[b]:
    if last>=0 and di==reverse[last]:continue
    _,to,g=darts[di]
    key=(to,(phase+g[0])%m,di)
    nxt[key]+=c
  state=nxt
  for (b,phase,last),c in state.items():totals[b,phase]+=c
 vals=[{'target_base':b,'phase':phase,'words':totals[b,phase]} for b in range(3) for phase in range(m)]
 low=min(v['words'] for v in vals)
 counts.append({'root_base':root,'total_NB_words_le9':sum(totals.values()),'minimum_words':low,
 'minimum_slots':[v for v in vals if v['words']==low],'slots':vals})
 assert sum(totals.values())==39365
comm=((pow(r139,3,139)-1)*2-(pow(r139,11,139)-1)*8)%139
facts={'status':'ACTUAL_LITERAL_AND_EXACT_VOLTAGE_RECIPE_RECOVERED','source_n':3243,'source_m':6486,
 'degree_histogram':{'4':3243},'source_bytes':(P/'source3243.raw_adj.txt').stat().st_size,
 'published_D_inherited':8,'source_BFS':0,'recipe_arcs_checked':checked,'all_source_arcs_match':True,
 'authors':'Eyal Loz, communicated July2006; official verifier reports Aut C47:C23 order1081, not Cayley/not vertex-transitive.',
 'description_URL':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g8.html',
 'literal_URL':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD8/Loz_3243.txt',
 'verifier_URL':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD8/3243_loz_SageMath.txt',
 'base_vertices':3,'deck_group_order':1081,'group':'F47 semidirect C23, multiplier6 of exactorder23',
 'right_multiplication':'(x,y)*(a,c)=(x+a mod23,y+6^x*c mod47)',
 'zero_based_vertex_encoding':'base*1081+x+23*y',
 'darts':[{'id':i,'from':d[0],'to':d[1],'phase':d[2][0],'translation':d[2][1],'reverse':reverse[i]} for i,d in enumerate(darts)],
 'voltage_orders_positive':{'loop0':23,'loop1':23,'loop2':23,'cross12':23},
 'deck_cover_proof':'All actual arcs match the right voltage recipe; left group translations preserve adjacency and act regularly on each base fibre. The literal three contiguous blocks are deck orbits.',
 'raw_phase_minimum_le9':min(x['minimum_words'] for x in counts),'proposed_field139_capacity_pass':min(x['minimum_words'] for x in counts)>=139,
 'least_primitive23_root_mod139':r139,'proposed_loop01_commutator_translation':comm,
 'candidate_generated':False,'candidate_BFS':0,'actual_new_n':None,'actual_new_D':None,'ordinary_bad_unordered_pairs':None,
 'CPU_seconds':time.process_time()-start}
(P/'SOURCE_FACTS.json').write_text(json.dumps(facts,indent=2)+'\n')
(P/'PHASE_RAW_COUNTS.json').write_text(json.dumps({'scope':'Fixed3-base phase quotient, all nonbacktracking words of length<=9, no field endpoint evaluation.','roots':counts,'source_BFS':0,'candidate_BFS':0},indent=2)+'\n')
(P/'RESULT.json').write_text(json.dumps({'status':'SOURCE_AND_PHASE_CAPACITY_RECOVERED_PARENT_DECISION_PENDING','source_n':3243,'source_m':6486,'min_raw':facts['raw_phase_minimum_le9'],'p139_capacity_pass':facts['proposed_field139_capacity_pass'],'proposed_r139':r139,'commutator_nonzero':comm!=0,'source_BFS':0,'candidate_generated':False,'CPU_seconds':facts['CPU_seconds']},indent=2)+'\n')
print(json.dumps({k:facts[k] for k in ['all_source_arcs_match','recipe_arcs_checked','raw_phase_minimum_le9','proposed_field139_capacity_pass','least_primitive23_root_mod139','proposed_loop01_commutator_translation','CPU_seconds']},indent=2))
print(json.dumps([{'root':x['root_base'],'min':x['minimum_words'],'witness':x['minimum_slots'][0]} for x in counts]))
