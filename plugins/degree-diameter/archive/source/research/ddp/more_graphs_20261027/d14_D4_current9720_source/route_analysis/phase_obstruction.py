from pathlib import Path
from collections import Counter
import itertools,json,time
P=Path(__file__).parent;start=time.process_time()
I=(1,0,0,1);minus=(2,0,0,2);a=(0,1,2,2);b=(0,1,2,1)
def inv(X):aa,bb,cc,dd=X;return (dd,-bb%3,-cc%3,aa)
def mul(X,Y):return tuple(sum(X[2*i+k]*Y[2*k+j] for k in range(2))%3 for i in range(2) for j in range(2))
xs=[a,inv(a),b,inv(b)];ph=[1,-1,2,-2];names=['a','A','b','B'];levels=[];wordcount=0
for length in range(5):
 c=Counter();words=[]
 for w in itertools.product(range(4),repeat=length):
  wordcount+=1;X=I;z=0
  for t in w:X=mul(X,xs[t]);z+=ph[t]
  if X==minus:c[z]+=1;words.append(''.join(names[t] for t in w))
 levels.append({'wide_length':length,'word_count':4**length,'minusI_endpoint_words':len(words),'minusI_integer_phase_histogram':dict(sorted(c.items())),'minusI_mod9_phases':sorted({x%9 for x in c}),'words':words})
assert all(r['minusI_endpoint_words']==0 for r in levels[:3])
assert set(levels[3]['minusI_mod9_phases'])==set(levels[4]['minusI_mod9_phases'])=={3,6}
phase3=set(levels[3]['minusI_mod9_phases']);phase4=set(levels[4]['minusI_mod9_phases']);variants=[]
for k in [2,3,4]:
 moves={-1,1,-k,k};reachable=phase3|phase4|{(z+s)%9 for z in phase3 for s in moves}
 missing=sorted(set(range(9))-reachable)
 assert missing
 variants.append({'extra_inverse_pair':k,'plain_steps':sorted(moves),'minusI_reachable_phases_in_at_most4':sorted(reachable),'minusI_missing_phases':missing,'D4_controller_obstruction':True})
r={'status':'FIXED_C9_ONE_EXTRA_PLAIN_PAIR_COMPLETE_CONTROLLER_OBSTRUCTION','wide_words_examined':wordcount,'length4_wide_words_examined':256,'levels':levels,'variants':variants,'derivation':'Since -I requires at least3 wide letters, a total<=4 word has either3 wideletters plus at mostone central plainstep, or4 wideletters and no plainstep. Central steps commute with wide controller labels. This lists every controller route, including inverse-letter cancellations.','new_graphs':0,'BFS':0,'ordinary_bad_unordered_pairs':None,'CPU_seconds':time.process_time()-start,'prediction':'SUPPORTED','scope':'G=SL2(3)xC9; fixeda=(Xa,1),b=(Xb,2), retainedp+/-1 and exactlyone additionalinversepairp+/-k. k2/3/4 exhaustdistinctnonzero pairs otherthan1. Not arbitraryC9 controllers or degree16D4 graphs.'}
(P/'PHASE_OBSTRUCTION_RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k!='levels'}));print('levels',[(x['wide_length'],x['minusI_integer_phase_histogram']) for x in levels])
