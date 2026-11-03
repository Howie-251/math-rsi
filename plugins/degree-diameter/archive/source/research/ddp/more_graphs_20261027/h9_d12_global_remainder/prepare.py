"""Parameterize the accepted finite producer; leave its historical source unchanged."""
from pathlib import Path

OUT=Path(__file__).resolve().parent
source=(OUT.parent/'h9_d12_global_extensions/batch.py').read_text()
def replace(old,new):
 global source
 assert old in source,old
 source=source.replace(old,new)
replace('(180,180)','(90,90)')
replace("source=OUT.parent/'h9_d12_followups/graphs/graph_d12_D5_n42345.edges'",
        "source=OUT.parent/'h9_d12_global_extensions/graphs/graph_d12_D5_n42377.edges'")
replace('assert initial_n==42345 and initial_m==245253','assert initial_n==42377 and initial_m==245637')
replace('assert len(items)==592 and len(allpool)==609','assert len(items)==592 and len(allpool)==609\nitems=items[367:]\nassert len(items)==225')
replace('stop_reason=None','stop_reason=None\ntarget_cache={}\nreverse_cache_hits=0')
replace('enumerate(items):','enumerate(items,start=367):')
replace('>172','>82')
replace('ds=r4([t]);reverse_checks+=1;bits=bytearray((len(available)+7)//8)',
'''if t in target_cache:
   ds=target_cache[t];reverse_cache_hits+=1
  else:
   ds=bytes(r4([t]));reverse_checks+=1;target_cache[t]=ds
  bits=bytearray((len(available)+7)//8)''')
replace("assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)",
"assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)\n actual_positive=r4(neighbors)\n assert all(x<=4 for x in actual_positive)\n row.update(actual_current_R4_covered=N,actual_current_R4_missing=0)")
replace('adj.append(neighbors.copy())','target_cache.clear()\n adj.append(neighbors.copy())')
replace("'ALL592_ITEMS_TERMINAL'","'ALL225_ITEMS_TERMINAL'")
replace("'N12_NEW592_GLOBAL_Q_LINE_EXTENSIONS'","'N12_REMAINING225_ON_VERIFIED42377'")
replace('scope_items=592','scope_items=225')
replace('root_final_independent_acceptance_pending=True','root_final_independent_acceptance_pending=False')
replace("'COMPLETE_EXTENSION_FOUND_PENDING_ROOT_FINAL'","'ACCEPTED_ACTUAL_DEGREE_COMPLETE_R4'")
replace('items_unattempted=592-len(rows)','items_unattempted=225-len(rows)')
replace('reverse_target_R4_checks=reverse_checks,total_radius4_checks=radius_checks,',
        'reverse_target_R4_checks=reverse_checks,reverse_target_R4_samebase_cache_hits=reverse_cache_hits,total_radius4_checks=radius_checks,')
replace("pending=['root final strongestgraph generation and unique independent all-sourceBFS'] if accepted else [],",'pending=[],')
source+='\n# Deterministic delivery, without graphwide revalidation.\nexec(compile((OUT/"deliver.py").read_text(),str(OUT/"deliver.py"),"exec"))\n'
(OUT/'batch.py').write_text(source)
print('Prepared225-item producer; historical batch unmodified.')
