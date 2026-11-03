"""Move a leaf triangle as a whole, allowing an invalid intermediate switch.

Only the 48 specified moves from the saved graph are considered. This changes
triangle intersection blocks from one three-triangle chain to two bowties.
"""
from pathlib import Path
import json,time
import numpy as np
from diagnose import cycles

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'second_mechanism/control_unrestricted_n31.edges'


def main():
    begin=time.process_time()
    rows=[tuple(map(int,l.split())) for l in SOURCE.read_text().splitlines()]
    n,m=rows[0];edges=set(tuple(sorted(e)) for e in rows[1:]);A=np.zeros((n,n),dtype=np.int64)
    for u,v in edges:A[u,v]=A[v,u]=1
    adj=[set(np.flatnonzero(A[v]).tolist()) for v in range(n)]
    core={0,1,11,18,19,24,30};triangles=cycles(adj,3);results=[];invalid=[];best=n*n
    for hub,leaf in [(30,[0,1]),(11,[18,19])]:
        for w in sorted(set(range(n))-core):
            local=[t for t in triangles if w in t];assert len(local)==1
            own=set(local[0])-{w};external=sorted(adj[w]-own);assert len(external)==2
            remove={tuple(sorted(e)) for e in [(hub,leaf[0]),(hub,leaf[1]),(w,external[0]),(w,external[1])]}
            add={tuple(sorted(e)) for e in [(w,leaf[0]),(w,leaf[1]),(hub,external[0]),(hub,external[1])]}
            if len(remove)!=4 or len(add)!=4 or any(u==v for u,v in add) or (edges-remove)&add:
                invalid.append(dict(hub=hub,w=w,reason='self-loop or duplicate after simultaneous exchange'));continue
            newedges=(edges-remove)|add;B=np.zeros((n,n),dtype=np.int64)
            for u,v in newedges:B[u,v]=B[v,u]=1
            assert len(newedges)==62 and np.all(B.sum(axis=1)==4)
            B3=(B@B)@B;zeros=np.argwhere(B3==0).tolist()
            assert np.all(np.diag(B3)>0)
            bad=sorted([p for p in zeros if p[0]<=p[1]])
            record=dict(hub=hub,detached_triangle=sorted([hub]+leaf),new_shared_vertex=w,
                        other_triangle=local[0],remove=sorted(remove),add=sorted(add),
                        net_remove=sorted(remove-add),net_add=sorted(add-remove),
                        net_removed_edge_count=len(remove-add),
                        zero_count=len(zeros),missing_unordered_pairs=bad,
                        triangle_count=int(np.trace(B3)//6),
                        four_cycle_count=len(cycles([set(np.flatnonzero(B[u]).tolist()) for u in range(n)],4)))
            results.append(record)
            if len(zeros)<best:
                best=len(zeros)
                (HERE/'triangle_transfer_best.edges').write_text(f'{n} {len(newedges)}\n'+''.join(f'{u} {v}\n' for u,v in sorted(newedges)))
                (HERE/'triangle_transfer_best.json').write_text(json.dumps(record,indent=2)+'\n')
    genuine=[r for r in results if r['net_removed_edge_count']==4]
    out=dict(scope='48 joint leaf-triangle transfers from saved 31-vertex graph; not a general search',
             proposed=48,valid=len(results),invalid=invalid,best_zero_count=best,
             genuine_four_edge_count=len(genuine),best_genuine_four_edge_zero_count=min(r['zero_count'] for r in genuine),
             cpu_seconds=time.process_time()-begin,results=results)
    (HERE/'joint_triangle_transfer.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('results','invalid')},indent=2))
    print('best',json.loads((HERE/'triangle_transfer_best.json').read_text()))


if __name__=='__main__':main()
