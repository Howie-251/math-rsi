"""Fresh read-only T63 certificate audit; writes only its review evidence JSON."""
from pathlib import Path
from itertools import combinations, permutations
import hashlib, json
ROOT = Path(__file__).resolve().parent
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def matchings(xs):
    if not xs:
        yield ()
    else:
        a, *rest = xs
        for j, b in enumerate(rest):
            for tail in matchings(rest[:j] + rest[j+1:]):
                yield ((a,b),) + tail
def parity(x): return bin(x).count('1') % 2
def short(a,b): return a ^ b in (1,2,4,8)
verts = set(range(16))
even = sorted(x for x in verts if not parity(x))
odd = verts - set(even)
manifest = json.loads((ROOT/'A8_Q4_T63_manifest.json').read_text())
source_names = ['A8_Q4_T63_CLASSIFICATION.md','A8_DOUBLE_BRIDGE_SUFFICIENT.md',
 'A8_THREE_BRIDGE_SUFFICIENT.md','A8_PARTIAL_PROOF_PACKAGE.md',
 'Q4_T15_CLASSIFICATION.md','Q4_GENERAL_AUGMENTATION.md',
 'A8_Q4_T63_manifest.json','A8_Q4_T63_verify.py','A8_Q4_T63_verified.json']
source_names += [r['file'] for r in manifest['rows']]
hashes = {n:digest(ROOT/n) for n in source_names}
full_domain = {(h,u) for h in combinations(even,6) for u in combinations(h,3)}
owner = {}
rows = []
for row in manifest['rows']:
    holes, avoided = set(row['holes']), set(row['forbidden'])
    assert len(holes)==6 and holes <= set(even) and len(avoided)==3 and avoided <= holes
    covered = sorted(verts-holes)
    universe = set(matchings(covered))
    assert len(universe)==945
    seen = set()
    raw = (ROOT/row['file']).read_bytes()
    assert len(raw)==29*945
    yes = no = 0
    obstruction_edges = set()
    for offset in range(0,len(raw),29):
        mate, sequence = raw[offset:offset+16], list(raw[offset+16:offset+29])
        assert all(mate[x]==255 for x in holes)
        assert all(mate[x] in covered and mate[x]!=x and mate[mate[x]]==x for x in covered)
        edges = tuple((x,mate[x]) for x in covered if x<mate[x])
        assert edges in universe and edges not in seen
        seen.add(edges)
        ob = []
        for a in odd:
            neighbors = [a^(1<<i) for i in range(4) if a^(1<<i) not in avoided]
            if len(neighbors)==1 and mate[a]==neighbors[0]:
                ob.append(tuple(sorted((a,neighbors[0]))))
        if sequence==[255]*13:
            assert ob
            obstruction_edges.update(ob)
            no += 1
        else:
            assert not ob
            assert len(sequence)==len(set(sequence))==13 and set(sequence)==verts-avoided
            adjacency = {x:set() for x in sequence}
            for i,x in enumerate(sequence):
                y=sequence[(i+1)%13]
                adjacency[x].add(y); adjacency[y].add(x)
                assert mate[x]==y or short(x,y)
            assert all(len(adjacency[x])==2 for x in sequence)
            assert all(mate[x] in adjacency[x] for x in covered)
            yes += 1
    assert seen==universe
    orbit = set()
    for perm in permutations(range(4)):
        # A different implementation of bit permutation; then translate.
        mapped = {x:sum(((x>>perm[i])&1)<<i for i in range(4)) for x in verts}
        for translation in even:
            orbit.add((tuple(sorted(mapped[x]^translation for x in holes)),
                       tuple(sorted(mapped[x]^translation for x in avoided))))
    assert len(orbit)==row['orbit']
    for geometry in orbit:
        assert geometry not in owner
        owner[geometry]=row['file']
    assert (yes,no)==(row['positive'],row['negative'])
    rows.append({'file':row['file'],'orbit':len(orbit),'positive':yes,'negative':no,
                 'negative_obstruction_edges':sorted(obstruction_edges)})
assert set(owner)==full_domain and len(owner)==560
# Check both numerical parities: translation by 1 is a bijection.
odd_domain = {(tuple(sorted(x^1 for x in h)),tuple(sorted(x^1 for x in u))) for h,u in full_domain}
assert len(odd_domain)==560 and not full_domain & odd_domain
# The concrete fourth residual geometry; no assumptions on required-edge lengths.
H={0,15,23,27,29,1,2,4}
cuts=[]
for bit in (8,16):
    A={x for x in range(32) if not x&bit}; B=set(range(32))-A
    ha=H&A; hb=H&B
    minority={x for x in ha if parity(x)}
    majority={x for x in ha if not parity(x)}
    assert minority=={1,2,4} and len(majority)==2
    bridges={x^bit for x in minority}
    assert bridges <= B-H and len(hb)==3 and all(not parity(x) for x in hb)
    common={a for a in B if all((a^w) in (1,2,4,8,16) for w in bridges)}
    assert common=={bit}
    remaining={bit^(1<<i) for i in range(5) if (1<<i)!=bit}-bridges
    assert remaining=={24}
    cuts.append({'bit':bit,'bridges':sorted(bridges),'obstruction_edge':[bit,24]})
assert len({24,8,16})==3  # Edges 8--24 and 16--24 conflict in every matching.
assert hashes=={n:digest(ROOT/n) for n in source_names}, 'Input changed during audit'
result={'status':'PASS','geometry_even':560,'geometry_odd':560,'orbits':7,
 'matching_records':sum(r['positive']+r['negative'] for r in rows),
 'positive':sum(r['positive'] for r in rows),'analytic_negative':sum(r['negative'] for r in rows),
 'rows':rows,'fourth_orbit_cuts':cuts,'audited_input_hashes':hashes,
 'review_checker_sha256':digest(Path(__file__))}
(ROOT/'A8_BRIDGE_INPUTS_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('rows','audited_input_hashes')},indent=2))
