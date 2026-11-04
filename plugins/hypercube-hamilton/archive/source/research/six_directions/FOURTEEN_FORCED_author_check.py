"""Producer positive certificate self-check; NOT independent mathematical acceptance."""
from pathlib import Path
import json,hashlib,collections,struct
R=Path(__file__).resolve().parent
reports=json.loads((R/'FOURTEEN_FORCED_summary.json').read_text())['reports'];tot=collections.Counter();results=[]
def pairing(rec,terminals):
 assert set(rec)==terminals and len(rec)==len(terminals) and len(set(rec))==len(rec)
 p={}
 for a,b in zip(rec[::2],rec[1::2]):assert a!=b;p[a]=b;p[b]=a
 return p
for report in reports:
 pre=R/report['prefix'];g=report['geometry'];H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H;fixed={tuple(e) for e in report['forced_pairs']};Kminus=K-{x for e in fixed for x in e};n=len(Kminus);size=report['target_rank'];width=report['forest_record_bytes']
 f=Path(str(pre)+'_forests.bin').read_bytes();fp=Path(str(pre)+('_full_pairs.bin' if fixed else '_pairs.bin')).read_bytes();rp=Path(str(pre)+'_pairs.bin').read_bytes();cols=Path(str(pre)+'_columns.bin').read_bytes();matrix=Path(str(pre)+'_matrix.bin').read_bytes()
 assert len(f)==size*width and len(fp)==size*len(K) and len(rp)==size*n and len(cols)==size*n and len(matrix)==size*size//8
 derived=[]
 for j in range(size):
  adj={x:[] for x in range(32)};seen=set();parent=list(range(32))
  def find(x):
   while parent[x]!=x:x=parent[x]
   return x
  for a,b in zip(f[j*width:(j+1)*width:2],f[j*width+1:(j+1)*width:2]):
   assert 0<=a<32 and 0<=b<32 and (a^b).bit_count()==1 and tuple(sorted((a,b))) not in seen
   seen.add(tuple(sorted((a,b))));adj[a].append(b);adj[b].append(a);aa,bb=find(a),find(b);assert aa!=bb;parent[aa]=bb
  for x in range(32):assert len(adj[x])==(0 if x in U else 1 if x in K else 2)
  pp={}
  for a in K:
   mates=[b for b in K if b!=a and find(a)==find(b)];assert len(mates)==1;pp[a]=mates[0]
  assert pp==pairing(fp[j*len(K):(j+1)*len(K)],K)
  for h,p,q in report['forced_cherries']:
   assert set(adj[h])=={p,q} and len(adj[p])==len(adj[q])==1 and pp[p]==q
  red={x:y for x,y in pp.items() if x in Kminus};assert red==pairing(rp[j*n:(j+1)*n],Kminus);derived.append(red)
 cp=[pairing(cols[j*n:(j+1)*n],Kminus) for j in range(size)];computed=[]
 for pp in derived:
  label={};at=0
  for x in sorted(Kminus):
   if x not in label:label[x]=label[pp[x]]=at;at+=1
  row=0
  for j,cc in enumerate(cp):
   parent=list(range(at));merges=0
   def find(x):
    while parent[x]!=x:x=parent[x]
    return x
   for a,b in cc.items():
    if a>b:continue
    aa,bb=find(label[a]),find(label[b])
    if aa!=bb:parent[aa]=bb;merges+=1
   if merges==at-1:row|=1<<j
  computed.append(row)
 assert b''.join(x.to_bytes(size//8,'little') for x in computed)==matrix
 piv={}
 for row in computed:
  while row:
   p=row.bit_length()-1
   if p in piv:row^=piv[p]
   else:piv[p]=row;break
 assert len(piv)==size
 results.append({'index':report['index'],'rank':size,'forests':size,'matrix_bits':size*size,'forced_pairs':len(fixed)});tot['forests']+=size;tot['columns']+=size;tot['matrix_bits']+=size*size
coverage=json.loads((R/'FOURTEEN_FORCED_coverage.json').read_text());raw=(R/'FOURTEEN_FORCED_witnesses.bin').read_bytes();assert len(raw)==coverage['safe']*40
counts=collections.Counter()
for rec in struct.iter_unpack('<BIHBQIIIB4B7x',raw):
 v,i,local,d,S,M,J,O,nr,*end=rec;assert local in {r['index'] for r in reports} and nr in (0,1,2);counts[v]+=1
source_report=json.loads((R/'FOURTEEN_HALL_REVIEW.json').read_text());assert source_report['verdict']=='PASS'
for name,h in coverage['input_hashes'].items():assert source_report['audited_input_hashes'][name].removeprefix('sha256:')==h
out={'status':'PRODUCER_AUTHOR_CHECK_SUCCESS_NOT_INDEPENDENT_ACCEPTANCE','totals':dict(tot),'local_reports':results,'chosen_witness_header_counts':dict(counts),'independent_local_and_actual_application_review_still_required':True,'source_Hall_final_PASS_bound':True,'source_Hall_review_sha256':hashlib.sha256((R/'FOURTEEN_HALL_REVIEW.json').read_bytes()).hexdigest(),'full_fourteen_hole_proved':False,'full_P6_proved':False}
(R/'FOURTEEN_FORCED_author_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
