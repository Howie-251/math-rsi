import json,pathlib,resource,subprocess,time
HERE=pathlib.Path(__file__).resolve().parent
RECIPE=HERE.parent/'COVER_RECIPE.json'
start=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+c.ru_utime+c.ru_stime-c0.ru_utime-c0.ru_stime
assert not (HERE/'RESULT.json').exists()
pred=json.loads((HERE/'PREDICTION.json').read_text())
allowed=pred['capacity_permitted_moduli']
assert all(m in [18,19] for m in allowed) and allowed
a=json.loads(RECIPE.read_text())
assert a['source_n']==20400 and a['source_m']==61200 and a['base_count']==48 and a['moduli']==[5,5,17]
assert a['full_source_edges_matched']==61200 and a['reverse_port_binding_checked']
rows=a['base_ports'];assert len(rows)==48
with (HERE/'ports.centered.txt').open('w') as out:
    for v,row in enumerate(rows):
        assert row['base']==v and len(row['darts'])==6
        for k,d in enumerate(row['darts']):
            assert d['port']==k
            c=d['c17'];c=c if c<=8 else c-17
            out.write(f'{d["to"]} {d["a"]} {d["b"]} {c} {d["reverse_port"]}\n')
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],check=True)
compiled=cpu()
with (HERE/'probe.log').open('w') as log:
    subprocess.run([str(HERE/'probe'),str(HERE/'ports.centered.txt'),str(HERE),*map(str,allowed)],stdout=log,stderr=log,check=True,timeout=12)
native=json.loads((HERE/'NATIVE_RESULT.json').read_text())
cases=[json.loads((HERE/f).read_text()) for f in native['case_result_files']]
r={'status':'FIRST_COMPLETE_HIT' if native['hit'] else 'FROZEN_CYCLIC_MODULI_COMPLETE_NO_HIT','cases':cases,
   'fixed_moduli':[18,19],'capacity_permitted_moduli':allowed,'case_moduli_evaluated':[x['m'] for x in cases],
   'compile_CPU_seconds':compiled,'native_CPU_seconds':native['native_CPU_seconds'],'total_batch_CPU_seconds':cpu(),
   'source_BFS':0,'source_decode_repeated':0,'Aut_or_normal_recovery_repeated':0,
   'prediction':'SUPPORTED' if native['hit'] else 'REFUTED',
   'actual_n':next((x['n'] for x in cases if x['complete_D7']),None),
   'actual_D':next((x['actual_global_D'] for x in cases if x['complete_D7']),None),
   'ordinary_bad_unordered_pairs':0 if native['hit'] else None,
   'pending':['Root independent first newparameter acceptance'] if native['hit'] else []}
(HERE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
