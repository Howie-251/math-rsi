"""Fresh review orchestration; production inputs are read-only throughout."""
from pathlib import Path
import json, hashlib, math, subprocess, datetime

O=Path(__file__).resolve().parent
R=O.parent
read=lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
def digest(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''): h.update(b)
    return 'sha256:'+h.hexdigest()

original=read(R/'T15_CORE27_FULL_CLOSURE_VERIFICATION.json')
hashes={p:digest(R/p) for p in original['audited_input_hashes']}
assert hashes==original['audited_input_hashes']
hashes['T15_CORE27_FULL_CLOSURE_VERIFICATION.json']=digest(R/'T15_CORE27_FULL_CLOSURE_VERIFICATION.json')

for c in (1,3,5):
    fresh=read(O/f'c{c}_rank.json')
    assert fresh==read(R/f't15_core27_c{c}_residual_verification.json')
freshB=read(O/'B_spectra.json')
assert freshB==read(R/'t15_core27_B_verification.json')
for c in (1,3):
    def exceptions(path):
        out=[]
        for line in path.read_text().splitlines():
            t=line.split(); i=t.index('F'); out.append(tuple(map(int,t[1:i]+t[i+1:])))
        return out
    fresh=exceptions(O/f't15_core27_checked_core27_c{c}_B_exceptions.txt')
    inputs=(R/f't15_core27_c{c}_B_inputs.txt').read_text().splitlines()
    expected=[tuple(map(int,line.split())) for line in inputs[1:]]
    assert len(fresh)==len(set(fresh))==int(inputs[0]) and set(fresh)==set(expected)
assert freshB[1]['B_types']['0']==24*math.factorial(3)
assert all(m=='0' or max((int(m)&7).bit_count(),(int(m)>>3).bit_count())>=2 for m in freshB[1]['B_types'])

# Execute exact submitted Python checkers, redirecting only their final write.
for name,outname in [('verify_t15_core27_blockers.py','t15_core27_blockers_verification.json'),
                     ('verify_t15_core27_full_closure.py','T15_CORE27_FULL_CLOSURE_VERIFICATION.json')]:
    text=(R/name).read_text()
    old=f"(R/'{outname}').write_text"
    assert text.count(old)==1
    text=text.replace(old,f"(Path({str(O/outname)!r})).write_text")
    # Blocker originally imports Path itself, as does aggregate.
    exec(compile(text,str(R/name),'exec'),{'__file__':str(R/name),'__name__':'__main__'})
    actual=read(O/outname); expected=read(R/outname)
    if 'generated_at' in actual:
        del actual['generated_at']; del expected['generated_at']
    assert actual==expected

# Assertions must be live: corrupt a valid first record in several independent ways.
data=(R/'t15_core27_c1_residual.bin').open('rb').read(56)
cases={}
b=bytearray(data); b[27]=b[26]; cases['cycle_repeated_vertex']=bytes(b)
b=bytearray(data); b[0]=b[1]; cases['required_edge_loop']=bytes(b)
b=bytearray(data); b[26]=19; cases['omitted_vertex']=bytes(b)
cases['truncated_record']=data[:-1]
cases['duplicate_record']=data+data
results=[]
for name,blob in cases.items():
    path=O/(name+'.bin'); path.write_bytes(blob)
    p=subprocess.run([str(O/'rank.exe'),'1',str(R/'t15_core27_c1_B_inputs.txt'),str(path),'9','6','15','8'],capture_output=True)
    assert p.returncode!=0
    results.append({'case':name,'rejected':True,'exit_code':p.returncode,'diagnostic':p.stderr.decode(errors='replace')[-600:]})

# Producer supports A port zero: it uses -1 as unset and excludes only three A holes.
# Prove at least one verified residual record actually has that boundary case.
portzero=[]
for c in (1,3,5):
    found=None
    with (R/f't15_core27_c{c}_residual.bin').open('rb') as f:
        for k in range(100000):
            d=f.read(56)
            if not d: break
            for j in range(13):
                u,v=d[2*j:2*j+2]
                if (u==1 and v%2==0) or (v==1 and u%2==0): found=k; break
            if found is not None:break
    assert found is not None
    portzero.append({'c':c,'verified_record_with_A_port_zero':found})

output={'status':'PASS','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'all_declared_hashes_match':True,'audited_input_hashes':hashes,
        'fresh_full_rank_runs':[read(O/f'c{c}_rank.json') for c in (1,3,5)],
        'fresh_B_spectra':freshB,'blocker_and_aggregate_replay_equal':True,
        'adversarial_rejections':results,'A_port_zero_examples':portzero}
(O/'independent_checks.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k not in ('audited_input_hashes','fresh_B_spectra','adversarial_rejections')},indent=2))
