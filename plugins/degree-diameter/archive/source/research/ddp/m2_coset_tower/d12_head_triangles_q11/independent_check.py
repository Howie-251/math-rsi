"""One q11 saved graph: independent edges and proof-supported three-orbit BFS.

No producer arithmetic tables, distance caches, or other sample graphs are read.
This deliberately does not run full-source BFS on all 43923 vertices.
"""
import json
import time
from collections import Counter, deque
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
STEM = OUT/'profile.best'
saved = json.loads(Path(str(STEM)+'.json').read_text())
Q, J, A, K = 11, 10, 363, 110
L, B, H, N, M = 39930, 3630, 363, 43923, 263538
BS, HS = L, L+B
S = set(saved['S'])
assert len(S) == len(saved['S']) == 11 and 0 not in S
assert all(0 < s < L for s in S)
pw = [pow(2,j,Q) for j in range(J)]
assert len(set(pw)) == J

def enc(u,v,w):
    return u % Q + Q*(v % Q) + Q*Q*(w % 3)

def dec(x):
    return x % Q, x//Q % Q, x//(Q*Q)

def add(x,y):
    u,v,w = dec(x)
    a,b,c = dec(y)
    return enc(u+a,v+b,w+c)

def neg(x):
    u,v,w = dec(x)
    return enc(-u,-v,-w)

def kp(k,l):
    b,j = k % Q, k//Q
    d,t = l % Q, l//Q
    return (b+pw[2*j % J]*d) % Q + Q*((j+t) % J)

def ki(k):
    b,j = k % Q, k//Q
    return -pw[-2*j % J]*b % Q + Q*(-j % J)

def act(k,x):
    b,j = k % Q, k//Q
    u,v,w = dec(x)
    return enc(pw[3*j % J]*u+b*pw[j]*v,pw[j]*v,w)

# Independent arithmetic tables, built only from the displayed field formulas.
acts = [[act(k,x) for x in range(A)] for k in range(K)]
adds = [[add(x,y) for y in range(A)] for x in range(A)]
kps = [[kp(k,l) for l in range(K)] for k in range(K)]
kis = [ki(k) for k in range(K)]

def gp(g,h):
    x,k = g % A,g//A
    y,l = h % A,h//A
    return adds[x][acts[k][y]]+A*kps[k][l]

def gi(g):
    x,k = g % A,g//A
    return neg(acts[kis[k]][x])+A*kis[k]

assert {gi(s) for s in S} == S
assert all(gp(s,gi(s)) == gp(gi(s),s) == 0 for s in S)
# These additive maps are determined by the two F11 basis vectors and C3 basis.
for k in range(K):
    assert kps[k][kis[k]] == kps[kis[k]][k] == 0
    for l in range(K):
        assert all(acts[kps[k][l]][x] == acts[k][acts[l][x]] for x in (1,Q,Q*Q))

def require(condition,stage,details):
    if not condition:
        Path(str(STEM)+'.independent_mismatch.json').write_text(json.dumps({
            'status':'STOPPED_AT_MISMATCH_NO_RERUN','stage':stage,'details':details},indent=2)+'\n')
        raise AssertionError(stage)

expected = set()
for g in range(L):
    for s in S:
        h = gp(g,s)
        assert g != h
        if g < h:
            expected.add((g,h))
    x,k = g % A,g//A
    expected.add((g,BS+x+A*(k//Q)))
for j in range(J):
    for x in range(A):
        expected.add((BS+x+A*j,HS+x))
triangles = set()
for u in range(Q):
    for v in range(Q):
        t = [HS+enc(u,v,w) for w in range(3)]
        triangles.update((t[i],t[j]) for i,j in ((0,1),(0,2),(1,2)))
assert len(triangles) == 363
expected |= triangles
assert len(expected) == M
build_cpu = time.process_time()-START

tokens = list(map(int,Path(str(STEM)+'.edges').read_text().split()))
n,m = tokens[:2]
assert (n,m) == (N,M) and len(tokens) == 2+2*m
edges = [tuple(sorted(e)) for e in zip(tokens[2::2],tokens[3::2])]
actual = set(edges)
assert len(actual) == m and all(0 <= u < v < n for u,v in edges)
require(actual == expected,'independent_edge_set',{
    'missing_expected':sorted(expected-actual),'unexpected_saved':sorted(actual-expected)})
assert {e for e in actual if e[0] >= HS} == triangles
adj = [[] for _ in range(N)]
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)
assert set(map(len,adj)) == {12}

# Left (z,k0) acts on a head x by z+k0*x. K fixes the C3 coordinate;
# equal (u,v) and distinct w therefore remain a head-triangle edge.
# Verify all K actions on all head edges, and the three A basis translations.
head_action_edge_checks = 0
for k in range(K):
    for u,v in triangles:
        image = tuple(sorted((HS+acts[k][u-HS],HS+acts[k][v-HS])))
        assert image in triangles
        head_action_edge_checks += 1
for z in (1,Q,Q*Q):
    for u,v in triangles:
        image = tuple(sorted((HS+adds[z][u-HS],HS+adds[z][v-HS])))
        assert image in triangles
        head_action_edge_checks += 1

layers = [('leaf',0,BS),('block',BS,HS),('head',HS,N)]
sizes = [L,B,H]
root_results, all_dist = [], []
bfs_start = time.process_time()
for name,root,_ in layers:
    dist = [-1]*N
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u]+1
                queue.append(v)
    assert -1 not in dist
    all_dist.append(dist)
    root_results.append({'root':root,'layer':name,'unreachable':0,
        'eccentricity':max(dist),'missing':sum(d > 5 for d in dist),
        'distance_histogram':dict(sorted(Counter(dist).items())),
        'distance_histograms_by_target_layer':{
            target:dict(sorted(Counter(dist[lo:hi]).items())) for target,lo,hi in layers},
        'missing_by_target_layer':[sum(d > 5 for d in dist[lo:hi]) for _,lo,hi in layers]})
bfs_cpu = time.process_time()-bfs_start
require([r['missing'] for r in root_results] == saved['root_missing'],'root_missing',root_results)
require([r['eccentricity'] for r in root_results] == saved['root_eccentricities'],
        'root_eccentricities',root_results)
require([r['missing_by_target_layer'] for r in root_results] == saved['root_missing_by_target_layer'],
        'root_layer_missing',root_results)
diameter = max(r['eccentricity'] for r in root_results)
ordered_hist = Counter()
for size,row in zip(sizes,root_results):
    for d,count in row['distance_histogram'].items():
        ordered_hist[d] += size*count
assert sum(ordered_hist.values()) == N*N and ordered_hist[0] == N
assert all(count % 2 == 0 for d,count in ordered_hist.items() if d)
ordered_bad = sum(size*r['missing'] for size,r in zip(sizes,root_results))
assert ordered_bad % 2 == 0
bad = ordered_bad//2
assert bad == saved['bad_unordered_pairs']
pair_types = {}
for i in range(3):
    for j in range(i,3):
        forward = root_results[i]['distance_histograms_by_target_layer'][layers[j][0]]
        reverse = root_results[j]['distance_histograms_by_target_layer'][layers[i][0]]
        assert all(sizes[i]*forward.get(d,0) == sizes[j]*reverse.get(d,0)
                   for d in set(forward)|set(reverse))
        count = sizes[i]*root_results[i]['missing_by_target_layer'][j]
        if i == j:
            assert count % 2 == 0
            count //= 2
        pair_types[['L','B','H'][i]+['L','B','H'][j]] = count
assert sum(pair_types.values()) == bad

bb_start = time.process_time()
def h_orbit(x):
    return {acts[b][x] for b in range(Q)}

words = [{0}]
for _ in range(3):
    words.append(words[-1] | {gp(g,s) for g in words[-1] for s in S})
HS_term = {x for s in S for x in h_orbit(s % A)}
triangle_term = {Q*Q,2*Q*Q}
predicted = []
for j in range(J):
    word_term = {x for g in words[3] if (g//A)//Q == j for x in h_orbit(g % A)}
    shifted = {x for s in words[1]
               for x in h_orbit(acts[Q*((j-(s//A)//Q) % J)][s % A])}
    predicted.append(word_term | HS_term | shifted | triangle_term)
actual_BB = [{x for x in range(A) if all_dist[1][BS+x+A*j] <= 5} for j in range(J)]
mismatches = [{'j':j,'x':x,'coordinates':dec(x),'predicted':x in predicted[j],
               'BFS_distance':all_dist[1][BS+x+A*j]} for j in range(J) for x in range(A)
              if (x in predicted[j]) != (x in actual_BB[j])]
require(not mismatches,'BB_formula_all_3630_targets',mismatches)
masks = [sum(1 << x for x in row) for row in predicted]
saved_words = saved['original_BB_masks_little_endian_64bit_words']
assert len(saved_words) == J and all(len(row) == 6 for row in saved_words)
saved_masks = [sum(word << (64*i) for i,word in enumerate(row)) for row in saved_words]
assert all(mask >> A == 0 for mask in saved_masks)
require(masks == saved_masks,'all_original_BB_masks',{'independent':masks,'saved':saved_masks})
bb_missing = sum(A-len(row) for row in actual_BB)
axis_missing = sum(1 for row in actual_BB for x in range(A) if dec(x)[1] == 0 and x not in row)
offaxis_missing = bb_missing-axis_missing
assert bb_missing == saved['original_BB_missing'] == root_results[1]['missing_by_target_layer'][1]
assert axis_missing == saved['original_axis_BB_missing']
assert offaxis_missing == saved['original_offaxis_BB_missing']
bb_cpu = time.process_time()-bb_start
total_cpu = time.process_time()-START

proof = {
    'group':'(F11^2 x C3) semidirect (F11 semidirect C10)',
    'K_product':'(b,j)(d,l)=(b+2^(2j)d,j+l)',
    'action':'(u,v,w) -> (2^(3j)u+b*2^j*v,2^j*v,w)',
    'H':'{(b,0): b in F11}',
    'head_triangle_preservation':'left (z,k) sends (u,v,w) to (z_uv+k(u,v),z_w+w); same uv and distinct w are preserved',
    'leaf_edge_preservation':'left t sends {g,gs} to {tg,(tg)s}',
    'tree_edge_preservation':'left t sends g -> gH -> gK to tg -> (tg)H -> (tg)K',
    'transitivity':'left G is transitive on G, G/H and G/K; these are exactly the three labeled layers',
    'block_witness':'(x,(0,j)) sends root H to block(x,j)',
    'head_witness':'(x,identity_K) sends root K to head(x)',
    'action_composition_basis_checks':K*K*3,
    'head_edge_checks_all_K_and_A_basis_translations':head_action_edge_checks,
    'full_edge_formula_matched_saved_graph':True,
    'consequence':'maximum representative eccentricity is exact diameter; weighted distance histograms and bad pair counts are exact'}
verification = {
    'status':'COMPLETE_PROOF_SUPPORTED_THREE_ORBIT_VERIFICATION',
    'verification_method':'complete BFS from one representative of each proved left-G layer orbit',
    'n':N,'m':M,'simple':True,'connected':True,'min_degree':12,'max_degree':12,
    'diameter':diameter,'target_diameter':5,'valid':diameter <= 5,
    'bad_unordered_pairs':bad,'unreachable_unordered_pairs':0,
    'roots_checked':3,'root_vertices':[0,BS,HS],'root_orbit_sizes':sizes,
    'represented_root_count':N,'full_source_BFS_performed':False,
    'ordered_distance_histogram':dict(sorted(ordered_hist.items())),
    'bad_unordered_pairs_by_type':pair_types,
    'representative_roots':root_results,'orbit_reduction_proof':proof,
    'independent_edges_exactly_equal':True,'original_BB_missing':bb_missing,
    'BB_all_3630_targets_pointwise_match':True,'all_10_original_BB_masks_match':True,
    'CPU_seconds':total_cpu,'graph_reconstruction_CPU_seconds':build_cpu,
    'three_BFS_CPU_seconds':bfs_cpu,'BB_CPU_seconds':bb_cpu,
    'scope':'Only profile.best; no preflight or other graph; no candidate search; no full43923-source BFS'}
(OUT/'best.independent_verify.json').write_text(json.dumps(verification,indent=2)+'\n')
result = dict(verification)
result.update({'input':'profile.best.edges','S':sorted(S),'head_triangle_edges_checked':len(triangles),
    'BB_formula':'H W3 H union H W1 K union K W1 H plus two head-triangle shifts',
    'BB_masks':masks,'BB_BFS_masks':[sum(1 << x for x in row) for row in actual_BB],
    'BB_BFS_distances_in_label_order':all_dist[1][BS:HS],
    'BB_word_ball_sizes':list(map(len,words)),
    'original_axis_BB_missing':axis_missing,'original_offaxis_BB_missing':offaxis_missing})
Path(str(STEM)+'.independent_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:verification[key] for key in ['status','n','m','diameter',
    'bad_unordered_pairs','roots_checked','root_orbit_sizes','represented_root_count',
    'full_source_BFS_performed','bad_unordered_pairs_by_type','ordered_distance_histogram',
    'original_BB_missing','CPU_seconds','three_BFS_CPU_seconds']},indent=2))
