import json,pathlib,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(14,15))
start=time.process_time();P=pathlib.Path(__file__).resolve().parent

def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
gauge={
 'operation':'(a,b)*(c,d)=(a+r^b*c,b+d); right voltage multiplication',
 'parent_source':'../SOURCE.json','source_graph_loaded_or_reverified':False,
 'common_inner_conjugation':'Conjugating by (c,0) changes translation a of phase b by c*(1-r^b). Since r^4=r!=1, choose c to make A1 translation0.',
 'side_gauge':'Old B_h becomes new B_(h*S0^-1); crossT becomes T*S0^-1, firstcross=e; B-internalg becomes S0*g*S0^-1; A unchanged.',
 'normalized_phase_pattern':{'internal_A':[4,3],'internal_B':[1,6],'cross_A_to_B':[0,4,1]},
 'normalized_voltages':{'A1':[0,4],'A2':['u',3],'B1':['v',1],'B2':['w',6],'T0':[0,0],'T1':['s',4],'T2':['t',1]},
 'free_variable_order':['u','v','w','s','t'],
 'normalization_scope':'All5 free translations after valid common and side coordinate changes; nonzero scalar multiplication yields projective representatives. Possible isomorphic duplicates remain.',
 'connectedness':'Pure phase4 generates C9 on A; identity cross transfers it to B. Any nonzero free translation voltage compared to its pure phase gives nonzero additive F43 translation; hence all nonzero tuples connected. Allzero disconnected.',
 'simplicity_and_degree':'Internal inverse phases distinct/nonzero; each side has four internal arcs. Three cross phases0,4,1 distinct; even cross identity connects different types. Degree7 throughout.',
 'projective_charts':[{'first_nonzero_index':i,'cases':43**(4-i)} for i in range(5)],
 'cases_per_action':sum(43**i for i in range(5)),'actions':[6,36],'total_scope':2*sum(43**i for i in range(5))}
pred={
 'prediction_id':'P_MICHEL43_PROJECTIVE_THIN_CROSS','frozen_before_capacity_and_native_profile':True,
 'falsifiable_prediction':'At least one normalized projective parameter among7,000,402 fully covers the minimum-freeform-capacity cross-side slot selected deterministically for its action. Full36-slot coverage is tested separately.',
 'target_Delta':7,'target_D':4,'savedL':684,'n':{'actual':None,'hypothetical':774},
 'p':43,'quotient':9,'actions':[6,36],'action_orders':[3,3],
 'free_variable_order':['u','v','w','s','t'],'cases_per_action':3500201,'normalized_scope':7000402,
 'thin_slot_rule':'Among cross-side slots, minimum distinct5-variable endpoint forms; ties lex(root,target_side,phase). Only full thin-slot cases evaluate the other35 slots, ordered by capacity and then lex.',
 'profile_gate':'Exactly first1000 supported projective cases once; complete remainder only if projected native plus capacity CPU<=15seconds. Profile range is not replayed. Otherwise mark partial/UNKNOWN without widening.',
 'acceptance':'Both orbit roots must cover all774 endpoints in<=4; only such full hits get edges and a first independent check.',
 'no_other_phase_prime_seed_MIP_or_badscore':True,'workers':1,'CPU_budget_seconds':15}
save('GAUGE.json',gauge);save('PREDICTION.json',pred)
phase=[4,3,1,6,0,4,1];origin=[0,0,1,1,0,0,0];dest=[0,0,1,1,1,1,1]
variable=[None,0,1,2,None,3,4]
actions=[];allcoeff=[]
for r in [6,36]:
 arcs=[[] for _ in range(2)]
 for j,b in enumerate(phase):
  vec=[0]*5
  if variable[j] is not None:vec[variable[j]]=1
  inv=[(-pow(r,(-b)%9,43)*a)%43 for a in vec]
  arcs[origin[j]].append((2*j,dest[j],b,tuple(vec)))
  arcs[dest[j]].append((2*j+1,origin[j],(-b)%9,tuple(inv)))
 sets=[];rows=[]
 for root in range(2):
  slots=[[set() for _ in range(9)]for _ in range(2)];slots[root][0].add((0,)*5)
  front=[(root,0,(0,)*5,-1)];counts=[1]
  for length in range(1,5):
   nxt=[]
   for side,b,vec,prev in front:
    for label,side2,d,w in arcs[side]:
     if prev>=0 and label==(prev^1):continue
     val=tuple((x+pow(r,b,43)*y)%43 for x,y in zip(vec,w));ph=(b+d)%9
     slots[side2][ph].add(val);nxt.append((side2,ph,val,label))
   front=nxt;counts.append(len(front))
  assert counts==[1,7,42,252,1512]
  for side in range(2):
   for ph in range(9):
    idx=root*18+side*9+ph;sets.append(sorted(slots[side][ph]));rows.append({'slot':idx,'root':root,'target_side':side,'phase':ph,'capacity':len(slots[side][ph])})
 failed=[x for x in rows if x['capacity']<43]
 thin=min((x for x in rows if x['root']!=x['target_side']),key=lambda x:(x['capacity'],x['root'],x['target_side'],x['phase']))
 order=[thin['slot']]+[x['slot']for x in sorted(rows,key=lambda x:(x['capacity'],x['root'],x['target_side'],x['phase'])) if x['slot']!=thin['slot']]
 actions.append({'r':r,'all36_slots':rows,'minimum_capacity':min(x['capacity']for x in rows),'thin_cross_slot':thin,'evaluation_order':order,'capacity_failed_slots':failed,'status':'CAPACITY_REJECTED'if failed else'CAPACITY_PASSED'})
 allcoeff.append((r,sets,order))
with(P/'coefficients.txt').open('w')as f:
 f.write('2\n')
 for r,sets,order in allcoeff:
  f.write(str(r)+'\n'+' '.join(map(str,order))+'\n')
  for vals in sets:
   f.write(str(len(vals))+'\n')
   for row in vals:f.write(' '.join(map(str,row))+'\n')
save('CAPACITY.json',{'status':'COMPLETE_GAUGED_FIVE_VARIABLE_CAPACITY','actions':actions,'capacity_CPU_seconds':time.process_time()-start,'source_BFS':0,'source_reverified':False})
print([(a['r'],a['minimum_capacity'],a['thin_cross_slot'])for a in actions]);print('capacityCPU',time.process_time()-start)
