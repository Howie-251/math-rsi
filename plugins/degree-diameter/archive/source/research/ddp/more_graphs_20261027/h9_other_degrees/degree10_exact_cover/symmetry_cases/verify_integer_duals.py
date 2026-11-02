"""Exact integer checks and original-row binding for saved reduced-case duals; no solver/BFS."""
from pathlib import Path
import json
import numpy as np
H=Path(__file__).resolve().parent;E=H.parent
raw=(E/'unique_cover_rows.u8.bin').read_bytes();U=np.unpackbits(np.frombuffer(raw,dtype=np.uint8).reshape(26117,46),axis=1,bitorder='little')[:,:364]
checks=[]
for case in [4,3,2,1,0]:
 p=H/f'case{case}';dpath=p/'integer_dual.json'
 if not dpath.exists():continue
 d=json.loads(dpath.read_text());m=json.loads((p/'model.json').read_text());free=m['free_columns'];ones=m['fixed_one_columns'];zeros=m['initial_fixed_zero_columns']
 assert len(ones)==1 and not m['singleton_forcing']
 assert not m['inactive_columns_fixed_zero']
 assert sorted(free+ones+zeros)==list(range(364))
 active=np.flatnonzero(~U[:,ones].any(axis=1));B=U[np.ix_(active,free)]
 packed=np.packbits(B,axis=1,bitorder='little');unique,idx=np.unique(packed,axis=0,return_index=True)
 assert unique.tobytes()==(p/'rows.u8.bin').read_bytes()
 assert active[idx].tolist()==m['representative_original_unique_rows']
 # Sum at most364 positive integer weights against exact0/1 coefficients.
 loads=np.zeros(len(free),dtype=np.int64);total=0
 for row,w in d['weighted_reduced_rows']:
  assert isinstance(w,int) and w>0
  bits=np.unpackbits(unique[row],bitorder='little')[:len(free)].astype(np.int64)
  loads +=w*bits;total +=w
 den=d['denominator'];cap=m['remaining_pin_cap']
 assert loads.tolist()==d['per_free_column_loads']
 assert total==d['total_row_weight'] and int(loads.max())<=den and total>cap*den
 checks.append(dict(case=case,exact_integer_dual_valid=True,reduced_rows_bound_to_original=True,total_row_weight=total,denominator=den,
   remaining_pin_cap=cap,fixed_one_count=len(ones),integer_total_pin_lower_bound=len(ones)+(total+den-1)//den,max_column_load=int(loads.max())))
(H/'integer_duals_checked.json').write_text(json.dumps(dict(method='Exact integer0/1 row sums; recomputed row substitution and dedup from original26117coverer rows',cases=checks,new_solver_calls=0,new_BFS=0),indent=2)+'\n')
print(json.dumps(checks))
