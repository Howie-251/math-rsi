"""One authorized published-census radius filter; no network or graph search."""
import resource
resource.setrlimit(resource.RLIMIT_CPU,(42,42))
from pathlib import Path
from collections import Counter
import json,time

OUT=Path(__file__).resolve().parent
INPUT=OUT.parent
INDEX=INPUT.parent
ORDERS=list(range(42,54))+list(range(105,162))
START=time.process_time()

def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2)+'\n')

def decode_s6(raw,expected):
    """Sparse6 b,x stream, including the standard overlarge-padding break."""
    raw=raw.rstrip(b'\r\n')
    if raw.startswith(b'>>sparse6<<'):
        raw=raw[11:]
    if not raw.startswith(b':'):
        raise ValueError('non-sparse6 graph line')
    data=raw[1:]
    if not data or any(c<63 or c>126 for c in data):
        raise ValueError('invalid sparse6 character')
    if data[0]!=126:
        n=data[0]-63;off=1
    elif len(data)>=4 and data[1]!=126:
        n=((data[1]-63)<<12)|((data[2]-63)<<6)|(data[3]-63);off=4
    else:
        raise ValueError('unexpected 36bit order encoding in this n<=161 scope')
    if n!=expected:
        raise ValueError(f'decoded order {n} != filename {expected}')
    k=max(1,(n-1).bit_length());width=k+1;mask=(1<<k)-1
    adj=[0]*n;bits=[1<<i for i in range(n)]
    v=0;buffer=0;nbits=0;edges=0;finished=False
    for c in data[off:]:
        buffer=(buffer<<6)|(c-63);nbits+=6
        while nbits>=width:
            nbits-=width;pair=(buffer>>nbits)&((1<<width)-1)
            b=pair>>k;x=pair&mask
            v+=b
            if x>=n or v>=n:
                finished=True;break
            if x>v:
                v=x
            else:
                if x==v:
                    raise ValueError('loop in decoded census graph')
                if adj[x]&bits[v]:
                    raise ValueError('repeated edge in decoded census graph')
                adj[x]|=bits[v];adj[v]|=bits[x];edges+=1
        if finished:
            break
        buffer &= (1<<nbits)-1
    if edges!=2*n or any(a.bit_count()!=4 for a in adj):
        raise ValueError('decoded graph is not simple4regular with2n edges')
    return adj

def lines(path):
    for lineno,raw in enumerate(path.open('rb'),1):
        stripped=raw.rstrip(b'\r\n')
        if not stripped or stripped==b'>>sparse6<<':
            yield lineno,raw,None
        else:
            yield lineno,raw,stripped

def radius(adj,root,D):
    seen=1<<root;front=seen;hist=[1]
    for depth in range(1,D+1):
        nxt=0
        while front:
            bit=front&-front;front-=bit;nxt|=adj[bit.bit_length()-1]
        front=nxt&~seen;seen|=front;hist.append(front.bit_count())
    return seen,hist

def main():
    receipt=json.loads((INPUT/'DOWNLOAD_RECEIPT.json').read_text())
    if receipt.get('status')!='COMPLETE_DOWNLOAD':
        raise ValueError('download must be COMPLETE_DOWNLOAD before graph parsing')
    completed=receipt.get('completed_orders')
    if completed is not None and sorted(completed)!=ORDERS:
        raise ValueError('complete download orders mismatch')
    expected={e['order_from_filename']:e for e in json.loads((INDEX/'CENTRAL_INDEX.json').read_text())['entries']}
    actual_inputs=[]
    for n in ORDERS:
        path=INPUT/f'Cay4val_{n}.s6'
        if path.stat().st_size!=expected[n]['uncompressed_size']:
            raise ValueError('member size differs from complete central index')
        actual_inputs.append({'n':n,'path':str(path),'bytes':path.stat().st_size,'target_D':3 if n<=53 else 4})
    save('INPUT_RECEIPT.json',{'download_status':receipt['status'],'members':actual_inputs,'member_count':69,'complete_census_claim':'inherited from published authors','network_requests':0})

    # Only parser calibration: three new literal graphs, zero radius/BFS calls.
    import networkx as nx
    checks=[]
    for n in [42,108,128]:
        first=next((x for x in lines(INPUT/f'Cay4val_{n}.s6') if x[2] is not None),None)
        if first is None:raise ValueError('missing first calibration graph')
        lineno,raw,s=first;adj=decode_s6(s,n);G=nx.from_sparse6_bytes(s)
        target=[sum(1<<v for v in G[u]) for u in range(n)]
        if G.is_multigraph() or nx.number_of_selfloops(G) or adj!=target:
            raise ValueError('custom sparse6 decoder differs from NetworkX')
        checks.append({'order':n,'member_line':lineno,'adjacency':'EXACT_MATCH_NETWORKX','edges':G.number_of_edges(),'radius_checks':0})
    save('PARSER_CALIBRATION.json',{'status':'THREE_LITERAL_ADJACENCIES_MATCH','checks':checks,'standard':'installed NetworkX from_sparse6_bytes; v>=n or x>=n terminates padding','BFS':0})

    counts=Counter();members=[];hit=None;processed_orders=[]
    with (OUT/'CASES.jsonl').open('w') as casefile:
        for n in ORDERS:
            D=3 if n<=53 else 4;full=(1<<n)-1;graphs=0;non_graph_lines=0;total_lines=0;rootpasses=0
            for lineno,raw,s in lines(INPUT/f'Cay4val_{n}.s6'):
                total_lines+=1
                if s is None:
                    non_graph_lines+=1;continue
                adj=decode_s6(s,n);graphs+=1;counts['decoded_simple_quartic_graphs']+=1
                reached,hist=radius(adj,0,D);counts['root0_radius_checks']+=1
                missing=(full^reached).bit_count()
                row={'order':n,'target_D':D,'member_line':lineno,'graph_in_member':graphs,'root0_R_missing':missing,'root0_R_histogram':hist,'actual_global_D':None,'ordinary_bad_unordered_pairs':None}
                if missing:
                    counts['root0_radius_rejects']+=1
                    row['status']='ROOT0_TARGET_RADIUS_FAIL'
                    missmask=full^reached;row['first_missing_vertex']=(missmask&-missmask).bit_length()-1
                else:
                    rootpasses+=1;counts['root0_radius_passes']+=1
                    firstfail=None
                    for root in range(1,n):
                        seen,rhist=radius(adj,root,D);counts['additional_positive_validation_roots']+=1
                        if seen!=full:
                            firstfail={'root':root,'R_missing':(full^seen).bit_count()};break
                    if firstfail:
                        row['status']='ROOT0_PASS_LATER_ROOT_FAIL';row['later_root_failure']=firstfail
                        counts['later_root_rejects']+=1
                    else:
                        row['status']='PRODUCER_ALLROOT_POSITIVE_PENDING_PARENT';row['actual_global_D']=D
                        edges=[(u,v) for u in range(n) for v in range(u+1,n) if adj[u]>>v&1]
                        (OUT/'candidate.edges').write_text(f'{n} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in edges))
                        (OUT/'candidate.original.s6').write_bytes(raw)
                        hit={**row,'source_member':f'Cay4val_{n}.s6','source_archive':'https://atlas.graphsym.net/Cay4val/Cay4valUpTo1025.zip','acceptance':'PARENT_INDEPENDENT_ACCEPTANCE_PENDING','all_roots_checked':n}
                        save('HIT.json',hit);counts['producer_allroot_hits']+=1
                casefile.write(json.dumps(row)+'\n')
                if counts['decoded_simple_quartic_graphs']%128==0 or hit:
                    casefile.flush();save('checkpoint.json',{'status':'HIT' if hit else 'RUNNING','order':n,'member_line':lineno,'graphs_in_current_member':graphs,'counts':dict(counts),'CPU_seconds':time.process_time()-START})
                if hit:break
            members.append({'order':n,'target_D':D,'graphs_processed':graphs,'raw_lines_read':total_lines,'non_graph_lines':non_graph_lines,'root0_passes':rootpasses,'complete_member':not bool(hit),'decoded_order_and_simple4regular':'ALL_MATCH','expected_graph_count':None,'census_count_scope':'every physical graph line accounted for; archive metadata provides no per-order graph count'})
            casefile.flush();save('MEMBER_RECEIPTS.json',members)
            if hit:break
            processed_orders.append(n)
    result={'status':'PRODUCER_HIT_STOP_REMAINDER_UNTESTED' if hit else 'COMPLETE_ALL69_NO_IMPROVEMENT','prediction':'SUPPORTED_PRODUCER_PENDING_PARENT' if hit else 'REFUTED_COMPLETE_PUBLISHED_CENSUS_FILTER','selected_orders':ORDERS,'completed_orders':processed_orders,'member_count_complete':len(processed_orders),'remaining_order_count':len(ORDERS)-len(processed_orders),'counts':dict(counts),'hit':hit,'actual_global_D':hit['actual_global_D'] if hit else None,'ordinary_bad_unordered_pairs':None,'conditional_census_scope':'All improved degree<=4 Cayley graphs in the(4,3)/(4,4) Moore-bounded orders, conditional on the published complete census and these literal member receipts. No new census/classification proof.','CPU_seconds':time.process_time()-START,'source_BFS':0,'sourcegroup108_reexecution':0,'solver_calls':0,'network_requests':0}
    save('WORKER_RESULT.json',result);save('checkpoint.json',{'status':result['status'],'counts':dict(counts),'completed_orders':processed_orders});print(json.dumps(result),flush=True)

if __name__=='__main__':
    try:main()
    except Exception as ex:
        save('WORKER_ERROR.json',{'status':'ERROR_NO_COMPLETE_SCOPE','exception':repr(ex),'CPU_seconds':time.process_time()-START})
        raise
