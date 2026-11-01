"""Exact scalar check of the seven-four-set forest argument; no set-family enumeration."""
from pathlib import Path
from math import comb
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
# Independently generate all decreasing component size partitions of7.
def partitions(n,k,last=None):
 if k==0:
  if n==0:yield ()
  return
 for a in range(min(n,last if last is not None else n),0,-1):
  for tail in partitions(n-a,k-1,a):yield (a,)+tail
rows=[]
for k in range(1,8):
 for sizes in partitions(7,k):
  # Supports of distinct4-sets: singleton >=4, nontrivial >=5.
  lower=sum(4 if s==1 else 5 for s in sizes)
  if k>=5:assert lower>17
  if k==4 and lower<=17:assert sizes==(4,1,1,1) and lower==17
  row={'components':k,'sizes':sizes,'distinct_support_lower':lower}
  if k==3:
   pairwise_linear_lower=sum(4*s-comb(s,2) for s in sizes)
   assert pairwise_linear_lower>17
   row['support_lower_if_all_intersections_le1']=pairwise_linear_lower
  rows.append(row)
joints={j:comb(9+j,2+j) for j in range(4)}
assert joints=={0:36,1:120,2:330,3:792}
deductions={'components_le2':5*joints[1]+joints[0],'components3':joints[2]+3*joints[1]+2*joints[0],'components4':3*joints[3]+3*joints[0]}
assert deductions=={'components_le2':636,'components3':762,'components4':2484}
D=comb(17,10);red=comb(13,6);blue=comb(13,10);empty=comb(12,5)+comb(12,10)
bare=7*red+25*blue+empty
assert (D,red,blue,empty,bare)==(19448,1716,286,858,20020)
assert min(deductions.values())==636 and bare-636<D
# A/B exact trace-stage residuals each have one total surplus attachment.
choices=[]
for size in (3,4):
 for surplus_point in range(5):
  attachments=[7 if i<size else (5 if size==3 else 3) for i in range(5)]
  attachments[surplus_point]+=1
  assert sum(attachments)==32
  eligible=[i for i in range(size) if attachments[i]==7]
  assert len(eligible)>=size-1
  choices.append({'nonempty_trace_size':size,'surplus_point':surplus_point,'attachments':attachments,'eligible_red_points':eligible})
out={'status':'PASS','scope':__doc__,'partitions':rows,'joint_numerators':joints,'same_tree_deduction_bounds':deductions,'D':D,'bare':bare,'strict_numerator':bare-636,'strict_margin':D-(bare-636),'strict_bound':str(Fraction(bare-636,D)),'AB_all_surplus_locations':choices,'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('partitions','AB_all_surplus_locations')}))
