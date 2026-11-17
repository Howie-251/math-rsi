"""Bounded deterministic subset/transversal calibration on one retained model."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib
import json
import platform
import resource
import time

HERE=Path(__file__).resolve().parent


def main():
    assert platform.system()=='Linux'
    resource.setrlimit(resource.RLIMIT_CPU,(60,60))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    started=time.monotonic()
    original=json.loads((HERE/'sat_complete_assignment.json').read_text())
    diag=json.loads((HERE/'deterministic_diagnostics_result.json').read_text())['sat16']
    names=original['names'];idx={s:i for i,s in enumerate(names)}
    def mask(s):return sum(1<<idx[x] for x in s)
    def labels(m):return [s for i,s in enumerate(names) if m&(1<<i)]
    red=[(mask(p),p) for p in diag['R6']]
    blue=[(mask(p),p) for p in diag['B5']]
    bad=[('R6',m,p) for m,p in red]+[('B5',m,p) for m,p in blue]
    def obstacles(m):return [{'type':c,'path':p} for c,s,p in bad if s&m==s]
    h,r=mask(diag['canonical_H']),mask(diag['canonical_R'])
    min_t=diag['canonical_R_transversal']['all_minimum_transversals']
    assert len(min_t)==26 and all(len(t)==2 for t in min_t)
    maximum=-1;max_count=0;max_example=None
    for m in range(1<<len(names)):
        size=m.bit_count()
        if size<maximum:continue
        if any(s&m==s for _,s,_ in bad):continue
        if size>maximum:maximum=size;max_count=0;max_example=labels(m)
        max_count+=1
    counts=Counter();y_rows=[];example=None;safe_example=None
    for t_names in min_t:
        tmask=mask(t_names);ymask=r&~tmask
        assert ymask.bit_count()==9 and not obstacles(ymask)
        sat_rows=[]
        for hh in diag['canonical_H']:
            hp=1<<idx[hh]
            hobs=obstacles(ymask|hp)
            sat_rows.append({'h':hh,'unsafe':bool(hobs),'obstacle_count':len(hobs)})
            for tt in t_names:
                tp=1<<idx[tt]
                tobs=obstacles(ymask|tp)
                for yy in labels(ymask):
                    yp=1<<idx[yy]
                    swapped=(tmask&~tp)|yp
                    internal_red=[(m,p) for m,p in red if m&r==m]
                    private=all(m&swapped for m,_ in internal_red)
                    h_common=bool(hobs) and all(yy in z['path'] for z in hobs)
                    t_common=bool(tobs) and all(yy in z['path'] for z in tobs)
                    counts['all_h_t_y']+=1
                    if private:counts['private_minimum_swap']+=1
                    if h_common:counts['h_single_nonempty_all_hit_y']+=1
                    if private and h_common:
                        counts['private_and_h_single_common_blocker']+=1
                        joint=obstacles((ymask&~yp)|hp|tp)
                        counts['private_common_joint_unsafe' if joint else 'private_common_joint_safe']+=1
                        if t_common:
                            counts['both_singles_nonempty_common_y']+=1
                            counts['both_singles_common_joint_unsafe' if joint else 'both_singles_common_joint_safe']+=1
                            record={'T':t_names,'Y':labels(ymask),'h':hh,'t':tt,'y':yy,
                                    'T_minus_t_plus_y':labels(swapped),'is_minimum_transversal':private,
                                    'Y_plus_h_obstacles':hobs,'Y_plus_t_obstacles':tobs,
                                    'joint_set':labels((ymask&~yp)|hp|tp),'joint_obstacles':joint,
                                    'joint_unsafe':bool(joint)}
                            if joint and example is None:example=record
                            if not joint and safe_example is None:safe_example=record
        y_rows.append({'T':t_names,'Y':labels(ymask),'against_canonical_H':sat_rows,
                       'all_five_H_additions_unsafe':all(z['unsafe'] for z in sat_rows)})
    counts['Y_with_all_five_H_additions_unsafe']=sum(z['all_five_H_additions_unsafe'] for z in y_rows)
    T=mask(['h1','p0']);U=mask(['h5','v']);exchange=[]
    for replacement in ['h5','v']:
        changed=(T&~mask(['p0']))|mask([replacement])
        uncovered=[p for m,p in red if m&r==m and not(m&changed)]
        assert uncovered
        exchange.append({'replacement':replacement,'new_set':labels(changed),'unhit_internal_R6':uncovered})
    report={'scope':'Deterministic enumeration on retained SAT16 only; no new assignment search or capacity claim',
            'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'assignment_sha256':hashlib.sha256((HERE/'sat_complete_assignment.json').read_bytes()).hexdigest(),
            'seconds':time.monotonic()-started,'maximum_safe_subset_size':maximum,
            'maximum_safe_subset_count':max_count,'one_maximum_safe_subset':max_example,
            'counts':dict(counts),'all_26_minimum_T_and_Y':y_rows,
            'one_joint_obstacle_counterexample':example,'one_safe_exchange_example':safe_example,
            'nonmatroid':{'T':['h1','p0'],'U':['h5','v'],'removed':'p0','failed_exchanges':exchange}}
    with (HERE/'exchange_enumeration_result.json').open('x') as out:json.dump(report,out,indent=2)
    print(json.dumps({k:v for k,v in report.items() if k!='all_26_minimum_T_and_Y'},indent=2))


if __name__=='__main__':main()
