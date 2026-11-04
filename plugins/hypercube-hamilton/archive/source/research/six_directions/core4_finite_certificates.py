"""Generate and independently check every explicitly saved core4 residual."""
import json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
def run(c):
    prefix='t15_core4_r4_small_c0' if c==0 else f'r4_joint_fourbridge_core4_c{c}'
    report=json.loads((R/f'{prefix}.json').read_text(encoding='utf-8-sig'))
    expected=report['residual_inputs'] if c==0 else report['residual']
    inp=R/f'{prefix}_residual_inputs.bin';cert=R/f'{prefix}_residual.bin';failure=R/f'{prefix}_failures.txt'
    assert inp.stat().st_size==26*expected
    data=json.loads(subprocess.check_output([str(R/'q5_full_input_certifier.exe'),str(inp),str(cert),str(failure),'1','2'],text=True))
    (R/f'{prefix}_certificates.json').write_text(json.dumps(data,indent=2)+'\n')
    assert data['total']==data['positive']==expected and data['unknown']==data['negative']==0
    check=json.loads(subprocess.check_output([str(R/'verify_q5_full_input_certificates.exe'),str(inp),str(cert),str(expected),'1','2'],text=True))
    (R/f'{prefix}_certificates_verification.json').write_text(json.dumps(check,indent=2)+'\n')
    print(c,expected,check['status'],flush=True)
if __name__=='__main__':
    for c in (0,4,6,8):run(c)
