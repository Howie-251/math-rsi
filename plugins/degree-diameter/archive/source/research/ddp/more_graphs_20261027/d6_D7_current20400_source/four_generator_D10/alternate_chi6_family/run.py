import json,pathlib,resource,subprocess,time
HERE=pathlib.Path(__file__).resolve().parent
START=time.process_time();Z=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+c.ru_utime+c.ru_stime-Z.ru_utime-Z.ru_stime
assert not (HERE/'RESULT.json').exists()
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],check=True)
compiled=cpu()
with (HERE/'probe.log').open('w') as log:
    subprocess.run([str(HERE/'probe'),str(HERE),str(9.5-cpu())],stdout=log,stderr=log,check=True,timeout=15)
r=json.loads((HERE/'NATIVE_RESULT.json').read_text())
r.update(compile_CPU_seconds=compiled,total_batch_CPU_seconds=cpu(),unattempted_settings=216-r['settings_processed'],
         actual_n=20400 if r['hit'] else None,actual_D=None,ordinary_bad_unordered_pairs=0 if r['hit'] else None,
         hypothetical_n=20400,prediction='SUPPORTED' if r['hit'] else 'UNRESOLVED' if r['CPU_limited'] else 'REFUTED',pending=[])
if r['hit']:
    h=json.loads((HERE/'FIRST_HIT.json').read_text());r.update(actual_D=h['actual_global_D'],graph_file=str(HERE/'graph_d4_D10_n20400.edges'),pending=['Root independent acceptance/Gemini'])
    recipe={'field':'F5','alpha_matrix':[[4,2],[1,1]],'beta_matrix':[[0,4],[1,4]],'chi17_alpha':6,
            'H_law':'(u,v)*(s,t)=(u+(-1)^v*s mod3,v+t mod16)','action':'rho(u,v)=beta^u alpha^v oncolumnvectors',
            'positive_generators':[{'V':[0,0],'c17':0,'u':0,'v':h['a']},{'V':h['normal_vector'],'c17':1,'u':1,'v':h['b']}],
            'inverse':'(-rho(h^-1)V,-6^(-v)*c,h^-1); computedinnewgroup',
            'vertex_encoding':'V=x+5*y;Q=c+17*(u+3*v);vertex=25*Q+V',
            'Cayley_diameter_proof':'Lefttranslations transitivelypreservealladjacency; actualcompleteidentityBFS gives exactwholeD.',
            'field_add':[[int((x+y)%5) for y in range(5)] for x in range(5)],
            'field_mul':[[int(x*y%5) for y in range(5)] for x in range(5)]}
    (HERE/'FIRST_HIT_RECIPE.json').write_text(json.dumps(recipe,indent=2)+'\n')
(HERE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');(HERE/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
