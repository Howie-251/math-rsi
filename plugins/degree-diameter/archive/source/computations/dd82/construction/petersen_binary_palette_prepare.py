"""Complete L-preserving interface palettes of the actual double-HS seed.

Reuse the completed 01 and 23 domains; enumerate the other thirteen by
exact cover of their seven-route support. This is a finite subfamily, not
a claim that every arbitrary six-Petersen target preserves these supports.
"""
from itertools import combinations
from pathlib import Path
import json
import time

from hs_augmentation import dump
from petersen_four_fiber_reassembly import SOURCE, adjacency, matching

HERE = Path(__file__).resolve().parent
OUT = HERE/"petersen_binary_palette_run"


start,wall = time.process_time(),time.monotonic()
OUT.mkdir(exist_ok=True)
assert not (OUT/"palettes.json").exists(), "No unchanged rerun"
original = {tuple(e) for e in json.loads(SOURCE.read_text())["edges"]}
ns = adjacency(original)
internal = sorted(e for e in original if e[0]//10==e[1]//10)
f = {(i,j):matching(ns,i,j) for i in range(6) for j in range(6) if i!=j}
reuse01 = json.loads((HERE/"petersen_paired_core_reassembly_run/core_domains.json").read_text())["domain01"]
reuse23 = json.loads((HERE/"petersen_paired_core_exchange_run/domain.json").read_text())
palettes = []
for i,j in combinations(range(6),2):
    pi = [{v-10*i for v in ns[10*i+u] if v//10==i} for u in range(10)]
    pj = [{v-10*j for v in ns[10*j+u] if v//10==j} for u in range(10)]
    old = [v-10*j for v in f[i,j]]
    support = set()
    for u,v in enumerate(old):
        cells = {(u,v)}|{(w,v) for w in pi[u]}|{(u,w) for w in pj[v]}
        assert len(cells)==7 and support.isdisjoint(cells)
        support |= cells
    domains,placements = [],{}
    for u in range(10):
        row=[]
        for v in range(10):
            cells={(u,v)}|{(w,v) for w in pi[u]}|{(u,w) for w in pj[v]}
            if cells<=support:
                row.append(v)
                placements[u,v]=sum(1<<(10*a+b) for a,b in cells)
        domains.append(row)
    reused = (i,j) in ((0,1),(2,3))
    nodes = 0
    if reused:
        saved = reuse01 if (i,j)==(0,1) else reuse23
        assert saved["complete"]
        solutions = saved["solutions"]
    else:
        solutions,state=[],[-1]*10
        def visit(u,used,covered):
            global nodes
            nodes += 1
            if u==10:
                assert covered.bit_count()==70
                solutions.append(state[:])
                return
            for v in domains[u]:
                mask=placements[u,v]
                if not (used>>v&1) and not (covered&mask):
                    state[u]=v
                    visit(u+1,used|(1<<v),covered|mask)
        visit(0,0,0)
    assert old in solutions
    assert len(solutions)==2
    # Verify the retained complete local solutions directly, including reuse.
    for solution in solutions:
        count=[[0]*10 for _ in range(10)]
        for u,v in enumerate(solution):
            count[u][v]+=1
            for w in pi[u]:count[w][v]+=1
            for w in pj[v]:count[u][w]+=1
        assert all(count[u][v]==int((u,v) in support) for u in range(10) for v in range(10))
    ordered=[old,next(p for p in solutions if p!=old)]
    palettes.append(dict(fibers=[i,j],permutations=ordered,allowed_arrows=domains,
                         support=sorted(support),complete=True,reused_domain=reused,
                         new_search_nodes=nodes))

# The fixed-A theorem requires the five Petersen graphs pulled back through
# a chosen root's five matching interfaces to be identical. This property is
# invariant under coordinate relabeling of every fiber.
root_signatures=[]
for root in range(6):
    pulled=[]
    for j in range(6):
        if j==root:continue
        image=f[root,j]
        pulled.append(tuple((u,v) for u,v in combinations(range(10),2) if image[v] in ns[image[u]]))
    root_signatures.append(dict(root=root,distinct_normalized_internal_graphs=len(set(pulled)),
                                all_five_equal=len(set(pulled))==1))
assert all(not row["all_five_equal"] for row in root_signatures)
report=dict(source=str(SOURCE),internal_edges=internal,palettes=palettes,
            complete=True,palette_sizes=[len(p["permutations"]) for p in palettes],
            total_binary_assignments=1<<15,
            original_seed_root_normalization=root_signatures,
            historical_scope="The original seed belongs to this palette family but has no root with five identical pulled-back Petersen graphs, so the fixed-A all-layer-exchanging theorem does not cover this family. Earlier all-15 annealing was not exhaustive over this new exact L-preserving palette.",
            cpu_seconds=time.process_time()-start,wall_seconds=time.monotonic()-wall)
dump(OUT/"palettes.json",report)
lines=["60 90 15"]+[f"{u} {v}" for u,v in internal]
for p in palettes:
    lines.append(" ".join(map(str,p["fibers"])))
    lines.extend(" ".join(map(str,row)) for row in p["permutations"])
(OUT/"input.txt").write_text("\n".join(lines)+"\n")
print(json.dumps({k:v for k,v in report.items() if k not in ("internal_edges","palettes")}))
