from pathlib import Path
import json,itertools,collections
P=Path(__file__).resolve().parent
j=json.loads((P/'FOURTEEN_RESIDUAL_STRUCTURE.json').read_text());r=j['orbit_rows'][87];T={z^32 for z in r['Z']};E=[x for x in range(1,32) if x.bit_count()%2==0];O=[x for x in range(1,32) if x.bit_count()%2 and x not in (1,2,4,8,16,14)];adj={o:sum(1<<i for i,e in enumerate(E) if (e^o).bit_count()==1) for o in O}
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
res={'status':'PRODUCER_AUXILIARY_CARDINALITY_DP_NOT_INDEPENDENT_REVIEW','orbit_index':87,'E':E,'O':O,'T':sorted(T),'by_matching_size':dict(counts),'maximal_T_covered_matchings':sum(counts.values()),'method':'Enumerate unmatched optional odd subset; inject all other odds into even neighbors; require every neighbor of unmatched odd vertices to be used.'}
(P/'FOURTEEN_STAR_B_EXPAND_A_count_87.json').write_text(json.dumps(res,indent=2)+'\n');print(res)
