from pathlib import Path
from collections import Counter
import json,time

P=Path(__file__).resolve().parent
B=P.parent.parent/'breadth_20261027_wave3'
t=time.process_time()
original=json.loads((B/'controller_lift192/base_words.json').read_text())
bases=[('A_original_named_multigraph',[tuple(e) for e in original['edges']]),
       ('B_octahedron_K222',[(u,v) for u in range(6) for v in range(u+1,6) if u//2!=v//2])]
results=[]
for name,edges in bases:
    assert len(edges)==12
    parent=list(range(6))
    def root(u):
        while parent[u]!=u:u=parent[u]
        return u
    tree=[]
    for e,(u,v) in enumerate(edges):
        a,b=root(u),root(v)
        if a!=b:parent[a]=b;tree.append(e)
    free=[e for e in range(12) if e not in tree]
    assert len(tree)==5 and len(free)==7
    if name.startswith('A_'):assert tree==original['tree'] and free==original['free']
    index={e:i for i,e in enumerate(free)}
    adj=[[] for _ in range(6)]
    for e,(u,v) in enumerate(edges):adj[u].append((v,e,1));adj[v].append((u,e,-1))
    assert all(len(row)==4 for row in adj)
    walks=[[[] for _ in range(6)] for _ in range(6)]
    for start in range(6):
        def go(u,prev_e,left,coeff,word):
            if not left:
                walks[start][u].append((tuple(coeff),word))
                return
            for v,e,sign in adj[u]:
                if e==prev_e:continue
                new=coeff[:]
                if e in index:new[index[e]]+=sign
                go(v,e,left-1,new,word+[[e,sign]])
        go(start,-1,4,[0]*7,[])
        assert sum(map(len,walks[start]))==108
    records=[]
    intmat=[];modmat=[];wordmat=[]
    for u in range(6):
        im=[];mm=[];wm=[]
        for v in range(6):
            words=walks[u][v]
            forms=sorted({c for c,w in words})
            modforms=sorted({tuple(x%13 for x in c) for c in forms})
            assert len(forms)==len(modforms) # coefficients lie in [-4,4], so mod 13 is injective
            record=dict(slot=[u,v],NB4_named_words=len(words),integer_distinct=len(forms),mod13_distinct=len(modforms),
                        integer_forms=forms,mod13_forms=modforms,zero_form_present=(0,)*7 in forms)
            records.append(record);im.append(len(forms));mm.append(len(modforms));wm.append(len(words))
        intmat.append(im);modmat.append(mm);wordmat.append(wm)
    minimum=min(r['mod13_distinct'] for r in records)
    tight=[r['slot'] for r in records if r['mod13_distinct']==minimum]
    fail=next((r for r in records if r['mod13_distinct']<13),None)
    result=dict(name=name,vertices=6,edges=[list(e) for e in edges],orientation='ascending endpoints',
                tree_rule='Kruskal in named-edge order; tree voltages gauged to zero',tree_edge_ids=tree,free_edge_ids=free,
                voltage_group='C13',controller_target_order=78,fiber_dimension=4,fiber_field=3,resulting_target_order_if_all_conditions_met=6318,
                NB4_words_per_root=108,integer_capacity_matrix=intmat,mod13_capacity_matrix=modmat,named_word_count_matrix=wordmat,
                minimum_capacity=minimum,tight_slots=tight,status='CAPACITY_OBSTRUCTION_STOP' if fail else 'SYMBOLIC_CAPACITY_PASSES_NOT_EXISTENCE',
                obstruction=None if fail is None else dict(slot=fail['slot'],capacity=fail['mod13_distinct'],required=13,
                    integer_forms=fail['integer_forms'],mod13_forms=fail['mod13_forms'],
                    named_NB4_words=[word for coeff,word in walks[fail['slot'][0]][fail['slot'][1]]],
                    reason='Every assignment evaluates these forms to at most this many residues, fewer than all 13 fiber elements.'),
                diagonal=[dict(slot=r['slot'],integer_distinct=r['integer_distinct'],mod13_distinct=r['mod13_distinct'],zero_form_present=r['zero_form_present']) for r in records if r['slot'][0]==r['slot'][1]],
                slots=records,actual_voltage_assignments_tested=0,controller_graph_generated=False,ordinary_BFS_performed=False)
    results.append(result)
out=dict(status='TWO_FIXED_BASES_SYMBOLIC_SCREEN_COMPLETE',bases=results,CPU_seconds=time.process_time()-t,
         immediate_reverse_rule='forbid reversal along the same named edge only; parallel other named edges are allowed',
         existence_claim=False,parameter_search_started=False,pending=[])
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
for r in results:
    print(r['name'],r['status'],'min',r['minimum_capacity'],'tight',r['tight_slots'])
    print('capacities',r['mod13_capacity_matrix'])
    print('diagonal',r['diagonal'])
print('CPU',out['CPU_seconds'])
