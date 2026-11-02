import json,time
from pathlib import Path
start=time.process_time();out=Path(__file__).parent
p=5;I=((1,0),(0,1));A=((1,1),(2,4));B=((0,4),(1,4))
def mm(X,Y):return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2))%5 for j in range(2)) for i in range(2))
def mp(X,n):
 r=I
 for _ in range(n):r=mm(r,X)
 return r
def mv(X,w):return tuple(sum(X[i][j]*w[j] for j in range(2))%5 for i in range(2))
rho=[[mm(mp(B,i),mp(A,m)) for m in range(8)] for i in range(3)]
def mul(g,h):
 a,b,i,j,m=g;aa,bb,ii,jj,nn=h;w=mv(rho[i][m],(aa,bb))
 return ((a+w[0])%5,(b+w[1])%5,(i+pow(2,m,3)*ii)%3,(j+pow(2,m,5)*jj)%5,(m+nn)%8)
def inv(g):
 a,b,i,j,m=g;n=-m%8;k=-pow(2,n,3)*i%3;w=mv(rho[k][n],(a,b))
 return (-w[0]%5,-w[1]%5,k,-pow(2,n,5)*j%5,n)
def qcode(g):a,b,i,j,m=g;return ((5*a+b)*3+i)*8+m
def qdecode(x):m=x%8;x//=8;i=x%3;x//=3;return (x//5,x%5,i,0,m)
E=(0,0,0,0,0);Y=(0,0,0,0,1);D=(0,2,1,4,4);P=(0,1,1,1,4);Q=(1,4,1,4,7)
positive=[('loop0',Y),('loop1',D),('identity_link',E),('linkP',P),('linkQ',Q)]
orders={}
for name,g in positive:
 z=E;n=0
 while True:
  n+=1;z=mul(z,g)
  if z==E:break
  assert n<=3000
 orders[name]=n
assert mp(A,2)==((3,0),(0,3)) and mp(A,8)==I
assert mm(A,B)==mm(mp(B,2),A)
# dart=(id,source_base,target_base,quotient_voltage,z-polynomial)
darts=[]
for idx,(sb,tb,g) in enumerate([(0,0,Y),(1,1,D),(0,1,E),(0,1,P),(0,1,Q)]):
 j=g[3];m=g[4];f=[0]*8;f[0]=j
 zinv=[0]*8;zinv[-m%8]=-j
 darts.append((2*idx,sb,tb,g,tuple(f)))
 darts.append((2*idx+1,tb,sb,inv(g),tuple(zinv)))
bybase=[[d for d in darts if d[1]==b] for b in range(2)]
assert [len(x) for x in bybase]==[5,5]
steps=[[] for _ in range(1200)]
for b in range(2):
 for qc in range(600):
  state=qdecode(qc);m=state[4]
  for di,sb,tb,g,f in bybase[b]:
   endpoint=mul(state,g);shift=tuple(f[(k-m)%8] for k in range(8))
   steps[600*b+qc].append((di,600*tb+qcode(endpoint),shift))
root_rows=[];formal_records=[];total_words=0
for rootbase in range(2):
 counts=[0]*1200;forms=[set() for _ in range(1200)];firstword=[None]*1200
 def dfs(state,last,depth,vec,word):
  global total_words
  counts[state]+=1;forms[state].add(vec);total_words+=1
  if firstword[state] is None:firstword[state]=word
  if depth==7:return
  for di,to,shift in steps[state]:
   if last>=0 and di==(last^1):continue
   dfs(to,di,depth+1,tuple(vec[k]+shift[k] for k in range(8)),word+[di])
 dfs(600*rootbase,-1,0,(0,)*8,[])
 assert sum(counts)==27306
 minraw=min(counts);minforms=min(map(len,forms));rawslot=counts.index(minraw);formslot=next(i for i,F in enumerate(forms) if len(F)==minforms)
 row={'root_base':rootbase,'word_count':sum(counts),'minimum_raw_words':minraw,'minimum_raw_slot':{'target_base':rawslot//600,'Q':list(qdecode(rawslot%600))},'minimum_formal_z_polynomials':minforms,'minimum_formal_slot':{'target_base':formslot//600,'Q':list(qdecode(formslot%600))},'formal_slot_coefficients':sorted(forms[formslot]),'raw_slot_count_histogram':{str(k):counts.count(k) for k in sorted(set(counts))},'formal_slot_count_histogram':{str(k):sum(len(s)==k for s in forms) for k in sorted(set(map(len,forms)))}}
 root_rows.append(row)
 formal_records.append({'root_base':rootbase,'slots':[{'target_base':i//600,'quotient_index':i%600,'raw_word_count':counts[i],'polynomial_forms':sorted(forms[i])} for i in range(1200)]})
K=min(r['minimum_raw_words'] for r in root_rows);KF=min(r['minimum_formal_z_polynomials'] for r in root_rows)
res={'status':'COMPLETE_TWO_ROOT_QUOTIENT_ROUTE_CAPACITY','source_order':6000,'group_order':3000,'quotient_without_z_order':600,'projected_graph_states':1200,'named_NB_words_per_root':27306,'total_named_words':total_words,'source_positive_voltage_orders':orders,'raw_route_capacity_min':K,'formal_z_capacity_min':KF,'formal_ring':'Z[r]/(r^8-1), coefficients with literal forward source z-exponents 1 or 4; inverse exponents use -r^(-m)*j','formal_scope':'A polynomial count is an upper bound on possible distinct cyclic endpoints for any compatible scalar action r^8=1. It is not an evaluated endpoint-coverage certificate.','prediction_thin_raw_less_than_13':'SUPPORTED' if K<13 else 'REFUTED','root_rows':root_rows,'CPU_seconds':time.process_time()-start,'source_BFS':0,'new_graphs':0,'candidate_modulus_evaluations':0}
(out/'CAPACITY_RESULT.json').write_text(json.dumps(res,indent=2)+'\n')
(out/'FORMAL_Z_POLYNOMIAL_SETS.json').write_text(json.dumps({'coefficient_order':'r^0 through r^7','roots':formal_records},separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='root_rows'}))
