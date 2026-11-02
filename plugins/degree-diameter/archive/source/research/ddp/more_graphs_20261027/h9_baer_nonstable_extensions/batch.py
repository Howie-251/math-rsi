from pathlib import Path
import json,subprocess,time,resource
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[3];P=OUT.parent
resource.setrlimit(resource.RLIMIT_CPU,(8,9));start=time.process_time()
source=P/'h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges'
with source.open() as f:
 initial_n,initial_m=map(int,f.readline().split());adj=[[] for _ in range(initial_n)]
 for line in f:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
current=source;m=initial_m;rows=[];accepted=[]
pool=json.loads((P/'h9_baer_nonstable_global_pool/pool12.json').read_text())['records']
assert len(pool)==2
(OUT/'PREDICTION.json').write_text(json.dumps(dict(source_n=initial_n,scope=2,prediction='At leastone new nonstable Baer11 set can cover the remainingextras with one anchor.',anchor_cap=1,budget_CPU=5,old_graph_reverified=False),indent=2)+'\n')
(OUT/'items').mkdir(exist_ok=True);(OUT/'graphs').mkdir(exist_ok=True)
for item in sorted(pool,key=lambda v:tuple(v['pins'])):
 pins=item['pins'];N=len(adj);row=dict(pool_index=item['pool_index'],source_n=N,source_m=m,mandatory_pins=pins,anchor_cap=12-len(pins));assert len(pins)==11
 if any(len(adj[v])>=12 for v in pins):row['status']='CURRENT_DEGREE_BLOCKED';rows.append(row);continue
 prefix=OUT/'items'/f"pool{item['pool_index']}_n{N}";pinfile=Path(str(prefix)+'.pins.txt');pinfile.write_text(' '.join(map(str,pins))+'\n')
 subprocess.run([str(P/'h9_d12_eightpin_extensions/cover'),'prepare',str(current),str(pinfile),str(prefix)],check=True)
 d=json.loads(Path(str(prefix)+'.json').read_text());miss=d['missing'];assert all(v>=41356 for v in miss)
 row.update(mandatory_missing=len(miss),core_missing=0,native_CPU=d['CPU_seconds'])
 anchors=[] if not miss else (d['exact_anchors'] if d.get('exact_one_or_two_found') and len(d['exact_anchors'])<=1 else None)
 if anchors is None:row['status']='EXACT_NO_AT_MOST_ONE_ANCHOR';rows.append(row);continue
 ns=sorted(pins+anchors);olddegrees=[len(adj[v]) for v in ns];assert len(ns)==len(set(ns))<=12 and max(olddegrees)<12
 if anchors:
  pinfile.write_text(' '.join(map(str,ns))+'\n');selected=Path(str(prefix)+'_selected')
  subprocess.run([str(P/'h9_d12_eightpin_extensions/cover'),'verify',str(current),str(pinfile),str(selected)],check=True)
  check=json.loads(Path(str(selected)+'.json').read_text());assert check['missing_count']==0
 row.update(status='ACCEPTED_BY_COMPLETE_CURRENT_R4',new_vertex=N,full_neighbor_set=ns,anchors=anchors,old_neighbor_degrees=olddegrees,new_n=N+1,new_m=m+len(ns),selected_R4_missing=0,core_missing=0,geometric_witness=item)
 adj.append(ns.copy())
 for v in ns:adj[v].append(N)
 m+=len(ns);current=OUT/'graphs'/f'graph_d12_D5_n{len(adj)}.edges'
 with current.open('w') as f:
  f.write(f'{len(adj)} {m}\n')
  for u,vs in enumerate(adj):
   for v in vs:
    if u<v:f.write(f'{u} {v}\n')
 row['graph_file']=str(current.relative_to(ROOT));accepted.append(row);rows.append(row);print('HIT '+json.dumps(row),flush=True)
child=resource.getrusage(resource.RUSAGE_CHILDREN)
r=dict(status='COMPLETE_FIXED_TWO_NONSTABLE_BAERS',initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=m,final_graph=str(current.relative_to(ROOT)),rows=rows,records=accepted,accepted_extensions=len(accepted),CPU_seconds=time.process_time()-start+child.ru_utime+child.ru_stime,old_source_BFS=0,pending=[])
(OUT/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print('TERMINAL '+json.dumps({k:v for k,v in r.items() if k not in ['rows','records']}),flush=True)
