#!/usr/bin/env python3
"""Exact row-matrix hole-budget certificate with a forward prefix counter."""
import argparse,hashlib,json,pathlib,platform,subprocess,time
assert platform.system()=='Linux'
pa=argparse.ArgumentParser();pa.add_argument('--rows',required=True);pa.add_argument('--budget',type=int,required=True);pa.add_argument('--out',required=True);args=pa.parse_args();out=pathlib.Path(args.out);out.mkdir(exist_ok=False);rows=json.loads(pathlib.Path(args.rows).read_text());cap=args.budget+1;counter={};v=70
for i in range(1,71):
    for j in range(1,min(i,cap)+1):v+=1;counter[i,j]=v
clauses=[[h+1 for h in r['support']] for r in rows];assert all(r['rhs']==1 for r in rows)
for i in range(1,71):
    clauses.append([-i,counter[i,1]])
    if i>1:
        for j in range(1,min(i-1,cap)+1):clauses.append([-counter[i-1,j],counter[i,j]])
        for j in range(2,min(i,cap)+1):clauses.append([-i,-counter[i-1,j-1],counter[i,j]])
clauses.append([-counter[70,cap]]);cnf=out/'formula.cnf';proof=out/'proof.drat';cnf.write_text('p cnf %s %s\n'%(v,len(clauses))+''.join(' '.join(map(str,c))+' 0\n' for c in clauses));result=dict(host=platform.node(),row_file=args.rows,row_sha256=hashlib.sha256(pathlib.Path(args.rows).read_bytes()).hexdigest(),row_count=len(rows),budget=args.budget,variables=v,clauses=len(clauses),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest(),status='INCOMPLETE')
solver='/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat';checker='/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim'
with (out/'solver.log').open('w') as log:
    t=time.monotonic()
    try:p=subprocess.run([solver,str(cnf),str(proof)],stdout=log,stderr=subprocess.STDOUT,timeout=30);code=p.returncode
    except subprocess.TimeoutExpired:code='TIMEOUT'
    result['solver']=dict(returncode=code,seconds=time.monotonic()-t)
if code==20 and 's UNSATISFIABLE' in (out/'solver.log').read_text():
    with (out/'checker.log').open('w') as log:
        t=time.monotonic()
        try:p=subprocess.run([checker,str(cnf),str(proof)],stdout=log,stderr=subprocess.STDOUT,timeout=25);checked=p.returncode
        except subprocess.TimeoutExpired:checked='TIMEOUT'
        result['checker']=dict(returncode=checked,seconds=time.monotonic()-t)
    result['status']='CHECKED_UNSAT' if checked==0 and 's VERIFIED' in (out/'checker.log').read_text() else 'RAW_UNSAT_UNCHECKED'
else:result['status']='SAT_OR_UNKNOWN'
if proof.exists():result['proof_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest();result['proof_bytes']=proof.stat().st_size
(out/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
