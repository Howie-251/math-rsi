from pathlib import Path
import sys,json,importlib.util,os
base=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(base/'workflow_copy/base/tools'))
import current_context as c
spec=importlib.util.spec_from_file_location('batch',base/'workflow_copy/plugins/degree-diameter/tools/d5_blocking_batch.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
spec=importlib.util.spec_from_file_location('receipts',base/'workflow_copy/plugins/degree-diameter/tools/extension_receipts.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
root=base/'workflow_fixture';root.mkdir(exist_ok=True)
(root/'source.edges').write_text('42402 245937\n')
(root/'planes.txt').write_text('754\n')
(root/'prior.txt').write_text('prior review')
state={'status':'PAUSED','current_context':{'current_work':{'in_flight':{}},'families':{'12,5':{'generator_domain':'d12_754_planes_core41356','accepted_orders':[42402],'latest_graph':{'n':42402,'m':245937,'edge_file':str(root/'source.edges'),'evidence':{'prior':'accepted'}}}}}}
p=root/'STATE.json';p.write_text(json.dumps(state))
plan=b.build_plan(p,root/'planes.txt',root/'should_not_be_created',1,2,3)
checks={'imports_in_intended_repository_layout':'PASS','paused_plan_only_reading':'PASS'}
try:b.execute(plan);raise AssertionError('paused execute accepted')
except ValueError as exc:checks['paused_execution_guard']=str(exc)
assert not (root/'should_not_be_created').exists()
state['status']='ACTIVE';state['current_context']['current_work']['in_flight']={'job':{'terminal_result':'RESULT.json'}}
(root/'RESULT.json').write_text('{}');p.write_text(json.dumps(state))
try:b.execute(plan);raise AssertionError('returned result bypassed')
except ValueError as exc:checks['terminal_result_execution_guard']=str(exc)
state['current_context']['current_work']['in_flight']={};state['current_context']['families']['12,5']['latest_graph']['n']=42403;p.write_text(json.dumps(state))
try:b.execute(plan);raise AssertionError('stale source accepted')
except ValueError as exc:checks['stale_source_execution_guard']=str(exc)
assert not (root/'should_not_be_created').exists()
state['current_context']['families']['12,5']['latest_graph']['n']=42402
state['current_context']['families']['12,5']['latest_graph']['edge_file']='source.edges';p.write_text(json.dumps(state))
try:b.build_plan(p,root/'planes.txt',root/'unused',1,2,3);raise AssertionError('unexpected relative source resolution')
except FileNotFoundError as exc:checks['relative_source_uses_process_cwd_not_state_dir']=str(exc)
request={'review_mode':'reuse','reuse_scope':'unchanged','prior_reviews':[{'path':'prior.txt','scope':'lemma'}]}
try:c.request_text(state,request,state_dir=root);raise AssertionError('unexpected relative review resolution')
except ValueError as exc:checks['relative_prior_review_uses_process_cwd_not_state_dir']=str(exc)
# Zero-prefix author receipt binding check: use same-n mismatched m, demonstrating exact source binding is inherited rather than checked.
cur={'families':{'12,5':{'degree':12,'diameter':5,'phase_start_order':42402,'accepted_orders':[42402],'latest_graph':{'n':42402,'m':245937}}}}
a={'running':False,'source_n':42402,'accepted_new_graphs':0,'final_n':42402,'final_m':1,'final_edgefile':'other.edges','status':'UNKNOWN'}
i={'status':'PASS','source':{'n':42402,'m':1,'previously_independently_accepted_diameter_upper_bound':5},'prefixes':[],'independently_accepted_prefix_count':0,'final_graph':{'n':42402,'m':1,'simple':True,'maximum_degree':12,'diameter_upper_bound':5},'author_final_graph_comparison':{'status':'MATCH','path':'/elsewhere/other.edges','author_n':42402,'author_m':1,'missing_edge_count':0,'extra_edge_count':0}}
res=r.consume(cur,a,i,family_key='12,5',evidence={'author':'a','independent':'i'},acceptance_basis='parent accepted')
checks['receipt_accepts_same_order_different_source_m']='CONFIRMED: caller must bind exact accepted source; helper only checks source n membership'
(base/'WORKFLOW_SMOKE_RESULT.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps(checks,indent=2))
