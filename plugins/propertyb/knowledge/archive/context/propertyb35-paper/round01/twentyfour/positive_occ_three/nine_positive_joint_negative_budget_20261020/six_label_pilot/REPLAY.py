"""Independent set-based counts for the stopping graph; no negative layouts."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from math import comb
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
j=json.loads((HERE/'PROFILE.json').read_text());f=j['first_nongated'];A=list(map(set,f['sets']));U=set().union(*A)
C={k:[set(c) for c in combinations(sorted(U),k) if all(set(c)&a for a in A)] for k in (3,4)}
assert [len(C[k]) for k in (3,4)]==[f['C3'],f['C4']]==[0,64]
pair_counts={};triple_counts={}
for q in combinations(sorted(U),2):
 Q=set(q);miss=[a for a in A if not a&Q]
 # Enumerate only the two new points against the missed labels, independent
 # of the source's counter over complete transversal candidates.
 c=sum(all(set(ext)&a for a in miss) for ext in combinations(sorted(U-Q),2))
 pair_counts[q]=c
 assert c==sum(Q<=r for r in C[4])
for q in combinations(sorted(U),3):
 Q=set(q);miss=[a for a in A if not a&Q]
 good=set.intersection(*miss) if miss else U
 triple_counts[q]=len(good-Q)
 assert triple_counts[q]==sum(Q<=r for r in C[4])
p3=sorted((sum(set(q)<=r for r in C[3]) for q in combinations(sorted(U),2)),reverse=True)
p4=sorted(pair_counts.values(),reverse=True);h=max(triple_counts.values());failed=[];full=[]
for t in range(4):
 for b in range(21-t):
  for u in range(t+1):
   for v in range(min(b,4-u)+1):
    B3=sum(p3[:u])+t-u+v;B4=sum(p4[:u])+(t-u+v)*h+b-v
    row={'u':u,'t':t,'v':v,'b':b,'C3_blocker':B3,'C4_blocker':B4,'C3_strict':len(C[3])>B3,'C4_strict':len(C[4])>B4}
    full.append(row)
    if not row['C3_strict'] and not row['C4_strict']:failed.append(row)
assert len(failed)==7
maxpairs=[q for q,n in pair_counts.items() if n==max(p4)]
nextmax=max(n for n in pair_counts.values() if n<max(p4))
# Structural observation only: all top3 selections leave sixteen candidates
# sharing the unchosen top pair. This is not added to the gate or used to
# continue the domain recursion.
top3_left=[]
for chosen in combinations(maxpairs,3):
 left=[r for r in C[4] if not any(set(q)<=r for q in chosen)]
 common=set.intersection(*left) if left else set()
 top3_left.append({'chosen_pairs':chosen,'remaining_candidates':len(left),'common_points':sorted(common)})
 assert len(left)==16 and len(common)==2
out={'status':'PASS','C3':0,'C4':64,'all_pair_extensions_checked':len(pair_counts),'all_triple_extensions_checked':len(triple_counts),
 'pair_extension_histogram':dict(Counter(pair_counts.values())),'maximum_pairs':maxpairs,'next_largest_pair_extension':nextmax,
 'maximum_triple_extension':h,'all_legal_parameter_rows':full,'nongated_legal_rows':failed,
 'top_three_pair_leftover_observation':top3_left,'cpu_seconds':time.process_time()-start,
 'scope':'Only independently replays the first graph and all allowed parameters. Not complete six-label domain or a signed counterexample.'}
(HERE/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('all_legal_parameter_rows','top_three_pair_leftover_observation')})
