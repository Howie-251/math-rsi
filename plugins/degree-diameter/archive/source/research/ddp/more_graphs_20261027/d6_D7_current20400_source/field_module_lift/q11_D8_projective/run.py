import json,pathlib,resource,shutil,subprocess,sys,time
HERE=pathlib.Path(__file__).resolve().parent
FORMS=pathlib.Path(sys.argv[1]).resolve()
START=time.process_time();C0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+r.ru_utime+r.ru_stime-C0.ru_utime-C0.ru_stime
assert not (HERE/'RESULT.json').exists()
old=json.loads((HERE.parent/'q11_D8_control/RESULT.json').read_text())
assert old['connected'] and old['actual_global_D']==9 and not old['accepted_D8']
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],check=True)
compiled=cpu()
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'GENERIC_1463_RUNNING','forms':str(FORMS),'compile_CPU_seconds':compiled,'CPU_budget':30},indent=2)+'\n')
with (HERE/'search.log').open('w') as log:
    subprocess.run([str(HERE/'search'),str(FORMS),str(HERE/'parameters.txt'),str(HERE),str(29.5-cpu())],
                   stdout=log,stderr=log,check=True,timeout=40)
r=json.loads((HERE/'NATIVE_RESULT.json').read_text())
r.update(compile_CPU_seconds=compiled,total_batch_CPU_seconds=cpu(),
         unattempted_new_settings=1463-r['new_settings_processed'],inherited_control_count=1,
         all_projective_classes=1464,D7_preplanned2625_included=False,
         actual_n=None,actual_D=None,ordinary_bad_unordered_pairs=None,
         prediction='SUPPORTED' if r['hit'] else 'UNRESOLVED' if r['CPU_limited'] else 'REFUTED',pending=[])
if r['hit']:
    actual=json.loads((HERE/'ACTUAL_GRAPH_RESULT.json').read_text())
    params=json.loads((HERE/'SURVIVOR_PARAMETERS.json').read_text())
    assert actual['accepted_D8'] and actual['connected']
    tables=HERE.parent/'representation_tables/q11_control/TABLES.json'
    shutil.copyfile(tables,HERE/'HIT_FIELD_TABLES.json')
    recipe=json.loads((HERE.parent/'q11_D8_control/RECIPE.json').read_text())
    v=params['normal_tuple'];recipe['positive_generators'][1]['normal']=v[:2];recipe['positive_generators'][2]['normal']=v[2:]
    recipe['normal_tuple']=v;recipe['field_TABLES']='HIT_FIELD_TABLES.json'
    (HERE/'FIRST_HIT_RECIPE.json').write_text(json.dumps(recipe,indent=2)+'\n')
    r.update(actual_n=98736,actual_D=actual['actual_global_D'],ordinary_bad_unordered_pairs=0,
             graph_file=str(HERE/'graph_d6_D8_n98736.edges'),
             pending=['Root independent acceptance/Gemini'])
(HERE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':r['status'],'settings_processed':r['new_settings_processed'],'total_batch_CPU_seconds':r['total_batch_CPU_seconds'],'pending':r['pending']},indent=2)+'\n')
print(json.dumps(r,indent=2))
