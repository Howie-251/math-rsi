from pathlib import Path
import json,itertools,collections
P=Path(__file__).resolve().parent
j=json.loads((P/'FOURTEEN_RESIDUAL_STRUCTURE.json').read_text());r=j['orbit_rows'][85];T={z^32 for z in r['Z']};E=[x for x in range(1,32) if x.bit_count()%2==0];O=[x for x in range(1,32) if x.bit_count()%2 and x not in (1,2,4,8,16,14)];adj={o:sum(1<<i for i,e in enumerate(E) if (e^o).bit_count()==1) for o in O}
optional=sorted(set(O)-T);counts=collections.Counter()
for subset in range(1<<len(optional)):
 U={x for i,x in enumerate(optional) if subset>>i&1};matched=[o for o in O if o not in U];required=0
 for x in U:required|=adj[x]
 dp={0:1}
 for o in matched:
  nxt=collections.defaultdict(int)
  for used,n in dp.items():
   free=adj[o]&~used
   while free:
    bit=free&-free;free-=bit;nxt[used|bit]+=n
  dp=nxt
 counts[len(matched)]+=sum(n for used,n in dp.items() if not required&~used)
res={'status':'PRODUCER_AUXILIARY_CARDINALITY_DP_NOT_INDEPENDENT_REVIEW','orbit_index':85,'E':E,'O':O,'T':sorted(T),'by_matching_size':dict(counts),'maximal_T_covered_matchings':sum(counts.values()),'method':'Enumerate unmatched optional odd subset; inject all other odds into even neighbors; require every neighbor of unmatched odd vertices to be used.'}
(P/'FOURTEEN_RESIDUAL_STRUCTURE_maxA_count_85.json').write_text(json.dumps(res,indent=2)+'\n');print(res)
# a compact check of the18-hole150 structure, without promoting its domain
f=P/'EIGHTEEN_POST12_HALL_remaining_v31_covered.bin'
if f.exists():
 raw=f.read_bytes();records={tuple(raw[i:i+17]) for i in range(0,len(raw),17)};maps=[[sum(((x>>p[d])&1)<<d for d in range(5))|(x&32) for x in range(64)] for p in itertools.permutations(range(5))];rows=[]
 while records:
  rep=min(records);orb={tuple(sorted(tr[x] for x in rep[:8]))+tuple(sorted(tr[x] for x in rep[8:])) for tr in maps};assert orb<=records;records-=orb
  rows.append({'orbit_size':len(orb),'Z':rep[:8],'W':rep[8:],'all_Z_in_B':all(x&32 for x in rep[:8]),'W_contains_full_root_star':set((1,2,4,8,16,32))<=set(rep[8:]),'b':sum(not x&32 for x in rep[8:]),'A_extra_odd_holes':[x for x in rep[8:] if not x&32 and x not in (1,2,4,8,16)]})
 (P/'FOURTEEN_RESIDUAL_STRUCTURE_eighteen_template.json').write_text(json.dumps({'status':'CONDITIONAL18_DOMAIN_TEMPLATE_ONLY','rows':rows},indent=2)+'\n');print('18 template',rows)
