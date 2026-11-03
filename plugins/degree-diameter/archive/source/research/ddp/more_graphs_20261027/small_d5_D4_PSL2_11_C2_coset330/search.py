import resource
resource.setrlimit(resource.RLIMIT_CPU,(18,18))
from pathlib import Path
from array import array
from collections import Counter
from itertools import combinations
import json,sys,time
out=Path(__file__).resolve().parent;start=time.process_time();old=out.parent/'small_d6_D3_PSL2_11_C5_coset132'
def save(name,obj):(out/name).write_text(json.dumps(obj,indent=2)+'\n')
data=json.loads((old/'INPUT_TABLES.json').read_text());table=array('H')
with (old/'group_table.u16le.bin').open('rb') as f:table.fromfile(f,660*660)
assert sys.byteorder=='little' and len(table)==660*660
T=lambda a,b:table[a*660+b]
I=data['identity_id'];t=data['t_id'];inv=data['inverse_ids'];H=[I,t]
assert t!=I and T(t,t)==I
N=[g for g in range(660) if T(g,t)==T(t,g)]
# New C2 cosets, preserving source table and matrix ids exactly.
assigned={};cosets=[];reps=[]
for x in [I]+[g for g in range(660) if g!=I]:
 if x in assigned:continue
 C=sorted({x,T(x,t)});assert len(C)==2 and not any(y in assigned for y in C)
 c=len(cosets);cosets.append(C);reps.append(x)
 for y in C:assigned[y]=c
assert len(cosets)==330 and assigned[I]==0 and len(assigned)==660

def double(g):return frozenset(T(h,T(g,k)) for h in H for k in H)
remain=set(range(660));ds=[]
while remain:
 D=double(min(remain));assert D<=remain;remain-=D;ds.append(D)
byset={D:i for i,D in enumerate(ds)};used=set();atoms=[]
for i,D in enumerate(ds):
 if i in used:continue
 Di=frozenset(inv[g] for g in D);j=byset[Di];used|={i,j}
 U=D|Di
 if U==frozenset(H):continue
 assert not U&set(H)
 atoms.append({'atom_id':len(atoms),'degree':len(U)//2,'doublecoset_indices':sorted({i,j}),'source_doublecoset_degrees':[len(ds[k])//2 for k in sorted({i,j})],'selfpaired':i==j,'group_ids':sorted(U),'representative_matrices':[data['matrices'][min(ds[k])] for k in sorted({i,j})]})
weights=Counter(a['degree'] for a in atoms)
input_binding={'reused_group_directory':str(old),'group_order':660,'identity_id':I,'H':H,'H_generator_t_id':t,'H_generator_matrix':data['matrices'][t],'normalizer_order':len(N),'normalizer_ids':N,'vertices':330,'cosets':cosets,'representatives':reps,'element_to_coset':[assigned[g] for g in range(660)],'doublecosets':[sorted(D) for D in ds],'doublecoset_size_histogram':dict(Counter(map(len,ds))),'inverse_atom_degree_histogram':dict(weights),'atoms':atoms,'group_reconstruction':0,'oldgroup_verification':0}
save('INPUT_BINDING.json',input_binding)
if len(N)!=12 or weights!=Counter({1:3,2:25,4:69}):
 r={'status':'ACTUAL_BINDING_MISMATCH_STOP','actual_normalizer_order':len(N),'actual_weights':dict(weights),'prediction':'NOT_TESTED','CPU_seconds':time.process_time()-start};save('WORKER_RESULT.json',r);print(json.dumps(r));sys.exit(0)
# Each invariant symmetric atom is stored once as actual adjacency bitsets.
AA=[]
for a in atoms:
 D=a['group_ids'];A=[]
 for x in reps:
  ns={assigned[T(x,d)] for d in D};assert len(ns)==a['degree'];A.append(sum(1<<v for v in ns))
 for u,mask in enumerate(A):
  assert not(mask>>u&1)
  ns=mask
  while ns:
   bit=ns&-ns;ns-=bit;assert A[bit.bit_length()-1]>>u&1
 # Bind representative independence for this new stabilizer, not old group algebra.
 assert all(sum(1<<v for v in {assigned[T(x,d)] for d in D})==A[c] for c,C in enumerate(cosets) for x in C)
 AA.append(A);a['root_neighbors']=[v for v in range(330) if A[0]>>v&1]
full=(1<<330)-1
assert sum(a['degree'] for a in atoms)==329
assert all((__import__('functools').reduce(int.__or__,(A[u] for A in AA),0))==(full^(1<<u)) for u in range(330))
save('ATOMS.json',{'atoms':atoms,'count':len(atoms),'degree_histogram':dict(weights),'all_neighbor_rows_partition_complete_graph':True,'representative_independence':'ALL660_GROUP_REPRESENTATIVES_PER_ATOM_MATCH'})
ones=[a['atom_id'] for a in atoms if a['degree']==1];twos=[a['atom_id'] for a in atoms if a['degree']==2];fours=[a['atom_id'] for a in atoms if a['degree']==4]
candidates=[]
for a in ones:
 for b,c in combinations(twos,2):candidates.append(('1+2+2',tuple(sorted((a,b,c)))))
for a in ones:
 for b in fours:candidates.append(('1+4',tuple(sorted((a,b)))))
for a in twos:candidates.append(('1+1+1+2',tuple(sorted(tuple(ones)+(a,)))))
assert len(candidates)==len({s for typ,s in candidates})==1132
save('CANDIDATE_INPUT.json',{'count':1132,'types':dict(Counter(t for t,s in candidates)),'candidate_atoms':[{'type':t,'atoms':s} for t,s in candidates]})

def closure(A):
 seen=1;stack=[0]
 while stack:
  u=stack.pop();new=A[u]&~seen
  seen|=new
  while new:
   bit=new&-new;new-=bit;stack.append(bit.bit_length()-1)
 return seen.bit_count()
def R4(A):
 seen=1;front=1;hist=[1]
 for depth in range(4):
  nxt=0
  while front:
   bit=front&-front;front-=bit;nxt|=A[bit.bit_length()-1]
  front=nxt&~seen;seen|=front;hist.append(front.bit_count())
 return seen,hist
stats=Counter();typed=Counter();hit=None
with (out/'CASES.jsonl').open('w') as f:
 for i,(typ,S) in enumerate(candidates):
  A=[0]*330
  for a in S:
   B=AA[a]
   for u in range(330):A[u]|=B[u]
  assert all(mask.bit_count()==5 and not(mask>>u&1) for u,mask in enumerate(A))
  reach=closure(A);stats['processed']+=1;typed[typ]+=1
  row={'case':i,'atom_ids':S,'type':typ,'n':330,'m':825,'degree':5,'simple':True,'connected':reach==330,'closure_size':reach,'R4_histogram':None,'R4_missing':None,'actual_global_D':None,'ordinary_bad_unordered_pairs':None}
  if reach!=330:row['status']='DISCONNECTED';stats['disconnected']+=1
  else:
   stats['connected']+=1;seen,hist=R4(A);stats['identity_R4_checks']+=1;missing=330-seen.bit_count();row.update({'R4_histogram':hist,'R4_missing':missing,'first_missing_coset':((full^seen)&-(full^seen)).bit_length()-1 if missing else None})
   if missing:row['status']='CONNECTED_R4_FAIL';stats['R4_failures']+=1
   else:
    row['status']='HIT_D4_PENDING_PARENT';row['actual_global_D']=4;hit=row;stats['hits']+=1
    edges=[(u,v) for u,mask in enumerate(A) for v in range(u+1,330) if mask>>v&1];assert len(edges)==825
    (out/'graph330.edges').write_text('330 825\n'+''.join(f'{u} {v}\n' for u,v in edges));save('HIT.json',row);save('PARAMETERS.json',{'G':'PSL2(F11)','H_generator':data['matrices'][t],'atoms':[atoms[a] for a in S],'vertex_definition':'xH, identityH has label0','input':'INPUT_BINDING.json','source_group_input':str(old/'INPUT_TABLES.json'),'source_group_table':str(old/'group_table.u16le.bin')})
  f.write(json.dumps(row)+'\n')
  if i%32==0 or hit:f.flush();save('checkpoint.json',{'status':'HIT' if hit else 'RUNNING','processed':stats['processed'],'total':1132,'stats':dict(stats),'CPU_seconds':time.process_time()-start})
  if hit:break
r={'status':'HIT_STOP_REMAINDER_UNTESTED' if hit else 'COMPLETE_ALL1132_NO_HIT','prediction':'SUPPORTED_PENDING_PARENT' if hit else 'REFUTED_COMPLETE_FIXED_ACTION','target_Delta':5,'target_D':4,'savedL':252,'n':330,'m':825,'group_order':660,'H_order':2,'normalizer_order':len(N),'inverse_atom_degree_histogram':dict(weights),'total_cases':1132,'processed':stats['processed'],'untested':1132-stats['processed'],'processed_by_type':dict(typed),'stats':dict(stats),'hits':int(hit is not None),'actual_global_D':4 if hit else None,'ordinary_bad_unordered_pairs':None,'CPU_seconds':time.process_time()-start,'group_reconstruction':0,'source_BFS':0,'allroot_BFS':0,'extra_groups_or_subgroups':0}
save('WORKER_RESULT.json',r);save('checkpoint.json',{'status':r['status'],'processed':stats['processed'],'untested':r['untested'],'stats':dict(stats)});print(json.dumps(r),flush=True)
