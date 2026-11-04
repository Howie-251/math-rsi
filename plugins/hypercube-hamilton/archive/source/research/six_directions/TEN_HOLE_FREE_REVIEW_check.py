"""Independent ten-free-hole geometry audit. No producer modules/data loaded.
Run in this directory: python TEN_HOLE_FREE_REVIEW_check.py
Requires g++ on PATH; writes only TEN_HOLE_FREE_REVIEW_* artifacts.
"""
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import subprocess

P = Path(__file__).resolve().parent
CORES = (0,1,2,4,5,7,8,10,13,14,15,18,19,21,23,24,25,27,31,32,35,37,38,44)
def digest(path):
    return 'sha256:' + hashlib.sha256(path.read_bytes()).hexdigest()
def key(omitted, included):
    assert len(set(omitted)) == 2 and len(set(included)) == 3
    assert not set(omitted) & set(included)
    assert all(x.bit_count()%2 for x in (*omitted,*included))
    return sum(1<<x for x in omitted) | (sum(1<<x for x in included)<<32)
def main():
    manifest=json.loads((P/'TEN_HOLE_FREE_REVIEW_imports.json').read_text(encoding='utf8'))
    for n,h in manifest['hashes'].items():
        assert digest(P/n)==h, ('stale imported theorem',n)
    # This JSON supplies labeled representatives only, never coverage counts.
    reps = json.loads((P/'t15_analytic_geometry.json').read_text(encoding='utf8'))['T15']['residual_orbits']
    for c in CORES:
        r=reps[c];a=manifest['complete_core_registry'][str(c)]
        assert sorted([0]+r['avoided']+r['included'])==a['holes']
        assert r['avoided']==a['omitted']
        report=json.loads((P/a['review']).read_text(encoding='utf8'))
        assert report['verdict']=='PASS'
    permutations = list(it.permutations(range(5)))
    allowed = {}
    for c in CORES:
        r = reps[c]
        for pi,p in enumerate(permutations):
            def image(x): return sum(((x>>j)&1)<<p[j] for j in range(5))
            om = tuple(sorted(map(image,r['avoided'])))
            inc = tuple(sorted(map(image,r['included'])))
            k = key(om,inc)
            if k in allowed: assert allowed[k][1] == c
            allowed[k] = ('core',c,pi)
    core_image_count = len(allowed)
    split_count = 0
    odd = [x for x in range(32) if x.bit_count()%2]
    for five in it.combinations(odd,5):
        for om in it.combinations(five,2):
            inc = tuple(x for x in five if x not in om)
            for d in range(5):
                if sum((x>>d)&1 for x in five)==2 and ((om[0]^om[1])>>d)&1:
                    split_count += 1
                    allowed.setdefault(key(om,inc),('split',d,-1))
                    break
    # Independently check every translate/delete map on every 6-cube face.
    projections = 0
    for d in range(6):
        delete = lambda x: (x&((1<<d)-1)) | ((x>>(d+1))<<d)
        for minority in range(64):
            face = [x for x in range(64) if (x>>d)&1 == (minority>>d)&1]
            assert delete(minority^minority)==0
            assert len({delete(x^minority) for x in face})==32
            for x,y in it.combinations(face,2):
                assert (x^y).bit_count()==(delete(x^minority)^delete(y^minority)).bit_count()
            projections += 1
    lookup=P/'TEN_HOLE_FREE_REVIEW_lookup.txt'
    with lookup.open('w',encoding='ascii') as f:
        for k,(kind,index,pi) in sorted(allowed.items()):
            f.write(f'{k} {0 if kind=="core" else 1} {index} {pi}\n')
    exe=P/'TEN_HOLE_FREE_REVIEW_check.exe'
    subprocess.run(['g++','-O3','-std=c++17',str(P/'TEN_HOLE_FREE_REVIEW_check.cpp'),'-o',str(exe)],check=True)
    subprocess.run([str(exe)],cwd=P,check=True)
    census=json.loads((P/'TEN_HOLE_FREE_REVIEW_census.json').read_text())
    assert census['remaining']==0
    # A second total-domain count reverses the two parity classes. Choose W
    # first, then count all allowed nonroot even quadruples combinatorially.
    reverse_counts={}
    for v in (7,31):
        total=0
        others=[x for x in range(64) if x.bit_count()%2 and x.bit_count()!=1 and x!=v]
        for four in it.combinations(others,4):
            w=(v,)+four
            n=sum(all((x^y).bit_count()!=1 for y in w) for x in range(1,64) if x.bit_count()%2==0)
            total+=math.comb(n,4)
        reverse_counts[v]=total
        assert total==next(r['eligible'] for r in census['targets'] if r['v']==v)
    # Replay all retained concrete witnesses independently in Python, including
    # actual bridge-source legality, projected marked roles and acceptance.
    checked=0;seen=set()
    with (P/'TEN_HOLE_FREE_REVIEW_witness.tsv').open() as f:
        for line in f:
            row=list(map(int,line.split()))
            v=row[0];z=row[1:5];w=row[5:10];d,s,t,kind,index,pi=row[10:]
            geometry=(v,tuple(sorted(z)),tuple(sorted(w)))
            assert geometry not in seen
            seen.add(geometry)
            assert v in w and len(set([0]+z+w))==10
            assert all(x.bit_count()%2==0 for x in z)
            assert all(x.bit_count()%2==1 for x in w)
            assert all((x^y).bit_count()!=1 for x in [0]+z for y in w)
            side=lambda x: ((x^v)>>d)&1==0
            za=[x for x in z if side(x)];wa=[x for x in w if side(x)]
            zb=[x for x in z if not side(x)];wb=[x for x in w if not side(x)]
            if (len(za),len(wa))==(3,2):
                assert s in za and t in za and s!=t
                minority=zb[0];included=wb
            else:
                assert (len(za),len(wa))==(1,4)
                assert s in wa and t in wa and s!=t and v not in (s,t)
                assert (1<<d) not in (s,t)
                minority=wb[0];included=zb
            delete=lambda x:(x&((1<<d)-1))|((x>>(d+1))<<d)
            om=tuple(sorted(delete((x^(1<<d))^minority) for x in (s,t)))
            inc=tuple(sorted(delete(x^minority) for x in included))
            assert allowed[key(om,inc)]==(('core' if kind==0 else 'split'),index,pi)
            if kind==0:
                r=reps[index];p=permutations[pi]
                image=lambda x:sum(((x>>j)&1)<<p[j] for j in range(5))
                assert om==tuple(sorted(map(image,r['avoided'])))
                assert inc==tuple(sorted(map(image,r['included'])))
            else:
                assert sum((x>>index)&1 for x in om+inc)==2
                assert ((om[0]^om[1])>>index)&1
            checked+=1
    assert checked==sum(x['T15'] for x in census['targets'])
    result={'status':'PASS','standalone':True,'producer_modules_or_census_read':False,
            'complete_core_ids':CORES,'core_orbit_images':core_image_count,
            'split_marked_geometries':split_count,'accepted_marked_geometries':len(allowed),
            'face_translation_projections_checked':projections,
            'reverse_parity_domain_counts':reverse_counts,
            'frozen_import_hashes_checked':len(manifest['hashes']),
            'witnesses_independently_replayed':checked,'census':census,
            'hashes':{n:digest(P/n) for n in ('TEN_HOLE_FREE_CLOSURE.md','t15_analytic_geometry.json',
              'TEN_HOLE_FREE_REVIEW_check.py','TEN_HOLE_FREE_REVIEW_check.cpp','TEN_HOLE_FREE_REVIEW_imports.json',
              'TEN_HOLE_FREE_REVIEW_lookup.txt','TEN_HOLE_FREE_REVIEW_census.json','TEN_HOLE_FREE_REVIEW_witness.tsv')}}
    (P/'TEN_HOLE_FREE_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
