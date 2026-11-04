"""Producer lookup of already accepted marked local input scopes; no forced T17."""
from pathlib import Path
from itertools import permutations
import json,hashlib
P=Path(__file__).resolve().parent
maps=[tuple(sum(((x>>p[i])&1)<<i for i in range(5)) for x in range(32)) for p in permutations(range(5))]
odd=[x for x in range(32) if x.bit_count()%2];oi={x:i for i,x in enumerate(odd)}
def mask(xs):return sum(1<<x for x in xs)
def small(xs):return sum(1<<oi[x] for x in xs)
reviews=['Q5_T26_RANK_BATCH_REVIEW.json','Q5_T15_RANK_BATCH_REVIEW.json','Q5_T17_RANK_BATCH_REVIEW.json','Q5_T63_RANK_REVIEW.json','Q5_T63_COMPLETE_SPLIT_REVIEW.json','TEN_HOLE_COVERED_PARTIAL_REVIEW.json','T44_Q5_CLOSURE_REVIEW.json']
for r in reviews:assert json.loads((P/r).read_text())['verdict']=='PASS'
T26=set();T15=set(map(int,(P/'TEN_HOLE_COVERED_PARTIAL_REVIEW_lookup.txt').read_text().split()));T17=set();T63=set()
for row in json.loads((P/'Q5_T26_RANK_batch_summary.json').read_text())['reports']:
 assert row['full_rank'];g=row['geometry'];M=g['minority'];J=g['majority'];U=g['omitted']
 for shift in M:
  for m in maps:
   delta=m[M[0]^M[1]];jm=small(m[x^shift] for x in J);um=small(m[x^shift] for x in U)
   T26.add(delta|(jm<<5)|(um<<21))
for row in json.loads((P/'Q5_T15_RANK_batch_summary.json').read_text())['reports']:
 assert row['full_rank'];g=row['geometry']
 for m in maps:
  om={m[x] for x in g['omitted']};inc={m[x] for x in g['majority']}-om;T15.add(mask(om)|(mask(inc)<<32))
for row in json.loads((P/'Q5_T17_RANK_batch_summary.json').read_text())['orbits']:
 assert row['full_rank'];g=row['marked_geometry']
 for m in maps:
  om={m[x] for x in g['omitted']};inc={m[x] for x in g['majority']}-om;T17.add(mask(om)|(mask(inc)<<32))
for row in json.loads((P/'Q5_T63_RANK_batch_summary.json').read_text())['reports']:
 assert row['full_rank'];g=row['geometry']
 for m in maps:
  for shift in range(32):T63.add(mask(m[x]^shift for x in g['holes'])|(mask(m[x]^shift for x in g['omitted'])<<32))
for name,lookup in [('T26',T26),('T15',T15),('T17',T17),('T63',T63)]:
 (P/f'HIGHER_Q5_FULL_{name}_lookup.txt').write_text(''.join(str(x)+'\n' for x in sorted(lookup)))
sources=reviews+['Q5_T26_RANK_batch_summary.json','Q5_T15_RANK_batch_summary.json','Q5_T17_RANK_batch_summary.json','Q5_T63_RANK_batch_summary.json','TEN_HOLE_COVERED_PARTIAL_REVIEW_lookup.txt']
out={'status':'PRODUCER_LOOKUP_PENDING_REVIEW','counts':{'T26':len(T26),'T15':len(T15),'T17_unforced':len(T17),'T63_rank':len(T63)},'forced_T17_used':False,'input_hashes':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in sources}}
(P/'HIGHER_Q5_FULL_lookups.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['counts']))
