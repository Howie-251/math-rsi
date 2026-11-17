"""Diagnostics of the retained SAT witness and one supplied seven-point fixture."""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import platform
import resource
import time
from finite_fixtures import analyze

HERE=Path(__file__).resolve().parent


def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()


def transversal(universe, paths):
    universe=set(universe)
    relevant=[set(p) for p in paths if set(p)<=universe]
    for size in range(len(universe)+1):
        answers=[list(s) for s in combinations(sorted(universe),size)
                 if all(set(s)&p for p in relevant)]
        if answers:return {'tau':size,'all_minimum_transversals':answers,'internal_R6_count':len(relevant)}


def main():
    assert platform.system()=='Linux'
    resource.setrlimit(resource.RLIMIT_CPU,(60,60))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    start=time.monotonic()
    raw=json.loads((HERE/'sat_complete_assignment.json').read_text())
    names=raw['names']; index={name:i for i,name in enumerate(names)}
    colors={tuple(index[x] for x in row['points']):'R' if row['red'] else 'B' for row in raw['triples']}
    data=analyze(names,colors)
    frozen_r=['p0','p1','p2','p3','u','v']
    frozen_h=[x for x in names if x not in frozen_r]
    red6=data['R6']
    tails={s:[p for p in red6 if p[0]==s and set(p[1:])<=set(frozen_h)] for s in frozen_r}
    assert all(tails.values()),'missing frozen H-only tail'
    diagnostic={'retained_assignment_sha256':sha(HERE/'sat_complete_assignment.json'),
                'independent_original_check_sha256':sha(HERE/'sat_semantic_result.json'),
                'frozen_labels_primary':True,'frozen_H':frozen_h,'frozen_R':frozen_r,
                'p':data['p'],'Pplus':data['Pplus'],'Pminus':data['Pminus'],'G':data['G'],
                'canonical_H':data['H'],'canonical_R':data['R'],
                'R6':red6,'F':data['F'],'W':data['W'],
                'canonical_H_ambient_R6_sources':data['H_ambient_R6_sources'],
                'frozen_R_transversal':transversal(frozen_r,red6),
                'canonical_R_transversal':transversal(data['R'],red6),
                'all_six_frozen_sources_have_frozen_H_only_tail':True,
                'all_frozen_H_only_tails':tails,'B5':data['B5'],
                'frozen_H_max_red_path':max(len(p) for p in data['all_subset_paths']['R'] if set(p)<=set(frozen_h)),
                'canonical_H_max_red_path':max(len(p) for p in data['all_subset_paths']['R'] if set(p)<=set(data['H']))}
    blocker_names=['a1','a2','a3','a4','y','h1','h2']
    blocker=analyze(blocker_names,{t:'B' if t==(4,5,6) else 'R' for t in combinations(range(7),3)})
    y=set(blocker_names[:5])
    r6=[set(p) for p in blocker['R6']]
    checks={'Y_plus_h1_is_R6':y|{'h1'} in r6,
            'Y_plus_h2_is_R6':y|{'h2'} in r6,
            'deleting_y_kills_separate_h1_R6':not any(p<=((y-{'y'})|{'h1'}) for p in r6),
            'deleting_y_kills_separate_h2_R6':not any(p<=((y-{'y'})|{'h2'}) for p in r6),
            'Y_minus_y_plus_both_is_R6':(y-{'y'})|{'h1','h2'} in r6}
    assert all(checks.values())
    blocker['joint_blocker_checks']=checks
    report={'scope':'Deterministic diagnostics only; no new SAT search, expansion or acceptance',
            'status':'PASS','source_sha256':sha(Path(__file__)),
            'analyzer_source_sha256':sha(HERE/'finite_fixtures.py'),
            'seconds':time.monotonic()-start,'sat16':diagnostic,'blocker7':blocker}
    with (HERE/'deterministic_diagnostics_result.json').open('x') as out:json.dump(report,out,indent=2)
    print(json.dumps({'status':'PASS','seconds':report['seconds'],'sat16':diagnostic,
                      'blocker7':{'max_R':blocker['max_R'],'max_B':blocker['max_B'],
                                  'max_endpoint_sum':blocker['max_endpoint_sum'],'checks':checks}},indent=2))


if __name__=='__main__':main()
