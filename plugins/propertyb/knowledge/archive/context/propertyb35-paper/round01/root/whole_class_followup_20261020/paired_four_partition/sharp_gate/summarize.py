"""Summarize the frozen C++ full receipt, without rerunning any color counts."""
from pathlib import Path
from math import factorial
from collections import Counter
import json
P=Path(__file__).resolve().parent
d=json.loads((P/'RESULT.json').read_text())
def decode(k):
    digits=[]
    for _ in range(16):
        digits.append(k%5)
        k//=5
    assert k==0
    digits.reverse()
    return tuple(tuple(digits[4*i:4*i+4]) for i in range(4))
bykey={z['key']:z for z in d['records']}
per_orbit=Counter()
terminals=[]
for line in (P/'DOMAIN_MAP.tsv').read_text().splitlines():
    k,c=map(int,line.split())
    M=decode(k)
    assert list(M)==sorted(M)
    assert all(sum(row)==4 for row in M)
    assert all(sum(M[i][j] for i in range(4))==4 for j in range(4))
    mul=factorial(4)
    for n in Counter(M).values():
        mul//=factorial(n)
    assert c in bykey
    per_orbit[c]+=mul
    terminals.append(k)
assert len(terminals)==len(set(terminals))==465 and len(per_orbit)==43
for z in d['records']:
    z['row_column_labeled_matrix_count']=per_orbit[z['key']]
(P/'REPRESENTATIVES.json').write_text(json.dumps(d['records'],indent=2)+'\n')
manifest={'row_compositions':35,'column_permutations':24,'row_sorted_terminals':465,
          'fully_labeled_matrices':sum(per_orbit.values()),'row_column_orbits':43,'complete':d['complete'],
          'direct_X_subsets_per_representative':43758,'direct_X_subset_tests_full43':43*43758,
          'weighted_S_samples_per_representative':92378,'maximum_failure':12324,
          'maximizer_ids':[z['id'] for z in d['records'] if z['failure_count']==12324],
          'caller_base':79614,'caller_total':79614+12324,'caller_slack':92378-79614-12324,
          'profile_cpu_seconds':json.loads((P/'PROFILE.json').read_text())['total_cpu_seconds'],
          'full_cpu_seconds':d['total_cpu_seconds']}
assert manifest['fully_labeled_matrices']==10147
assert d['complete'] and d['checked']==43 and d['maximum_failure']==12324
(P/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
