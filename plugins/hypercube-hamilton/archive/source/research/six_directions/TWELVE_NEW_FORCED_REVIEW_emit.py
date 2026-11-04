import pathlib,json,hashlib,datetime
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
m=load('TWELVE_NEW_FORCED_MANIFEST.json');p=load('TWELVE_NEW_FORCED_REVIEW_prepare.json');c=load('TWELVE_NEW_FORCED_REVIEW_check.json');f=load('TWELVE_NEW_FORCED_REVIEW_finish.json');s=load('TWELVE_NEW_FORCED_summary.json')
assert p['status']==c['status']==f['status']=='PASS'
for n,h in m['files'].items():assert sha(n)==h,n
art=['TWELVE_NEW_FORCED_REVIEW_prepare.py','TWELVE_NEW_FORCED_REVIEW_prepare.json','TWELVE_NEW_FORCED_REVIEW_rows.txt','TWELVE_NEW_FORCED_REVIEW_check.cpp','TWELVE_NEW_FORCED_REVIEW_check.json','TWELVE_NEW_FORCED_REVIEW_finish.py','TWELVE_NEW_FORCED_REVIEW_finish.json']
d={'audit_skill':'proof-checker','verdict':'PASS','reason_code':'27_explicit_single_cherry_local_iff_classifications_complete_by_independent_legal_forests_full_reduced_pairings_all_matrix_bits_and_GF2_rank512',
 'summary':'All27 stated T28/T19 local arbitrary-matching classifications pass: a short-added cycle exists iff the exact forced pair pq is absent.13824 forests,7077888 connectivity bits and27 independent rank512 eliminations verified. Local only; no Q6 coverage or full12/P6 closure.',
 'reviewer_agent_id':'/root/higher_q5_nearbalanced_review','reviewer_model':'gpt-6.1-sol','reviewer_reasoning':'high','model_override_source':'Explicit user-selected model/effort route relayed by parent overrides ARIS defaults',
 'reviewer_family':'openai','executor_family':'openai','review_independence':'same-family','acceptance_status':'provisional','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'trace_path':'TWELVE_NEW_FORCED_REVIEW.md','audited_input_hashes':{'TWELVE_NEW_FORCED_MANIFEST.json':sha('TWELVE_NEW_FORCED_MANIFEST.json'),**m['files']},
 'checker_artifact_hashes':{n:sha(n) for n in art},'report_hash':sha('TWELVE_NEW_FORCED_REVIEW.md'),
 'primary_source':{'title':'Cygan--Kratsch--Nederlof, Fast Hamiltonicity checking via bases of perfect matchings','url':'https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf','location':'Abstract PDFpage1; Theorem3.4 and Corollary3.5 PDFpage9','domain':'All perfect matchings of complete graph on even t>=2','field':'GF(2)','rank_formula':'2^(t/2-1)','substitution':{'t':20,'rank':512},'direct_primary_browsing_this_review':True},
 'details':{'issues':[],'mathematical_obligations_closed':11,'local_only':True,'local_classifications_proved':27,'types':p['types'],'claimed_indices':m['claimed_indices'],'accepted_marked_statements':[{'index':r['index'],'minority':r['geometry']['minority'],'majority':r['geometry']['majority'],'omitted':r['geometry']['omitted'],'forced_hole':r['forced_hole'],'forced_pair':r['forced_pair']} for r in s['reports']],
 'universal_required_matching_scope':'Every perfect matching F of the complete graph on exactly K=Q5 minus H; no short/bipartite/parity condition.',
 'necessary_obstruction':'Exact available neighbors force p-h-q; F containing pq closes isolated triangle, forbidden for required28/29-vertex cycle.',
 'sufficient_condition':'F excludes pq; contract a-p-q-b to ab on20 terminals, use independently proved rank512 spanning and nonzero complete columns, then expand.',
 'exact_iff_classification':True,'common_automorphism_preserves_all_marked_data':True,'available_cherry_neighbors_independently_checked':True,'physical_fixed_cherry_checked':True,
 'covered_endpoints':22,'reduced_endpoints':20,'forests_verified':13824,'full_and_reduced_endpoint_pairings_verified':13824,'matching_columns_verified':13824,'matrix_bits_recomputed':7077888,'independent_GF2_eliminations':27,'rank_GF2_each':512,'matrix_bits_exactly_match_frozen':True,
 'rank_basis_uses_recomputed_matrix':True,'producer_pivots_or_combos_used_for_rank':False,'original_512_by_1024_matrices_or_extraction_metadata_trusted':False,'generator_exhaustiveness_required':False,
 'small_labelled_contraction_equivalences_checked':f['small_labelled_contraction_equivalences_checked'],'frozen_hashes_checked_before_and_after':249,'reports':c['reports'],
 'actual_Q6_application_audited':False,'new_Q6_coverage_count_accepted':0,'Q6_application_requires_actual_marked_source_and_root_obstruction_checks':True,
 'full_T28_proved':False,'full_T19_proved':False,'full_twelve_hole_proved':False,'full_higher_hole_layers_proved':False,'full_P6_proved':False,'production_or_main_state_modified':False},
 'full_twelve_hole_proved':False,'full_P6_proved':False,
 'scope':'The27 exact marked local necessary-and-sufficient classifications only, modulo primary general GF2 matching-connectivity rank theorem. No actual Q6 application, full T28/T19, complete twelve-hole or P6 closure.'}
(R/'TWELVE_NEW_FORCED_REVIEW.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'verdict':'PASS','review_sha256':sha('TWELVE_NEW_FORCED_REVIEW.json'),'report_sha256':sha('TWELVE_NEW_FORCED_REVIEW.md')},indent=2))
