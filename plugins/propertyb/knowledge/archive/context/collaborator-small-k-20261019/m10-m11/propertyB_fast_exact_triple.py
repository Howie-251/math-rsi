"""Fast, rigorously rounded integer-only 3-lock certificates.

S=2**40: m*(m-1)*S < 2**63 for the certified k=10/11 cases.
Each numerator is nonnegative and bounded by that quantity, so all numpy.int64
products and accumulations are mathematically proved free of overflow.
"""
import sys,time
import numpy as np
from itertools import combinations_with_replacement
from propertyB_k10_k11_certified import FixedCertificate,CEIL,triple_D
S=1<<40
SHIFT=12
assert (1<<52)//S == 1<<SHIFT

class FastExact(FixedCertificate):
    def table(self,v,s):
        t,A,B,WH,WL=super().table(v,s)
        key=(v,s,'arrays')
        if self.cache.get(key) is None:
            # 52-bit correctly rounded estimates safely coarsened to 40 bits
            Au=np.array([[(z+(1<<SHIFT)-1)>>SHIFT for z in row] for row in A],dtype=np.int64)
            Bu=np.array([[(z+(1<<SHIFT)-1)>>SHIFT for z in row] for row in B],dtype=np.int64)
            wu=np.array([[[(z+(1<<SHIFT)-1)>>SHIFT for z in row] for row in layer] for layer in WH],dtype=np.int64)
            wl=np.array([[[z>>SHIFT for z in row] for row in layer] for layer in WL],dtype=np.int64)
            self.cache[key]=(t,Au,Bu,wu,wl)
        return self.cache[key]
    def bound(self,v,cnt):
        m=self.M;k=self.k
        assert sum(cnt)==m and min(cnt)>=0
        assert m*(m-1)*S < (1<<63), 'possible int64 overflow'
        n=(len(cnt)-1).bit_length()
        t,A,B,W,V=self.table(v,n)
        cn=np.array(cnt,dtype=np.int64)
        # dot and einsum never exceed m*(m-1)*S in magnitude,
        # since every exact probability is <=1 and weights all nonnegative.
        a=A@cn
        b=B@cn
        c=np.einsum('hij,i,j->h',W,cn,cn,optimize=True)-np.einsum('hii,i->h',W,cn)
        for j,h in enumerate(t):
            deg=sum(int(cn[x]) for x in range(len(cn)) if x&(1<<j))
            q=CEIL((k-1)*deg-(v-1),k-2)
            cells=[]
            for x in range(len(cn)):
                if not x&(1<<j):continue
                for y in range(x,len(cn)):
                    if not y&(1<<j):continue
                    cap=int(cn[x])*(int(cn[x])-1)//2 if x==y else int(cn[x])*int(cn[y])
                    if cap:cells.append((int(V[h-1,x,y])+int(V[h-1,y,x]),cap))
            cells.sort()
            D=0
            for w,cap in cells:
                used=min(q,cap)
                D+=w*used
                q-=used
                if q==0:break
            assert q==0
            c[h-1]-=D
        assert np.all(c>=0),('negative',v,cnt)
        return int(np.minimum(np.minimum(a,b),c).sum())


def cert(k,m,lo,hi):
    t0=time.time();cal=FastExact(k,m);worst=(0,None,None,None);total=0
    for v in range(lo,hi+1):
        d0=CEIL(v-1,k-1);D=triple_D(k,m,v)
        for d in combinations_with_replacement(range(d0,D+1),3):
            for typ in (False,True):
                z=cal.three(v,d,typ)
                total+=1
                if z>=S:raise AssertionError((k,m,v,D,d,typ,z,S))
                if z>worst[0]:worst=(z,v,d,typ)
        if v==lo or v%5==0 or v==hi:
            print('PASS',k,'v',v,'D',D,'profiles',total,'max',worst[0],'S',S,'gap',(S-worst[0])/S,'elapsed',round(time.time()-t0,2),flush=True)
    print('FULL 3LOCK PASS',k,m,lo,hi,total,'worst',worst,'SEC',round(time.time()-t0,2),flush=True)

if __name__=='__main__':
    if int(sys.argv[1])==10:cert(10,1111,267,316)
    else:cert(11,2274,430,500)
