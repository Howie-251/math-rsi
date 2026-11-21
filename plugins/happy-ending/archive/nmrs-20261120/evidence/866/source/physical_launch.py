"""One create-only scoped launch; never restarts or touches an old job."""
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

assert platform.system()=='Linux'
HERE=Path(__file__).resolve().parent
assert not (HERE/'physical-launch.json').exists()
assert not (HERE/'h13-physical-all02').exists()
with (HERE/'physical-preparation-driver.log').open('w') as stream:
    process=subprocess.Popen([sys.executable,'-B',str(HERE/'physical_prepare.py')],stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
record={'status':'STARTED_CONTROLLED_FULL_PHYSICAL_PIPELINE','preparation_pid':process.pid,'started_unix':time.time(),'external_deadline':None}
(HERE/'physical-launch.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record),flush=True)
