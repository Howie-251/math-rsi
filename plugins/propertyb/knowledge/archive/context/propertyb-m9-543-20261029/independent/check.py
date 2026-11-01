#!/usr/bin/env python3
"""Independent complete-domain reconstruction and injection-probability replay.
No author probability, profile-generation, selection, or coverage module is imported.
"""
import argparse,json,itertools,time
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from math import comb,prod
from pathlib import Path
OUT=Path(__file__).resolve().parent;BASE=OUT.parent
K=9;M=542;TOTAL=4878

def ceiling(n,d):return -(-n//d)
@lru_cache(None)
def falling(n,r):return prod(range(n-r+1,n+1)) if 0<=r<=n else 0
@lru_cache(None)
def context(v,slots,h):
    bit=next((1<<j for j,p in enumerate(slots) if p==h),0)
    left=h-1-sum(p<h for p in slots)
    right=v-h-sum(p>h for p in slots)
    return left,right,sum(1<<j for j,p in enumerate(slots) if p<h),sum(1<<j for j,p in enumerate(slots) if p>h),bit
@lru_cache(None)
def injection(v,slots,h,t,u=None):
    """Uniform injections of named free vertices; endpoints or fixed-pair probability."""
    n=v-len(slots);a,b,left,right,bit=context(v,slots,h);r=K-t.bit_count()
    if u is None:
        result=[]
        for capacity,mask in ((a,left),(b,right)):
            if bit:
                p=Q(falling(capacity,r),falling(n,r)) if t&bit and not t&~(mask|bit) else Q(0)
            else:
                p=Q(r*falling(capacity,r-1),falling(n,r)) if r>0 and not t&~mask else Q(0)
            result.append(p)
        return tuple(result)
    s=K-u.bit_count()
    if bit:
        if t&u!=bit or t&~(left|bit) or u&~(right|bit) or r+s>n:return Q(0)
        return Q(falling(a,r)*falling(b,s),falling(n,r+s))
    if t&~left or u&~right or r<1 or s<1 or r+s-1>n:return Q(0)
    return Q(falling(a,r-1)*falling(b,s-1),falling(n,r+s-1))

def deduction(v,slots,ell,j,avoid):
    bit=1<<j;typ=[t for t in ell if t&bit];cells=[]
    for i,t in enumerate(typ):
        for u in typ[i:]:
            cap=ell[t]*(ell[t]-1)//2 if t==u else ell[t]*ell[u]
            if cap:cells.append((t|u,cap,injection(v,slots,slots[j],t,u)+injection(v,slots,slots[j],u,t)))
    masks=[r for r in range(1<<len(slots)) if not r&bit] if avoid else [0]
    answer=Q(0)
    for forbidden in masks:
        f=sum(count for t,count in ell.items() if t&bit and not t&forbidden)
        need=max(0,ceiling(8*f-(v-1-forbidden.bit_count()),7));value=Q(0)
        permitted=sorted((weight,cap) for union,cap,weight in cells if not union&forbidden)
        for weight,cap in permitted:
            used=min(need,cap);value+=used*weight;need-=used
            if not need:break
        assert need==0,(v,slots,j,forbidden,f)
        answer=max(answer,value)
    return answer

def locked(v,slots,ell,avoid):
    slots=tuple(slots);ell={t:n for t,n in ell.items() if n}
    assert len(set(slots))==len(slots) and all(1<=p<=v for p in slots)
    assert min(ell.values())>=0 and sum(ell.values())==M
    deductions={p:deduction(v,slots,ell,j,avoid) for j,p in enumerate(slots)}
    out=Q(0)
    for h in range(1,v+1):
        end=sum(n*injection(v,slots,h,t)[0] for t,n in ell.items())
        start=sum(n*injection(v,slots,h,t)[1] for t,n in ell.items())
        pair=sum(n*(m-(t==u))*injection(v,slots,h,t,u) for t,n in ell.items() for u,m in ell.items())
        assert pair>=deductions.get(h,0)
        out+=min(end,start,pair-deductions.get(h,0))
    return out

def unlocked(v):
    multi=max(0,ceiling(M*comb(K,2)-comb(v,2),comb(K-1,2)))
    ordered=M*(M-1)-2*multi
    return sum(min(M*injection(v,(),h,0)[0],M*injection(v,(),h,0)[1],ordered*injection(v,(),h,0,0)) for h in range(1,v+1))

def profile(ds,tri=None):
    if len(ds)==1:return {0:M-ds[0],1:ds[0]}
    if len(ds)==2:return {0:M-sum(ds)+1,1:ds[0]-1,2:ds[1]-1,3:1}
    blocks=(7,) if tri else (3,5,6);ell={b:1 for b in blocks}
    for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
    ell[0]=M-sum(ell.values());return ell

def key(v,kind,ds=(),tri=None):return (v,kind,tuple(ds),tri)
def rowkey(row):return key(row['v'],row['kind'],row.get('degrees',()),row.get('triple'))
def clear():
    context.cache_clear();injection.cache_clear()

def normalize_ell(ell):return {int(t):n for t,n in ell.items() if n}
def replay_row(row):
    v=row['v'];kind=row['kind'];ds=tuple(row.get('degrees',()));tri=row.get('triple')
    if kind=='zero':
        assert not row['positions'] and not row['ell'];return unlocked(v)
    ell=profile(ds,tri)
    assert normalize_ell(row['ell'])==normalize_ell(ell)
    assert min(ell.values())>=0 and sum(ell.values())==M
    s=len(ds);assert [sum(n for t,n in ell.items() if t>>j&1) for j in range(s)]==list(ds)
    for a,b in itertools.combinations(range(s),2):assert sum(n for t,n in ell.items() if t>>a&1 and t>>b&1)==1
    if s==3:assert ell.get(7,0)==tri
    assert row['deduction'] in ('full_pool','max_R')
    return locked(v,row['positions'],ell,row['deduction']=='max_R')

def original_domain():
    small=[]
    for v in range(17,57):
        p=Q(M*(comb(v//2,K) if v//2>=K else 0)+M*(comb(v-v//2,K) if v-v//2>=K else 0),comb(v,K))
        assert p<1;small.append((v,str(p)))
    assert max(Q(p) for _,p in small)==Q(6233,6307)
    necessary=[v for v in range(17,TOTAL+1) if v*ceiling(v-1,8)<=TOTAL and Q(M*((comb(v//2,K) if v//2>=K else 0)+(comb(v-v//2,K) if v-v//2>=K else 0)),comb(v,K))>=1]
    assert necessary==list(range(57,196))
    assert 196*ceiling(195,8)>TOTAL and all(comb(v,9)>=M for v in necessary)
    return small,necessary

def reconstruct(table):
    """Recompute routing inequalities, rather than route by submitted row presence."""
    expected={};parents=[];selections=[];routing=Counter()
    for v in range(57,196):
        if v<=134:
            expected[key(v,'zero')]=dict();continue
        d0=ceiling(v-1,8)
        if v>=183:
            Z=29*v-TOTAL;T=234-v;assert Z>0 and 16*Z>T*T
            rmin=ceiling(Z,29-d0)
            for r in range(rmin,v+1):assert r*r>2*(T*r-8*Z)
            selections.append(dict(v=v,d0=d0,D=28,Z=Z,T=T,gap=16*Z-T*T,rmin=rmin))
            for ds in itertools.combinations_with_replacement(range(d0,29),3):
                for tri in (0,1):expected[key(v,'three',ds,tri)]=profile(ds,tri)
            continue
        for d in range(d0,TOTAL//v+1):
            if v<=154:
                u=locked(v,(v//2,),profile((d,)),False);routing['one_tests']+=1
                if u<1:expected[key(v,'one',(d,))]=profile((d,));continue
            n=2*(v-1)-8*d;assert n>0
            # Enumerate candidates by the integer degree inequality, not by the author's floor formula.
            partner=[e for e in range(d,M+1) if v*d+n*(e-d)<=TOTAL]
            assert partner and partner==list(range(d,max(partner)+1))
            for e in partner:
                ell=profile((d,e));avoid=(v<=154)
                u=locked(v,(v//2,v//2+1),ell,avoid);routing['two_tests']+=1
                if u<1:expected[key(v,'two',(d,e))]=ell;continue
                common=n-1-(8*e-v+1);assert common>0
                base=v*d+n*(e-d);assert base<=TOTAL
                third=[f for f in range(e,M+1) if base+common*(f-e)<=TOTAL]
                assert third and third==list(range(e,max(third)+1))
                parents.append(dict(v=v,d=d,e=e,common_pool=common,fmax=max(third)))
                for f in third:
                    for tri in (0,1):expected[key(v,'conditional_three',(d,e,f),tri)]=profile((d,e,f),tri)
        clear()
    assert set(expected)==set(table),dict(extra=list(set(table)-set(expected))[:5],missing=list(set(expected)-set(table))[:5])
    for k,ell in expected.items():
        if ell:assert normalize_ell(ell)==normalize_ell(table[k]['ell'])
    return expected,parents,selections,dict(routing)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--profile',type=int,default=0);args=ap.parse_args()
    rows=json.loads((BASE/'CANDIDATE.json').read_text())['rows'];table={rowkey(r):r for r in rows};assert len(table)==len(rows)==3450
    started=time.process_time()
    if args.profile:
        sampled=[]
        for kind in ('zero','one','two','conditional_three','three'):
            group=[r for r in rows if r['kind']==kind];stride=max(1,len(group)//args.profile)
            sampled.extend(group[::stride][:args.profile])
        for i,r in enumerate(sampled):
            u=replay_row(r);assert u==Q(r['U'])<1
            if i%args.profile==args.profile-1:clear()
        duration=time.process_time()-started
        print(json.dumps(dict(profile_rows=len(sampled),cpu_seconds=duration,estimated_replay_cpu=duration*3450/len(sampled)),indent=2));return
    small,vertices=original_domain();expected,parents,selections,routing=reconstruct(table);domain_cpu=time.process_time()-started
    replay=[];grouped={};lastv=None
    for r in sorted(rows,key=lambda r:(r['v'],r['kind'],tuple(r.get('degrees',())),r.get('triple',-1))):
        if lastv!=r['v']:clear();lastv=r['v']
        u=replay_row(r);assert u==Q(r['U'])<1,(rowkey(r),str(u),r['U'])
        replay.append(dict(v=r['v'],kind=r['kind'],degrees=r.get('degrees',[]),triple=r.get('triple'),U=str(u)))
        grouped.setdefault(r['kind'],[]).append(u)
    result=dict(status='PASS_WITH_DECLARED_IMPORTS',review_independence='same-family',acceptance_status='provisional',k=K,M=M,total_degree=TOTAL,
        vertex_domain=vertices,balanced=small,original_domain_reconstructed=True,decision_tree_reconstructed=True,rows=len(rows),exact_matches=len(replay),strict_rows=len(replay),
        groups={kind:dict(rows=len(values),maximum=str(max(values))) for kind,values in grouped.items()},
        conditional_parent_count=len(parents),conditional_parents=parents,low_degree_triple_selection=selections,routing_evaluations=routing,
        domain_cpu_seconds=domain_cpu,total_cpu_seconds=time.process_time()-started,
        imports=['Random-greedy failure-to-critical-pair theorem and uniform conditional-permutation interpretation re-read in propertyB_small_k/propertyB_k8_k9_proof.md §2; not re-proved in a theorem prover.','No author numerical or coverage module imported; falling-factorial injection method adapted from previously reviewed m6 independent/check.py, with uniformity9 and link8/maxintersection7 re-derived here.'],
        replay=replay)
    (OUT/'CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('replay','balanced','vertex_domain','conditional_parents','low_degree_triple_selection')},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
