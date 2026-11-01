import subprocess,time,json,os,signal,sys
from pathlib import Path
source=Path(sys.argv[1]);log=Path(sys.argv[2]);start=time.monotonic();peak=0;reason=None
with log.open('w') as f:
 p=subprocess.Popen(['lake','env','lean',str(source)],stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
 while p.poll() is None:
  lines=subprocess.check_output(['ps','-axo','pid,pgid,rss'],text=True).splitlines()[1:]
  rss=sum(int(row.split()[2])*1024 for row in lines if row.split()[1]==str(p.pid));peak=max(peak,rss)
  if time.monotonic()-start>20 or rss>4_000_000_000:
   reason='20sec_or_4GB';os.killpg(p.pid,signal.SIGTERM);p.wait();break
  time.sleep(.25)
r={'exit':p.returncode,'elapsed':time.monotonic()-start,'peak_group_rss':peak,'stop_reason':reason};print(json.dumps(r));log.with_suffix('.json').write_text(json.dumps(r,indent=2))
