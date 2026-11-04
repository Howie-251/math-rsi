from pathlib import Path
from itertools import combinations,permutations
import json,hashlib
P=Path(__file__).resolve().parent
J=json.loads((P/'FOURTEEN_RESIDUAL_STRUCTURE.json').read_text())
pc=int.bit_count
mask=lambda xs:sum(1<<x for x in xs)
shift=lambda m,a:mask(x^a for x in range(32) if m>>x&1)
project=lambda x,d:(x&((1<<d)-1))|((x>>(d+1))<<d)
lift=lambda x,d:(x&((1<<d)-1))|((x>>d)<<(d+1))
nb=lambda x:[x^(1<<d) for d in range(6)]
reg={}
for line in (P/'FOURTEEN_REUSE_REVIEW_registry.txt').read_text().splitlines():
 m,j,o,R,f,i=map(int,line.split())
 if R:reg.setdefault((m,j,o),set()).add(((R,),'accepted',f,i))
new=json.loads((P/'FOURTEEN_FORCED_candidate_classes.json').read_text())['classes']
perms=[[sum(((x>>d)&1)<<p[d] for d in range(5)) for x in range(32)] for p in permutations(range(5))]
for g in new:
 geo=g['geometry'];rr=g['forced_pairs']
 for a in geo['minority'] or geo['omitted']:
  for p in perms:
   k=tuple(mask(p[x^a] for x in geo[z]) for z in ('minority','majority','omitted'));R=tuple(mask(p[x^a] for x in pair) for pair in rr)
   reg.setdefault(k,set()).add((R,'candidate',40,g['index']))
summary=[];totals={};novel=0
for v in (1,7,31):
 name=f'FOURTEEN_HALL_remaining_v{v}_covered.bin';raw=(P/name).read_bytes();recs=[tuple(raw[i:i+13]) for i in range(0,len(raw),13)]
 after=(P/f'FOURTEEN_FORCED_remaining_v{v}_covered.bin').read_bytes();remainset={tuple(after[i:i+13]) for i in range(0,len(after),13)}
 hits=[]
 for index,rec in enumerate(recs):
  Z=rec[:6];W=rec[6:];H={0,*rec};covered=set(range(64))-H
  forced=set()
  for x in covered:
   neigh=[y for y in nb(x) if y in covered]
   if len(neigh)==1:forced.add(tuple(sorted((x,neigh[0]))))
  candidates=[]
  for d in range(6):
   if not v>>d&1:continue # root must lie in B for this new route
   ZA=[x for x in Z if x>>d&1];ZB=[x for x in Z if not x>>d&1];WA=[x for x in W if x>>d&1];WB=[x for x in W if not x>>d&1]
   s=len(ZA)+1-len(WA);even=s>=0
   if even:
    if not WA:continue
    pool=ZA;mi=ZB;ma=WB
   else:s=-s;pool=[x for x in WA if x!=(1<<d)];mi=WB;ma=ZB
   if s<3 or s>len(pool):continue
   M=mask(project(x,d) for x in mi);base=mask(project(x,d) for x in ma)
   for S in combinations(pool,s):
    Y=[x^(1<<d) for x in S]
    if any(y in H for y in Y):continue
    O=mask(project(y,d) for y in Y);major=base|O;anchor=(M or O)&-(M or O);anchor=anchor.bit_length()-1
    k=tuple(shift(m,anchor) for m in (M,major,O))
    for rr,status,fam,idx in sorted(reg.get(k,())):
     RR=[shift(pair,anchor) for pair in rr]
     roots=[pair for pair in RR if pair&1]
     if len(roots)!=1:continue
     R=roots[0]
     if pc(R)!=2:continue
     qproj=(R^1).bit_length()-1;q=lift(qproj,d)
     for x,y in forced:
      if q not in (x,y) or x>>d&1 or y>>d&1:continue
      # direct leaf certificate for all-original-M forced edge
      leaf=next(z for z in (x,y) if len([w for w in nb(z) if w in covered])==1)
      candidates.append(dict(source_index=index,cut=d,consumption='even' if even else 'odd',sources=list(S),M=M,J=major,U=O,R=R,all_forced_pairs=RR,local_status=status,family=fam,local_id=idx,other_obstruction_endpoint=q,forced_edge=[x,y],degree_one_vertex=leaf,new_after_FORCED=rec in remainset))
  if candidates:
   choice=min(candidates,key=lambda g:(g['local_status']=='candidate',g['cut'],g['family'],g['local_id'],g['sources']))
   hits.append(choice)
 positives={x['source_index'] for x in hits};res=b''.join(bytes(rec) for i,rec in enumerate(recs) if i not in positives)
 newhits=[x for x in hits if x['new_after_FORCED']];nids={x['source_index'] for x in newhits};novel+=len(newhits)
 merged=b''.join(bytes(rec) for i,rec in enumerate(recs) if rec in remainset and i not in nids)
 (P/f'FOURTEEN_RESIDUAL_STRUCTURE_rootpair_witness_v{v}.json').write_text(json.dumps(hits,indent=2)+'\n')
 (P/f'FOURTEEN_RESIDUAL_STRUCTURE_remaining_v{v}_covered.bin').write_bytes(merged)
 summary.append({'v':v,'input':len(recs),'rootpair_positive':len(hits),'new_after_FORCED':len(newhits),'remaining_after_FORCED_and_rootpair':len(merged)//13,'local_status_hist':{z:sum(x['local_status']==z for x in hits) for z in ('accepted','candidate')}})
 print(summary[-1])
J['rootpair_application']=summary;J['rootpair_new_after_FORCED']=novel
# augment exact forced classifications with elementary degree-one certificates.
for row in J['orbit_rows']:
 H={0,*row['representative']};row['forced_edge_degree_one_certificates']=[]
 for e,o in row['forced_edges']:
  leaf=next(z for z in (e,o) if len([w for w in nb(z) if w not in H])==1)
  row['forced_edge_degree_one_certificates'].append({'edge':[e,o],'leaf':leaf,'covered_neighbors':[w for w in nb(leaf) if w not in H]})
(P/'FOURTEEN_RESIDUAL_STRUCTURE.json').write_text(json.dumps(J,indent=2)+'\n')
print('novel',novel)
