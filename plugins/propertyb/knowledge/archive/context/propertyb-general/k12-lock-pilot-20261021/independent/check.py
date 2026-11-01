"""Independent domain reconstruction and exact-rational boundary replay.
No imports from the author's certificate or scanner modules.
"""
import json,time
from pathlib import Path
from math import comb
from fractions import Fraction as Q
from itertools import combinations_with_replacement
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT.parent/'pilot/M4660.json').read_text())
M=4660; K=12; begin=time.monotonic()
def C(n,r):return comb(n,r) if n>=0 and 0<=r<=n else 0
def ceil(a,b):return -((-a)//b)
def reconstruct():
    # Necessary constraints: pair-cover minimum degree and balanced-coloring UB.
    # Include the edge-capacity prerequisite separately, not as an implicit assumption.
    vertices=[]
    for v in range(2*K-1,K*M+1):
        if v*ceil(v-1,K-1)>K*M:continue
        if M*(C(v//2,K)+C((v+1)//2,K))<C(v,K):continue
        assert C(v,K)>=M
        vertices.append(v)
    assert vertices==DATA['candidate_v']
    assert [r['v'] for r in DATA['rows']]==vertices
    counts={}; details=[]; membership={}
    for row in DATA['rows']:
        v=row['v']; mode=row['mode']; low=ceil(v-1,11); upper=55920//v
        assert row['d0']==low and row['minimum_degree_upper']==upper
        ranges=[]
        if mode=='none':ps=[()]
        elif mode=='one':
            assert row['degree_range']==[low,upper]
            ps=list((d,) for d in range(low,upper+1))
        elif mode=='two':
            ps=[]
            for d in range(low,upper+1):
                sd=2*v-2-11*d; assert sd>0
                # Search integer B directly, independently of the author's quotient.
                B=next(b for b in range(d,M+1) if v*d+sd*(b+1-d)>55920)
                rr=dict(d=d,s_d=sd,e_min=d,e_max=B); ranges.append(rr)
                ps.extend((d,e) for e in range(d,B+1))
            assert ranges==row['degree_ranges']
        else:
            feasible=[]
            # Exhaust all D, proving that the saved minimum is actually minimal.
            for D in range(low,M+1):
                Z=(D+1)*v-55920; diff=22*Z-(11*(D+1)-v+2)**2
                if Z>0 and diff>0:feasible.append(D)
            assert feasible and row['D']==min(feasible)
            D=min(feasible); assert row['degree_range']==[low,D]
            assert row['Z']==(D+1)*v-55920
            assert row['existence_strict_difference']==22*row['Z']-(11*(D+1)-v+2)**2
            ps=[(ds,flag) for ds in combinations_with_replacement(range(low,D+1),3) for flag in [False,True]]
        assert len(ps)==row['profiles']
        wp=row['worst_profile']; wp=(tuple(wp[0]),wp[1]) if mode=='three' else tuple(wp)
        assert wp in ps
        assert 0<=row['worst_z']<DATA['S']
        counts[mode]=counts.get(mode,0)+len(ps)
        details.append(dict(v=v,mode=mode,profiles=len(ps),d0=low,upper=upper,D=row.get('D'),degree_ranges=ranges))
        membership[v]=ps
    assert sum(counts.values())==691429
    return dict(candidate_vertices=vertices,edge_capacity_checked_for_all=True,profiles=counts,total_profiles=sum(counts.values()),per_vertex=details),membership

def counts_for(mode,p):
    if mode=='none':return [M]
    if mode=='one':d,=p;return [M-d,d]
    if mode=='two':d,e=p;return [M-d-e+1,d-1,e-1,1]
    (a,b,c),triple=p
    return ([M-a-b-c+2,a-1,b-1,0,c-1,0,0,1] if triple else [M-a-b-c+3,a-2,b-2,1,c-2,1,1,0])

def exact(v,mode,p):
    n=counts_for(mode,p); s=(len(n)-1).bit_length(); N=v-s
    locks=[[],[v//2],[v//2,v//2+1],[v//2-1,v//2,v//2+1]][s]
    total=Q(0)
    overlap=max(0,ceil(M*C(12,2)-C(v,2),C(11,2))) if not s else None
    for h in range(1,v+1):
        a=h-1-sum(t<h for t in locks);b=v-h-sum(t>h for t in locks)
        L=sum(1<<j for j,t in enumerate(locks) if t<h)
        R=sum(1<<j for j,t in enumerate(locks) if t>h)
        j=locks.index(h) if h in locks else None
        last=[];first=[];pair={}
        for x in range(len(n)):
            r=12-x.bit_count()
            if j is None:
                last.append(Q(r*C(a,r-1),N*C(N-1,r-1)) if r>=1 and x&~L==0 else Q(0))
                first.append(Q(r*C(b,r-1),N*C(N-1,r-1)) if r>=1 and x&~R==0 else Q(0))
            else:
                last.append(Q(C(a,r),C(N,r)) if x&(1<<j) and (x&~(1<<j))&~L==0 else Q(0))
                first.append(Q(C(b,r),C(N,r)) if x&(1<<j) and (x&~(1<<j))&~R==0 else Q(0))
            for y in range(len(n)):
                z=12-y.bit_count();w=Q(0)
                if j is None:
                    if x&~L==0 and y&~R==0 and min(r,z)>=1 and r+z-1<=N:
                        w=Q(C(a,r-1)*C(b,z-1),N*C(N-1,r-1)*C(N-r,z-1))
                elif x&y==(1<<j) and (x&~(1<<j))&~L==0 and (y&~(1<<j))&~R==0 and r+z<=N:
                    w=Q(C(a,r)*C(b,z),C(N,r)*C(N-r,z))
                pair[x,y]=w
        A=sum((nx*w for nx,w in zip(n,last)),Q(0));B=sum((nx*w for nx,w in zip(n,first)),Q(0))
        crit=sum((nx*(ny-int(x==y))*pair[x,y] for x,nx in enumerate(n) for y,ny in enumerate(n)),Q(0))
        if not s:crit-=2*overlap*pair[0,0]
        if j is not None:
            degree=sum(nx for x,nx in enumerate(n) if x&(1<<j))
            needed=ceil(11*degree-(v-1),10);assert needed>=0
            capacities=[]
            for x,nx in enumerate(n):
                for y in range(x,len(n)):
                    if x&(1<<j) and y&(1<<j):
                        cap=C(nx,2) if x==y else nx*n[y]
                        if cap:capacities.append((pair[x,y]+pair[y,x],cap))
            for weight,cap in sorted(capacities):
                take=min(needed,cap);crit-=take*weight;needed-=take
                if needed==0:break
            assert needed==0
        assert min(A,B,crit)>=0
        total+=min(A,B,crit)
    return total

coverage,params=reconstruct()
(ROOT/'DOMAIN_CHECK.json').write_text(json.dumps(coverage,indent=2)+'\n')
# Each mode global saved maximizer; both sides of every transition; outer endpoints.
selected={93,510,511,512,513,563,564,565,566,647,648,649,650,781,782}
for mode in ['none','one','two','three']:
    selected.add(max((r for r in DATA['rows'] if r['mode']==mode),key=lambda r:r['worst_z'])['v'])
replays=[]
for row in DATA['rows']:
    if row['v'] not in selected:continue
    v=row['v'];mode=row['mode'];p=row['worst_profile']
    tests=[p]
    if mode in ['one','two']:tests.append(params[v][-1])
    if mode=='three':
        tests.extend([((row['d0'],)*3,True),((row['D'],)*3,False),((row['D'],)*3,True)])
    seen=set()
    for p in tests:
        key=json.dumps(p)
        if key in seen:continue
        seen.add(key)
        value=exact(v,mode,p)
        assert value<=Q(row['worst_z'],DATA['S'])<1
        item=dict(v=v,mode=mode,profile=p,exact_numerator=str(value.numerator),exact_denominator=str(value.denominator),saved_upper_numerator=row['worst_z'],saved_denominator=DATA['S'],exact_below_saved_upper=True,strict=True)
        replays.append(item)
        print('FRACTION PASS',v,mode,p,'elapsed',round(time.monotonic()-begin,3),flush=True)
summary=dict(status='PASS',coverage='All candidate vertices and every selected-mode parameter domain reconstructed independently; exact Fraction arithmetic for selected boundaries only.',total_profile_domain=coverage['total_profiles'],mode_counts=coverage['profiles'],fraction_replays=replays,full_probability_replay=False,full_replay_not_attempted_reason='691429 profiles times up to 782 rank positions with arbitrary Fraction objects is not suitable for the 120-second independent arithmetic budget; no claim of complete independent probability replay.',wall_seconds=time.monotonic()-begin)
(ROOT/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='fraction_replays'},indent=2),flush=True)
