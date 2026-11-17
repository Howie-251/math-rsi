from pathlib import Path
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,'/mnt/c/users/anony/desktop/project/research/ex_qn_c4/coevolve/launches/near-extremal-20261115/finite8_root_checks')
from fractions import Fraction as F
from itertools import combinations,combinations_with_replacement
from collections import Counter
import json,sys,hashlib
from check_connector_point_cuts import GROUP,SQ,ROOTS,rootmap,quadratic,ORDER

def pmask(p,h):return sum(1<<h[1][i] for i in range(4) if p>>i&1)
def fmask(f,h):return sum(1<<h[0][i] for i in range(4) if f>>i&1)+(pmask(f>>4,h)<<4)
def project(g,block):
 E={e for k,e in enumerate(ORDER) if g>>k&1};adj=[set() for _ in range(16)]
 for a,b in E:adj[a].add(b);adj[b].add(a)
 assert all(len(adj[a]&adj[b])<=1 for a in range(16) for b in range(a))
 def edge(a,b):return b in adj[a]
 U=[[0]*15 for _ in range(15)]
 for a,b in combinations(range(4),2):
  for v in range(16):
   if v&((1<<a)|(1<<b)):continue
   vs=[v,v^(1<<a),v^(1<<b),v^(1<<a)^(1<<b)];r=sum(1<<k for k,(s,t) in enumerate(SQ) if edge(vs[s],vs[t]));cr=min(rootmap(r,h) for h in GROUP)
   if cr!=ROOTS[block]:continue
   h0=next(h for h in GROUP if rootmap(r,h)==cr);st=[h for h in GROUP if rootmap(cr,h)==cr]
   codes=[sum(1<<k for k,(s,t) in enumerate(SQ) if edge(vs[s]^(1<<c),vs[t]^(1<<c))) for c in range(4) if c not in [a,b]];codes=[pmask(c,h0) for c in codes];assert max(codes)<15
   for h in st:
    s,t=[pmask(c,h) for c in codes];U[s][t]+=2240//len(st);U[t][s]+=2240//len(st);U[s][s]+=448//len(st);U[t][t]+=448//len(st)
 return U

def main():
 path=Path(sys.argv[1]).resolve();pointpath=path.parent/'INPUT_POINT.json';cut=json.loads(path.read_text());point=json.loads(pointpath.read_text(),parse_float=F);assert hashlib.sha256(pointpath.read_bytes()).hexdigest()==cut['input_sha256']
 Q=cut['small_Q'];assert len(Q)==15 and all(len(r)==15 for r in Q);assert all(type(Q[i][j]) is int and Q[i][j]==Q[j][i] for i in range(15) for j in range(15))
 vals=[quadratic(Q,Counter(xs)) for xs in combinations_with_replacement(range(15),6)];minimum=min(vals);assert len(vals)==38760 and minimum>=0
 b=cut['block'];r=ROOTS[b];codes=[f for f in range(240) if all(not((r>>k&1) and(f>>(k+4)&1) and(f>>s&1) and(f>>t&1)) for k,(s,t) in enumerate(SQ))];st=[h for h in GROUP if rootmap(r,h)==r];assert codes==cut['full_state_codes'];assert [f>>4 for f in codes]==cut['full_state_to_label'];assert len(st)==cut['root_stabilizer_size']==4
 expected=[[sum(Q[fmask(f,h)>>4][fmask(g,h)>>4] for h in st) for g in codes] for f in codes];assert expected==cut['full_Q']
 M=[[F() for j in range(15)] for i in range(15)]
 for g,w in point['lambda']:
  U=project(g,b)
  for i in range(15):
   for j in range(15):M[i][j]+=w*U[i][j]/129024
 value=len(st)*sum(Q[i][j]*M[j][i] for i in range(15) for j in range(15));assert str(value)==cut['exact_target_pairing'] and str(value/cut['positive_normalization'])==cut['normalized_pairing'] and value<0
 witness=None
 for xs in combinations_with_replacement(range(15),4):
  v=quadratic(Q,Counter(xs))
  if v<0:witness={'histogram':dict(Counter(xs)),'quadratic':v};break
 out=dict(status='PASS_ROOT_INDEPENDENT_PARALLEL15_DOMAIN_AND_LITERAL_PAIR',count=38760,minimum=minimum,actual_Q4_masks=len(point['lambda']),full_state_count=len(codes),all_full_kernel_entries_exact=True,root_stabilizer_size=len(st),exact_pairing=str(value),normalized_pairing=str(value/cut['positive_normalization']),float_normalized=float(value/cut['positive_normalization']),small_total4_noncopositive_witness=witness,input_sha256=cut['input_sha256'],cut_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),scope='Concrete arithmetic plusRootderivedsmallprojectionpullback; freshgeneralsemanticreview ofnewfamilypending. No globalNO/graph/682bound.')
 output=Path(__file__).with_name('PARALLEL15_MASTER102_CUT_CHECK.json');output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
