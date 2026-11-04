"""PRODUCER extraction; resulting reduced certificates require fresh independent review."""
from pathlib import Path
import json
R=Path(__file__).resolve().parent
classes=json.loads((R/'FOURTEEN_MID_REDUCED_candidate_classes.json').read_text())['classes'];out=[]
def pairs(rec):return tuple((a,b) for a,b in zip(rec[::2],rec[1::2]))
def record(es):return bytes(x for e in sorted(tuple(sorted(e)) for e in es) for x in e)
def compress(F,fixed,Kminus):
 adj={x:[] for e in F+fixed for x in e}
 for a,b in F+fixed:adj[a].append(b);adj[b].append(a)
 seen=set();result=[]
 for start in sorted(Kminus):
  if start in seen:continue
  x=start;previous=None;walk=set()
  while True:
   assert x not in walk;walk.add(x)
   if x!=start and x in Kminus:break
   step=[y for y in adj[x] if y!=previous];assert len(step)==1
   previous,x=x,step[0]
  result.append((start,x));seen|=walk
 assert seen==set(adj),'selected full column contains a cycle with fixed pairs'
 return tuple(result)
for cls in classes:
 if not cls['forced_pairs']:continue # index54 is unchanged positive source certificate
 i=cls['index'];g=cls['geometry'];H=set(g['minority']+g['majority']);K=set(range(32))-H;fixed=tuple(map(tuple,cls['forced_pairs']));Kminus=K-{x for e in fixed for x in e};n=len(K);nr=cls['target_rank'];nc=1<<(n//2-1);width=(32-len(g['omitted'])-n//2)*2
 src=R/cls['source_prefix'];pre=R/f'FOURTEEN_MID_REDUCED_orbit_{i:03d}'
 matrix=Path(str(src)+'_matrix.bin').read_bytes();assert len(matrix)==nr*(nc//8)
 fullrows=[int.from_bytes(matrix[j*(nc//8):(j+1)*(nc//8)],'little') for j in range(nr)];basis={}
 for original in fullrows:
  x=original
  while x:
   p=x.bit_length()-1
   if p in basis:x^=basis[p]
   else:basis[p]=x;break
  assert x
 chosen=sorted(basis);assert len(chosen)==nr
 fullcols=Path(str(src)+'_columns.bin').read_bytes();assert len(fullcols)==nc*n
 reducedcols=[record(compress(pairs(fullcols[j*n:(j+1)*n]),fixed,Kminus)) for j in chosen]
 fullpairs=Path(str(src)+'_pairs.bin').read_bytes();assert len(fullpairs)==nr*n
 reducedpairs=[]
 for j in range(nr):
  pp={tuple(sorted(e)) for e in pairs(fullpairs[j*n:(j+1)*n])};assert set(fixed)<=pp
  reducedpairs.append(record(pp-set(fixed)))
 reducedrows=[sum(((row>>j)&1)<<k for k,j in enumerate(chosen)) for row in fullrows]
 pivots=[0]*nr;combos=[0]*nr
 for j,original in enumerate(reducedrows):
  x=original;c=1<<j
  while x:
   p=x.bit_length()-1
   if pivots[p]:x^=pivots[p];c^=combos[p]
   else:pivots[p]=x;combos[p]=c;break
  assert x
 assert all(pivots)
 for suffix in ['_forests.bin','_config.txt']:Path(str(pre)+suffix).write_bytes(Path(str(src)+suffix).read_bytes())
 assert Path(str(pre)+'_forests.bin').stat().st_size==nr*width
 Path(str(pre)+'_full_pairs.bin').write_bytes(fullpairs);Path(str(pre)+'_pairs.bin').write_bytes(b''.join(reducedpairs));Path(str(pre)+'_columns.bin').write_bytes(b''.join(reducedcols))
 for suffix,rows in [('_matrix.bin',reducedrows),('_pivots.bin',pivots),('_combos.bin',combos)]:Path(str(pre)+suffix).write_bytes(b''.join(row.to_bytes(nr//8,'little') for row in rows))
 item={**cls,'prefix':pre.name,'forest_record_bytes':width,'source_column_indices':chosen,'rows':nr,'status':'PRODUCER_REDUCED_CERTIFICATE_REQUIRES_INDEPENDENT_REVIEW'}
 Path(str(pre)+'.json').write_text(json.dumps(item,indent=2)+'\n');out.append(item)

for c in classes:
 if not c['forced_pairs']:out.append({**c,'prefix':c['source_prefix'],'forest_record_bytes':36,'rows':2048,'status':'PRODUCER_ONLY'})
(R/'FOURTEEN_MID_REDUCED_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','reports':out},indent=2)+'\n')
print('Prepared',len(out),'local inputs')
