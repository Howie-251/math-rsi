import subprocess,time,os,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
p=Path(sys.argv[1]).resolve(); tag=sys.argv[2]
env=os.environ.copy();env['ELAN_HOME']=str(ROOT/'.tools/elan');env['PATH']=env['ELAN_HOME']+'/bin:'+env['PATH']
start=time.monotonic();maxrss=0;reason=None
with (HERE/(tag+'.log')).open('w')as log:
 proc=subprocess.Popen(['lake','env','lean',str(p)],cwd=ROOT/'formal',env=env,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
 while proc.poll()is None:
  time.sleep(.2)
  state=subprocess.run(['ps','-axo','pid=,ppid=,rss='],capture_output=True,text=True).stdout
  rows=[tuple(map(int,l.split()))for l in state.splitlines()if len(l.split())==3]
  children={proc.pid}
  for _ in range(5):children|={pid for pid,ppid,rss in rows if ppid in children}
  rss=max([rss for pid,ppid,rss in rows if pid in children]or[0]);maxrss=max(maxrss,rss)
  if time.monotonic()-start>20:reason='20sec_limit'
  if rss>4*1024*1024:reason='4GiB_limit'
  if reason:
   import signal
   os.killpg(proc.pid,signal.SIGTERM);proc.wait();break
result=dict(file=str(p),exit=proc.returncode,wall=time.monotonic()-start,max_single_rss_kib=maxrss,stopped=reason)
(HERE/(tag+'.json')).write_text(json.dumps(result,indent=2)+'\n');print(result);print((HERE/(tag+'.log')).read_text()[-3000:])
