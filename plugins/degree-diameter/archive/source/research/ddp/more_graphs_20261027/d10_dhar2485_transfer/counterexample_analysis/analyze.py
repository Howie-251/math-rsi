"""Exact reduced-word linearforms for one source phase pattern and one controlled phase change."""
from pathlib import Path
import json,time,resource,sys
resource.setrlimit(resource.RLIMIT_CPU,(170,170));START=time.process_time();H=Path(__file__).resolve().parent;ROOT=H.parents[4]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen

def save(name,obj):
 def txt(z):
  if isinstance(z,str):return[z]
  if isinstance(z,dict):return[t for v in z.values() for t in txt(v)]
  if isinstance(z,(list,tuple)):return[t for v in z for t in txt(v)]
  return[]
 assert not screen('\n'.join(txt(obj)));(H/name).write_text(json.dumps(obj,indent=2)+'\n')
assert not (H/'RESULT.json').exists(),'Finite controlled route analysis already completed'
save('PREDICTION.json',dict(status='FROZEN_BEFORE_NONFAITHFUL_FORM_COUNTS',original_phases=[1,3,6,7,9],controlled_phases=[1,3,6,8,9],
 P1='The actionkernel commuting block identities may force a universal freevoltage capacity below101 for order5 and below113 for order7.',
 P2='Changing onlyDphase7to8 will split the named kernelcommutation collision and increase the minimum universal phaseform capacity for both order5 andorder7.',
 named_order5_words=['C a D B','D B C a'],named_order7_words=['D A C','A C D'],
 scope='Free translations, sameC35quotient, diameter4, one controlled D7to8 phase change. No fixedpoly endpoint search,127case, graph generation or BFS.'))
# Monic cyclotomicpolynomials needed for the exact universal action orders.
def divmonic(a,b):
 a=a[:];out=[0]*max(1,len(a)-len(b)+1)
 while len(a)>=len(b):
  k=len(a)-len(b);c=a[-1];out[k]=c
  for j,v in enumerate(b):a[k+j]-=c*v
  while a and a[-1]==0:a.pop()
 assert not a;return out
phi={5:[1]*5,7:[1]*7};a=[0]*29
for j in [0,7,14,21,28]:a[j]=1
phi[35]=divmonic(a,[1]*5)

def monomials(d):
 f=phi[d];degree=len(f)-1;out=[]
 for e in range(d):
  v=[0]*max(d,degree+1);v[e]=1
  for k in range(len(v)-1,degree-1,-1):
   c=v[k]
   if c:
    for j,a in enumerate(f):v[k-degree+j]-=c*a
  out.append(tuple(v[:degree]))
 return out
words=[()];level=[()]
for depth in range(1,5):
 new=[]
 for w in level:
  for i in range(5):
   for s in [1,-1]:
    if w and w[-1]==(i,-s):continue
    new.append(w+((i,s),))
 words.extend(new);level=new
assert len(words)==8201

def name(w):return ''.join(chr(65+i) if s==1 else chr(97+i) for i,s in w)

def forms(phases,d):
 mons=monomials(d);n=len(mons[0]);byphase=[{} for _ in range(35)];wordforms={};raw=[0]*35
 for w in words:
  coeff=[0]*(5*n);suffix=0
  for i,s in reversed(w):
   e=(suffix if s==1 else suffix-phases[i])%d
   for j,v in enumerate(mons[e]):coeff[i*n+j]+=s*v
   suffix+=s*phases[i]
  phase=suffix%35;key=tuple(coeff);byphase[phase].setdefault(key,[]).append(name(w));wordforms[name(w)]=(phase,key);raw[phase]+=1
 return byphase,wordforms,raw

patterns={'original':[1,3,6,7,9],'D7to8':[1,3,6,8,9]};profiles={};big={}
for label,phases in patterns.items():
 profiles[label]={};big[label]={}
 for d in [5,7,35]:
  ff,wf,raw=forms(phases,d);counts=[len(v) for v in ff];mn=min(counts);small=[i for i,c in enumerate(counts) if c==mn]
  example=[]
  for p in small:
   duplicates=sorted((v for v in ff[p].values() if len(v)>1),key=lambda v:(-len(v),v))
   example.append(dict(phase=p,largest_forced_overlap_words=duplicates[:4]))
  profiles[label][str(d)]=dict(action_order=d,universal_integer_form_capacity=counts,raw_reducedword_counts=raw,minimum=mn,tightphases=small,
   forced_overlap_wordcount=sum(raw)-sum(counts),tightphase_overlap_examples=example)
  big[label][d]=(ff,wf)

def evalkey(k,d,p,r):
 n=len(phi[d])-1;pows=[pow(r,j,p) for j in range(n)]
 return tuple(sum(k[i*n+j]*pows[j] for j in range(n))%p for i in range(5))
finite=[]
for p,d in [(101,5),(113,7)]:
 roots=[r for r in range(2,p) if pow(r,d,p)==1]
 assert len(roots)==d-1
 for label in patterns:
  ff,wf=big[label][d]
  for r in roots:
   counts=[len({evalkey(k,d,p,r) for k in f}) for f in ff];mn=min(counts)
   finite.append(dict(pattern=label,p=p,action_order=d,r=r,form_capacity=counts,minimum=mn,tightphases=[i for i,c in enumerate(counts) if c==mn],
      uniform_all_translation_obstruction=mn<p))
# Exact named collision before/after the only controlled phase change.
witness=[]
for d,left,right in [(5,'CaDB','DBCa'),(7,'DAC','ACD')]:
 for label in patterns:
  wf=big[label][d][1];p,k=wf[left];q,l=wf[right];assert p==q
  n=len(phi[d])-1
  diff=[[k[i*n+j]-l[i*n+j] for j in range(n)] for i in range(5)]
  witness.append(dict(action_order=d,pattern=label,words=[left,right],phase=p,equal_universal_forms=k==l,difference_by_generator=diff))

# Numeric form basis relation used for each action order is stored explicitly.
save('CYCLOTOMIC_FORMS.json',dict(polynomials={str(k):v for k,v in phi.items()},coefficient_order='Five generators A..E, each polynomial basis1,r,...,r^(phi(order)-1)',
 rule='Rightaction wordendpoint sum of signed generatorvoltage times r^(suffixphase), inverse contribution -r^(-generatorphase).'))
save('WITNESSES.json',dict(kernel_subgroup='For action orderd, all elements with phase divisiblebyd form an abelian subgroup.',witnesses=witness))
result=dict(status='COMPLETE_CONTROLLED_LINEAR_ROUTE_ANALYSIS',words=8201,quotient=35,degree=10,radius=4,profiles=profiles,finite_action_evaluations=finite,
 P1_order5_below101=profiles['original']['5']['minimum']<101,P1_order7_below113=profiles['original']['7']['minimum']<113,
 P2_minimum_increases_order5=profiles['D7to8']['5']['minimum']>profiles['original']['5']['minimum'],P2_minimum_increases_order7=profiles['D7to8']['7']['minimum']>profiles['original']['7']['minimum'],
 CPU_seconds=time.process_time()-START,old_BFS_repeated=False,adjacency_graph_generated=False,fixedpoly_endpoints_tested=False)
save('RESULT.json',result)
print('UNIVERSAL',json.dumps({label:{d:(v['minimum'],v['tightphases']) for d,v in table.items()} for label,table in profiles.items()}))
print('FINITE',json.dumps([{k:x[k] for k in ['pattern','p','r','minimum','tightphases','uniform_all_translation_obstruction']} for x in finite]))
print('CPU',result['CPU_seconds'])
