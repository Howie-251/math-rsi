"""One complete cap-bounded residue decision over the persisted supports."""
from pathlib import Path
import json
import time

start=time.process_time()
out=Path(__file__).resolve().parent
meta=json.loads((out/'SUPPORTS.json').read_text())
K=meta['K']
raw=(out/meta['binary']).read_bytes()
assert len(raw)==57600*16
earlier=json.loads((out.parent/'RESULT.json').read_text())
records=[]
for m in range(18,K+1):
    if m in [18,19]:
        r=next(r for r in earlier['moduli'] if r['m']==m)
        assert not r['complete_R7_endpoint_certificate']
        records.append({'m':m,'n':1200*m,'admissible':False,'first_hole':r['first_hole'],
                        'earlier_exact_residue_result_reused':True,'slots_evaluated_now':0})
        continue
    first=None
    for slot in range(57600):
        mask=int.from_bytes(raw[16*slot:16*slot+16],'little')
        X=[c for c in range(-56,57) if (mask>>(c+56))&1]
        residues={c%m for c in X}
        if len(residues)<m:
            root,q=divmod(slot,1200)
            first={'root_base':root,'target_base':q//25,'a':q%5,'b':q%25//5,
                   'missing_c':sorted(set(range(m))-residues),'integer_scalar_endpoint_sums':X}
            break
    records.append({'m':m,'n':1200*m,'admissible':first is None,'first_hole':first,
                    'earlier_exact_residue_result_reused':False,'slots_evaluated_now':slot+1})
result={'K':K,'cap_witness':meta['cap_witness'],'larger_candidate_moduli':list(range(18,K+1)),
        'admissible_moduli':[r['m'] for r in records if r['admissible']],
        'modulus_results':records,'all_m_above_K_excluded_by_cardinality':True,
        'CPU_seconds':time.process_time()-start,'graph_generation':False,'BFS':0}
(out/'RESIDUE_DECISION.json').write_text(json.dumps(result,indent=2)+'\n')
