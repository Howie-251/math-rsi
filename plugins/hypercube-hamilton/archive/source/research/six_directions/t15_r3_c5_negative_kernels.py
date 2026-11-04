"""Inverse multiplicities for occupied bridges at c5; candidate reductions."""
import itertools,json,collections
from pathlib import Path
R=Path(__file__).resolve().parent
edge=lambda a,b:tuple(sorted((a,b)))
def main():
    generation=json.loads((R/'q4_balanced_two_avoided_generation.json').read_text());neg={}
    for row in generation['rows']:
        r,y=row['avoided'];data=(R/f'q4_balanced_two_avoided_{r}_{y}.bin').read_bytes();base=[]
        for i in range(0,len(data),30):
            if data[i+16:i+30]==bytes([255])*14:
                m=data[i:i+16];base.append(frozenset((a,m[a]) for a in range(16) if a<m[a]<16))
        for perm0 in itertools.permutations(range(3)):
            p=perm0+(3,)
            def tr(v):return sum(((v>>j)&1)<<p[j] for j in range(4))
            key=(tr(r),tr(y));vals={frozenset(edge(tr(a),tr(b)) for a,b in f) for f in base}
            if key in neg:assert neg[key]==vals
            neg[key]=vals
    reports=[]
    for core,r,s,y in [(0,3,5,1),(5,3,6,1),(8,3,15,1),(15,10,15,1),(23,3,5,8),(26,3,15,8),(27,6,15,8)]:
        fs=[];tables=[]
        for z in (r,s):
            counts=collections.Counter()
            for L in neg[z,y]:
                for Q in itertools.combinations(sorted(L),2):
                    F=L-set(Q);ports=tuple(sorted({z,*[v for e in Q for v in e]}))
                    counts[ports,tuple(sorted(F))]+=1
            # Occupied quotient has at least two realizable of the three pairings.
            bad={k:n for k,n in counts.items() if n>=2}
            tables.append(dict(bridge=z,negatives=len(neg[z,y]),
                inverse_multiplicity_histogram=dict(collections.Counter(counts.values())),
                at_least_two_bad_quotients=[dict(ports=p,matching=f,negative_quotients=n) for (p,f),n in sorted(bad.items())]))
            fs.append(bad)
        both=set(fs[0])&set(fs[1])
        reports.append(dict(core=core,bridges=[r,s],B_omitted=y,tables=tables,
            common_bad=[dict(ports=p,matching=f) for p,f in sorted(both)]))
    out=dict(scope='c5 occupied bridge inverse kernels only; internal bridge and global theorem not claimed',reports=reports,full_t15_proved=False)
    (R/'t15_r3_c5_negative_kernels.json').write_text(json.dumps(out,indent=2)+'\n')
    for r in reports:print(r['core'],[(t['bridge'],t['inverse_multiplicity_histogram'],len(t['at_least_two_bad_quotients'])) for t in r['tables']],'common',len(r['common_bad']))
if __name__=='__main__':main()
