"""Fresh deterministic audit: no producer verifier or producer coverage execution."""
from pathlib import Path
from itertools import permutations, combinations
from collections import Counter
import hashlib,json,subprocess
R=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
load=lambda n:json.loads((R/n).read_text(encoding='utf-8'))
manifest=load('Q5_T17_RANK_BATCH_MANIFEST.json')
assert sha((R/'Q5_T17_RANK_BATCH_MANIFEST.json').read_bytes())=='77122b232fd586043f6960ce466d465cbbd5ccce97aaac72dfecf8418bcdef6b'
for name,h in manifest['input_hashes'].items():assert sha((R/name).read_bytes())==h.removeprefix('sha256:'),name
forced={5,6,9,11,12,13,17}
statement_rows=[
([1,2,7,11,13,21,31],[1,2,13]),([1,2,7,13,26,28,31],[1,2,28]),
([1,2,7,25,26,28,31],[1,2,28]),([7,11,13,19,21,26,28],[7,11,19]),
([1,2,4,7,11,28,31],[1,2,4]),([1,2,4,11,13,22,31],[1,2,4]),
([1,2,13,14,21,25,28],[1,2,14]),([1,7,11,14,22,26,31],[1,7,11]),
([1,2,4,7,11,21,31],[1,2,4]),([1,7,14,22,25,26,31],[1,7,25]),
([1,2,4,11,19,25,26],[1,2,4]),([1,2,4,7,11,13,31],[1,2,4]),
([1,2,4,11,13,14,31],[1,2,4]),([1,7,14,22,25,26,28],[1,7,25]),
([1,7,11,14,21,26,28],[1,11,21]),([1,7,11,21,26,28,31],[1,11,21]),
([1,2,4,7,11,13,14],[1,2,4])]
perms=list(permutations(range(5)))
def image(x,perm):return sum(((x>>i)&1)<<perm[i] for i in range(5))
maps=[tuple(image(x,p) for x in range(32)) for p in perms]
orbits={};configs={};local=[]
for i in range(1,18):
    pre=f'Q5_T17_RANK_{"forced" if i in forced else "batch"}_{i:02}'
    a=list(map(int,(R/(pre+'_config.txt')).read_text().split()));h=set(a[:8]);om=set(a[8:11]);configs[i]=(h,om)
    assert (sorted(h-{0}),sorted(om))==statement_rows[i-1]
    assert len(h)==8 and 0 in h and len(om)==3 and om<=h-{0}
    for mp in maps:
        key=(tuple(sorted(mp[x] for x in h-{0})),tuple(sorted(mp[x] for x in om)))
        assert key not in orbits or orbits[key][0]==i
        ob=tuple(sorted(mp[x] for x in (8,16))) if i in forced else ()
        orbits[key]=(i,ob)
    p=subprocess.run([str(R/'Q5_T17_RANK_BATCH_REVIEW_check.exe'),pre,str(int(i in forced))],cwd=R,check=True,capture_output=True,text=True)
    local.append(json.loads(p.stdout))
(R/'Q5_T17_RANK_BATCH_REVIEW_local.json').write_text(json.dumps(local,indent=2)+'\n')
def erasebit(x,d):return sum(((x>>j)&1)<<(j-(j>d)) for j in range(6) if j!=d)
def insertbit(x,d):return sum(((x>>j)&1)<<(j+(j>=d)) for j in range(5))
def adjacent(x,y):return (x^y).bit_count()==1
def sig(w):return (w['v'],w['input_index'],w['cut'],tuple(w['source_triple']),w['orbit_id'])
uf=load('Q5_T17_RANK_batch_projection_witnesses.json');fp=load('Q5_T17_RANK_forced_projection_witnesses.json');sf=load('Q5_T17_RANK_forced_safe_witnesses.json')
U={(x['v'],x['input_index']):x for x in uf};F={(x['v'],x['input_index']):x['choices'] for x in fp};S={(x['v'],x['input_index']):x for x in sf}
assert len(U)==len(uf) and len(F)==len(fp) and len(S)==len(sf)
seenU=set();seenF=set();seenS=set();counts=[];projection_counts=Counter();sourcehashes={}
for v in (1,7,31):
    name=f'Q5_T26_RANK_BATCH_REVIEW_remaining_v{v}.bin';raw=(R/name).read_bytes();sourcehashes[name]=sha(raw)
    assert raw==(R/f'Q5_T26_RANK_batch_remaining_v{v}.bin').read_bytes() and len(raw)%9==0
    records=[raw[k:k+9] for k in range(0,len(raw),9)];assert len(set(records))==len(records)
    rem1=[];rem2=[];uc=fc=0
    for ix,record in enumerate(records):
        z=set(record[:4]);w=set(record[4:]);assert len(z)==4 and len(w)==5 and 0 not in z and v not in z|w
        assert all(0<x<64 and x.bit_count()%2==0 for x in z) and all(0<x<64 and x.bit_count()%2==1 for x in w)
        assert not any(adjacent(x,y) for x,y in combinations(z|w,2))
        choices={};unf=[];ff=[]
        for d in range(6):
            A={x for x in range(64) if ((x>>d)&1)==((v>>d)&1)};B=set(range(64))-A
            za=z&A;wa=w&A
            if (len(za),len(wa))==(3,1):triples=[tuple(sorted(za))];minor=next(iter(z&B));original=w&B
            elif (len(za),len(wa))==(0,4):triples=combinations(sorted(wa-{1<<d}),3);minor=next(iter(w&B));original=z&B
            else:continue
            for triple in triples:
                Y={x^(1<<d) for x in triple};assert len(Y)==3 and Y<=B and not Y&(z|w|{0})
                major=tuple(sorted(erasebit(x^minor,d) for x in original|Y));om=tuple(sorted(erasebit(x^minor,d) for x in Y))
                assert len(major)==7 and len(set(major))==7
                if (major,om) not in orbits:continue
                oid,normalizedOB=orbits[(major,om)]
                ob=tuple(sorted(insertbit(x,d)^minor for x in normalizedOB))
                if oid in forced:
                    assert len(ob)==2 and set(ob)<=B and not set(ob)&(z|w|Y)
                    assert all(adjacent(x,minor) for x in ob)
                info=(d,tuple(triple),oid,minor,major,om,ob)
                choices[(d,tuple(triple),oid)]=info
                (ff if oid in forced else unf).append(info);projection_counts['forced' if oid in forced else 'unforced']+=1
        key=(v,ix)
        def check_witness(p):
            assert p['v']==v and p['input_index']==ix and p['Z']==sorted(z) and p['W']==sorted(w)
            t=choices[(p['cut'],tuple(p['source_triple']),p['orbit_id'])]
            d,triple,oid,minor,major,om,ob=t
            assert p['minority']==minor and tuple(p['normalized_majority'])==major and tuple(p['normalized_omitted'])==om
            perm=p['permutation'];assert sorted(perm)==list(range(5));h,co=configs[oid]
            assert {image(x,perm) for x in major}==h-{0} and {image(x,perm) for x in om}==co
            if oid in forced:
                assert p['canonical_forced_pair']==[8,16] and tuple(p['actual_B_forced_pair'])==ob
                assert p['global_root_in_OB_pair']==(0 in ob)
            return t
        if unf:
            assert key in U and key not in F and key not in S
            assert check_witness(U[key])[2] not in forced;seenU.add(key);uc+=1
        else:
            assert key not in U;rem1.append(record)
            if ff:
                assert key in F and len({sig(p) for p in F[key]})==len(F[key])
                supplied={check_witness(p) for p in F[key]};assert supplied==set(ff);seenF.add(key)
            else:assert key not in F
            safe=[t for t in ff if 0 not in t[-1]]
            if safe:
                assert key in S and check_witness(S[key]) in safe;seenS.add(key);fc+=1
            else:assert key not in S;rem2.append(record)
        # No unforced/forced witness can be accepted solely by marginal orbit counts.
    b1=b''.join(rem1);b2=b''.join(rem2)
    assert b1==(R/f'Q5_T17_RANK_batch_remaining_v{v}.bin').read_bytes()
    assert b2==(R/f'Q5_T17_RANK_after_safe_forced_remaining_v{v}.bin').read_bytes()
    dest=f'Q5_T17_RANK_BATCH_REVIEW_remaining_v{v}.bin';(R/dest).write_bytes(b2)
    counts.append(dict(v=v,input=len(records),unforced=uc,forced_only_safe=fc,remaining=len(rem2),remaining_file=dest,remaining_sha256=sha(b2),unforced_remaining_sha256=sha(b1)))
assert seenU==set(U) and seenF==set(F) and seenS==set(S)
assert [a['unforced'] for a in counts]==[570,918,1110]
assert [a['forced_only_safe'] for a in counts]==[220,396,420]
assert [a['remaining'] for a in counts]==[120,162,180]
result=dict(status='PASS',manifest_sha256=sha((R/'Q5_T17_RANK_BATCH_MANIFEST.json').read_bytes()),manifest_bound_files_verified=len(manifest['input_hashes']),source_hashes=sourcehashes,local=local,forests=sum(a['forests'] for a in local),matrix_bits=sum(a['bits'] for a in local),reports=counts,actual_projection_counts=dict(projection_counts),unforced_witnesses=len(U),forced_only_all_choice_records=len(F),safe_witnesses=len(S),root_in_OB_projections_used=0)
(R/'Q5_T17_RANK_BATCH_REVIEW_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:val for k,val in result.items() if k!='local'},indent=2))
