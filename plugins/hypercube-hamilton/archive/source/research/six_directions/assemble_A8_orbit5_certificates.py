"""Assemble disjoint completed positive batches; check every input identity."""
import json,hashlib,os
from pathlib import Path
R=Path(__file__).resolve().parent
N=2732625
raw=(R/'A8_orbit5_joint_bad_inputs.bin').read_bytes();assert len(raw)==24*N
batches=[(0,1000000,R/'A8_orbit5_prefix_0_1000000.bin')]
for start in range(1000000,2500001,250000):
    n=min(250000,N-start);d=json.loads((R/f'A8_orbit5_chunk_{start}.json').read_text())
    assert d['total']==d['positive']==n and d['unknown']==d['search_exhausted']==0
    batches.append((start,n,R/f'A8_orbit5_chunk_{start}.bin'))
target=R/'A8_orbit5_joint_bad_certificates.bin';temporary=R/'A8_orbit5_joint_bad_certificates_assembling.bin'
assert target.resolve().parent==R.resolve()==temporary.resolve().parent
reports=[];position=0
with temporary.open('wb') as out:
    for start,n,p in batches:
        assert start==position
        b=p.read_bytes();assert len(b)==55*n
        for j in range(n):assert b[55*j:55*j+24]==raw[24*(start+j):24*(start+j)+24],(start,j)
        out.write(b);position+=n
        reports.append({'start':start,'records':n,'file':p.name,'sha256':hashlib.sha256(b).hexdigest()})
assert position==N
# Original full producer was explicitly stopped after verified prefix capture.
os.replace(temporary,target)
result={'status':'ASSEMBLED_ALL_POSITIVE_BATCHES','records':N,'input_identity_checked_for_every_record':True,
        'record_bytes':55,'certificate_bytes':target.stat().st_size,'certificate_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
        'batches':reports,'full_orbit_acceptance':'pending independent domain and cycle review','full_a8_proved':False}
(R/'A8_orbit5_joint_bad_certification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='batches'}))
