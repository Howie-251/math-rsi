from pathlib import Path
from collections import defaultdict
import itertools,json,time
P=Path(__file__).parent;start=time.process_time()
I=(1,0,0,1);a=(0,1,2,2);b=(0,1,2,1)
def inv(X):aa,bb,cc,dd=X;return (dd,-bb%3,-cc%3,aa)
def mul(X,Y):return tuple(sum(X[2*i+k]*Y[2*k+j] for k in range(2))%3 for i in range(2) for j in range(2))
xs=[a,inv(a),b,inv(b)];phase=[1,-1,7,-7];names=['a','A','b','B'];S=[-4,-1,1,4]
plain=[{0}]
for _ in range(4):plain.append(plain[-1]|{(u+s)%10 for u in plain[-1] for s in S})
cover=defaultdict(set);words=0;witness={}
for length in range(5):
 for w in itertools.product(range(4),repeat=length):
  X=I;z=0
  for i in w:X=mul(X,xs[i]);z+=phase[i]
  for t in plain[4-length]:
   c=(z+t)%10;cover[X].add(c);witness.setdefault((X,c),{'wideword':''.join(names[i] for i in w),'wide_phase':z,'plain_residue':t,'plain_budget':4-length})
  words+=1
allX=[X for X in itertools.product(range(3),repeat=4) if (X[0]*X[3]-X[1]*X[2])%3==1]
missing=[{'SL2':list(X),'central':i} for X in allX for i in range(10) if i not in cover[X]]
res={'status':'SINGLE_M10_FRAME_COARSE_ALLOWED' if not missing else 'SINGLE_M10_FRAME_COARSE_REJECTED','A':1,'B':7,'plain_steps':S,'wide_words':words,'controller_states_reached':sum(map(len,cover.values())),'controller_order':240,'SL2_minimum_reached_central_phases':min(len(cover[X]) for X in allX),'missing_controller_slots':missing,'minusI_reached_phases':sorted(cover[(2,0,0,2)]),'prediction':'SUPPORTED' if not missing else 'REFUTED','proof_method':'For eachwideword lengthr<=4,appendany centralplainword oflength<=4-r. Plaincentrality makes these exactlyallcontrollerendpoints without graph construction or BFS.','CPU_seconds':time.process_time()-start,'actual_graphs':0,'BFS':0,'phase_frames_evaluated':1,'fiber_relation_evaluations':0,'actual_n':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,'scope':'Onlythissingleframe; fullcontrollercoverageisnecessarynot sufficientforthe19440-point fiberlift. NootherA/B/pair/modulus checked.'}
(P/'ANALYSIS_RESULT.json').write_text(json.dumps(res,indent=2)+'\n')
(P/'CONTROLLER_WORD_CERTIFICATE.json').write_text(json.dumps({'A':1,'B':7,'plain_steps':S,'plain_residue_sets_upto_lengths':[sorted(t) for t in plain],'slots':[{'SL2':list(X),'central':i,**witness[X,i]} for X in allX for i in range(10) if (X,i) in witness]},indent=2)+'\n')
print(json.dumps(res))
