"""Bounded actual P-trace caller census; stops at first nongated necessary input.
Only missing P3+K2 and 3K2, high count 4 then 3; no H or outer-layout enumeration.
"""
from pathlib import Path
from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter
import json, time

HERE = Path(__file__).resolve().parent
EDGES = list(combinations(range(7), 2))
MISSING = {'P3_K2': ((0,1),(1,2),(3,4)),
           '3K2': ((0,1),(2,3),(4,5))}


def gate(m4, m3, t, b):
    assert min(m4,m3,t,b) >= 0
    p = m4+m3
    if m3 == 0:
        if m4 <= 7 and t <= 4 and b <= 35: return 'PURE7_T4_B35'
        if m4 <= 6 and t <= 6 and b <= 35: return 'PURE6_T6_B35'
        if m4 <= 5 and t <= 10 and b <= 32: return 'PURE5_T10_B32'
        if m4 == 8 and t <= 4 and b <= 17: return 'PURE8_T4_B17'
        if m4 == 8 and t <= 3 and b <= 20: return 'PURE8_T3_B20'
        if m4 <= 10 and t == 0 and b <= 27: return 'PURE10_T0_B27_ROOT'
    if p <= 5 and t <= 2: return 'SMALL5_T2'
    if p <= 4 and t <= 8 and b <= 32: return 'SMALL4_T8_B32'
    if p <= 7 and m3 <= 2 and t <= 1: return 'MIXED7_TWO3_T1_ANYB'
    if p <= 7 and m3 <= 4 and t == 0: return 'MIXED7_FOUR3_T0_ANYB'
    return None


def move(mask, perm):
    return sum(1 << perm[i] for i in range(7) if mask >> i & 1)


def setup(F):
    fs = {tuple(sorted(e)) for e in F}
    aut = [p for p in permutations(range(7))
           if {tuple(sorted((p[i],p[j]))) for i,j in F} == fs]
    maps = [{m:move(m,p) for m in range(128)} for p in aut]
    internal = [127 ^ ((1 << i)|(1 << j)) for i,j in F]
    ci = [sum(t >> i & 1 for t in internal) for i in range(7)]
    C = [i for i,c in enumerate(ci) if c == 3]
    D = [i for i in range(7) if i not in C]
    return aut,maps,internal,ci,C,D


def canonical(hi,maps):
    return min(tuple(sorted(mp[t] for t in hi)) for mp in maps)


def trace_check(internal, hi, J, private, blue):
    out = Counter()
    traces = [(t,1) for t in internal]+[(t,1) for t in hi]
    traces += [((1 << i)|(1 << j),n) for (i,j),n in zip(EDGES,J)]
    traces += [(1 << i,n) for i,n in enumerate(private)]
    assert sum(n for t,n in traces)==35
    for t,n in traces:
        if not n: continue
        if t & blue == t: out['P',5-t.bit_count()] += n
        elif not t & blue: out['N',5-t.bit_count()] += n
    assert set(out) <= {('P',4),('P',3),('N',3),('N',4)}
    return out['P',4],out['P',3],out['N',3],out['N',4]


def main():
    cpu0=time.process_time();wall0=time.perf_counter();reports=[];first=None;complete=True
    setups={name:setup(F) for name,F in MISSING.items()}
    jobs=[(r,name,k) for r in (4,3) for name in MISSING
          for k in range(2 if r==4 else 4)]
    try:
        for r,name,k in jobs:
            F=MISSING[name];aut,maps,internal,ci,C,D=setups[name]
            n3,n4=r-k,k;n2=9-2*n3-3*n4;n1=23+n3+2*n4
            triples=[sum(1 << i for i in S) for S in combinations(D,3)]
            quads=[sum(1 << i for i in S) for S in combinations(D,4)]
            representatives=set();raw_hi=0
            for a in combinations_with_replacement(triples,n3):
                for b in combinations_with_replacement(quads,n4):
                    raw_hi+=1;representatives.add(canonical(a+b,maps))
            accepted=[];uses=Counter();per_hi=[];invalid_hi=0
            for hid,hi in enumerate(sorted(representatives)):
                if time.process_time()-cpu0>120: raise TimeoutError('120 CPU-second budget')
                h=[sum(t >> i & 1 for t in hi) for i in range(7)]
                w=[sum(t.bit_count()-1 for t in hi if t >> i & 1) for i in range(7)]
                cap=[min(8-ci[i]-h[i],15-4*ci[i]-w[i]) for i in range(7)]
                needed=[eid for eid,(i,j) in enumerate(EDGES)
                        if not any(t >> i & 1 and t >> j & 1 for t in internal+list(hi))]
                if min(cap)<0 or len(needed)>n2:
                    invalid_hi+=1;continue
                base=[0]*21;base_d=[0]*7
                for eid in needed:
                    base[eid]=1;i,j=EDGES[eid];base_d[i]+=1;base_d[j]+=1
                if any(d>c for d,c in zip(base_d,cap)):
                    invalid_hi+=1;continue
                blue_options=[(eid,i,j,(1 << i)|(1 << j)) for eid,(i,j) in enumerate(EDGES)
                              if (i,j) not in F and all(t & ((1 << i)|(1 << j)) for t in hi)]
                count=0
                for extra in combinations_with_replacement(range(21),n2-len(needed)):
                    J=base.copy();s=base_d.copy()
                    for eid in extra:
                        J[eid]+=1;i,j=EDGES[eid];s[i]+=1;s[j]+=1
                    if any(d>c for d,c in zip(s,cap)):continue
                    private=[8-ci[i]-h[i]-s[i] for i in range(7)]
                    assert min(private)>=0 and sum(private)==n1
                    count+=1;found=None;possibilities=[]
                    for eid,i,j,blue in blue_options:
                        signature=(private[i]+private[j],J[eid],n2-s[i]-s[j]+J[eid],n1-private[i]-private[j])
                        assert trace_check(internal,hi,J,private,blue)==signature
                        tag=gate(*signature)
                        possibilities.append(dict(blue=[i,j],signature=list(signature),gate=tag))
                        if tag:
                            found=[list(hi),[e for e,n in enumerate(J) for _ in range(n)],eid,tag]
                            break
                    if found is None:
                        first=dict(missing=name,F=[list(e) for e in F],r=r,n3=n3,n4=n4,n2=n2,n1=n1,
                                   high_masks=list(hi),high_sets=[[i for i in range(7) if t >> i & 1] for t in hi],
                                   internal_degrees=ci,high_occurrences=h,weighted_high_occurrences=w,
                                   J=[[list(EDGES[e]),n] for e,n in enumerate(J) if n],private=private,
                                   all_admissible_blue_pairs=possibilities,
                                   meaning='necessary P-trace input only, no complete H constructed')
                        break
                    accepted.append(found);uses[found[3]]+=1
                per_hi.append(dict(id=hid,high_masks=list(hi),necessary_J_checked=count))
                if first:break
            filename=f'{name}_r{r}_n4{k}_ACCEPTED.json'
            (HERE/filename).write_text(json.dumps(accepted,separators=(',',':'))+'\n')
            reports.append(dict(missing=name,r=r,n3=n3,n4=n4,n2=n2,n1=n1,aut_size=len(aut),
                                raw_high_multisets=raw_hi,high_orbits=len(representatives),
                                impossible_high_orbits=invalid_hi,accepted=len(accepted),
                                completed=first is None,gate_uses=dict(uses),per_high=per_hi,
                                witnesses_file=filename))
            print(name,r,k,'hi',len(representatives),'accepted',len(accepted),'nongated',bool(first),flush=True)
            if first:complete=False;break
    except TimeoutError as e:
        complete=False
        first=dict(stopped_reason=str(e))
    report=dict(scope=__doc__,completed_all_jobs=complete,first_nongated=first,jobs=reports,
                pair_order=[list(e) for e in EDGES],cpu_seconds=time.process_time()-cpu0,
                wall_seconds=time.perf_counter()-wall0)
    (HERE/'RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
    print('FINAL',dict(complete=complete,cpu_seconds=report['cpu_seconds'],first_nongated=first),flush=True)


if __name__=='__main__':main()
