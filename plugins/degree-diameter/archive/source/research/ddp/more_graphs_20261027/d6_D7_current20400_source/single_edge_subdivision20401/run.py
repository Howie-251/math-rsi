import json,pathlib,resource,subprocess,time
HERE=pathlib.Path(__file__).resolve().parent
CSR=HERE.parent/'rooted_wl_recovery/adjacency.csr.u32le.bin'
start=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+c.ru_utime+c.ru_stime-c0.ru_utime-c0.ru_stime
assert not (HERE/'RESULT.json').exists()
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],check=True)
compile_cpu=cpu()
subprocess.run([str(HERE/'probe'),str(CSR),str(HERE)],check=True,timeout=6)
r=json.loads((HERE/'NATIVE_RESULT.json').read_text())
r.update(compile_CPU_seconds=compile_cpu,total_batch_CPU_seconds=cpu(),
         hypothetical_n=20401,actual_n=20401 if r['hit'] else None,
         actual_D=7 if r['hit'] else None,ordinary_bad_unordered_pairs=0 if r['hit'] else None,
         pending=['Root independent newparameter acceptance'] if r['hit'] else [])
r['prediction']='SUPPORTED' if any(c['newroot_R7_missing']==0 for c in r['cases']) else 'REFUTED'
(HERE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
