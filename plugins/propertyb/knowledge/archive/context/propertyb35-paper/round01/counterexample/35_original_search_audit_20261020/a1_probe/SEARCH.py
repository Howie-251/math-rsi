#!/usr/bin/env python3
"""One bounded original-H A1 COVER/CEGIS probe, independent of proof formulas."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from datetime import datetime,timezone
from math import comb
import argparse,json,random,sys,threading,time
import pysat
from pysat.solvers import Minicard,Minisat22
HERE=Path(__file__).resolve().parent
N=21;K=5;M=35;TARGET=[6,7]+[8]*9+[9]*10
CENTER=[0,1]+[2]*4+[1]*15

def dump(p,obj):p.write_text(json.dumps(obj,indent=2)+'\n')
def solve(s,deadline,conflicts,seconds):
 remaining=deadline-time.monotonic()
 if remaining<=0:return None
 s.conf_budget(conflicts)
 timer=threading.Timer(min(seconds,remaining),s.interrupt);timer.daemon=True;timer.start()
 try:return s.solve_limited(expect_interrupt=True)
 finally:timer.cancel();timer.join();s.clear_interrupt()
def exact(s,ls,value):
 s.add_atmost(ls,value);s.add_atmost([-i for i in ls],len(ls)-value)
def proper(edges,red):
 red=set(red);return all(0<len(set(e)&red)<5 for e in edges)
def validate(edges):
 assert len(edges)==35 and len({tuple(e) for e in edges})==35
 assert all(len(e)==5 and len(set(e))==5 and all(0<=v<21 for v in e) for e in edges)
 deg=[sum(v in e for e in edges) for v in range(21)];assert deg==TARGET,deg
 co=Counter(pair for e in edges for pair in combinations(e,2))
 assert all(co[p]>=1 for p in combinations(range(21),2))
 xc=[0]+[co[(0,v)] for v in range(1,21)];assert xc==CENTER,xc
 return dict(degrees=deg,center_codegrees=xc,pair_codegrees=[[a,b,co[(a,b)]] for a,b in combinations(range(21),2)])
def exhaust(edges):
 masks=[sum(1<<v for v in e) for e in edges];checked=0
 for red in range(1,1<<21,2):
  checked+=1
  if all(red&m not in (0,m) for m in masks):
   return dict(non_2_colorable=False,checked=checked,red=[v for v in range(21) if red>>v&1])
 return dict(non_2_colorable=True,checked=checked,red=None)
def main():
 p=argparse.ArgumentParser();p.add_argument('--seconds',type=float,default=120);p.add_argument('--batch',type=int,default=16);p.add_argument('--max-candidates',type=int,default=100000);p.add_argument('--conflicts',type=int,default=20000);p.add_argument('--slice-seconds',type=float,default=3);p.add_argument('--seed',type=int,default=20261020);args=p.parse_args()
 assert 0<args.seconds<=120
 started=time.monotonic();cpu=time.process_time();deadline=started+args.seconds;rng=random.Random(args.seed)
 universe=list(combinations(range(21),5));ids={e:i+1 for i,e in enumerate(universe)};masks=[sum(1<<v for v in e) for e in universe]
 summary=dict(status='RUNNING',started_utc=datetime.now(timezone.utc).isoformat(),command=[sys.executable]+sys.argv,python=sys.version.split()[0],python_sat=pysat.__version__,vertices=21,uniformity=5,edges=35,edge_variables=len(universe),target_degrees=TARGET,target_center_codegrees=CENTER,paircover=True,fixed_first_edge=False,affine_seed_used=False,seed=args.seed,time_budget_seconds=args.seconds,batch=args.batch,conflicts_per_solve=args.conflicts,seconds_per_solve=args.slice_seconds,candidates=0,cuts=0,unrestricted_oracle_calls=0,supplemental_oracle_calls=0,master_solve_calls=0,master_unknown_slices=0,proof_claim=False)
 logs={n:(HERE/(n+'.jsonl')).open('w') for n in ['candidates','cuts','events']};seen=set();sizehist=Counter()
 def event(**obj):
  obj['elapsed_seconds']=time.monotonic()-started;logs['events'].write(json.dumps(obj)+'\n');logs['events'].flush();print(json.dumps(obj),flush=True)
 def addcut(master,edges,red,cid,source):
  assert proper(edges,red)
  rmask=sum(1<<v for v in red)
  if not rmask&1:rmask^=(1<<21)-1
  if rmask in seen:return False
  red=[v for v in range(21) if rmask>>v&1];blue=[v for v in range(21) if not rmask>>v&1]
  clause=sorted(ids[e] for side in [red,blue] for e in combinations(side,5))
  assert clause==[i+1 for i,m in enumerate(masks) if m&rmask in (0,m)]
  assert not {ids[tuple(e)] for e in edges}&set(clause)
  master.add_clause(clause);seen.add(rmask);summary['cuts']+=1;sizehist[len(red)]+=1
  logs['cuts'].write(json.dumps(dict(cut=summary['cuts'],candidate=cid,red=red,source=source,literal_count=len(clause)))+'\n');logs['cuts'].flush();return True
 try:
  with Minicard() as master:
   variables=list(range(1,len(universe)+1));exact(master,variables,35)
   for v,d in enumerate(TARGET):exact(master,[i+1 for i,e in enumerate(universe) if v in e],d)
   for v in range(1,21):exact(master,[i+1 for i,e in enumerate(universe) if 0 in e and v in e],CENTER[v])
   for a,b in combinations(range(21),2):master.add_clause([i+1 for i,e in enumerate(universe) if a in e and b in e])
   # Only phases, no edge assertion: six role-compatible centre edges.
   star=[(0,2,6,7,8),(0,3,9,10,11),(0,1,4,12,13),(0,2,3,14,15),(0,4,5,16,17),(0,5,18,19,20)]
   phaseids={ids[tuple(sorted(e))] for e in star};master.set_phases([v if v in phaseids else -v for v in variables])
   dump(HERE/'INITIAL_PHASE.json',dict(role='phase preference only; no fixed edges or affine restriction',edges=[sorted(e) for e in star]))
   event(event='MASTER_READY',edge_variables=len(universe))
   last_report=time.monotonic()
   while time.monotonic()<deadline and summary['candidates']<args.max_candidates:
    summary['master_solve_calls']+=1;sat=solve(master,deadline,args.conflicts,args.slice_seconds)
    if sat is None:
     summary['master_unknown_slices']+=1
     if time.monotonic()-last_report>=20:event(event='MASTER_UNKNOWN',candidates=summary['candidates'],cuts=summary['cuts'],slices=summary['master_unknown_slices']);last_report=time.monotonic()
     continue
    if sat is False:summary['status']='MASTER_UNSAT_UNCERTIFIED';break
    chosen=sorted(v for v in master.get_model() if 1<=v<=len(universe));edges=[universe[v-1] for v in chosen];stats=validate(edges)
    r_masks=[sum(1<<v for v in e) for e in edges]
    assert all(any(m&r in (0,m) for m in r_masks) for r in seen)
    summary['candidates']+=1;cid=summary['candidates'];clauses=[[sgn*(v+1) for v in e] for e in edges for sgn in [1,-1]]+[[1]]
    with Minisat22(bootstrap_with=clauses) as oracle:
     summary['unrestricted_oracle_calls']+=1;satcolor=solve(oracle,deadline,args.conflicts,args.slice_seconds);model=oracle.get_model() if satcolor is True else None
    red=[v for v in range(21) if v+1 in model] if model is not None else None
    row=dict(candidate=cid,edges=edges,**stats,unrestricted_coloring_sat=satcolor,red=red);logs['candidates'].write(json.dumps(row)+'\n');logs['candidates'].flush()
    if satcolor is None:summary['status']='COLOR_ORACLE_UNKNOWN';break
    if satcolor is False:
     event(event='UNSAT_CANDIDATE_BEGIN_INDEPENDENT_EXHAUSTION',candidate=cid);verification=exhaust(edges)
     dump(HERE/'ALLEGED_COUNTEREXAMPLE.json',dict(**row,independent_exhaustive=verification));assert verification['non_2_colorable']
     summary['status']='COUNTEREXAMPLE_INDEPENDENTLY_EXHAUSTED';break
    assert proper(edges,red);added=int(addcut(master,edges,red,cid,'unrestricted_oracle'))
    # More unrestricted proper colourings, never balanced-only inference.
    with Minisat22(bootstrap_with=clauses) as supplemental:
     while added<args.batch and time.monotonic()<deadline:
      supplemental.set_phases([v+1 if rng.getrandbits(1) else -(v+1) for v in range(21)])
      summary['supplemental_oracle_calls']+=1;ss=solve(supplemental,deadline,args.conflicts,args.slice_seconds)
      if ss is not True:break
      mm=supplemental.get_model();rr=[v for v in range(21) if v+1 in mm];added+=int(addcut(master,edges,rr,cid,'unrestricted_supplement'))
      supplemental.add_clause([-(v+1) if v in rr else v+1 for v in range(21)])
    event(event='CANDIDATE_COLOURABLE',candidate=cid,cuts_added=added,total_cuts=summary['cuts'])
   else:
    summary['status']='TIME_BUDGET_NO_COUNTEREXAMPLE' if time.monotonic()>=deadline else 'CANDIDATE_BUDGET_NO_COUNTEREXAMPLE'
   summary['master_stats']=master.accum_stats()
 except BaseException as error:
  summary['status']='ERROR';summary['error']=repr(error);raise
 finally:
  summary['elapsed_seconds']=time.monotonic()-started;summary['process_cpu_seconds']=time.process_time()-cpu;summary['finished_utc']=datetime.now(timezone.utc).isoformat();summary['cut_red_size_histogram']=dict(sizehist)
  dump(HERE/'SUMMARY.json',summary)
  for f in logs.values():f.close()
 print(json.dumps(summary),flush=True)
if __name__=='__main__':main()
