#!/usr/bin/env python3
"""All4320 exact boundary-route gates; no old-sourceD3BFS or fiber graph."""
import itertools
import json
import time
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'Exoo72/INPUT.json'

def reach3(N,root):
    reach=1<<root
    for depth in range(3):
        new=reach;scan=reach
        while scan:
            bit=scan&-scan;scan-=bit;v=bit.bit_length()-1;new|=N[v]
        reach=new
    return reach
def save(name,data):(HERE/name).write_text(json.dumps(data,indent=2)+'\n')

def main():
    start=time.process_time();assert (HERE/'PRED.json').exists()
    C=json.loads(SOURCE.read_text())['controller'];assert len(C)==72 and all(len(x)==5 for x in C)
    N=[sum(1<<v for v in row) for row in C]
    edges=[(u,v) for u,row in enumerate(C) for v in row if u<v];assert len(edges)==180
    perms=list(itertools.permutations(range(4)));records=[];survivors=[];hist=Counter();nexisting=0
    for edge,(u,v) in enumerate(edges):
        A=[w for w in C[u] if w!=v];B=[w for w in C[v] if w!=u]
        assert len(A)==len(B)==4 and not set(A)&set(B)
        boundary=set(A)|set(B)
        assert not any(y in C[x] for x in boundary for y in boundary if x!=y)
        alive=((1<<72)-1)^((1<<u)|(1<<v));H=[mask&alive for mask in N]
        RA=[reach3(H,x) for x in A];RB=[reach3(H,x) for x in B]
        D=[[bool(H[a]&H[b]) for b in B] for a in A]
        EA=[[bool(RA[i]>>A[j]&1) for j in range(4)] for i in range(4)]
        EB=[[bool(RB[i]>>B[j]&1) for j in range(4)] for i in range(4)]
        nexisting+=sum(EA[i][j] for i in range(4) for j in range(i+1,4))+sum(EB[i][j] for i in range(4) for j in range(i+1,4))
        attempts=[]
        for sigma in perms:
            ip=[sigma.index(j) for j in range(4)];fail=None
            for side,points,E in [('A',A,EA),('B',B,EB)]:
                for i in range(4):
                    for j in range(i+1,4):
                        first,last=(D[j][sigma[i]],D[i][sigma[j]]) if side=='A' else (D[ip[i]][j],D[ip[j]][i])
                        if not(E[i][j] or first or last):
                            fail={'side':side,'indices':[i,j],'old_vertex_pair':[points[i],points[j]],'existing_H_le3':E[i][j],'first_matching_repair':first,'last_matching_repair':last};break
                    if fail:break
                if fail:break
            attempts.append({'sigma':sigma,'passes_boundary_gate':fail is None,'failure':fail})
            if fail:hist[fail['side']]+=1
            else:survivors.append({'source_edge_index':edge,'deleted':[u,v],'A':A,'B':B,'sigma':sigma})
        records.append({'edge':edge,'deleted':[u,v],'A':A,'B':B,'AunionB_independent':True,'D_commonneighbor_matrix':D,'existing_A_le3':EA,'existing_B_le3':EB,'attempts':attempts})
    save('BOUNDARY_CERTIFICATE.json',{'source_controller':C,'per_source_edge':records})
    save('BOUNDARY_SURVIVORS.json',survivors)
    # One targeted counterfactual pair check validates the no-route diagnosis,
    # not a full-root BFS or controller acceptance run.
    failed=next(((e,a) for e in records for a in e['attempts'] if a['failure']),None)
    check=None
    if failed:
        e,a=failed;u,v=e['deleted'];alive=((1<<72)-1)^((1<<u)|(1<<v));H=[mask&alive for mask in N]
        for i,j in enumerate(a['sigma']):
            x,y=e['A'][i],e['B'][j];H[x]|=1<<y;H[y]|=1<<x
        x,y=a['failure']['old_vertex_pair'];assert not(reach3(H,x)>>y&1)
        check={'deleted':[u,v],'sigma':a['sigma'],'unreachable_le3_pair':[x,y],'direct_new_adjacency_R3_pair_check':True,'full_controller_BFS':False}
        save('ONE_TARGETED_FAILURE_CHECK.json',check)
    result={'status':'ALL4320_FAIL_EXACT_SAME_SIDE_GATE' if not survivors else 'BOUNDARY_SURVIVORS_REQUIRE_NEW_CONTROLLER_CHECK','parameter_assignments':4320,'source_edges':180,'matchings_per_edge':24,'structural_independence_checks_passed':180,'boundary_survivors':len(survivors),'first_failing_side_histogram':dict(hist),'original_H_existing_same_side_pairs_over180edges':nexisting,'oldsource_D3_BFS':0,'new_full_controller_BFS':0,'targeted_failure_pair_checks':int(check is not None),'fiber_graphs':0,'solver_calls':0,'CPU_seconds':time.process_time()-start,'CPU_budget_seconds':20,'workers':1}
    save('PREFLIGHT_RESULT.json',result)
    print(json.dumps(result))

if __name__=='__main__':main()
