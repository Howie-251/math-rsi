"""Independent generation: only mathematical input, no discovery imports.
All necessary PL-filtered J inputs are tried against actual indexed trace colors.
"""
import json
import time
from pathlib import Path
from itertools import combinations, combinations_with_replacement, permutations, product
from collections import Counter

HERE=Path(__file__).resolve().parent
PAIRS=tuple(combinations(range(7),2))
SHAPES=(('P3_K2',((0,1),(1,2),(3,4))),('3K2',((0,1),(2,3),(4,5))))
MASK=lambda ss:sum(1<<i for i in ss)
BLUES=tuple(MASK(ss) for n in (2,3) for ss in combinations(range(7),n))

def graphs(n):
    rows=[]
    for ids in combinations_with_replacement(range(21),n):
        d=[0]*7;cover=0
        for eid in ids:
            a,b=PAIRS[eid];d[a]+=1;d[b]+=1;cover|=1<<eid
        rows.append((ids,d,cover))
    return rows

def gate(sig):
    p2,p3,p4,t,b=sig;p=p2+p3+p4
    if not p:return 'EMPTY'
    if p<=4 and t<=3:return 'SMALL4_T3'
    if p<=5 and p2<=3 and t<=2:return 'SMALL5_T2'
    if p2:return None
    if not p3:
        if p4<=7 and t<=4 and b<=35:return 'PURE7_T4_B35'
        if p4==8 and t<=3 and b<=20:return 'PURE8_T3_B20'
        if p4<=8 and not t and b<=27:return 'PURE8_T0_B27'
    if p<=7 and p3<=2 and t<=1:return 'MIXED7_TWO3_T1_ANYB'
    if p<=7 and p3<=4 and not t:return 'MIXED7_FOUR3_T0_ANYB'
    if not p3 and p4<=11 and not t and b<=17:return 'ELEVEN_P4_T0_B17'
    return None

def classify(traces,blue):
    count=Counter();codes=[]
    for mask in traces:
        hit=mask&blue
        if hit and hit!=mask:codes.append('.');continue
        size=5-mask.bit_count()
        key=('P' if hit==mask else 'N')+str(size)
        count[key]+=1;codes.append(key)
    # This rejects internal monochromatic edges, missed high traces (N1/N2),
    # and any positive singleton rather than silently dropping their risks.
    if set(count)-{'P2','P3','P4','N3','N4'}:return None,None
    sig=tuple(count[k] for k in ('P2','P3','P4','N3','N4'))
    assert len(codes)==35 and sum(sig)+codes.count('.')==35
    return sig,codes

def main():
    started=time.process_time();alljobs=[]
    G={n:graphs(n) for n in range(4)}
    for name,F in SHAPES:
        fs={frozenset(e) for e in F}
        autos=[p for p in permutations(range(7))
               if {frozenset((p[a],p[b])) for a,b in F}==fs]
        D=sorted(set().union(*map(set,F)));C=sorted(set(range(7))-set(D))
        internal=tuple(127^MASK(e) for e in F)
        ci=[sum(m>>i&1 for m in internal) for i in range(7)]
        options={k:tuple(MASK(ss) for ss in combinations(D,k)) for k in (3,4)}
        moves={m:tuple(MASK(p[i] for i in range(7) if m>>i&1) for p in autos)
               for m in options[3]+options[4]}
        def canon(high):
            return min(tuple(sorted(moves[m][j] for m in high)) for j in range(len(autos)))
        for r,n4 in ((4,0),(4,1),(3,0),(3,1),(3,2),(3,3)):
            n3=r-n4;n2=9-2*n3-3*n4;n1=23+n3+2*n4
            rawhigh=0;reps=set()
            for h3,h4 in product(combinations_with_replacement(options[3],n3),
                                 combinations_with_replacement(options[4],n4)):
                rawhigh+=1;reps.add(canon(h3+h4))
            accepted=[];uncovered=[];per_high=[];uses=Counter();blueuses=Counter()
            for oid,high in enumerate(sorted(reps)):
                hi=[sum(m>>i&1 for m in high) for i in range(7)]
                wi=[sum(m.bit_count()-1 for m in high if m>>i&1) for i in range(7)]
                cap=[min(8-ci[i]-hi[i],15-4*ci[i]-wi[i]) for i in range(7)]
                force=0
                for eid,(a,b) in enumerate(PAIRS):
                    ab=(1<<a)|(1<<b)
                    if not any(m&ab==ab for m in internal+high):force|=1<<eid
                total=0
                for ids,si,support in G[n2]:
                    if support&force!=force or any(si[i]>cap[i] for i in range(7)):continue
                    total+=1
                    ui=[8-ci[i]-hi[i]-si[i] for i in range(7)]
                    assert min(ui)>=0 and sum(ui)==n1
                    traces=internal+high+tuple(MASK(PAIRS[e]) for e in ids)+tuple(
                        1<<i for i in range(7) for _ in range(ui[i]))
                    assert len(traces)==35
                    witness=None
                    for blue in BLUES:
                        sig,codes=classify(traces,blue)
                        if sig is None:continue
                        tag=gate(sig)
                        if tag is None:continue
                        witness=[list(high),list(ids),[i for i in range(7) if blue>>i&1],tag,list(sig),codes]
                        uses[tag]+=1;blueuses[blue.bit_count()]+=1
                        break
                    if witness is None:uncovered.append([list(high),list(ids)])
                    else:accepted.append(witness)
                per_high.append({'id':oid,'high_masks':high,'necessary_J_checked':total})
            fname=f'{name}_r{r}_n4{n4}_WITNESSES.json'
            (HERE/fname).write_text(json.dumps(accepted,separators=(',',':'))+'\n')
            if uncovered:(HERE/fname.replace('WITNESSES','UNCOVERED')).write_text(json.dumps(uncovered)+'\n')
            row=dict(missing=name,r=r,n3=n3,n4=n4,n2=n2,n1=n1,aut_size=len(autos),C=C,
                     raw_high_multisets=rawhigh,high_orbits=len(reps),accepted=len(accepted),
                     uncovered=len(uncovered),gate_uses=dict(uses),blue_size_uses=dict(blueuses),
                     per_high=per_high,witness_file=fname)
            alljobs.append(row)
            print(name,r,n4,'orbits',len(reps),'accepted',len(accepted),'uncovered',len(uncovered),flush=True)
    result=dict(scope=__doc__,complete=True,domain='J sum, private nonnegative, PL capacity, P pair coverage; every such input gate-tested',
                edge_order=PAIRS,witness_encoding='[high masks, J edge ids, blue P set, gate, [P2,P3,P4,N3,N4], all 35 source-index categories]',
                jobs=alljobs,total=sum(j['accepted'] for j in alljobs),uncovered=sum(j['uncovered'] for j in alljobs),
                process_seconds=time.process_time()-started)
    (HERE/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
    assert result['uncovered']==0
    print('PASS',result['total'],result['process_seconds'],flush=True)

if __name__=='__main__':main()
