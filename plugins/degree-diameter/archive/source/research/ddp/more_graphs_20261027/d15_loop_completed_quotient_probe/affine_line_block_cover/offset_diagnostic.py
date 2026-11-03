"""Read only existing line masks; supply every raw line to joint cover."""
from pathlib import Path
from collections import Counter,defaultdict
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(5,5))
START=time.process_time()
P=Path(__file__).resolve().parent
assert json.loads((P/'OFFSET_DIAGNOSTIC_PREDICTION.json').read_text())['frozen_before_reading_grouped_mask_values']
sources=[]
for label,n,D,expected_lines in [('source15552',15552,4,2808),('source102060',102060,5,3510)]:
    stored=json.loads((P/f'{label}_LINE_BLOCK_MASKS.json').read_text())
    free=json.loads((P.parent/'full_free_directions'/f'{label}_FREE_DIRECTION_GROUPS.json').read_text())
    rows=stored['raw_lines']
    assert stored['n']==free['n']==n and len(rows)==expected_lines
    assert [row['raw_line_index'] for row in rows]==list(range(expected_lines))
    ballorder=free['literal_free_ball_row_order']
    pin_to_row={pin:i for i,pin in enumerate(ballorder)}
    assert len(pin_to_row)==len(ballorder)==free['free_pin_count']
    groups=defaultdict(list)
    joint_lines=[]
    for row in rows:
        assert len(row['pins'])==len(set(row['pins']))==3
        assert all(pin in pin_to_row for pin in row['pins'])
        assert all(pin//free['bin_size']==row['controller'] for pin in row['pins'])
        key=(row['controller'],row['direction_index'])
        groups[key].append(row)
        joint_lines.append({'line_id':row['raw_line_index'],
                            'selector_variable':row['raw_line_index']+1,
                            'controller':row['controller'],
                            'direction_index':row['direction_index'],
                            'local_offsets':row['local_offsets'],
                            'pins':row['pins'],'cost':3,
                            'ball_row_indices':[pin_to_row[pin] for pin in row['pins']]})
    assert len(groups)==13*free['loop_controller_count']
    equal_groups=0
    equal_comparisons=0
    comparisons=0
    distinct_hist=Counter()
    first=None
    group_details=[]
    for (controller,direction),cosets in sorted(groups.items()):
        assert len(cosets)==9 and len({tuple(c['pins']) for c in cosets})==9
        masks=[int(c['blockmask_decimal']) for c in cosets]
        distinct=len(set(masks))
        distinct_hist[distinct]+=1
        all_equal=distinct==1
        equal_groups+=all_equal
        for i in range(1,9):
            comparisons+=1
            match=masks[i]==masks[0]
            equal_comparisons+=match
            if not match and first is None:
                first={'controller':controller,'direction_index':direction,
                       'first_line_id':cosets[0]['raw_line_index'],
                       'other_line_id':cosets[i]['raw_line_index'],
                       'first_pins':cosets[0]['pins'],'other_pins':cosets[i]['pins'],
                       'first_blockmask_decimal':str(masks[0]),'other_blockmask_decimal':str(masks[i])}
        group_details.append({'controller':controller,'direction_index':direction,
                              'coset_line_ids':[c['raw_line_index'] for c in cosets],
                              'distinct_block_masks':distinct,'all_nine_equal':all_equal})
    interface={'source':label,'n':n,'m':free['m'],'D':D,'Delta':15,
               'bin_size':free['bin_size'],'line_count':len(joint_lines),
               'line_ids_base':0,'selector_variables_base':1,'ball_row_indices_base':0,
               'cache_paths_relative_to':'research/ddp/more_graphs_20261027',
               'cache':free['cache'],'literal_free_ball_row_order':ballorder,
               'lines':joint_lines,
               'all_raw_lines_preserved':True,
               'selected_line_budget':5,
               'distinct_pin_rule':'Union selected pins before adding spokes; at most5 lines gives at most15 distinct pins.',
               'no_blockmask_deduplication':'Equal full-fibre block columns do not imply equal partial-target or joint-fibre coverage. Every original coset remains a separate line object.'}
    interface_name=f'{label}_JOINT_LINE_INTERFACE.json'
    (P/interface_name).write_text(json.dumps(interface,ensure_ascii=False,indent=2)+'\n')
    summary={'source':label,'n':n,'D':D,'raw_lines':len(rows),
             'controller_count_with_lines':free['loop_controller_count'],
             'direction_groups':len(groups),'cosets_per_group':9,
             'groups_with_all_nine_masks_equal':equal_groups,
             'all_groups_equal':equal_groups==len(groups),
             'nonreference_coset_comparisons':comparisons,
             'equal_nonreference_coset_comparisons':equal_comparisons,
             'distinct_masks_per_group_histogram':dict(sorted(distinct_hist.items())),
             'first_counterexample':first,
             'joint_cover_interface':interface_name,
             'interface_all_lines_pins_cache_rows_checked':True,
             'group_details':group_details}
    sources.append(summary)
result={'status':'COMPLETE_STORED_OFFSET_BLOCKMASK_AND_JOINT_INTERFACE_CHECK',
        'prediction_status':'SUPPORTED' if all(s['all_groups_equal'] for s in sources) else 'REFUTED',
        'sources':sources,'CPU_seconds':time.process_time()-START,
        'scope':'Only equality of previously computed full-fibre block columns; no equivalence of cached line balls, partial-target columns or simultaneous line choices is asserted.',
        'new_balls':0,'cached_ball_OR':0,'BFS':0,'solver_calls':0,'new_graphs':0}
(P/'OFFSET_DIAGNOSTIC.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({**result,'sources':[{k:v for k,v in s.items() if k!='group_details'} for s in sources]},ensure_ascii=False))
