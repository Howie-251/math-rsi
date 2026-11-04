"""Whole-A8 geometry cover and fixed-import gate audit; no producer execution."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import hashlib,json,sys
R=Path(__file__).resolve().parent
def sha(n):
    h=hashlib.sha256()
    with (R/n).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return 'sha256:'+h.hexdigest()
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
E=[x for x in range(32) if x.bit_count()%2==0];O=[x for x in range(32) if x not in E]
N={x:{y for y in range(32) if (x^y).bit_count()==1} for x in range(32)}
representatives=[((3,5,6,15),(8,25,26)),((3,5,6,15),(25,26,28)),
                 ((3,5,15,23),(25,26,28)),((15,23,27,29),(1,2,4)),
                 ((15,23,27,29),(2,4,8))]
source_reports=[('A6_CLOSURE_DRAFT.md','A6_CLOSURE_REVIEW.json'),
                ('A8_PARTIAL_PROOF_PACKAGE.md','A8_PARTIAL_REVIEW.json'),
                ('A8_DELTA4_FIRST_ORBIT.md','A8_DELTA4_FIRST_ORBIT_REVIEW.json'),
                ('A8_ORBITS2_3_ANALYTIC_CLOSURE.md','A8_ORBITS2_3_REVIEW.json'),
                ('A8_ORBIT4_FULL_CLOSURE.md','A8_ORBIT4_FULL_REVIEW.json'),
                ('A8_ORBIT5_FULL_CLOSURE.md','A8_ORBIT5_FULL_REVIEW.json')]
images=[];marked={}
for k,(z,w) in enumerate(representatives,1):
    group=set()
    for p in permutations(range(5)):
        def image(x):return sum((1<<p[j]) for j in range(5) if x&(1<<j))
        geom=(tuple(sorted(map(image,z))),tuple(sorted(map(image,w))))
        group.add(geom)
        if geom in marked:assert marked[geom][0]==k
        else:marked[geom]=(k,p)
    assert len(group)==[60,20,30,30,20][k-1]
    assert all(group.isdisjoint(g) for g in images)
    images.append(group)
assert len(marked)==160
domain=set();good=set();residual=set();witness=[];counts=Counter()
for w in combinations(O,3):
    allowed=sorted(set(E)-{0}-set().union(*(N[x] for x in w)))
    for z in combinations(allowed,4):
        geom=(z,w);assert geom not in domain;domain.add(geom)
        major={0,*z};minor=set(w)
        cuts=[]
        for j in range(5):
            low={x for x in range(32) if x&(1<<j)==0}
            d=len(major&low)-len(minor&low)
            if d in (1,2,3):cuts.append((j,d))
        if cuts:
            assert geom not in marked;good.add(geom);j,d=cuts[0]
            witness.append([*z,*w,'cut',j,d]);counts['delta123']+=1
        else:
            assert geom in marked;residual.add(geom);k,p=marked[geom]
            witness.append([*z,*w,'orbit',k,*p]);counts['orbit'+str(k)]+=1
assert len(domain)==2700 and len(good)==2540 and residual==set(marked)
assert good.isdisjoint(residual) and good|residual==domain
old=load('A8_geometry_census.json')
assert old['total']==2700 and old['good']==2540 and old['residual']==160
for k,row in enumerate(old['residual_orbits']):
    assert row['size']==len(images[k])
    assert images[k]=={(tuple(x['Z']),tuple(x['W'])) for x in row['members']}
with (R/'Q5_A8_FULL_REVIEW_witness.tsv').open('w',encoding='ascii') as f:
    for row in sorted(witness,key=lambda row:row[:7]):f.write('\t'.join(map(str,row))+'\n')
geometry={'status':'PASS','domain':2700,'delta123':2540,'residual':160,
          'orbit_sizes':[len(g) for g in images],'partition_counts':dict(counts),
          'all_orbits_disjoint':True,'residual_union_exact':True,
          'root_minority_adjacency_excluded':False,'producer_executed_or_imported':False,
          'matching_instances_reenumerated':0,'whole_A8_gate':'NOT_EVALUATED'}
(R/'Q5_A8_FULL_REVIEW_geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
print(json.dumps(geometry,indent=2))
if '--final' in sys.argv:
    imported={};bindings=[]
    for source,report in source_reports:
        a=load(report)
        assert a['verdict']=='PASS',('final import gate not met',report,a['verdict'])
        expected=a['audited_input_hashes'][source].removeprefix('sha256:')
        assert sha(source).removeprefix('sha256:')==expected,('stale proof',source)
        imported[source]=sha(source);imported[report]=sha(report)
        report_md=report.replace('.json','.md');imported[report_md]=sha(report_md)
        bindings.append({'proof':source,'review':report,'verdict':'PASS','source_hash_bound':True})
    # Independently hash finite-domain/cycle files cited by the accepted last
    # two orbit reviews; do not redo their already accepted matching checks.
    evidence={}
    for report in ['A8_ORBIT4_FULL_REVIEW.json','A8_ORBIT5_FULL_REVIEW.json']:
        a=load(report)
        for n,h in a['audited_input_hashes'].items():
            assert sha(n).removeprefix('sha256:')==h.removeprefix('sha256:'),('stale orbit evidence',report,n)
            evidence[n]=sha(n)
    certificate='A8_orbit5_joint_bad_certificates.bin'
    assert (R/certificate).stat().st_size==150294375
    assert evidence[certificate]=='sha256:4faabf92ae61845e9a12b36a754998b03f14bf143e263999a6c6e731ac397f22'
    # The independent geometry source was accepted by the preceding partial
    # review; bind it too, without using its counts as our coverage oracle.
    partial=load('A8_PARTIAL_REVIEW.json')
    assert sha('A8_geometry_census.json')==partial['audited_input_hashes']['A8_geometry_census.json']
    imported['A8_geometry_census.json']=sha('A8_geometry_census.json')
    for source,_ in source_reports:
        text=(R/source).read_text(encoding='utf-8-sig')
        assert 'K8' not in text and 'Q5_A8_FULL_CLOSURE' not in text,('unexpected reverse dependency',source)
    out={'status':'PASS','audited_input_hashes':{'Q5_A8_FULL_CLOSURE.md':sha('Q5_A8_FULL_CLOSURE.md')},
         'imported_dependency_hashes':imported,'accepted_orbit_evidence_hashes':evidence,
         'import_bindings':bindings,'geometry':geometry,
         'checker_artifact_hashes':{n:sha(n) for n in ['Q5_A8_FULL_REVIEW_check.py','Q5_A8_FULL_REVIEW_geometry.json','Q5_A8_FULL_REVIEW_witness.tsv']},
         'all_import_gates_PASS':True,'K8_used_as_A8_import':False,
         'orbit5_positive_certificate_bytes':150294375,'orbit5_positive_certificate_records':2732625,
         'large_prior_matching_checks_rerun':False,'full_Q5_A8_proved_modulo_imports':True,
         'full_Q6_P6_proved':False}
    (R/'Q5_A8_FULL_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('FINAL IMPORT GATES PASS')
