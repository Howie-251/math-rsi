import itertools,collections,json
from pathlib import Path
R=Path('.');raw=(R/'q4_distance1_avoided_table.bin').read_bytes();neg=[raw[i:i+16] for i in range(0,len(raw),30) if raw[i+16]==255];assert len(neg)==51
es=[(a,b) for a in range(16) for b in range(a+1,16) if (a^b).bit_count()==1]
bad=collections.defaultdict(int)
for idx,(u,v) in enumerate(es):
 j=(u^v).bit_length()-1
 perm=list(range(4));perm[0],perm[j]=perm[j],perm[0]
 tr=lambda a:sum(((a>>i)&1)<<perm[i] for i in range(4))^u
 for m in neg:
  F={(min(tr(a),tr(m[a])),max(tr(a),tr(m[a]))) for a in range(16) if a<m[a]<16}
  for a,b in F:
   for x,y in ((a,b),(b,a)):
    P=(F-{(a,b)})|{tuple(sorted((u,x))),tuple(sorted((v,y)))}
    assert len(P)==8 and len({z for e in P for z in e})==16
    mate={a:b for e in P for a,b in (e,e[::-1])};key=sum(mate[i]<<(4*i) for i in range(16));bad[key]|=1<<idx
(R/'eight_ep0_q4_PB_bad_optional.txt').write_text('\n'.join(f'{k} {v}' for k,v in sorted(bad.items()))+'\n')
print(len(bad),sum(x.bit_count() for x in bad.values()))
