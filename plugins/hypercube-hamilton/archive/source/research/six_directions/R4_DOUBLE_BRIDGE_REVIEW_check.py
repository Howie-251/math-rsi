"""Fresh read-only rerun and structural/joint audit; writes review artifacts only."""
import hashlib, itertools, json, sys
from pathlib import Path
R = Path(__file__).resolve().parent
sys.path.insert(0, str(R))
inputs = set()
def read(name):
    inputs.add(name)
    return (R/name).read_bytes()
def load(name):
    return json.loads(read(name))
def rerun(name, replacement, argv=None):
    code = read(name).decode('utf-8')
    for before, after in replacement:
        assert before in code
        code = code.replace(before, after)
    old = sys.argv
    sys.argv = [str(R/name), *(argv or [])]
    try:
        exec(compile(code, str(R/name), 'exec'), {'__file__':str(R/name),'__name__':'__main__'})
    finally:
        sys.argv = old
def matching(edges):
    e = frozenset(tuple(sorted(x)) for x in edges)
    vs = [v for x in e for v in x]
    assert len(e) == len(edges) and len(set(vs)) == len(vs)
    assert all(0 <= a < b < 16 for a,b in e)
    return e
rerun('verify_q4_three_avoided_all.py', [('q4_three_avoided_all_verification.json','R4_DOUBLE_BRIDGE_REVIEW_q4_check.json')])
catalogue = load('q4_three_avoided_all_generation.json')
for row in catalogue['rows']:
    read(row['file'])
read('verify_q4_three_avoided.py')
data = {}
for s,t in ((3,5),(3,15),(6,10),(6,15)):
    rerun('verify_r4_inverse_blockers.py', [("f'r4_inverse_blockers_{s}_{t}_{y}_verification.json'", "f'R4_DOUBLE_BRIDGE_REVIEW_inverse_{s}_{t}_{y}.json'")], list(map(str,(s,t,1))))
    source = load(f'r4_boundary_blocking_{s}_{t}_1.json')
    assert source['bridges'] == [s,t] and source['B_omitted'] == 1
    assert {(r['c'],r['mode']) for r in source['reports']} == set(itertools.product(range(4,13,2), ('distinct','paired','s_port','t_port','ports')))
    assert len(source['reports']) == 25
    for row in source['reports']:
        for item in row['items']:
            F = matching(item['matching'])
            assert item['bad_outputs']
            vs = {v for e in F for v in e}
            assert not vs & {0,1}
            mode = row['mode']
            assert ((s in vs,t in vs) == {'distinct':(True,True),'paired':(True,True),'s_port':(False,True),'t_port':(True,False),'ports':(False,False)}[mode])
            if mode == 'paired': assert (s,t) in F
            if mode == 'distinct': assert (s,t) not in F
    data[s,t] = source

# Enumerate every marked coordinate permutation carrying each actual bridge
# pair to any saved canonical pair, and require identical transported null sets.
joint = load('r4_joint_blocking_check.json')
actual = {(row['core'],row['c']):row for row in joint['reports']}
assert len(actual) == len(joint['reports']) == 15
summaries = []
for core, bridges in ((1,(3,5,9)),(4,(3,5,15)),(24,(6,10,15))):
    nullsets = []
    for a,b in itertools.combinations(bridges,2):
        images = []
        for p in itertools.permutations(range(4)):
            tr = lambda v: sum(((v>>j)&1)<<p[j] for j in range(4))
            if tr(1) != 1: continue
            st = tuple(sorted((tr(a),tr(b))))
            if st not in data: continue
            inv = {tr(v):v for v in range(16)}
            ns = {c:set() for c in range(4,13,2)}
            for row in data[st]['reports']:
                ns[row['c']].update(frozenset(tuple(sorted((inv[u],inv[v]))) for u,v in item['matching']) for item in row['items'] if item['blocking_pairing'] is None)
            images.append(ns)
        assert images and all(image == images[0] for image in images)
        nullsets.append(images[0])
    for c in range(4,13,2):
        expected = set.intersection(*(ns[c] for ns in nullsets))
        row = actual[core,c]
        observed = {matching(edges) for edges in row['matchings']}
        assert expected == observed and len(observed) == len(row['matchings']) == row['unresolved']
        summaries.append({'core':core,'c':c,'residual_count':len(expected)})
for name in ('R4_DOUBLE_BRIDGE_BLOCKING.md','r4_boundary_blocking_probe.py','r3_boundary_blocking_probe.py','r4_joint_blocking_check.py','q4_three_avoided_all_verification.json'):
    read(name)
out = {'status':'PASS','review_independence':'same-family','acceptance_status':'provisional','joint_residuals':summaries,'audited_input_hashes':{name:hashlib.sha256((R/name).read_bytes()).hexdigest() for name in sorted(inputs)}}
(R/'R4_DOUBLE_BRIDGE_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k != 'audited_input_hashes'}))
