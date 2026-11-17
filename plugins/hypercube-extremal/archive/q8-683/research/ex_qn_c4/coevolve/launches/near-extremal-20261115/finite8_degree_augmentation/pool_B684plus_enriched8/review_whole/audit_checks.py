"""Whole-proof review checks. Writes only beside this file; no producer imports."""
import json, hashlib, re
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations_with_replacement
from collections import Counter
from math import comb

HERE=Path(__file__).resolve().parent
P=HERE.parent
BASE=P.parents[1]
def read(p): return json.loads(Path(p).read_text())
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def nearest(n,d): return (2*n+d)//(2*d)
e=read(P/'exact_row_combination001/EXACT_COMBINATION.json')
a=read(P/'B684_ACTIVE_83_PARAMETERS.json')
meta=read(P/'CUT_ROW_METADATA.json')
assert sha(P/'CUT_ROW_METADATA.json')==a['metadata_sha256']
assert sha(P/'exact_row_combination001/EXACT_COMBINATION.json')==a['exact_combination_sha256']
active={i for i,v in enumerate(e['z']) if v}
assert active=={r['row_index'] for r in a['rows']} and len(active)==83
assert len(e['y'])==356 and len(e['z'])==8051 and all(v<=0 for v in e['z'])
dims=[240,212,190,187,170,9]
parameters=[]
for r in a['rows']:
    i=r['row_index']; m=r['full_metadata_row']; assert m==meta[i]
    assert F(r['positive_weight'])==-F(e['z'][i],10**9)>0
    h=hashlib.sha256(json.dumps(m,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert h==r['canonical_row_sha256']
    s=m.get('positive_power2_normalization',m.get('positive_normalization',1))
    assert isinstance(s,int) and s>0
    if m['kind'] in ('PSD','INTEGER_ROUNDING'):
        assert len(m['q'])==dims[m['block']] and all(type(v) is int for v in m['q'])
        if m['kind']=='PSD': assert m['block'] in range(4)
        else: assert m['n']==6 and type(m['t']) is int and m['block'] in range(5)
    if 'source' in m:
        assert sha(P/m['source'])==r['source_file_sha256']
    if 'exact_parameter_receipt' in r:
        assert sha(P/r['exact_parameter_receipt'])==r['exact_parameter_receipt_sha256']
    parameters.append({'row':i,'kind':m['kind'],'scale':s,'parameter_hash':r['parameter_sha256_used_in_table']})

# Complete profile enumeration from the inequalities, without using the source enumerator.
C=[735,534,333,177,66,0,0,105,345]
bc=[40,30,20,11,4,0,0,5,16]
profiles=read(P/'PROFILE_SNAPSHOT.json')['remaining']
generated=[]
for m in range(684,689):
    cap=138432-201*m
    def visit(degs,left,arr):
        if not degs:
            n6=m-sum(d*arr[d] for d in range(9))-5*(128-sum(arr))
            n5=128-sum(arr)-n6
            if min(n5,n6)<0: return
            row=arr.copy();row[5]=n5;row[6]=n6
            if sum(a*b for a,b in zip(row,bc))<=6912-10*m: generated.append((m,tuple(row)))
            return
        d=degs[0]
        for n in range(min(left//C[d],128-sum(arr))+1):
            arr[d]=n;visit(degs[1:],left-C[d]*n,arr);arr[d]=0
    visit([1,2,3,4,7,8],cap,[0]*9)
actual=[(r['m'],tuple(r['degrees'])) for r in profiles]
assert len(actual)==len(set(actual))==645 and set(actual)==set(generated)
assert Counter(m for m,_ in generated)=={684:385,685:170,686:66,687:20,688:4}
for row in profiles:
    n=row['degrees'];assert row['C']==sum(x*y for x,y in zip(C,n)) and row['b']==sum(x*y for x,y in zip(bc,n))
# Check both rearrangements coefficient by coefficient.
low=[sum(comb(d,j)*comb(8-d,6-j) for j in range(3) if j<=d and 0<=6-j<=8-d) for d in range(9)]
assert low==[28,28,28,18,6,0,0,0,0]
assert [40*comb(d,3)+2*comb(d,6)-5*low[d]-402*d+1610 for d in range(9)]==[2*x for x in C]
assert [comb(d,3)-10*d+40 for d in range(9)]==bc

# Full histogram order and exact endpoint-orbit cover (not a moment-only inference).
raw=read(P/'GENERATOR_HISTOGRAMS.json'); de=read(P/'GENERATOR_DEDUPLICATION.json')
expected=[]; allowed=[]
flip=lambda s: ((s&1)<<1)|((s&2)>>1)|(s&4)
def reversed_hist(x): return tuple(x[flip(i)] for i in range(len(x)))
for r in (0,1):
    for xs in combinations_with_replacement(range(8-r),7):
        x=[xs.count(i) for i in range(8-r)]
        if r==0 and x[7]==0: continue
        expected.append({'root_retained':r,'counts':x})
        da=r+sum((s&1)*v for s,v in enumerate(x));db=r+sum(((s>>1)&1)*v for s,v in enumerate(x))
        allowed.append(r==0 or ((da!=1 or x[6]==7) and (db!=1 or x[5]==7)))
assert raw==expected and len(raw)==3432
keep={i for i,ok in enumerate(allowed) if ok}
assert len(keep)==3202 and Counter(raw[i]['root_retained'] for i in keep)=={0:1716,1:1486}
partition=[i for g in de['groups'] for i in g]
assert len(partition)==len(set(partition)) and set(partition)==keep
for k,g in zip(de['selected_original_indices'],de['groups']):
    assert k in g
    h=raw[k]; orbit={(h['root_retained'],tuple(h['counts'])),(h['root_retained'],reversed_hist(h['counts']))}
    assert {(raw[j]['root_retained'],tuple(raw[j]['counts'])) for j in g}==orbit
assert len(de['groups'])==1751

# The concrete conditional parameter is an analytic equality on d=1,...,8.
c=read(P/'vertex_pricing/master_195/CONDITIONAL_VERTEX_CUT.json')
ss=[0,1,1,0,1,1,1,0,1]
assert c['integer_Q']==[[10**6*(2*x*y-1) for y in ss] for x in ss]
assert c['degree_bias_raw'][0]==0
for d in range(1,9):
    S=28-comb(8-d,2)
    assert c['degree_bias_raw'][d]==-10**6*(2*S*S-784)

# Recompute all extrema and rounding errors with integers only.
D=int(e['common_denominator']);T=10**9
nw=e['packed_kernel_numerators'];nh=e['histogram_packed_numerators']
assert len(nw)==101801 and len(nh)==5
q=[nearest(n*T,D) for n in nw];qh=[nearest(n*T,D) for n in nh]
starts=[0]
for d in dims:starts.append(starts[-1]+d*(d+1)//2)
errs=[abs(n*T-v*D) for n,v in zip(nw,q)]
eps=F(max(errs[:starts[5]])+max(errs[starts[5]:]),D*T)+F(16*max(abs(n*T-v*D) for n,v in zip(nh,qh)),64512*D*T)
delta=F(e['y'][0]+e['y'][1],10**9)
am=F(max(e['alpha_numerators']),D);bm=F(max(e['beta_numerators']),D)
assert delta==F(92993,500000000) and am==F(276661617,1027604480000000000) and bm==F(1,250000000)
assert eps==F(529874002317,601295421440000000000)
assert eps<=F(1,T)+F(8,64512*T)
matwords=(P/'exact_row_combination001/oracle_matrices.txt').read_text().split()
it=iter(map(int,matwords));assert [next(it) for _ in range(3)]==[1,-1,64512]
for b,dim in enumerate(dims):
    assert next(it)==dim
    M=[[next(it) for j in range(dim)] for i in range(dim)]
    assert all(M[i][j]==M[j][i] for i in range(dim) for j in range(dim))
    assert [M[i][j] for i in range(dim) for j in range(i,dim)]==q[starts[b]:starts[b+1]]
assert list(it)==[]
assert list(map(int,(P/'exact_row_combination001/oracle_linear.txt').read_text().split()))==[0]+qh
matrixhash='1a909bcc59b9ff22c679fc0d2c0ffed6e6a145e83688053793319e746feee372'
linearhash='1c2c16f76a493f9b171a145d7748b7993b1e092a5716524f43f9d6ef03c02506'
assert sha(P/'exact_row_combination001/oracle_matrices.txt')==matrixhash
assert sha(P/'exact_row_combination001/oracle_linear.txt')==linearhash
rawmax=-37440;M=F(rawmax,64512*T)
assert M==F(-13,22400000000)
margin=delta-am-bm-eps-M
assert margin==F(782808475930428709,4209067950080000000000)>0

# Bind real independent finite computations; do not rerun unchanged large work.
ind=read(BASE/'finite8_root_checks/exact_dual/review/independent_B8/INDEPENDENT_RESULT.json')
assert all(sha(path)==h for path,h in ind['hashes'].items())
assert len(ind['finite_active_checks'])==9
assert [x['minimum'] for x in ind['finite_active_checks'] if x['kind']=='CONNECTOR_FINITE6_EXTRA']==[240,240,112,176,56,104,66,128]
assert ind['exact_safe_margin']==str(margin) and ind['all356_exact_equality_maps_rebuilt']
for path,h in read(BASE/'finite8_root_checks/exact_dual/review/FINAL_CHECKS.json')['hashes'].items(): assert sha(path)==h
for path,h in read(P/'exact_row_combination001/RESULT.json')['parameter_source_hashes'].items(): assert sha(path)==h
for path,h in read(P/'FROZEN_CANDIDATE_INPUT_HASHES.json')['hashes'].items(): assert sha(P/path)==h
historical_mismatches=[]
for path,h in read(P/'RUN001_FROZEN_INPUT_HASHES.json')['hashes'].items():
    actual=sha(P/path)
    if actual!=h: historical_mismatches.append({'path':path,'historical_sha256':h,'current_sha256':actual})
freeze=BASE/'finite8_root_checks/exact_dual/review/FREEZE.json'
for path,h in read(freeze)['files'].items(): assert sha(freeze.parent/path)==h
q6=read(BASE/'finite8_q6_import_audit/FRESH_REPLAYS.json')
assert q6['case_count']==25 and len(q6['cases'])==25 and q6['verified_additions']==4383882
for case in q6['cases']:
    exe,cnf,trace=map(Path,case['command'])
    assert sha(exe)==case['checker_binary_sha256'] and sha(exe.with_suffix('.cpp'))==case['checker_source_sha256']
    assert sha(cnf)==case['cnf_sha256'] and sha(trace)==case['proof_sha256']
    assert case['returncode']==0 and case['real_replay']['valid'] and case['real_replay']['final_empty_clause']
    assert case['real_replay']['verified_additions']==case['strict_syntax']['additions']
assert sum(c['real_replay']['verified_additions'] for c in q6['cases'])==4383882
out={'status':'PASS_EXACT_SMALL_COVERS_PARAMETERS_HASH_BINDINGS_AND_MARGIN','profile_counts':dict(Counter(m for m,_ in generated)), 'raw_histograms':len(raw),'allowed_histograms':len(keep),'endpoint_orbits':1751,'active_rows':parameters,'conditional195':'analytic_identity_d1_to_d8_and_n0_zero','delta':str(delta),'alpha_max':str(am),'beta_max':str(bm),'eps':str(eps),'local_M':str(M),'margin':str(margin),'q6_bound_real_cases':25,'q6_bound_checked_additions':4383882,'query_matrix_sha256':matrixhash,'query_linear_sha256':linearhash,'large_work_replayed_here':False,'current_candidate_manifest_all_hashes_match':True,'historical_run001_not_a_current_input_manifest':historical_mismatches}
(HERE/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='active_rows'},indent=2))
