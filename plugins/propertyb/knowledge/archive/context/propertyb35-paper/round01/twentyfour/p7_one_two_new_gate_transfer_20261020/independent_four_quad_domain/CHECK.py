"""Independent J-first, capacity-pruned high-trace recursion and35-index replay.
Does not import/read FOUR_QUAD_PROFILE.py or REPLAY_FOUR_QUADS.py.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent;SOURCE=HERE.parent/'FOUR_QUAD_WITNESSES.jsonl'
P=tuple(range(7));FULL=(1<<7)-1;PAIRS=tuple(combinations(P,2));PM=tuple((1<<a)|(1<<b) for a,b in PAIRS)
QUADS=tuple(m for m in range(128) if m.bit_count()==4)
VERTS={m:tuple(v for v in P if m>>v&1) for m in range(128)}
PAIR_COV={m:sum(1<<k for k,p in enumerate(PM) if p&m==p) for m in range(128)}
SHAPES=((3,6),(3,12));start=time.process_time()
witness={}
for line in SOURCE.open():
 r=json.loads(line);shape,qs,jm,u,blue,gate,sig=r
 k=(shape,tuple(sorted(qs)),jm);assert k not in witness
 witness[k]=(tuple(u),blue,gate,tuple(sig))
assert len(witness)==77840
seen=set();counts=Counter();gates=Counter();classified=0;repeated_high=Counter();outrows=[]
for shape,F in enumerate(SHAPES):
 internals=tuple(FULL^m for m in F)
 ci=tuple(sum(bool(m>>v&1) for m in internals) for v in P)
 basecov=PAIR_COV[internals[0]]|PAIR_COV[internals[1]]
 necessary=0;gatecounts=Counter();leafs=0
 for jm in PM:
  si=tuple(int(jm>>v&1) for v in P)
  cap=tuple(min(8-ci[v]-si[v],(15-4*ci[v]-si[v])//3) for v in P)
  assert min(cap)>=0
  h=[0]*7;chosen=[]
  def rec(first,depth,cov):
   nonlocal_dummy=None
   global classified
   if depth==4:
    if cov!=(1<<21)-1:return
    k=(shape,tuple(chosen),jm)
    assert k not in seen and k in witness
    u=tuple(8-ci[v]-si[v]-h[v] for v in P)
    expected_u,blue,gate,expected_sig=witness[k]
    assert u==expected_u and min(u)>=0 and sum(u)==28
    assert all(si[v]+3*h[v]<=15-4*ci[v] for v in P)
    # Reconstruct each of35 actual-index P traces directly.
    traces=list(internals)+chosen+[jm]
    for v in P:traces.extend([1<<v]*u[v])
    assert len(traces)==35
    assert all(sum(m>>v&1 for m in traces)==8 for v in P)
    assert sum(5-m.bit_count() for m in traces)==119
    assert all(any(m&p==p for m in traces) for p in PM)
    assert all(sum(5-m.bit_count() for m in traces if m>>v&1)>=17 for v in P)
    assert blue.bit_count()==2 and blue not in F and jm&blue!=jm
    assert all(q&blue and q&~blue for q in chosen)
    pos=Counter();neg=Counter()
    for m in traces:
     if m&blue and m&~blue:continue
     (pos if m&~blue==0 else neg)[5-m.bit_count()]+=1
    assert pos[1]==pos[2]==pos[3]==neg[1]==neg[2]==0
    sig=(pos[4],neg[3],neg[4]);assert sig==expected_sig
    m,t,b=sig
    if gate==0:assert m<=7 and t<=4 and b<=35
    elif gate==1:assert m==8 and t<=3 and b<=20  # exact old L17 gate
    elif gate==2:assert m==9 and t<=3 and t+b<=20
    else:raise AssertionError(gate)
    seen.add(k);counts[shape]+=1;gates[shape,gate]+=1;classified+=35
    repeated_high[shape]+=len(set(chosen))<4
    return
   remaining=4-depth
   if sum(cap[v]-h[v] for v in P)<4*remaining:return
   for qi in range(first,len(QUADS)):
    q=QUADS[qi];vs=VERTS[q]
    if any(h[v]>=cap[v] for v in vs):continue
    for v in vs:h[v]+=1
    chosen.append(q)
    rec(qi,depth+1,cov|PAIR_COV[q])
    chosen.pop()
    for v in vs:h[v]-=1
  rec(0,0,basecov|PAIR_COV[jm])
 outrows.append({'shape':shape,'missing':F,'necessary':counts[shape],
                 'gate_counts':{str(g):gates[shape,g] for g in range(3)},
                 'sources_with_repeated_high_trace':repeated_high[shape]})
assert seen==set(witness) and [counts[0],counts[1]]==[26189,51651]
out={'status':'PASS','scope':__doc__,'rows':outrows,'total_sources':len(seen),'classified_source_indices':classified,
 'J_first_capacity_recursion_domain_equals_all_saved_keys':True,
 'each_source_own_blue_and_old7_oldL17eight_new9_hypotheses_checked':True,
 'no_H_or_exterior_incidence_search':True,'cpu_seconds':time.process_time()-start}
(HERE/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
