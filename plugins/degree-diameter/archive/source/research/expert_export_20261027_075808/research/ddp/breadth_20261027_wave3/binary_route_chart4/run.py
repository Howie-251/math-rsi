from pathlib import Path
import subprocess, resource, json, time
P=Path(__file__).resolve().parent
t=time.process_time();w=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
subprocess.run(['g++','-O3','-std=c++17',str(P/'search.cpp'),'-o',str(P/'search')],check=True)
r1=resource.getrusage(resource.RUSAGE_CHILDREN)
def limit(): resource.setrlimit(resource.RLIMIT_CPU,(55,55))
with (P/'search_result.json').open('w') as out:subprocess.run([str(P/'search')],stdout=out,check=True,preexec_fn=limit)
r2=resource.getrusage(resource.RUSAGE_CHILDREN)
d=json.loads((P/'search_result.json').read_text())
d.update(compile_CPU_seconds=r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime,search_process_CPU_seconds=r2.ru_utime+r2.ru_stime-r1.ru_utime-r1.ru_stime,python_CPU_seconds=time.process_time()-t,wall_seconds=time.monotonic()-w,worker_count=1,search_process_CPU_hard_limit=55,internal_stop_CPU_seconds=54,requested_total_CPU_budget_seconds=60,controller_generated=False,large_lift_generated=False)
d['total_CPU_seconds']=d['compile_CPU_seconds']+d['search_process_CPU_seconds']+d['python_CPU_seconds']
if d['status']=='FOUND_UNIVERSAL_BINARY_LENGTH4_CHART':
 def mul(cols,x):
  out=0
  for j,c in enumerate(cols):
   if x>>j&1:out^=c
  return out
 def inverse(cols):
  im={mul(cols,x):x for x in range(16)}
  assert len(im)==16
  return [im[1<<j] for j in range(4)]
 def rank(cs):
  piv={}
  for v in cs:
   while v:
    j=v.bit_length()-1
    if j in piv:v^=piv[j]
    else:piv[j]=v;break
  return len(piv)
 mats=[d['A_a_columns'],inverse(d['A_a_columns']),d['A_b_columns'],inverse(d['A_b_columns'])]
 bs=[1,mul(mats[1],1),d['b_b'],mul(mats[3],d['b_b'])]
 inv=[1,0,3,2];cert=[]
 for a in range(4):
  for b in range(4):
   if b==inv[a]:continue
   for c in range(4):
    if c==inv[b]:continue
    for e in range(4):
     if e==inv[c]:continue
     word=[a,b,c,e];cols=[]
     for j in range(4):
      v=bs[word[j]]
      for k in range(j+1,4):v=mul(mats[word[k]],v)
      cols.append(v)
     rr=rank(cols);assert rr==4;cert.append(dict(word=word,columns=cols,rank=rr))
 for i in range(4):
  assert all(mul(mats[inv[i]],mul(mats[i],1<<j))==1<<j for j in range(4))
  assert mul(mats[inv[i]],bs[i])==bs[inv[i]]
 chart=dict(field=2,dimension=4,length=4,symbols=['a','a_inverse','b','b_inverse'],inverse=inv,matrix_columns=mats,matrix_rows=[[[col>>i&1 for col in cols] for i in range(4)] for cols in mats],b_codes=bs,b_vectors=[[x>>i&1 for i in range(4)] for x in bs],python_independent_word_check=cert,inverse_identities_verified=True)
 (P/'chart.json').write_text(json.dumps(chart,indent=2)+'\n')
 d['independent_python_check']='all108word_rank4_and_inverse_identities'
(P/'terminal.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({k:v for k,v in d.items() if k!='first_bad_word_counts'}))
