"""Small deterministic checks for source identities; no source/H classification."""
from itertools import combinations,product
from pathlib import Path
import json,time

HERE=Path(__file__).resolve().parent
start=time.process_time()
# h=0 is red, y=1 is blue. The other red points and blue points just
# distinguish actual edge indices/owners in the complete five-subset domain.
red={0,2,3,4,9}; blue={1,5,6,7,8}
newred=(red-{0})|{1}
transition=[]
for edge in combinations(range(10),5):
    e=set(edge);j=len(e&blue)
    if not 1<=j<=4:continue
    if j==4 and 0 in e:continue # h is a sink
    if j==1 and 1 in e and 0 not in e:continue # F_y contains h
    oldowner=next(iter(e&red)) if j==4 else None
    newblue=(set(range(10))-newred)
    jj=len(e&newblue)
    assert 1<=jj<=4
    newowner=next(iter(e&newred)) if jj==4 else None
    expected=None
    if j==4 and 1 not in e:expected=oldowner
    if j==3 and 0 in e and 1 not in e:expected=next(iter((e&red)-{0}))
    assert newowner==expected and newowner!=1
    transition.append({'edge':edge,'old_blue_count':j,'new_blue_count':jj,
                       'old_red_owner':oldowner,'new_red_owner':newowner})

# The pairwise cut identity is linear in arbitrary nonnegative pair weights.
cutchecks=[]
for pair in combinations(range(10),2):
    e=set(pair)
    old=int(len(e&red)==1);new=int(len(e&newred)==1)
    rowh=int(0 in e);rowy=int(1 in e)
    crossh=int(0 in e and old);crossy=int(1 in e and old)
    both=int(e=={0,1})
    assert new-old==rowh+rowy-2*crossh-2*crossy+2*both
    cutchecks.append(pair)

# q_i = total private multiplicity of blue owner i; m_i = number of its
# private indices incident to a given h. D is the minimum duplicate cost.
ownerchecks=0
for b in range(1,6):
    for q in product(range(1,6),repeat=b):
        u=sum(x-1 for x in q)
        if u>4:continue
        for m in product(*(range(x+1) for x in q)):
            a=sum(m);D=sum(max(0,x-1) for x in m)
            Y=sum(qi==1 and mi==1 for qi,mi in zip(q,m))
            assert Y>=max(0,a-u-min(u,D))
            ownerchecks+=1

beta=[]
for B in range(6,15):
    cases=[]
    for a in range(7):
        bh=18-B-2*a;c=B-12+a
        if bh<0 or c<0 or a+bh+c!=6:continue
        need=bh+a*(a-1)//2
        cases.append({'a':a,'t_h':bh,'n3_h':c,'N2_lower':need})
    minimum=min(k['N2_lower'] for k in cases)
    assert minimum>=15-B
    if B in (6,7,8):assert minimum=={6:15,7:11,8:8}[B]
    else:
        tight=[k for k in cases if k['N2_lower']==15-B]
        assert all(k['a'] in (2,3) for k in tight)
    beta.append({'beta':B,'minimum_N2':minimum,'all_low_star_cases':cases})

out={'status':'PASS_COMMON_SOURCE_LOCAL_IDENTITIES',
     'review_independence':'same-family','acceptance_status':'provisional',
     'proper_edge_transition_cases':len(transition),'transitions':transition,
     'weighted_pair_cut_checks':len(cutchecks),
     'private_owner_multiplicity_checks':ownerchecks,
     'private_owner_check_domain':{'blue_owners':'1..5','each_private_multiplicity':'1..5','total_extra_private':'0..4','h_incidence':'0..q_i'},
     'effective_beta_domain':beta,
     'new_layouts':0,'new_actual_branch_closure':False,
     'cpu_seconds':time.process_time()-start}
(HERE/'SOURCE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('transitions','effective_beta_domain')},indent=2))
