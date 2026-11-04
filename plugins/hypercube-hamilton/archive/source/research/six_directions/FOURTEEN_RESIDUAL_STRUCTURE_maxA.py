from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import json
P=Path(__file__).resolve().parent
J=json.loads((P/'FOURTEEN_RESIDUAL_STRUCTURE.json').read_text())
mask=lambda xs:sum(1<<x for x in xs)
proj=lambda x,d:(x&((1<<d)-1))|((x>>(d+1))<<d)
shift=lambda m,a:mask(x^a for x in range(32) if m>>x&1)
reg={}
# all accepted explicit local statements plus the20 newly accepted unforced inputs
for filename in ('FOURTEEN_REUSE_REVIEW_registry.txt','FOURTEEN_CACHED_REVIEW_selected_registry.txt'):
 for line in (P/filename).read_text().splitlines():
  t=list(map(int,line.split()));m,j,o=t[:3]
  if len(t)==6:R,f,i=t[3:]
  else:R=0;f,i=t[3:]
  reg.setdefault((m,j,o),[]).append((R,f,i,'accepted'))
# forthcoming new classes; use their local statements conditionally only
for c in json.loads((P/'FOURTEEN_FORCED_candidate_classes.json').read_text())['classes']:
 geo=c['geometry']
 if len(c['forced_pairs'])!=1:continue
 for a in geo['minority'] or geo['omitted']:
  for p in permutations(range(5)):
   tr=lambda x:sum(((x>>d)&1)<<p[d] for d in range(5))
   k=tuple(mask(tr(x^a) for x in geo[z]) for z in ('minority','majority','omitted'))
   rr=mask(tr(x^a) for x in c['forced_pairs'][0]);reg.setdefault(k,[]).append((rr,40,c['index'],'candidate'))
rows=[]
for row in J['orbit_rows']:
 opts=[]
 for cut in row['cuts']:
  if not cut.get('maximal_A_candidate'):continue
  d=cut['d'];A={x for x in range(64) if not x>>d&1};Z=row['Z'];W=row['W'];WA=cut['J'];WB=[x for x in W if x not in A]
  for t in cut['T']:
   if t==row['v']:continue
   for w in cut['w_options']:
    for b in WA:
     if b==w:continue
     S=[x for x in WA if x not in (w,b)]
     M=mask(proj(x,d) for x in WB);major=mask(proj(x,d) for x in Z if x!=t^(1<<d))|mask(proj(x,d) for x in S)
     O=mask(proj(x,d) for x in S);a=((M or O)&-(M or O)).bit_length()-1
     k=tuple(shift(m,a) for m in (M,major,O))
     for rr,f,i,status in reg.get(k,[]):
      R=shift(rr,a)
      protected=mask(proj(x,d) for x in (w,b))
      if R and not R&protected:continue
      opts.append({'cut':d,'t':t,'w':w,'b':b,'sources':S,'B_M':M,'B_J':major,'B_U':O,'B_R':R,'local_family':f,'local_id':i,'local_status':status})
 row['maximal_A_B_options']=opts
 if opts:rows.append({'orbit_index':row['index'],'v':row['v'],'orbit_size':row['orbit_size'],'options':len(opts),'cuts':sorted({x['cut'] for x in opts}),'accepted_options':sum(x['local_status']=='accepted' for x in opts)})
print('rootstar options',len(rows),'orbits',sum(r['orbit_size'] for r in rows),'records');print(rows)
J['maximal_A_option_summary']=rows
(P/'FOURTEEN_RESIDUAL_STRUCTURE.json').write_text(json.dumps(J,indent=2)+'\n')
