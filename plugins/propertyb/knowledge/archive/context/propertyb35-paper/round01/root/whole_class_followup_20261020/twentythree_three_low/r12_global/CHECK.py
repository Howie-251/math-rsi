"""Only scalar low-trace identities and two exact aggregate obstruction rows.
No original-H construction, local coloring menu, DP or optimization solver.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
domains=[]
for E in range(7):
    n2=6-E
    numerator=72-2*n2
    if numerator%3:continue
    n3=numerator//3;n0=35-n2-n3;bad=2*E;good=n3-bad
    ps=[p for p in range(3,12) if 12*p<=3*(2*bad)+2*(3*n2)]
    domains.append({'E':E,'n1':0,'n2':n2,'n3':n3,'n0':n0,'bad_triples':bad,'unit_triples':good,
                    'possible_p_by_low_high_incidence':ps,'R_degree_sum_upper':{str(p):10*p-7 for p in ps}})
assert [z['E'] for z in domains]==[0,3,6]
assert domains[0]['possible_p_by_low_high_incidence']==[3]
assert domains[1]['possible_p_by_low_high_incidence']==[3,4]
assert domains[2]['possible_p_by_low_high_incidence']==[3,4,5,6]
witnesses=[]
for E,Rdegrees,Qdegrees,rows in [
 (3,[8,8,8,9],[10]*7,[(0,2,3,5),(0,1,4,5),(2,2,1,3),(3,2,0,6),(3,0,2,16)]),
 (6,[8,9,9,9,9,9],[10]*5,[(0,3,2,7),(0,2,3,4),(3,2,0,12),(3,0,2,12)])]:
    # row=(low count, R count, Q count, multiplicity); all 35 original
    # edges represented only by class occupancies, not by actual point sets.
    assert sum(m for l,r,q,m in rows)==35
    assert all(l+r+q==5 for l,r,q,m in rows)
    p=len(Rdegrees);q=len(Qdegrees);DR=sum(Rdegrees);DQ=sum(Qdegrees)
    assert p+q==11 and DR+DQ==103
    assert sum(l*m for l,r,q,m in rows)==72
    assert sum(r*m for l,r,q,m in rows)==DR
    assert sum(q*m for l,r,q,m in rows)==DQ
    RR=sum(r*(r-1)//2*m for l,r,q,m in rows)
    QQ=sum(q*(q-1)//2*m for l,r,q,m in rows)
    RQ=sum(r*q*m for l,r,q,m in rows)
    LR=sum(l*r*m for l,r,q,m in rows);LQ=sum(l*q*m for l,r,q,m in rows)
    WRR=RR-p*(p-1)//2;WQQ=QQ-q*(q-1)//2;WRQ=RQ-p*q
    assert min(WRR,WQQ,WRQ)>=0
    assert 2*WRR+WRQ+(LR-12*p)==4*DR-22*p
    assert 2*WQQ+WRQ+(LQ-12*q)==4*DQ-22*q
    assert WRR+WQQ+WRQ+E+(LR+LQ-12*11)==97
    assert all(r==0 for l,r,q,m in rows if l==3 and q==2)
    witnesses.append({'E':E,'R_degrees':Rdegrees,'Q_degrees':Qdegrees,'class_edge_rows':rows,
                      'low_R_incidence':LR,'low_Q_incidence':LQ,'RR_pair_incidence':RR,'QQ_pair_incidence':QQ,
                      'RQ_pair_incidence':RQ,'RR_excess':WRR,'QQ_excess':WQQ,'RQ_excess':WRQ,
                      'low_R_excess':LR-12*p,'low_Q_excess':LQ-12*q,
                      'warning':'class-incidence witness only, not an actual H or a noncolorability example'})
out={'status':'PASS','scope':__doc__,'domains':domains,'aggregate_obstructions':witnesses,
     'CPU_seconds':time.process_time()-start}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
