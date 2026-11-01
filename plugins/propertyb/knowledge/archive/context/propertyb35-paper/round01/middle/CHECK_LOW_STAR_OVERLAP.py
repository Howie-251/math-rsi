from fractions import Fraction
from math import comb
from pathlib import Path
import json

out={}
p23=Fraction(comb(11,5)+comb(12,5),comb(23,5))
p24=Fraction(2*comb(12,5),comb(24,5))
assert p23==p24==Fraction(6,161)
out['mono_probability']={'n23':str(p23),'n24':str(p24)}
out['unique_family_17_margin']=str(17*p23-2*(35*p23-1))
assert Fraction(out['unique_family_17_margin'])==Fraction(4,161)
out['source_thresholds']=[]
for n,start in [(24,5),(23,6)]:
    d=25-n
    for r in range(start,n+1):
        lower=(36*r+(r+5+d)-1)//(r+5+d)
        assert lower>=17
        out['source_thresholds'].append({'n':n,'r':r,'cauchy_lower':lower})
# These are only compatible scalar data, not actual H constructions.
out['scalar_obstructions']=[]
for n,R,B,E in [(24,7,16,23),(23,10,12,22)]:
    assert R+B==n-1
    assert E==n-1 and 174-2*E>=R*B
    out['scalar_obstructions'].append({'n':n,'R':R,'B':B,'E':E,
                                      'cross_associations':174-2*E,
                                      'cross_required':R*B})
assert 174-2*23<11*12
out['n24_three_three_excluded']={'E_lower':23,'E_upper':(174-11*12)//2}
# Fully explicit link families for the compatible scalar obstructions.
for n in (24,23):
    redblocks=2 if n==24 else 3
    link=[]
    nextv=1
    for _ in range(redblocks):
        link.append([0,nextv,nextv+1,nextv+2]);nextv+=3
    red=set().union(*(set(a) for a in link))
    for _ in range(6-redblocks):
        link.append(list(range(nextv,nextv+4)));nextv+=4
    union=set().union(*(set(a) for a in link))
    assert len(union)==n-1 and sum(map(len,link))-len(union)==25-n
    out[f'explicit_link_n{n}']={'blocks':link,'red':sorted(red),
                              'red_count':len(red),'blue_count':len(union-red),
                              'only_link_and_scalar_witness':True}
# Actual low-trace sufficient examples from (6).
assert 6*4-comb(4,2)-2+1==17
assert 6*4-comb(4,2)-4+3==17
out['trace_conditions']={'n24_r4_W2_Q1_lower':17,'n23_r4_C4_quad_lower':17}
out['status']='PASS_SCALARS_ONLY_NOT_H_REALIZATION'
p=Path(__file__).with_name('LOW_STAR_OVERLAP_SCALARS.json')
p.write_text(json.dumps(out,indent=2)+'\n')
print(out['status'], 'p=',p23,'unique17_margin=',out['unique_family_17_margin'])
