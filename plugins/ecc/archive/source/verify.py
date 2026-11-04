#!/usr/bin/env python3
"""Run finite/certificate checks or pinned Lean builds from a relocated package."""
from pathlib import Path
import argparse, json, os, shutil, subprocess, sys, time
if not __debug__:
    raise RuntimeError('Assertions are required; do not use Python -O.')
ROOT = Path(__file__).resolve().parent

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('mode', choices=['quick', 'certificates', 'lean'])
    ap.add_argument('--output-dir', type=Path)
    ap.add_argument('--get-cache', action='store_true')
    ap.add_argument('--dependency-cache', type=Path, help='Existing pinned Lake packages directory; used only by copied Lean projects')
    ap.add_argument('--cxx', default=os.environ.get('CXX', 'c++'))
    ap.add_argument('--cpu-seconds', type=float, default=600)
    ap.add_argument('--wall-seconds', type=float, default=900)
    args = ap.parse_args()
    if sys.version_info < (3, 10):
        ap.error('Python >= 3.10 is required.')
    if args.output_dir is None: ap.error('--output-dir is required for this mode')
    out = args.output_dir.resolve()
    if out == ROOT or ROOT in out.parents: ap.error('Put verification output outside the release folder')
    out.mkdir(parents=True, exist_ok=False)
    report = {'mode':args.mode, 'status':'RUNNING', 'commands':[],
              'full_coset_domains_rerun':False, 'scope':'No published classification is rerun.'}
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    env.pop('PYTHONOPTIMIZE', None)
    def run(name, cmd, cwd=ROOT):
        print(f'Running {name}', flush=True)
        start=time.monotonic()
        with (out/(name+'.log')).open('w') as log:
            p=subprocess.run(list(map(str,cmd)),cwd=cwd,env=env,stdout=log,stderr=subprocess.STDOUT)
        report['commands'].append({'name':name,'command':list(map(str,cmd)), 'exit_code':p.returncode,'wall_seconds':time.monotonic()-start,'log':name+'.log'})
        report['status']='FAIL' if p.returncode else 'RUNNING'
        (out/'RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
        if p.returncode: raise SystemExit(f'{name} failed; see {out/(name+".log")}')
    py=sys.executable; c=ROOT/'computation'; manifest=ROOT/'evidence/manifest.json'
    if args.mode in ['quick','certificates']:
        run('finite-data',[py,c/'check_data.py','--output',out/'finite-data.json'])
        run('catalogue',[py,c/'reproduce.py','catalogue','--output-dir',out/'catalogue'])
        run('saved-sets',[py,c/'check_saved_sets.py','--manifest',manifest,'--output',out/'saved-sets.json'])
        # This validates every full-scan input binding and prints 344 commands.
        run('full-scan-plan',[py,c/'reproduce.py','full-f','--all','--implementation','both','--cpu-seconds',args.cpu_seconds,'--output-dir',out/'unused-scan-output'])
        if args.mode == 'certificates':
            run('pair-replay',[py,c/'replay_all.py','--manifest',manifest,'--output-dir',out/'pair-replay','--cxx',args.cxx,'--cpu-seconds',args.cpu_seconds,'--wall-seconds',args.wall_seconds])
    else:
        lake=shutil.which('lake') or str(Path.home()/'.elan/bin/lake')
        for name, targets, audits in [('ecc43',['ECC.Main','ECC.Corollaries'],['Audit.lean','CorollariesAudit.lean']),('ecc42',['ECC42'],['Audit.lean'])]:
            project=out/'projects'/name
            shutil.copytree(ROOT/'formal'/name,project)
            if args.dependency_cache:
                cache=args.dependency_cache.resolve()
                lock=json.loads((project/'lake-manifest.json').read_text())
                # Refuse a cache at an unrelated revision.
                for pkg in lock['packages']:
                    repo=cache/pkg['name']
                    rev=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
                    if rev != pkg['rev']:raise RuntimeError(f'Wrong dependency revision: {pkg["name"]}')
                    if subprocess.check_output(['git','-C',str(repo),'status','--porcelain','--untracked-files=no'],text=True).strip():
                        raise RuntimeError(f'Modified dependency source: {pkg["name"]}')
                (project/'.lake').mkdir()
                (project/'.lake/packages').symlink_to(cache,target_is_directory=True)
            if args.get_cache:run(name+'-cache',[lake,'exe','cache','get'],project)
            run(name+'-build',[lake,'build',*targets],project)
            for audit in audits:run(name+'-'+audit.removesuffix('.lean'),[lake,'env','lean',audit],project)
        report['scope']='Fresh project builds and type/transitive-axiom audits; external theorem and computation arguments remain explicit.'
        report['dependency_cache_reused']=bool(args.dependency_cache)
    report['status']='PASS'
    (out/'RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='commands'},indent=2))

if __name__=='__main__': main()
