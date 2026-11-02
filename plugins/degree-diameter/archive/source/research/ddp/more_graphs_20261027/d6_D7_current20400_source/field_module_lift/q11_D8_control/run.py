import json,pathlib,resource,subprocess,time
HERE=pathlib.Path(__file__).resolve().parent
start=time.process_time();zero=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+c.ru_utime+c.ru_stime-zero.ru_utime-zero.ru_stime
assert not (HERE/'RESULT.json').exists()
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],check=True)
compiled=cpu()
subprocess.run([str(HERE/'probe'),str(HERE)],check=True,timeout=5)
r=json.loads((HERE/'NATIVE_RESULT.json').read_text())
r.update(compile_CPU_seconds=compiled,total_batch_CPU_seconds=cpu(),actual_n=98736,
         ordinary_bad_unordered_pairs=0 if r['accepted_D8'] else None,
         separate_from_D7_projective_2625=True,
         pending=['Root independent acceptance/Gemini'] if r['accepted_D8'] else [])
(HERE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
recipe={'q':11,'field':'integersmod11','alpha':[[7,5],[1,4]],'beta':[[0,10],[1,10]],
        'H':'beta^u alpha^v; (u,v)*(s,t)=(u+(-1)^v*s mod3,v+t mod16)',
        'chi17':'5^v mod17','module_action':'rho(u,v)=beta^u alpha^v oncolumnvectors',
        'positive_generators':json.loads((HERE/'PREDICTION.json').read_text())['positive_generators'],
        'inverse':'(-rho(h^-1)V,-5^(-v)*c,h^-1), recomputedinthenewfield',
        'vertex_encoding':'V=x+11*y; Q=c+17*(u+3*v); vertex=121*Q+V',
        'source_recipe':'../../h48_complement/SOURCE_SEMIDIRECT_RECIPE.json',
        'field_add':[[int((x+y)%11) for y in range(11)] for x in range(11)],
        'field_mul':[[int(x*y%11) for y in range(11)] for x in range(11)]}
(HERE/'RECIPE.json').write_text(json.dumps(recipe,indent=2)+'\n')
print(json.dumps(r,indent=2))
