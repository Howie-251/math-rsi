from pathlib import Path
import json,itertools,hashlib,collections
P=Path(__file__).resolve().parent
rows=json.loads((P/'FOURTEEN_RESIDUAL_STRUCTURE_maxA_options.json').read_text());r=next(r for r in rows if r['orbit_index']==85);T={x^32 for x in r['Z']};E={x for x in range(1,32) if x.bit_count()%2==0};O={x for x in range(32) if x.bit_count()%2 and x not in (1,2,4,8,16,14)};G=E|O
maps=[[sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)] for p in itertools.permutations(range(5))]
opts={(o['q'],o['t'],o['w'],o['b'],o['case'],o['permutation']):o for o in r['options']}
forests={c:(P/f'TWELVE_ROOT_STAR_OPENING_case_{c:02}_forests.bin').read_bytes() for c in range(5)}
raw=(P/'FOURTEEN_RESIDUAL_STRUCTURE_maxA_full_85_certificates.bin').read_bytes();assert len(raw)%32==0
seen=set();usedforest=set();cases=collections.Counter();sizes=collections.Counter()
for off in range(0,len(raw),32):
 a=raw[off:off+32];m=a[22];q,t,w,b,c=a[23:28];i=int.from_bytes(a[28:30],'little');pi=a[30]
 key=(q,t,w,b,c,pi);assert key in opts;op=opts[key];assert a[31]==1
 L=[(a[2*j],a[2*j+1]) for j in range(m)];assert all(x<y and (x^y).bit_count()==1 and x in G and y in G for x,y in L)
 endpoints=[x for pair in L for x in pair];assert len(set(endpoints))==2*m and T<=set(endpoints) and q not in endpoints
 assert all(y in endpoints for x in G-set(endpoints) for y in G if (x^y).bit_count()==1)
 ident=tuple(sorted(L));assert ident not in seen;seen.add(ident);sizes[m]+=1;cases[c]+=1
 source=forests[c][i*32:(i+1)*32];assert len(source)==32
 tr=maps[pi];F=[(tr[source[j]],tr[source[j+1]]) for j in range(0,32,2)]
 deg=[0]*32;parent=list(range(32))
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 def join(x,y):
  x=find(x);y=find(y);assert x!=y;parent[x]=y
 for x,y in F:
  assert (x^y).bit_count()==1;deg[x]+=1;deg[y]+=1;join(x,y)
 assert all(deg[x]==(0 if x in (0,31) else 2 if x in (q,b) else 1) for x in range(32))
 assert (q,t) in F or (t,q) in F
 hv=next(y if x==31 else x for x,y in L if 31 in (x,y));Lp=[(x,y) for x,y in L if 31 not in (x,y)]+[(w,hv)]
 for x,y in Lp:join(x,y);deg[x]+=1;deg[y]+=1
 assert all(deg[x] in (1,2) for x in range(32) if x not in (0,31))
 ends=[x for x in range(32) if deg[x]==1];assert sum(x.bit_count()%2==0 for x in ends)*2==len(ends) and len(ends)>=8
 usedforest.add((c,i,pi))
count=json.loads((P/'FOURTEEN_RESIDUAL_STRUCTURE_maxA_count_85.json').read_text())['maximal_T_covered_matchings'];assert len(seen)==count==287469
j={'status':'PRODUCER_SANITY_NOT_INDEPENDENT_ACCEPTANCE','certificates':len(seen),'maximal_domain_count_DP':count,'size_histogram':dict(sizes),'case_histogram':dict(cases),'distinct_transformed_forests_used':len(usedforest),'all_selected_actual_forests_and_unions_checked':True,'complete_domain_follows_from_positive_uniqueness_and_DP_cardinality':True,'remaining_finite_acceptance_gate':'Fresh independent review required'}
(P/'FOURTEEN_RESIDUAL_STRUCTURE_maxA_sanity.json').write_text(json.dumps(j,indent=2)+'\n');print(j)
# sixty-record actual orbit and disjoint complement after the separate FORCED gate.
fullmaps=[[sum(((x>>p[d])&1)<<d for d in range(5))|(x&32) for x in range(64)] for p in itertools.permutations(range(5))];rep=r['Z']+r['W'];orb={tuple(sorted(tr[x] for x in rep[:6]))+tuple(sorted(tr[x] for x in rep[6:])) for tr in fullmaps};assert len(orb)==60
for v in (1,7,31):
 src=(P/f'FOURTEEN_FORCED_remaining_v{v}_covered.bin').read_bytes();recs=[tuple(src[k:k+13]) for k in range(0,len(src),13)];positive=[x for x in recs if v==31 and x in orb];rem=[x for x in recs if not(v==31 and x in orb)]
 if v==31:assert set(positive)==orb
 (P/f'FOURTEEN_RESIDUAL_STRUCTURE_maxA_positive_v{v}_covered.bin').write_bytes(b''.join(map(bytes,positive)))
 (P/f'FOURTEEN_RESIDUAL_STRUCTURE_maxA_remaining_v{v}_covered.bin').write_bytes(b''.join(map(bytes,rem)))
 print(v,'positive',len(positive),'remaining',len(rem))
