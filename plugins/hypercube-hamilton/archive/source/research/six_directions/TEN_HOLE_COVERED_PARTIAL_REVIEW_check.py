"""Independent lookup preparation and final residual/witness audit.

Run `prepare`, compile/run the C++ checker, then run `finish`.
Never imports or executes a producer; its residuals are comparison targets only.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib,json,sys
R=Path(__file__).resolve().parent
IDS=(0,1,2,4,5,7,8,10,13,14,15,18,19,21,23,24,25,27,31,32,35,37,38,44)
def sha(n):return 'sha256:'+hashlib.sha256((R/n).read_bytes()).hexdigest()
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def mask(xs):return sum(1<<x for x in xs)
def swap(x,i):return x^(3<<i) if ((x>>i)^(x>>(i+1)))&1 else x
def orbit(seed):
    seen={seed};todo=[seed]
    while todo:
        a,b=todo.pop()
        for i in range(4):
            p=(tuple(sorted(swap(x,i) for x in a)),tuple(sorted(swap(x,i) for x in b)))
            if p not in seen:seen.add(p);todo.append(p)
    return seen
if sys.argv[1]=='prepare':
    fixed=load('TEN_HOLE_FREE_REVIEW_imports.json')
    for n,h in fixed['hashes'].items():assert sha(n)==h,('stale',n)
    accepted=set();core=set()
    for k in IDS:
        row=fixed['complete_core_registry'][str(k)]
        assert load(row['review'])['verdict']=='PASS'
        a=tuple(row['omitted']);b=tuple(x for x in row['holes'] if x!=0 and x not in a)
        assert len(a)==2 and len(b)==3 and all(x.bit_count()%2 for x in a+b)
        for om,inc in orbit((a,b)):core.add(mask(om)|(mask(inc)<<32))
    assert len(core)==1600;accepted|=core
    odd=[x for x in range(32) if x.bit_count()%2]
    split=set()
    for om in combinations(odd,2):
        for inc in combinations([x for x in odd if x not in om],3):
            for d in range(5):
                high=[x for x in om+inc if x&(1<<d)]
                if len(high)==2 and len(set(om)&set(high))==1:
                    split.add(mask(om)|(mask(inc)<<32));break
    accepted|=split
    (R/'TEN_HOLE_COVERED_PARTIAL_REVIEW_lookup.txt').write_text(''.join(str(k)+'\n' for k in sorted(accepted)))
    newdeps=['TEN_HOLE_COVERED_PARTIAL_A8_TRANSFER.md','HIGHER_HOLE_UNIFIED_TRANSFER.md',
             'HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_K8_CLOSURE.md','Q5_K8_REVIEW.json',
             'A8_PARTIAL_PROOF_PACKAGE.md','A8_PARTIAL_REVIEW.json',
             'A8_DELTA4_FIRST_ORBIT.md','A8_DELTA4_FIRST_ORBIT_REVIEW.json',
             'TEN_HOLE_FREE_REVIEW_imports.json','TEN_HOLE_FREE_REVIEW.json']
    source_bindings=0
    for n in newdeps:
        if n.endswith('_REVIEW.json'):
            report=load(n);assert report['verdict']=='PASS',n
            for source,h in report.get('audited_input_hashes',{}).items():
                if source in newdeps:
                    assert sha(source)==h,(n,'stale audited source',source)
                    source_bindings+=1
    out={'status':'PASS','core_ids':IDS,'core_images':len(core),'split_marked_geometries':len(split),
         'accepted_lookup_entries':len(accepted),'frozen_old_import_hashes_checked':len(fixed['hashes']),
         'direct_accepted_source_bindings_checked':source_bindings,
         'imported_dependency_hashes':{**fixed['hashes'],**{n:sha(n) for n in newdeps}}}
    (R/'TEN_HOLE_COVERED_PARTIAL_REVIEW_imports.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print({k:v for k,v in out.items() if k!='imported_dependency_hashes'})
elif sys.argv[1]=='finish':
    census=load('TEN_HOLE_COVERED_PARTIAL_REVIEW_census.json')
    imports=load('TEN_HOLE_COVERED_PARTIAL_REVIEW_imports.json')
    for n,h in imports['imported_dependency_hashes'].items():assert sha(n)==h,('changed during audit',n)
    assert sum(r['eligible'] for r in census['targets'])==145248180
    assert sum(r['after_old'] for r in census['targets'])==121690
    assert sum(r['newly_covered'] for r in census['targets'])==30465
    assert [r['remaining'] for r in census['targets']]==[26880,29955,34390]
    residuals=[]
    for rec in census['targets']:
        v=rec['v'];own=f'TEN_HOLE_COVERED_PARTIAL_REVIEW_remaining_v{v}.bin';prod=f'ten_covered_after_partial_a8_v{v}.bin'
        def records(n):
            b=(R/n).read_bytes();assert len(b)%9==0
            rows=[b[i:i+9] for i in range(0,len(b),9)]
            assert len(set(rows))==len(rows)
            return sorted(rows)
        a,b=records(own),records(prod);assert len(a)==rec['remaining'] and a==b
        residuals.append({'v':v,'count':len(a),'independent_file':own,'independent_sha256':sha(own),
                          'producer_comparison_file':prod,'producer_sha256':sha(prod),
                          'sorted_records_sha256':'sha256:'+hashlib.sha256(b''.join(a)).hexdigest(),'exact_sets_equal':True})
    seen=set();hist=Counter();a8types=Counter()
    for line in (R/'TEN_HOLE_COVERED_PARTIAL_REVIEW_witness.tsv').read_text().splitlines():
        row=list(map(int,line.split()));v=row[0];z=row[1:5];w=row[5:10];code,d,source,j,claimed=row[10:]
        geom=(v,tuple(z),tuple(w));assert geom not in seen;seen.add(geom)
        assert len(set([0]+z+w+[v]))==11 and all(not(x^y).bit_count()==1 for x in z for y in w)
        A=lambda x:(x>>d&1)==(v>>d&1)
        za=[x for x in z if A(x)];zb=[x for x in z if not A(x)]
        wa=[x for x in w if A(x)];wb=[x for x in w if not A(x)]
        assert (len(za),len(wa))=={1:(0,1),2:(1,1),3:(0,2),4:(3,4),5:(4,4),6:(3,5)}[code]
        if code==1:assert source==j==claimed==-1
        else:
            if code==2:
                assert source in za;y=source^(1<<d);L=zb;J=wb+[y]
            elif code==3:
                assert source in wa and source!=1<<d;y=source^(1<<d);L=wb;J=zb+[y]
            elif code==4:y=v;L=za;J=wa+[y]
            elif code==5:
                assert source in za;y=v;L=[x for x in za if x!=source];J=wa+[y]
            else:
                assert source in wa and source!=1<<d;y=v;L=za;J=[x for x in wa if x!=source]+[y]
            assert len(set(L))==3 and len(set(J))==5 and not set(L)&set(J) and y in J
            assert all((x^q).bit_count()!=1 for x in L for q in J if q!=y)
            assert j!=d and 0<=j<6
            nl=sum((x>>j&1)==(y>>j&1) for x in L);nj=sum((x>>j&1)==(y>>j&1) for x in J)
            assert nj-nl==claimed
            assert claimed in (1,2,3) or (nl,nj)==(1,5)
            a8types[claimed]+=1
        hist[(v,code)]+=1
    assert len(seen)==30465
    for rec in census['targets']:
        for code,n in rec['new_rule_counts'].items():assert hist[(rec['v'],int(code))]==n
    result={'status':'PASS','census':census,'lookup':{k:imports[k] for k in ['core_ids','core_images','split_marked_geometries','accepted_lookup_entries']},
            'new_witnesses_replayed':len(seen),'new_witness_A8_delta_counts':dict(sorted(a8types.items())),
            'direct_accepted_source_bindings_checked':imports['direct_accepted_source_bindings_checked'],
            'exact_residual_comparisons':residuals,'complete_ten_hole_proved':False,'full_P6_proved':False,
            'producer_modules_or_census_used_as_oracle':False,'matching_feasibility_filter_used':False,
            'imported_dependency_hashes':imports['imported_dependency_hashes'],
            'checker_artifact_hashes':{n:sha(n) for n in ['TEN_HOLE_COVERED_PARTIAL_REVIEW_check.py','TEN_HOLE_COVERED_PARTIAL_REVIEW_check.cpp','TEN_HOLE_COVERED_PARTIAL_REVIEW_lookup.txt','TEN_HOLE_COVERED_PARTIAL_REVIEW_imports.json','TEN_HOLE_COVERED_PARTIAL_REVIEW_census.json','TEN_HOLE_COVERED_PARTIAL_REVIEW_witness.tsv']}}
    (R/'TEN_HOLE_COVERED_PARTIAL_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['imported_dependency_hashes','checker_artifact_hashes']},indent=2))
