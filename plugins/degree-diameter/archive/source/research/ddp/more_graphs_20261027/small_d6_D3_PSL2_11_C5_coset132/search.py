import resource
resource.setrlimit(resource.RLIMIT_CPU,(18,18))
from pathlib import Path
from collections import Counter,deque
from array import array
import json,time,sys
out=Path(__file__).resolve().parent;start=time.process_time();p=11

def save(name,obj):(out/name).write_text(json.dumps(obj,indent=2)+'\n')
def canonical(m):return min(m,tuple((-v)%p for v in m))
def mm(x,y):
 a,b,c,d=x;e,f,g,h=y
 return canonical(((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p))
matrices=sorted({canonical((a,b,c,d)) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a*d-b*c)%p==1})
assert len(matrices)==660
lookup={m:i for i,m in enumerate(matrices)};I=lookup[canonical((1,0,0,1))]
T=[[lookup[mm(x,y)] for y in matrices] for x in matrices]
inv=[lookup[canonical((d,(-b)%p,(-c)%p,a))] for a,b,c,d in matrices]
assert all(T[g][inv[g]]==T[inv[g]][g]==I and T[g][I]==T[I][g]==g for g in range(660))
h=lookup[canonical((3,0,0,4))];t=lookup[canonical((0,1,10,0))]
H=[];cur=I
while cur not in H:H.append(cur);cur=T[cur][h]
assert len(H)==5 and cur==I and T[t][t]==I and {T[t][T[u][inv[t]]] for u in H}==set(H)
N=[g for g in range(660) if {T[g][T[u][inv[g]]] for u in H}==set(H)]
invols=[g for g in range(660) if g!=I and T[g][g]==I]
assert len(N)==10 and len(invols)==55 and len(set(N)&set(invols))==5
outside=sorted(set(invols)-set(N));assert len(outside)==50

def double(g):return frozenset(T[a][T[g][b]] for a in H for b in H)
Dt=double(t);assert len(Dt)==5
seen=set();orbital_inputs=[]
for g in outside:
 D=double(g)
 if D in seen:continue
 seen.add(D);assert len(D)==25 and len(D&set(invols))==5
 assert {inv[x] for x in D}==set(D) and not D&set(H) and not D&Dt
 orbital_inputs.append({'representative_id':g,'representative_matrix':matrices[g],'D':sorted(D),'involution_ids':sorted(D&set(invols))})
assert len(orbital_inputs)==10
# Enumerate all stabilizer suborbits as a finite binding for the scope proof.
remaining=set(range(660));allD=[]
while remaining:
 D=double(min(remaining));assert D<=remaining;remaining-=D;allD.append(D)
selfD=[D for D in allD if {inv[x] for x in D}==set(D)]
assert len(allD)==28 and Counter(map(len,allD))==Counter({5:2,25:26})
assert Counter(map(len,selfD))==Counter({5:2,25:10})
# Right H cosets xH, root H first, then lex group-id representatives.
assigned={};cosets=[];reps=[]
for x in [I]+[g for g in range(660) if g!=I]:
 if x in assigned:continue
 C=sorted(T[x][u] for u in H);cid=len(cosets)
 assert len(set(C))==5 and not any(u in assigned for u in C)
 cosets.append(C);reps.append(x)
 for u in C:assigned[u]=cid
assert len(cosets)==132 and len(assigned)==660 and assigned[I]==0
matching=[sorted({assigned[T[x][d]] for d in Dt}) for x in reps]
assert all(len(ns)==1 and ns[0]!=i and matching[ns[0]]==[i] for i,ns in enumerate(matching))
coords={'field':11,'matrix_encoding':'flattened(a,b,c,d), lex minimum of plusminus pair','matrices':matrices,'identity_id':I,'inverse_ids':inv,'H_generator_id':h,'H':H,'t_id':t,'normalizer':N,'involutions':invols,'outside_involutions':outside,'cosets':cosets,'coset_representatives':reps,'element_to_coset':[assigned[g] for g in range(660)],'matching_neighbor':[r[0] for r in matching],'orbitals':orbital_inputs,'full_doublecoset_summary':{'count':len(allD),'sizes':dict(Counter(map(len,allD))),'inverseclosed_sizes':dict(Counter(map(len,selfD)))}}
save('INPUT_TABLES.json',coords)
assert sys.byteorder=='little'
with (out/'group_table.u16le.bin').open('wb') as f:array('H',(x for row in T for x in row)).tofile(f)
save('TABLE_SCHEMA.json',{'path':'group_table.u16le.bin','dtype':'uint16 little endian','shape':[660,660],'entry':'projective canonical matrix product id; matrices and inverses in INPUT_TABLES.json','bytes':660*660*2})
binding={'G':660,'H':5,'N':10,'vertices':132,'involutions':55,'normalizer_involutions':5,'outside_involutions':50,'selfpaired_val5_orbitals':10,'outside_D_size':25,'involutions_per_selfpaired_D':5,'matching_degree':1,'all_stabilizer_suborbits':28,'selfpaired_suborbit_degrees':{'0_loop_excluded':1,'1_matching':1,'5':10},'nonselfpaired_degree5_suborbits':16,'inversepaired_nonself_union_degree':10,'source_BFS':0}
save('BINDING.json',binding)

def closure(adj):
 seen={0};stack=[0]
 while stack:
  for v in adj[stack.pop()]:
   if v not in seen:seen.add(v);stack.append(v)
 return len(seen)
def R3(adj):
 d=[-1]*132;d[0]=0;q=deque([0])
 while q:
  u=q.popleft()
  if d[u]==3:continue
  for v in adj[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 hist=Counter(x for x in d if x>=0)
 return d,[hist[k] for k in range(4)]
rows=[];hit=None
with (out/'CASES.jsonl').open('w') as f:
 for i,o in enumerate(orbital_inputs):
  D=set(o['D'])|set(Dt)
  adj=[sorted({assigned[T[x][d]] for d in D}) for x in reps]
  assert all(len(a)==6 and u not in a and all(u in adj[v] for v in a) for u,a in enumerate(adj))
  # Verify rep independence using all5 group representatives of each coset.
  assert all({assigned[T[x][d]] for d in D}==set(adj[cid]) for cid,C in enumerate(cosets) for x in C)
  degree5=[sorted(set(a)-set(matching[u])) for u,a in enumerate(adj)]
  assert all(len(a)==5 for a in degree5)
  reach=closure(adj);row={'case':i,'representative_id':o['representative_id'],'representative_matrix':o['representative_matrix'],'D_size':25,'root_degree5_neighbors':degree5[0],'root_matching_neighbor':matching[0][0],'n':132,'m':396,'degree':6,'simple':True,'representative_independence':'ALL660_REPRESENTATIVES_MATCH','connected':reach==132,'closure_size':reach,'R3_histogram':None,'R3_missing':None,'actual_global_D':None,'ordinary_bad_unordered_pairs':None}
  if reach==132:
   d,hist=R3(adj);missing=d.count(-1);row.update({'R3_histogram':hist,'R3_missing':missing,'first_missing_coset':d.index(-1) if missing else None})
   row['status']='CONNECTED_R3_FAIL' if missing else 'HIT_D3_PENDING_PARENT'
   if not missing:
    assert max(d)==3;row['actual_global_D']=3;hit=row
    edges=[(u,v) for u,a in enumerate(adj) for v in a if u<v];assert len(edges)==396
    (out/'graph132.edges').write_text('132 396\n'+''.join(f'{u} {v}\n' for u,v in edges))
    save('HIT.json',row);save('PARAMETERS.json',{'G':'PSL2(F11)','H_generator':matrices[h],'matching_t':matrices[t],'orbital_g':o['representative_matrix'],'D_ids':sorted(D),'vertex_definition':'xH with root0=H','input_tables':'INPUT_TABLES.json','group_law':'matrix multiplication mod11, canonicalize plusminus'})
  else:row['status']='DISCONNECTED'
  rows.append(row);f.write(json.dumps(row)+'\n');f.flush()
  save('checkpoint.json',{'status':'HIT' if hit else 'RUNNING','processed':len(rows),'total':10,'CPU_seconds':time.process_time()-start})
  if hit:break
result={'status':'HIT_STOP_REMAINDER_UNTESTED' if hit else 'COMPLETE_ALL10_NO_HIT','prediction':'SUPPORTED_PENDING_PARENT' if hit else 'REFUTED_COMPLETE_FIXED_ACTION','target_Delta':6,'target_D':3,'savedL':120,'n':132,'m':396,'group_order':660,'H_order':5,'total_cases':10,'processed':len(rows),'untested':10-len(rows),'connected_cases':sum(x['connected'] for x in rows),'identity_R3_checks':sum(x['connected'] for x in rows),'R3_failures':sum(x['status']=='CONNECTED_R3_FAIL' for x in rows),'hits':int(hit is not None),'actual_global_D':3 if hit else None,'ordinary_bad_unordered_pairs':None,'binding':binding,'CPU_seconds':time.process_time()-start,'source_BFS':0,'allroot_BFS':0,'extra_groups_or_subgroups':0}
save('WORKER_RESULT.json',result);save('checkpoint.json',{'status':result['status'],'processed':len(rows),'untested':10-len(rows)});print(json.dumps(result),flush=True)
