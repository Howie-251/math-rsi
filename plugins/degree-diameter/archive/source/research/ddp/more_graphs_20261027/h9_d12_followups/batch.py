"""Fixed6 exact followups of verified42343. One CPU; no all-source BFS."""
from pathlib import Path
import json
import resource
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
OLD = ROOT / 'research/ddp/global_coverage_20261027'
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_newbase_checks']
source = OLD/'candidate42343/graph_d12_D5_n42343.edges'
with source.open() as stream:
    initial_n, initial_m = map(int,stream.readline().split())
    adj=[[] for _ in range(initial_n)]
    for line in stream:
        u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert initial_n==42343 and initial_m==245229
assert sum(map(len,adj))==2*initial_m and max(map(len,adj))==12
for ns in adj:ns.sort()
pool=json.loads((OLD/'h9_quadric_line_extension_pool/pool.json').read_text())['records']
assert len(pool)==7
rows=[]
accepted=[]
current_m=initial_m
radius_checks=0
reverse_checks=0
unknown=False

def r4_distances(seeds):
    global radius_checks
    dist=bytearray([255])*len(adj);queue=list(seeds)
    for s in seeds:dist[s]=0
    for u in queue:
        depth=dist[u]+1
        if depth>4:break
        for v in adj[u]:
            if dist[v]==255:dist[v]=depth;queue.append(v)
    radius_checks+=1
    return dist

def path_from_anchor(anchor,target,dist):
    assert dist[anchor]<=4
    path=[anchor]
    while path[-1]!=target:
        u=path[-1];path.append(min(v for v in adj[u] if dist[v]+1==dist[u]))
    return path

def write_accepted():
    output=dict(initial_graph=str(source.relative_to(ROOT)),initial_n=initial_n,initial_m=initial_m,
                target_Delta=12,target_D=5,final_n=len(adj),final_m=current_m,
                accepted_extension_count=len(accepted),records=accepted,
                final_independent_allsource_BFS_owner='root',
                final_independent_acceptance_pending=True)
    (OUT/'accepted_extensions.json').write_text(json.dumps(output,indent=2)+'\n')

for candidate in range(1,7):
    stepstart=time.process_time()
    if stepstart-START>170:unknown=True;break
    pins=pool[candidate]['pins']
    N=len(adj)
    row=dict(candidate=candidate,source_n=N,source_m=current_m,mandatory_pins=pins,
             mandatory_pin_current_degrees=[len(adj[v]) for v in pins],
             previously_accepted_candidates=[r['candidate'] for r in accepted])
    blocked=[v for v in pins if len(adj[v])>=12]
    if blocked:
        row.update(status='DEGREE_INFEASIBLE_ON_THIS_BASE',saturated_mandatory_pins=blocked,
                   CPU_seconds=time.process_time()-stepstart)
        rows.append(row);continue
    mandatory=r4_distances(pins)
    (OUT/f'candidate{candidate}_mandatory_R4.u8.bin').write_bytes(mandatory)
    missing=[v for v in range(N) if mandatory[v]==255]
    row.update(mandatory_R4_missing=missing,mandatory_R4_missing_count=len(missing),
               mandatory_R4_allold_covered_count=N-len(missing))
    pinset=set(pins)
    available=[v for v in range(N) if len(adj[v])<12 and v not in pinset]
    row['allowed_anchors']=len(available)
    allbits=(1<<len(available))-1
    coverers={};distances={}
    for t in missing:
        if time.process_time()-START>170:unknown=True;break
        ds=r4_distances([t]);reverse_checks+=1
        bits=bytearray((len(available)+7)//8)
        for j,v in enumerate(available):
            if ds[v]<=4:bits[j>>3]|=1<<(j&7)
        coverers[t]=int.from_bytes(bits,'little');distances[t]=bytes(ds)
    if unknown:
        row.update(status='UNKNOWN_CPU_LIMIT',reverse_targets_completed=len(coverers),
                   CPU_seconds=time.process_time()-stepstart);rows.append(row);break
    anchors=[] if not missing else None
    firsttested=0
    if missing:
        order=sorted(missing,key=lambda t:(coverers[t].bit_count(),t))
        one=allbits
        for t in order:one&=coverers[t]
        row['one_anchor_exists']=bool(one)
        if one:
            anchors=[available[(one&-one).bit_length()-1]]
        else:
            cursor=allbits
            while cursor:
                if firsttested%128==0 and time.process_time()-START>170:unknown=True;break
                first=cursor&-cursor;cursor-=first
                second=allbits&~first
                for t in order:
                    if not (coverers[t]&first):
                        second&=coverers[t]
                        if not second:break
                firsttested+=1
                if second:
                    anchors=[available[first.bit_length()-1],available[(second&-second).bit_length()-1]]
                    break
    row['first_anchors_tested']=firsttested
    if unknown:
        row.update(status='UNKNOWN_CPU_LIMIT',CPU_seconds=time.process_time()-stepstart)
        rows.append(row);break
    if anchors is None:
        row.update(status='NO_AT_MOST_TWO_ANCHORS_ON_THIS_BASE',
                   all_allowed_first_anchors_exhausted=True,CPU_seconds=time.process_time()-stepstart)
        rows.append(row);continue
    neighbors=sorted(pins+anchors)
    assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)
    evidence=[]
    for t in missing:
        a=next(a for a in anchors if distances[t][a]<=4)
        evidence.append(dict(target=t,covering_anchor=a,old_base_distance=distances[t][a],
                             path=path_from_anchor(a,t,distances[t])))
    row.update(status='COMPLETE_EXTENSION_FOUND_PENDING_ROOT_FINAL',new_vertex=N,
               full_neighbor_set=neighbors,anchors=anchors,new_vertex_degree=len(neighbors),
               neighbors_old_degrees=[len(adj[v]) for v in neighbors],
               coverage_paths_for_mandatory_missing=evidence,
               alloldvertices_R4_covered=True,new_n=N+1,new_m=current_m+len(neighbors),
               CPU_seconds=time.process_time()-stepstart)
    # Every recorded path belongs to the prior base. Retain this accepted point for the next row.
    adj.append(neighbors.copy())
    for v in neighbors:adj[v].append(N)
    current_m+=len(neighbors)
    assert max(map(len,adj))<=12
    rows.append(row);accepted.append(row)
    (OUT/f'candidate{candidate}_complete_extension.json').write_text(json.dumps(row,indent=2)+'\n')
    write_accepted()
    print('HIT '+json.dumps(dict(candidate=candidate,source_n=N,new_n=N+1,new_vertex=N,
                              mandatory_pins=pins,anchors=anchors,full_neighbor_set=neighbors,
                              missing_targets=len(missing),CPU_seconds=row['CPU_seconds'])),flush=True)

write_accepted()
status='UNKNOWN_CPU_LIMIT_PARTIAL_BATCH' if unknown else 'COMPLETE_FIXED6_BATCH'
result=dict(prediction_id='H9_FIXED6_ON_42343',status=status,
            prediction_outcome='SUPPORTED_COMPLETE_EXTENSION_EXISTS' if accepted else ('UNKNOWN' if unknown else 'REFUTED_THIS_SEQUENTIAL_BATCH'),
            initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,
            target_Delta=12,target_D=5,candidate_rows_completed=len(rows),rows=rows,
            accepted_extensions=len(accepted),accepted_candidates=[r['candidate'] for r in accepted],
            mandatory_multisource_R4_checks=sum('mandatory_R4_missing' in r for r in rows),
            reverse_target_R4_checks=reverse_checks,total_radius4_checks=radius_checks,
            actual_allsource_BFS_executed=0,historical42343_artifacts_modified=False,
            final_graph_generated_by_producer=False,
            pending=['root final expanded-graph generation and unique independent all-source BFS'] if accepted else [],
            CPU_seconds=time.process_time()-START,
            failure_scope='Each rejection is for its recorded actual current base. No automatic retry on a later base, no thirdanchor or new geometric lines.')
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
