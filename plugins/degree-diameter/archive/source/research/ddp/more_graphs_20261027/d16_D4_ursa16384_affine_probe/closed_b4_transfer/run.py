"""Finite cached-word necessary screen, including every controller port overlap."""
from collections import Counter
from pathlib import Path
import json
import resource
import time

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
OUT=Path(__file__).resolve().parent
words=json.loads((OUT.parent/'route_capacity/WORD_IMAGES.json').read_text())['records']
index={tuple(r['word_types']):i for i,r in enumerate(words)}
prefix=[index[tuple(r['word_types'][:-1])] if r['word_types'] else -1 for r in words]
last=[r['word_types'][-1] if r['word_types'] else -1 for r in words]
image_masks=[sum(1<<v for v in r['fibers']) for r in words]
assert words[index[(1,1,1,1)]]['rank']==words[index[(2,2,2,2)]]['rank']==4
FULL=(1<<256)-1
alpha=[1,2,3,0];beta=[1,3,0,2]
ia=[alpha.index(b) for b in range(4)];ib=[beta.index(b) for b in range(4)]
rows=[]
passers=[]
limited=False
for m in (17,19,18):
    for x in range(m):
        for y in range(m):
            if time.process_time()-START>9.5:
                limited=True
                break
            va=[0,x,y,0];vb=[m-1,0,0,1]
            trans=[]
            for b in range(4):
                for k in range(m):
                    trans.append([m*alpha[b]+(k+va[b])%m,
                                  m*beta[b]+(k+vb[b])%m,
                                  m*ib[b]+(k-vb[ib[b]])%m,
                                  m*ia[b]+(k-va[ia[b]])%m])
            simple=all(len(set(t))==4 and g not in t for g,t in enumerate(trans))
            assert all(trans[trans[g][s]][3-s]==g for g in range(4*m) for s in range(4))
            for g in range(4*m):
                h=g
                for _ in range(4):h=trans[h][1]
                assert h==g
            roots=[]
            for b in range(4):
                n=4*m
                ends=[b*m]*len(words)
                masks=[0]*n
                counts=[0]*n
                sole_rank=[-1]*n
                g4=[False]*n
                for i,r in enumerate(words):
                    if i:ends[i]=trans[ends[prefix[i]]][last[i]]
                    g=ends[i]
                    masks[g]|=image_masks[i]
                    counts[g]+=1;sole_rank[g]=r['rank']
                    if r['rank']==4:g4[g]=True
                assert masks[b*m]==FULL
                missing=[]
                for g,mask in enumerate(masks):
                    if mask!=FULL:
                        miss=FULL^mask
                        missing.append({'controller':g,'target_base':g//m,'target_phase':g%m,
                                        'missing_fiber_count':256-mask.bit_count(),
                                        'first_missing_fiber':(miss&-miss).bit_length()-1,
                                        'route_count':counts[g],
                                        'unique_rank3':counts[g]==1 and sole_rank[g]==3})
                roots.append({'source_base':b,'source_controller':b*m,'source_fiber':0,
                              'missing_target_controllers':missing,
                              'missing_fiber_count':sum(z['missing_fiber_count'] for z in missing),
                              'unique_rank3_slot_count':sum(z['unique_rank3'] for z in missing),
                              'rank4_route_controller_targets':sum(g4),
                              'strong_G4_all_targets':all(g4)})
            necessary=all(r['missing_fiber_count']==0 for r in roots)
            strong=all(r['strong_G4_all_targets'] for r in roots)
            row={'ordinal':len(rows),'phase_group':'even18_control' if m==18 else 'original650',
                 'm':m,'x':x,'y':y,'va':va,'vb':vb,'hypothetical_n':4*m*256,
                 'simple_controller':simple,'b4_closed_all_controllers':True,
                 'samefiber_full_all_x_by_rank4_b4':True,
                 'zero_fiber_necessary_pass':necessary,'strong_G4_certificate_pass':strong,
                 'no_unique_rank3_slots':all(r['unique_rank3_slot_count']==0 for r in roots),
                 'source_roots':roots}
            rows.append(row)
            if necessary:
                passers.append({k:v for k,v in row.items() if k!='source_roots'})
        if limited:break
    if limited:break
summary={}
for label,expected in [('original650',650),('even18_control',324)]:
    group=[r for r in rows if r['phase_group']==label]
    summary[label]={'expected':expected,'evaluated':len(group),'untested':expected-len(group),
                    'simple_controller':sum(r['simple_controller'] for r in group),
                    'non_simple_controller_retained':sum(not r['simple_controller'] for r in group),
                    'necessary_passers':sum(r['zero_fiber_necessary_pass'] for r in group),
                    'strong_G4_passers':sum(r['strong_G4_certificate_pass'] for r in group),
                    'no_unique_rank3_slots':sum(r['no_unique_rank3_slots'] for r in group),
                    'first_failed_source_base_histogram':dict(Counter(next((q['source_base'] for q in r['source_roots'] if q['missing_fiber_count']),-1) for r in group))}
result={'status':'UNKNOWN_CPU_LIMIT' if limited else 'COMPLETE_650_PLUS_SEPARATE324_FIXED_WORD_UNION_SCREEN',
        'total_expected':974,'evaluated':len(rows),'untested':974-len(rows),'groups':summary,
        'necessary_passers':passers,'source_fiber_representatives_per_assignment':4,
        'words_per_root':341,'all_nonreduced_words_included':True,'simple_controller_filter_applied':False,
        'source_graph_parses':0,'word_image_recomputations':0,'graph_BFS':0,'actual_graphs_generated':0,
        'prediction_disposition_main':'SUPPORTED' if summary['original650']['necessary_passers'] else 'REFUTED' if summary['original650']['untested']==0 else 'UNKNOWN',
        'prediction_disposition_even':'SUPPORTED' if summary['even18_control']['no_unique_rank3_slots'] else 'REFUTED' if summary['even18_control']['untested']==0 else 'UNKNOWN',
        'scope':'Only the974 stated constant-chart controllers; any zero-fiber missing target is a genuine necessary route obstruction, not merely failed sufficient rank4 certificate.',
        'actual_candidate_D':None,'ordinary_bad_unordered_pairs':None,
        'CPU_seconds':time.process_time()-START,'running':False,'pending':[]}
(OUT/'ROWS.json').write_text(json.dumps(rows,indent=2)+'\n')
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
