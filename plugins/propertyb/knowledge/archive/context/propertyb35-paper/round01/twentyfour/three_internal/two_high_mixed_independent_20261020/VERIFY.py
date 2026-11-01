"""Independent P3+K2 / 3K2, two-high complete actual P-side selection replay.
No discovery program or data imports. Integer standard-library calculations only.
"""
from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter
from pathlib import Path
import json
import time

HERE=Path(__file__).resolve().parent
PAIRS=tuple(combinations(range(7),2))
SHAPES=(('P3+K2',((0,1),(1,2),(3,4))),
        ('3K2',((0,1),(2,3),(4,5))))


def image(mask,p):
    return sum(1<<p[v] for v in range(7) if mask>>v&1)


def canonical(high,autos):
    return min(tuple(sorted(image(mask,p) for mask in high)) for p in autos)


def graph_domain(n):
    out=[]
    for edges in combinations_with_replacement(range(21),n):
        degree=[0]*7;mult=[0]*21;support=0
        for eid in edges:
            a,b=PAIRS[eid]
            degree[a]+=1;degree[b]+=1;mult[eid]+=1;support|=1<<eid
        out.append((edges,tuple(degree),tuple(mult),support))
    return out


def gate(m4,m3,t,b):
    assert min(m4,m3,t,b)>=0
    p=m4+m3
    if not p:return 'EMPTY'
    if p<=4 and t<=3:return 'SMALL4_T3'
    if p<=5 and t<=2:return 'SMALL5_T2'
    if m3==0:
        if m4<=5 and t<=10 and b<=32:return 'PURE5_T10_B32'
        if m4<=6 and t<=6 and b<=35:return 'PURE6_T6_B35'
        if m4<=7 and t<=4 and b<=22:return 'PURE7_T4_B22'
        if m4==8 and t<=4 and b<=17:return 'PURE8_T4_B17'
        if m4==8 and t<=3 and b<=20:return 'PURE8_T3_B20'
    if m3<=1 and p<=7:
        if t==0 and b<=21:return 'MIXED7_ONE3_T0_B21'
        if t<=1 and b<=20:return 'MIXED7_ONE3_T1_B20'
    if m4==7 and m3==1 and t==0 and b<=20:return 'MIXED8_ONE3_T0_B20'
    # Only the one-negative-triple theorem, not its new zero-triple extension.
    if p<=7 and m3<=2 and t<=1:return 'NEW_MIXED7_TWO3_T1_BANY'
    return None


def classify_every_index(internal,high,edges,private,blue):
    traces=list(internal)+list(high)
    traces.extend((1<<PAIRS[e][0])|(1<<PAIRS[e][1]) for e in edges)
    traces.extend(1<<v for v in range(7) for _ in range(private[v]))
    assert len(traces)==35
    counts=Counter()
    proper=0
    for mask in traces:
        hit=mask&blue
        if hit==mask:counts['P'+str(5-mask.bit_count())]+=1
        elif not hit:counts['N'+str(5-mask.bit_count())]+=1
        else:proper+=1
    assert set(counts)<={'P4','P3','N3','N4'},counts
    return (counts['P4'],counts['P3'],counts['N3'],counts['N4']),proper


def main():
    start=time.process_time()
    graphs={n:graph_domain(n) for n in (3,4,5)}
    gate_ids={}
    all_shapes=[]
    for name,F in SHAPES:
        st=time.process_time()
        support=sorted(set().union(*map(set,F)))
        C=sorted(set(range(7))-set(support))
        fset={frozenset(e) for e in F}
        autos=[]
        for perm in permutations(support):
            p=list(range(7))
            for a,b in zip(support,perm):p[a]=b
            if {frozenset((p[a],p[b])) for a,b in F}==fset:autos.append(p)
        internal=tuple(127^((1<<a)|(1<<b)) for a,b in F)
        c=[sum(mask>>v&1 for mask in internal) for v in range(7)]
        possible=[sum(1<<v for v in ss) for k in (3,4) for ss in combinations(support,k)]
        all_high=list(combinations_with_replacement(possible,2))
        reps=sorted({canonical(h,autos) for h in all_high})
        rows=[]
        for oid,high in enumerate(reps):
            n2=11-sum(mask.bit_count() for mask in high);n1=30-n2
            h=[sum(mask>>v&1 for mask in high) for v in range(7)]
            weight=[sum(mask.bit_count()-1 for mask in high if mask>>v&1) for v in range(7)]
            private_cap=[8-c[v]-h[v] for v in range(7)]
            exterior_cap=[15-4*c[v]-weight[v] for v in range(7)]
            required=sum(1<<eid for eid,(a,b) in enumerate(PAIRS)
                         if not any(mask>>a&1 and mask>>b&1 for mask in internal+high))
            blue_pairs=[(eid,a,b,(1<<a)|(1<<b)) for eid,(a,b) in enumerate(PAIRS)
                        if frozenset((a,b)) not in fset
                        and all(mask&((1<<a)|(1<<b)) for mask in high)]
            wide=pl=miss=0;uses=Counter();witnesses=[];misses=[]
            for edges,d,mult,edge_support in graphs[n2]:
                if any(d[v]>private_cap[v] for v in range(7)):continue
                if edge_support&required!=required:continue
                wide+=1
                if any(d[v]>exterior_cap[v] for v in range(7)):continue
                pl+=1
                private=[private_cap[v]-d[v] for v in range(7)]
                assert sum(private)==n1
                witness=None
                for bid,a,b,blue in blue_pairs:
                    counts=(private[a]+private[b],mult[bid],n2-d[a]-d[b]+mult[bid],
                            n1-private[a]-private[b])
                    tag=gate(*counts)
                    if tag is None:continue
                    independent,proper=classify_every_index(internal,high,edges,private,blue)
                    assert independent==counts
                    assert proper+sum(counts)==35
                    if tag not in gate_ids:gate_ids[tag]=len(gate_ids)
                    witness=[list(edges),bid,gate_ids[tag]]
                    uses[tag]+=1
                    break
                if witness is None:miss+=1;misses.append(list(edges))
                else:witnesses.append(witness)
            file=f'{name.replace("+","_")}_ORBIT_{oid:02d}_WITNESSES.json'
            (HERE/file).write_text(json.dumps(witnesses,separators=(',',':'))+'\n')
            if misses:(HERE/file.replace('WITNESSES','UNCOVERED')).write_text(json.dumps(misses)+'\n')
            rows.append(dict(id=oid,high_masks=high,high_sets=[[v for v in support if mask>>v&1] for mask in high],
                             n2=n2,n1=n1,private_degree_cap=private_cap,exterior_degree_cap=exterior_cap,
                             required_pairs=[PAIRS[e] for e in range(21) if required>>e&1],
                             raw_J=len(graphs[n2]),wide_J=wide,PL_J=pl,uncovered=miss,
                             gate_uses=dict(uses),witnesses_file=file))
        shape=dict(name=name,missing_pairs=F,C=C,D=support,internal_degrees=c,
                   support_automorphism_order=len(autos),raw_high_pairs=len(all_high),
                   high_orbits=len(reps),raw_J=sum(r['raw_J'] for r in rows),
                   wide_J=sum(r['wide_J'] for r in rows),PL_J=sum(r['PL_J'] for r in rows),
                   uncovered=sum(r['uncovered'] for r in rows),orbits=rows,
                   process_seconds=time.process_time()-st)
        all_shapes.append(shape)
        print(name,'orbits',len(reps),'wide',shape['wide_J'],'PL',shape['PL_J'],'miss',shape['uncovered'],flush=True)
    result=dict(complete=True,scope=__doc__,domain='J sum, private nonnegative, uncovered P pairs, exterior capacity; no other filters',
                witness_encoding='[nondecreasing J edge indices, blue pair index, gate id]',
                edge_order=PAIRS,gate_ids=gate_ids,used_zero_triple_extension=False,
                shapes=all_shapes,process_seconds=time.process_time()-start)
    (HERE/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
    assert all(not s['uncovered'] for s in all_shapes)
    print('PASS',result['process_seconds'],flush=True)


if __name__=='__main__':main()
