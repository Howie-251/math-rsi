import json,os,subprocess,sys,time
from pathlib import Path
D=Path(__file__).resolve().parent;start=time.monotonic();rows=list(range(2,62));ticks=os.sysconf('SC_CLK_TCK')
def finite_cpu():
 vals=[]
 for p in list(D.glob('*_RESULT.json'))+list((D/'build_history').glob('*_RESULT.json')):
  try:r=json.loads(p.read_text())
  except Exception:continue
  if 'CPU_seconds' not in r:continue
  m=r.get('module','')
  if 'Input' in m or m in ['OppositeGQ35SpreadFastTables','OppositeGQ35SpreadIncidence']:vals.append(r['CPU_seconds'])
 return sum(vals)
state={'status':'RUNNING','driver_pid':os.getpid(),'workers':3,'expected_rows':rows,'per_module_max_CPU':115,'entire_finite_CPU_budget':750,'generic_budget':450,'finite_prior_CPU':finite_cpu(),'completed':[],'stop_conditions':['first module failure stops further dispatch','750 aggregate finite CPU including all previous attempts','no automatic restart']};todo=list(rows);active={};stop=False

def snapshot():
 running=[];cpu=0
 for i,entry in active.items():
  pid=None;h=D/f'OppositeGQ35SpreadInputRow{i:02}_HANDLE.json'
  if h.exists():
   x=json.loads(h.read_text());pid=x.get('pid') if x.get('status')=='RUNNING' else None
  if pid:
   try:
    a=Path(f'/proc/{pid}/stat').read_text().split();cpu+=(int(a[13])+int(a[14]))/ticks
   except FileNotFoundError:pass
  running.append({'row':i,'wrapper_pid':entry.pid,'compiler_pid':pid})
 state['active']=running;state['finite_completed_attempts_CPU']=finite_cpu();state['active_CPU']=cpu;state['elapsed_wall']=time.monotonic()-start
 (D/'INPUT_BATCH_HANDLE.json').write_text(json.dumps(state,indent=2)+'\n')
 return state['finite_completed_attempts_CPU']+cpu
while todo or active:
 while todo and len(active)<3 and not stop:
  i=todo.pop(0);m=f'OppositeGQ35SpreadInputRow{i:02}';p=D/f'{m}_RESULT.json'
  if p.exists() and json.loads(p.read_text()).get('exit_code')==0:
   state['completed'].append(i);continue
  log=(D/f'{m}_driver.log').open('w')
  active[i]=subprocess.Popen([sys.executable,str(D/'compile.py'),m,'115'],stdout=log,stderr=subprocess.STDOUT);log.close()
 for i,p in list(active.items()):
  if p.poll() is None:continue
  r=json.loads((D/f'OppositeGQ35SpreadInputRow{i:02}_RESULT.json').read_text())
  if r['exit_code']==0:state['completed'].append(i)
  else:state['failure']=r;stop=True;state['status']='STOP_MODULE_FAILURE'
  del active[i]
  if len(state['completed'])%10==0:print(json.dumps({'completed':len(state['completed']),'finite_CPU':finite_cpu()}),flush=True)
 total=snapshot()
 if total>=750 and not stop:
  stop=True;state['status']='STOP_AGGREGATE_FINITE_BUDGET'
  for x in state['active']:
   if x['compiler_pid']:os.kill(x['compiler_pid'],15)
 if stop and not active:break
 time.sleep(0.25)
if not stop:state['status']='COMPLETE_ALL60_REMAINING_ROWS'
state['unstarted_rows']=todo;state['finite_all_attempts_CPU']=finite_cpu();state['elapsed_wall']=time.monotonic()-start
(D/'INPUT_BATCH_RESULT.json').write_text(json.dumps(state,indent=2)+'\n');(D/'INPUT_BATCH_HANDLE.json').write_text(json.dumps(state,indent=2)+'\n');print(json.dumps(state),flush=True)
