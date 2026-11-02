#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import csv,json,os,resource,time

HERE=Path(__file__).resolve().parent
PREP=0.15
BUDGET=5.0
HISTORY_CPU=3.000075512
PAPER_RESERVE=0.1
numeric_hard_cap=int(BUDGET-HISTORY_CPU-PREP-PAPER_RESERVE)
resource.setrlimit(resource.RLIMIT_CPU,(numeric_hard_cap,numeric_hard_cap))
def save(name,data):(HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
save('HANDLE.json',{'pid':os.getpid(),'phase':'standard_base_and_once_NB_form_generation','running':True,
                     'worker_count':1,'CPU_budget_seconds':BUDGET,'conservative_preparation_charge_seconds':PREP,
                     'prior_history_charged_CPU_seconds':HISTORY_CPU,'paper_CPU_reserve_seconds':PAPER_RESERVE,
                     'numeric_process_hard_CPU_cap_seconds':numeric_hard_cap})
edge_set=set()
for i in range(5):
    edge_set.add(tuple(sorted((i,(i+1)%5))))
    edge_set.add(tuple(sorted((5+i,5+(i+2)%5))))
    edge_set.add((i,5+i))
edges=sorted(edge_set)
tree=sorted([(0,1),(1,2),(2,3),(3,4)]+[(i,5+i)for i in range(5)])
chords=sorted(edge_set-set(tree))
assert len(edges)==15 and len(tree)==9 and len(chords)==6
adj=[[]for _ in range(10)]
for u,v in edges:adj[u].append(v);adj[v].append(u)
for row in adj:row.sort()
assert all(len(row)==3 for row in adj)
var={e:i for i,e in enumerate(chords)}
tree_adj=[[]for _ in range(10)]
for u,v in tree:tree_adj[u].append(v);tree_adj[v].append(u)
depth=[None]*10;depth[0]=0;stack=[0]
while stack:
    u=stack.pop()
    for v in tree_adj[u]:
        if depth[v]is None:depth[v]=depth[u]+1;stack.append(v)
assert all(d is not None for d in depth)
switches=[d%2 for d in depth]
canonical_bits=[(1+depth[u]+depth[v])%2 for u,v in chords]
canonical_sig=sum(x<<i for i,x in enumerate(canonical_bits))
save('INPUT_AND_TREE_GAUGE.json',{'base':'classicalPetersen10outerC5/innerstep2/spokes','n':10,'m':15,
 'edges':edges,'tree_edges':tree,'oriented_cotree_edges':chords,'variable_count':6,'tree_root':0,
 'tree_depths':depth,'canonical_all_edge_odd_vertex_switches':switches,
 'canonical_all_edge_odd_cotree_bits':canonical_bits,'canonical_signature_integer':canonical_sig,
 'integer_coefficients':'chordsmall→largeadds+1,reverse−1;tree0',
 'C14_gauge_domain':'sixindependentZ14voltages;treegaugecomplete','source_D2_or_any_BFS_checked':False})

words=[];slotwords={(u,v):[]for u in range(10)for v in range(10)}
def dfs(root,path,coeff):
    u=path[-1]
    record={'word_id':len(words),'root':root,'target':u,'length':len(path)-1,'vertices':list(path),
            'integer_coefficients':list(coeff),'coefficients_mod7':[x%7 for x in coeff]}
    words.append(record);slotwords[root,u].append(record)
    if len(path)==7:return
    previous=path[-2]if len(path)>1 else None
    for v in adj[u]:
        if v==previous:continue
        next_coeff=list(coeff);e=tuple(sorted((u,v)))
        if e in var:next_coeff[var[e]]+=1 if u<v else -1
        dfs(root,path+[v],tuple(next_coeff))
for root in range(10):dfs(root,[root],(0,)*6)
assert len(words)==1900
raw_class_counts={'diagonal':Counter(),'adjacent':Counter(),'nonadjacent':Counter()}
slot_stats=[]
for (u,v),ws in slotwords.items():
    kind='diagonal'if u==v else'adjacent'if v in adj[u]else'nonadjacent'
    raw_class_counts[kind][len(ws)]+=1
    slot_stats.append({'root':u,'target':v,'endpoint_class':kind,'raw_words':len(ws),
                       'distinct_integer_vectors':len({tuple(w['integer_coefficients'])for w in ws}),
                       'distinct_mod7_vectors':len({tuple(w['coefficients_mod7'])for w in ws})})
raw_prediction_supported=(raw_class_counts['diagonal']==Counter({25:10})and
                          raw_class_counts['adjacent']==Counter({21:30})and
                          raw_class_counts['nonadjacent']==Counter({17:60}))
save('ALL_NB_WORDS_AND_INTEGER_FORMS.json',{'length_bound':6,'empty_word_included':True,
 'source_roots':10,'total_words':len(words),'oriented_cotree_edges':chords,'words':words})
with (HERE/'SLOT_RAW_FORM_COUNTS.csv').open('w',newline='')as f:
    w=csv.DictWriter(f,fieldnames=list(slot_stats[0]));w.writeheader();w.writerows(slot_stats)
save('HANDLE.json',{'pid':os.getpid(),'phase':'all64parity_signatures_raw_and_distinct_mod7_capacity',
                     'running':True,'worker_count':1,'CPU_budget_seconds':BUDGET,'actual_words_generated_once':1900})

signatures=[];raw_survivors=[];form_survivors=[]
all_slots=[(u,v,p)for u in range(10)for v in range(10)for p in range(2)]
for sig in range(64):
    bits=[(sig>>i)&1 for i in range(6)]
    buckets={key:[]for key in all_slots}
    for w in words:
        parity=sum(c*b for c,b in zip(w['integer_coefficients'],bits))%2
        buckets[w['root'],w['target'],parity].append(w)
    raw_counts={key:len(ws)for key,ws in buckets.items()}
    mod7_sets={key:{tuple(w['coefficients_mod7'])for w in ws}for key,ws in buckets.items()}
    raw_slot=min(all_slots,key=lambda key:(raw_counts[key],key))
    form_slot=min(all_slots,key=lambda key:(len(mod7_sets[key]),key))
    raw_min=raw_counts[raw_slot];form_min=len(mod7_sets[form_slot])
    rawpass=raw_min>=7;formpass=form_min>=7
    if rawpass:raw_survivors.append(sig)
    if formpass:form_survivors.append(sig)
    rec={'signature_integer':sig,'six_bits':bits,'raw_word_gate_pass':rawpass,
         'distinct_mod7_form_gate_pass':formpass,'minimum_raw_word_count':raw_min,
         'raw_tight_slot':list(raw_slot),'raw_tight_word_ids':[w['word_id']for w in buckets[raw_slot]],
         'minimum_distinct_mod7_vectors':form_min,'mod7_form_tight_slot':list(form_slot),
         'form_tight_raw_words':len(buckets[form_slot]),
         'form_tight_word_ids':[w['word_id']for w in buckets[form_slot]],
         'form_tight_distinct_mod7_vectors':[list(v)for v in sorted(mod7_sets[form_slot])],
         'status':'NECESSARY_PARITY_PASS_NOT_C14_GRAPH'if formpass else'FAIL_RAW_WORD_CAPACITY'if not rawpass else'FAIL_DISTINCT_MOD7_FORM_CAPACITY'}
    signatures.append(rec)
save('ALL64_SIGNATURE_RESULTS.json',signatures)
with (HERE/'ALL64_SIGNATURE_SUMMARY.csv').open('w',newline='')as f:
    w=csv.writer(f);w.writerow(['signature','bits','status','min_raw','raw_tight_slot','min_mod7_forms','form_tight_slot'])
    for r in signatures:w.writerow([r['signature_integer'],''.join(map(str,r['six_bits'])),r['status'],r['minimum_raw_word_count'],r['raw_tight_slot'],r['minimum_distinct_mod7_vectors'],r['mod7_form_tight_slot']])
canonical=signatures[canonical_sig]
canon_key=tuple(canonical['raw_tight_slot'])
canon_words=[w for w in slotwords[canon_key[0],canon_key[1]]if sum(c*b for c,b in zip(w['integer_coefficients'],canonical_bits))%2==canon_key[2]]
canonical_binding=all(sum(c*b for c,b in zip(w['integer_coefficients'],canonical_bits))%2==
                      (w['length']+switches[w['target']]-switches[w['root']])%2 for w in words)
assert canonical_binding
canon_class='diagonal'if canon_key[0]==canon_key[1]else'adjacent'if canon_key[1]in adj[canon_key[0]]else'nonadjacent'
nonadj_six_words=[w for w in slotwords[0,2]if sum(c*b for c,b in zip(w['integer_coefficients'],canonical_bits))%2==1]
save('CANONICAL_NONADJACENT_SIX_WORD_WITNESS.json',{'slot':[0,2,1],'base_relation':'nonadjacent','raw_count':len(nonadj_six_words),'distinct_mod7_forms':len({tuple(w['coefficients_mod7'])for w in nonadj_six_words}),'tight_words':nonadj_six_words})
save('CANONICAL_BIPARTITE_DOUBLECOVER_CAPACITY.json',{
 'signature':canonical_sig,'six_bits':canonical_bits,'tree_vertex_switches':switches,
 'all1900_words_gauge_length_parity_identity_bound':True,
 'bipartite_model':'alloriginaledgeparities1;aftertreegaugepartitionissheet+vertexswitch',
 'minimum_raw_count':canonical['minimum_raw_word_count'],'tight_slot':canonical['raw_tight_slot'],
 'tight_slot_base_class':canon_class,'tight_words':canon_words,
 'distinct_mod7_form_count_in_tight_slot':len({tuple(w['coefficients_mod7'])for w in canon_words}),
 'strict_C14_no_for_this_signature':not canonical['raw_word_gate_pass'],
 'no20vertex_graph_or_BFS_generated':True})

alias_slot_count=sum(r['raw_words']!=r['distinct_mod7_vectors']for r in slot_stats)
status='COMPLETE_NO_PETERSEN_C14_TRANSLATION_COVER_D6_BY_PARITY_CAPACITY'if not form_survivors else'NECESSARY_PARITY_SURVIVORS_C7_ASSIGNMENTS_UNTESTED'
result={'status':status,'target':{'degree':3,'diameter':6,'hypothetical_order':140},
 'source_base':'standardPetersen10/15','source_roots':10,'NB_max_length':6,'empty_word_included':True,
 'all_directed_NB_words_generated_once':len(words),'raw_slot_class_counts':{k:dict(v)for k,v in raw_class_counts.items()},
 'raw_25_21_17_prediction_supported':raw_prediction_supported,
 'integer_and_mod7_vectors_saved':True,'unconditioned_slots_with_mod7_form_aliases':alias_slot_count,
 'parity_signatures_tested':64,'parity_target_slots_per_signature':200,
 'raw_word_capacity_survivors':raw_survivors,'distinct_mod7_form_capacity_survivors':form_survivors,
 'stronger_form_gate_only_rejections':[s for s in raw_survivors if s not in form_survivors],
 'canonical_bipartite_signature':canonical_sig,'canonical_tight_slot':canonical['raw_tight_slot'],
 'canonical_min_raw_count':canonical['minimum_raw_word_count'],'canonical_min_mod7_form_count':canonical['minimum_distinct_mod7_vectors'],
 'canonical_nonadjacent_6_prediction_supported':len(nonadj_six_words)==6,
 'gate_survivor_meaning':'Onlyatleast7distinctmod7coefficientvectorsperorderedpair/parity;notendpointimagesorcompatibleC7voltages.',
 'CRT_gauge_domain':'AllsixZ14translationvoltagesafter9tree-edgegauge;independentF2sixsignatures/F7sixparameters.',
 'complete_NO_scope_if_no_survivors':'OnlyordinaryC14translationcoversofthisPetersenbase;notarbitrarypermutationcoversorall3D6graphs.',
 'survivor_graph_structure_classification':'NOT_PERFORMED;noonlydodecahedronclaim',
 'F2power4_alias_obstruction':'Paperownerusesactualdiag25andinversepairs;notasecondnumericalbatch',
 'C7_or_C14_voltage_assignments_evaluated':0,'new140_graph_BFS_solver_Lean_field_ARIS_queries':0,
 'source_D2_or_source_allroot_validity':0,'graph_parameter_Lean_increment':[0,0,0],
 'root_Wiki_HTML_modified':False,'conservative_preparation_charge_seconds':PREP,
 'prior_history_charged_CPU_seconds':HISTORY_CPU,'paper_CPU_reserve_seconds':PAPER_RESERVE,
 'actual_process_CPU_seconds':time.process_time(),'total_charged_CPU_seconds':HISTORY_CPU+PAPER_RESERVE+PREP+time.process_time(),
 'CPU_budget_seconds':BUDGET,'worker_count':1,'next':'STOP_REPORT_PARITY_SURVIVORS_NO_C7_C14_ASSIGNMENT_OR_SECOND_BATCH'}
save('RESULT.json',result)
(HERE/'NOTE.md').write_text(f'''# PetersenC14 parity route gate

Actualstatus:{status}. All1900NBwords(includingempty)weregeneratedoncewithinteger6-chordforms. Rawslotclassesare{result['raw_slot_class_counts']};the25/21/17predictionis{raw_prediction_supported}. Thebaseistheexplicitclassical10/15input,notanewgraphoritsD2verification.

Exactly64paritysignatureswerecheckedon200orderedpair/parityslots. Rawcapacitysurvivors:{raw_survivors}. Strongerdistinctmod7formcapacitysurvivors:{form_survivors}. Signaturedataretainsrawcountsanddistinctvectorcountsseparately;nodistinctvectorcountiscalledanactualendpointimage. Theunconditioned100slotswithraw/mod7formaliasingnumber{alias_slot_count}. ActualwordIDsandvectorsareexported,notonlyminima.

Canonicalall-edge-odd/bipartitedoublecoverhasgaugedsignature{canonical_sig},bits{canonical_bits};itwascomputedfromtreevertexswitchesandall1900length-parityidentitieswerebound. Itsminimumrawslotis{canonical['raw_tight_slot']}({canon_class}),count{canonical['minimum_raw_word_count']}<7. ThisclosesonlythatparitybranchregardlessC7voltagechoices;itisnotaprematureclassificationoftheothersurvivors.

Ashortestordinarycoverwalkprojectsnonbacktracking:an immediatebaseedge reversalforcesactualedge reversalandsamefullvertex. EachwordhasoneC14endpointfromafixedroot. Forafixedparitysignature,targetparityhassevenC7vertices;fewerthan7wordsor7distinctF7coefficientvectorscannotcoverthem. AtrueC14D6covermustthereforepassalltheseslots. Conversely,gatepassleavesmod7evaluationcollisionsandglobalparametercompatibilityopen. NoC7/C14assignment,140graphorBFSwasattempted.

Treegaugeeliminates9edgesleaving6independentZ14variables;CRTseparatesparityandmod7components. Every64signaturebranchisaccountedfor,butfinitegatepassisnotagraph. Canonicaldoublecoverfailuredoesnotimplyallbipartite/multifiberliftsareclosed. TheF2^4inverse-aliaspaperstatementisseparateanddoesnotintroduceasecondnumericbatch.

Wholegatecharged{HISTORY_CPU+PAPER_RESERVE+PREP+time.process_time():.9f}/5CPUincludespriorhistory{HISTORY_CPU:.9f},paperreserve{PAPER_RESERVE},preparation{PREP},imports,theonewordgenerationandall64checks,oneworker. HistorysamemodelstrictNO/UNKNOWNwasnotlocated;existingdifferent-source/D2scopeswerenotreusedasnegativeproofs. Noothergraph,field,seed,voltageorclassificationisstarted.
''')
terminal={'status':status,'running':False,'all_processes_terminal':True,'worker_count':1,
 'actual_process_CPU_seconds':time.process_time(),'conservative_preparation_charge_seconds':PREP,
 'prior_history_charged_CPU_seconds':HISTORY_CPU,'paper_CPU_reserve_seconds':PAPER_RESERVE,
 'total_charged_CPU_seconds':HISTORY_CPU+PAPER_RESERVE+PREP+time.process_time(),'CPU_budget_seconds':BUDGET,
 'NB_generation_batches':1,'parity_signatures_completed':64,'no_timer_reset':True,'no_automatic_continuation':True}
save('TERMINAL.json',terminal);save('HANDLE.json',{'pid':os.getpid(),'phase':'terminal',**terminal})
print(json.dumps({'result':result,'terminal':terminal},ensure_ascii=False,indent=2))
