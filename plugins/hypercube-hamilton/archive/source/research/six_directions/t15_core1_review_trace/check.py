from pathlib import Path
import sys,runpy,json,hashlib
R=Path.cwd(); T=R/'t15_core1_review_trace';sys.path.insert(0,str(R))
manifest=json.loads((R/'t15_core1_full_closure_verification.json').read_text())
for f,h in manifest['proof_input_hashes'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h,f
print('fixed manifest hashes PASS',len(manifest['proof_input_hashes']),flush=True)
for side,holes,nedges,nrows in [('A',{0,3,5,9},5,62370),('B',{0,1},6,945945)]:
 n=0
 for line in (R/f't15_core1_c2_{side}_types.txt').open():
  bits,p,q,*a=map(int,line.split());assert 0<=bits<512 and len(a)==2*nedges
  assert all(0<=x<16 and x not in holes for x in a) and len(set(a))==len(a)
  assert p<q and set([p,q])==set(range(16))-holes-set(a)
  n+=1
 assert n==nrows
 print('strict c2 input validity',side,n,flush=True)
from q4_five_avoided_jpair_prepare import verify
rows=[verify(tuple(r['omitted'])) for r in json.loads((R/'t15_core1_five_avoided_inputs.json').read_text())['rows']]
(T/'five_avoided.json').write_text(json.dumps({'status':'PASS','rows':rows},indent=2))
print('18 five avoided full tables PASS',flush=True)
from verify_q4_extension_certificates import check
q4=[check(f'q4_two_hole_{s}.bin',[0,s],0) for s in (3,15)]
(T/'N14.json').write_text(json.dumps({'status':'PASS','rows':q4},indent=2)); print('N14 270270 PASS',flush=True)
original=Path.write_text
def redirected(self,*a,**kw):return original(T/self.name,*a,**kw)
Path.write_text=redirected
for f,args in [('verify_q4_three_avoided.py',[]),('verify_r4_inverse_blockers.py',['3','5','1']),('verify_t15_core1_c0_B.py',[]),('verify_t15_core1_joint_B.py',[]),('verify_t15_core1_full_closure.py',[])]:
 sys.argv=[f,*args];runpy.run_path(str(R/f),run_name='__main__')
 print(f,'PASS',flush=True)
zero=set()
for line in (R/'t15_core1_c2_B_types.txt').open():
 a=list(map(int,line.split()))
 if not a[0]:zero.add(frozenset(tuple(a[i:i+2]) for i in range(3,len(a),2)))
B2={frozenset(tuple(q[i:i+2]) for i in range(0,len(q),2)) for q in [list(map(int,l.split())) for l in (R/'t15_core1_route_B2.txt').read_text().splitlines() if l.strip()]}
assert zero==B2 and len(B2)==420
print('B2 zero-spectrum exact list PASS',flush=True)
