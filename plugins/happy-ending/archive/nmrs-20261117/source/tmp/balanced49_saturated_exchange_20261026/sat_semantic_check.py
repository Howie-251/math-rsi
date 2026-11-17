"""Independent exact semantic checker from complete triple colors, no search."""
from itertools import combinations


def check(names, colors, frozen_h, required):
    n=len(names)
    packets=0
    for a,b,c,d in combinations(range(n),4):
        bits=[colors[a,b,c],colors[a,b,d],colors[a,c,d],colors[b,c,d]]
        assert sum(x!=y for x,y in zip(bits,bits[1:]))<=1, ('packet',a,b,c,d)
        packets+=1
    maxima={c:{} for c in [False,True]}
    six=[]
    subsets=0
    for size in range(2,n+1):
        for path in combinations(range(n),size):
            subsets+=1
            for color in [False,True]:
                local=all(colors[path[i],path[i+1],path[i+2]]==color for i in range(size-2))
                full=all(colors[t]==color for t in combinations(path,3))
                assert local==full, ('closure',path,color)
                if not local: continue
                pair=path[0],path[-1]
                maxima[color][pair]=max(size,maxima[color].get(pair,0))
                assert size<(7 if color else 6), ('forbidden path',path,color)
                if color and size==6:
                    assert path[0] not in frozen_h, ('H-origin R6',path)
                    six.append([names[x] for x in path])
    for pair in combinations(range(n),2):
        assert maxima[True][pair]+maxima[False][pair]<=8, ('weak7',pair)
    for path in required:
        assert all(colors[t] for t in combinations(path,3)), ('required',path)
    return {'status':'PASS','packets':packets,'subsets_size_ge2':subsets,
            'max_R':max(maxima[True].values()),'max_B':max(maxima[False].values()),
            'max_same_endpoint_sum':max(maxima[True][p]+maxima[False][p] for p in maxima[True]),
            'frozen_H':[names[x] for x in sorted(frozen_h)],'R6':six,
            'all_H_ambient_R6_sources_absent':True,'specified_paths_red':True,
            'endpoint_rows':[{'endpoints':[names[x] for x in p],'R':maxima[True][p],
                              'B':maxima[False][p]} for p in combinations(range(n),2)]}
