"""Small exact algebra checks for PROOF.md; not a source/H enumeration."""
from itertools import product
from pathlib import Path
import json

rows = []
for ew, ea, eb, ec in product(range(4), repeat=4):
    if ew + ea + eb + ec != 3:
        continue
    j = (4-ew-eb, 4-ew-ec, 3-ea-eb, 3-ea-ec)
    if min(j) < 0:
        continue
    sw, sa = ew+j[0]+j[1], ea+j[2]+j[3]
    sb, sc = eb+j[0]+j[2], ec+j[1]+j[3]
    assert (sw,sa,sb,sc) == (5+ea,3+ew,4+ec,4+eb)
    if sw > 7 or max(sa,sb,sc) > 6:
        continue
    if ec or eb or ew >= 2:
        mode = 'nonadjacent_common_and_high_degree_T_point'
    else:
        assert (ew,ea,eb,ec) == (1,2,0,0)
        assert (sw,sa,sb,sc) == (7,4,4,4)
        mode = 'common_small_negative_point'
    rows.append(dict(attachments=[ew,ea,eb,ec], cross_weights=j,
                     degrees=[sw,sa,sb,sc], mode=mode))

# Formula (3): blue singleton counts plus blue/blue J multiplicity.
formula_checks = 0
for k in (3,4):
    n2 = 14-k
    for r,z,beta in product(range(n2+1),range(n2+1),(0,1)):
        sq = n2-r+z
        uq = (12+beta if k == 3 else 12)-sq
        if uq < 0:
            continue
        assert uq+z == (r+1+beta if k == 3 else r+2)
        formula_checks += 1

out = dict(status='PASS', scope='scalar identities and exact equality-case exhaustion only',
           p3_equality_rows=rows, crosspair_formula_checks=formula_checks,
           actual_coverage='analytic PROOF.md, not inferred from this script')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(rows),'equality attachment cases;',formula_checks,'formula checks')
