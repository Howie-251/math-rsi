import json,pathlib,resource,shutil,subprocess,time
HERE=pathlib.Path(__file__).resolve().parent
START=time.process_time();C0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    x=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+x.ru_utime+x.ru_stime-C0.ru_utime-C0.ru_stime
assert not (HERE/'RESULT.json').exists()
meta=json.loads((HERE/'normal6_matrix_forms.meta.json').read_text())
assert meta['status']=='READY_COMPLETE_TWO_MODEL_NORMAL6_MATRIX_FORMS'
old=json.loads((HERE.parent/'q9_D8_free_B/RESULT.json').read_text())
assert old['status']=='COMPLETE_FREE_B_FAMILY_NO_HIT'
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],check=True)
compiled=cpu()
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'NEW132698_RUNNING','compile_CPU_seconds':compiled,'budget_CPU_seconds':30,'inherited162_recomputed':False},indent=2)+'\n')
with (HERE/'search.log').open('w') as log:
    subprocess.run([str(HERE/'search'),str(HERE/'normal6_matrix_forms.bin'),str(HERE/'parameters.u8.bin'),
                    str(HERE/'field_tables.u8.bin'),str(HERE),str(29.5-cpu())],
                   stdout=log,stderr=log,check=True,timeout=40)
r=json.loads((HERE/'NATIVE_RESULT.json').read_text())
r.update(compile_CPU_seconds=compiled,total_batch_CPU_seconds=cpu(),unattempted_new_settings=132698-r['new_settings_processed'],
         all_projective_settings_two_models=132860,inherited_closed_settings=162,
         actual_n=None,actual_D=None,ordinary_bad_unordered_pairs=None,
         hypothesis_n=19440,prediction='SUPPORTED' if r['hit'] else 'UNRESOLVED' if r['CPU_limited'] else 'REFUTED',pending=[])
if r['hit']:
    actual=json.loads((HERE/'ACTUAL_GRAPH_RESULT.json').read_text());params=json.loads((HERE/'SURVIVOR_PARAMETERS.json').read_text())
    assert actual['accepted_D8'] and len(actual['roots'])==2
    im=json.loads((HERE/'FORMS_INPUT_META.json').read_text());m=next(x for x in im['models'] if x['scalar']==params['scalar'])
    recipe={'scalar':params['scalar'],'alpha':m['alpha'],'beta':m['beta'],'normal_tuple':params['normal_tuple'],
            'field':'FIELD_TABLES.json','group':'(F9² × C5) ⋊ (C3 ⋊ C8), ycy^-1=c^-1, χ_z(y)=2',
            'vertex_encoding':'base*9720+81*(z+5*(u+3v))+(x+9y)',
            'voltage_rule':'E=e,Y=y; A=(VA,c1,z1,y4),B=(VB,c1,z4,y7),D=(VD,c1,z4,y4);allinversescomputedinnewgroup.',
            'complete_roots':actual['roots'],'proof':'Leftdecktranslations aretransitiveineachtwo basefibres; bothidentityroots fullychecked.'}
    (HERE/'FIRST_HIT_RECIPE.json').write_text(json.dumps(recipe,indent=2)+'\n')
    r.update(actual_n=19440,actual_D=actual['actual_global_D'],ordinary_bad_unordered_pairs=0,
             graph_file=str(HERE/'graph_d5_D8_n19440.edges'),pending=['Root independent acceptance/Gemini'])
(HERE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':r['status'],'new_settings_processed':r['new_settings_processed'],'total_batch_CPU_seconds':r['total_batch_CPU_seconds'],'pending':r['pending']},indent=2)+'\n')
print(json.dumps(r,indent=2))
