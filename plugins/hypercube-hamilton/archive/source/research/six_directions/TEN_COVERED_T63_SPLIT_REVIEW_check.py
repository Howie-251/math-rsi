"""Independent read-only input audit; never imports or runs a producer."""
from pathlib import Path
from itertools import combinations, permutations
from collections import Counter
import json, hashlib, datetime
R=Path(__file__).resolve().parent
def digest(p): return hashlib.sha256((R/p).read_bytes()).hexdigest()
def load(p): return json.loads((R/p).read_text(encoding='utf-8'))
manifest=load('Q5_T63_COMPLETE_SPLIT_manifest.json')
initial={p:digest(p) for p in manifest['hashes']}
assert initial==manifest['hashes']
assert all((R/p).stat().st_size==n for p,n in manifest['sizes'].items())
# Verify accepted frozen residuals against prior review's bindings, as imports.
accepted=load('Q5_A8_CONSEQUENCES_REVIEW.json')
assert accepted['verdict']=='PASS'
profile=load('ten_covered_t63_complete_split_profile.json')
inputs=['TEN_COVERED_T63_SPLIT_APPLICATION.md','ten_covered_t63_complete_split_profile.py','ten_covered_t63_complete_split_profile.json','Q5_A8_CONSEQUENCES_REVIEW.json','HIGHER_HOLE_UNIFIED_TRANSFER.md','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_T63_COMPLETE_SPLIT.md','Q5_T63_COMPLETE_SPLIT_manifest.json']
for p in ('HIGHER_HOLE_UNIFIED_TRANSFER.md','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json'):
    assert digest(p)==accepted['audited_input_hashes'][p]
for v in (1,7,31): inputs += [f'ten_covered_after_full_A8_v{v}.bin',f'ten_covered_t63_complete_split_remaining_v{v}.bin']
input_hashes={p:digest(p) for p in inputs}
def short(a,b): return (a^b).bit_count()==1
def proj(x,d): return sum(((x>>i)&1)<<(i-(i>d)) for i in range(6) if i!=d)
def routes(z,w,v):
    found=[]
    for outer in range(6):
        inside=lambda x: (x>>outer&1)==(v>>outer&1)
        ze=[x for x in z if inside(x)];wo=[x for x in w if inside(x)]
        row=(len(ze),len(wo))
        if row==(4,2): source=ze; base=set(w)-set(wo)
        elif row==(1,5): source=[x for x in wo if (x^(1<<outer))!=0];base=set(z)-set(ze)
        else: continue
        for selection in combinations(source,3):
            mirrors={x^(1<<outer) for x in selection}
            assert len(mirrors)==3 and 0 not in mirrors
            assert mirrors.isdisjoint(set(z)|set(w))
            # An original crossing port at a mirror would have to match its free source.
            assert all(x in set(z)|set(w) for x in selection)
            holes=set(base)|mirrors
            assert len(holes)==6 and len({x.bit_count()%2 for x in holes})==1
            local_h=tuple(sorted(proj(x,outer) for x in holes));local_u=tuple(sorted(proj(x,outer) for x in mirrors))
            good=[d for d in range(5) if (sum((x>>d&1)==0 for x in local_h),sum((x>>d&1)==0 for x in local_u)) in ((2,1),(4,2))]
            if good: found.append((outer,row,tuple(selection),local_h,local_u,tuple(good)))
    return found
reports=[]
for v,declared in zip((1,7,31),profile['reports']):
    p=f'ten_covered_after_full_A8_v{v}.bin';raw=(R/p).read_bytes()
    assert digest(p)==accepted['audited_input_hashes'][p]
    assert len(raw)%9==0 and declared['v']==v
    recs=[raw[i:i+9] for i in range(0,len(raw),9)]
    assert len(recs)==len(set(recs))
    wit={w['input_index']:w for w in declared['witnesses']}
    assert len(wit)==len(declared['witnesses'])
    remaining=[];hits=set();legal_positive_choices=0
    for index,rec in enumerate(recs):
        z,w=list(rec[:4]),list(rec[4:])
        assert z==sorted(z) and w==sorted(w) and len(set(rec))==9
        assert 0 not in rec and v not in w and all(x<64 for x in rec)
        assert all(x.bit_count()%2==0 for x in z) and all(x.bit_count()%2==1 for x in w)
        assert not any(short(x,y) for x in z for y in w)
        options=routes(z,w,v);legal_positive_choices+=len(options)
        if options:
            hits.add(index);assert index in wit
            a=wit[index]
            claimed=(a['cut'],tuple(a['row']),tuple(a['S']),tuple(a['H']),tuple(a['U']),tuple(a['split_witness'][0]))
            assert claimed in options
        else: remaining.append(rec);assert index not in wit
    frozen=(R/f'ten_covered_t63_complete_split_remaining_v{v}.bin').read_bytes()
    assert frozen==b''.join(remaining)
    assert {frozen[i:i+9] for i in range(0,len(frozen),9)}==set(recs)-{recs[i] for i in hits}
    assert set(wit)==hits and len(hits)==declared['conditionally_covered'] and len(remaining)==declared['remaining']
    assert declared['input_sha256']==digest(p) and declared['remaining_sha256']==hashlib.sha256(frozen).hexdigest()
    reports.append(dict(v=v,input_count=len(recs),newly_covered=len(hits),remaining=len(remaining),positive_source_choices_checked=legal_positive_choices,all_declared_witnesses_valid=True,exact_bytes_equal=True,exact_set_equal=True,remaining_sha256=hashlib.sha256(frozen).hexdigest()))
assert sum(r['newly_covered'] for r in reports)==12916 and sum(r['remaining'] for r in reports)==41306
# Optional local interface witnesses are checked positively, including connectivity.
ports=load('Q5_T63_four_port_complete.json');global_raw=(R/'Q5_T63_exception_positive_cycles.bin').read_bytes();bridges=Counter()
assert {e['input_index'] for e in ports['witnesses']}==set(range(1320))
def ce(c): return {tuple(sorted((x,c[(i+1)%len(c)]))) for i,x in enumerate(c)}
for entry in ports['witnesses']:
    i=entry['input_index'];record=global_raw[i*63:i*63+63];assert len(record)==63
    local=[]
    for side in ('A','B'):
        c=entry[side+'_cycle'];deleted={tuple(sorted(e)) for e in entry[side+'_deleted']};es=ce(c)
        offset=0 if side=='A' else 16;mate=record[offset:offset+16]
        omit={0} if side=='A' else set(record[32:34])
        assert len(c)==len(set(c)) and set(c)==set(range(16))-omit
        required={tuple(sorted((x,y))) for x,y in enumerate(mate) if y!=255}
        assert required<=es and deleted<=es and not(required&deleted)
        assert all(short(x,y) for x,y in es-required)
        assert sorted(x for e in deleted for x in e)==entry['ports'] and len(entry['ports'])==len(set(entry['ports']))
        local.append({(a+offset,b+offset) for a,b in es-deleted})
    joined=local[0]|local[1]|{(x,x+16) for x in entry['ports']}
    assert joined==ce(list(record[34:]))
    assert entry['bridges']==len(entry['ports']);bridges[entry['bridges']]+=1
assert len(ports['witnesses'])==1320 and bridges=={4:1308,6:12}
# Reconstruct all marked six-hole geometries and parity-preserving orbits.
even=[x for x in range(32) if x.bit_count()%2==0]
unseen={(h,u) for h in combinations(even,6) for u in combinations(h,3)}
total=len(unseen);good_count=0;orbit_count=0;good_orbits=0
automorphisms=[]
for p in permutations(range(5)):
    linear=[sum(((x>>j)&1)<<p[j] for j in range(5)) for x in range(32)]
    for shift in even:automorphisms.append([x^shift for x in linear])
def has_split(h,u): return any((sum((x>>d&1)==0 for x in h),sum((x>>d&1)==0 for x in u)) in ((2,1),(4,2)) for d in range(5))
while unseen:
    h,u=next(iter(unseen));orbit={(tuple(sorted(m[x] for x in h)),tuple(sorted(m[x] for x in u))) for m in automorphisms}
    assert orbit<=unseen;unseen-=orbit;orbit_count+=1
    good=has_split(h,u);assert all(has_split(a,b)==good for a,b in orbit)
    if good:good_count+=len(orbit);good_orbits+=1
assert (total,good_count,orbit_count,good_orbits)==(160160,133760,135,106)
assert initial=={p:digest(p) for p in initial}
assert input_hashes=={p:digest(p) for p in input_hashes}
output=dict(status='PASS',manifest_hashes_checked=len(initial),manifest_sizes_checked=len(manifest['sizes']),frozen_inputs_unchanged=True,producer_imported_or_executed=False,reports=reports,newly_covered=12916,remaining_open=41306,local_positive_interfaces_checked=1320,geometry_census=dict(total=total,good=good_count,orbits=orbit_count,good_orbits=good_orbits),audited_input_hashes=input_hashes,manifest_input_hashes=initial)
(R/'TEN_COVERED_T63_SPLIT_REVIEW_check.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in output.items() if 'hashes' not in k},indent=2))
