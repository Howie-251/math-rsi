"""Verify explicit complements and complete 7! input coverage, independent of C++ search."""
import csv,itertools,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
EV=(3,5,6,9,10,12,15)
def edge(a,b):return tuple(sorted((a,b)))
def decode(s):return [ord(c)-ord('A') if c!='-' else -1 for c in s]
def check_pairing(p,vertices):
    assert len(p)==16
    for a in range(16):
        if a not in vertices:assert p[a]==-1
        else:assert p[a] in vertices and p[p[a]]==a and (a^p[a]).bit_count()==1
def main():
    seen=set();count=0
    with (ROOT/'near_perfect_half_layer_probe.csv').open(newline='',encoding='ascii') as f:
        for row in csv.DictReader(f):
            perm=tuple(decode(row['perm']));assert len(perm)==7 and set(perm)==set(EV) and perm not in seen
            seen.add(perm);a=decode(row['N0']);b=decode(row['N1'])
            check_pairing(a,set(range(16)));check_pairing(b,set(range(2,16)))
            m={edge(2*q,2*q+1) for q in range(16) if q.bit_count()%2 and q!=1}
            m.add((1,3));m|={edge(2*q,2*r+1) for q,r in zip(EV,perm)}
            flat=[q for e in m for q in e];assert len(m)==15 and len(set(flat))==30 and set(flat)==set(range(32))-{0,2}
            assert all(p.bit_count()%2!=q.bit_count()%2 for p,q in m)
            n={edge(2*q,2*a[q]) for q in range(16)}|{edge(2*q+1,2*b[q]+1) for q in range(2,16)}|{(2,3)}
            assert not m&n and all((p^q).bit_count()==1 for p,q in n)
            graph={q:[] for q in range(32)}
            for p,q in m|n:graph[p].append(q);graph[q].append(p)
            assert all(len(graph[q])==(1 if q in (0,1) else 2) for q in graph)
            path=[0]
            while path[-1]!=1:
                options=[q for q in graph[path[-1]] if len(path)==1 or q!=path[-2]]
                assert len(options)==1 and options[0] not in path;path.append(options[0])
            assert len(path)==32;count+=1
    assert seen==set(itertools.permutations(EV)) and count==math.factorial(7)
    result=dict(status='PASS',complete_input_bijections=count,
                scope='one explicitly defined near-perfect B(Q5) family, root0 target1, holes0/2; not all B(Q5), not Q6',
                verification='explicit original matchings and short complement edges; Hamilton connectivity; all 7! permutations present exactly once')
    (ROOT/'half_layer_family_verification.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
