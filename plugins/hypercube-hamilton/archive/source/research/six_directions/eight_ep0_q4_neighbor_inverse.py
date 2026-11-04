import json,itertools,collections
from pathlib import Path
R=Path('.');norm=lambda a,b:tuple(sorted((a,b)))
results=[]
for v in (3,15):
 bad=collections.defaultdict(set);source_counts={}
 for s in (1,2,4,8):
  h=1 if (v^s).bit_count()==1 else 7
  for p in itertools.permutations(range(4)):
   tr=lambda a:sum(((a>>i)&1)<<p[i] for i in range(4))^v
   if tr(h)==s:break
  raw=(R/f'q4_distance{h.bit_count()}_avoided_table.bin').read_bytes();assert len(raw)==135135*30
  n=0
  for off in range(0,len(raw),30):
   if raw[off+16]!=255:continue
   n+=1;m=raw[off:off+16];F=frozenset(norm(tr(a),tr(m[a])) for a in range(16) if a<m[a]<16)
   mate={a:b for e in F for a,b in (e,e[::-1])};t=mate[0];M=(F-{norm(0,t)})|{norm(s,t)}
   assert len(M)==7 and {a for e in M for a in e}==set(range(16))-{0,v}
   bad[M].add(s)
  source_counts[s]=n
 hist=collections.Counter(map(len,bad.values()));worst=max(hist);examples=[{'matching':sorted(M),'bad_neighbors':sorted(ss),'available_neighbors':sorted({1,2,4,8}-ss)} for M,ss in bad.items() if len(ss)==worst]
 results.append({'free_hole':0,'omitted':v,'source_negative_counts':source_counts,'bad_neighbor_histogram':dict(sorted(hist.items())),'universal_positive_matchings':135135-len(bad),'minimum_optional_neighbor_union_size':4-worst,'worst_examples':examples})
(R/'eight_ep0_q4_neighbor_inverse.json').write_text(json.dumps({'scope':'Exact inverse classification from audited opposite-hole 14cycle tables; semantic review pending','results':results},indent=2));print([(r['omitted'],r['bad_neighbor_histogram'],r['minimum_optional_neighbor_union_size'],r['worst_examples'][:1]) for r in results])
