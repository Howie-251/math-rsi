"""One independent n1/n4/n3 pass over all99 source moment domains under explicit all-lambda<=4. No layouts."""
from pathlib import Path
from math import comb
import json,time,argparse
P=Path(__file__).resolve().parent;M=P.parent.parent/'middle';st=time.process_time();ap=argparse.ArgumentParser();ap.add_argument('--profile',action='store_true');arg=ap.parse_args();INF=10**9
source=json.loads((M/'min_degree_seven_gamma_four_low_excess_diagnostic_20261020/RESULT.json').read_text())
strong=json.loads((M/'min_degree_seven_low_excess_strong_pairs_20261020/RESULT.json').read_text())
cap12=set(json.loads((M/'min_degree_seven_cap12_transfer_20261020/RESULT.json').read_text())['cap12_ready_ids']);assert len(cap12)==27
high=json.loads((P/'HIGH_ROW_CHECK.json').read_text());assert high['status']=='PASS';G={j['D']:j['G_D_tau0_through140'] for j in high['tables']}
oldfiltered=json.loads((P/'HIGH_ROW_FILTER_RESULT.json').read_text());oldjobs={j['id']:j for j in oldfiltered['jobs']}
exceptions=set(strong['spectra_with_unexcluded_pairs']);whole=set(strong['nonB_all_lambda_le4_spectrum_ids']);assert len(exceptions)==18 and len(whole)==81 and whole.isdisjoint(exceptions)
# Independent row19 DP, initialized from the sum/cost of zero pairs.
dp={0:0}
for _ in range(19):
 nxt={}
 for s,c in dp.items():
  for lam in (1,2,3,4):nxt[s+lam]=min(nxt.get(s+lam,INF),c+comb(lam-1,2))
 dp=nxt
for s in range(78):
 formula=INF if not 19<=s<=76 else max(0,s-38,2*s-95)
 assert dp.get(s,INF)==formula
# Same convex35 shared box from an independently balanced five-class construction.
box={}
for n1 in range(397,526):
 q,rem=divmod(2*n1,30);cells=[rem//5+int(i<rem%5) for i in range(5)]
 box[n1]=360*q+sum(cells[i]*cells[j] for i in range(5) for j in range(i))
jobs=[];partial=None
for job in source['jobs']:
 sid=job['spectrum_id'];ds=job['degrees'];assert len(ds)==21 and sum(ds)==175 and min(ds)==7 and sum(max(d-9,0) for d in ds)==job['e']<=4
 W=sum(d*(d-1)//2 for d in ds);assert W==job['W'];D,D2=sorted(ds)[-1],sorted(ds)[-2];r=max(0,4*D-40)
 rowchoices=[{'mutual_lambda':l,'required_tau':comb(l-1,2)+dp.get(4*D-l,INF)+dp.get(4*D2-l,INF)} for l in range(1,5)]
 rowunion=min(x['required_tau'] for x in rowchoices)
 costs=sorted(d for d in ds for _ in range(d*(d-1)//2));prefix=[0]
 for d in costs:prefix.append(prefix[-1]+d)
 coef=(sum(sorted(ds,reverse=True)[:6])-6)//2;c3=[min(12 if sid in cap12 else 13,G[D][tau]) for tau in range(141)]
 # C4 table uses a4<=min(tau//3,tau-r), in addition to all prior bounds.
 c4={}
 for tau in range(r,141):
  a4max=min(tau//3,tau-r);ellmax=2 if tau==0 else 3 if tau<3 else 4
  for t in range(47):c4[tau,t]=min(4*t,3*t+(D2-4)*a4max,2*t+(D2-3)*tau,ellmax*t)
 count=0;rowdiscard=0;maximum=-1;witness=None;survivors=[]
 for n1 in range(397,526):
  sharedP=box[n1];cost=prefix[n1]
  for t in range((W-n1)//4+1):
   lo=max(0,-((-2*r+W-280+8*t-n1)//3),W+n1-1190-2*t)
   hi=min((560-W-8*t+n1)//3,(W-n1-4*t)//3)
   if (lo-W+n1)%2:lo+=1
   for m in range(lo,hi+1,2):
    count+=1;tau=(W-280+3*m+8*t-n1)//2
    if tau<rowunion:rowdiscard+=1;continue
    n2=(W-n1-3*m-4*t)//2;n0=595-(W+n1-m-2*t)//2
    a0=33*n0;a1=35*n1-cost;a2=coef*n2;a3=c3[tau]*m;a4=c4[tau,t]
    # Layer-cake maximum, independent of root's descending-weight allocation.
    tail3=a3+a4;tail2=a2+tail3;tail1=a1+tail2;tail0=a0+tail1
    v=6864*n1+36*min(sharedP,tail0)+84*min(sharedP,tail1)+210*min(sharedP,tail2)+462*min(sharedP,tail3)+924*min(sharedP,a4)
    if v>maximum or v>=5445440:
     key={'n':[n0,n1,n2,m,t],'tau':tau,'twice_L':v,'caps':[a0,a1,a2,a3,a4],'C3_coefficient':c3[tau],'a4_max':min(tau//3,tau-r),'two_row_tau_lower':rowunion}
     if v>maximum:maximum=v;witness=key
     if v>=5445440:survivors.append(key)
   if time.process_time()-st>18.5:
    partial={'spectrum_id':sid,'resume_n1_n4':[n1,t],'prefix_keys':count};break
  if partial:break
 if partial:break
 assert count==job['complete_domain'],(sid,count,job['complete_domain'])
 if sid in oldjobs:
  expected={(tuple(x['n']),x['tau'],x['new_twice_L']) for x in oldjobs[sid]['survivors']}
  actual={(tuple(x['n']),x['tau'],x['twice_L']) for x in survivors};assert actual==expected,(sid,len(actual),len(expected))
 jobs.append({'spectrum_id':sid,'degrees':ds,'e':job['e'],'W':W,'D':D,'D2':D2,'S6':sum(sorted(ds)[-6:]),'cap12_actual_caller':sid in cap12,'lambda4_subcase_only':sid in exceptions,'full_paircap_from_nonB_pair_gates':sid in whole,'complete_source_moment_keys':count,'two_row_required_tau':rowunion,'two_row_mutual_lambda_branches':rowchoices,'discarded_by_two_row_union':rowdiscard,'capacity_evaluated_keys':count-rowdiscard,'maximum_twice_L':maximum,'maximum_witness':witness,'strict':not survivors,'survivor_count':len(survivors),'survivors':survivors})
 print('SPECTRUM',sid,'KEYS',count,'ROWEXCLUDED',rowdiscard,'SURVIVORS',len(survivors),'MAX',maximum,'CPU',time.process_time()-st,flush=True)
 if arg.profile:break
out={'status':'CPU_BOUNDED_PARTIAL' if partial else 'PROFILE_ONE_COMPLETE_SPECTRUM' if arg.profile else 'PASS_COMPLETE99_LAMBDA4_CONDITIONAL_DOMAINS','scope':__doc__,'hypotheses':['21 points35 simple5edges/paircover/minimum degree exactly7','e=summax(d-9,0)<=4','Gamma minimum degree4','all pointpair codegrees<=4 is explicit for every one of99 spectra','generic e<=4 cap13 local theorem; cap12 only for explicit27 actual callers'],'scalar_threshold_twice_L':5445440,'source99_spectra':99,'expected_source_moment_keys':source['completed_moment_keys'],'all_h19_values_independently_DP_checked':True,'h19_DP_table':dp,'cap12_actual_caller_ids':sorted(cap12),'prior81_survivor_sets_all_exactly_compared':len([j for j in jobs if not j['lambda4_subcase_only']])==81,'completed_spectra':len(jobs),'complete_source_moment_keys':sum(j['complete_source_moment_keys'] for j in jobs),'discarded_by_two_row_union':sum(j['discarded_by_two_row_union'] for j in jobs),'strict_spectrum_count':sum(j['strict'] for j in jobs),'strict_lambda4_subcase_only_ids':[j['spectrum_id'] for j in jobs if j['strict'] and j['lambda4_subcase_only']],'strict_whole_spectrum_ids_given_nonB_pair_import':[j['spectrum_id'] for j in jobs if j['strict'] and not j['lambda4_subcase_only']],'remaining_spectrum_ids':[j['spectrum_id'] for j in jobs if not j['strict']],'survivor_count':sum(j['survivor_count'] for j in jobs),'all_survivors_saved':True,'jobs':jobs,'partial':partial,'cpu_seconds':time.process_time()-st}
if not arg.profile and not partial:assert len(jobs)==99 and out['complete_source_moment_keys']==source['completed_moment_keys']==8042299
(P/('FINAL_LAMBDA4_PROFILE.json' if arg.profile else 'FINAL_LAMBDA4_VERIFY.json')).write_text(json.dumps(out,indent=2)+'\n');print('RESULT',out['status'],out['completed_spectra'],out['strict_spectrum_count'],out['survivor_count'],out['cpu_seconds'])
