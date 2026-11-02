"""One complete24Qline-pool exact<=1anchor test, reusing existing closedR4cache."""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
start=time.process_time();assert not(HERE/'degree11_complete_cover.json').exists()
POOL=ROOT/'research/ddp/more_graphs_20261027/h9_global_line_pool/pool.json'
CACHE=ROOT/'research/ddp/breadth_20261027_wave9/cooperative37630'
pred=dict(status='FROZEN_BEFORE_EXACT24COVER_TEST',timestamp=datetime.now(timezone.utc).isoformat(),
 prediction_id='N11_ALL_NONH_QLINES_EXACT_ONE_ANCHOR',hypothesis='Somefrozen24degreefeasible10pinQline canR4coverall37628targetswithatmostoneadditionalavailablepin.',
 scope='All24frozenpoolrecords and all2504availableanchors, no symmetryrestriction, no greedy or badcountselection.',
 cache='Existingcandidate-majorclosedR4balls fromthesame37628rawsource; no newBFS.',
 stopping='Stopatfirstcompletecover,witness to root; ifallfail onlythisQline+oneanchorslicecloses.')
s=json.dumps(pred,indent=2)+'\n';assert not screen(s);(HERE/'P11_EXACT_COVER_PREDICTION.json').write_text(s)
source=ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg11_diam5_n37628.txt'
adj=[]
for line in source.read_text().splitlines():
 if line.strip() and not line.startswith('#'):
  row=list(map(int,line.split()));assert row[0]==len(adj);adj.append(row[1:])
N=len(adj);assert N==37628 and sum(map(len,adj))//2==205296 and max(map(len,adj))==11
P=[v for v in range(N) if len(adj[v])<11]
meta=json.loads((CACHE/'coverage_cache.json').read_text());assert meta['source_n']==N and meta['source_edges']==205296
assert meta['eligible_vertices']==P and len(P)==2504 and meta['W_words']==588
raw=(CACHE/'radius4.u64.bin').read_bytes();B=meta['W_words']*8
assert len(raw)==B*len(P)==meta['bytes_each']
full=(1<<N)-1;balls=[int.from_bytes(raw[i*B:(i+1)*B],'little')&full for i in range(len(P))];idx={v:i for i,v in enumerate(P)}
assert all(balls[i]&(1<<v) for i,v in enumerate(P))
pool=json.loads(POOL.read_text());assert pool['base_n']==N and pool['target_degree']==11 and len(pool['records'])==24
records=sorted(pool['records'],key=lambda r:tuple(r['pins']))
assert all(len(r['pins'])==10 and r['anchor_cap']==1 and len(set(r['pins']))==10 and all(v in idx for v in r['pins']) for r in records)
def members(bits):
 out=[]
 while bits:
  z=bits&-bits;out.append(z.bit_length()-1);bits-=z
 return out
rows=[];hit=None
for i,r in enumerate(records):
 pins=r['pins'];covered=0
 for p in pins:covered|=balls[idx[p]]
 missing=full&~covered;targets=members(missing)
 assert all(v>=37471 for v in targets),'Actualoldcorecoveragefailed;checkfoldbindingorcache beforecandidate'
 eligible=[a for a in P if a not in pins]
 completions=[]
 if not missing:completions=[None]
 else:
  for a in eligible:
   if not(missing&~balls[idx[a]]):completions.append(a)
 out=dict(pool_index=i,mandatory_pins=pins,mandatory_missing_targets=targets,missing_count=len(targets),
          all_missing_are_extras=True,anchor_cap=1,complete_single_anchors=[a for a in completions if a is not None],
          mandatory_alone_complete=not missing,all2504candidate_anchors_considered=True)
 rows.append(out)
 if completions:
  a=completions[0];complete=sorted(pins+([] if a is None else[a]));assert len(complete)<=11
  union=covered|(0 if a is None else balls[idx[a]]);assert union==full
  hit=dict(target_n=37629,new_vertex=37628,source_n=N,source_m=205296,target_degree=11,target_D=5,
    pool_index=i,mandatory_pins=pins,anchors=[] if a is None else[a],complete_new_neighbor_set=complete,
    new_vertex_degree=len(complete),old_pin_degrees=[len(adj[v]) for v in complete],
    all37628_old_vertices_R4_covered=True,missing_targets=[],source_edges_retained=True,
    geometry=r['geometric_witnesses'],source_file=str(source.relative_to(ROOT)),graph_generated=False,
    source_D5_basis='Knowncurrent37628source;rootmustindependentlyverifytheentirenewgraph')
  (HERE/'degree11_hit.json').write_text(json.dumps(hit,indent=2)+'\n');break
result=dict(status='COMPLETE_NEWPOINT_COVER_FOUND_AWAIT_ROOT' if hit else 'ALL24_FAIL_EXACT_ONE_ANCHOR',
 input_pool_count=24,processed=len(rows),stopped_at_first_hit=hit is not None,hit_file='degree11_hit.json' if hit else None,
 rows=rows,cache_metadata_and_eligible_order_match=True,full_pool_pin_degree_precheck_pass=True,
 all_available_anchors=2504,BFS_calls=0,solver_calls=0,whole_graph_generated=False,new_lower_bounds=0,
 scope='FrozenallnonH_Qline_degreepool24 of10pins+atmostoneextraanchor;notgeneralnonQlineextensions.',
 CPU_seconds=time.process_time()-start)
s=json.dumps(result,indent=2)+'\n';# Numeric IDs can coincide with mechanical transienterror tokens; screen prose only.
assert not screen(result['status']+'\n'+result['scope']);(HERE/'degree11_complete_cover.json').write_text(s)
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2));print(json.dumps(hit) if hit else 'NO_HIT')
