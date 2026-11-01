"""Independent exact IE for the saved fractional obstruction; no scipy."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, combinations
from math import comb,ceil
import json
P=Path(__file__).resolve().parent
L=[{0,1,2,6},{3,4,7,10},{5,8,11,12},{6,7,13,14},{8,9,15,16},{9,17,18,19}]
LM=[sum(1<<a for a in q) for q in L]
def completion(red,blue):
 if red&blue:return 0
 r=red.bit_count();f=20-r-blue.bit_count();k=10-r
 return comb(f,k) if 0<=k<=f else 0
def avoid(e,ec,colors):
 z=0
 for v in product((0,*colors),repeat=6):
  red=sum(1<<a for a in e) if ec==1 else 0
  blue=sum(1<<a for a in e) if ec==2 else 0
  sign=1
  for i,c in enumerate(v):
   if c:sign=-sign
   if c==1:red|=LM[i]
   if c==2:blue|=LM[i]
  z+=sign*completion(red,blue)
 return z
def count(e):return sum(avoid(e,c,(1,))+avoid(e,c,(2,))-avoid(e,c,(1,2)) for c in (1,2))
# Empty e must not double count its two artificial color orientations.
C=avoid([],0,(1,))+avoid([],0,(2,))-avoid([],0,(1,2));assert C==167174
j=json.loads((P/'LP.json').read_text());W=j['rational_witness'];z=[F(q['multiplicity']) for q in W]
assert len(W)==47 and sum(z)==29 and all(0<x<=1 for x in z)
deg=[7]*5+[6]+[6]*4+[8]*10
for a in range(20):assert sum(v for q,v in zip(W,z) if a in q['edge'])==deg[a]
for a,b in combinations(range(20),2):
 if not any({a,b}<=l for l in L):assert sum(v for q,v in zip(W,z) if a in q['edge'] and b in q['edge'])>=1
for q in W:assert count(q['edge'])==q['weight']
obj=sum(v*q['weight'] for q,v in zip(W,z));assert obj==172638>C
# Actual pair-event and Gram-rank arithmetic, not an H existence check.
joint=[506,22,132,572,2002]
assert sum(comb(d,2)*n for d,n in ((6,5),(7,5),(8,10)))==460
Q=ceil(F(116**2-21*464,42));assert Q==89
out={'status':'PASS','conditional_C_count':C,'exact_fractional_objective':str(obj),'excess_above_C':str(obj-C),'independently_IE_checked_weights':len(W),'exact_degree_paircover_simplecap_constraints':True,'source_lower_bound':2288,'star_clearing_target_lower_bound':ceil(F(4*2288,9)),'joint_mono_numerators_by_intersection':joint,'Gram_Q_lower_bound':Q,'Gram_d0_plus_d3_plus_3d4_lower_bound':18,'scope':'one fixed A1 link; fractional obstruction to this single-edge conditional-risk relaxation, not an H or signed unsatisfiable construction'}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
