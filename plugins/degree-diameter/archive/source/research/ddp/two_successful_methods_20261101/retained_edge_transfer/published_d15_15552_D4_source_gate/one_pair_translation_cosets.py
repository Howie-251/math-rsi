"""One-pair follow-up within the original10CPU route experiment."""
import collections,itertools,json,resource,time
from pathlib import Path
started=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(8,8))
D=Path(__file__).resolve().parent
p=json.loads((D/'NEW_ROUTE4_SELECTED_PAIR.json').read_text());assert p['pair']==[0,0]
def code(x):return sum((x[i]%3)*3**i for i in range(4))
qualified=[];rejected=[];union={}
for route in p['route_details']:
    cols=route['noise_columns'];images={}
    for noise in itertools.product(range(3),repeat=len(cols)):
        y=[sum(c[i]*t for c,t in zip(cols,noise))%3 for i in range(4)]
        images.setdefault(code(y),list(noise))
    difference=[[(route['M'][i][j]-int(i==j))%3 for i in range(4)]for j in range(4)]
    tests=[code(v)for v in difference]+[code(route['c'])]
    if all(y in images for y in tests):
        q=dict(word=route['word'],M=route['M'],c=route['c'],noise_columns=cols,
               noise_image_size=len(images),noise_image_codes=sorted(images),
               M_minus_I_column_noise_coefficients=[images[y]for y in tests[:4]],
               constant_noise_coefficients=images[tests[4]])
        qi=len(qualified);qualified.append(q)
        for y,coeff in images.items():union.setdefault(y,dict(qualified_word_index=qi,word=route['word'],noise_coefficients=coeff))
    else:rejected.append(dict(word=route['word'],failed_columns_or_c=[i for i,y in enumerate(tests)if y not in images],failed_vector_codes=[y for y in tests if y not in images]))
missing=sorted(set(range(81))-set(union))
r=dict(status='SUPPORTED_ONE_PAIR_ALLX_TRANSLATION_COSET_COVER'if not missing else'REFUTED_TRANSLATION_COSET_UNION_NOT_ALL81',
   pair=[0,0],same_original_budget=True,word_lengths_max=4,closed_words_tested=len(p['route_details']),
   qualifying_word_count=len(qualified),qualifying_noise_image_histogram=dict(sorted(collections.Counter(q['noise_image_size']for q in qualified).items())),
   actual_noise_union_size=len(union),missing_vector_codes=missing,
   missing_vectors=[[v//3**i%3 for i in range(4)]for v in missing],
   qualifying_words=qualified,rejected_words=rejected,union_vector_noise_witnesses=union,
   old_exact_M_c_group_max39_preserved=True,old_fullrank4word_hypothesis_refutation_preserved=True,
   allx_statement_proved_by_certificate=not missing,
   allx_formula='For h=y-x choose noisealpha withNalpha=h; subtract sum_i x_i timescolumnwitness_i andconstantwitness. ThenMx+c+Nnoise=y.',
   other_pairs_tested=0,graph_BFS_field_atomicrank_Lean_runs=0,
   CPU_seconds=time.process_time()-started)
(D/'NEW_ROUTE4_TRANSLATION_COSETS.json').write_text(json.dumps(r,indent=2)+'\n')
main=json.loads((D/'NEW_ROUTE4_RESULT.json').read_text())
main['same_original_pair_translation_coset_followup']={k:r[k]for k in ['status','pair','closed_words_tested','qualifying_word_count','actual_noise_union_size','missing_vector_codes','allx_statement_proved_by_certificate','CPU_seconds']}
main['prior_measured_CPU_seconds']=main['CPU_seconds'];main['CPU_seconds']+=r['CPU_seconds']
main['conservative_whole_batch_CPU_upper_bound_seconds']=2.
(D/'NEW_ROUTE4_RESULT.json').write_text(json.dumps(main,indent=2)+'\n')
t=json.loads((D/'NEW_ROUTE4_TERMINAL.json').read_text());t.update(CPU_seconds=main['CPU_seconds'],translation_coset_status=r['status'],
    same_original10CPU_budget=True,conservative_whole_batch_CPU_upper_bound_seconds=2.,selected_pairs_examined=1,running=False)
(D/'NEW_ROUTE4_TERMINAL.json').write_text(json.dumps(t,indent=2)+'\n')
print(json.dumps({k:r[k]for k in ['status','closed_words_tested','qualifying_word_count','qualifying_noise_image_histogram','actual_noise_union_size','missing_vector_codes','allx_statement_proved_by_certificate','CPU_seconds']}))
