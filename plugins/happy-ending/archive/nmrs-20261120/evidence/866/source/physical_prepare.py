"""Controlled no-deadline preparation then the one full-domain solver driver."""
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

assert platform.system()=='Linux'
HERE=Path(__file__).resolve().parent
record={'status':'PREPARING_FULL_PHYSICAL_H13','pid':os.getpid(),'started_unix':time.time(),'steps':[],'external_deadline':None}


def save():
    path=HERE/'physical-preparation.tmp.json'
    path.write_text(json.dumps(record,indent=2))
    path.replace(HERE/'physical-preparation.json')


for name in ['physical_build.py','physical_calibrate.py','physical_audit.py','physical_run.py']:
    log=HERE/(name.replace('.py','.log'))
    assert not log.exists()
    with log.open('w') as stream:
        process=subprocess.Popen([sys.executable,'-B',str(HERE/name)],stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
        step={'script':name,'pid':process.pid,'started_unix':time.time()}
        record['steps'].append(step)
        save()
        code=process.wait()
    step.update(returncode=code,finished_unix=time.time())
    if code!=0:
        record['status']='STOPPED_AT_FAILED_PREPARATION_OR_DRIVER'
        save()
        raise SystemExit(code)
    save()
record['status']='FULL_PHYSICAL_DRIVER_FINISHED'
record['finished_unix']=time.time()
save()
