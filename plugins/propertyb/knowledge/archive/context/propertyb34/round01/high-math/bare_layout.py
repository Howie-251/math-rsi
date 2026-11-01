"""Fast exact no-deduction layout bound for screening complete local catalogues."""
from math import factorial
from fractions import Fraction

def falling(a,r):
 if r<0 or a<r:return 0
 z=1
 for j in range(r):z*=a-j
 return z

class BareLayout:
 def __init__(self,v,pos):
  self.v=v;self.pos=tuple(pos);self.s=len(pos);self.N=v-self.s;self.D=factorial(self.N);self.rows=[]
  for k in range(1,v+1):
   left=sum(1<<i for i,p in enumerate(pos) if p<k);right=sum(1<<i for i,p in enumerate(pos) if p>k);pivot=next((1<<i for i,p in enumerate(pos) if p==k),0)
   a=k-1-left.bit_count();b=v-k-right.bit_count();ran=range(6) if pivot else range(1,6);shift=int(not pivot)
   aw={r:falling(a,r-shift)*factorial(self.N-r)*(1 if pivot else r) for r in ran};bw={r:falling(b,r-shift)*factorial(self.N-r)*(1 if pivot else r) for r in ran}
   cw={(r,q):falling(a,r-shift)*falling(b,q-shift)*factorial(self.N-r-q+shift) for r in ran for q in ran if r+q-shift<=self.N}
   self.rows.append((left,right,pivot,aw,bw,cw))
 def bound(self,ns,with_rows=False):
  total=0;out=[];ts=[(t,n,5-t.bit_count()) for t,n in ns.items()]
  for left,right,pivot,aw,bw,cw in self.rows:
   ls={};rs={}
   for t,n,r in ts:
    if pivot and not t&pivot:continue
    if not (t^pivot)&~left:ls[r]=ls.get(r,0)+n
    if not (t^pivot)&~right:rs[r]=rs.get(r,0)+n
   A=sum(n*aw.get(r,0) for r,n in ls.items());B=sum(n*bw.get(r,0) for r,n in rs.items())
   if (not A or not B) and not with_rows:continue
   C=sum(n*m*cw.get((r,q),0) for r,n in ls.items() for q,m in rs.items())
   base_r=4 if pivot else 5;C-=ns.get(pivot,0)*cw.get((base_r,base_r),0)
   total+=min(A,B,C)
   if with_rows:out.append((Fraction(A,self.D),Fraction(B,self.D),Fraction(C,self.D)))
  answer=Fraction(total,self.D)
  return (answer,out) if with_rows else answer
