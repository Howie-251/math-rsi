"""Fixed-witness exact certificates for all local rules and the complete delta=8 unit-star reduction."""
from pathlib import Path
import sys,json,itertools,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(HERE)]
from pilot import evaluate,double,triple,json_value
from unit_star_pilot import profile
from four_neighbor_pilot import partitions,canonical

def certify(z,label,extra=None):
 ns={int(k):v for k,v in z['counts'].items()}
 r=evaluate(19,ns,tuple(z['positions']),True)
 assert r['strict'] and str(r['bound'])==str(z['bound'])
 return dict(label=label,**(extra or {}),**r)

def main():
 start=time.time();out=[]
 pairdata=json.loads((HERE/'PAIR_SCAN.json').read_text())+json.loads((HERE/'TARGET_SCAN.json').read_text())
 tripledata=json.loads((HERE/'MIXED_SCAN.json').read_text())+json.loads((ROOT/'context/propertyb35-paper/round01/middle/PILOT.json').read_text())['triples']
 for b in range(11,29):
  r=evaluate(19,double(19,8,b,1),(1,2),True);assert r['strict'];out.append(dict(label='unit_partner_large',degrees=[8,b],codegree=1,**r))
 for ds,c0 in [([8,8],3),([8,9],4),([8,10],4),([9,9],4),([9,10],4),([10,10],4)]:
  for c in range(c0,min(ds)+1):
   z=next(z for z in pairdata if z['d']==ds and z['c']==c and z['strict'])
   r=evaluate(19,double(19,*ds,c),z['pos'],True);assert r['strict'];out.append(dict(label='unit_neighbours_strong_pair',degrees=ds,codegree=c,**r))
 targets=[([8,8,8],[1,1,1]),([8,8,8],[2,2,2]),([8,8,9],[1,1,1]),([8,8,9],[1,1,3])]
 targets +=[(d,[1,1,c]) for d,cs in [([8,8,10],[1,2,3]),([8,9,9],[1,2]),([8,9,10],[1,2]),([8,10,10],[1,2,3])] for c in cs]
 for ds,cs in targets:
  ts=[1] if ds==[8,8,8] and cs==[2,2,2] else [0,1]
  for t in ts:
   zs=[z for z in tripledata if z.get('d',z.get('degrees'))==ds and z.get('c',z.get('codegrees'))==cs and z.get('t',z.get('triple'))==t and z['strict']]
   assert zs,(ds,cs,t)
   z=zs[0];pos=z.get('pos',z.get('positions'));r=evaluate(19,triple(19,ds,cs,t),pos,True);assert r['strict']
   out.append(dict(label='unit_neighbours_triple_rule',degrees=ds,codegrees=cs,triple=t,**r))
 first=json.loads((HERE/'UNIT_STAR_PILOT.json').read_text())['profiles']
 for z in first:
  ns=profile(tuple(z['degrees'][1:]),z['partition'],z['t']);assert ns=={int(k):v for k,v in z['counts'].items()}
  if z['strict']:out.append(certify(z,'strict_three_neighbours',{k:z[k] for k in ['degrees','partition','t']}))
 second=json.loads((HERE/'FOUR_NEIGHBOR_PILOT.json').read_text())['profiles']
 for z in second:out.append(certify(z,'residual_four_neighbours',{k:z[k] for k in ['degrees','partition','triples','quadruple']}))
 result=dict(scope=__doc__,profile_count=len(out),all_strict=all(z['strict'] for z in out),independent_A_B_C_check=True,max_bound=max(z['bound'] for z in out),elapsed_seconds=time.time()-start,profiles=out)
 (HERE/'DELTA8_CERTIFICATE.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
 print(json.dumps(json_value({k:v for k,v in result.items() if k!='profiles'}),indent=2))
if __name__=='__main__':main()
