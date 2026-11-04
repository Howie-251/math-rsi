"""Independent low-gap structural verifier and optional complete A-mask audit.
No producer or Hamilton search imported. Graph paths use adjacency components.
"""
import itertools,json,struct,hashlib,sys
from pathlib import Path
R=Path(__file__).resolve().parent

def pm(v,short=False):
 if not v:yield ();return
 a=v[0]
 for i,b in enumerate(v[1:],1):
  if short and (a^b).bit_count()!=1:continue
  for tail in pm(v[1:i]+v[i+1:],short):yield ((a,b),)+tail

patterns=[]
for pair in itertools.combinations([7,11,13,14],2):
 rem=tuple(x for x in range(1,15) if x not in pair)
 for F in pm(rem,True):patterns.append(F+((15,pair[0]),(15,pair[1])))
assert len(patterns)==len(set(patterns))==96
for F in patterns:
 deg=[0]*16
 for a,b in F:assert (a^b).bit_count()==1;deg[a]+=1;deg[b]+=1
 assert deg==[0]+[1]*14+[2]
reports=[]
for c in (1,3,5):
 # Validate the complete A matching domain by edge-set rank/set equality.
 raw=(R/f'A8_typed_c{c}_A.bin').read_bytes();assert len(raw)%32==0
 eligible=set(range(16))-{0,1,2,4,15};seen=set();types={};empty=0
 pairinglist=list(pm(tuple(range(c+3))));ranks={frozenset(F):i for i,F in enumerate(pairinglist)}
 for off in range(0,len(raw),32):
  m=raw[off:off+16];lo,hi=struct.unpack('<QQ',raw[off+16:off+32]);mask=lo|(hi<<64)
  holes={x for x in range(16) if m[x]==255};ports=holes-{0,1,2,4,15};assert len(ports)==c and ports<=eligible
  assert all(m[x]<16 and m[x]!=x and m[m[x]]==x for x in set(range(16))-holes)
  F=frozenset((x,m[x]) for x in range(16) if x<m[x]<16);key=(tuple(sorted(ports)),F);assert key not in seen;seen.add(key)
  assert mask and mask.bit_length()<=len(pairinglist);types[mask]=types.get(mask,0)+1
  if '--full-a' in sys.argv:
   T=[1,2,4]+sorted(ports);tset=set(T);actual=0
   for N in patterns:
    if any(tuple(sorted(e)) in F for e in N):continue
    adj=[set() for x in range(16)]
    for a,b in list(F)+list(N):adj[a].add(b);adj[b].add(a)
    left=set(range(1,16));matching=[];ok=True
    while left:
     start=min(left);stack=[start];comp=set()
     while stack:
      a=stack.pop()
      if a in comp:continue
      comp.add(a);stack.extend(adj[a]-comp)
     left-=comp;end=comp&tset
     if len(end)!=2:ok=False;break
     a,b=sorted(T.index(x) for x in end);matching.append((a,b))
    if ok:actual|=1<<ranks[frozenset(matching)]
   assert actual==mask
 expected=set()
 for ports in itertools.combinations(sorted(eligible),c):
  for F in pm(tuple(sorted(eligible-set(ports)))):expected.add((ports,frozenset(F)))
 assert seen==expected
 # Verify every B input and prove that ANY boundary pairing is impossible.
 braw=(R/f'A8_three_bridge_low_B_c{c}.bin').read_bytes();assert len(braw)%16==0
 bkeys=set();sub={};bpairs=0
 for off in range(0,len(braw),16):
  m=braw[off:off+16];ports={x for x in range(16) if m[x]==255}-{7,11,13};assert len(ports)==c
  assert all(m[x]<16 and m[x]!=x and m[m[x]]==x for x in set(range(16))-{7,11,13}-ports)
  assert {x for x in range(16) if m[x]==255}==ports|{7,11,13}
  assert m[0]!=8 and m not in bkeys;bkeys.add(m)
  Y={1,2,4};P=len(Y&ports)+sum(m[y] in Y for y in Y)//2
  active=lambda x:x in ports or m[x] in Y
  extra=int(active(0) and active(8));assert (c+3)//2==P+extra
  # Count G components independently to certify the structural premise:
  # its T-endpoint components are P pairs plus exactly 0 or 2 terminal roots.
  ts=sorted(ports);adj={x:set() for x in range(16+c+3)}
  def add(a,b):adj[a].add(b);adj[b].add(a)
  for x in range(16):
   if x<m[x]<16:add(x,m[x])
  for i,y in enumerate([1,2,4]):add(16+i,y)
  for i,x in enumerate(ts):add(19+i,x)
  pending=set(range(16,19+c));tt=0;term=[]
  while pending:
   start=min(pending);stack=[start];comp=set()
   while stack:
    x=stack.pop()
    if x in comp:continue
    comp.add(x);stack.extend(adj[x]-comp)
   roots=comp&set(range(16,19+c));pending-=roots
   ends={x for x in comp if len(adj[x])==1}
   assert len(ends)==2 and 1<=len(roots)<=2
   if len(roots)==2:tt+=1
   else:term.append(next(iter(ends-roots)))
  assert tt==P and (term==[] if extra==0 else sorted(term)==[0,8])
  bpairs+=1
 # Confirm stored B masks cover exactly all inputs and crossing bijections.
 br=(R/f'A8_typed_c{c}_B.bin').read_bytes();record=32+c;assert len(br)==bpairs*__import__('math').factorial(c)*record
 certkeys=set()
 for off in range(0,len(br),record):
  m=br[off:off+16];perm=tuple(br[off+16:off+16+c]);mask=br[off+16+c:off+32+c]
  assert m in bkeys and sorted(perm)==list(range(c)) and mask==bytes(16)
  assert (m,perm) not in certkeys;certkeys.add((m,perm))
 assert len(certkeys)==bpairs*__import__('math').factorial(c)
 reports.append(dict(crossings=c,A_inputs=len(seen),A_types=len(types),A_masks_recomputed='--full-a' in sys.argv,B_inputs=bpairs,B_bijections=len(certkeys),B_all_masks_empty=True))
 print(reports[-1],flush=True)
out=dict(status='PASS',scope='Complete low-gap domains and structural impossibility of this fixed three-bridge transfer; NOT an A8 counterexample',short_patterns=96,reports=reports,full_a8_proved=False)
(R/'A8_typed_spectrum_verified.json').write_text(json.dumps(out,indent=2)+'\n')
