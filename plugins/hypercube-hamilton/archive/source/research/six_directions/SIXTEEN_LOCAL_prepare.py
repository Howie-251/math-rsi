"""Producer extraction of only nine CHOSEN local inputs; source files unchanged."""
from pathlib import Path
import json
R=Path(__file__).resolve().parent
selected=[9,11,1,2,33,7,12,14,15]
classes={r['index']:r for r in json.loads((R/'SIXTEEN_LOCAL_candidate_classes.json').read_text())['classes']}
def pairlist(rec):return tuple(zip(rec[::2],rec[1::2]))
def record(es):return bytes(x for e in sorted(tuple(sorted(e)) for e in es) for x in e)
out=[]
for i in selected:
 c=classes[i];g=c['geometry'];H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H;fixed=tuple(map(tuple,c['forced_pairs']));n=len(K);size=c['target_rank'];width=2*(32-len(U)-n//2)
 if not fixed:
  out.append({**c,'prefix':c['source_prefix'],'forest_record_bytes':width,'rows':size,'status':'PRODUCER_UNCONDITIONAL_INPUT_PENDING_INDEPENDENT_REVIEW'});continue
 assert len(fixed)==1
 p,q=fixed[0];Kminus=K-{p,q};src=R/c['source_prefix'];pre=R/f'SIXTEEN_LOCAL_FORCED_orbit_{i:03d}';nc=1<<(n//2-1)
 matrix=Path(str(src)+'_matrix.bin').read_bytes();assert len(matrix)==size*(nc//8)
 fullrows=[int.from_bytes(matrix[j*(nc//8):(j+1)*(nc//8)],'little') for j in range(size)];basis={}
 for original in fullrows:
  x=original
  while x:
   b=x.bit_length()-1
   if b in basis:x^=basis[b]
   else:basis[b]=x;break
  assert x
 chosen=sorted(basis);assert len(chosen)==size
 columns=Path(str(src)+'_columns.bin').read_bytes();assert len(columns)==nc*n;reducedcols=[]
 for j in chosen:
  f={a:b for a,b in pairlist(columns[j*n:(j+1)*n]) for a,b in [(a,b),(b,a)]};assert f[p]!=q
  a,b=f[p],f[q];del f[p];del f[q];f[a]=b;f[b]=a;assert set(f)==Kminus;reducedcols.append(record((a,b) for a,b in f.items() if a<b))
 fullpairs=Path(str(src)+'_pairs.bin').read_bytes();assert len(fullpairs)==size*n;reducedpairs=[]
 for j in range(size):
  pp={tuple(sorted(e)) for e in pairlist(fullpairs[j*n:(j+1)*n])};assert (p,q) in pp;reducedpairs.append(record(pp-{(p,q)}))
 rows=[sum(((row>>j)&1)<<k for k,j in enumerate(chosen)) for row in fullrows];pivots=[0]*size;combos=[0]*size
 for j,original in enumerate(rows):
  x=original;comb=1<<j
  while x:
   b=x.bit_length()-1
   if pivots[b]:x^=pivots[b];comb^=combos[b]
   else:pivots[b]=x;combos[b]=comb;break
  assert x
 for suffix in ['_forests.bin','_config.txt']:Path(str(pre)+suffix).write_bytes(Path(str(src)+suffix).read_bytes())
 assert Path(str(pre)+'_forests.bin').stat().st_size==size*width
 Path(str(pre)+'_full_pairs.bin').write_bytes(fullpairs);Path(str(pre)+'_pairs.bin').write_bytes(b''.join(reducedpairs));Path(str(pre)+'_columns.bin').write_bytes(b''.join(reducedcols))
 for suffix,data in [('_matrix.bin',rows),('_pivots.bin',pivots),('_combos.bin',combos)]:Path(str(pre)+suffix).write_bytes(b''.join(x.to_bytes(size//8,'little') for x in data))
 item={**c,'prefix':pre.name,'forest_record_bytes':width,'rows':size,'source_column_indices':chosen,'status':'PRODUCER_REDUCED_INPUT_PENDING_INDEPENDENT_REVIEW'};Path(str(pre)+'.json').write_text(json.dumps(item,indent=2)+'\n');out.append(item)
(R/'SIXTEEN_LOCAL_CERT_summary.json').write_text(json.dumps({'status':'PRODUCER_NINE_CHOSEN_INPUTS_PENDING_INDEPENDENT_REVIEW','selected_indices':selected,'reports':out,'full_sixteen_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
print('Produced nine chosen local inputs, source evidence unchanged.')
