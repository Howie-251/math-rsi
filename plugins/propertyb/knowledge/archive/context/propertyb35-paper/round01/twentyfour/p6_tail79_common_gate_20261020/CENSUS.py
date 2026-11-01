"""Frozen79 P-side inputs; reconstruct own35traces, all60 proper P-colourings.
No exterior incidence is invented. Exact per-exterior-point signedocc cannot be
recovered from a P-trace inventory; the true caller gives the uniform bound7.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter,defaultdict
import json,time
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'positive_occ_three/nine_positive_joint_negative_budget_20261020/budget21_difference/P6_REMAINING.jsonl'
P=tuple(range(6));C=set(range(5));PAIRS=tuple(combinations(P,2))
BLUES=[b for k in range(1,6) for b in combinations(P,k) if set(b)&C and C-set(b)]
assert len(BLUES)==60
start=time.process_time()
def gate(s):
 p4,p3,p2,p1,n1,n2,t,b,ulb=s;m=p4+p3+p2+p1
 if p1 or n1:return None
 if m==0:return 'empty'
 if n2:
  if p3 or p2:return None
  for R in range(5):
   for S in range(4):
    T=9-2*R-S;B=18+R+S
    if T>=0 and p4==5-S and ulb>=17-3*S and n2<=R and t<=T and b<=B:return 'sparse_parameter_R%d_S%d'%(R,S)
  if p4==2 and ulb>=8 and n2<=3:return 'two_disjoint_3N2'
  return None
 if m<=4 and t<=3:return 'four_small_3T'
 if m<=5 and t<=1:return 'five_small_1T'
 if m<=5 and p2<=3 and t<=2:return 'five_small_2T'
 if p2:return None
 if m<=7 and p3<=2 and t<=1:return 'seven_mixed_2small_1T'
 if m<=7 and p3<=4 and t==0:return 'seven_mixed_4small_0T'
 if m==8 and p3<=2 and t==0 and b<=21:return 'eight_mixed_2small_0T_B21'
 if p3:return None
 if p4<=5 and ((t<=10 and b<=32) or t+b<=35):return 'five_four_joint35'
 if p4<=6 and t<=6 and b<=35:return 'six_four_6T'
 if p4<=6 and ulb>=14 and t<=8 and b<=20:return 'six_four_large_union'
 if p4<=7 and t<=4 and b<=35:return 'seven_four_4T'
 if p4<=8 and t==0 and b<=27:return 'eight_four_0T_B27'
 if p4<=11 and t==0 and b<=17:return 'eleven_four_0T_B17_L18'
 if p4==8 and t<=2 and b<=18:return 'eight_four_2T_B18_L18'
 if p4==8 and t<=1 and b<=20:return 'eight_four_1T_B20_L18'
 if p4==9 and t<=3:return 'nine_four_3T_arbitraryB_L18'
 return None

def provisional10(s):return s[:6]==(10,0,0,0,0,0) and s[6]<=2 and s[7]<=18

def build(r,index):
 degrees=[8+int(v==r['nine']) for v in P]
 traces=[tuple(range(5))]+[tuple(t) for t in r['higher']]
 for p,n in zip(PAIRS,r['J']):traces.extend([p]*n)
 h=Counter(v for t in traces for v in t)
 private=[degrees[v]-h[v] for v in P]
 for v,u in enumerate(private):traces.extend([(v,)]*u)
 assert min(private)>=0 and len(traces)==35
 assert [sum(v in t for t in traces) for v in P]==degrees
 assert [sum(1<<v for v in t) for t in traces]==r['trace_masks']
 assert sum(5-len(t) for t in traces)==126
 unions=[max(0,18-sum(5-len(t) for t in traces if v in t and len(t)>1)) for v in P]
 assert unions==r['private_star_union_lower_bounds']
 menus=[]
 for blue in BLUES:
  B=set(blue);pos=Counter();neg=Counter();roles=[];ps=[];ns=[]
  for i,t in enumerate(traces):
   S=set(t);k=5-len(t)
   if S<=B:pos[k]+=1;role='P';ps.append(i)
   elif not S&B:neg[k]+=1;role='N';ns.append(i)
   else:role='proper'
   roles.append([i,role,k])
  assert roles[0][1]=='proper'
  sig=(pos[4],pos[3],pos[2],pos[1],neg[1],neg[2],neg[3],neg[4],max(unions[v] for v in blue))
  active=sum(k for _,sign,k in roles if sign!='proper')
  assert active<=126
  menus.append({'blue':blue,'signature':sig,'roles':roles,'positive_source_indices':ps,'negative_source_indices':ns,
   'positive_count_by_size':{str(k):pos[k] for k in range(1,5)},'negative_count_by_size':{str(k):neg[k] for k in range(1,5)},
   'signed_total_occurrence':active,'signed_point_occurrence_upper_bound':[7]*18,
   'signed_point_occurrence_exact':'not determined by P-traces; <= actual exterior degree7',
   'private_positive_groups':[{'center':v,'edge_indices':[i for i,t in enumerate(traces) if t==(v,)],'count':private[v],'union_lower_bound':unions[v]} for v in blue],
   'proved_gate':gate(sig),'provisional_exact10_match':provisional10(sig)})
 old={tuple(c['blue']):c for c in r['choices']}
 assert len(old)==35
 for c in menus:
  if tuple(c['blue']) in old:
   a=old[tuple(c['blue'])]
   assert tuple(a['signature'])==c['signature'] and a['positive_source_indices']==c['positive_source_indices'] and a['negative_source_indices']==c['negative_source_indices']
 return {'source_index':index,'source_key':[r['inventory'],r['nine'],r['higher'],r['J']],
  'inventory':r['inventory'],'nine':r['nine'],'higher':r['higher'],'J':r['J'],
  'trace_masks':[sum(1<<v for v in t) for t in traces],'singleton_counts':private,
  'private_star_union_lower_bounds':unions,'PL_realizability':'Only original necessary P/L aggregate capacities; no exterior realization asserted.',
  'menus':menus}

seen=set();allrows=[];proven=[];conditional=[];tail=[];cells=Counter();best=Counter();sigfreq=Counter();loose=defaultdict(set)
for i,line in enumerate(SOURCE.open()):
 raw=json.loads(line);r=build(raw,i);key=json.dumps(r['source_key']);assert key not in seen;seen.add(key);allrows.append(r)
 w=next((c for c in r['menus'] if c['proved_gate']),None)
 q=next((c for c in r['menus'] if c['provisional_exact10_match']),None)
 if w:proven.append(dict(source_key=r['source_key'],source_index=i,blue=w['blue'],signature=w['signature'],gate=w['proved_gate']))
 elif q:conditional.append(dict(source_key=r['source_key'],source_index=i,blue=q['blue'],signature=q['signature'],gate='provisional_exact10P4_2T18B_L18_D7'))
 else:
  tail.append(r);cells[(tuple(r['inventory']),r['nine'])]+=1
  clean=[c for c in r['menus'] if not any(c['signature'][k] for k in (2,3,4,5))]
  assert clean
  w=min(clean,key=lambda c:(sum(c['signature'][:4]),c['signature'][1],c['signature'][6],c['signature'][7]))
  best[w['signature'][:8]]+=1
  for s in {tuple(c['signature'][:8]) for c in r['menus']}:sigfreq[s]+=1
  for c in r['menus']:
   s=c['signature'];p4,p3,p2,p1,n1,n2,t,b,ulb=s;m=p4+p3+p2+p1
   if not any((p2,p1,n1,n2)):
    if m==8 and p3<=2 and t<=2 and b<=20:loose['eight_mixed_le2P3_2T20B'].add(i)
    if m==9 and p3<=2 and t<=2 and b<=20:loose['nine_mixed_le2P3_2T20B'].add(i)
    if m<=10 and p3<=2 and t<=2 and b<=20:loose['atmostten_mixed_le2P3_2T20B'].add(i)
    if p3==0 and m<=11 and t<=4 and b<=20:loose['atmosteleven_pure_4T20B'].add(i)
   if p4==9 and not any((p3,p2,p1,n1)) and n2<=1 and t<=2 and b<=18:loose['nine_pure_1N2_2T18B'].add(i)
assert len(allrows)==79
for name,rows in [('ALL79_MENUS.jsonl',allrows),('PROVED_NEW.jsonl',proven),('PROVISIONAL_TEN_MATCHES.jsonl',conditional),('CONDITIONAL_REMAINING.jsonl',tail)]:
 with (HERE/name).open('w') as f:
  for r in rows:f.write(json.dumps(r,separators=(',',':'))+'\n')
out={'status':'COMPLETE_FROZEN79_SOURCE_MENU_CENSUS','sources':79,'old35_menus_checked':79*35,
 'all_proper_P_colourings':79*60,'original_edges_classified':79*60*35,
 'new_proved_gate_matches':len(proven),'provisional_ten_matches':len(conditional),'conditional_remaining':len(tail),
 'counts_by_inventory_nine':[{'inventory':k[0],'nine':k[1],'conditional_remaining':v} for k,v in sorted(cells.items())],
 'signature_order':['P4','P3','P2','P1','N1','N2','N3','N4','guaranteed_positive_union_lower_bound'],
 'provisional_ten_status':'Not treated as proved; exact10P4,L18,T<=2,B<=18,D7,N1=N2=0 only.',
 'best_clean_signature_by_source':[{'signature':s,'sources':n} for s,n in best.most_common()],
 'all_signature_frequency_in_conditional_remaining':[{'signature':s,'sources':n} for s,n in sigfreq.most_common()],
 'unproved_common_interfaces':[{'name':k,'sources':len(v),'source_indices':sorted(v)} for k,v in sorted(loose.items())],
 'perpoint_occurrence_scope':'Actual exterior point incidence is not present in P-side inventories. Each true caller has18 degree7 exterior points; each active original edge contributes exactly one signed constraint, so each actual signedpoint degree<=7. Stored signedtotalocc is exact; perpoint7 cap is proved, not fabricated exact degrees.',
 'cpu_seconds':time.process_time()-start}
(HERE/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k not in ('all_signature_frequency_in_conditional_remaining','best_clean_signature_by_source','unproved_common_interfaces')})
print('best',out['best_clean_signature_by_source']);print('interfaces',out['unproved_common_interfaces'])
