import itertools,json,pathlib,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(2,3))
P=pathlib.Path(__file__).resolve().parent;start=time.process_time()
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
save('PREDICTION.json',{
 'prediction_id':'P_SMALL120_CAYLEY_D4','frozen_before_group_tables_or_endpoint_tests':True,
 'falsifiable_prediction':'At least one inverseclosed4-generator Cayleyset in S5 or SL2(F5) covers all120 identityroot endpoints within4 steps.',
 'target_Delta':4,'target_D':4,'savedL':104,'baseline_as_of':'2026-10-27','n':{'actual':None,'hypothetical':120},
 'groups':['S5','SL2(F5)'],'S5_expected_scope':27831,'SL2F5_expected_scope':1711,
 'sets_include_nongenerating_cases':True,'scope':'All inverseclosed subsets of4 distinct nonidentity group elements:4involutions;2involutions+1ordinaryinversepair;2ordinaryinversepairs. No conjugacy/orbit reduction.',
 'SL2_optional_diagnostic':'Count projected60 centralquotient classes fullyreached<=4 but120 endpointsnotfull;track whether central-I reached, no best badpair score.',
 'acceptance':'Onlyall120rootendpoints generate a full240edge graph; first newparameter gets one independent120graph check.',
 'CPU_budget_seconds':3,'compilation_separate':True,'workers':1,'no_MIP_externalreview_Lean_othergroups_localrepair':True,
 'ledger_lookup':'OldMobius108Schreier andQ8lift112 are different objects;no prior exact S5/SL2F5 degree4 D4 exhaustive scope found.'})
groups=[]
# Right Cayley edges g -> g*s. Multiplication p*q is permutation composition p after q.
elems=list(itertools.permutations(range(5)));ix={p:i for i,p in enumerate(elems)};identity=ix[tuple(range(5))]
table=[[ix[tuple(p[q[i]]for i in range(5))]for q in elems]for p in elems]
inv=[row.index(identity)for row in table]
parity=[sum(p[i]>p[j]for i in range(5)for j in range(i+1,5))%2 for p in elems]
groups.append({'name':'S5','elements':elems,'identity':identity,'central_minusI':-1,'table':table,'inverse':inv,'parity':parity,'quotient':[-1]*120,'operation':'(p*q)(i)=p(q(i)); Cayley arcs g->g*s'})
elems=[(a,b,c,d)for a,b,c,d in itertools.product(range(5),repeat=4)if(a*d-b*c)%5==1];ix={p:i for i,p in enumerate(elems)};identity=ix[(1,0,0,1)]
def mul(x,y):
 a,b,c,d=x;e,f,g,h=y
 return((a*e+b*g)%5,(a*f+b*h)%5,(c*e+d*g)%5,(c*f+d*h)%5)
table=[[ix[mul(p,q)]for q in elems]for p in elems];inv=[ix[(d,(-b)%5,(-c)%5,a)]for a,b,c,d in elems]
neg=[ix[tuple((-z)%5 for z in x)]for x in elems];canon=sorted({min(i,j)for i,j in enumerate(neg)});qid={x:i for i,x in enumerate(canon)};quotient=[qid[min(i,j)]for i,j in enumerate(neg)]
groups.append({'name':'SL2F5','elements':elems,'identity':identity,'central_minusI':ix[(4,0,0,4)],'table':table,'inverse':inv,'parity':[0]*120,'quotient':quotient,'operation':'2x2 matrix multiplication modulo5; Cayley arcs g->g*s'})
summary=[]
with(P/'group_tables.txt').open('w')as f:
 f.write('2\n')
 for g in groups:
  assert len(g['elements'])==120
  I=[i for i,j in enumerate(g['inverse'])if i==j and i!=g['identity']]
  R=[i for i,j in enumerate(g['inverse'])if i<j]
  n=len(I);k=len(R)
  summary.append({'name':g['name'],'order':120,'identity':g['identity'],'involutions':n,'ordinary_inversepairs':k,'scope_four_involutions':len(list(itertools.combinations(I,4))),'scope_two_involutions_onepair':n*(n-1)//2*k,'scope_two_pairs':k*(k-1)//2,'central_minusI':g['central_minusI'],'operation':g['operation']})
  f.write(f"{g['name']} 120 {g['identity']} {g['central_minusI']}\n")
  for name in ['inverse','parity','quotient']:f.write(' '.join(map(str,g[name]))+'\n')
  for row in g['table']:f.write(' '.join(map(str,row))+'\n')
assert summary[0]['involutions']==25 and summary[0]['ordinary_inversepairs']==47
assert summary[1]['involutions']==1 and summary[1]['ordinary_inversepairs']==59
save('GROUPS.json',{'groups':summary,'preparation_CPU_seconds':time.process_time()-start,'group_axioms_inherited_from_concrete_permutation_and_matrix_operations':True})
save('group_elements.json',{g['name']:{'operation':g['operation'],'identity':g['identity'],'central_minusI':g['central_minusI'],'elements':g['elements']}for g in groups})
print('GROUPS',summary,'prepCPU',time.process_time()-start)
