#!/usr/bin/env python3
"""Linux stdlib complete at-most-seven CNF binding audit, no solver."""
import hashlib,json,pathlib,platform
assert platform.system()=='Linux'
root=pathlib.Path(__file__).resolve().parent;rows=json.loads((root/'first/rows.json').read_text());cnf=root/'budget7/formula.cnf'
actual=[list(map(int,line.split()))[:-1] for line in cnf.read_text().splitlines()[1:]];expected=[]
for r in rows:
    if r['kind']!='imported_total_holes_at_least_7':assert r['rhs']==1;expected.append([v+1 for v in r['support']])
names=[(i,j) for i in range(1,71) for j in range(1,9) if j<=i];lookup={name:k+71 for k,name in enumerate(names)}
for i in range(1,71):
    expected.append([-i,lookup[i,1]])
    for j in range(1,9):
        if (i-1,j) in lookup:expected.append([-lookup[i-1,j],lookup[i,j]])
    for j in range(2,9):
        if (i,j) in lookup:expected.append([-i,-lookup[i-1,j-1],lookup[i,j]])
expected.append([-lookup[70,8]]);assert actual==expected
header=cnf.read_text().splitlines()[0];assert header=='p cnf %s %s'%(70+len(names),len(expected))
result=json.loads((root/'budget7/result.json').read_text());assert result['cnf_sha256']==hashlib.sha256(cnf.read_bytes()).hexdigest()
assert result['status']=='CHECKED_UNSAT' and result['checker']['returncode']==0 and 's VERIFIED' in (root/'budget7/checker.log').read_text()
proof=root/'budget7/proof.drat';assert hashlib.sha256(proof.read_bytes()).hexdigest()==result['proof_sha256']
cover=json.loads((root/'first/cover.json').read_text());holes=cover['holes'];assert len(holes)==8 and all(len(set(holes)&set(r['support']))>=r['rhs'] for r in rows)
print(json.dumps(dict(host=platform.node(),status='PASS',row_clauses=93,counter_variables=len(names),total_clauses=len(expected),checked_at_most_7_unsat=True,verified_8_hole_witness=True,exact_matrix_minimum=8,cardinality_soundness='forward induction forces threshold(i,j) when prefix count >=j; actual prefix thresholds extend every <=7 vector',scope='the 93 proved necessary rows only; no real signotope construction'),indent=2))
