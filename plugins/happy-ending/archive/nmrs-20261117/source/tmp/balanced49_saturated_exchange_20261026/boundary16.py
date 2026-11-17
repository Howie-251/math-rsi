"""One exact 16-point frozen-label decision, bounded external AE solve."""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import os
import platform
import resource
import shutil
import subprocess
import time
from sat_semantic_check import check

HERE=Path(__file__).resolve().parent
SOLVER=Path('/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat')
NAMES=['p0','p1','p2','p3','u','h1','h2','h3','h4','h5','v','j1','j2','j3','j4','j5']
H=set(range(5,10))|set(range(11,16))
REQUIRED=[(0,1,2,3,4,10),(4,5,6,7,8,9),(10,11,12,13,14,15)]


def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()


def limits(seconds):
    def apply():
        resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
        os.sched_setaffinity(0,sorted(os.sched_getaffinity(0))[:2])
    return apply


def run(command,label,seconds):
    started=time.monotonic()
    with (HERE/(label+'.stdout')).open('x') as out,(HERE/(label+'.stderr')).open('x') as err:
        try:
            result=subprocess.run(command,stdout=out,stderr=err,timeout=seconds+5,preexec_fn=limits(seconds))
            status={'exit_code':result.returncode}
        except subprocess.TimeoutExpired:
            status={'status':'TIMEOUT'}
    return {'command':command,'seconds':time.monotonic()-started,**status,
            'stdout_sha256':sha(HERE/(label+'.stdout')),'stderr_sha256':sha(HERE/(label+'.stderr'))}


def build():
    triples=list(combinations(range(16),3))
    variable={t:i+1 for i,t in enumerate(triples)}
    ids={tuple(s):tuple(variable[t] for t in combinations(s,3))
         for k in range(3,8) for s in combinations(range(16),k)}
    counts=Counter()
    body=HERE/'boundary16.body'
    with body.open('x') as out:
        def clause(group,lits):
            values=set(lits)
            if any(-x in values for x in values):
                counts[group+'_tautologies_skipped']+=1
                return
            row=sorted(values,key=lambda x:(abs(x),x))
            out.write(' '.join(map(str,row))+' 0\n')
            counts[group]+=1
        for q in combinations(range(16),4):
            entries=tuple(variable[t] for t in combinations(q,3))
            for bits in product([False,True],repeat=4):
                if sum(x!=y for x,y in zip(bits,bits[1:]))>1:
                    clause('packet',[-v if bit else v for v,bit in zip(entries,bits)])
        for s in combinations(range(16),7):clause('no_R7',[-v for v in ids[s]])
        for s in combinations(range(16),6):
            clause('no_B6',ids[s])
            if s[0] in H:clause('no_H_origin_R6',[-v for v in ids[s]])
        for a,b in combinations(range(16),2):
            inside=range(a+1,b)
            for red_size in [4,5,6]:
                blue_size=9-red_size
                for ri in combinations(inside,red_size-2):
                    red=ids[(a,*ri,b)]
                    for bi in combinations(inside,blue_size-2):
                        blue=ids[(a,*bi,b)]
                        clause('no_weak7_R'+str(red_size)+'B'+str(blue_size),[-v for v in red]+list(blue))
        for s in REQUIRED:
            for v in ids[s]:clause('required_R6',[v])
    count=sum(v for k,v in counts.items() if not k.endswith('_tautologies_skipped'))
    cnf=HERE/'boundary16.cnf'
    with cnf.open('xb') as out,body.open('rb') as source:
        out.write(f'p cnf {len(triples)} {count}\n'.encode())
        shutil.copyfileobj(source,out)
    # body is retained as construction evidence; no predecessor files touched.
    metadata={'schema':'explicit_triples_frozen_boundary16_v1','variables':len(triples),
              'clauses':count,'groups':dict(counts),'names':NAMES,
              'frozen_H':sorted(H),'frozen_R':[i for i in range(16) if i not in H],
              'required_R6':[list(s) for s in REQUIRED],
              'triple_variables':[{'id':variable[t],'triple':list(t)} for t in triples],
              'semantics':'id true iff ordered triple red; no auxiliaries; fixed labels, no recanonicalization',
              'weak_binding':'All same-endpoint R4+B5,R5+B4,R6+B3 pairs, allowing shared interiors; R7/B6 exclude all remaining sum9 cases; packet makes consecutive paths equal cliques',
              'cnf_sha256':sha(cnf),'builder_sha256':sha(Path(__file__)),
              'independent_checker_sha256':sha(HERE/'sat_semantic_check.py')}
    (HERE/'boundary16_binding.json').write_text(json.dumps(metadata,indent=2))
    return metadata


def proofcheck(report):
    source=Path('/data/ktqiu_hdd/math_agent/cadical-sc2025/test/cnf/drat-trim.c')
    if not source.is_file():
        report['proof_check']={'status':'UNAVAILABLE','reason':'known checker source absent'}
        return
    copied=HERE/'drat-trim.c'
    shutil.copyfile(source,copied)
    binary=HERE/'drat-trim'
    compile_=run(['gcc','-O2',str(copied),'-o',str(binary)],'checker_compile',20)
    report['checker_compile']=compile_
    if compile_.get('exit_code')!=0:return
    report['checker_source_sha256']=sha(copied)
    report['checker_binary_sha256']=sha(binary)
    controls=[]
    for name,cnf,expected in [('valid','p cnf 1 2\n1 0\n-1 0\n',True),('invalid','p cnf 1 1\n1 0\n',False)]:
        c=HERE/('control_'+name+'.cnf');p=HERE/('control_'+name+'.drat')
        c.write_text(cnf);p.write_text('0\n')
        result=run([str(binary),str(c),str(p),'-t','10'],'control_'+name,15)
        stdout=(HERE/('control_'+name+'.stdout')).read_text()
        accepted=result.get('exit_code')==0 and stdout.count('s VERIFIED')==1
        result.update(expected_accept=expected,accepted=accepted)
        controls.append(result)
        if accepted!=expected:raise ValueError('checker control mismatch')
    report['checker_controls']=controls
    checked=run([str(binary),str(HERE/'boundary16.cnf'),str(HERE/'boundary16.drat'),'-t','120'],'proof_check',125)
    stdout=(HERE/'proof_check.stdout').read_text()
    checked['verified']=checked.get('exit_code')==0 and stdout.count('s VERIFIED')==1
    report['proof_check']=checked
    report['finite_unsat_checked']=checked['verified']


def main():
    assert platform.system()=='Linux'
    report={'scope':'One finite16point decision only; no full-capacity theorem or acceptance',
            'finite_unsat_checked':False,'finite_sat_audited':False}
    try:
        metadata=build()
        report['binding']=metadata
        report['solver_sha256']=sha(SOLVER)
        command=[str(SOLVER),'--time=180','--no-binary',str(HERE/'boundary16.cnf'),str(HERE/'boundary16.drat')]
        result=run(command,'solver',185)
        report['solver']=result
        report['proof_sha256']=sha(HERE/'boundary16.drat')
        stdout=(HERE/'solver.stdout').read_text()
        if result.get('exit_code')==10 and 's SATISFIABLE' in stdout:
            values={}
            for line in stdout.splitlines():
                if line.startswith('v '):
                    for x in map(int,line.split()[1:]):
                        if x:values[abs(x)]=x>0
            assert set(values)==set(range(1,metadata['variables']+1)), 'incomplete model'
            for line in (HERE/'boundary16.cnf').read_text().splitlines()[1:]:
                lits=list(map(int,line.split()))[:-1]
                assert any(values[abs(x)]==(x>0) for x in lits), 'CNF assignment rejected'
            colors={tuple(row['triple']):values[row['id']] for row in metadata['triple_variables']}
            audited=check(NAMES,colors,H,REQUIRED)
            (HERE/'sat_semantic_result.json').write_text(json.dumps(audited,indent=2))
            (HERE/'sat_complete_assignment.json').write_text(json.dumps({'names':NAMES,'triples':[{'points':[NAMES[v] for v in t],'red':c} for t,c in colors.items()]},indent=2))
            report['finite_sat_audited']=True
        elif result.get('exit_code')==20 and 's UNSATISFIABLE' in stdout:
            report['raw_status']='UNSAT'
            proofcheck(report)
        else:report['raw_status']='INCONCLUSIVE'
    except Exception as exc:
        report['error']={'type':type(exc).__name__,'detail':str(exc)}
    (HERE/'boundary16_result.json').write_text(json.dumps(report,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k!='binding'},indent=2),flush=True)


if __name__=='__main__':main()
