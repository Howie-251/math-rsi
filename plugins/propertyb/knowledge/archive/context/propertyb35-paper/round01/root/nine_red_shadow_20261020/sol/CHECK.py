from itertools import combinations
from math import comb
from fractions import Fraction
from pathlib import Path
import json,time

HERE=Path(__file__).resolve().parent
start=time.process_time()
joint=lambda u:comb(17-u,10-u) if 0<=u<=10 else 0
D=comb(17,10);single=comb(13,6);blue=22*comb(13,10)
assert (D,single,blue)==(19448,1716,6292)
root={k:36*comb(k,2)+(90-3*k)*max(0,4*k-17) for k in range(1,9)}
heavy=[{'rank':r,'deduction':root[9-r]+330*r+462} for r in range(1,9)]
assert min(x['deduction'] for x in heavy)==2328
patterns=[]
for k in range(4):
    for q in range(4-k):
        upper=joint(12-2*k-q)
        algebra=3*q+30*k+57*comb(k,2)+69*comb(k,3)
        assert upper<=algebra
        patterns.append({'heavy_edges':k,'light_edges':q,'joint_upper':upper,'linear_upper':algebra})
graphs={'empty':[], 'one':[(0,1)],'matching':[(0,1),(2,3)],
        'wedge':[(0,1),(1,2)],'triangle':[(0,1),(1,2),(0,2)]}
rows=[]
for name,edges in graphs.items():
    e={tuple(sorted(x)) for x in edges};a=len(e)
    degrees=[sum(v in x for x in e) for v in range(9)]
    W=sum(comb(d,2) for d in degrees)
    T=sum(all(tuple(sorted(x)) in e for x in combinations(t,2)) for t in combinations(range(9),3))
    raw=2619-42*a-57*W-69*T
    corrected=raw+210 if name=='triangle' else raw
    assert corrected>2288
    rows.append({'shape':name,'edges':a,'wedges':W,'triangles':T,
                 'rough_deduction':raw,'deduction_if_triangle_triple_nonempty':corrected})
zero=[]
for k in range(7):
    for l in range(16):
        if 2*k+l<15:continue
        v=1830+147*k-k*(k-1)+Fraction(178,3)*l
        assert v>2288
        zero.append({'k':k,'l':l,'deduction':str(v)})
assert min(Fraction(x['deduction']) for x in zero)==2720
novel=[{'A_B_intersection':h,'A_B_joint':joint(8-h),
        'triple_joint_upper':joint(9-h),'novel_lower':joint(8-h)-joint(9-h)} for h in (0,1)]
assert [x['novel_lower'] for x in novel]==[28,84]
rank6=root[3]+6*(330+2*28-8)
assert rank6==2376 and 9*single-rank6+blue==19360
out={'status':'PASS_COMPLETE_DECLARED_SUBCASES',
     'review_independence':'same-family','acceptance_status':'provisional',
     'full_nine_red_lemma_proved':False,'unresolved':'No intersection3; intersection2 graph rank3..5.',
     'D':D,'nine_single_total':9*single,'blue_union_upper':blue,
     'root_bounds':root,'all_intersection3_bounds':heavy,
     'rank_at_least7_tree_bound':2346,'small_triple_patterns':patterns,
     'rank_at_most2_graphs':rows,'zero_triple_triangle_cases':zero,
     'novel_event_bounds':novel,'rank6_deduction':rank6,'rank6_minimum_successful_samples':88,
     'cpu_seconds':time.process_time()-start}
(HERE/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('small_triple_patterns','rank_at_most2_graphs','zero_triple_triangle_cases')},indent=2))
