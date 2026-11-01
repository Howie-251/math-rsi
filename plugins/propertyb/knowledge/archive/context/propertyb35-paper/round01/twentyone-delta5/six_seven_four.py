"""x5 plus p6,q7 and two degree8 neighbours after the unique 6/7/8 residual; complete shared four-neighbour domain."""
from pathlib import Path
import sys,itertools,time,json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
# star_low has no run-on-import side effects and provides exact actual unit-star recovery.
from star_low import parts,recover,SubsetEngine,json_value
HERE=Path(__file__).parent

def main():
 st=time.time();out=[]
 for c in (1,2):
  for pp in [((0,1),(2,3)),((0,1),(2,),(3,))]:
   for a,b in itertools.product((0,1),repeat=2):
    high={7:0,11:0,13:a,14:b,15:0};ns=recover(5,[6,7,8,8],[2,1,1,1,1,c],pp,high)
    if ns is None:continue
    eng=SubsetEngine(21,5,ns);z=eng.verify(eng.solve());z.update(neighbor_degrees=[6,7,8,8],neighbor_codegrees=[2,1,1,1,1,c],center_partition=pp,neighbor_triples=[0,0,a,b],neighbor_quadruple=0,strict=z['bound']<1);out.append(z);print(c,pp,a,b,z['bound'],flush=True)
 (HERE/'SIX_SEVEN_FOUR_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('domain',len(out),'strict',sum(r['strict'] for r in out),'seconds',time.time()-st)
if __name__=='__main__':main()
