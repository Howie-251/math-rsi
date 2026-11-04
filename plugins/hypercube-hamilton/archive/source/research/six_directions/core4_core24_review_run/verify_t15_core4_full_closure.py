"""Freeze core4's exact finite evidence and explicit imported proof scope."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
def read(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
def matching_lines(n):
    ans=[]
    for line in (R/n).read_text().splitlines():
        a=list(map(int,line.split()));assert len(a)%2==0
        ans.append(tuple(sorted(tuple(sorted(a[i:i+2])) for i in range(0,len(a),2))))
    assert len(ans)==len(set(ans));return set(ans)
def main():
    files={'T15_CORE4_FULL_CLOSURE.md','verify_t15_core4_full_closure.py','r4_joint_fourbridge_parent.cpp','verify_r4_joint_fourbridge_generic.cpp',
        't15_core4_r4_small_spectra.cpp','t15_core4_r4_small_negative.txt','t15_core4_r4_c2_types.cpp','verify_t15_core4_r4_c2_types.cpp',
        'verify_t15_core4_r4_c0_B.py','q5_full_input_certifier.cpp','verify_q5_full_input_certificates.cpp','R4_DOUBLE_BRIDGE_REVIEW.md','R4_DOUBLE_BRIDGE_REVIEW.json',
        'r4_joint_blocking_check.json','verify_q4_three_avoided_all.py','q4_three_avoided_all_verification.json','q4_five_avoided_probe.cpp','q4_five_avoided_jpair_prepare.py'}
    review=read('R4_DOUBLE_BRIDGE_REVIEW.json');assert review['verdict']=='PASS_WITH_SCOPE_LIMITS'
    for n,h in review['audited_input_hashes'].items():assert sha(n)==h.removeprefix('sha256:'),(n,h)
    fixed=next(x for x in read('q4_five_avoided_jpair_verification.json')['reports'] if x['core']==4)
    assert len(fixed['rows'])==18
    for row in fixed['rows']:assert sha(row['file'])==row['sha256'];files.add(row['file'])
    frozen='t15_core4_five_avoided_inputs.json';(R/frozen).write_text(json.dumps(dict(status='PASS',**fixed),indent=2)+'\n');files.add(frozen)
    c0=read('t15_core4_r4_c0_B_verification.json');assert c0['status']=='PASS' and c0['B_exceptions']==175 and c0['residual_full_input_list_rebuilt']==1819125
    c2=read('t15_core4_r4_c2_types_verification.json');assert c2['status']=='PASS' and c2['A_inputs']==62370 and c2['B_inputs']==945945 and c2['exceptional_B_inputs']==616 and c2['residual_full_inputs']==76839840
    files.update({'t15_core4_r4_c0_B_verification.json','t15_core4_r4_c2_types_verification.json','t15_core4_r4_c2_A_types.txt','t15_core4_r4_c2_B_types.txt','t15_core4_r4_c2_types.json'})
    exceptions=set()
    for line in (R/'t15_core4_r4_c2_B_types.txt').read_text().splitlines():
        a=list(map(int,line.split()))
        if a[0]==0:exceptions.add(tuple(sorted(tuple(sorted(a[i:i+2])) for i in range(3,len(a),2))))
    assert len(exceptions)==616 and matching_lines('r4_joint_fourbridge_core4_B2.txt')==exceptions
    joint=read('r4_joint_blocking_check.json')['reports'];rows=[]
    for c,nA,nB,total,residual in ((2,62370,616,76839840,0),(4,51975,272,339292800,3045),(6,13860,32,319334400,8820),(8,1485,1,59875200,2520)):
        inp=f'r4_joint_fourbridge_core4_B{c}.txt';actual=matching_lines(inp);assert len(actual)==nB
        if c>=4:assert actual=={tuple(map(tuple,F)) for F in next(r['matchings'] for r in joint if r['core']==4 and r['c']==c)}
        prefix=f'r4_joint_fourbridge_core4_c{c}';a=read(prefix+'.json');b=read(prefix+'_coverage_verification.json')
        assert b['status']=='PASS'
        for k,v in [('c',c),('A',nA),('B',nB),('inputs',total),('residual',residual)]:assert a[k]==b[k]==v,(prefix,k)
        assert (R/(prefix+'_residual_inputs.bin')).stat().st_size==residual*26
        files.update({inp,prefix+'.json',prefix+'_coverage_verification.json',prefix+'_residual_inputs.bin'});rows.append(b)
    direct=[]
    for c,count in ((0,1819125),(4,3045),(6,8820),(8,2520)):
        prefix='t15_core4_r4_small_c0' if c==0 else f'r4_joint_fourbridge_core4_c{c}'
        a=read(prefix+'_certificates.json');b=read(prefix+'_certificates_verification.json')
        assert a['total']==a['positive']==b['records']==count and a['negative']==a['unknown']==0 and b['status']=='PASS'
        assert (R/(prefix+'_residual_inputs.bin')).stat().st_size==count*26 and (R/(prefix+'_residual.bin')).stat().st_size==count*56
        files.update({prefix+'_residual_inputs.bin',prefix+'_residual.bin',prefix+'_certificates.json',prefix+'_certificates_verification.json'});direct.append(b)
    out=dict(status='PASS',scope='Complete candidate core4 finite package; fresh semantic audit pending',original_holes=[0,1,2,7,11,31],omitted=[1,2],fourbridge=rows,direct_certificates=direct,total_fourbridge_inputs=sum(r['inputs'] for r in rows),total_direct_certificates=sum(r['records'] for r in direct),input_sha256={n:sha(n) for n in sorted(files)},full_eight_hole_proved=False)
    assert out['total_fourbridge_inputs']==795342240 and out['total_direct_certificates']==1833510
    (R/'T15_CORE4_FULL_CLOSURE_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('input_sha256','fourbridge','direct_certificates')}))
if __name__=='__main__':main()
