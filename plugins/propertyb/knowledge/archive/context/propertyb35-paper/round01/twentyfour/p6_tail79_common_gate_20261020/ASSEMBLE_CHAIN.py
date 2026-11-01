"""Bind root-accepted ten-gate59 and candidate mixedeight19, without conflation."""
from pathlib import Path
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
rows=list(map(json.loads,(HERE/'ALL79_MENUS.jsonl').open()))
ten=[];tail=[];mixed=[];last=[]
for r in rows:
 w=next((c for c in r['menus'] if c['signature'][:6]==[10,0,0,0,0,0] and c['signature'][6]<=2),None)
 if w:
  ten.append({'source_index':r['source_index'],'source_key':r['source_key'],'trace_masks':r['trace_masks'],'selected_blue':w['blue'],'selected_signature':w['signature'],'selected_roles':w['roles'],'positive_source_indices':w['positive_source_indices'],'negative_source_indices':w['negative_source_indices'],'signed_total_occurrence':w['signed_total_occurrence'],'point_occurrence_cap':[7]*18,'gate':'proofs/propertyb35/TEN_POSITIVE_TWO_TRIPLES_REPAIR.md','status':'root_paper_accepted; specified_cross_family_review_pending','full_menu_record':'ALL79_MENUS.jsonl source_index='+str(r['source_index'])})
 else:
  tail.append(r)
  options=[c for c in r['menus'] if sum(c['signature'][:2])==8 and c['signature'][1]<=1 and not any(c['signature'][k] for k in (2,3,4,5)) and c['signature'][6]<=2 and c['signature'][7]<=19]
  if options:
   w=min(options,key=lambda c:(c['signature'][6],c['signature'][1],c['signature'][7],c['blue']))
   mixed.append({'source_index':r['source_index'],'source_key':r['source_key'],'trace_masks':r['trace_masks'],'selected_blue':w['blue'],'selected_signature':w['signature'],'selected_roles':w['roles'],'private_positive_groups':w['private_positive_groups'],'signed_total_occurrence':w['signed_total_occurrence'],'point_occurrence_cap':[7]*18,'status':'candidate_mixed8_gate_independent_review_pending','full_menu_record':'ALL79_MENUS.jsonl source_index='+str(r['source_index'])})
  else:last.append(r)
assert (len(ten),len(tail),len(mixed),len(last))==(59,20,19,1)
for name,data in [('TEN_SOURCES59.jsonl',ten),('ROOT_CURRENT_TAIL20.jsonl',tail),('CANDIDATE_MIXED8_SOURCES19.jsonl',mixed),('IF_MIXED8_ACCEPTED_TAIL1.jsonl',last)]:
 with (HERE/name).open('w') as f:
  for r in data:f.write(json.dumps(r,separators=(',',':'))+'\n')
T={r['source_index'] for r in ten};M={r['source_index'] for r in mixed};L={r['source_index'] for r in last};assert not T&M and not T&L and not M&L and T|M|L==set(range(79))
cells=lambda data: [{'inventory':k[0],'nine':k[1],'count':n} for k,n in sorted(Counter((tuple(r['source_key'][0]),r['source_key'][1]) for r in data).items())]
last0=last[0];clean=[c for c in last0['menus'] if not any(c['signature'][k] for k in (2,3,4,5))]
last_w=min(clean,key=lambda c:(sum(c['signature'][:4]),c['signature'][1],c['signature'][6],c['signature'][7]))
out={'status':'EXACT_DISJOINT_SOURCE_CHAIN','input79':79,'root_accepted_ten':59,'current_tail20':20,'candidate_new_mixed8':19,'if_newmixedaccepted_tail':1,'all_keys_disjoint_exhaustive':True,
 'ten_by_inventory_nine':cells(ten),'candidate_mixed8_by_inventory_nine':cells(mixed),
 'ten_signed_counts':[{'signature':s,'count':n} for s,n in Counter(tuple(r['selected_signature'][:8]) for r in ten).items()],
 'mixed_signed_counts':[{'signature':s,'count':n} for s,n in Counter(tuple(r['selected_signature'][:8]) for r in mixed).items()],
 'last_source_index':last0['source_index'],'last_source_key':last0['source_key'],'last_minimum_clean_blue':last_w['blue'],'last_minimum_clean_signature':last_w['signature'],
 'current_status':'Only59 moved to root-paper-accepted gate.19 candidate newgate remain unaccepted here until root reads independent review. Last1 not covered.',
 'cpu_seconds':time.process_time()-start}
(HERE/'CHAIN.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
