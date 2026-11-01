"""New bounded run: pair choices first, then triples, adding eleven-positive repair.
Every original indexed P trace is colored directly; no assumption that high traces are proper.
"""
from pathlib import Path
from itertools import combinations, combinations_with_replacement
from collections import Counter
import sys,json,time

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
import diagnose as old
EDGES=old.EDGES


def signature(internal,hi,J,private,blue):
    counts=Counter()
    traces=[(t,1) for t in internal]+[(t,1) for t in hi]
    traces += [((1<<i)|(1<<j),n) for (i,j),n in zip(EDGES,J)]
    traces += [(1<<i,n) for i,n in enumerate(private)]
    assert sum(n for _,n in traces)==35
    for t,n in traces:
        if not n:continue
        if t & blue == t:counts['P',5-t.bit_count()]+=n
        elif not t & blue:counts['N',5-t.bit_count()]+=n
    return counts


def choose_gate(c):
    if any(n for (sign,size),n in c.items()
           if (sign=='P' and size not in (2,3,4)) or (sign=='N' and size not in (3,4))):
        return None
    p2,p3,p4=c['P',2],c['P',3],c['P',4]
    t,b=c['N',3],c['N',4]
    if p2==p3==t==0 and p4<=8 and b<=27:
        return 'PURE8_T0_B27'
    if p2==0:
        z=old.gate(p4,p3,t,b)
        if z:return z
    if p2+p3+p4<=5 and p2<=3 and t<=2:
        return 'SMALL5_T2_AT_MOST_THREE_P2'
    if p2+p3+p4<=4 and t<=3:
        return 'SMALL4_T3_ANYB'
    if p2==p3==t==0 and p4<=11 and b<=17:
        return 'ELEVEN_P4_T0_B17'
    return None


def main():
    cpu0=time.process_time();wall0=time.perf_counter();reports=[];first=None;complete=True
    setups={name:old.setup(F) for name,F in old.MISSING.items()}
    blue_choices=[(S,sum(1<<i for i in S)) for k in (2,3) for S in combinations(range(7),k)]
    jobs=[(r,name,k) for r in (4,3) for name in old.MISSING for k in range(2 if r==4 else 4)]
    try:
        for r,name,k in jobs:
            F=old.MISSING[name];aut,maps,internal,ci,C,D=setups[name]
            n3,n4=r-k,k;n2=9-2*n3-3*n4;n1=23+n3+2*n4
            ts=[sum(1<<i for i in S) for S in combinations(D,3)]
            qs=[sum(1<<i for i in S) for S in combinations(D,4)]
            reps=set();raw=0
            for a in combinations_with_replacement(ts,n3):
                for b in combinations_with_replacement(qs,n4):
                    raw+=1;reps.add(old.canonical(a+b,maps))
            accepted=[];uses=Counter();sizes=Counter();per_hi=[];invalid=0
            for hid,hi in enumerate(sorted(reps)):
                if time.process_time()-cpu0>120:raise TimeoutError('120 CPU-second budget')
                h=[sum(t>>i&1 for t in hi) for i in range(7)]
                w=[sum(t.bit_count()-1 for t in hi if t>>i&1) for i in range(7)]
                cap=[min(8-ci[i]-h[i],15-4*ci[i]-w[i]) for i in range(7)]
                needed=[e for e,(i,j) in enumerate(EDGES)
                        if not any(t>>i&1 and t>>j&1 for t in internal+list(hi))]
                if min(cap)<0 or len(needed)>n2:invalid+=1;continue
                base=[0]*21;sd=[0]*7
                for e in needed:
                    base[e]=1;i,j=EDGES[e];sd[i]+=1;sd[j]+=1
                if any(d>c for d,c in zip(sd,cap)):invalid+=1;continue
                total=0
                for extra in combinations_with_replacement(range(21),n2-len(needed)):
                    J=base.copy();s=sd.copy()
                    for e in extra:
                        J[e]+=1;i,j=EDGES[e];s[i]+=1;s[j]+=1
                    if any(d>c for d,c in zip(s,cap)):continue
                    private=[8-ci[i]-h[i]-s[i] for i in range(7)]
                    assert min(private)>=0 and sum(private)==n1
                    total+=1;found=None;possibilities=[]
                    for blue_set,blue in blue_choices:
                        sig=signature(internal,hi,J,private,blue)
                        tag=choose_gate(sig)
                        if tag:
                            found=[list(hi),[e for e,n in enumerate(J) for _ in range(n)],list(blue_set),tag,
                                   [sig['P',2],sig['P',3],sig['P',4],sig['N',3],sig['N',4]]]
                            break
                        possibilities.append(dict(blue=list(blue_set),
                                                  signed=[[z,d,n] for (z,d),n in sorted(sig.items()) if n]))
                    if found is None:
                        first=dict(missing=name,F=[list(e) for e in F],r=r,n3=n3,n4=n4,n2=n2,n1=n1,
                                   high_masks=list(hi),high_sets=[[i for i in range(7) if t>>i&1] for t in hi],
                                   ci=ci,hi=h,J=[[list(EDGES[e]),n] for e,n in enumerate(J) if n],private=private,
                                   all_pair_and_triple_signatures=possibilities,
                                   scope='necessary P-trace inventory only; no full H constructed')
                        break
                    accepted.append(found);uses[found[3]]+=1;sizes[len(found[2])]+=1
                per_hi.append(dict(id=hid,high_masks=list(hi),necessary_J_checked=total))
                if first:break
            filename=f'{name}_r{r}_n4{k}_ACCEPTED.json'
            (HERE/filename).write_text(json.dumps(accepted,separators=(',',':'))+'\n')
            reports.append(dict(missing=name,r=r,n3=n3,n4=n4,n2=n2,n1=n1,aut_size=len(aut),
                                raw_high_multisets=raw,high_orbits=len(reps),impossible_high_orbits=invalid,
                                accepted=len(accepted),completed=first is None,gate_uses=dict(uses),
                                blue_size_uses=dict(sizes),per_high=per_hi,witnesses_file=filename))
            print(name,r,k,'accepted',len(accepted),'non',bool(first),flush=True)
            if first:complete=False;break
    except TimeoutError as e:
        complete=False;first=dict(stopped_reason=str(e))
    report=dict(scope=__doc__,completed_all_jobs=complete,first_nongated=first,jobs=reports,
                pair_order=[list(e) for e in EDGES],cpu_seconds=time.process_time()-cpu0,
                wall_seconds=time.perf_counter()-wall0)
    (HERE/'RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
    print('FINAL',dict(complete=complete,cpu_seconds=report['cpu_seconds'],first_nongated=first),flush=True)


if __name__=='__main__':main()
