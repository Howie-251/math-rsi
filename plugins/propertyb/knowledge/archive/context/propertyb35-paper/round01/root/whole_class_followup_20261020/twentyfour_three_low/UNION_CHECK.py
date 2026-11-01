"""Refined caller parameters and small shared-budget arithmetic, no H search."""
from pathlib import Path
from time import process_time
import json

def dr(m):
    return max(55*max(m-1,0),1595 if m>=6 else 0,2035 if m>=7 else 0)

def db(m):
    return max(11*max(m-1,0),616 if m>=7 else 0)

def oriented(du,dv,p,su,sv,a):
    return (77681+243*p+2002*du-1822*su+948*sv-5005*a
            -dr(du-1-su-a)-db(dv-1-sv-a))

def refined(du,dv,p,su,sv,a):
    return min(oriented(du,dv,p,su,sv,a),oriented(dv,du,p,sv,su,a))

def valid_rows(du,dv):
    for p in (0,1):
        for su in range(4-2*p):
            for sv in range(4-2*p-su):
                for a in range(min(du,dv)):
                    if min(du-1-su-a,dv-1-sv-a,21+p-du-dv+su+sv+a)>=0:
                        yield (refined(du,dv,p,su,sv,a),p,su,sv,a)

def main():
    start=process_time()
    seven=[]
    for d in range(7,36):
        for row in valid_rows(7,d):
            seven.append((row[0],d,*row[1:]))
    assert max(seven)[0]==92328 <92378
    eight={}
    necessary_rows=0
    for d in range(8,36):
        rows=list(valid_rows(8,d))
        if rows:
            eight[str(d)]=max(rows)
        for total,p,su,sv,a in rows:
            necessary_rows+=1
            if total>=92378:
                assert a==0 and su==0 and p==0 and sv in (2,3) and d>=9+sv
    assert [eight[str(d)][0] for d in (8,9,10)]==[91289,91469,92237]
    assert refined(8,11,0,0,2,0)==92942
    assert refined(9,9,1,0,0,0)==93291
    # q=0, r=12. A=#7, z/y/x are #8 with (a3,a2)=(0,6)/(2,3)/(4,0).
    # The proof first forces H=1; retain unique-big incident-triple cap N<=8.
    survivors=[]
    for A in range(3):
        for z in range(3):
            for y in range(7):
                for x in range(7):
                    B=z+y+x
                    N=2*y+4*x
                    for H in range(13-A-B):
                        if A+z>2 or 2*(A+z)+y>6 or N>12:
                            continue
                        if 2*A+B-2*H<5:
                            continue
                        if y+x>0 and H==0:
                            continue
                        assert A in (1,2) and H==1
                        if N>8:
                            continue
                        survivors.append(dict(A=A,B=B,H=H,z=z,y=y,x=x,N=N))
    assert survivors==[dict(A=2,B=3,H=1,z=0,y=2,x=1,N=8)]
    # This last arithmetic face forces dw=11,Kw=12, hence s_big=3 on every
    # w-triple, which the actual refined gate strictly closes.
    assert refined(8,11,0,0,3,0)==91586 <92378
    # q=3 forces n8<=3 by charge, but degree sum forces n8>=5.
    assert 2*4>6 and 24-3>19
    # q=6 forces all 12 high points to degree at least nine.
    assert 12*9>103
    result=dict(status="PASS",scope="refined caller and shared r12 budget arithmetic only",
                imported_bounds=dict(red6=1595,red7=2035,blue7=616),
                seven_all_d_worst=max(seven),seven_parameter_rows=len(seven),
                eight_maxima=eight,eight_necessary_condition_rows=necessary_rows,
                eight_eight_to_ten_margins={str(d):92378-eight[str(d)][0] for d in (8,9,10)},
                first_eight_eleven_unclosed_parameter=dict(p=0,s8=0,sbig=2,alpha=0,bound=92942),
                q0_aggregate_survivor_before_last_gate=survivors,
                last_face_failure_bound=91586,r12_faces_closed=[0,3,6],
                original_hypergraphs_enumerated=0,cpu_seconds=process_time()-start)
    Path(__file__).with_name("UNION_RESULT.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="eight_maxima"},indent=2))

if __name__=="__main__":
    main()
