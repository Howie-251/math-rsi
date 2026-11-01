"""Small scalar/source-type checks only. No H, coloring or negative search."""
from itertools import product
from pathlib import Path
import json

swap=[]
for j,h,y in product(range(1,5),(0,1),(0,1)):
 if h>5-j or y>j or (j==4 and h) or (j==1 and y and not h):
  continue
 new=j+h-y
 assert 1<=new<=4
 actual=int(new==1)-int(j==1)
 expected=-int(j==1 and h and not y)+int(j==2 and y and not h)
 assert actual==expected
 swap.append([j,h,y,new,actual])

b12=[]
for u,t in ((0,0),(0,1),(1,0)):
 for c in range(8-u):
  kappa_lower=4-2*t if u==0 else 2
  sinks_lower=1+u+c
  margin=kappa_lower*sinks_lower-2*c
  assert margin>0
  b12.append(dict(u=u,N2=t,cut_half=c,sinks_lower=sinks_lower,
                  each_sink_kappa_lower=kappa_lower,strict_margin=margin))

b13=[]
for u,t in ((0,0),(0,1),(1,0)):
 for bh in range(t+1):
  cap=u+1+t-bh
  assert 2*cap+bh<=4-bh<5
  kappa=6-2*u-2*t+bh
  assert kappa>=4
 for c in range(7-u):
  margin=4*(1+u+c)-2*c
  assert margin>0
  b13.append(dict(u=u,N2=t,cut_half=c,strict_margin=margin))

transfer=[]
for u,c,t in product(range(2),range(2),range(3)):
 ap=(t,4-2*t,t,1)
 up=t-1-u-c
 if up<0:
  continue
 for n2 in range(11+c):
  N=(12+u,n2,10+c-n2,12-u-c)
  if min(N[j]-ap[j] for j in range(4))<0:
   continue
  new=(N[3]-1+ap[2],N[2]-ap[2]+ap[1],
       N[1]-ap[1]+ap[0],1+N[0]-ap[0])
  assert sum(new)==34 and min(new)>=0
  assert new[0]-12==up and new[1]+new[2]-10==c
  assert u+up+c==t-1<=1
  delta=18-3*u-c-N[1]
  delta_new=18-3*up-c-new[1]
  assert delta+delta_new==25
  transfer.append(dict(u=u,c=c,t=t,N=N,new_N=new,
                       delta=delta,new_delta=delta_new))

assert [6*(M-1)+(b*b-43*b)//2 for M,b in ((34,12),(34,13),(34,14))]==[12,3,-5]
assert 13-6==7 and 9-7==2  # r7 boundary: delta7 and N2=2
for bh in range(3):
 assert 2*(3-bh)+bh<8

out=dict(status='PASS',scope='proper-edge swap and source-color scalar interfaces only',
         edge_swap_rows=swap,b12_excluded_capacity_rows=b12,
         b13_excluded_capacity_rows=b13,single_N4_transfer_rows=transfer,
         conclusion_b12='N1+N2>=14',conclusion_b13='N1+N2>=15',
         low_count_source_corollary='r<=7 implies minimum blue count <=12',
         not_a_coloring_proof=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(swap),'edge swap rows;',len(b12)+len(b13),'capacity rows;',
      len(transfer),'single-N4 transfer rows')
