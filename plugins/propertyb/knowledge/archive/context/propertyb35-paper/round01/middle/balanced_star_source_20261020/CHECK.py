from math import comb
from fractions import Fraction
from pathlib import Path
import json,time
start=time.process_time()
def C(n,k):return comb(n,k) if n>=0 and 0<=k<=n else 0
rows=[]
for n,d,t in [(21,6,2),(22,7,3)]:
    N=n-1;a=N//2;e=4*d-N;F=N-8*t+e;den=C(N,a)
    assert e>=0 and 2*t<=d and F>=0
    witnesses=C(d,t)*C(d-t,t)
    # Count fixed-edge monochromatic balanced colorings directly on its N-5 free points.
    one_edge_num=C(N-5,a-5)+C(N-5,a)
    p=Fraction(one_edge_num,den)
    assert p==Fraction(C(a,5)+C(N-a,5),C(N,5))
    hbar_num=(35-d)*one_edge_num
    star_num=witnesses*C(F,F//2)
    total=Fraction(hbar_num+star_num,den)
    assert total<1
    # A strictly wider forced-color domain than actual selected link blocks.
    max_assignments=0;checked=0
    for r in range(N+1):
        for b in range(N-r+1):
            if r+b<8*t-e:continue
            f=N-r-b
            assert 0<=f<=F
            choices=C(f,a-r)
            assert choices<=C(F,F//2)
            max_assignments=max(max_assignments,choices);checked+=1
    # Central-binomial monotonic domination used in the proof.
    for f in range(F+1):
        for k in range(f+1):assert C(f,k)<=C(F,F//2)
    rows.append({'n':n,'d':d,'t':t,'N':N,'a':a,'link_excess':e,'F':F,
                 'candidate_colored_index_pairs':witnesses,'balanced_denominator':den,
                 'fixed_edge_bad_assignments':one_edge_num,'fixed_edge_bad_probability':str(p),
                 'hbar_bad_numerator':hbar_num,'star_bad_numerator_upper':star_num,
                 'total_numerator_upper':hbar_num+star_num,'total_probability_upper':str(total),
                 'strict_margin':str(1-total),'wider_forced_color_pairs_checked':checked,
                 'max_assignments_in_wider_forced_domain':max_assignments})
assert rows[0]['total_numerator_upper']==180474 and rows[0]['balanced_denominator']==184756
assert rows[1]['total_numerator_upper']==347368 and rows[1]['balanced_denominator']==352716
out={'status':'PASS_EXACT_SCALARS','rows':rows,'cpu_seconds':time.process_time()-start,
     'scope':'No hypergraph/link/negative-layout enumeration; Fraction arithmetic and small forced-color-count bounds only.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows:print('PASS',r['n'],r['d'],r['total_probability_upper'],'margin',r['strict_margin'])
