"""Scalar replay only: no H, coloring, private-edge or negative layout search."""
from pathlib import Path
import json

rows=[]
for e in range(4):
  for t in range(e+1):
    for m in range(t+1):
      if (m==0)!=(t==0):
        continue
      q=e-t
      for b in range(q+1):
        if (b==0)!=(q==0):
          continue
        private_meeting_Z=t+b+q
        assert private_meeting_Z<=2*e-t<=2*e-m
        all_edges_meeting_Z=13-e+private_meeting_Z
        uniform_upper=13+e-m
        assert all_edges_meeting_Z<=uniform_upper
        need=16*(8-m)
        bound=6*uniform_upper
        margin=need-bound
        assert margin==50-6*e-10*m and margin>0
        rows.append(dict(e=e,mixed_private_indices=t,mixed_private_points=m,
                         protected_extra_indices=q,multiple_private_protected_points=b,
                         private_indices_meeting_Z_upper=private_meeting_Z,
                         edges_meeting_Z_upper=all_edges_meeting_Z,
                         uniform_edges_upper=uniform_upper,
                         required_Z_P_pairs=need,uniform_pair_capacity=bound,
                         strict_margin=margin))
out=dict(status='PASS',scope='small scalar capacity domain only',rows=rows,
         minimum_strict_margin=min(r['strict_margin'] for r in rows),
         new_conclusion='second six-star normal form impossible; min(a,b)<=1 source',
         remaining_obligation='repair the possible single bad star edge')
assert out['minimum_strict_margin']==2
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(rows),'scalar rows; minimum strict pair margin2')
