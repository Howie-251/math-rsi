from pathlib import Path
import json
import time

begin = time.process_time()
HERE = Path(__file__).resolve().parent
assert not (HERE / 'run.json').exists()
cpp = (HERE.parent / 'search.cpp').read_text()


def replace_once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new)


cpp = replace_once(cpp,
    'int completed=0,best=1025,best_cursor=-1;bool found=false,timeout=false,calibrated=false;',
    'int completed=0,best=1025,best_cursor=-1,form_capacity_rejected=0,min_constant_bad=513,quotient_complete_legal=0;bool found=false,timeout=false,calibrated=false;')
cpp = replace_once(cpp,
    'for(int k=0;k<F;k++)for(int value=0;value<QP;value++)if(value!=source[free_edges[k]]){\n  int cursor=k*31+value-(value>source[free_edges[k]]);assert(cursor==completed);',
    'int cursor=-1;\n for(int ka=0;ka<F;ka++)for(int kb=ka+1;kb<F;kb++)for(int va=0;va<QP;va++)if(va!=source[free_edges[ka]])for(int vb=0;vb<QP;vb++)if(vb!=source[free_edges[kb]]){\n  cursor++;assert(cursor==completed);')
cpp = replace_once(cpp,
    'State q=source;q[free_edges[k]]=value;auto empty=make_forms(q);int total_empty=0;for(int x:empty)total_empty+=x;',
    'State q=source;q[free_edges[ka]]=va;q[free_edges[kb]]=vb;auto empty=make_forms(q);int total_empty=0;for(int x:empty)total_empty+=x;')
cpp = replace_once(cpp,
    'results<<"{\\"cursor\\":"<<cursor<<",\\"changed_edge\\":"<<free_edges[k]<<",\\"new_quotient_value\\":"<<value<<",\\"empty_slots_by_root\\":";list(results,empty);',
    'results<<"{\\"cursor\\":"<<cursor<<",\\"changed_edges\\":["<<free_edges[ka]<<\',\'<<free_edges[kb]<<"],\\"new_quotient_values\\":["<<va<<\',\'<<vb<<"],\\"empty_slots_by_root\\":";list(results,empty);')
cpp = replace_once(cpp,
    'center_entered++;scores.fill(0);legal.fill(false);solutions(constraints,[&](int z){legal[z]=true;});',
    '''quotient_complete_legal++;int constant_bad_slots=0;
  for(auto&forms:slots){assert(!forms.empty());auto first=forms[0];bool single=true;for(auto f:forms)if(f.mask!=first.mask||f.b!=first.b){single=false;break;}constant_bad_slots+=single;}
  min_constant_bad=min(min_constant_bad,constant_bad_slots);
  if(constant_bad_slots){form_capacity_rejected++;completed++;results<<",\\"status\\":\\"CENTRAL_FORM_CAPACITY_FAIL\\",\\"constant_bad_slots\\":"<<constant_bad_slots<<",\\"central_assignments_scored\\":0}\\n";continue;}
  center_entered++;scores.fill(0);legal.fill(false);solutions(constraints,[&](int z){legal[z]=true;});''')
cpp = cpp.replace('COMPLETE_403_NO_D3', 'COMPLETE_74958_NO_D3').replace('planned_projections\\":403', 'planned_projections\\":74958')
cpp = replace_once(cpp,
    'out<<",\\"best_projection_cursor\\":";',
    '''out<<",\\"quotient_complete_with_legal_center_space\\":"<<quotient_complete_legal<<",\\"central_form_capacity_rejected\\":"<<form_capacity_rejected<<",\\"minimum_constant_bad_slots_in_quotient_complete_legal_scope\\":";if(min_constant_bad<=512)out<<min_constant_bad;else out<<"null";
 out<<",\\"best_projection_cursor\\":";''')
(HERE / 'search.cpp').write_text(cpp)
driver = (HERE.parent / 'run.py').read_text()
driver = driver.replace('from calibrate import check', 'import sys\nsys.path.insert(0, str(Path(__file__).resolve().parent.parent))\nfrom calibrate import check')
driver = driver.replace("HERE.parent / 'nonabelian4_256_search'", "HERE.parent.parent / 'nonabelian4_256_search'")
driver = driver.replace("'../nonabelian4_256_search/best.independent_check.json'", "'../../nonabelian4_256_search/best.independent_check.json'")
driver = driver.replace('change exactly one of13 free quotient values to each of31 alternatives; original projection excluded',
                        'change exactly two distinct free quotient values to each of31 alternatives apiece; original and one-coordinate projections excluded')
driver = driver.replace('ascending free-edge index, then ascending alternative quotient code',
                        'lexicographic pair of free-edge indices, then ascending first and second alternative quotient codes')
driver = driver.replace("'planned_projections': 403", "'planned_projections': 74958")
driver = driver.replace("'projection_filter': 'reject if any of4x128 quotient target slots has no length<=3 walk',",
                        "'projection_filter': 'reject any empty quotient slot; then reject any slot with only one distinct(mask,b) form after legal-center feasibility',")
driver = driver.replace('remaining = 180 - preparation - 3',
                        "source_prep = json.loads((HERE / 'preparation.json').read_text())['CPU_seconds']\nremaining = 180 - preparation - source_prep - 3")
driver = driver.replace("'preparation_CPU_seconds': preparation, 'process_CPU_limit_seconds': remaining,",
                        "'preparation_CPU_seconds': preparation, 'source_preparation_CPU_seconds': source_prep, 'process_CPU_limit_seconds': remaining,")
driver = driver.replace('total_CPU_seconds=cpu() - begin,', 'source_preparation_CPU_seconds=source_prep, total_CPU_seconds=cpu() - begin + source_prep,')
driver = driver.replace("run['total_CPU_seconds'] = cpu() - begin", "run['total_CPU_seconds'] = cpu() - begin + source_prep")
(HERE / 'run.py').write_text(driver)
(HERE / 'preparation.json').write_text(json.dumps({
    'source': '../search.cpp and ../run.py; unchanged affine-system and group-word core',
    'new_scope': '74958 disjoint two-coordinate quotient changes from original832 source',
    'new_necessary_filter': 'reject any singleton distinct(mask,b) slot before central enumeration',
    'CPU_seconds': time.process_time() - begin, 'compiled': False, 'started': False,
}, indent=2) + '\n')
print('Prepared exactly74958 projections; no starts or graph generated.')
