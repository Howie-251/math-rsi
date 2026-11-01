"""Independent replay of every serialized P-trace witness; no generator imports."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time

HERE=Path(__file__).resolve().parent
PAIRS=list(combinations(range(7),2))
FS={'P3_K2':((0,1),(1,2),(3,4)), '3K2':((0,1),(2,3),(4,5))}


def accepts(tag,p2,p3,p4,t,b):
    p=p2+p3+p4
    predicates={
        'PURE7_T4_B35':p2==p3==0 and p4<=7 and t<=4 and b<=35,
        'PURE6_T6_B35':p2==p3==0 and p4<=6 and t<=6 and b<=35,
        'PURE5_T10_B32':p2==p3==0 and p4<=5 and t<=10 and b<=32,
        'PURE8_T4_B17':p2==p3==0 and p4==8 and t<=4 and b<=17,
        'PURE8_T3_B20':p2==p3==0 and p4==8 and t<=3 and b<=20,
        'PURE8_T0_B27':p2==p3==t==0 and p4<=8 and b<=27,
        'SMALL5_T2':p2==0 and p<=5 and t<=2,
        'SMALL4_T8_B32':p2==0 and p<=4 and t<=8 and b<=32,
        'SMALL5_T2_AT_MOST_THREE_P2':p<=5 and p2<=3 and t<=2,
        'SMALL4_T3_ANYB':p<=4 and t<=3,
        'MIXED7_TWO3_T1_ANYB':p2==0 and p<=7 and p3<=2 and t<=1,
        'MIXED7_FOUR3_T0_ANYB':p2==0 and p<=7 and p3<=4 and t==0,
        'ELEVEN_P4_T0_B17':p2==p3==t==0 and p4<=11 and b<=17,
    }
    assert tag in predicates,tag
    return predicates[tag]


def main():
    started=time.process_time();src=json.loads((HERE/'RESULT.json').read_text())
    assert src['completed_all_jobs'] and src['first_nongated'] is None
    results=[];total=0;uses=Counter();blue_sizes=Counter();positive2=0
    for job in src['jobs']:
        F=FS[job['missing']];internal=[127 ^ ((1<<i)|(1<<j)) for i,j in F]
        ci=[sum(t>>i&1 for t in internal) for i in range(7)]
        C={i for i,c in enumerate(ci) if c==3}
        rows=json.loads((HERE/job['witnesses_file']).read_text());seen=set();local=Counter()
        assert len(rows)==job['accepted'] and job['completed']
        for hi,edges,blue,tag,stored in rows:
            key=tuple(hi),tuple(edges)
            assert key not in seen;seen.add(key)
            assert len(hi)==job['r'] and sum(t.bit_count()==4 for t in hi)==job['n4']
            assert all(t.bit_count() in (3,4) and not any(t>>i&1 for i in C) for t in hi)
            assert len(edges)==job['n2'] and edges==sorted(edges)
            J=Counter(edges);s=[0]*7
            for e,n in J.items():
                i,j=PAIRS[e];s[i]+=n;s[j]+=n
            h=[sum(t>>i&1 for t in hi) for i in range(7)]
            w=[sum(t.bit_count()-1 for t in hi if t>>i&1) for i in range(7)]
            private=[8-ci[i]-h[i]-s[i] for i in range(7)]
            assert min(private)>=0 and sum(private)==job['n1']
            assert all(s[i]+w[i]<=15-4*ci[i] for i in range(7))
            masks=internal+hi+[(1<<PAIRS[e][0])|(1<<PAIRS[e][1]) for e in edges]
            assert all(any(t>>i&1 and t>>j&1 for t in masks) for i,j in PAIRS)
            assert len(blue) in (2,3) and len(set(blue))==len(blue)
            B=set(blue);out=Counter()
            traces=[(set(i for i in range(7) if t>>i&1),1) for t in internal+hi]
            traces += [(set(PAIRS[e]),n) for e,n in J.items()]
            traces += [({i},n) for i,n in enumerate(private)]
            assert sum(n for T,n in traces)==35
            for T,n in traces:
                if not n:continue
                if T<=B:out['P',5-len(T)]+=n
                elif T.isdisjoint(B):out['N',5-len(T)]+=n
            assert set(out)<={('P',2),('P',3),('P',4),('N',3),('N',4)}
            values=[out['P',2],out['P',3],out['P',4],out['N',3],out['N',4]]
            assert values==stored and accepts(tag,*values)
            positive2+=out['P',2];local[tag]+=1;uses[tag]+=1;blue_sizes[len(blue)]+=1
        results.append(dict(missing=job['missing'],r=job['r'],n4=job['n4'],checked=len(rows),gate_uses=dict(local)))
        total+=len(rows)
    report=dict(PASS=True,total=total,blue_size_uses=dict(blue_sizes),
                positive_two_set_indices_in_accepted_witnesses=positive2,
                gate_uses=dict(uses),jobs=results,cpu_seconds=time.process_time()-started)
    (HERE/'SAVED_REPLAY.json').write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items() if k!='jobs'})


if __name__=='__main__':main()
