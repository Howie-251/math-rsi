"""Complete independent certificate check, with exhaustive short completions
for each negative. The producer's Hamilton DFS is not trusted for negatives.
"""
import hashlib
import json
import sys
from pathlib import Path
from collections import Counter
ROOT = Path(__file__).resolve().parent
HOLE=int(sys.argv[1]) if len(sys.argv)>1 else 7
assert HOLE in (1,7)

def pairings(n):
    k=1
    for x in range(1,n,2): k*=x
    return k

def negative_check(f):
    even=[x for x in range(16) if x not in (0,HOLE) and x.bit_count()%2==0]
    odd={x for x in range(16) if x not in (0,HOLE) and x.bit_count()%2}
    adj={x:[y for y in sorted(odd) if (x^y).bit_count()==1 and tuple(sorted((x,y))) not in f] for x in even}
    hist=Counter()
    def visit(i,left,h):
        if i==7:
            g={x:set() for x in range(16) if x not in (0,HOLE)}
            for x,y in f|set(h): g[x].add(y);g[y].add(x)
            assert all(len(ns)==2 for ns in g.values())
            unseen=set(g);components=0
            while unseen:
                components+=1;stack=[unseen.pop()]
                while stack:
                    fresh=g[stack.pop()]&unseen;unseen-=fresh;stack.extend(fresh)
            hist[components]+=1
            return
        x=even[i]
        for y in adj[x]:
            if y in left: visit(i+1,left-{y},h+[tuple(sorted((x,y)))])
    visit(0,odd,[])
    assert hist[1]==0
    return dict(sorted(hist.items()))

def main():
    distance=HOLE.bit_count()
    source=ROOT/f'q4_distance{distance}_avoided_table.bin';raw=source.read_bytes()
    assert len(raw)==135135*30
    seen=bytearray(135135);bad=[];good=0
    for offset in range(0,len(raw),30):
        m=raw[offset:offset+16];c=raw[offset+16:offset+30]
        assert {x for x in range(16) if m[x]==255}=={0,HOLE}
        vertices=set(range(16))-{0,HOLE}
        for x in vertices: assert m[x] in vertices and m[x]!=x and m[m[x]]==x
        f={tuple(sorted((x,m[x]))) for x in vertices}
        rest=sorted(vertices);rank=0
        while rest:
            x=rest.pop(0);i=rest.index(m[x]);rank+=i*pairings(len(rest)-1);rest.pop(i)
        assert not seen[rank];seen[rank]=1
        if c==bytes([255])*14:
            hist=negative_check(f)
            half=[]
            for j in range(4):
                for p in range(2):
                    layer={tuple(sorted((x,x^(1<<j)))) for x in range(16) if not x>>j&1 and x.bit_count()%2==p}
                    if layer<=f: half.append([j,p])
            bad.append({'matching':sorted(f),'rank':rank,'half_layers':half,'completion_component_histogram':hist})
        else:
            assert len(set(c))==14 and set(c)==vertices
            edges={tuple(sorted((x,y))) for x,y in zip(c,c[1:]+c[:1])}
            assert len(edges)==14 and f<=edges
            assert all((x^y).bit_count()==1 for x,y in edges-f)
            good+=1
    assert all(seen) and good+len(bad)==135135
    result={'status':'PASS','scope':f'complete Q4 holes0,{HOLE} avoided-circle table',
            'matching_records':135135,'positive':good,'negative':len(bad),
            'half_layer_negatives':sum(bool(x['half_layers']) for x in bad),
            'nonhalf_negatives':sum(not x['half_layers'] for x in bad),'exceptions':bad,
            'table_sha256':hashlib.sha256(raw).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'q5_a4_proved':False,'full_p6_proved':False}
    (ROOT/f'q4_distance{distance}_avoided_table_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','matching_records','positive','negative','half_layer_negatives','nonhalf_negatives']}))
if __name__=='__main__':main()
