"""Complete marked 3:7/two-omission domain with independent included holes."""
from pathlib import Path
from itertools import combinations,permutations
import json
R=Path(__file__).resolve().parent
ev=[x for x in range(32) if x.bit_count()%2==0];od=[x for x in range(32) if x.bit_count()%2]
PERM=[tuple(sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)) for p in permutations(range(5))]
rows=[];minor_reports=[]
for pair in combinations(ev[1:],2):
    M=(0,*pair)
    canonical=min(tuple(sorted(t[x^s] for x in M)) for s in M for t in PERM)
    if M!=canonical:continue
    allowed=[y for y in od if all((x^y).bit_count()!=1 for x in M)]
    if len(allowed)<5:continue
    stab=[tuple(t[x^s] for x in range(32)) for s in M for t in PERM if tuple(sorted(t[x^s] for x in M))==M]
    domain=set();marked=set()
    for inc in combinations(allowed,5):
        for U in combinations([y for y in od if y not in inc],2):
            J=tuple(sorted(inc+U));domain.add((J,U))
            marked.add(min((tuple(sorted(t[x] for x in J)),tuple(sorted(t[x] for x in U))) for t in stab))
    images=set()
    for J,U in sorted(marked):
        orbit={(tuple(sorted(t[x] for x in J)),tuple(sorted(t[x] for x in U))) for t in stab}
        assert not images&orbit;images.update(orbit)
        rows.append({'minority':M,'majority':J,'omitted':U,'minor_stabilizer_orbit_size':len(orbit)})
    assert images==domain
    minor_reports.append({'minority':M,'available_included_majority':allowed,'stabilizer_size':len(stab),'raw_marked_domain':len(domain),'marked_orbits':len(marked)})
for i,row in enumerate(rows):row['index']=i
out={'status':'PRODUCER_ONLY','scope':'All Q5 3:7 holes with two marked majority omissions and included holes independent, modulo cube automorphisms','minority_orbits':minor_reports,'marked_orbits':len(rows),'rows':rows}
(R/'Q5_T37_INDEPENDENT_geometry.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
