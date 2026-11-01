"""Filter prior Fraction rows under root's selection lemmas; independently classify K5 traces."""
import itertools,json
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parent
a=json.loads((P/'FIVE.json').read_text());patterns={tuple(r['blocks']) for r in a['rows']}
pairs=list(itertools.combinations(range(5),2));pidx={x:i for i,x in enumerate(pairs)}
dp={0:{()}};block_count=0
for mask in range(1,32):
 vs=[i for i in range(5) if mask>>i&1]
 if len(vs)<2:continue
 block_count+=1;edges=sum(1<<pidx[x] for x in itertools.combinations(vs,2))
 nxt={used:set(parts) for used,parts in dp.items()}
 for used,parts in dp.items():
  if not used&edges:nxt.setdefault(used|edges,set()).update(tuple(sorted((*part,mask))) for part in parts)
 dp=nxt
independent=dp[(1<<10)-1];assert independent==patterns
out=[]
for v in (42,43,44):
 rows=[r for r in a['rows'] if r['v']==v];assert len(rows)==32
 kept=[r for r in rows if max(b.bit_count() for b in r['blocks'])<=(4 if v==42 else 3)]
 exclude=[r for r in rows if r not in kept];worst=max(kept,key=lambda r:Fraction(r['U']))
 assert all(r['strict'] and Fraction(r['U'])<1 for r in kept)
 for r in kept:assert len(r['positions'])==len(set(r['positions']))==5
 out.append(dict(v=v,restriction='no five-point block' if v==42 else 'all blocks have size at most three',patterns=len(kept),excluded_patterns=len(exclude),remaining_non_strict=0,max_U=worst['U'],max_row=worst,excluded=[dict(blocks=r['blocks'],U=r['U'],strict=r['strict']) for r in exclude],rows=kept))
result=dict(status='PASS_RESTRICTED_EXISTING_FRACTIONS',scope='No probability recomputation; filters exact previously computed FIVE.json rows under root-owned structural selection lemmas',complete_K5_classification=dict(original_patterns=len(patterns),independent_DP_patterns=len(independent),candidate_clique_blocks=block_count,equal=True,method='each candidate clique block processed once in disjoint-pair-union dynamic programming'),selection_proof_owner='root; separate independent review requested',vertices=out)
(P/'TAIL_RESTRICTED.json').write_text(json.dumps(result,indent=2))
print([(r['v'],r['patterns'],r['max_U']) for r in out])
