"""Bounded M35 real-edge small-lock pilot, n21 degree8 and n23 degree7; not a free five-lock catalogue."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[3]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from pilot import evaluate,double,triple
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
from multilock import json_value

def main():
    start=time.time();out=[];impossible=[]
    cases=[]
    for n,d in [(21,8),(23,7)]:
        for c in range(1,d+1):cases.append((n,[d,d],f'pair_c{c}',double(n,d,d,c)))
        cases.append((n,[d]*3,'three_pair111_common1',triple(n,[d]*3,(1,1,1),1)))
        for s in (4,5):
            ns={0:35-1-s*(d-1),(1<<s)-1:1}|{1<<i:d-1 for i in range(s)}
            if min(ns.values())<0:impossible.append(dict(n=n,degrees=[d]*s,case=f'{s}_common1_other_single',counts=ns,reason='negative empty trace forced'))
            else:cases.append((n,[d]*s,f'{s}_common1_other_single',ns))
    for n,ds,tag,ns in cases:
        en=SubsetEngine(n,len(ds),ns);proposal=en.solve();z=evaluate(n,ns,tuple(proposal['positions']),True)
        assert z['bound']==proposal['bound']
        # Independent35-edge-label injection formula; quotas verified separately.
        stubs=[frozenset(i+1 for i in range(len(ds)) if t>>i&1) for t,c in ns.items() for _ in range(c)]
        rr=independent_rows(n,tuple(proposal['positions']),stubs)
        assert len(stubs)==35
        assert all((r['A'],r['B'],r['C'])==(a['A'],a['B'],a['C']) for r,a in zip(z['rows'],rr))
        assert z['bound']==sum((min(r['A'],r['B'],r['C']-a['deduction']) for r,a in zip(rr,z['rows'])),Q())
        z.update(degrees=ds,case=tag,independent_injection=True,subset_dp_layout_optimal=True);out.append(z)
        print(n,tag,str(z['bound']),z['strict'],z['positions'])
    result=dict(scope=__doc__,status='PASS',cases=out,impossible_trace_inputs=impossible,elapsed_seconds=time.time()-start)
    (HERE/'LOW_EDGE_PILOT.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
    print('elapsed',result['elapsed_seconds'])
if __name__=='__main__':main()
