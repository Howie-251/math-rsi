"""Independent center-edge-union plus explicit three-high Mobius reconstruction of all mixed unit modes.
No full five-point inclusive inversion, position DP, or optimizer is called.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parent))
from replay_r3 import fixed,joint

def key(ns):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(32))
def main():
 start=time.time();Ps=[]
 for word in product(range(3),repeat=3):
  if word[0] or any(word[i]>max(word[:i])+1 for i in (1,2)):continue
  Ps.append(tuple(sum(1<<i for i,x in enumerate(word) if x==j) for j in range(max(word)+1)))
 assert len(Ps)==5;inc=lambda P,A:int(any(B&A==A for B in P));modes=[('u8_10_10',[8,10,10],False,False,2486,824),('u8_10_11',[8,10,11],False,False,2486,1463),('u8_8_10',[8,8,10],True,False,281,102),('u8_8_11',[8,8,11],True,False,281,102),('p8_8_10',[8,8,10],True,True,41,26)];summaries=[]
 # The pair exclusions used to put every inclusive high pair into1..4.
 old=json.loads((HERE.parents[1]/'DIAGNOSIS.json').read_text())['pairs'];strong=[]
 for r in old:
  if tuple(r['degrees']) in ((8,8),(8,10),(10,10)) and r['codegree']>=5:assert fixed(r)<1;strong.append((r['degrees'],r['codegree']))
 new=json.loads((HERE/'MIXED_STRONG_PAIRS.json').read_text())['cases']
 for r in new:assert fixed(r)<1;strong.append((r['degrees'],r['codegree']))
 assert len(strong)==24
 for name,deg,separated,paired,nlabel,norbit in modes:
  expected=set();partitions=[(1,2,4)] if paired else [P for P in Ps if not separated or not inc(P,3)]
  for P1,P2 in product(partitions,repeat=2):
   for c12,c13,c23 in product((2,) if separated else range(1,5),range(1,5),range(1,5)):
    for tt in range(min(c12,c13,c23)+1):
     high={1:deg[0],2:deg[1],4:deg[2],3:c12,5:c13,6:c23,7:tt}
     if paired:J=dict(high);J[1]-=2;J[2]-=2;J[4]-=1
     else:J={A:v-inc(P1,A)-inc(P2,A) for A,v in high.items()}
     nn={7:J[7],3:J[3]-J[7],5:J[5]-J[7],6:J[6]-J[7],1:J[1]-J[3]-J[5]+J[7],2:J[2]-J[3]-J[6]+J[7],4:J[4]-J[5]-J[6]+J[7]};nn[0]=23-sum(nn.values())
     if min(nn.values())<0:continue
     ns={A<<2:v for A,v in nn.items()}
     if paired:
      ns.update({3:1,19:1,1:3,2:3,5:1,9:1,6:1,10:1})
     else:
      ns[3]=2
      for i,P in enumerate((P1,P2)):
       ns[1<<i]=5-len(P)
       for B in P:ns[(1<<i)|(B<<2)]=1
     assert sum(ns.values())==35
     expected.add(key(ns))
  dom=json.loads((HERE/(name+'_DOMAIN.json')).read_text());assert len(expected)==nlabel and expected=={key(r['counts']) for r in dom['labelled']} and len(dom['orbits'])==norbit
  for r in dom['labelled']:
   ns={int(t):v for t,v in dom['orbits'][r['orbit']]['counts'].items()};p=r['from_representative_high_permutation'];swap=r['from_representative_low_swap'];assert [deg[i] for i in p]==deg
   def move(t):return ((((t&1)<<1)|((t&2)>>1)) if swap else(t&3))|sum(1<<(p[i]+2) for i in range(3) if t>>(i+2)&1)
   assert key({move(t):v for t,v in ns.items()})==key(r['counts'])
  filename=name+('_TRANSFER.json' if name=='u8_10_11' else '_DP.json');data=json.loads((HERE/filename).read_text());assert data['complete'] and len(data['cases'])==norbit;values={};pure=0;overrides=0
  for r in data['cases']:
   assert key(r['counts'])==key(dom['orbits'][r['id']]['counts']);v=fixed(r);values[r['id']]=v;pure+=int(v<1)
  if name=='u8_10_11':
   fixes=json.loads((HERE/'u8_10_11_FAILED_TRANSFER_DP.json').read_text())['cases'];assert len(fixes)==13
   for r in fixes:
    assert key(r['counts'])==key(dom['orbits'][r['id']]['counts']);v=fixed(r);assert v<1;values[r['id']]=v;overrides+=1
  else:
   for z in json.loads((HERE/(name+'_JOINT.json')).read_text())['results']:
    verified=joint.verify(z,v=20,s=5,expected_degrees=[7,7,*deg]);values[z['source_id']]=Q(verified['bound']);overrides+=1
  assert all(v<1 for v in values.values())
  summary=dict(mode=name,labelled_count=nlabel,orbit_count=norbit,transport_checks=nlabel,fixed_first_pass_strict=pure,strict_overrides=overrides,all_strict=True,max_final_bound=str(max(values.values())),max_final_id=max(values,key=values.get));summaries.append(summary);print(summary,flush=True)
 result=dict(status='PASS',scope=__doc__,new_mixed_strong_pairs=len(new),all_strong_pairs=len(strong),modes=summaries,elapsed_seconds=time.time()-start)
 (HERE/'MIXED_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS seconds',time.time()-start,flush=True)
if __name__=='__main__':main()
