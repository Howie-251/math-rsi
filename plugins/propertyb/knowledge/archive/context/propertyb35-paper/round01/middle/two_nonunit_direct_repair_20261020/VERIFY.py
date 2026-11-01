"""Independent algebraic threshold + size/intersection-orbit verification."""
from math import comb
from itertools import combinations_with_replacement
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def extras(kind,r):
 if kind=='P':return 0
 if kind==0:return C(11,r-5)+C(11,r)
 return C(11+kind,r)
# Obtain the15 safe/exact thresholds from the affine risk formula, not trace-mask enumeration.
threshold={};cert=[]
for a,b in combinations_with_replacement(['P',0,2,3,4],2):
 good=[]
 assert 32*C(12,8)-31*C(8,0)>C(16,8) # r8 is never strict evenwithzeroextras.
 for r in range(9,17):
  D=C(16,r);R=C(12,r-4);B=C(12,r);J=C(8,r-8);slope=R-B-J
  assert slope>=0 and R>=B
  extra=extras(a,r)+extras(b,r)
  if 32*B+extra<D:good.append((0,r,32*B+extra,D))
  if slope>0:
   cmax=min(32,(D-1-(32*B+J+extra))//slope)
   if cmax>=1:good.append((cmax,r,32*B+J+extra+cmax*slope,D))
  else:assert 32*B+J+extra>=D
 cmax=max(x[0] for x in good);k=cmax+1
 chosen=min((x for x in good if x[0]==cmax),key=lambda x:x[2]/x[3]);threshold[frozenset((a,b))]=k
 # One fixedr fromthis certificate coversall c<=k-1 bythe verified monotonic slope.
 cert.append({'residual_types':[a,b],'k':k,'boundary_c':cmax,'r':chosen[1],'bad_count':chosen[2],'samples':chosen[3]})
# Generate19orbits from(j1,j2,h) andthe four membership-cell sizes, not S5canonicalization.
rows=[];labels=0
for j1,j2 in combinations_with_replacement([0,2,3,4],2):
 for h in range(max(0,j1+j2-5),j1+1):
  cells={'both':h,'only1':j1-h,'only2':j2-h,'neither':5-j1-j2+h}
  types={'both':('P','P'),'only1':('P',j2),'only2':(j1,'P'),'neither':(j1,j2)}
  ks={cell:threshold[frozenset(types[cell])] for cell,count in cells.items() if count}
  S=sum(cells[cell]*ks[cell] for cell in ks)
  count=C(5,j1)*C(j1,h)*C(5-j1,j2-h)
  if j1==j2 and h<j1:assert count%2==0;count//=2
  labels+=count
  rows.append({'j1':j1,'j2':j2,'h':h,'cells':cells,'k_by_cell':ks,'sum_k':S,'labels':count})
assert len(rows)==19 and labels==351
old=json.loads((P/'CHECK.json').read_text());table={(tuple(r['sizes']),r['intersection_size']):(r['sum_k'],r['orbit_size']) for r in old['rows']}
assert all(table[((r['j1'],r['j2']),r['h'])]==(r['sum_k'],r['labels']) for r in rows)
weak=[r for r in rows if r['sum_k']==32];assert len(weak)==3 and all(r['sum_k']>=32 for r in rows)
assert [(r['j1'],r['j2'],r['h']) for r in weak]==[(3,3,1),(3,4,2),(4,4,3)]
assert all(r['cells']['both']>=1 and r['k_by_cell']['both']==8 for r in weak)
# Final exception repair uses onlythe proved support bound andthese exact counts.
D=C(16,9);bare=8*C(12,5)+24*C(12,9)
overlap_joint=C(9,2);arbitrary_joint=C(8,1);deduct=5*overlap_joint+2*arbitrary_joint
assert (D,bare,deduct,bare-deduct,D-(bare-deduct))==(11440,11616,196,11420,20)
out={'status':'PASS_INDEPENDENT_SCALARS_AND_ORBIT_COVERAGE','threshold_certificates':cert,'orbits_from_sizes_intersection':rows,'labeled_pairs':labels,'remaining_equalities':weak,'final_eight_red_event_repair':{'distinct4sets':8,'ground':16,'overlap_components_max':3,'overlap_forest_min':5,'D':D,'bare_bad':bare,'tree_deduction':deduct,'bad_bound':bare-deduct,'success_lower':20},'cpu_seconds':time.process_time()-st}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS independent15thresholds/19orbits/351labels; universalfinalsuccess20;CPU',out['cpu_seconds'])
