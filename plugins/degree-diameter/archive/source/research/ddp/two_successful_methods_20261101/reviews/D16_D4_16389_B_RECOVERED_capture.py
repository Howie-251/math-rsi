"""Read only an existing local conversation DB; never send or restart a call."""
import json,os,shutil,sqlite3,time
from datetime import datetime,timezone
from pathlib import Path
D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal').is_dir())
DB=Path('/root/.gemini/antigravity-cli/conversations/5da20cd4-ab3f-4327-9df5-8d0e80d7eee3.db')
CLI=R/'.aris/antigravity-state/prompt-dz3a1pp4/cli.log'
def vi(b,i):
 v=0;s=0
 while True:
  q=b[i];i+=1;v|=(q&127)<<s
  if q<128:return v,i
  s+=7

def fields(b):
 out=[];i=0
 while i<len(b):
  k,i=vi(b,i);f,w=k>>3,k&7
  if w==0:v,i=vi(b,i)
  elif w==2:n,i=vi(b,i);v=b[i:i+n];i+=n
  elif w in(1,5):n=8 if w==1 else 4;v=b[i:i+n];i+=n
  else:raise ValueError(w)
  out.append((f,w,v))
 return out

def nested(b,f):return [v for ff,w,v in fields(b)if ff==f and w==2]
def alive(pid):
 try:os.kill(pid,0);return True
 except ProcessLookupError:return False
started=time.monotonic();observations=[]
while True:
 c=sqlite3.connect('file:'+str(DB)+'?mode=ro',uri=True)
 rows=c.execute('select idx,step_type,status,step_payload from steps order by idx').fetchall();c.close()
 prompt_idx=None;prompt=''
 for idx,ty,st,b in rows:
  if ty==14:
   for p in nested(b,19):
    for t in nested(p,2):
     s=t.decode('utf-8')
     if 'New exact-scope D4 review' in s and '(16,4,16389,128835)' in s:prompt_idx=idx;prompt=s
 finals=[]
 if prompt_idx is not None:
  for idx,ty,st,b in rows:
   if idx>prompt_idx and ty==15 and st==3:
    for p in nested(b,20):
     for t in nested(p,1):
      s=t.decode('utf-8')
      if len(s)>500 and '16389' in s and '128835' in s:
       finals.append((idx,b,s,nested(p,8)))
 if CLI.exists():shutil.copyfile(CLI,D/'D16_D4_16389_B_LIVE_CLI_CAPTURE.log')
 obs=dict(UTC=datetime.now(timezone.utc).isoformat(),latest_idx=rows[-1][0],new_D4_user_prompt_idx=prompt_idx,original_agy_PID3400606_alive=alive(3400606),original_parent_PID3400580_alive=alive(3400580),matched_final_indices=[x[0]for x in finals])
 observations.append(obs)
 result=dict(status='RECOVERED_LOCAL_COMPLETE_FINAL_TEXT'if finals else'ORIGINAL_CALL_NEW_D4_PROMPT_OBSERVED_FINAL_NOT_YET_OBSERVED',
  transport='original exec872 handle lost; read-only local DB recovery, not a new tool result',
  toolraw_SUCCESS_claim=False,new_message_or_retry_sent=False,scope=[16,4,16389,128835],thread_id='5da20cd4-ab3f-4327-9df5-8d0e80d7eee3',database=str(DB),
  extraction='steps.step_payload nested field20.field1 only; field3 summaries excluded',observations=observations,elapsed_wall_seconds=time.monotonic()-started)
 if prompt:
  (D/'D16_D4_16389_B_RECOVERED_USER_PROMPT.txt').write_text(prompt)
 if finals:
  idx,b,s,f8=finals[-1]
  (D/'D16_D4_16389_B_RECOVERED_RESPONSE.txt').write_text(s)
  (D/'D16_D4_16389_B_RECOVERED_STEP_PAYLOAD.bin').write_bytes(b)
  result.update(final_step_idx=idx,complete_response_characters=len(s),complete_response_UTF8_bytes=len(s.encode()),field8_equal_to_field1=bool(f8)and all(t.decode()==s for t in f8),source_role='B original single exact-scope request; no root verdict inferred')
 (D/'D16_D4_16389_B_RECOVERED_STATUS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(obs),flush=True)
 if finals or time.monotonic()-started>=190:break
 time.sleep(25)
