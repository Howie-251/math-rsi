"""Offline original35 A1 source and COVER replay. Standard library; no SAT."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from math import comb
import json,time
P=Path(__file__).resolve().parent
st=time.process_time();summary=json.loads((P/'SUMMARY.json').read_text())
assert summary['status']!='RUNNING'
rows=[json.loads(s) for s in (P/'candidates.jsonl').read_text().splitlines()]
cuts=[json.loads(s) for s in (P/'cuts.jsonl').read_text().splitlines()]
assert len(rows)==summary['candidates'] and len(cuts)==summary['cuts']
assert summary['vertices']==21 and summary['uniformity']==5 and summary['edges']==35
assert not summary['fixed_first_edge'] and not summary['affine_seed_used']
universe=list(combinations(range(21),5));um=[sum(1<<v for v in e) for e in universe]
expected=[6,7]+[8]*9+[9]*10;xc=[0,1]+[2]*4+[1]*15
assert summary['target_degrees']==expected and summary['target_center_codegrees']==xc
assert summary['unrestricted_oracle_calls']==len(rows)
assert summary['master_solve_calls']>=summary['master_unknown_slices']
assert summary['proof_claim'] is False
previous=[];out=[];seen=set();by_candidate={}
for c in cuts:by_candidate.setdefault(c['candidate'],[]).append(c)
for row in rows:
 edges=[tuple(e) for e in row['edges']]
 assert len(edges)==len(set(edges))==35
 assert all(tuple(sorted(e))==e and len(set(e))==5 and min(e)>=0 and max(e)<21 for e in edges)
 deg=[sum(v in e for e in edges) for v in range(21)];assert deg==expected==row['degrees']
 co={pair:sum(set(pair)<=set(e) for e in edges) for pair in combinations(range(21),2)}
 assert min(co.values())>=1
 assert [[a,b,n] for (a,b),n in co.items()]==row['pair_codegrees']
 assert [0]+[co[(0,v)] for v in range(1,21)]==xc==row['center_codegrees']
 em=[sum(1<<v for v in e) for e in edges]
 assert all(any(r&m in (0,m) for m in em) for r in previous)
 sat=row['unrestricted_coloring_sat']
 if sat is True:
  red=row['red'];assert len(set(red))==len(red) and all(0<=v<21 for v in red)
  rr=sum(1<<v for v in red);assert all(rr&m not in (0,m) for m in em)
 elif sat is False:
  checked=0
  for rr in range(1,1<<21,2):
   checked+=1;assert any(rr&m in (0,m) for m in em),'SAT UNSAT claim is false'
  assert checked==1<<20
 else:
  assert sat is None and summary['status']=='COLOR_ORACLE_UNKNOWN'
 for cut in by_candidate.get(row['candidate'],[]):
  red=cut['red'];assert len(set(red))==len(red) and all(0<=v<21 for v in red)
  rr=sum(1<<v for v in red);assert rr&1 and rr not in seen;seen.add(rr)
  # Independent direct proper test on the entire literal original H.
  assert all(0<len(set(e)&set(red))<5 for e in edges)
  blue=sorted(set(range(21))-set(red));cs={e for e in combinations(sorted(red),5)}|{e for e in combinations(blue,5)}
  direct={e for e,m in zip(universe,um) if rr&m in (0,m)}
  assert cs==direct and len(cs)==cut['literal_count']==comb(len(red),5)+comb(21-len(red),5)
  previous.append(rr)
 out.append(dict(candidate=row['candidate'],edges=35,degree_role='PASS',all_210_pair_codegrees='PASS',unrestricted_coloring_sat=sat,cuts_checked=len(by_candidate.get(row['candidate'],[]))))
assert set(by_candidate)<=set(row['candidate'] for row in rows)
result=dict(status='PASS',scope='Saved finite A1 original-H artifacts only; no global nonexistence claim',solver_used=False,new_search_ran=False,candidate_records=len(rows),proper_candidates=sum(r['unrestricted_coloring_sat'] is True for r in rows),cuts_checked=len(cuts),individual_results=out,search_terminal_status=summary['status'],cpu_seconds=time.process_time()-st)
(P/'VERIFY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
