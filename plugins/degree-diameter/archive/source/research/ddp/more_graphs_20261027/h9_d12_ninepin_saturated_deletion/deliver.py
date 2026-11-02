"""Append the single accepted9pin+3anchor literal; one edge-set generator comparison, no BFS."""
from pathlib import Path
import copy,json,subprocess,sys
H=Path(__file__).resolve().parent;ROOT=H.parents[3];DELIVERY=H.parent/'delivery'
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen

def save(path,obj):
 def ss(z):
  if isinstance(z,str):return[z]
  if isinstance(z,dict):return[t for v in z.values() for t in ss(v)]
  if isinstance(z,(tuple,list)):return[t for v in z for t in ss(v)]
  return[]
 assert not screen('\n'.join(ss(obj)));path.write_text(json.dumps(obj,indent=2)+'\n')
result=json.loads((H/'RESULT.json').read_text());assert result['accepted_count']==1 and (result['initial_n'],result['final_n'],result['final_m'])==(42396,42397,245877)
r=result['records'][0];pins=r['full_neighbor_set'];mandatory=r['mandatory_pins'];anchors=r['anchors']
assert pins==sorted(set(pins)) and len(pins)==12 and len(mandatory)==9 and len(anchors)==3
assert sorted(mandatory+anchors)==pins and r['deleted_saturated_pin']==13863 and 13863 not in pins
assert r['actual_current_R4_missing']==0 and r['covered_old_vertices']==42396 and max(r['old_neighbor_degrees'])<12
check=json.loads((ROOT/r['native_verify_file']).read_text())
assert check['status']=='FULL_SELECTED_R4_CHECK_COMPLETE' and check['missing_count']==0 and check['covered_count']==42396
assert check['source_n']==42396 and check['source_m']==245865 and check['pins']==pins
assert check['pin_current_degrees']==r['old_neighbor_degrees']
path=DELIVERY/'families.json';parameters=json.loads(path.read_text());family=parameters['families']['12']
old12=copy.deepcopy(family['steps']);old11=copy.deepcopy(parameters['families']['11']);old_independent=copy.deepcopy(family['strongest_independent_verification'])
assert parameters['distinct_explicit_examples']==57 and family['example_count']==len(old12)==54 and family['strongest_n']==42396
assert family['last_independent_allsource_order']==42377 and old_independent['n']==42377 and parameters['Lean_complete_graph_instances']==0
family['steps'].append(dict(step=55,source_n=42396,source_m=245865,
 source='Previously accepted degree12 family prefix on labels0..42395 by complete per-step degree/R4 induction; last independent allsource42377',
 new_vertex=42396,pins=pins,mandatory_pins=mandatory,deleted_saturated_pin=13863,anchors=anchors,
 old_pin_degrees=r['old_neighbor_degrees'],new_vertex_degree=12,new_n=42397,new_m=245877,
 complete_currentbase_R4_certificate=True,actual_current_R4_covered=42396,actual_current_R4_missing=0,
 source_evidence='research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/accepted_01.json',
 native_R4_evidence=r['native_verify_file'],
 mandatory_pin_scope='Nine-point subset obtained by deleting saturated pin13863 from a ten-pin ambient Qline; no automatic fullcore coverage is asserted for this subset.',
 anchor_selection='Rare-missing-target first anchor with gain/complement ordering and exactatmosttwo-anchor tail; completeactualcurrentR4 required.',
 parent_pending=False,accepted_by_production_induction=True,
 verification_scope='Parent accepted existing production actualdegree+completecurrentR4; no new independent R4, allsourceBFS, externalreview or Leaninstance.'))
assert family['steps'][:54]==old12 and parameters['families']['11']==old11
proof='Retain all previous edges. Each literal full neighbor set, whether a complete Qline image or a selected subset plus anchors, is accepted only with actualcurrentdegree within cap and actualclosedR4 coverage of every currentoldvertex. No geometric wholecore guarantee is inferred for subsets. By induction oldold distances do not increase and newold distances are at most5. The degree-specificD4Moore upper bounds give exactD5 for these orders. Full allsourceBFS is not claimed for every prefix.'
family.update(example_orders=list(range(42343,42398)),example_count=55,strongest_n=42397,strongest_m=245877,
 proof_scope=proof,edge_count_formula='245217 + sum(new_vertex_degree for all applied literalsteps)',
 strongest_complete_verification=dict(kind='Parent accepted production degree+completeR4 induction',n=42397,m=245877,max_degree=12,diameter_exact=5,
   actualnewstep_R4_missing=0,parent_pending=False,accepted_by_production_induction=True,newallsourceBFS=0,newindependentR4=0,newexternalreview=0),
 last_independent_allsource_order=42377)
assert family['strongest_independent_verification']==old_independent
parameters.update(package='All58 explicit H9 neighborhood+anchor extension examples',distinct_explicit_examples=58,proof_schema=proof,
 reviewed_example_count=38,Lean_complete_graph_instances=0)
parameters['mathematical_strongest_bounds']['N(12,5)']=42397
parameters['latest_mainfamily_extension']=dict(source_n=42396,new_examples=1,final_n=42397,source_file=result['final_graph'],
 old57_literal_steps_preserved=True,method='Deleteone saturatedQline pin; nine mandatorypins plus threeanchors, accepted by actualdegree and completecurrentR4 induction',
 mandatory_pins=mandatory,deleted_saturated_pin=13863,anchors=anchors,parent_pending=False,accepted_by_production_induction=True,
 new_allsource_BFS=0,new_independent_R4=0,new_external_review=0,reviewed_examples_retained=38,last_allsource_retained=42377,Lean_complete_graph_instances=0)
save(path,parameters)
# Exactly one generator reconstruction comparison; no graph output, R4 computation or BFS.
with (H/'generator_dry_run.json').open('w') as stream:
 subprocess.run([sys.executable,str(DELIVERY/'family_generator.py'),'--degree','12','--order','42397','--dry-run','--compare',str(ROOT/result['final_graph'])],stdout=stream,check=True)
gen=json.loads((H/'generator_dry_run.json').read_text());assert gen['comparison']['edge_set_matches'] and not gen['BFS_performed'] and not gen['graph_written']
save(H/'delivery_update.json',dict(total_examples=58,degree12_examples=55,degree11_examples=3,strongest_n=42397,strongest_m=245877,
 old57_literal_steps_preserved=True,old12step_count54_preserved=True,new_literal_steps=1,mandatory_pins=mandatory,deleted_saturated_pin=13863,anchors=anchors,
 parent_pending=False,accepted_by_production_induction=True,generator_edge_set_matches=True,generator_dry_run='generator_dry_run.json',
 last_independent_allsource=42377,reviewed_examples=38,Lean_complete_graph_instances=0,
 new_BFS_performed=False,new_R4_performed=False,new_external_review=False,shared_Wiki_HTML_finalproof_modified=False))
# Reconcile local handoff labels with the parent's production acceptance decision.
for name in ['RESULT.json','terminal.json']:
 data=json.loads((H/name).read_text());data.update(root_final_strongest_check_pending=False,parent_pending=False,accepted_by_production_induction=True,
  root_independent_final_check_status='NOT_RUN_PARENT_ACCEPTED_EXISTING_PRODUCTION_INDUCTION',mathematical_examples_accepted_by_parent=1)
 save(H/name,data)
params=json.loads((H/'parameters.json').read_text());params.update(root_independent_final_check_pending=False,parent_pending=False,accepted_by_production_induction=True);save(H/'parameters.json',params)
for name in ['accepted_01.json','first_hit.json']:
 data=json.loads((H/name).read_text());data.update(parent_pending=False,accepted_by_production_induction=True);save(H/name,data)
report=(H/'REPORT.md').read_text().replace('independently verified42396-vertex source','previously accepted42396-vertex source (complete per-step degree/R4 induction; last allsource42377)')
report=report.replace("The parent's independent final graph acceptance is still pending here; no full-source BFS or external review was run by this agent.","The parent accepted this extension using the existing actualdegree and completeR4 production evidence and SingleExtension induction. No independent R4, full-source BFS or external review was added; latest independent allsource order remains42377.")
report=report.replace("The new graph's parent verification and any merge with another source42396 branch are separate next steps owned by the parent.","Parent acceptance is terminal: accepted_by_production_induction, parent_pending=false. The main delivery now contains58 literal examples, including55 degree12 prefixes through42397. Old57 literals, latest allsource42377, reviewed38 and Lean0 are preserved. One generator reconstruction exactly matches the produced edge set; no new R4, BFS or external review was performed. Any merge with another source42396 branch is outside this completed task.")
assert not screen(report);(H/'REPORT.md').write_text(report)
print('Delivered58: D12examples55; old57literals preserved; generator edge-set MATCH; no newR4/BFS/review.')
