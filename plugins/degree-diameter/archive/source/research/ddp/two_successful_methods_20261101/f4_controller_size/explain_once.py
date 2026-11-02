#!/usr/bin/env python3
"""Explain the complete controller failure by saturated same-base residues."""
import itertools
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
images=json.loads((HERE/'FORMAL_RESIDUE_CAPACITY.json').read_text())['formal_images_by_target_base']
def residues(base,params):
    return {sum(a*b for a,b in zip(x['coefficients'],params))%22 for x in images[base]}

cases=[]
for a,b,c in itertools.product(range(1,22),repeat=3):
    if a==11 or (b+c)%22==0:continue
    vals=(a,b,c,1,11)
    if len(residues(0,vals))!=22:continue
    missing=[[x for x in range(22) if x not in residues(k,vals)] for k in range(3)]
    cases.append({'alpha':a,'beta':b,'gamma':c,'tau':1,'missing_residues_by_target_base':missing})
assert all(x['missing_residues_by_target_base'][1] or x['missing_residues_by_target_base'][2] for x in cases)
result={
 'status':'NORMALIZED_SATURATED_SAME_BASE_CASES_ALL_FAIL_OTHER_BASE',
 'normalization':'Full root0 same-base coverage requires all22 formal images distinct. Parity of the ten +/- pairs forces tau odd; tau=11 collides with the halfdeck. All other odd tau are units, so rescale to tau=1.',
 'normalized_alpha_beta_gamma_cases':len(cases),
 'alpha_values':sorted({x['alpha'] for x in cases}),
 'all_cases_have_explicit_missing_other_base_residue':True,
 'cases':cases,
 'scope':'All voltage assignments in the stated C3 x Z22 organization; no claims about other66-point controllers or changed fiber rules.'
}
(HERE/'NORMALIZED_RESIDUE_EXPLANATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))

if __name__=='__main__':pass
