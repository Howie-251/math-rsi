"""Check explicit common-column relaxation witnesses; not actual hypergraphs."""
from pathlib import Path
import json,time

HERE=Path(__file__).resolve().parent
start=time.process_time()
specs=[(20,[8,5,5,6,7],[[2,1,1,1,2]]*9),
       (22,[8,5,6,6,6],[[2,1,2,1,1]]*9),
       (24,[9,5,5,6,6],[[2,2,1,1,1]]*4+[[2,1,2,1,1]]*5)]
exceptional_outside=[[1,1,1,0,0],[1,1,1,0,0],
                     [1,1,0,1,1],[1,0,1,1,1]]
rows=[]
for source,a,low in specs:
    # Four clean degree9 rows, followed by P0,P1,y,z; the latter have r=1.
    matrix=[[1]*5 for _ in range(4)]+[[0,0,0,1,1],[0,0,0,1,1],
                                      [0,0,1,0,0],[0,1,0,0,0]]
    targets=[9]*4+[7,6,6,6]
    remaining=[4*a[i]-sum(row[i] for row in low+matrix) for i in range(5)]
    for row,target in zip(matrix,targets):
        for _ in range(target-sum(row)):
            eligible=[i for i in range(5) if remaining[i]>0 and row[i]<a[i]]
            assert eligible
            i=max(eligible,key=lambda i:(remaining[i],-row[i]))
            row[i]+=1;remaining[i]-=1
    assert remaining==[0]*5
    incidence=low+matrix
    extra=[[0]*5 for _ in range(13)]+exceptional_outside
    r=[0]*13+[1]*4
    degrees=[sum(row)+rv for row,rv in zip(incidence,r)]
    assert degrees==[7]*9+[9]*4+[8,7,7,7]
    assert sum(degrees)==128 and sum(d-7 for d in degrees)==9
    assert all(sum(row[i] for row in incidence)==4*a[i] for i in range(5))
    assert all(0<=row[i]<=a[i] for row in incidence for i in range(5))
    assert all(incidence[w][i]+extra[w][i]>=1 for w in range(17) for i in range(5))
    assert all(sum(row)==7 for row in low)
    assert len(low)==9 and len(incidence)==17
    selected_degrees=[a[0]+4]+[x+3 for x in a[1:]]
    assert sum(selected_degrees)+sum(degrees)==175
    rows.append({'source':source,'a':a,'F_degrees':selected_degrees,
                 'D':4,'C':13,'h':9,'clean7_rows':low,
                 'other_clean_rows':matrix[:4],
                 'dirty_rows_P0_P1_y_z':matrix[4:],
                 'dirty_exceptional_F_incidence':exceptional_outside,
                 'outside_degrees':degrees,'column_totals':[4*x for x in a],
                 'scope':'Satisfies common c_i column constraints and F/outside pair-cover minima only; not an actual H or counterexample.'})
out={'status':'PASS_THREE_COLUMN_RELAXATION_WITNESSES',
     'review_independence':'same-family','acceptance_status':'provisional',
     'new_probability_layouts':0,'old175_clean8_replays':False,
     'actual_gamma4_branch_closed':False,'witnesses':rows,
     'cpu_seconds':time.process_time()-start}
(HERE/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'},indent=2))
