"""Prepare spectra and check all pairwise optional-edge intersections."""
import json,sys,itertools,collections
from pathlib import Path
R=Path(__file__).resolve().parent
def pairings(vs):
    if not vs:yield [];return
    a=vs[0]
    for b in vs[1:]:
        for rest in pairings([v for v in vs if v not in (a,b)]):yield [[a,b],*rest]
def prepare():
    groups=json.loads((R/'t15_single_avoided_face_probe.json').read_text())['results']
    cases=[]
    for g in groups:
        stalls=g['levels'][0]['items']
        if not g['levels'][0]['unresolved']:continue
        h=next(z for z in g['allowed_targets'] if z not in g['free_targets'])
        for t in stalls:
            assert t['usable']==[h] and len(t['ports'])==1
            cases.append(dict(id=len(cases),orbit=g['orbit'],face='A',cyclic=0,
                support=65534,root=t['ports'][0],target=h,matching=t['matching']))
        holes={g['minority'],g['forbidden'],h,*g['free_targets']}
        for f in pairings(sorted(set(range(16))-holes)):
            cases.append(dict(id=len(cases),orbit=g['orbit'],face='B',cyclic=1,
                support=65535^(1<<g['forbidden'])^(1<<h),root=g['minority'],target=-1,matching=f))
    (R/'t15_single_crossing_spectrum_inputs.json').write_text(json.dumps(cases)+'\n')
    (R/'t15_single_crossing_spectrum_inputs.txt').write_text('\n'.join(' '.join(map(str,[c['id'],c['cyclic'],c['support'],c['root'],c['target'],len(c['matching']),*[v for e in c['matching'] for v in e]])) for c in cases)+'\n')
    print('prepared',len(cases))
def check():
    cases=json.loads((R/'t15_single_crossing_spectrum_inputs.json').read_text())
    results=json.loads((R/'t15_single_crossing_spectra.json').read_text())
    edges=[(a,b) for a in range(16) for b in range(a+1,16) if (a^b).bit_count()==1]
    eid={e:i for i,e in enumerate(edges)};groups=collections.defaultdict(lambda:collections.defaultdict(list))
    assert len(cases)==len(results)
    for c,r in zip(cases,results):
        assert c['id']==r['id'] and r['witnesses']
        F={tuple(sorted(e)) for e in c['matching']};mask=0
        for p in r['witnesses']:
            assert len(p)==len(set(p))==c['support'].bit_count()
            assert set(p)=={v for v in range(16) if c['support']>>v&1}
            assert p[0]==c['root']
            if not c['cyclic']:assert p[-1]==c['target']
            E={tuple(sorted((a,b))) for a,b in zip(p,p[1:]+(p[:1] if c['cyclic'] else []))}
            assert F<=E and all((a^b).bit_count()==1 for a,b in E-F)
            for e in E-F:mask|=1<<eid[e]
        assert mask==r['spectrum']
        groups[c['orbit']][c['face']].append((c,r))
    stats=[];failures=[]
    for orb,g in groups.items():
        hist=collections.Counter()
        for a,ra in g['A']:
            for b,rb in g['B']:
                intersection=ra['spectrum']&rb['spectrum'];hist[intersection.bit_count()]+=1
                if not intersection:failures.append([orb,a['id'],b['id']])
        stats.append(dict(orbit=orb,A=len(g['A']),B=len(g['B']),intersection_histogram=dict(hist)))
    out=dict(scope='ALL_C1_STALLED_PAIRS_FOR_FOUR_LISTED_T15_ORBITS',positive_witness_check='PASS',groups=stats,empty_intersections=failures,full_t15_proved=False)
    (R/'t15_single_crossing_spectra_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({**out,'empty_intersections_count':len(failures),'empty_intersections':failures[:5]},indent=2))
if __name__=='__main__':(prepare if len(sys.argv)>1 and sys.argv[1]=='prepare' else check)()
