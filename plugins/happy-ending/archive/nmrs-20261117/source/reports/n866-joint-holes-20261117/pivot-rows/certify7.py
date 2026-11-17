#!/usr/bin/env python3
"""Linux-only exact at-most-seven hole encoding and bounded external proof run."""
import hashlib,json,pathlib,platform,subprocess,time
assert platform.system()=='Linux'
root=pathlib.Path(__file__).resolve().parent;out=root/'budget7';out.mkdir(exist_ok=False);rows=json.loads((root/'first/rows.json').read_text())
clauses=[];metadata=[]
for i,r in enumerate(rows):
    if r['kind']=='imported_total_holes_at_least_7':continue
    assert r['rhs']==1;clauses.append([v+1 for v in r['support']]);metadata.append(dict(kind='row',row=i))
counter={};nextvar=70
for i in range(1,71):
    for j in range(1,min(i,8)+1):nextvar+=1;counter[i,j]=nextvar
for i in range(1,71):
    clauses.append([-i,counter[i,1]]);metadata.append(dict(kind='counter_input',i=i))
    if i>1:
        for j in range(1,min(i-1,8)+1):clauses.append([-counter[i-1,j],counter[i,j]]);metadata.append(dict(kind='counter_inherit',i=i,j=j))
        for j in range(2,min(i,8)+1):clauses.append([-i,-counter[i-1,j-1],counter[i,j]]);metadata.append(dict(kind='counter_increment',i=i,j=j))
clauses.append([-counter[70,8]]);metadata.append(dict(kind='at_most_7'))
cnf=out/'formula.cnf';proof=out/'proof.drat';cnf.write_text('p cnf %s %s\n'%(nextvar,len(clauses))+''.join(' '.join(map(str,c))+' 0\n' for c in clauses))
(out/'clause-metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
solver='/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat';checker='/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim'
result=dict(host=platform.node(),variables=nextvar,clauses=len(clauses),row_clauses=93,cardinality='sum of first 70 hole Booleans <= 7; forward threshold counter',cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest(),status='INCOMPLETE')
with (out/'solver.log').open('w') as log:
    t=time.monotonic()
    try:p=subprocess.run([solver,str(cnf),str(proof)],stdout=log,stderr=subprocess.STDOUT,timeout=30);code=p.returncode
    except subprocess.TimeoutExpired:code='TIMEOUT'
    result['solver']=dict(returncode=code,seconds=time.monotonic()-t)
if code==20 and 's UNSATISFIABLE' in (out/'solver.log').read_text():
    with (out/'checker.log').open('w') as log:
        t=time.monotonic()
        try:p=subprocess.run([checker,str(cnf),str(proof)],stdout=log,stderr=subprocess.STDOUT,timeout=20);checked=p.returncode
        except subprocess.TimeoutExpired:checked='TIMEOUT'
        result['checker']=dict(returncode=checked,seconds=time.monotonic()-t)
    result['status']='CHECKED_UNSAT' if checked==0 and 's VERIFIED' in (out/'checker.log').read_text() else 'RAW_UNSAT_UNCHECKED'
elif code==10:result['status']='SAT_REQUIRES_RETURNED_MODEL_RECHECK'
else:result['status']='TIMEOUT_OR_UNKNOWN'
if proof.exists():result['proof_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest();result['proof_bytes']=proof.stat().st_size
(out/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
