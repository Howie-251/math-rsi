"""Source-recovery check only: match author recipe IDs against literal edges.

No diameter/BFS/search of new graph parameters. Two prescribed C4 conventions:
first order4 element and the project's earlier order12-torus C4.
"""
from pathlib import Path
import json
import time

OUT=Path(__file__).resolve().parent
P=23
I=(1,0,0,1)


def canon(a):
    return min(a,tuple(-x%P for x in a))


def mul(a,b):
    x,y,z,w=a;r,s,t,u=b
    return canon(((x*r+y*t)%P,(x*s+y*u)%P,(z*r+w*t)%P,(z*s+w*u)%P))


def power(a,n):
    v=I
    for _ in range(n):v=mul(v,a)
    return v


def inv(a):
    x,y,z,w=a
    return canon((w,-y%P,-z%P,x))


def main():
    started=time.process_time()
    group=set()
    for a in range(P):
        for b in range(P):
            for c in range(P):
                if a:group.add(canon((a,b,c,(1+b*c)*pow(a,-1,P)%P)))
                elif b*c%P==P-1:
                    for d in range(P):group.add(canon((a,b,c,d)))
    source_edges={tuple(map(int,line.split())) for line in (OUT/'graph_d6_k5_n1518.edges').read_text().splitlines()}
    source_edges={tuple(sorted(e)) for e in source_edges}
    rows=[]
    for ordering in ['rowmajor_lex','reverse_tuple_lex']:
        G=sorted(group,key=(lambda z:z) if ordering=='rowmajor_lex' else (lambda z:z[::-1]));G.remove(I);G.insert(0,I)
        assert len(G)==6072
        first4=next(g for g in G if power(g,4)==I and power(g,2)!=I)
        torus=next(g for g in G if power(g,12)==I and power(g,6)!=I and power(g,4)!=I)
        invol=next(g for g in G if g!=I and power(g,2)==I)
        invol2=next(g for g in G if g not in [I,invol] and power(g,2)==I and mul(g,invol)==mul(invol,g))
        candidates=[('first_order4',[power(first4,j) for j in range(4)]),
                    ('old_torus_C4',[power(power(torus,3),j) for j in range(4)]),
                    ('first_V4',[I,invol,invol2,mul(invol,invol2)])]
        for side in ['gH','Hg']:
            for name,H in candidates:
                lookup={};reps=[]
                for g in G:
                    if g in lookup:continue
                    v=len(reps);reps.append(g)
                    for s in H:lookup[mul(g,s) if side=='gH' else mul(s,g)]=v
                assert len(reps)==1518
                selected=[]
                for v in [329,967,981]:
                    orbit=sorted({lookup[mul(s,reps[v]) if side=='gH' else mul(reps[v],s)] for s in H})
                    reverse=sorted({lookup[mul(s,inv(reps[v])) if side=='gH' else mul(inv(reps[v]),s)] for s in H})
                    selected.append(dict(recipe_id=v,representative_matrix=reps[v],root_suborbit=orbit,reverse_suborbit=reverse))
                neigh=sorted({v for row in selected for v in row['root_suborbit']})
                edges=set()
                if neigh==[329,435,533,776,967,981]:
                    for u,g in enumerate(reps):
                        for v in neigh:edges.add(tuple(sorted((u,lookup[mul(g,reps[v]) if side=='gH' else mul(reps[v],g)]))))
                rows.append(dict(ordering=ordering,side=side,convention=name,H_generators=H[1:2] if name!='first_V4' else H[1:3],H=H,selected=selected,root_neighbors=neigh,
                                 exact_literal_edge_match=edges==source_edges,
                                 generated_edge_count=len(edges)))
    result=dict(status='SOURCE_CONVENTION_CHECK_COMPLETE',group_size=len(group),source_edge_count=len(source_edges),rows=rows,
                CPU_seconds=time.process_time()-started,source_BFS=0,new_parameter_graphs=0)
    (OUT/'convention_check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
