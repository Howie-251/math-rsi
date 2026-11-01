"""Complete n24/M35 two-seven-lock domain for codegree5..7; exact fixed-layout replay."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent; ROOT=HERE.parents[5]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
from multilock import json_value

def main():
    start=time.time(); cases=[]
    for c in (5,6,7):
        ns={0:21+c,1:7-c,2:7-c,3:c}; engine=SubsetEngine(24,2,ns)
        left=0; value=0
        for k in range(1,25):
            p=1 if k==11 else 2 if k==24 else 0
            value+=engine.value(k,left,p); left|=p
        cert=engine.verify(dict(bound=Q(value,engine.D),positions=[11,24],counts=engine.ns))
        assert cert['bound']<1 and all(z['loss']==0 for z in cert['certificates'])
        # Reconstruct 35 distinct edge indices directly from the degree equations.
        stubs=[frozenset(i+1 for i in range(2) if t>>i&1) for t,n in ns.items() for _ in range(n)]
        replay=independent_rows(24,(11,24),stubs)
        assert len(stubs)==35 and sum((r['bound'] for r in replay),Q())==cert['bound']
        cert.update(degrees=[7,7],codegree=c,strict=True,independent_bound=str(sum((r['bound'] for r in replay),Q())))
        cases.append(cert)
    out=dict(status='PASS',scope=__doc__,complete_codegree_domain=[5,6,7],cases=cases,elapsed_seconds=time.time()-start)
    (HERE/'STRONG_77_PAIR.json').write_text(json.dumps(json_value(out),indent=2)+'\n')
    print([(x['codegree'],str(x['bound'])) for x in cases])
if __name__=='__main__':main()
