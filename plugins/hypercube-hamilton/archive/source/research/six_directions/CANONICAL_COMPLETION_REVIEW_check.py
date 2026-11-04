"""Independent exhaustive audit. No imports from generator or primary checker."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import hashlib, json, math

ROOT = Path(__file__).resolve().parent
ODD = tuple(x for x in range(16) if x.bit_count() % 2)

def edge(a,b): return tuple(sorted((a,b)))
def edges(m): return frozenset((a,b) for a,b in enumerate(m) if a < b < 16)
def matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for j in range(1,len(vertices)):
        b = vertices[j]
        for rest in matchings(vertices[1:j]+vertices[j+1:]):
            yield ((a,b),)+rest

def negative_histogram(f, vertices):
    # Every cycle containing the perfect matching f has a complementary
    # perfect matching of short edges disjoint from f. Enumerate it directly.
    hist = Counter()
    def rec(left, chosen):
        if not left:
            adj = {a:[] for a in vertices}
            for a,b in tuple(f)+chosen:
                adj[a].append(b); adj[b].append(a)
            assert all(len(v)==2 for v in adj.values())
            todo=set(vertices); count=0
            while todo:
                count+=1; stack=[todo.pop()]
                while stack:
                    for b in adj[stack.pop()]:
                        if b in todo: todo.remove(b); stack.append(b)
            hist[count]+=1
            return
        a=min(left)
        for bit in range(4):
            b=a^(1<<bit)
            if b in left and edge(a,b) not in f:
                rec(left-{a,b},chosen+(edge(a,b),))
    rec(set(vertices),())
    assert not hist[1]
    return dict(sorted(hist.items()))

def check_table(hole):
    filename=ROOT/f'q4_distance{hole.bit_count()}_avoided_table.bin'
    raw=filename.read_bytes()
    assert len(raw)==135135*30
    seen=set(); bad=set(); half=0; histograms=[]
    vertices=set(range(16))-{0,hole}
    for pos in range(0,len(raw),30):
        m=raw[pos:pos+16]; cycle=raw[pos+16:pos+30]
        assert m not in seen; seen.add(m)
        assert {a for a in range(16) if m[a]==255}=={0,hole}
        assert all(m[a] in vertices and m[a]!=a and m[m[a]]==a for a in vertices)
        f=edges(m)
        assert len(f)==7
        if cycle==bytes([255])*14:
            histograms.append(negative_histogram(f,vertices))
            bad.add(m)
            layers=[]
            for bit in range(4):
                for parity in range(2):
                    layer={edge(a,a^(1<<bit)) for a in range(16)
                           if not a&(1<<bit) and a.bit_count()%2==parity}
                    if layer<=f: layers.append((bit,parity))
            half+=bool(layers)
        else:
            assert set(cycle)==vertices and len(cycle)==len(set(cycle))
            ce={edge(cycle[i],cycle[(i+1)%14]) for i in range(14)}
            assert len(ce)==14 and f<=ce
            assert all((a^b).bit_count()==1 for a,b in ce-f)
    # Valid unique involutions and the exact 13!! cardinality prove coverage.
    assert len(seen)==math.prod(range(1,14,2))
    return bad, {'records':len(seen),'positive':len(seen)-len(bad),
                 'negative':len(bad),'half_layer_negatives':half,
                 'nonhalf_negatives':len(bad)-half,'negative_histograms':histograms,
                 'sha256':hashlib.sha256(raw).hexdigest()}

def main():
    base={}; tables={}
    for hole in (1,7):
        base[hole],tables[hole]=check_table(hole)
        print('verified table',hole,tables[hole]['negative'],flush=True)
    bad={}
    for y in ODD:
        perm=tuple(i for i in range(4) if y&(1<<i))+tuple(i for i in range(4) if not y&(1<<i))
        def trans(x): return sum(1<<perm[i] for i in range(4) if x&(1<<i))
        values=set()
        for m in base[1 if y.bit_count()==1 else 7]:
            n=bytearray([255]*16)
            for a,b in enumerate(m):
                if b!=255:n[trans(a)]=trans(b)
            assert n[y]==255 and n[0]==255
            values.add(bytes(n))
        bad[y]=values
    def fails(m,d,y):
        if d==y:return True
        k=m[y]; n=bytearray(m)
        n[y]=255; n[d]=k; n[k]=d
        return bytes(n) in bad[y]
    stalled=[]; count=0; byroot=Counter()
    # Independent forward scan of ALL near-perfect local inputs.
    for d in range(1,16):
        for f in matchings(tuple(x for x in range(1,16) if x!=d)):
            count+=1; m=bytearray([255]*16)
            for a,b in f:m[a]=b;m[b]=a
            if fails(m,d,7) and fails(m,d,11):
                stalled.append((d,bytes(m),frozenset(f)));byroot[d]+=1
    assert count==2027025 and len(stalled)==256
    print('forward near-perfect scan',count,'stalls',len(stalled),flush=True)
    levels=[]
    for c in range(1,16,2):
        size=(15-c)//2; counts=Counter()
        for d,m,f in stalled:
            for sub in combinations(sorted(f),size):counts[frozenset(sub)]+=1
        total=c*math.prod(range(1,c-1,2))
        partials=[f for f,n in counts.items() if n==total]
        results=[]
        for f in partials:
            ports=tuple(sorted(set(range(1,16))-{a for e in f for a in e}))
            assert len(ports)==c
            available=Counter(); completions=0
            # Fresh forward enumeration for every partial, rather than inverse
            # counts from any stored negative list of transformed originals.
            for d in ports:
                for extra in matchings(tuple(a for a in ports if a!=d)):
                    m=bytearray([255]*16)
                    for a,b in tuple(f)+extra:m[a]=b;m[b]=a
                    completions+=1
                    for y in ODD:
                        if not fails(m,d,y):available[y]+=1
            assert completions==total
            assert not available[7] and not available[11]
            good=tuple(y for y in ODD if available[y])
            if c in (1,3):assert len(good)>=4
            if c in (5,7):
                assert len(good)==4 and not set(good)&set(ports)
                assert all(available[y]==total for y in good)
            results.append({'matching':sorted(f),'ports':ports,'good':good,
                            'available_completions':dict(available)})
        levels.append({'crossings':c,'stalls':len(partials),'completions':total,
                       'candidate_partials':len(counts),
                       'good_histogram':dict(Counter(len(x['good']) for x in results)),
                       'results':results})
        print('level',c,'stalls',len(partials),flush=True)
    assert [x['stalls'] for x in levels]==[256,210,42,2,0,0,0,0]
    assert [x['candidate_partials'] for x in levels]==[256,1372,3048,3596,2366,808,84,1]
    h1=frozenset(((2,3),(4,5),(8,9),(14,15)))
    h2=frozenset(((1,3),(4,6),(8,10),(13,15)))
    c7={frozenset(map(tuple,x['matching'])) for x in levels[3]['results']}
    assert c7=={h1,h2}
    for item in levels[2]['results']:
        f=frozenset(map(tuple,item['matching']))
        assert (h1<=f) != (h2<=f)
    output={'status':'PASS','scope':'Independent deterministic finite lemma checks; semantic gluing reviewed separately',
            'tables':tables,'near_perfect_inputs':count,'near_perfect_stalls':len(stalled),
            'stalls_by_root':dict(byroot),'levels':levels,
            'residual_original_full_matching_counts':{'c5':42*math.comb(9,1)*105*120,
                                                    'c7':2*math.comb(9,3)*15*5040},
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'CANONICAL_COMPLETION_REVIEW_check.json').write_text(json.dumps(output,indent=2)+'\n')
    print('PASS',flush=True)

if __name__=='__main__':main()
