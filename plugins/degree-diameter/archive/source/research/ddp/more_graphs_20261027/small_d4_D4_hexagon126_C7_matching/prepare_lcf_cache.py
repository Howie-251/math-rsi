"""Direct primary LCF source and one radius<=4 cache. No matching/SAT/D6 BFS."""
from pathlib import Path
from collections import deque,Counter
import json,time
OUT=Path(__file__).resolve().parent;start=time.process_time()
def save(n,x):(OUT/n).write_text(json.dumps(x,indent=2)+'\n')
bind=json.loads((OUT/'BINDING_INPUT.json').read_text());J=[17,27,-13,-59,-35,35,-11,13,-53,53,-27,21,57,11,-21,-57,59,-17]
assert bind['LCF_offsets']==J
E={tuple(e) for e in bind['LCF_edges']}
assert len(E)==189
# The already constructed candidate is now independently sourced by the primaryrecipe.
assert E=={tuple(sorted((i,(i+1)%126))) for i in range(126)}|{tuple(sorted((i,(i+J[i%18])%126))) for i in range(126)}
adj=[[] for _ in range(126)]
for u,v in sorted(E):assert u!=v;adj[u].append(v);adj[v].append(u)
assert all(len(a)==3 and len(set(a))==3 for a in adj) and all(u%2!=v%2 for u,v in E)
for a in adj:a.sort()
sigma=[(i+18)%126 for i in range(126)]
assert {tuple(sorted((sigma[u],sigma[v]))) for u,v in E}==E
cycles=[[(r+18*s)%126 for s in range(7)] for r in range(18)]
assert len({v for C in cycles for v in C})==126 and all(len(set(C))==7 and sigma[C[-1]]==C[0] for C in cycles)
assert Counter(C[0]%2 for C in cycles)==Counter({0:9,1:9}) and all(len({v%2 for v in C})==1 for C in cycles)
source={'status':'DIRECT_PRIMARY_LCF_RECIPE_BOUND','source_name':'Generalizedhexagon order2/Tutte12cage primaryLCF recipe','n':126,'m':189,'degree':3,'LCF_offsets':J,'repeats':7,'vertices':'0..125; edges cycle126 plus chordi->i+offset[i mod18]','primary_sources':[{'url':'https://www.maplesoft.com/support/help/errors/view.aspx?path=GraphTheory%2FSpecialGraphs%2FLCFGraph','claim':'Generalizedhexagon126/189 and this exact18offset repeated7','verification':'Parentread primary and supplied precise source facts; this stage makes no network call'},{'url':'https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/generators/smallgraphs.html#sage.graphs.generators.smallgraphs.Tutte12Cage','claim':'126/189/girth12/D6','verification':'Primarydescription suppliedbyparent/sourceagent; D6 isnot recomputed'}],'adjacency':adj,'inherited_girth':12,'inherited_D':6,'new_globalD_BFS':0,'localtriad_isomorphism':'UNKNOWN atsingleGraphMatcher8CPUlimit; no mapping asserted or needed for this directprimarysource','source_selection_change':'UseprimaryLCF directly,not a retry or fabricatedresolution oflocaltriad binding'}
save('SOURCE_LCF_PRIMARY.json',source)
(OUT/'source126.edges').write_text('126 189\n'+''.join(f'{u} {v}\n' for u,v in sorted(E)))
save('AUTOMORPHISM.json',{'status':'DIRECT_ALL189_EDGE_IMAGES_MATCH','permutation':sigma,'formula':'v+18 mod126','order':7,'orbits':cycles,'orbit_representatives':list(range(18)),'orbit_vertex_encoding':'r+18*s, r0..17,s0..6','orbit_bipartition':[r%2 for r in range(18)],'even_orbit_indices':list(range(0,18,2)),'odd_orbit_indices':list(range(1,18,2)),'counts':[9,9],'source_binding':'SOURCE_LCF_PRIMARY.json','Autgroup_computation':False})
rows=[];raw=bytearray();far_pairs=[]
for root in range(126):
 d=[255]*126;d[root]=0;q=deque([root])
 while q:
  u=q.popleft()
  if d[u]==4:continue
  for v in adj[u]:
   if d[v]==255:d[v]=d[u]+1;q.append(v)
 hist=Counter(x for x in d if x!=255);assert [hist[k] for k in range(5)]==[1,3,6,12,24]
 closed=[[v for v,x in enumerate(d) if x<=r] for r in range(5)]
 far=[v for v,x in enumerate(d) if x==255];assert len(far)==80
 rows.append({'root':root,'histogram_R0_to_R4':[hist[k] for k in range(5)],'closed_R0_R1_R2_R3_R4':closed,'beyond_R4':far})
 raw.extend(d)
 far_pairs.extend((root,v) for v in far if root<v)
assert len(raw)==126*126 and len(far_pairs)==5040
assert all(raw[u*126+v]==raw[v*126+u] for u in range(126) for v in range(126))
(OUT/'old_distance_to4.u8.bin').write_bytes(raw)
save('RADIUS_CACHE.json',{'status':'COMPLETE_OLD_RADIUS4_CACHE_SINGLE_PASS','rows':rows,'distance_binary':{'path':'old_distance_to4.u8.bin','shape':[126,126],'encoding':'uint8, exact0..4,255meansdistance>4; no D5/D6 BFS'},'root_traversals':126,'maximum_depth':4,'R4_size':46,'far_unordered_pairs_count':5040,'far_opposite_parity_pairs':sum((u%2)!=(v%2) for u,v in far_pairs),'far_same_parity_pairs':sum((u%2)==(v%2) for u,v in far_pairs),'oldD5_D6_use':'Known sourceD6 andbipartition imply faropposite=5/farsame=6; notdistancesnewly traversed beyond4'})
save('OLD_FAR_PAIRS.json',{'old_R4_complement_pairs':far_pairs,'count':5040,'single_added_edge_condition':'Potentialmatchingdomain canrequire olddistance>4; this alone doesnot prohibit shortcyclesusing2newmatchingedges and isnot a completeaugmentedgirth certificate.','matching_atoms_constructed':0})
r={'status':'COMPLETE_DIRECT_PRIMARY_LCF_C7_AND_R4_INPUT_CACHE','n':126,'m':189,'degree':3,'actual_C7_order':7,'C7_orbits':18,'orbits_per_bipartition':[9,9],'all189_edgeimages_match':True,'radius_cache_traversals':126,'radius_limit':4,'R4_size_perroot':46,'old_far_unordered_pairs':5040,'far_opposite_parity_pairs':3024,'far_same_parity_pairs':2016,'inherited_girth':12,'inherited_D':6,'freshD6_BFS':0,'GraphMatcher_retries':0,'localtriad_iso_status':'UNKNOWN_PRESERVED','matching_graphs':0,'matching_atoms':0,'solver_calls':0,'CPU_seconds':time.process_time()-start}
save('SOURCE_CACHE_RESULT.json',r);print(json.dumps(r))
if __name__=='__main__':pass
