"""Small exact high-cohort relaxation for all fourteen r11 (q,a) faces."""
from pathlib import Path
from time import process_time
import json,sys

def faces():
    return [(q,a) for q in range(6) for a in range(12-2*q) if (a+2*q)%3==1]

def bounds(q,a,A,z):
    """Necessary caps on T=A+z inactive degree7/8 points."""
    T=A+z
    if a>=4:
        return A==0 and z<=3, (1 if a==4 else 0)
    if (q,a)==(0,1):
        return T<=4,0
    if (q,a)==(1,2):
        return T<=(2 if A else 3),1
    if (q,a)==(2,3):
        return T<=(2 if A else 3),0
    if (q,a)==(2,0):
        return T<=(3 if A else 4),1
    if (q,a)==(3,1):
        return T<=(2 if A else 4),0
    if (q,a) in ((4,2),(5,0)):
        return T<=1,1
    raise AssertionError((q,a))

def audit_face(q,a):
    R=11-2*q
    cap12=(11+R)//3
    out=[]
    for A in range(5):
        for z in range(5):
            valid,kmin=bounds(q,a,A,z)
            if not valid:
                continue
            T=A+z
            for Y in range(14-A-z):
                B=z+Y
                for C11 in range(5):
                    for C12 in range(4):
                        other=13-A-B-C11-C12
                        if other<0:
                            continue
                        minimum_excess=26-2*A-B+2*C11+3*C12
                        # a>0 low type B has only one non-F3 edge.
                        # If all high degrees <=9, its repetition occurs on a
                        # 9/9 F3 with a spoke, already excluded by the old formula.
                        if a>0 and C11+C12==0:
                            if other==0:
                                continue
                            minimum_excess+=1  # at least one degree-ten point
                        if minimum_excess>18:
                            continue
                        if Y>R-kmin*T:
                            continue
                        if Y>5*C11+cap12*C12:
                            continue
                        out.append(dict(A7=A,inactive8=z,active8=Y,C11=C11,
                                        C12plus=C12,other9or10=other,
                                        excess_lower_bound=minimum_excess,
                                        minimum_N8=Y))
    return dict(q=q,a=a,R=R,n1=a,n2=11-q-a,n3=(44+2*q+a)//3,
                cap12=cap12,aggregate_survivors=out)

def main():
    t0=process_time()
    domain=faces()
    assert len(domain)==14
    if "--profile" in sys.argv:
        domain=domain[:2]
    records=[audit_face(q,a) for q,a in domain]
    result=dict(status="PASS",scope="exact small integer necessary relaxation; not actual hypergraphs",
                complete=len(domain)==14,faces=records,
                cpu_seconds=process_time()-t0)
    name="PROFILE.json" if "--profile" in sys.argv else "AGGREGATE_RESULT.json"
    Path(__file__).with_name(name).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(dict(complete=result["complete"],
                          counts=[(r["q"],r["a"],len(r["aggregate_survivors"])) for r in records],
                          cpu_seconds=result["cpu_seconds"]),indent=2))

if __name__=="__main__":
    main()
