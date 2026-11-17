"""Independent fixed-object arithmetic and direct-import binding checker.
Does not run any author program, Hamilton search, or matching-family enumeration.
"""
import hashlib, json
from pathlib import Path
P=Path(__file__).resolve().parent
def read(n): return json.loads((P/n).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def edge(a,b): return tuple(sorted((a,b)))
def norm(es): return {edge(*e) for e in es}
def par(x): return x.bit_count()%2
def short(a,b): return (a^b).bit_count()==1
def reconstruct(base,vs,e,g,dirs):
    es={edge(x,x^base) for x in range(64) if not x&base}
    for x in [0,3]: es.remove(edge(x,x^base))
    for v in vs:
        for x in [v,v^e,v^e^g]: es.remove(edge(x,x^base))
        es|={edge(v,v^e),edge(v^e^base,v^e^g^base)}
    swaps=[]
    for d in dirs:
        choices=sorted((x,x^d) for x in range(64) if not x&base and x<(x^d) and edge(x,x^base) in es and edge(x^d,x^d^base) in es)
        x,y=choices[0]; swaps.append([x,y])
        es-={edge(x,x^base),edge(y,y^base)}
        es|={edge(x,y),edge(x^base,y^base)}
    return es,swaps
def facts(es):
    ends=[v for e in es for v in e]
    assert len(ends)==len(set(ends)) and all(short(*e) for e in es)
    holes=set(range(128))-set(ends)
    counts=[sum(a^b==1<<k for a,b in es) for k in range(7)]
    he=sorted(edge(a,b) for a in holes for b in holes if a<b and short(a,b))
    local=[{x-64*f for x in holes if x//64==f} for f in range(2)]
    internal=[{e for e in es if all(v//64==f for v in e)} for f in range(2)]
    fc=[[sum(a^b==1<<k for a,b in internal[f]) for k in range(6)] for f in range(2)]
    gates=[]
    for f in range(2):
        O={v for v in local[f] if par(v)}; E=local[f]-O
        for d in [0,3]:
            gates.append([sum((v>>k&1)!=(d>>k&1) for v in O)-sum((v>>k&1)!=(d>>k&1) for v in E) for k in range(6)])
    return dict(size=len(es),direction_counts=counts,hole_edges=he,holes=[sorted(s) for s in local],face_counts=fc,gates=gates)
A,sa=reconstruct(32,[12,24,5,18],1,2,[4,8,16])
B,sb=reconstruct(16,[6,33,34,5],8,2,[1,4,32])
pos=A|{edge(x+64,y+64) for x,y in B}|{(0,64),(3,67)}
w=read('R7_SIGNED_HOLE_MARGIN_WITNESS.json')
assert pos==norm(w['matching'])
fp=facts(pos)
assert fp['size']==54 and fp['direction_counts']==[6,8,4,6,14,14,2]
assert fp['hole_edges']==[(15,79),(50,114)]
assert fp['holes']==[[6,15,17,27,32,35,37,44,50,56],[12,15,16,19,21,22,40,43,49,50]]
assert sa==[[10,14],[1,9],[7,23]] and sb==[[8,9],[32,36],[7,39]]
assert fp['gates'][3][0]==1 and min(min(x) for x in fp['face_counts'])>=2
probe=read('R7_MARGIN_GATE_FIXED_PROBE.json'); pe=norm(probe['edges']); fn=facts(pe)
assert fn['size']==56 and fn['direction_counts']==[18,9,11,5,6,5,2]
assert fn['hole_edges']==[] and fn['gates']==[[-1,-1,-1,-1,-1,-2],[3,3,-1,-1,-1,-2],[5,4,2,2,3,3],[-3,-2,2,2,3,3]]
assert norm(probe['faces']['A']['edges'])|{edge(x+64,y+64) for x,y in probe['faces']['B']['edges']}|{(0,64),(3,67)}==pe
pb=norm(probe['faces']['B']['edges'])
freeB=set(range(64))-{x for e in pb for x in e}
OA={v for v in fn['holes'][0] if par(v)}
assert OA=={1,2,4,8,16} and not OA&freeB
assert {1<<k for k in range(6)}-OA=={32}
res=read('R7_MARGIN_GATE_RESIDUAL_WITNESS.json')
ra={edge(x^3,y^3) for x,y in pb}
re=ra|{edge(x+64,y+64) for x,y in pb}|{(0,64),(3,67)}
assert re==norm(res['edges'])
fr=facts(re)
assert fr['size']==56 and fr['direction_counts']==[8,14,16,4,6,6,2] and not fr['hole_edges']
assert fr['gates']==[[-3,-2,2,2,3,3],[5,4,2,2,3,3],[5,4,2,2,3,3],[-3,-2,2,2,3,3]]
assert not set(fr['holes'][0])&set(fr['holes'][1])
assert (set(range(64))-{x for e in ra for x in e})&freeB=={0,3}
for hs in fr['holes']:
    assert not any(short(h,c) for h in hs if par(h) for c in [0,3])
for f in [fn,fr]:
    assert all(d not in [0,1] for row in f['gates'] for d in row)
    assert [k for k,v in enumerate(f['direction_counts']) if v==2]==[6]
    assert min(min(x) for x in f['face_counts'])>=2
manifest=read('R7_SIGNED_HOLE_MARGIN_INPUTS.json'); bindings={}
for section in ['direct_import_hashes','comparison_hashes','author_artifact_hashes']:
    for n,h in manifest[section].items():
        actual=sha(P/n); assert actual==h.removeprefix('sha256:'),(n,actual,h); bindings[n]=actual
for report,source in [('../six_directions/P6_FULL_REVIEW.json','P6_FULL_CLOSURE.md'),('../six_directions/Q5_A10_FULL_REVIEW.json','Q5_A10_FULL_CLOSURE.md'),('PERFECT_MATCHING_SPLICE_REVIEW.json','PERFECT_MATCHING_SPLICE.md'),('R7_THREE_FREE_PAIRINGS_REVIEW.json','R7_THREE_FREE_PAIRINGS.md')]:
    r=read(report); assert r['verdict']=='PASS'
    assert sha((P/report).parent/source)==r['audited_input_hashes'][source].removeprefix('sha256:')
more=['R7_SIGNED_HOLE_MARGIN_INPUTS.json','R7_MARGIN_GATE_FIXED_PROBE.md','R7_MARGIN_GATE_RESIDUAL_WITNESS.md','R7_MARGIN_GATE_RESIDUAL_WITNESS.json','r7_margin_gate_residual_witness.py','R7_MARGIN_GATE_FIXED_PROBE.json']
for n in more: bindings[n]=sha(P/n)
out=dict(status='PASS',author_programs_executed=False,matching_family_enumeration=False,positive54=fp,original_probe56=fn,transport_residual56=fr,positive54_swaps=[sa,sb],verified_bindings=bindings,old_large_certificates_replayed=False,all_transitive_bindings_rehashed=False)
(P/'R7_SIGNED_HOLE_MARGIN_REVIEW_check.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','bound_files':len(bindings),'sizes':[fp['size'],fn['size'],fr['size']]},ensure_ascii=False))
