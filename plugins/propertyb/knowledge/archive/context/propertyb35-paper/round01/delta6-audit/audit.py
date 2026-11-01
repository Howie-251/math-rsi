"""Independent RGS relational-domain and exact fixed-witness audit; no search imports."""
from pathlib import Path
from itertools import combinations, product
from fractions import Fraction as F
from math import comb, prod
from collections import defaultdict, Counter
import json,time
HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'middle/twenty_remaining'
def load(n): return json.loads((SRC/n).read_text())
def canon(P): return tuple(sorted(tuple(sorted(b)) for b in P))
def key(ns): return tuple(sorted((int(t),n) for t,n in ns.items() if n))
def partitions(n):
    def rec(a):
        if len(a)==n:
            P=tuple(tuple(i for i,x in enumerate(a) if x==b) for b in range(max(a)+1))
            if max(map(len,P))<=4 and len(P)<=6: yield canon(P)
            return
        for x in range(max(a)+2): yield from rec(a+[x])
    yield from rec([0])
def restrict(P,S):
    return canon([[S.index(i) for i in b if i in S] for b in P if any(i in S for i in b)])
def moments(r,n):
    ns=dict(key(r['counts']))
    return {u:sum(c for t,c in ns.items() if (t>>1)&u==u) for u in range(1,1<<n)}
def recover(P,I,n):
    full=(1<<n)-1
    J={t:I[t]-int(any(t&sum(1<<i for i in b)==t for b in P)) for t in range(1,full+1)}
    ns={}
    for t in range(1,full+1):
        ns[t<<1]=sum((-1)**(u.bit_count()-t.bit_count())*J[u] for u in range(1,full+1) if u&t==t)
    ns[0]=29-sum(ns.values())
    ns[1]=6-len(P)
    for b in P: ns[1+sum(2<<i for i in b)]=1
    if any(c<0 or (c and t.bit_count()>5) for t,c in ns.items()): return None
    assert sum(ns.values())==35
    return key(ns)
def ordinary_recover(I,n):
    ns={t:sum((-1)**(u.bit_count()-t.bit_count())*c for u,c in I.items() if u&t==t) for t in range(1,1<<n)}
    ns[0]=35-sum(ns.values())
    return key(ns) if all(c>=0 for c in ns.values()) else None
def join_domain(n,degrees,residuals):
    grouped=defaultdict(list)
    for r in residuals:
        grouped[(tuple(r['neighbor_degrees']),canon(r['center_partition']))].append(moments(r,n-1))
    result=set();nodes=0;fulljoins=0;parts=0
    for P in partitions(n):
        parts+=1;relations=[]
        for S in combinations(range(n),n-1):
            choices=[]
            for I in grouped[(tuple(degrees[i] for i in S),restrict(P,S))]:
                G={sum(1<<S[j] for j in range(n-1) if u>>j&1):c for u,c in I.items()}
                choices.append(G)
            relations.append(choices)
        if any(not rs for rs in relations): continue
        relations.sort(key=len)
        def dfs(j,I):
            nonlocal nodes,fulljoins
            nodes+=1
            if j==len(relations):
                fulljoins+=1
                tops=(0,1) if n==5 else ((0,) if n==6 else range(1+min(v for t,v in I.items() if t.bit_count()==n-1)))
                for top in tops:
                    II=I|{(1<<n)-1:top}
                    assert len(II)==(1<<n)-1
                    if any(v>1 for t,v in II.items() if t.bit_count()==5): continue
                    z=recover(P,II,n)
                    if z is not None: result.add((tuple(degrees),z))
                return
            for G in relations[j]:
                if all(t not in I or I[t]==c for t,c in G.items()): dfs(j+1,I|G)
        dfs(0,{1<<i:d for i,d in enumerate(degrees)})
    return result,dict(partitions=parts,nodes=nodes,fulljoins=fulljoins,profiles=len(result))
def fall(a,r): return prod(range(a-r+1,a+1)) if 0<=r<=a else 0
def probability(N,a,b,r,q,free=False):
    d=r+q+int(free)
    return F(fall(a,r)*fall(b,q),fall(N,d)) if r>=0 and q>=0 and d<=N else F()
def rows(ns,pos):
    s=len(pos);N=20-s;full=(1<<s)-1;out=[]
    for k in range(1,21):
        L=sum(1<<i for i,p in enumerate(pos) if p<k);R=sum(1<<i for i,p in enumerate(pos) if p>k)
        p=full^L^R;free=p==0;a=k-1-L.bit_count();b=20-k-R.bit_count()
        A=B=C=F();left=[];right=[]
        for t,c in ns.items():
            r=5-t.bit_count()
            if (not p and r and not t&~L) or (p and t&p and not (t^p)&~L):
                A+=c*(r if free else 1)*probability(N,a,b,r-int(free),0,free);left.append((t,c,r))
            if (not p and r and not t&~R) or (p and t&p and not (t^p)&~R):
                B+=c*(r if free else 1)*probability(N,a,b,0,r-int(free),free);right.append((t,c,r))
        for t,c,r in left:
            for u,d,q in right:
                assert t&u==p
                C+=(c*d-(c if t==u else 0))*probability(N,a,b,r-int(free),q-int(free),free)
        out.append((A,B,C))
    return out
def weight(t,u,i,pos):
    p=1<<i;k=pos[i];L=sum(1<<j for j,z in enumerate(pos) if z<k);R=sum(1<<j for j,z in enumerate(pos) if z>k)
    if t&u!=p or (t^p)&~L or (u^p)&~R: return F()
    return probability(20-len(pos),k-1-L.bit_count(),20-k-R.bit_count(),5-t.bit_count(),5-u.bit_count())
def slots(ns,i,pos):
    ts=sorted(t for t in ns if t>>i&1);out=[]
    for a,t in enumerate(ts):
        for u in ts[a:]:
            cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
            if cap: out.append([weight(t,u,i,pos)+weight(u,t,i,pos),cap,t,u])
    return out
def loss(ns,i,pos,c):
    inv=slots(ns,i,pos);p=1<<i
    if 'q_total' in c:
        d=sum(v for t,v in ns.items() if t&p);qt=max(0,(4*d-17)//3);qp=max(0,(4*ns.get(p,0)-(20-len(pos))+2)//3)
        assert (qt,qp)==(c['q_total'],c['q_pure']);z=F();left=qp
        for t in sorted(inv):
            if t[2]==t[3]==p:
                take=min(left,t[1]);left-=take;t[1]-=take;z+=take*t[0]
        assert not left;left=max(0,qt-qp)
        for t in sorted(inv):
            take=min(left,t[1]);left-=take;z+=take*t[0]
        assert not left
    else:
        ds=[];main=F()
        for x in c['dual']:
            R=x['avoid'];alpha=F(x['alpha']);assert alpha>=0 and not R&p
            f=sum(v for t,v in ns.items() if t&p and not t&R);q=max(0,(4*f-19+R.bit_count()+2)//3)
            assert (f,q)==(x['edge_count'],x['q']);main+=alpha*q;ds.append((R,alpha))
        pen=sum((cap*max(F(),sum((a for R,a in ds if not (t|u)&R),F())-w) for w,cap,t,u in inv),F());z=max(F(),main-pen)
        if 'main' in c: assert (main,pen)==(F(c['main']),F(c['penalty']))
    assert z==F(c['loss']);return z
def verify_fixed(r):
    ns=dict(key(r['counts']));pos=r['positions'];s=len(pos)
    assert len(set(pos))==s and all(1<=p<=20 for p in pos) and sum(ns.values())==35
    assert all(t.bit_count()<=5 and c>0 for t,c in ns.items())
    cs=r.get('certificates',r.get('quotas'));assert len(cs)==s
    deductions={pos[i]:loss(ns,i,pos,c) for i,c in enumerate(cs)}
    z=sum((min(A,B,C-deductions.get(k,F())) for k,(A,B,C) in enumerate(rows(ns,pos),1)),F())
    assert z==F(r['bound'])
    if 'strict' in r: assert r['strict']==(z<1)
    return z
def verify_joint(x):
    ns=dict(key(x['counts']));s=max(t.bit_length() for t in ns);expected=[]
    for i in range(s):
        ts=sorted(t for t in ns if t>>i&1)
        for a,t in enumerate(ts):
            for u in ts[a:]:
                cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
                if cap: expected.append(dict(center=i,t=t,u=u,capacity=cap))
    assert expected==x['slots'];slots_=expected;demand=[F()]*len(expected);quota=F()
    for c in x['quotas']:
        i,R=c['center'],c['avoid'];alpha=F(c['delta']);assert alpha>=0 and not R&(1<<i)
        f=sum(v for t,v in ns.items() if t>>i&1 and not t&R)
        q=max(0,(4*f-19+R.bit_count()+2)//3)
        ids=[j for j,z in enumerate(expected) if z['center']==i and not (z['t']|z['u'])&R]
        assert c.get('kind') is None and (f,q,ids)==(c['edge_count'],c['q'],c['slots'])
        quota+=q*alpha
        for j in ids:demand[j]+=alpha
    free=linear=mass=F();ws=[F()]*len(expected)
    for layout in x['layouts']:
        g=F(layout['probability']);assert g>0;mass+=g;pos=layout['positions'];rr=rows(ns,pos)
        free0=sum((min(z) for k,z in enumerate(rr,1) if k not in pos),F());assert free0==F(layout['free'],x['scale']);free+=g*free0
        for i,c in enumerate(layout['centers']):
            beta=F(layout['betas'][i]);assert 0<=beta<=g
            A,B,C=rr[pos[i]-1];ab=min(A,B)
            assert (ab,C)==(F(c['a'],x['scale']),F(c['c'],x['scale']));linear+=(g-beta)*ab+beta*C
            ww=[]
            for j,z in enumerate(expected):
                if z['center']==i:
                    w=weight(z['t'],z['u'],i,pos)+weight(z['u'],z['t'],i,pos);ww.append(w);ws[j]+=beta*w
            assert ww==[F(w,x['scale']) for w in c['weights']]
    assert mass==1
    penalties=[max(F(),d-w) for d,w in zip(demand,ws)]
    assert penalties==[F(z) for z in x['penalties']]
    penalty=sum((z['capacity']*p for z,p in zip(expected,penalties)),F());z=free+linear-quota+penalty
    assert (free,linear,quota,penalty)==tuple(F(x[k]) for k in ['free_average','linear_part','quota_part','capacity_penalty'])
    assert z==F(x['bound'])<1
    return z
def main():
    start=time.process_time();out={}
    # Integer-budget coverage, including every possible h,a,b triple.
    branches=Counter()
    for h in range(14,20):
        for a in range(h+1):
            for b in range(h-a+1):
                if 2*a+b<3*h-36: continue
                if a>=3: branch='three8'
                elif a==2: assert b>=2;branch='boundary' if b==2 else 'two8three9'
                elif a==1: assert b>=4;branch='one8four9'
                else: assert b>=6;branch='six9'
                if branch=='boundary': assert h==14
                branches[branch]+=1
    out['selection_budget']=dict(branches)
    # Boundary tables, rebuilt from every permitted inclusive intersection.
    exception=set()
    for c in range(1,8):
        for t in range(min(2,c)+1):
            z=ordinary_recover({1:6,2:7,4:7,3:2,5:2,6:c,7:t},3)
            if z is not None:exception.add(z)
    assert exception=={key(r['counts']) for r in load('EXCEPTION_TRIPLES.json')['cases']}
    four7=set()
    for ts in product(range(3),repeat=4):
        for top in range(min(ts)+1):
            I={1<<i:7 for i in range(4)}|{sum(1<<i for i in S):2 for S in combinations(range(4),2)}|dict(zip((7,11,13,14),ts))|{15:top}
            z=ordinary_recover(I,4)
            if z is not None:four7.add(z)
    assert four7=={key(r['counts']) for r in load('FOUR_SEVENS.json')['cases']}
    pre=set()
    for a,b,cs in [(6,6,range(1,7)),(6,7,[1])]:
        for c in cs:pre.add(ordinary_recover({1:a,2:b,3:c},2))
    assert pre=={key(r['counts']) for r in load('PAIRS.json')['cases'] if r['degrees']==[6,6] or r['degrees']==[6,7] and r['codegree']==1}
    out['boundary_domain_counts']=dict(preliminary_pairs=len(pre),exception_triples=len(exception),four_sevens=len(four7))
    # Rebuild the prerequisite two-neighbour domain directly from all pair moments.
    base2=set()
    for ds in ((8,8),(8,9),(9,9)):
        for P in partitions(2):
            for c in range(1,min(ds)+1):
                z=recover(P,{1:ds[0],2:ds[1],3:c},2)
                if z is not None:base2.add((ds,z))
    unit=load('UNIT_PAIRS.json')['cases']
    assert base2=={(tuple(r['degrees'][1:]),key(r['counts'])) for r in unit}
    # Give two-neighbour records the common relational interface.
    residual=[]
    for r in unit:
        if F(r['bound'])>=1:
            p=((0,1),) if r['triple'] else ((0,),(1,))
            residual.append(r|dict(neighbor_degrees=r['degrees'][1:],center_partition=p))
    dom3=set();stats=[]
    for ds in ((8,8,8),(8,8,9),(8,9,9),(9,9,9)):
        got,st=join_domain(3,ds,residual);dom3|=got;stats.append(dict(degrees=ds,**st))
    three=load('STAR_THREE_REFINED.json')['cases']
    assert dom3=={(tuple(r['neighbor_degrees']),key(r['counts'])) for r in three};out['three_RGS_join']=stats
    j3=load('STAR_THREE_JOINT.json')['results'];jids={r['source_id'] for r in j3 if F(r.get('bound','2'))<1}
    residual=[r for i,r in enumerate(three) if F(r['bound'])>=1 and i not in jids]
    assert len(residual)==24
    dom4=set();stats=[]
    for ds in ((8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9)):
        got,st=join_domain(4,ds,residual);dom4|=got;stats.append(dict(degrees=ds,**st))
    four=load('STAR_FOUR_DP.json')['cases'];joint=load('STAR_FOUR_JOINT.json')['results']
    assert dom4=={(tuple(r['neighbor_degrees']),key(r['counts'])) for r in four};out['four_RGS_join']=stats
    jids={r['source_id'] for r in joint if F(r.get('bound','2'))<1}
    residual=[r for r in four if not r['strict'] and r['source_id'] not in jids];assert len(residual)==97
    dom5=set();stats=[]
    for ds in ((8,8,9,9,9),(8,9,9,9,9),(9,9,9,9,9)):
        got,st=join_domain(5,ds,residual);dom5|=got;stats.append(dict(degrees=ds,**st))
    expected={(tuple(r['neighbor_degrees']),key(r['counts'])) for r in load('STAR_FIVE_DOMAIN.json')['cases']}
    assert dom5==expected;out['five_RGS_join']=stats
    five=load('STAR_FIVE_DP.json');assert five['complete']
    assert {(tuple(r['neighbor_degrees']),key(r['counts'])) for r in five['cases']}==dom5
    residual=[r for r in five['cases'] if not r['strict']];assert len(residual)==225
    got,st=join_domain(6,(9,)*6,residual)
    expected={(tuple(r['neighbor_degrees']),key(r['counts'])) for r in load('STAR_SIX_DOMAIN.json')['cases']}
    assert got==expected;out['six_RGS_join']=st
    six=load('STAR_SIX_DP.json');assert six['complete'] and len(six['cases'])==255
    assert {(tuple(r['neighbor_degrees']),key(r['counts'])) for r in six['cases']}==got
    out['domain_cpu_seconds']=time.process_time()-start
    # Profile fixed witnesses before bulk replay; do not run a position optimizer.
    pilot=five['cases'][:5]+six['cases'][:5];t=time.process_time()
    for r in pilot: verify_fixed(r)
    out['pilot']=dict(cases=10,cpu_seconds=time.process_time()-t)
    print('profile',out,flush=True)
    summaries=[]
    for name in ['PAIRS.json','UNIT_PAIRS.json','STAR_THREE_REFINED.json','EXCEPTION_TRIPLES.json','FOUR_SEVENS.json','STAR_FOUR_DP.json','STAR_FIVE_DP.json','STAR_SIX_DP.json']:
        rs=load(name)['cases']
        if name=='PAIRS.json':rs=[r for r in rs if r['degrees']==[6,6] or r['degrees']==[6,7] and r['codegree']==1]
        t=time.process_time();vals=[verify_fixed(r) for r in rs]
        summaries.append(dict(file=name,cases=len(vals),strict=sum(z<1 for z in vals),maximum_strict=str(max((z for z in vals if z<1),default=F())),cpu_seconds=time.process_time()-t))
        print(summaries[-1],flush=True)
    out['fixed_witnesses']=summaries;out['cpu_seconds']=time.process_time()-start;out['status']='PASS';out['review_independence']='same-family';out['acceptance_status']='provisional'
    joint_summary=[]
    for name,base in [('STAR_THREE_JOINT.json',three),('STAR_FOUR_JOINT.json',four)]:
        byid={r.get('source_id',i):r for i,r in enumerate(base)};t=time.process_time();vals=[]
        for r in load(name)['results']:
            if F(r.get('bound','2'))>=1:continue
            assert key(r['counts'])==key(byid[r['source_id']]['counts']);vals.append(verify_joint(r))
        joint_summary.append(dict(file=name,cases=len(vals),maximum=str(max(vals)),cpu_seconds=time.process_time()-t))
    out['joint_witnesses']=joint_summary;out['cpu_seconds']=time.process_time()-start
    (HERE/'AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
