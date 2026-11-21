"""Unbudgeted controlled AE, strict DRAT or complete original-model replay."""
import hashlib
import itertools as it
import json
import os
from pathlib import Path
import platform
import subprocess
import time

assert platform.system()=='Linux'
HERE=Path(__file__).resolve().parent
OUT=HERE/'h13-physical-all02'
ROOT=Path('<private-linux-workspace>')


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def save(result):
    temporary=OUT/'progress.tmp.json'
    temporary.write_text(json.dumps(result,indent=2))
    temporary.replace(OUT/'progress.json')


def original_replay(literals):
    structure=json.loads((OUT/'structure.json').read_text())
    prior=HERE/'h13-exact-wlog-third01'
    meta=json.loads((prior/'inputs/base-metadata.json').read_text())
    shapes=list(map(tuple,meta['universe']['column_heights']))
    cells=[{(x,y) for x in range(1,5) for y in range(1,s[x-1]+1)} for s in shapes]
    orders={tuple(pair):flag for pair,flag in structure['orders']}

    def before(a,b):
        if cells[a]<cells[b]:
            return True
        if cells[b]<cells[a]:
            return False
        return (orders[a,b] in literals) if a<b else (-orders[b,a] in literals)

    occupied=[a for a in range(70) if a+1 not in literals]
    physical=sorted(occupied,key=lambda a:sum(before(b,a) for b in occupied if b!=a))
    assert len(physical)==57 and all(before(a,b) for i,a in enumerate(physical) for b in physical[i+1:])
    colorvars={tuple(key):flag for key,flag in structure['colors']}
    chi={triple:int(colorvars[tuple(sorted(physical[i] for i in triple))] in literals) for triple in it.combinations(range(57),3)}
    valid={(0,0,0,0),(0,0,0,1),(0,0,1,1),(0,1,1,1),(1,1,1,1),(1,1,1,0),(1,1,0,0),(1,0,0,0)}
    path4=set()
    for a,t,u,v in it.combinations(range(57),4):
        assert tuple(chi[triple] for triple in ((a,t,u),(a,t,v),(a,u,v),(t,u,v))) in valid
        col=chi[a,t,u]
        if chi[t,u,v]==col:
            path4.add((a,u,v,col))
    path5=set()
    for a,t,u,col in path4:
        for v in range(u+1,57):
            if chi[t,u,v]==col:
                path5.add((a,v,col))
    assert all((a,b,1-col) not in path5 for a,b,col in path5)
    ranks={}
    computed=[(0,0,0,0)]
    for y in range(1,57):
        incoming=[]
        for x in range(y):
            rank=[1,1]
            for u in range(x):
                col=chi[u,x,y]
                rank[col]=max(rank[col],ranks[u,x][col]+1)
            assert max(rank)<=4
            ranks[x,y]=rank
            incoming.append(rank)
        computed.append(tuple(max((red for blue,red in incoming if blue>=coordinate),default=0) for coordinate in range(1,5)))
    assert computed==[shapes[a] for a in physical]
    labels={tuple(pair):{tuple(cell):flag for cell,flag in choices} for pair,choices in structure['labels']}
    for (x,y),rank in ranks.items():
        assert labels[physical[x],physical[y]][tuple(rank)] in literals
    record={'status':'PASS_ORIGINAL57_FULL_ORDER_PACKET_TRUE_RANK_P_AND_WEAK8',
            'physical_states':physical,'holes':[a for a in range(70) if a not in occupied],
            'chi_in_natural_order':{','.join(map(str,k)):'R' if v else 'B' for k,v in chi.items()},
            'packet_count':len(list(it.combinations(range(57),4))),
            'no_monochromatic_six':'actual rank recurrence max<=4',
            'no_same_end_five_five':True}
    (OUT/'original57.json').write_text(json.dumps(record,separators=(',',':')))
    return record


def main():
    manifest=json.loads((OUT/'manifest.json').read_text())
    audit=json.loads((OUT/'audit.json').read_text())
    calibration=json.loads((OUT/'calibration.json').read_text())
    assert audit['status'].startswith('PASS_PHYSICAL_FULL_')
    assert calibration['status']=='PASS_FULL_ORIGINAL36_PHYSICAL_CNF_EXCEPT_ONLY_H13_UPPER'
    cnf,proof=OUT/'formula.cnf',OUT/'proof.drat'
    assert sha(cnf)==manifest['cnf_sha256']==audit['cnf_sha256']==calibration['cnf_sha256']
    solver=ROOT/'AE_kissat2025_MAB/build/kissat'
    checker=ROOT/'cadical-sc2025/build/drat-trim'
    began=time.monotonic()
    result={'status':'RUNNING_FULL_PHYSICAL_SOLVER','driver_pid':os.getpid(),'started_unix':time.time(),
            'cnf_sha256':manifest['cnf_sha256'],'external_solve_deadline':None,'external_check_deadline':None,
            'solver_sha256':sha(solver),'checker_sha256':sha(checker),'source_sha256':sha(Path(__file__)),
            'checker_internal_limit_seconds':2147483647,'all13_holes_free':True,'external_review':'NONE'}
    command=[str(solver),str(cnf),str(proof)]
    with (OUT/'solver.log').open('w') as stream:
        process=subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
        result.update(process_pid=process.pid,process_pgid=os.getpgid(process.pid),command=command)
        save(result)
        code=process.wait()
    result.update(solver_returncode=code,solve_seconds=time.monotonic()-began)
    if code==20:
        result['status']='RUNNING_FULL_PHYSICAL_DRAT'
        command=[str(checker),str(cnf),str(proof),'-t','2147483647']
        with (OUT/'checker.log').open('w') as stream:
            process=subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
            result.update(process_pid=process.pid,process_pgid=os.getpgid(process.pid),command=command)
            save(result)
            checked=process.wait()
        markers=(OUT/'checker.log').read_text().count('s VERIFIED')
        result.update(checker_returncode=checked,verified_markers=markers,proof_sha256=sha(proof),proof_bytes=proof.stat().st_size)
        result['status']='CHECKED_UNSAT_H13_FULL_PHYSICAL_QUERY' if checked==0 and markers==1 else 'UNCHECKED_UNSAT'
    elif code==10:
        literals={int(token) for line in (OUT/'solver.log').read_text().splitlines() if line.startswith('v ') for token in line[2:].split() if int(token)}
        count=0
        with cnf.open() as source:
            for line in source:
                if line.startswith(('p','c')):
                    continue
                clause=list(map(int,line.split()))[:-1]
                assert any(literal in literals for literal in clause)
                count+=1
        assert count==manifest['clauses']
        (OUT/'assignment.json').write_text(json.dumps({'literals':sorted(literals)},separators=(',',':')))
        replay=original_replay(literals)
        result.update(status='SAT_ORIGINAL57_INDEPENDENT_PHYSICAL_REPLAY',checked_clauses=count,
                      original_replay_status=replay['status'],holes=replay['holes'])
    else:
        result['status']='UNKNOWN_OR_EXTERNAL_FAILURE'
    result['total_seconds']=time.monotonic()-began
    save(result)
    (OUT/'result.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
