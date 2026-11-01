from pathlib import Path
from itertools import product,combinations
from collections import Counter
from math import comb,ceil
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
domain=json.loads((P/'RESULT.json').read_text())['rows'][0]
tau=json.loads((P/'TAU_POOL_RESULT.json').read_text())['rows'][0]
ds=[7]*18+domain['high_degrees'];W=sum(comb(d,2) for d in ds);S6=sum(sorted(ds)[-6:]);pairs=[(0,1),(0,2),(1,2)]
def crosscap(cs):
 cp=dict(zip(pairs,cs));maxc=0;witness=None
 # Four distinct actual roles: low role -1 repeats<=18, three high identities0..2 unique.
 for roles in product((-1,0,1,2),repeat=4):
  hi=[r for r in roles if r>=0]
  if len(set(hi))<len(hi):continue
  deg=[7 if r<0 else domain['high_degrees'][r] for r in roles]
  caps=[]
  for a in range(2):
   row=[]
   for b in range(2,4):
    u,v=roles[a],roles[b]
    row.append(2 if u<0 and v<0 else (4 if max(u,v)==0 else 3) if min(u,v)<0 else cp[tuple(sorted((u,v)))])
   caps.append(row)
  # Exact two-by-two bipartite maximum flow via all16 cuts; each selected point
  # loses its outer G/J edge, leaving degree-1 middle capacity.
  cuts=[]
  for A in range(4):
   for B in range(4):
    cuts.append(sum(deg[i]-1 for i in range(2) if not A>>i&1)+sum(caps[i][j] for i in range(2) for j in range(2) if A>>i&1 and not B>>j&1)+sum(deg[j+2]-1 for j in range(2) if B>>j&1))
  z=min(cuts)
  if z>maxc:maxc=z;witness={'roles':roles,'degrees':deg,'pair_capacities':caps}
 return maxc,witness
profiles=[]
for z,t in zip(domain['domain'],tau['all_bounds']):
 assert z['pair_codegrees']==t['pair_codegrees'] and z['triple']==t['triple']
 cs=z['pair_codegrees'];trip=z['triple'];q=[]
 for mask in range(8):
  k=mask.bit_count();r=5-k;DF=7*r+sum(x for j,x in enumerate(domain['high_degrees']) if mask>>j&1)
  b=max(4,ceil((DF-39-comb(r,2))/k)) if k else 4
  if k==2:
   ij=tuple(j for j in range(3) if mask>>j&1);b=max(b,cs[pairs.index(ij)]-1)
  if k==3:b=max(b,sum(cs)-2*trip-1)
  q.append(b)
 E=ceil(sum(n*b for n,b in zip(z['high_trace_counts'],q))/2)
 c3,w=crosscap(cs)
 err=sum(max(0,c-4)*(min(domain['high_degrees'][i],domain['high_degrees'][j])-c) for (i,j),c in zip(pairs,cs))
 key=(E,t['tau_lower'],t['tau_upper'],c3,err,max(4,*cs))
 profiles.append({'pair_codegrees':cs,'triple':trip,'high_trace_counts':z['high_trace_counts'],'E_lower':E,'tau_lower':t['tau_lower'],'tau_upper':t['tau_upper'],'C3_coefficient':c3,'C3_witness':w,'C4_additive_error_baseline4':err,'maximum_lambda':max(4,*cs),'dedup_key':key})
groups={}
for z in profiles:groups.setdefault(tuple(z['dedup_key']),[]).append(z)
# One actual-domain profile with minimum marginal tau; do not multiply moment work by47.
selected=min(profiles,key=lambda z:(z['tau_lower'],z['E_lower'],z['triple']))
qv=[max(0,ceil((4*d-20)/3)) for d in ds];pvs=[comb(d,2)-q for d,q in zip(ds,qv)]
incs=[];price=[]
def B(d,t):
 a,b=divmod(2*t,d);return (d-b)*a*a+b*(a+1)*(a+1)
for d,p in zip(ds,pvs):
 incs.extend(B(d,t)-B(d,t-1) for t in range(1,p+1));price.extend([d]*p)
incs.sort();price.sort();bs=[0];ks=[0]
for x in incs:bs.append(bs[-1]+x)
for x in price:ks.append(ks[-1]+x)
def f(s):a,r=divmod(s,5);return (s*s-(5-r)*a*a-r*(a+1)**2)//2
Pcap={}
for n1 in range(397,min(525,len(incs))+1):
 q,r=divmod(2*n1,30)
 Pcap[n1]=min(q*f(30)+f(r),(900*q+r*r-bs[n1])//2)
count=0;remaining=[];maximum=-1;maxkey=None;n1max=min(525,595-selected['E_lower'],len(incs))
for tv in range(selected['tau_lower'],selected['tau_upper']+1):
 for n4 in range((140+tv)//6+1):
  for n3 in range((140+tv-6*n4)//3+1):
   n1=W-280-2*tv+3*n3+8*n4
   if not 397<=n1<=n1max:continue
   n2=140+tv-3*n3-6*n4;n0=735-W+tv-n3-3*n4
   if min(n0,n2)<0:continue
   count+=1
   caps=[33*n0,35*n1-ks[n1],(S6-6)//2*n2,selected['C3_coefficient']*n3,min(4*n4+selected['C4_additive_error_baseline4'],selected['maximum_lambda']*n4)]
   budget=Pcap[n1];value=6864*n1;allocation=[0]*5
   for weight,j in sorted(zip((36,120,330,792,1716),range(5)),reverse=True):
    use=min(budget,caps[j]);budget-=use;allocation[j]=use;value+=weight*use
   z={'tau':tv,'n':[n0,n1,n2,n3,n4],'P':Pcap[n1],'caps':caps,'allocation':allocation,'twice_L':value}
   if value>maximum:maximum=value;maxkey=z
   if value>=5445440:remaining.append(z)
 if time.process_time()-start>5:raise RuntimeError('five CPU cutoff before profile complete')
result={'status':'COMPLETE_ONE_PROFILE_COARSE_DIAGNOSTIC','scope':'First a18 spectrum13,18,18 only. All47 high trace inventories projected to safe caps and dedup; one minimum-tau actual necessary profile moment sweep. No claim all47 or all5 spectra closed. No probability layouts. Baseline4 C4 accounts all possible low/high lambda4; high-pair matching errors exact.','degrees':ds,'W':W,'S6':S6,'high_trace_profiles':len(profiles),'distinct_parameter_groups':len(groups),'groups':[{'key':k,'source_count':len(v)} for k,v in groups.items()],'selected_profile':selected,'vertex_singleton_capacities':pvs,'complete_moment_keys_in_selected_profile':count,'remaining_keys':len(remaining),'maximum_twice_L':maximum,'maximum_witness':maxkey,'first_remaining':remaining[:5],'all_remaining':remaining,'unscanned_profiles':len(profiles)-1,'cpu_seconds':time.process_time()-start}
(P/'COARSE_PILOT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:v for k,v in result.items() if k not in ['groups','all_remaining','degrees','vertex_singleton_capacities']})
