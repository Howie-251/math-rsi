from pathlib import Path
import array,collections,json
D=Path(__file__).resolve().parent;ROOT=D.parents[7]
def produce(stdout):
 s=json.loads((D/'FROZEN_SIGMA.json').read_text())['sigma'];positive=set()
 for line in stdout.splitlines():
  if line.startswith('v '):positive.update(x for x in map(int,line[2:].split()) if 1<=x<=684)
 shifts={}
 for x in sorted(positive):
  r,t=divmod(x-1,19)
  if r in shifts:raise RuntimeError('SHIFT_ROW_MULTIPLE')
  shifts[r]=t
 assert set(shifts)==set(range(36)) and shifts[0]==0 and len(set(s))==36
 A=array.array('I');A.frombytes((D.parent/'A_EXACT_LENGTH0_3.u32').read_bytes());MASK=(1<<19)-1;cache={}
 def rot(a,t):return ((a<<t)|(a>>(19-t)))&MASK
 def add(a,b):
  if not a or not b:return 0
  key=(min(a,b),max(a,b))
  if key in cache:return cache[key]
  z=0
  while a:
   bit=a&-a;a-=bit;z|=rot(b,bit.bit_length()-1)
  cache[key]=z;return z
 checked=[]
 for i in range(36):
  for j in range(36):
   z=0
   for r in range(36):
    m=0
    for a in range(4):
     for b in range(4-a):m|=add(A[(a*36+i)*36+r],A[(b*36+s[r])*36+j])
    z|=rot(m,shifts[r])
   if z!=MASK:raise RuntimeError('INDEPENDENT_A_ENDPOINT_COVER_FAILED')
   checked.append(z)
 (D/'INDEPENDENT_POINT_CHECK.json').write_text(json.dumps({'status':'ALL24624_ACTUAL_POINTS_PASS','sigma':s,'shifts':[shifts[r] for r in range(36)],'all1296_target_masks':checked,'recomputed_from_A_not_fixed_CNF_or_B':True},indent=2)+'\n')
 source=ROOT/'research/ddp/m1_sources/graph_7_4_n684.txt';old=set()
 with source.open() as f:
  for line in f:
   if not line.strip() or line.startswith('#'):continue
   u,v=map(int,line.split());assert 0<=u<684 and 0<=v<684 and u!=v;old.add(tuple(sorted((u,v))))
 assert len(old)==2394
 deg=collections.Counter(v for e in old for v in e);assert len(deg)==684 and set(deg.values())=={7}
 def nu(r,k):return 342*(r//18)+9*((r%2)+2*k)+(r%18)//2
 M=[[nu(r,k),nu(s[r],(k+shifts[r])%19)] for r in range(36) for k in range(19)]
 assert len({u for u,v in M})==len({v for u,v in M})==684
 E=old|{(u+684,v+684) for u,v in old}|{(u,v+684) for u,v in M};assert len(E)==5472
 with (D/'candidate1368.edges').open('w') as f:
  f.write('1368 5472\n')
  for u,v in sorted(E):f.write(f'{u} {v}\n')
 (D/'MATCHING684.json').write_text(json.dumps(M)+'\n')
 (D/'PARAMETERS.json').write_text(json.dumps({'n':1368,'m':5472,'degree':8,'target_D':4,'sigma':s,'shifts':[shifts[r] for r in range(36)],'source_literal':str(source.relative_to(ROOT)),'source_format':'comments_and_headerless_edgepairs','source_parse_count':1,'sourceD4validation_BFS':0,'status':'SEMANTIC_COVER_PASS_PENDING_PRODUCER_BFS_AND_FRESH'},indent=2)+'\n')
 return True
