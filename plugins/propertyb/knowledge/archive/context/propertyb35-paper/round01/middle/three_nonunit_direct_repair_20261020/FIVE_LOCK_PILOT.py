from pathlib import Path
from collections import Counter
from fractions import Fraction
import sys,time,json
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
st=time.process_time();tails=json.loads((P/'TAIL_RESULT.json').read_text())
# Fixed small menu: central six-lock band of old five-top certificate, omit one slot;
# the five actual five-lock end profiles saved in old quad/A3, plus their reflections.
old=json.loads((P.parent/'generic_quad_core_multiplicity_three_20261020/ACTUAL_A3_PARTITIONS.json').read_text())
old_end=sorted({tuple(z['positions']) for z in old['cases']});assert len(old_end)==5
central=[tuple(x for x in range(9,15) if x!=omit) for omit in range(9,15)]
menu=sorted(set(central+old_end+[tuple(22-x for x in pos) for pos in old_end]));assert len(menu)==16
inputs=[((7,11,28),(6,6,6,6,7)),((7,25,30),(4,6,6,6,9))]
out=[]
for traces,a in inputs:
 source=next(r for r in tails['rows'] if tuple(r['traces'])==traces)
 assert any(tuple(z['attachments'])==a for z in source['A2_A3_local_necessary_tail'])
 ns=Counter({31:1});ns.update(traces)
 for v,n in enumerate(a):ns[1<<v]+=n
 assert sum(ns.values())==35
 degrees=[sum(n for m,n in ns.items() if m>>v&1) for v in range(5)]
 e=SubsetEngine(21,5,dict(ns));e.inv={p:(0,0,[]) for p in e.inv}
 layouts=[]
 for pos in menu:
  bypos={k:1<<v for v,k in enumerate(pos)};left=0;val=0;rows=[]
  for k in range(1,22):
   p=bypos.get(k,0);b=e.value(k,left,p);assert b is not None;val+=b;rows.append(b);left|=p
  bound=Fraction(val,e.D);layouts.append({'positions':pos,'bound':str(bound),'strict':bound<1})
 best=min(layouts,key=lambda z:Fraction(z['bound']))
 # Independent expanded35-index injection replay even for the best nonstrict menu profile.
 stubs=[frozenset(v+1 for v in range(5) if m>>v&1) for m,n in ns.items() for _ in range(n)]
 assert len(stubs)==35
 ir=independent_rows(21,tuple(best['positions']),stubs)
 replay=sum((min(r['A'],r['B'],r['C']) for r in ir),Fraction())
 assert replay==Fraction(best['bound'])
 bp={k:1<<v for v,k in enumerate(best['positions'])};left=0
 for k,irrow in enumerate(ir,1):
  pivot=bp.get(k,0);assert Fraction(e.value(k,left,pivot),e.D)==min(irrow['A'],irrow['B'],irrow['C']);left|=pivot
 out.append({'traces':traces,'attachments':a,'counts':dict(ns),'selected_degrees':degrees,'all_35_edge_trace_masks':[sum(1<<(v-1) for v in ty) for ty in stubs],'zero_quota':True,'all_layouts':layouts,'best':best,'independent_35_index_replay_bound':str(replay),'ordered_distinct_pairs':1190,'rows':[{'k':r['k'],'A':str(r['A']),'B':str(r['B']),'C':str(r['C']),'minimum':str(min(r['A'],r['B'],r['C']))} for r in ir]})
 print(traces,a,'degree',degrees,'best',best,flush=True)
 assert time.process_time()-st<20
res={'scope':'Only two prerequested actual83-tail witnesses; fixed16-position menu, zero pair quota; no subset-position solve, new arrangements, original-H search or implicit automorphism. Failed bound is not impossibility. Stopped after first two hard cases as instructed.','menu_source':{'central':'old a1_five_top_repair fixed slots9..14 with one deleted slot','end':'five exact saved generic_quad_core ACTUAL_A3_PARTITIONS position profiles, plus reflection'},'menu':menu,'cases':out,'strict_count':sum(z['best']['strict'] for z in out),'cpu_seconds':time.process_time()-st}
(P/'FIVE_LOCK_PILOT.json').write_text(json.dumps(res,indent=2)+'\n');print('CPU',res['cpu_seconds'])
