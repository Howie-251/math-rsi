"""Small exact parameter audit; imports the already independently checked 12324."""
from itertools import combinations
from math import comb
from pathlib import Path
from time import process_time
import json

def score(du,dv,p,su,sv,alpha):
    return 243*p-5005*alpha+min(
        2002*du-1822*su+948*sv,
        2002*dv-1822*sv+948*su)

def structures():
    for p in (0,1):
        for su in range(4-2*p):
            for sv in range(4-2*p-su):
                yield p,su,sv

def main():
    t0=process_time()
    structures_all=list(structures())
    assert len(structures_all)==13
    algebra_rows=0
    for M in (34,35):
        for du in range(6,13):
            for dv in range(6,13):
                for alpha in range(min(du,dv)):
                    for p,su,sv in structures_all:
                        classes=(alpha,du-1-su-alpha,dv-1-sv-alpha,
                                 M-14+p-du-dv+su+sv+alpha)
                        if min(classes)<0:
                            continue
                        assert sum(classes)==M-16+p
                        free=12324*p+7722*su+8490*sv+7542*(3-2*p-su-sv)
                        assert free==22626-2760*p+180*su+948*sv
                        fixed=5005*classes[1]+3003*(classes[2]+classes[3])
                        assert fixed==3003*(M-16+p-alpha)+2002*(du-1-su-alpha)
                        total=free+fixed
                        assert total==3003*M-27424+243*p+2002*du-1822*su+948*sv-5005*alpha
                        if M==35:
                            assert total==77681+243*p+2002*du-1822*su+948*sv-5005*alpha
                        algebra_rows+=1
    corollaries={}
    for du,dv in ((7,7),(7,8)):
        rows=[score(du,dv,p,su,sv,a) for p,su,sv in structures_all
              for a in range(min(du,dv))]
        assert max(rows)<=14696
        corollaries[f"{du}/{dv}"]=dict(maximum_score=max(rows),
                                        maximum_total=77681+max(rows),
                                        margin=92378-77681-max(rows),
                                        parameter_rows=len(rows))
    necessary_rows=0
    failed_rows=0
    for dv in range(7,36):
        for alpha in range(7):
            for p,su,sv in structures_all:
                necessary_rows+=1
                if score(7,dv,p,su,sv,alpha)>14696:
                    failed_rows+=1
                    assert alpha==0 and su==0 and 1<=sv<=3-2*p and dv>=8+sv
    # Exact low-projection consequence for r=12 after all four-low edges excluded.
    low_rows={}
    for epsilon in (0,1):
        rows=[(x1,x2,x3) for x1 in range(7) for x2 in range(7) for x3 in range(7)
              if x1+x2+x3==6 and x2+2*x3==11+epsilon]
        assert rows==([(0,1,5)] if epsilon==0 else [(0,0,6)])
        low_rows[str(epsilon)]=rows
    r12=[]
    for q in range(7):
        n2=6-q
        if (60+2*q)%3==0:
            n3=(60+2*q)//3
            r12.append(dict(q_LL=q,n1=0,n2=n2,n3=n3))
    assert [row["q_LL"] for row in r12]==[0,3,6]
    # Aggregate obstruction to deriving an improved r-cutoff from these counts alone.
    high_types=[dict(count=5,d=8,a3=4,a2=0,k=0,pure=4),
                dict(count=3,d=9,a3=3,a2=3,k=3,pure=3),
                dict(count=3,d=9,a3=3,a2=2,k=1,pure=4),
                dict(count=1,d=9,a3=2,a2=3,k=0,pure=4)]
    for row in high_types:
        assert row["a3"]+row["a2"]+row["pure"]==row["d"]
        assert 3*row["a3"]+2*row["a2"]==12+row["k"]
    totals={key:sum(row["count"]*row[key] for row in high_types)
            for key in ("d","a3","a2","k","pure")}
    assert totals==dict(d=103,a3=40,a2=18,k=12,pure=45)
    assert score(8,9,0,0,0,0)>14696 and score(8,9,0,0,1,0)>14696
    out=dict(status="PASS",scope="caller algebra and necessary parameter implications only; no H enumeration",
             feasible_nonnegative_table_rows=algebra_rows,corollaries=corollaries,
             necessary_condition_rows=necessary_rows,rows_not_closed_by_gate=failed_rows,
             r12_local_rows=low_rows,r12_possible_low_count_faces=r12,
             aggregate_obstruction=dict(high_types=high_types,totals=totals,
                                       actual_H_realization_claimed=False),
             cpu_seconds=process_time()-t0)
    Path(__file__).with_name("RESULT.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ("aggregate_obstruction","r12_local_rows")},indent=2))

if __name__=="__main__":
    main()
