"""Complete open-neighborhood spare-star test; no distances or BFS.

Optional same interface for another already-bound source:
python scan.py --source EDGEFILE --degree D --out OWN_DIRECTORY
"""
from pathlib import Path
from array import array
from collections import Counter
import argparse
import json
import shutil
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]


def scan_source(source,degree,out,expected_n=None,expected_m=None,deadline=None):
    started=time.process_time();source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=True)
    with source.open() as f:
        n,m=map(int,f.readline().lstrip('#').split())
        if expected_n is not None:assert n==expected_n
        if expected_m is not None:assert m==expected_m
        degrees=[0]*n;edges=array('I');observed=0
        for line in f:
            u,v=map(int,line.split());degrees[u]+=1;degrees[v]+=1;edges.extend((u,v));observed+=1
            if deadline is not None and observed%16384==0 and time.process_time()>deadline:
                return dict(status='CPU_LIMIT_UNKNOWN_DURING_PARSE',source=str(source),source_n=n,source_m=m,
                    degree_cap=degree,edges_read=observed,complete=False,CPU_seconds=time.process_time()-started)
    assert observed==m and max(degrees)<=degree
    saturated=bytearray(d==degree for d in degrees)
    sat_neighbors=bytearray(n)
    for i in range(0,len(edges),2):
        u,v=edges[i],edges[i+1]
        if saturated[u]:sat_neighbors[v]+=1
        if saturated[v]:sat_neighbors[u]+=1
    candidates=[v for v in range(n) if sat_neighbors[v]==0 and degrees[v]>0]
    stem=f'd{degree}_n{n}'
    (out/(stem+'.saturated_neighbor_counts.u8.bin')).write_bytes(sat_neighbors)
    result=dict(status='COMPLETE_SPARE_STAR_SCAN',source=str(source),source_n=n,source_m=m,degree_cap=degree,
        degree_histogram=dict(sorted(Counter(degrees).items())),vertices_scanned=n,
        saturated_neighbor_count_histogram=dict(sorted(Counter(sat_neighbors).items())),
        saturated_neighbor_counts_file=stem+'.saturated_neighbor_counts.u8.bin',
        counts_layout='uint8 pervertex inascendinglabelorder',
        candidate_count=len(candidates),candidate_prototypes=candidates,complete=True,
        graph_generated=False,new_n=None,new_m=None,actual_D=None,source_BFS=0,hash_computations=0)
    if candidates:
        prototype=candidates[0]
        neighbors=[]
        for i in range(0,len(edges),2):
            u,v=edges[i],edges[i+1]
            if u==prototype:neighbors.append(v)
            elif v==prototype:neighbors.append(u)
        neighbors.sort()
        assert len(neighbors)==degrees[prototype] and all(degrees[v]<degree for v in neighbors)
        graph=out/f'graph_d{degree}_D5_n{n+1}.edges'
        with source.open() as old,graph.open('w') as new:
            old.readline();new.write(f'{n+1} {m+len(neighbors)}\n');shutil.copyfileobj(old,new)
            for v in neighbors:new.write(f'{v} {n}\n')
        result.update(graph_generated=True,prototype=prototype,new_vertex=n,new_n=n+1,new_m=m+len(neighbors),
            full_neighbor_set=neighbors,neighbors_old_degrees=[degrees[v] for v in neighbors],
            new_vertex_degree=len(neighbors),source_edges_retained=True,graph_file=str(graph),
            positive_proof='False twin reusesallprototype-first-step routes;newroot-prototype distance2;allneighbors haveactualdegree slack',
            acceptance='PRODUCER_EXACT_STRUCTURAL_HIT_ROOT_CHECK_PENDING')
    result['CPU_seconds']=time.process_time()-started
    (out/(stem+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path)
    parser.add_argument('--degree',type=int)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    if args.source:
        assert args.degree and args.out
        result=scan_source(args.source,args.degree,args.out)
        print(json.dumps(result));return
    prediction=json.loads((OUT/'PREDICTION.json').read_text());assert prediction['frozen_before_scan']
    started=time.process_time();rows=[];reused_cpu=0
    for spec in prediction['source_scopes']:
        existing=OUT/f'd{spec["degree"]}_n{spec["n"]}.json'
        if existing.exists():
            result=json.loads(existing.read_text())
            assert result['complete'] and (result['source_n'],result['source_m'],result['degree_cap'])==(spec['n'],spec['m'],spec['degree'])
            reused_cpu+=result['CPU_seconds']
        else:
            result=scan_source(ROOT/spec['source'],spec['degree'],OUT,spec['n'],spec['m'],started+2.7-reused_cpu)
        rows.append(result)
        print(json.dumps({k:result.get(k) for k in ['status','degree_cap','source_n','source_m','candidate_count','new_n','CPU_seconds']}),flush=True)
    complete=all(r['complete'] for r in rows)
    hits=sum(r.get('graph_generated',False) for r in rows)
    summary=dict(status='COMPLETE_TWO_ACTUAL_SOURCE_SPARE_STAR_SCAN' if complete else 'BUDGET_PARTIAL_UNKNOWN',
        rows=rows,prediction_supported=bool(hits) if complete else None,graph_hits=hits,
        CPU_seconds=reused_cpu+time.process_time()-started,reused_completed_scan_CPU_seconds=reused_cpu,
        source_BFS=0,hash_computations=0,
        scope='Onlyfullopen-neighborhood false-twin insertions onactual51417and94186sources',
        no_saturated_neighbor_deletions=True,pending=['Root independentfirstparametercheck'] if hits else [])
    (OUT/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
    (OUT/'terminal.json').write_text(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2)+'\n')
    print('TERMINAL '+json.dumps({k:v for k,v in summary.items() if k!='rows'}),flush=True)


if __name__=='__main__':main()
