"""Exact solver-free checking of the PG nine-positive countersearch domain."""
from itertools import combinations
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent
start=time.process_time();j=json.loads((HERE/'PROFILE.json').read_text())
points=j['points'];lines=list(map(frozenset,j['projective_lines']))
assert len(points)==len(lines)==13 and len(set(lines))==13
assert all(len(e)==4 for e in lines)
assert all(sum(set(pair)<=e for e in lines)==1 for pair in combinations(range(13),2))
for g in j['automorphism_generators']:
 pp=g['point_permutation'];lp=g['line_permutation']
 assert sorted(pp)==sorted(lp)==list(range(13))
 assert all(frozenset(pp[v] for v in lines[i])==lines[lp[i]] for i in range(13))
all_members=set();rows=[]
for row in j['rows']:
 members=set(map(tuple,row['excluded_orbit_members']))
 assert len(members)==row['excluded_orbit_size'] and not(all_members&members)
 assert tuple(row['excluded_line_indices']) in members
 for exc in members:
  for g in j['automorphism_generators']:
   assert tuple(sorted(g['line_permutation'][i] for i in exc)) in members
 all_members|=members
 pos=list(map(set,row['positive_sets']));minimal=[]
 # Independent order-by-size minimality criterion, not the source's
 # one-point-deletion test over bit masks.
 for k in range(14):
  for r in combinations(range(13),k):
   R=set(r)
   if all(R&A for A in pos) and not any(M<=R for M in minimal):minimal.append(frozenset(R))
 masks={sum(1<<v for v in R) for R in minimal}
 assert masks==set(row['minimal_transversal_masks'])
 m3=[r for r in minimal if len(r)==3];m4=[r for r in minimal if len(r)==4]
 if len(m3)>3:
  cert={'kind':'more_than_three_forced_negative_triples','forced_triples':len(m3),'allowed':3}
 else:
  assert len(m3)==1 and len(m4)>=42
  # A minimal triple cannot be contained in a minimal four-transversal.
  assert all(not m3[0]<=r for r in m4)
  cert={'kind':'forced_triple_plus_four_transversal_capacity','forced_triples':1,
        'minimal_four_transversals':len(m4),'other_triples_at_most':2,
        'each_other_triple_covers_at_most':13-3,
        'negative_four_budget_if_q_other_triples':'19-q',
        'maximum_cover':max(10*q+19-q for q in range(3)),'strict_gap':len(m4)-37}
  assert cert['strict_gap']>0
 rows.append({'case':row['case'],'orbit_size':len(members),'minimal_three':len(m3),'minimal_four':len(m4),'certificate':cert})
assert all_members==set(combinations(range(13),4))
out={'status':'PASS','excluded_domain':len(all_members),'orbit_sizes':[r['orbit_size'] for r in rows],
 'scope':'Only nine-line PG(2,3) positive families; all715 covered via checked projective automorphisms.',
 'solver_free_no_cover_certificates':rows,'cpu_seconds':time.process_time()-start}
(HERE/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
