from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
def bound(ns,pos):
 e=SubsetEngine(21,len(pos),ns);e.inv={p:(0,0,[]) for p in e.inv}
 lock={k:1<<v for v,k in enumerate(pos)};left=0;value=0
 for k in range(1,22):p=lock.get(k,0);value+=e.value(k,left,p);left|=p
 return Fraction(value,e.D)
def main():
 old=json.loads((P.parent/'generic_quad_core_multiplicity_three_20261020/ACTUAL_A3_PARTITIONS.json').read_text())
 end=sorted({tuple(z['positions']) for z in old['cases']});assert len(end)==5
 menu=sorted(set([tuple(k for k in range(9,15) if k!=omit) for omit in range(9,15)]+end+[tuple(22-k for k in pos) for pos in end]));assert len(menu)==16
 source=json.loads((P.parent/'three_nonunit_direct_repair_20261020/TAIL_RESULT.json').read_text())
 rows=[];all_generic=[]
 for r in source['rows']:
  for z in r['generic_tail']:
   all_generic.append((tuple(r['traces']),tuple(z['attachments'])))
   if min(z['original_F_degrees'])<7:continue
   ns=Counter({31:1});ns.update(r['traces'])
   for v,a in enumerate(z['attachments']):ns[1<<v]+=a
   assert sum(ns.values())==35
   vals=[(bound(ns,pos),pos) for pos in menu];U,pos=min(vals)
   ts=r['traces'];BF=sum((t.bit_count()-1)*(5-t.bit_count()) for t in ts) if all(ts) else None
   DF=sum(z['original_F_degrees']);rmax=(175-DF-7*BF)//(16-BF) if BF is not None and BF<16 else None
   rows.append(dict(traces=ts,attachments=z['attachments'],degrees=z['original_F_degrees'],F_high_excess=z['F_high_excess'],F_degree_sum=DF,BF=BF,clean_degree_max=rmax,counts=dict(ns),positions=pos,bound=str(U),strict=U<1,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals]))
 assert len(all_generic)==119
 out=dict(status='COMPLETE_MIN7_FIVE_LOCK_DOMAIN',scope='Exactly complete119 generic q3 failure attachments, filtered only all five actual F degrees>=7; no high-excess or global role bound.',source_generic_keys=119,necessary_inputs=len(rows),menu=menu,strict=sum(z['strict'] for z in rows),nonstrict=[z for z in rows if not z['strict']],cases=rows,cpu_seconds=time.process_time()-st)
 (P/'FIVE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('cases','menu')})
if __name__=='__main__':main()
