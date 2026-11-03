"""Source route diagnosis only: reduced words, not graph/BFS reconstruction."""
import collections,json,pathlib,time
P=pathlib.Path(__file__).resolve().parent;start=time.process_time()
PH=[1,3,6,7,9]
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def order(r,p):
 for d in range(1,36):
  if pow(r,d,p)==1:return d
 return None
source={'status':'EXACT_PUBLIC_SOURCE_COORDINATES_RECOVERED','target':[10,4],'savedL':2485,'source_order':2485,'source_group':{'quotient':35,'field':71,'action':2,'action_order':order(2,71)},'operation':'(i,x)*(j,y)=(i+j mod35,x*r^j+y modp); Cayley arcs right multiply.',
 'original_positive_generators':[[18,57],[12,66],[29,12],[33,22],[14,27]],
 'inverse':'(i,x)^-1=(-i,-x*r^(-i))',
 'phase_normalization':{'new_phase':'18*old_phase mod35','new_action':'old_action^2=4 mod71','positive_generators_after_inverse_choices':[[1,54],[3,13],[6,66],[7,27],[9,57]],'original_generator_order_and_inverse_choices':['old4 inverse','old3 inverse','old2','old5','old1']},
 'source_provenance':['context/DD_PORTFOLIO_START_20261026/baselines/generator_specs.json','context/DD_PORTFOLIO_START_20261026/tools/reproduce_known_cayley.py','research/ddp/m1_sources/desc_g4.html'],
 'official_url':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html','credit':'Dharunish Yugeswardeenoo, August17 2026; official labelDahr_2485.',
 'old_source_all_BFS_evidence':'context/DD_PORTFOLIO_START_20261026/validation/baseline_verification.json','old_edges_loaded':False,'old_source_BFS_repeated':False,
 'frozen_analysis_object':'Keep quotient35 and five inversepair phases1/3/6/7/9. Compare all<=4 reducedword endpoint forms by phase; actual source used only for route multiplicity analysis.'}
if __name__=='__main__':save('SOURCE.json',source)

def route_forms(p,r,source_values=None,m=35):
 arcs=[]
 for j,ph in enumerate(PH):
  v=[0]*4
  if j:v[j-1]=1
  arcs.append((ph,tuple(v)));arcs.append(((-ph)%m,tuple((-pow(r,(-ph)%m,p)*x)%p for x in v)))
 forms=[set()for _ in range(m)];bylen=[[0]*m for _ in range(5)];multip=[collections.Counter()for _ in range(m)]
 short=[set()for _ in range(m)];words_by_length=[1]
 front=[(0,(0,)*4,-1,())];forms[0].add((0,)*4);bylen[0][0]=1
 if source_values is not None:multip[0][0]=1;short[0].add(0)
 for length in range(1,5):
  nxt=[]
  for ph,v,prev,word in front:
   for j,(d,w)in enumerate(arcs):
    if prev>=0 and j==(prev^1):continue
    co=tuple((x*pow(r,d,p)+y)%p for x,y in zip(v,w));h=(ph+d)%m
    forms[h].add(co);bylen[length][h]+=1;nxt.append((h,co,j,word+(j,)))
    if source_values is not None:
     e=sum(x*y for x,y in zip(co,source_values))%p;multip[h][e]+=1
     if length<=3:short[h].add(e)
  front=nxt;words_by_length.append(len(front))
 rows=[]
 for ph in range(m):
  a={'phase':ph,'raw_words_by_length':[row[ph]for row in bylen],'raw_words_total':sum(row[ph]for row in bylen),'distinct_free4_forms':len(forms[ph])}
  if source_values is not None:
   m=multip[ph];a.update({'source_endpoint_coverage':len(m),'source_short_le3_coverage':len(short[ph]),'source_requires_length4_endpoints':p-len(short[ph]),'source_min_word_multiplicity':min(m.values()),'source_single_route_endpoints':[x for x in range(p)if m[x]==1],'source_endpoint_multiplicity_histogram':dict(sorted(collections.Counter(m.values()).items()))})
  rows.append(a)
 return rows,forms,words_by_length
if __name__=='__main__':
 r=4;p=71;c=18
 original=[54,13,66,27,57]
 norm=[(a+c*(1-pow(r,ph,p)))%p for a,ph in zip(original,PH)]
 assert norm[0]==0
 rows,forms,counts=route_forms(p,r,norm[1:])
 result={'status':'SOURCE_PHASE_DIAGNOSIS_COMPLETE','p':p,'r':r,'normalized_phases':PH,'common_conjugating_c':c,'conjugated_translations':norm,'source_values_free4':norm[1:],'reduced_words_by_length':counts,'phase_rows':rows,
  'minimum_freeform_capacity':min(x['distinct_free4_forms']for x in rows),'minimum_form_phases':[x['phase']for x in rows if x['distinct_free4_forms']==min(y['distinct_free4_forms']for y in rows)],
  'minimum_raw_word_count':min(x['raw_words_total']for x in rows),'minimum_raw_word_phases':[x['phase']for x in rows if x['raw_words_total']==min(y['raw_words_total']for y in rows)],
  'source_total_short_le3_reached':sum(x['source_short_le3_coverage']for x in rows),'old_source_BFS_repeated':False,'CPU_seconds':time.process_time()-start}
 save('SOURCE_PHASES.json',result)
 print('SOURCE norm',norm,'minimum forms',result['minimum_freeform_capacity'],result['minimum_form_phases'],'rawmin',result['minimum_raw_word_count'],result['minimum_raw_word_phases'],'CPU',result['CPU_seconds'])
 print('THIN',sorted(rows,key=lambda x:x['distinct_free4_forms'])[:5])
