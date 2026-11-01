from pathlib import Path
import subprocess,time,json,sys,os
ROOT=Path(__file__).resolve().parents[3]
OWNED=Path(__file__).resolve().parent
jobs=[('author',['python3','-B','development/propertyb-rebuild/forward-use/work/archive/context/propertyb-m7-131-20261029/check_candidate.py']),('independent',['python3','-B','development/propertyb-rebuild/forward-use/work/archive/context/propertyb-m7-131-20261029/independent/check.py'])]
records=[]
for name,argv in jobs:
    start=time.monotonic()
    result=subprocess.run(argv,cwd=ROOT,text=True,capture_output=True)
    (OWNED/(name+'.stdout.log')).write_text(result.stdout)
    (OWNED/(name+'.stderr.log')).write_text(result.stderr)
    records.append(dict(name=name,cwd='.',argv=argv,exit_code=result.returncode,wall_seconds=time.monotonic()-start))
    (OWNED/'COMMANDS.json').write_text(json.dumps(records,indent=2)+'\n')
    print(name,result.returncode,records[-1]['wall_seconds'],flush=True)
    if result.returncode:sys.exit(result.returncode)
