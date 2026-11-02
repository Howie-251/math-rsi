from pathlib import Path
import json,itertools,time
P=Path(__file__).parent;start=time.process_time();rec=json.loads((P.parent/'construction.json').read_text())['construction']
charts={t['symbol']:t for t in rec['charts']};names=['a','a^-1','b','b^-1'];label=['a','A','b','B']
M=[charts[s]['M'] for s in names];D=[charts[s]['d'] for s in names];c=charts['p']['d'];I2=(1,0,0,1)
def mm2(X,Y):return tuple(sum(X[2*i+k]*Y[2*k+j] for k in range(2))%3 for i in range(2) for j in range(2))
def inv2(X):a,b,c,d=X;return (d,-b%3,-c%3,a)
Xa=(0,1,2,2);Xb=(0,1,2,1);xs=[Xa,inv2(Xa),Xb,inv2(Xb)];ph=[1,-1,2,-2]
def mv(A,v):return tuple(sum(A[i][j]*v[j] for j in range(4))%3 for i in range(4))
def rank(cols):
 basis=[]
 for v in cols:
  v=list(v)
  for j,w in basis:
   k=v[j]
   v=[(a-k*b)%3 for a,b in zip(v,w)]
  if any(v):
   j=next(i for i,x in enumerate(v) if x);inv=1 if v[j]==1 else 2;v=[x*inv%3 for x in v];basis.append((j,v));basis.sort()
 return len(basis)
def route(word):
 cols=[];X=I2;z=0
 for s in word:
  cols=[mv(M[s],v) for v in cols]+[tuple(D[s])];X=mm2(X,xs[s]);z+=ph[s]
 return X,z,cols
normals=[]
for v in itertools.product(range(3),repeat=4):
 if any(v) and next(x for x in v if x)==1:normals.append(v)
good4=[];rankhist={}
for word in itertools.product(range(4),repeat=4):
 X,z,col=route(word);r=rank(col);rankhist[str(r)]=rankhist.get(str(r),0)+1
 if r==4:good4.append({'word':''.join(label[i] for i in word),'X':X,'integer_phase':z})
packets=[]
for word in itertools.product(range(4),repeat=3):
 X,z,col=route(word);r=rank(col)
 if r!=3:continue
 n=next(n for n in normals if all(sum(a*b for a,b in zip(n,v))%3==0 for v in col))
 offsets=[]
 for j in range(4):
  v=tuple(c)
  for s in word[j:]:v=mv(M[s],v)
  offsets.append(v)
 cls=[sum(a*b for a,b in zip(n,v))%3 for v in offsets]
 packets.append({'word':''.join(label[i] for i in word),'X':X,'integer_phase':z,'rank':r,'normal':n,'odd_plain_offsets':offsets,'odd_plain_coset_classes':cls,'odd_plain_union_size':27*len(set(cls)),'even_plain_union_size':27,'full_odd_packet':len(set(cls))==3})
profiles=[]
for modulus,k in [(5,1),(9,1),(9,2),(9,3)]:
 good={ (tuple(r['X']),r['integer_phase']%modulus) for r in good4 }
 tile=set()
 shifts=[-1,1]+([-k,k] if k>1 and k%2 else [])
 for q in packets:
  if q['full_odd_packet']:
   for t in shifts:tile.add((tuple(q['X']),(q['integer_phase']+t)%modulus))
 union=good|tile
 profiles.append({'modulus':modulus,'plain_exponents':[-1,1]+([-k,k] if k>1 else []),'controller_order':24*modulus,'rank4_word_slots':len(good),'full_odd_packet_slots':len(tile),'combined_sufficient_slots':len(union),'sufficient_full_D4_certificate':len(union)==24*modulus,'uncovered_by_this_certificate':[[list(X),z] for X,z in sorted(({(a,b,c,d) for a,b,c,d in itertools.product(range(3),repeat=4) if (a*d-b*c)%3==1}) for _ in [])] if False else []})
 # Save the actual missing finite controller slots without evaluating a fiber ball.
 allX=[X for X in itertools.product(range(3),repeat=4) if (X[0]*X[3]-X[1]*X[2])%3==1]
 profiles[-1]['uncovered_by_this_certificate']=[{'X':list(X),'phase':z} for X in allX for z in range(modulus) if (X,z) not in union]
res={'status':'COMPLETE_SMALL_SYMBOLIC_ROUTE_ANALYSIS','four_wide_words':256,'rank_histogram':rankhist,'rank4_words':len(good4),'three_wide_rank3_packets':len(packets),'full_odd_packets':sum(q['full_odd_packet'] for q in packets),'prediction':'SUPPORTED' if any(q['full_odd_packet'] for q in packets) else 'REFUTED','profiles':profiles,'packets':packets,'good4':good4,'CPU_seconds':time.process_time()-start,'source_BFS':0,'new_graphs':0,'ordinary_bad_unordered_pairs':None,'scope':'Rank4 path and parallel-hyperplane packet certificates only. Missing certificate slot is not actual missing fiber target.'}
(P/'ANALYSIS_ROUTE_COUNTS.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k not in ['packets','good4','profiles']}))
