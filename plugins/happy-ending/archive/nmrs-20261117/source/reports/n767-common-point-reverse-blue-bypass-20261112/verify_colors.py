"""Independent literal-color verifier. No imports from the generator/solver."""
from pathlib import Path
import hashlib, itertools, json, platform, socket, sys
ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'case-003'/'witness.json'
def main():
    raw=INPUT.read_bytes(); witness=json.loads(raw)
    col={tuple(item['vertices']):item['color'] for item in witness['colors']}
    n=13; vertices=range(n); expected=set(itertools.combinations(vertices,3))
    assert len(witness['colors'])==len(expected)==286 and set(col)==expected
    assert set(col.values())<={'R','B'}
    packet_bad=[]
    for packet in itertools.combinations(vertices,4):
        word=[col[t] for t in itertools.combinations(packet,3)]
        if sum(word[j]!=word[j-1] for j in range(1,4))>1: packet_bad.append(packet)
    # Bitmask enumeration visits every induced vertex subset exactly once.
    paths={c:[] for c in 'RB'}
    subset_count=0
    for mask in range(1<<n):
        sequence=tuple(v for v in vertices if mask&(1<<v))
        if len(sequence)<2: continue
        subset_count+=1
        windows=list(zip(sequence,sequence[1:],sequence[2:]))
        for c in 'RB':
            if all(col[t]==c for t in windows): paths[c].append(sequence)
    lengths={}
    for a,b in itertools.combinations(vertices,2):
        lengths[a,b]={c:{len(p) for p in paths[c] if p[0]==a and p[-1]==b} for c in 'RB'}
    forbidden_weak=[dict(endpoints=edge,R=r,B=b) for edge,cs in lengths.items() for r in cs['R'] for b in cs['B'] if r+b==9]
    red6=sorted(p for p in paths['R'] if len(p)==6)
    diag1=[p for p in red6 if (p[0],p[-1])==(0,12)]
    diag2=[p for p in red6 if (p[0],p[-1])==(1,11)]
    survivors=[p for p in red6 if 3 not in p]
    blue5=[p for p in paths['B'] if len(p)==5 and (p[0],p[-1])==(1,12)]
    edges=sorted({(p[0],p[-1]) for p in red6})
    after=sorted({(p[0],p[-1]) for p in survivors})
    def matching_number(edges):
        return max([0]+[k for k in range(1,len(edges)+1) if any(len({e[0] for e in s})==k and len({e[1] for e in s})==k for s in itertools.combinations(edges,k))])
    checks=dict(complete_color_table=True,packet_valid=not packet_bad,
        no_R7=not any(len(p)>=7 for p in paths['R']),no_B6=not any(len(p)>=6 for p in paths['B']),
        no_same_endpoint_weak7=not forbidden_weak,actual_diagonals=bool(diag1 and diag2),
        every_diagonal_R6_has_internal_x=all(3 in p[1:-1] for p in diag1+diag2),
        actual_forward_bypass=any((p[0],p[-1])==(0,11) for p in survivors),actual_reverse_B5=bool(blue5),
        all_R6_edges_exactly_three=set(edges)=={(0,11),(0,12),(1,11)},
        matching_drops_2_to_1=matching_number(edges)==2 and matching_number(after)==1,
        deletion_leaves_exactly_one_R6=len(survivors)==1,
        reverse_B5_also_survives_delete_x=any(3 not in p for p in blue5),
        original_enumeration_matches=red6==sorted(map(tuple,witness['R6'])) and all(sorted(paths[c])==sorted(map(tuple,witness['all_paths'][c])) for c in 'RB'))
    result=dict(all_checks_pass=all(checks.values()),checks=checks,host=socket.gethostname(),platform=platform.platform(),
      python=sys.executable,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=hashlib.sha256(raw).hexdigest(),
      points=n,triples=len(col),packets=715,nontrivial_subsets_enumerated=subset_count,
      path_counts={c:len(paths[c]) for c in 'RB'},longest={c:max(map(len,paths[c])) for c in 'RB'},
      diagonal_1_R6=diag1,diagonal_2_R6=diag2,all_R6=red6,after_delete_x_R6=survivors,
      reverse_B5=blue5,endpoint_edges=edges,after_delete_x_edges=after,
      matching_before=matching_number(edges),matching_after=matching_number(after),
      all_same_endpoint_length_sets=[dict(endpoints=e,**{c:sorted(s) for c,s in cs.items()}) for e,cs in lengths.items()],
      forbidden_weak7=forbidden_weak,packet_violations=packet_bad)
    (ROOT/'independent-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'colors.tsv').write_text('i\tj\tk\tcolor\n'+''.join('%d\t%d\t%d\t%s\n'%(*t,col[t]) for t in sorted(col)))
    print(json.dumps({k:result[k] for k in ('all_checks_pass','checks','path_counts','longest','diagonal_1_R6','diagonal_2_R6','after_delete_x_R6','reverse_B5')}))
    return 0 if result['all_checks_pass'] else 1
if __name__=='__main__': sys.exit(main())
