"""Complete independent Python-bigint replay of all zero/one-lock profiles.
Uses decimal fixed denominator 10**20 (author uses binary 2**52).
"""
import check as base
import json,time
from fractions import Fraction as Q
from pathlib import Path
C=base.C;M=4660;T=10**20;start=time.monotonic();OUT=Path(__file__).resolve().parent

def up(num,den):return (num*T+den-1)//den
def down(num,den):return num*T//den
results=[];total=0
for row in base.DATA['rows']:
    v=row['v'];mode=row['mode']
    if mode not in ('none','one'):continue
    if mode=='none':
        pairs=M*(M-1)-2*max(0,base.ceil(M*66-C(v,2),55));z=0
        for h in range(1,v+1):
            z+=min(M*up(12*C(h-1,11),v*C(v-1,11)),M*up(12*C(v-h,11),v*C(v-1,11)),pairs*up(C(h-1,11)*C(v-h,11),v*C(v-1,11)*C(v-12,11)))
        vals=[z]
    else:
        # Generate a new rank-wise probability table directly in integer arithmetic.
        lock=v//2;N=v-1;table=[]
        for h in range(1,v+1):
            a=h-1-int(lock<h);b=v-h-int(lock>h);last=[];first=[];w=[];wl=[]
            for x in [0,1]:
                r=12-x
                if h==lock:
                    last.append(up(C(a,r),C(N,r)) if x else 0)
                    first.append(up(C(b,r),C(N,r)) if x else 0)
                else:
                    last.append(up(r*C(a,r-1),N*C(N-1,r-1)) if not x or lock<h else 0)
                    first.append(up(r*C(b,r-1),N*C(N-1,r-1)) if not x or lock>h else 0)
                for y in [0,1]:
                    s=12-y
                    if h==lock:
                        admissible=x==y==1
                        num=C(a,r)*C(b,s);den=C(N,r)*C(N-r,s)
                    else:
                        admissible=(not x or lock<h) and (not y or lock>h)
                        num=C(a,r-1)*C(b,s-1);den=N*C(N-1,r-1)*C(N-r,s-1)
                    w.append(up(num,den) if admissible else 0)
                    wl.append(down(num,den) if admissible else 0)
            table.append((last,first,w,wl))
        vals=[]
        for d in range(row['degree_range'][0],row['degree_range'][1]+1):
            n0=M-d;n1=d;z=0
            for h,(A,B,w,wl) in enumerate(table,1):
                pair=n0*(n0-1)*w[0]+n0*n1*(w[1]+w[2])+n1*(n1-1)*w[3]
                if h==lock:
                    q=base.ceil(11*d-v+1,10)
                    assert 0<=q<=C(d,2)
                    pair-=q*2*wl[3]
                assert pair>=0
                z+=min(n0*A[0]+n1*A[1],n0*B[0]+n1*B[1],pair)
            vals.append(z)
    assert len(vals)==row['profiles'];assert max(vals)<T
    assert Q(max(vals),T)<=Q(row['worst_z'],base.DATA['S'])
    results.append(dict(v=v,mode=mode,profiles=len(vals),max_numerator=max(vals),denominator=T,strict=True,below_author_saved_max=True))
    total+=len(vals)
summary=dict(status='PASS',denominator=T,arithmetic='Python arbitrary integers only, separately written formulas; ceil upper and floor deletion',full_modes=['none','one'],profiles=total,per_vertex=results,wall_seconds=time.monotonic()-start)
(OUT/'INTEGER01.json').write_text(json.dumps(summary,indent=2)+'\n')
print('INDEPENDENT INTEGER COMPLETE',total,'profiles',summary['wall_seconds'],'seconds',flush=True)
