#!/usr/bin/env python3
import collections,itertools,json,pathlib,time
D=pathlib.Path(__file__).resolve().parent
def main():
    if (D/'RESULT.json').exists():raise SystemExit('one fixed small check already completed')
    start=time.process_time()
    flags=[(p,l) for p in range(1,8) for l in range(1,8) if (p&l).bit_count()%2==0]
    ids={f:i for i,f in enumerate(flags)}
    C=[]
    for p,l in flags:
        byp=sorted(x for x in flags if x[0]==p);byl=sorted(x for x in flags if x[1]==l)
        i=byp.index((p,l));j=byl.index((p,l))
        C.append([ids[byp[(i+1)%3]],ids[byp[(i-1)%3]],ids[byl[(j+1)%3]],ids[byl[(j-1)%3]]])
    inv=[1,0,3,2]
    assert len(C)==21 and all(len(set(row))==4 for row in C)
    assert all(C[C[u][p]][inv[p]]==u for u in range(21) for p in range(4))
    dhist=collections.Counter();wordhist=collections.Counter();positive=[];first=None
    for u in range(21):
        dist=[-1]*21;dist[u]=0;queue=collections.deque([u])
        while queue:
            a=queue.popleft()
            for b in C[a]:
                if dist[b]<0:dist[b]=dist[a]+1;queue.append(b)
        words=collections.defaultdict(list)
        for p,a in enumerate(C[u]):
            for q,b in enumerate(C[a]):
                for r,v in enumerate(C[b]):words[v].append({'vertices':[u,a,b,v],'ports':[p,q,r]})
        for v,d in enumerate(dist):
            dhist[d]+=1
            if d==3:
                n=len(words[v]);wordhist[n]+=1
                positive.append([u,v,n])
                if first is None:first={'u':u,'v':v,'source_flag':flags[u],'target_flag':flags[v],'words':words[v]}
    triangles=[list(t) for t in itertools.combinations(range(21),3)
               if all(b in C[a] for a,b in itertools.combinations(t,2))]
    assert dhist=={0:21,1:84,2:168,3:168} and wordhist=={2:168}
    assert len(triangles)==14
    controller={'flags':[list(f) for f in flags],'controller':C,'inverse_ports':inv,
                'degree':4,'undirected_edges':42,'triangles':triangles,
                'ordered_distance_histogram':dict(dhist),'distance3_length3_word_count_histogram':dict(wordhist),
                'all_distance3_pair_word_counts':positive,'first_witness':first}
    (D/'CONTROLLER.json').write_text(json.dumps(controller,indent=2)+'\n')
    pts=list(itertools.product(range(5),repeat=2))
    normals=[(1,0)]+[(a,1) for a in range(5)]
    lines={(i,k):sum(1<<(x+5*y) for x,y in pts if (n[0]*x+n[1]*y)%5==k)
           for i,n in enumerate(normals) for k in range(5)}
    crosses=[]
    for i,j in itertools.combinations(range(6),2):
        for a,b in itertools.product(range(5),repeat=2):
            mask=lines[i,a]|lines[j,b]
            assert mask.bit_count()==9
            crosses.append({'normal1':normals[i],'offset1':a,'normal2':normals[j],'offset2':b,'mask':mask})
    assert len(crosses)==375 and len({c['mask'] for c in crosses})==375
    ihist=collections.Counter();minimum=26;minpair=None;pairs=0
    for i,a in enumerate(crosses):
        for j in range(i,len(crosses)):
            b=crosses[j];mask=a['mask']&b['mask'];n=mask.bit_count()
            ihist[n]+=1;pairs+=1
            if n<minimum:
                minimum=n;minpair={'first':a,'second':b,'intersection_labels':[k for k in range(25) if mask>>k&1]}
    assert pairs==70500 and minimum==1
    (D/'CROSS_CHECK.json').write_text(json.dumps({'crosses':375,'all_unordered_pairs_including_self':pairs,
       'minimum_intersection':minimum,'intersection_histogram':dict(ihist),'minimum_witness':minpair},indent=2)+'\n')
    elapsed=time.process_time()-start;assert elapsed<10
    result={'status':'PREDICTION_SUPPORTED_UNIFORM100_RULE_EXCLUDED_BY_TWO_WORD_CAPACITY',
            'control_vertices':21,'control_distance3_ordered_pairs':168,'every_distance3_pair_words':2,
            'affine_crosses':375,'cross_pairs_checked':pairs,'minimum_cross_intersection':minimum,
            'rank3_word_points_per_retained_normal_plane':16,'rank_at_most2_word_slice_upper':5,
            'CPU_seconds':elapsed,'CPU_budget_seconds':10,'workers':1,'solver_calls':0,'large_graphs_generated':0,
            'large_graph_BFS':0,'plane_choices_enumerated':0,
            'scope':'Fixed Fano flag C21, one affine plane deleted per fiber, all edge noises transverse to target plane; no exclusion of general C21 retention or non-affine/nonuniform/chart-noise changes.'}
    (D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    (D/'TERMINAL.json').write_text(json.dumps({'running':False,'status':'COMPLETE','CPU_seconds':elapsed,'solver_calls':0,'large_graphs_generated':0},indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
