#!/usr/bin/env python3
import collections,itertools,json,pathlib,time
D=pathlib.Path(__file__).resolve().parent
def main():
    if (D/'RESULT.json').exists():raise SystemExit('one bounded local check already complete')
    start=time.process_time()
    pts=list(itertools.product(range(5),repeat=3))
    S={x for x in pts if x[2]!=0 and (x[0]-x[1])%5!=0}
    ell=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)];inv=[1,0,3,2]
    def add(x,y):return tuple((a+b)%5 for a,b in zip(x,y))
    def scale(k,x):return tuple(k*a%5 for a in x)
    def mat(m,x):return tuple(sum(a*b for a,b in zip(row,x))%5 for row in m)
    def line(x,e):return frozenset(add(x,scale(k,e)) for k in range(5))
    def inverse(m):
        a=[[v%5 for v in row]+[int(i==j) for j in range(3)] for i,row in enumerate(m)]
        for k in range(3):
            pivot=next(i for i in range(k,3) if a[i][k]);a[k],a[pivot]=a[pivot],a[k]
            f=pow(a[k][k],-1,5);a[k]=[f*v%5 for v in a[k]]
            for i in range(3):
                if i!=k:
                    f=a[i][k];a[i]=[(u-f*v)%5 for u,v in zip(a[i],a[k])]
        return [row[3:] for row in a]
    T0=[[0,1,1],[1,0,0],[0,0,1]]
    T2=[[1,0,1],[0,1,1],[1,1,1]]
    T=[T0,inverse(T0),T2,inverse(T2)]
    lineinfo=[]
    for p,e in enumerate(ell):
        ll={line(x,e) for x in pts};hist=collections.Counter(len(z&S) for z in ll)
        assert len(ll)==25 and hist=={0:5,4:20}
        lineinfo.append({'port':p,'line_intersection_histogram':dict(hist)})
    N={}
    chartinfo=[]
    for p in range(4):
        assert mat(T[p],ell[p])==ell[inv[p]]
        assert all(mat(T[inv[p]],mat(T[p],x))==x for x in pts)
        hist=collections.Counter()
        for x in S:
            N[p,x]=set(line(mat(T[p],x),ell[inv[p]]))&S
            hist[len(N[p,x])]+=1
        assert hist=={4:80}
        chartinfo.append({'port':p,'matrix':T[p],'per_source_point_neighbor_count_histogram':dict(hist),
                          'T_p_S_outside_S':len({mat(T[p],x) for x in S}-S)})
    reverse_checks=0
    for p in range(4):
        for x in S:
            for y in N[p,x]:assert x in N[inv[p],y];reverse_checks+=1
    imagehist=collections.Counter();unionhist=collections.Counter();same2hist=collections.Counter();groups=0
    for x in S:
        same2={x}
        for q in range(4):
            returned=set().union(*(N[inv[q],z] for z in N[q,x]))
            assert returned==set(line(x,ell[q]))&S
            same2|=returned
        same2hist[len(same2)]+=1
        for p in range(4):
            direct=N[p,x];images=[]
            for q in range(4):
                if q!=p:
                    returned=set().union(*(N[inv[q],z] for z in N[q,x]))
                    img=set().union(*(N[p,w] for w in returned));images.append(img)
            for q in range(4):
                if q!=inv[p]:
                    mids=set().union(*(N[q,y] for y in direct))
                    img=set().union(*(N[inv[q],z] for z in mids));images.append(img)
            assert len(images)==6
            for img in images:
                assert len(img)==16 and direct<=img
                imagehist[len(img)]+=1;groups+=1
            union=set().union(direct,*images);assert len(union)<=76
            unionhist[len(union)]+=1
    assert len(S)==80 and groups==1920 and same2hist=={13:80}
    elapsed=time.process_time()-start;assert elapsed<10
    result={'status':'S80_LOCAL_STRUCTURE_AND76_BASELINE_SUPPORTED','fiber_size':80,
            'directions':ell,'inverse_ports':inv,'line_checks':lineinfo,'charts':chartinfo,
            'reverse_edge_pairs_checked':reverse_checks,'same_fiber_length0_or2_histogram':dict(same2hist),
            'backtrack_images_checked':groups,'image_size_histogram':dict(imagehist),
            'every_image_contains_direct4':True,'six_image_union_histogram_for_this_chart_only':dict(unionhist),
            'universal_six_image_union_upper_bound':76,
            'CPU_seconds':elapsed,'CPU_budget_seconds':10,'workers':1,
            'solver_calls':0,'controller_lifts_generated':0,'large_graph_BFS':0,
            'chart_sample_scope':'One explicit admissible non-S-invariant chart quadruple, no parameter enumeration; universal conclusions rely on PROOF.md.'}
    (D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    (D/'TERMINAL.json').write_text(json.dumps({'running':False,'status':'COMPLETE','CPU_seconds':elapsed,'solver_calls':0,'large_graphs_generated':0},indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
