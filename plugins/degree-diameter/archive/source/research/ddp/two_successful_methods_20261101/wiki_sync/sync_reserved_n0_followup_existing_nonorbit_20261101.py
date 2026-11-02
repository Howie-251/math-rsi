"""Update existing448 node only; execute after449 owner explicitly releases Wiki."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import copy
import json
import runpy
import time

START=time.process_time()
R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki'
S='research/ddp/two_successful_methods_20261101/'
P=S+'retained_edge_transfer/published_d15_15552_D4_source_gate/nonorbit_clone_interface/reserved_neighborhood_block_selection16417/'
OUT=R/S/'wiki_sync'
RID='ddp-d16d4-source15552-nonorbit-fulln-local-exchange-no-global-unknown-20261101'
LABEL='RESERVED_N0_EXISTING_NONORBIT_FOLLOWUP_20261101'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def read(p):return json.loads((R/p).read_text())


def main():
    d=read(P+'RESULT.json');t=read(P+'TERMINAL.json');m0=read(P+'MODEL.json')
    assert d['status']=='UNKNOWN_NO32_IN_SINGLE_WINDOW'
    assert d['selected_count']==31 and not d['candidate_generated']
    assert d['returned_binary_allrows_handchecked'] and d['warm_set_status']=='HighsStatus.kOk'
    assert d['raw_solver']['model_status']=='HighsModelStatus.kTimeLimit'
    assert d['raw_solver']['mip_node_count']==7811
    assert t['all_processes_terminal'] and t['retries']==0
    assert abs(t['cumulative_CPU_seconds']-99.304068265)<1e-8
    assert m0['variables']==192 and m0['compressed_capacity_rows']==216
    assert m0['cardinality_rows']==1 and m0['nonzeros']==1248
    L=read('research-wiki/DDP_METHOD_LEDGER.json')
    before=L['record_count'];records={x['id']:x for x in L['rows']}
    assert before==449 and len(records)==449 and RID in records
    counts={k:L[k]for k in L if k!='rows'and any(z in k for z in ['graph_examples','parameter_pairs','Lean_graph_instances'])}
    # These are untouched byte-for-byte, including human top and449's new nav.
    protected={str(p.relative_to(R)):p.read_bytes()for p in [W/'index.md',W/'query_pack.md',W/'gap_map.md']}
    raw=copy.deepcopy(records[RID]['source_record']);metrics=raw.setdefault('other_metrics',{})
    assert 'reserved_N0_block_lookahead_actual' not in metrics
    metrics['before_reserved_N0_followup_snapshot']=dict(outcome_class=raw.get('outcome_class'),
        distance_text=raw.get('distance_text'),lesson=raw.get('lesson_and_restart_condition'))
    metrics['reserved_N0_block_lookahead_actual']=dict(
        status=d['status'],v0=0,actual_source_N0_size=14,block_variables=192,
        actual_old_rows_bound=15552,compressed_capacity_rows=216,cardinality_rows=1,nonzeros=1248,
        capacity='16-source_degree-1_N0; identicalfullrowcoeffsusetightestcap',
        olddegree14_capacity2_preserved_outside_N0=True,
        wholeW27_sourcecenter_rule='81*i+a+9*b+27*c; accepted27offsetorder',
        sumy_at_most32_objective_maxsum=True,y0_zero_extra0_distinctness=True,
        old_I32_is_warm_only_not_fixed=True,warm_count=31,warm_dropped_block=[0],
        actual_setSolution='HighsStatus.kOk',best_count=31,
        raw_model_status=d['raw_solver']['model_status'],raw_primal=d['raw_solver']['objective_function_value'],
        raw_dual=d['raw_solver']['mip_dual_bound'],raw_gap=d['raw_solver']['mip_gap'],
        actual_mip_nodes=7811,log_LP_iterations=577486,
        all15552reservedcaps_and_binary_handchecked=True,
        candidate_generated=False,no32_certified=False,run_calls=1,retries=0,
        prior_nonorbit_line_CPU=68.299114264,new_prep_charge=.5,
        actual_child_CPU=t['actual_child_CPU_seconds'],actual_driver_CPU=t['actual_driver_CPU_seconds'],
        cumulative_nonorbit_line_CPU=t['cumulative_CPU_seconds'],cumulative_cap=120,
        other_combination_C_line_CPU_not_added=True,
        graph_field_oldD4_BFS_Lean_ARIS=0,global_priority='UNKNOWN',
        STOP_no_other_v_seed_secondsolve=True)
    raw['distance_text']=(raw.get('distance_text','')+' 后续预留实际source N(0)14pins再重选32个W27块：literal15552行压216组取mincap＋sum≤32，192vars/217rows/1248nnz，old14cap2保留；旧I32删块0暖31，setSolutionkOk。唯一30s窗口进入7811nodes、577486LPiterations，但best31/rawdual约32/timeLimit，未得32，0图；累计nonorbit99.304068265/120（不混另一C-line成本）。仍UNKNOWN，不证明无32。')
    raw['outcome_class']='LOCAL_EXCLUSIONS_GLOBAL_AND_RESERVED_N0_LOOKAHEAD_UNKNOWN_STOP'
    raw['scope']=(raw.get('scope','')+' Same-nodefollowup:fixedv0=0originalN14reserved,192wholeW27blocksreselectedfromliteralincidence,olddegree14cap2retained,rowcoefficientduplicatescompressedwithminimumcap,sumy<=32/maxsum,warm31andone30stimewindow. Onlyreturn32wouldmake865distinctfullNclones/16417;actual31timeLimitisUNKNOWN,notno32. Doesnotretainprivate16416cloneedges,doesnotfixoldI32exceptstart.')
    raw['lesson_and_restart_condition']=('STOPbothcompletedglobalandthisreserved-v0window;donotresumeMIPorchangev/seedautomatically. Thelookaheadmatrixispin-levelactualoldNcapacity,notcompletedtargetdisjointapproximation;old14overlapsremain. Thissmallmodeldidbranch7811nodesbuttimeLimitwith31isnotmaximum31orfullsourceNO. Local<=4outclosuresremainhistoricalandscoped;global>864andfixedv0-32questionremainOPEN. SeparateCombinationCterminalisitsown449nodeandnotanewgraph.')
    raw['restart_condition']='Anewroot-authorizedconcretegeneratingrulebeyondthesestoppedwindows,nosecondsolver/v1/seedorlocalswapladderautomatically.'
    raw['unclosed_gap']='GlobalallcenterfullNpacking>864andfixedv0reserved32wholeblockfeasibilityremainUNKNOWN. No16417candidate,nogeneral16D4upperbound,max864notcertified. Same153/43/Lean47;separateCombinationCnode449keepsitsowncostandscope.'
    raw.setdefault('positive_guarantees',[]).extend([
        'LiteralA[w,i]countseveryactualoldNcontribution;ordinarycap16-degreeandprotectedcap15-degreeareexactolddegreeconditions,includingold14cap2.',
        'Identicalfull192coefficientrowscanbecompressedbyminimumcapwithall15552rowmapping;notbyguessedtargetlabels.',
        'sumy<=32withmaxsumhasvalue32iff32blocksarefeasible,buttimeLimitreturned31doesnotexclude32.',
        'Future865clonegraphwouldretainoriginal15552oldedgesonly;notprivate16416cloneedges. No graphwaswrittenbecauseactualbest31.'
    ])
    names=['PRED.md','run_once.py','MODEL.json','ALL15552_ROW_MAPPING.tsv','ROW_GROUPS.json',
           'WARM_START_INPUT.json','WARM_START_RETURN.json','RAW_SOLVER_RETURN.json','BEST_HANDCHECK.json',
           'RESULT.json','TERMINAL.json','FINAL.json','NOTE.md','MODEL_EXACTNESS_PAPER.md','MODEL_READ_REVIEW.md','SOLVER_STDOUT.log']
    if (R/P/'ROOT_DISPOSITION.json').is_file():names.append('ROOT_DISPOSITION.json')
    paths=[P+x for x in names];assert all((R/x).is_file()for x in paths)
    raw.setdefault('evidence_paths',[]).extend(x for x in paths if x not in raw['evidence_paths'])
    rowpath=OUT/f'{LABEL}_ROW.json';rowpath.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
    api=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
    helper=api['helper'];helper.rebuild_index=lambda *a,**k:None;helper.rebuild_query_pack=lambda *a,**k:None
    n=api['normalize'](raw);n['goal']['baseline_date']=raw.get('baseline_date',records[RID]['goal']['baseline_date'])
    assert n['id']==RID
    with (OUT/f'{LABEL}_NODE_CALLS.log').open('w')as log,contextlib.redirect_stdout(log):api['write_node'](n)
    records[RID]=n;L.update(rows=list(records.values()),updated_UTC=NOW)
    L['input_counts'][str(rowpath.relative_to(R))]=1
    (W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
    path=W/'DDP_METHOD_LEDGER.md';lines=path.read_text().splitlines()
    ix=[i for i,s in enumerate(lines)if s.startswith('| [')and '(experiments/'+RID+'.md)'in s]
    assert len(ix)==1
    safe=api['safe']
    lines[ix[0]]='| ['+safe(n['title'])+'](experiments/'+RID+'.md) | '+safe(api['goal_text'](n))+' | '+safe(api['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[N0 followup](../'+P+'NOTE.md) |'
    text='\n'.join(lines)+'\n';assert LABEL not in text
    text+='\n<!-- '+LABEL+' -->\n已有非orbit448节点原位追加：预留sourceN(0)后全192个W27块重选，唯一30s窗口7811nodes返回31、rawdual约32，未达32条件，UNKNOWN而非无32；0图、累计nonorbit99.304068265/120。449的CombinationC独立成本/终态保留，不增节点/方法/数学计数。\n'
    path.write_text(text)
    helper.append_log(str(W),LABEL+': existing448nodefollowuponly;449recordsunchanged. ReservedactualN0/192wholeW27/216mincapgroups,old14cap2,fullrowmapping;warm31kOk,30stimeLimit7811nodesbest31dualabout32UNKNOWN,no32proof/nograph. Nonorbit99.304068265/120includingpriorglobalandAPI;otherClinecostnotadded. No rebuild,index/query/gaphumantop exact,rootfilesuntouched,nofurthernumeric.')
    for p,old in protected.items():assert (R/p).read_bytes()==old
    after=read('research-wiki/DDP_METHOD_LEDGER.json')
    assert after['record_count']==before and len(after['rows'])==before
    assert {k:after[k]for k in counts}==counts
    receipt=dict(status='PASS_EXISTING448_RESERVED_N0_FOLLOWUP_UPSERT',updated_UTC=NOW,
       records_before=before,records_after=before,records_added=0,updated_id=RID,
       graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
       actual_followup_status=d['status'],candidate_generated=False,
       best31_not_no32=True,actual_nodes7811=True,cumulative_nonorbit_CPU_seconds=99.304068265,
       old_global_and_local_history_preserved=True,other449node_and_Cline_cost_separate=True,
       index_query_gap_and_human_top_byte_preserved=True,full_rebuild_or_reimport=False,
       root_STATE_ROUND_progress_REPORT_HTML_builder_files_modified=False,
       numeric_BFS_field_solver_Lean_ARIS_hash_runs=0,
       links_checked_by_fileexistence=len(paths),actual_sync_CPU_seconds=time.process_time()-START)
    (OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(receipt,ensure_ascii=False))


if __name__=='__main__':main()
