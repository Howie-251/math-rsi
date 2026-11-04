"""Fresh audit checks; never imports producer modules or trusts PASS fields."""
import hashlib, itertools, json
from pathlib import Path
R = Path(__file__).resolve().parent

def pm(vertices):
    if not vertices:
        yield ()
    else:
        a, *rest = vertices
        for i, b in enumerate(rest):
            for tail in pm(rest[:i] + rest[i+1:]):
                yield tuple(sorted(((min(a,b),max(a,b)),) + tail))

def components(n, *matchings):
    root=list(range(n))
    def find(v):
        while root[v]!=v:
            root[v]=root[root[v]];v=root[v]
        return v
    for m in matchings:
        for a,b in m:root[find(a)]=find(b)
    return len({find(v) for v in range(n)})

out={'status':'PASS','producer_modules_imported':False}
data=json.loads((R/'three_matchings_disconnection.json').read_text())
assert len(data['families'])==2
basis=[]
for f,n,size in zip(data['families'],(6,8),(15,105)):
    assert f['n']==n
    expected=set(pm(list(range(n))))
    actual=[tuple(sorted(tuple(sorted(e)) for e in m)) for m in f['matchings']]
    assert len(actual)==size and len(set(actual))==size and set(actual)==expected
    base=f['base_index'];assert actual[base]==tuple((a,a+1) for a in range(0,n,2))
    ws=f['witness_D_indices'];assert len(ws)==size*size==f['ordered_pairs']
    for a,b in itertools.product(range(size),repeat=2):
        d=ws[a*size+b];assert type(d)==int and 0<=d<size
        assert all(components(n,actual[d],actual[k])>1 for k in (base,a,b))
    basis.append({'N':n,'perfect_matchings':size,'ordered_pairs_verified':len(ws)})
out['disconnection_basis']=basis

# Independently parse every table record and isolate exactly the negative family.
raw=(R/'q4_balanced_two_avoided_3_1.bin').read_bytes()
assert len(raw)==10395*30
seen=set();negative=set()
for i in range(0,len(raw),30):
    record=raw[i:i+30];m=record[:16]
    assert {a for a,b in enumerate(m) if b==255}=={0,7,3,1}
    assert all(b==255 or (b!=a and b<16 and m[b]==a) for a,b in enumerate(m))
    edges=tuple((a,b) for a,b in enumerate(m) if a<b<16)
    assert len(edges)==6 and edges not in seen;seen.add(edges)
    if record[16]==255:
        assert record[16:]==bytes([255])*14;negative.add(edges)
assert seen==set(pm([a for a in range(16) if a not in {0,7,3,1}])) and len(negative)==3
def swap(v):
    bits=[(v>>j)&1 for j in range(4)]
    bits[1],bits[2]=bits[2],bits[1]
    return sum(b<<j for j,b in enumerate(bits))
neg={3:negative,5:{tuple(sorted(tuple(sorted((swap(a),swap(b)))) for a,b in m)) for m in negative}}
families={}
for z,w in ((3,5),(5,3)):
    family=set()
    for m in neg[z]:
        for kept in itertools.combinations(m,4):
            support={v for e in kept for v in e}
            ports=set(range(16))-{0,7,1}-support
            assert len(ports)==5 and z in ports
            if w in ports:family.add((tuple(sorted(ports)),tuple(sorted(kept))))
    assert len(family)==15
    families[z]=family
assert not families[3]&families[5]
out['c5_inverse']={'candidate_counts':{z:len(fs) for z,fs in families.items()},'intersection':[],
    'candidates':{z:[{'ports':p,'F_B':m} for p,m in sorted(fs)] for z,fs in families.items()}}

# Counterexample pass for the occupied quotient, with zd fixed as 01.
# Relabeling reduces any D containing zd to this consecutive matching.
quotients=[]
for n in (4,6,8,10,12,14):
    D=tuple((a,a+1) for a in range(0,n,2));checked=0;total=0
    for rp in pm(list(range(n))):
        total+=1
        if components(n,D,rp)!=1:continue
        mate={a:b for x,y in rp for a,b in ((x,y),(y,x))}
        assert mate[0]!=1
        q=[e for e in rp if 0 not in e and 1 not in e]
        q.append(tuple(sorted((mate[0],mate[1]))))
        assert len(q)==n//2-1
        assert sorted(v for e in q for v in e)==list(range(2,n))
        assert components(n-2,[(a-2,b-2) for a,b in q],[(a-2,b-2) for a,b in D[1:]])==1
        checked+=1
    quotients.append({'N':n,'R_enumerated':total,'connected_R_union_D':checked,'failures':0})
out['occupied_quotient_counterexample_pass']=quotients

audit=json.loads((R/'T15_BALANCED_BRIDGE_REVIEW.json').read_text(encoding='utf-8-sig'))
imports=['q4_two_hole_3.bin','q4_two_hole_15.bin','q4_balanced_two_avoided_3_1.bin',
         'T15_BALANCED_BRIDGE_REVIEW.md']
imports+= [p.name for p in R.glob('q4_balanced_two_avoided_*.bin') if p.name not in imports]
out['import_hash_matches']={}
for name in imports:
    h='sha256:'+hashlib.sha256((R/name).read_bytes()).hexdigest()
    assert h==audit['audited_input_hashes'][name]
    out['import_hash_matches'][name]=h

# Freshly compiled graph checker output, never producer spectrum PASS fields.
rows=json.loads((R/'T15_CORE0_FULL_B_check.json').read_text(encoding='utf-8-sig'))
assert len(rows)==2
out['B_exhaustion']=[]
for row,c,total in zip(rows,(1,3),(135135,1621620)):
    assert row['core']==0 and row['c']==c and row['total']==total
    h={int(mask):n for mask,n in row['B_types'].items()}
    assert sum(h.values())==total and all(n>0 for n in h.values())
    if c==3:
        assert 0 not in h
        assert all(max((m&7).bit_count(),(m>>3).bit_count())>=2 for m in h)
        assert not (R/'T15_CORE0_FULL_core0_c3_B_exceptions.txt').read_text().strip()
    else:
        assert h[0]==6
    out['B_exhaustion'].append(row)
exceptions=[]
for line in (R/'T15_CORE0_FULL_core0_c1_B_exceptions.txt').read_text().splitlines():
    words=line.split();assert words[0]=='ports' and words[2]=='F'
    nums=list(map(int,words[3:]));assert len(nums)==12
    exceptions.append((int(words[1]),tuple(zip(nums[::2],nums[1::2]))))
inputs=[]
for line in (R/'t15_r3_small_core0_c1_B_inputs.txt').read_text().splitlines():
    nums=list(map(int,line.split()));assert len(nums)==13
    inputs.append((nums[0],tuple(zip(nums[1::2],nums[2::2]))))
assert len(inputs)==len(exceptions)==len(set(inputs))==6 and set(inputs)==set(exceptions)
for port,edges in inputs:
    assert sorted(v for e in edges for v in e)==[v for v in range(16) if v not in {0,7,1,port}]
out['c1_exception_inputs_exact']=True
res=json.loads((R/'T15_CORE0_FULL_residual_check.json').read_text(encoding='utf-8-sig'))
assert res=={'status':'PASS','records':810810,'required_edges':13,'cycle_vertices':30,
             'record_bytes':56,'total_bytes':45405360}
assert (R/'t15_r3_small_core0_c1_residual.bin').stat().st_size==res['total_bytes']
out['residual_certificates']=res
out['residual_certificate_sha256']=hashlib.sha256((R/'t15_r3_small_core0_c1_residual.bin').read_bytes()).hexdigest()
output=R/'T15_CORE0_FULL_independent_check.json'
output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='c5_inverse'}))
