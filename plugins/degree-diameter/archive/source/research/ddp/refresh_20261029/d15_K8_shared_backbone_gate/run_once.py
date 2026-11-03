#!/usr/bin/env python3
"""One exact cached-support diagnostic, no source graph or distance code."""
import collections, datetime, json, os, resource, time
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
INPUT=HERE.parent/'d15_D4_K2_route_gate'
N,K,W=15552,648,11

def save(name,obj):
    (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def bits(x):
    while x:
        b=x&-x;yield b.bit_length()-1;x-=b

def main():
    wall=time.monotonic();resource.setrlimit(resource.RLIMIT_CPU,(5,5))
    save('HANDLE.json',dict(pid=os.getpid(),command=['python','run_once.py'],CPU_budget=5,workers=1,
        started_UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()))
    labels=list(map(int,(INPUT/'FREE_ORDER.txt').read_text().split()))
    assert len(labels)==K and len(set(labels))==K
    fibers=sorted({v//81 for v in labels});assert len(fibers)==24
    fiber_index={f:i for i,f in enumerate(fibers)}
    fm=[0]*24;fc=[0]*24
    for p,v in enumerate(labels):
        i=fiber_index[v//81];fm[i]|=1<<p;fc[i]+=1
    assert fc==[27]*24
    b2=(INPUT/'target_R2_support.u64le.bin').read_bytes()
    b3=(INPUT/'target_R3_support.u64le.bin').read_bytes()
    assert len(b2)==len(b3)==N*W*8
    records=[];bytriple=collections.defaultdict(list)
    block_hist=collections.Counter();vector_hist=collections.Counter()
    total_support_hist=collections.Counter();fiber_count_hist=[collections.Counter()for _ in fibers]
    for t in range(N):
        r2=int.from_bytes(b2[t*W*8:(t+1)*W*8],'little')
        assert r2.bit_length()<=K
        if r2.bit_count()!=3:continue
        cols=tuple(bits(r2));key=tuple(sorted(labels[p]for p in cols))
        r3=int.from_bytes(b3[t*W*8:(t+1)*W*8],'little')
        assert r3.bit_length()<=K and (r2 & ~r3)==0
        counts=tuple((r3&m).bit_count()for m in fm)
        block=sum((1<<i)for i,c in enumerate(counts)if c)
        rec=dict(target=t,triple=key,columns=cols,R3_counts=counts,R3_block_mask=block,R3_literal_support=r3)
        bytriple[key].append(len(records));records.append(rec)
        block_hist[block]+=1;vector_hist[counts]+=1;total_support_hist[sum(counts)]+=1
        for i,c in enumerate(counts):fiber_count_hist[i][c]+=1
    assert len(records)==5184
    keys=sorted(bytriple);ids={k:i for i,k in enumerate(keys)}
    block_keys=sorted(block_hist);block_ids={k:i for i,k in enumerate(block_keys)}
    vector_keys=sorted(vector_hist);vector_ids={k:i for i,k in enumerate(vector_keys)}
    port_distinct=[0]*K;port_weighted=[0]*K
    triple_records=[];geometric=collections.Counter();directions=collections.Counter()
    triple_multiplicity=collections.Counter();within_blocks=collections.Counter();within_vectors=collections.Counter();within_literals=collections.Counter()
    for key in keys:
        rows=[records[i]for i in bytriple[key]];cols=rows[0]['columns'];multiplicity=len(rows)
        for p in cols:port_distinct[p]+=1;port_weighted[p]+=multiplicity
        same=len({v//81 for v in key})==1
        points=[[((v%81)//3**i)%3 for i in range(4)]for v in key]
        line=same and all(sum(p[i]for p in points)%3==0 for i in range(4))
        direction=None
        if line:
            direction=[(points[1][i]-points[0][i])%3 for i in range(4)]
            leading=next(c for c in direction if c)
            direction=[c*leading%3 for c in direction]
            directions[tuple(direction)]+=1
        geometric['same_fiber'if same else 'multiple_fibers']+=1
        geometric['affine_line'if line else 'not_an_affine_line_in_one_fiber']+=1
        nb=len({r['R3_block_mask']for r in rows});nv=len({r['R3_counts']for r in rows});nl=len({r['R3_literal_support']for r in rows})
        within_blocks[nb]+=1;within_vectors[nv]+=1;within_literals[nl]+=1;triple_multiplicity[multiplicity]+=1
        triple_records.append(dict(id=ids[key],provider_labels=key,provider_columns=cols,target_count=multiplicity,
            targets=[r['target']for r in rows],same_freefiber=same,freefiber=key[0]//81 if same else None,
            affine_line_in_F3_4=line,normalized_direction=direction,
            distinct_R3_block_supports=nb,distinct_R3_fiber_count_vectors=nv,distinct_R3_literal_supports=nl))
    save('R2_TRIPLES.json',dict(scope='all 5184 targets with exactly3 R2 providers',triples=triple_records))
    save('PORT_MULTIPLICITIES.json',dict(ports=[dict(column=i,label=labels[i],fiber=labels[i]//81,
        distinct_triples=port_distinct[i],target_weighted_triples=port_weighted[i])for i in range(K)]))
    save('R3_BLOCK_SIGNATURES.json',dict(fiber_order=fibers,signatures=[dict(id=block_ids[b],mask=b,
        occupied_fibers=[fibers[i]for i in bits(b)],target_count=block_hist[b])for b in block_keys]))
    save('R3_COUNT_SIGNATURES.json',dict(fiber_order=fibers,signatures=[dict(id=vector_ids[v],counts=v,
        target_count=vector_hist[v])for v in vector_keys]))
    with (HERE/'SPARSE_TARGET_ROWS.jsonl').open('w')as f:
        for r in records:
            f.write(json.dumps(dict(target=r['target'],R2_triple_id=ids[r['triple']],
                R3_block_signature=block_ids[r['R3_block_mask']],R3_count_signature=vector_ids[r['R3_counts']]),separators=(',',':'))+'\n')
    save('SUPPORT_INTERFACE.json',dict(source_n=N,ports=K,row_words_u64=W,byte_order='little',
        R2_support=str((INPUT/'target_R2_support.u64le.bin').relative_to(ROOT)),
        R3_support=str((INPUT/'target_R3_support.u64le.bin').relative_to(ROOT)),
        column_to_oldlabel=labels,freefiber_order=fibers,freefiber_sizes=fc,
        scope='Original complete15552 target rows remain authoritative; diagnostic selects5184 only.',
        pin_limit_each=8,helpers=8,port_capacity=1,
        exact_constraint='for each target t and helper i: hit_T_R2(t) OR hit_Ai_R3(t)',
        backbone_necessary='hit_T_R2(t) OR |T intersect R3support(t)| >=8',
        symmetry_assumption=False))
    result=dict(status='COMPLETE_CACHED_SUPPORT_DIAGNOSTIC',pid=os.getpid(),targets=5184,
        distinct_R2_provider_triples=len(keys),R2_triple_target_multiplicity_histogram=dict(sorted(triple_multiplicity.items())),
        distinct_triple_geometry=dict(geometric),normalized_direction_histogram={str(k):v for k,v in directions.items()},
        port_distinct_triple_multiplicity_histogram=dict(sorted(collections.Counter(port_distinct).items())),
        port_target_weighted_multiplicity_histogram=dict(sorted(collections.Counter(port_weighted).items())),
        distinct_R3_block_supports=len(block_keys),R3_occupied_fiber_count_histogram=dict(sorted(collections.Counter({}).items())),
        distinct_R3_fiber_count_vectors=len(vector_keys),R3_total_provider_histogram=dict(sorted(total_support_hist.items())),
        per_triple_distinct_R3_block_signature_histogram=dict(sorted(within_blocks.items())),
        per_triple_distinct_R3_count_vector_histogram=dict(sorted(within_vectors.items())),
        per_triple_distinct_R3_literal_support_histogram=dict(sorted(within_literals.items())),
        R3_fiber_provider_histograms=[dict(fiber=fibers[i],histogram=dict(sorted(h.items())))for i,h in enumerate(fiber_count_hist)],
        CPU_seconds=time.process_time(),wall_seconds=time.monotonic()-wall,CPU_budget=5,
        source_graph_reads=0,ball_recomputations=0,BFS=0,solver_calls=0,new_graphs=0)
    occupied=collections.Counter()
    for b,n in block_hist.items():occupied[b.bit_count()]+=n
    result['R3_occupied_fiber_count_histogram']=dict(sorted(occupied.items()))
    save('RESULT.json',result)
    save('TERMINAL.json',dict(status=result['status'],pid=os.getpid(),returncode=0,CPU_seconds=result['CPU_seconds'],
        all_5184_rows_completed=True,running=False,pending=[]))
    print(json.dumps({k:result[k]for k in ['status','pid','CPU_seconds','distinct_R2_provider_triples',
        'R2_triple_target_multiplicity_histogram','distinct_triple_geometry','port_distinct_triple_multiplicity_histogram',
        'distinct_R3_block_supports','distinct_R3_fiber_count_vectors','per_triple_distinct_R3_block_signature_histogram',
        'per_triple_distinct_R3_literal_support_histogram']}))

if __name__=='__main__':main()
