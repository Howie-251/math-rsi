"""Fresh assembly review: exact marked-orbit replay, no producer imports.

Local universal matching theorems and earlier complete censuses are imports;
this file never substitutes a sampled matching for those quantifiers.
"""
from pathlib import Path
from itertools import permutations, combinations
import hashlib, json, re

P=Path(__file__).resolve().parent
def read(n): return (P/n).read_bytes()
def load(n): return json.loads(read(n))
def sha(n): return hashlib.sha256(read(n)).hexdigest()
def records(n):
    b=read(n); assert len(b)%9==0
    a=[b[k:k+9] for k in range(0,len(b),9)]
    assert len(a)==len(set(a))
    return a

reviews=['EIGHT_HOLE_FULL','HIGHER_HOLE_UNIFIED_TRANSFER','TEN_HOLE_FREE',
 'TEN_HOLE_COVERED_PARTIAL','Q5_A8_CONSEQUENCES','TEN_COVERED_T63_SPLIT',
 'TEN_COVERED_Q5_ENDPOINT','Q5_T26_RANK_BATCH','Q5_T15_RANK_BATCH']
bindings={}; imports={}
for stem in reviews:
    name=stem+'_REVIEW.json'; d=load(name); assert d['verdict']=='PASS'
    checked={}
    for group in d.values():
        if not isinstance(group,dict): continue
        for n,h in group.items():
            if not isinstance(h,str) or not re.fullmatch('(sha256:)?[0-9a-f]{64}',h): continue
            if not (P/n).exists(): continue # named schema fields handled below
            assert sha(n)==h.removeprefix('sha256:'),(name,n,'STALE')
            checked[n]=sha(n)
    if stem=='Q5_A8_CONSEQUENCES':
        e=d['evidence']
        for field in ['checker','report']:
            assert sha(e[field])==e[field+'_sha256'];checked[e[field]]=sha(e[field])
        n='Q5_A8_FULL_REVIEW.json';assert sha(n)==e['full_A8_final_review_sha256'];checked[n]=sha(n)
    bindings[name]=checked
    imports[name]={'sha256':sha(name),'declared_bindings_verified':len(checked)}

perms=[]
for perm in permutations(range(5)):
    perms.append((perm,[sum(((x>>j)&1)<<perm[j] for j in range(5)) for x in range(32)]))
look15={};look17={}
def register(table,ident,major,omitted,ob=None):
    for perm,im in perms:
        for shift in range(32):
            key=(shift,tuple(sorted(im[x]^shift for x in major)),tuple(sorted(im[x]^shift for x in omitted)))
            val=(ident,perm,shift,tuple(sorted(im[x]^shift for x in ob)) if ob else ())
            assert key not in table or table[key][0]==ident,('orbit overlap',ident)
            table[key]=val
for r in load('Q5_T15_RANK_batch_summary.json')['reports']:
    g=r['geometry'];register(look15,r['orbit_index'],g['majority'],g['omitted'])
for s in ['batch','forced']:
    for r in load('Q5_T17_RANK_'+s+'_summary.json')['orbits']:
        g=r['marked_geometry'];register(look17,r['id'],g['majority'],g['omitted'],g['forced_cherry_pair'])
proj=[[sum(((x>>j)&1)<<k for k,j in enumerate(j for j in range(6) if j!=cut)) for x in range(64)] for cut in range(6)]
def actual(rec,v):
    Z=set(rec[:4]);W=set(rec[4:]);assert len(Z)==4 and len(W)==5
    assert sorted(Z)==list(rec[:4]) and sorted(W)==list(rec[4:])
    assert 0 not in Z and v not in W and all(x<64 for x in Z|W)
    assert all(x.bit_count()%2==0 for x in Z) and all(x.bit_count()%2==1 for x in W)
    assert all((x^y).bit_count()!=1 for x in Z for y in W)
    found={k:[] for k in ['T15','unforced','forced_safe','forced_unsafe']};has17=False
    for cut in range(6):
        za={x for x in Z if (x>>cut&1)==(v>>cut&1)}
        wa={x for x in W if (x>>cut&1)==(v>>cut&1)}
        row=(len(za),len(wa))
        if row in [(3,2),(3,1)]: pool=za;minor=Z-za;base=W-wa
        elif row in [(1,4),(0,4)]:pool=wa-{1<<cut};minor=W-wa;base=Z-za
        else:continue
        is17=row in [(3,1),(0,4)];has17|=is17
        assert len(minor)==1
        for S in combinations(sorted(pool),3 if is17 else 2):
            Y={x^(1<<cut) for x in S};assert not (Y&({0}|Z|W))
            m=proj[cut][next(iter(minor))]
            major=tuple(sorted(proj[cut][x] for x in base|Y));om=tuple(sorted(proj[cut][x] for x in Y))
            key=(m,major,om);table=look17 if is17 else look15
            if key not in table:continue
            ident,perm,shift,ob=table[key]
            # Lift actual marked obstruction back to original Q6 B face.
            back={proj[cut][x]:x for x in range(64) if (x>>cut&1)!=(v>>cut&1)}
            obstruction=tuple(back[x] for x in ob)
            kind=('forced_unsafe' if 0 in obstruction else 'forced_safe') if ob else ('unforced' if is17 else 'T15')
            found[kind].append(dict(cut=cut,row=row,sources=S,minority=m,majority=major,omitted=om,
                 registry_id=ident,cube_permutation=perm,cube_shift=shift,obstruction_B=obstruction))
    return found,has17

rows=[];witnesses=[];residual17={};residual15={};all_sources={}
for v,expected in [(1,(910,570,220,120,480)),(7,(1476,918,396,162,846)),(31,(1710,1110,420,180,1020))]:
    source=f'Q5_T26_RANK_BATCH_REVIEW_remaining_v{v}.bin';a=records(source)
    assert sha(source)==load('Q5_T26_RANK_BATCH_REVIEW.json')['evidence'][source]
    rem15=set(records(f'Q5_T15_RANK_BATCH_REVIEW_remaining_v{v}.bin'))
    assert rem15<=set(a)
    new15=set();unforced=set();safe=set();none=set();no17=set()
    for index,rec in enumerate(a):
        f,has17=actual(rec,v)
        if not has17:no17.add(rec)
        if f['T15']:new15.add(rec)
        if f['unforced']:unforced.add(rec);kind='unforced'
        elif f['forced_safe']:safe.add(rec);kind='forced_safe'
        else:none.add(rec);kind='T15'
        assert f[kind],('UNCOVERED',v,index,list(rec))
        witnesses.append(dict(v=v,index=index,record=list(rec),route=kind,**f[kind][0]))
    assert new15==set(a)-rem15
    assert none==no17 and none<=new15
    assert not (unforced&safe or unforced&none or safe&none)
    assert unforced|safe|none==set(a)
    assert (len(a),len(unforced),len(safe),len(none),len(new15))==expected
    overlap=len((unforced|safe)&new15)
    rows.append(dict(v=v,input=len(a),T17_unforced=len(unforced),T17_forced_safe=len(safe),
          T17_remaining=len(none),T15_positive=len(new15),T15_T17_overlap=overlap,final_remaining=0))
    residual17[str(v)]=hashlib.sha256(b''.join(r for r in a if r in none)).hexdigest()
    residual15[str(v)]=hashlib.sha256(b''.join(r for r in a if r in rem15)).hexdigest()
    all_sources[source]=sha(source)
result=dict(stage='independent_union_verified_T17_acceptance_gate_separate',
 imports=imports,import_source_and_evidence_hashes=bindings,source_hashes=all_sources,
 rows=rows,remaining=0,actual_route_witnesses=len(witnesses),
 exact_T17_residual_hashes=residual17,exact_T15_residual_hashes=residual15,
 large_matching_certificates_rerun=False,old_complete_censuses_rerun=False)
(P/'TEN_HOLE_FULL_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'TEN_HOLE_FULL_REVIEW_witnesses.json').write_text(json.dumps(witnesses,separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['import_source_and_evidence_hashes']},indent=2))
