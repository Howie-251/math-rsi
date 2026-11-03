from pathlib import Path
import array,json,time
D=Path(__file__).resolve().parent;start=time.process_time();s=json.loads((D/'FROZEN_SIGMA.json').read_text())['sigma'];B=array.array('I');B.frombytes((D.parent/'BASE_COVER_MASKS.u32').read_bytes());assert len(s)==36 and len(set(s))==36 and len(B)==36**4
clauses=0;lits=0;coverlits=0;empty=0;minlen=10**9;maxlen=0
with (D/'FIXED_SIGMA_SHIFT.cnf').open('w') as out:
 out.write('p cnf 1332 26586\n')
 def emit(v):
  global clauses,lits
  out.write(' '.join(map(str,v))+' 0\n');clauses+=1;lits+=len(v)
 for i in range(36):
  for j in range(36):
   masks=[B[((i*36+j)*36+r)*36+s[r]] for r in range(36)]
   count=sum(m.bit_count() for m in masks);minlen=min(minlen,count);maxlen=max(maxlen,count)
   for k in range(19):
    line=[]
    for r,m in enumerate(masks):
     while m:
      bit=m&-m;m-=bit;q=bit.bit_length()-1;line.append(1+r*19+(k-q)%19)
    assert len(line)==count
    if not line:empty+=1
    emit(line);coverlits+=len(line)
 for r in range(36):
  v=[r*19+t+1 for t in range(19)];emit(v);base=685+r*18
  for i in range(18):emit([-v[i],base+i])
  for i in range(1,18):emit([-(base+i-1),base+i]);emit([-v[i],-(base+i-1)])
  emit([-v[18],-(base+17)])
 for t in range(1,19):emit([-1-t])
assert clauses==26586 and empty==0 and minlen>=19
(D/'SHIFT_MODEL_RESULT.json').write_text(json.dumps({'status':'COMPLETE_FIXED_SIGMA_EXACT_SHIFT_POINT_CNF','original_shift_variables':684,'aux_variables':648,'total_variables':1332,'clauses':clauses,'point_clauses':24624,'ALO':36,'AMO':1908,'gauge_units':18,'point_literals':coverlits,'all_literals':lits,'point_length_min':minlen,'point_length_max':maxlen,'empty_point_clauses':empty,'CNF_bytes':(D/'FIXED_SIGMA_SHIFT.cnf').stat().st_size,'actual_build_CPU':time.process_time()-start,'sigma':s,'all_targets_preserved':True,'old_DP_source_BFS_runs':0},indent=2)+'\n')
