"""The only216-family producer;3controls inherited,<=213new ordinaryrootBFS."""
from array import array
from pathlib import Path
import json
import resource
import subprocess
import time

START=time.process_time();CHILD=resource.getrusage(resource.RUSAGE_CHILDREN)
OUT=Path(__file__).resolve().parent;BASE=OUT.parent.parent
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+c.ru_utime+c.ru_stime-CHILD.ru_utime-CHILD.ru_stime
def read(path):
    a=array('I');a.frombytes(Path(path).read_bytes());return a
def save(name,data):(OUT/name).write_text(json.dumps(data,indent=2)+'\n')

assert (OUT/'normalization_proof/PROOF.md').exists()
assert (OUT/'normalization_proof/CONTROL_IDENTITIES.json').exists()
meta=json.loads((BASE/'rooted_wl_recovery/six_generators/GENERATORS.json').read_text())
alpha=read(meta['generators'][0]['map_file']);beta=read(BASE/'h48_complement/beta.pi.u32le.bin')
na=read(BASE/'normal425_cover/a5.pi.u32le.bin');nb=read(BASE/'normal425_cover/b5.pi.u32le.bin');nz=read(BASE/'normal425_cover/z17.pi.u32le.bin')
n=20400;bp=[array('I',range(n))]
for _ in range(4):bp.append(array('I',(nb[x] for x in bp[-1])))
nv=[array('I',(na[bp[t][nz[x]]] for x in range(n))) for t in range(5)]
nv.append(array('I',(nb[nz[x]] for x in range(n))))
with (OUT/'INPUT_PERMS.u32le.bin').open('wb') as f:
    f.write(array('I',[n]).tobytes())
    for a in [alpha,*nv,beta]:assert len(a)==n;f.write(a.tobytes())
save('THEORY_BINDING.json',{'coverage_status':'VALID','source':'normalization_proof/PROOF.md',
                          'oldcontrol_skip_status':'VALID','skip_identities':'normalization_proof/CONTROL_IDENTITIES.json',
                          'skipped_ordinals':[28,31,135],
                          'all_cases_connected':'Provedviaalphaandk=(v,1,beta),k^3givesC17;alpha²commutatordifferencegives2v;irreducibleX²−3givesV25'})
before=cpu();ret=subprocess.run(['g++','-O3','-std=c++17',str(OUT/'search.cpp'),'-o',str(OUT/'search')],capture_output=True,text=True)
assert ret.returncode==0,ret.stderr
compile_cpu=cpu()-before
remaining=10.0-cpu()-.20
assert remaining>0
save('checkpoint.json',{'status':'THEORY_VALID_AND_CONTROLS_VALID_NATIVE_RUNNING','fixed_cases':216,'inherited_skipped':3,
                       'parent_children_CPU_before_native':cpu(),'native_budget':remaining})
with (OUT/'native.log').open('w') as log:
    ret=subprocess.run([str(OUT/'search'),str(OUT/'INPUT_PERMS.u32le.bin'),str(OUT),str(remaining)],stdout=log,stderr=log,timeout=20)
if ret.returncode:
    result={'status':'UNKNOWN_NATIVE_PROCESS_FAILURE','returncode':ret.returncode,'parent_children_CPU_seconds':cpu(),
            'source_BFS':0,'running':False,'pending':[]}
else:
    result=json.loads((OUT/'NATIVE_RESULT.json').read_text())
    result.update(target_Delta=4,target_D=10,savedL=19306,source_group_order=20400,
                  coverage_theory_status='VALID',prior_controls_mapping_status='VALID',
                  compiled_CPU_seconds=compile_cpu,total_parent_children_CPU_seconds=cpu(),
                  old_source_D7_BFS=0,global_D_basis='Gammaactualregular;abstractrightregularaction preservesnewleftCayleyedges;connectedroot0ecc=globalD',
                  generator_vectors=[[1,0],[1,1],[1,2],[1,3],[1,4],[0,1]],
                  all_connected_by_theory=True,generator_tuning=False,running=False,pending=[])
    if result['hit_ordinal']>=0:
        hit=next(r for r in result['rows'] if r['ordinal']==result['hit_ordinal'])
        hit['normal5_vector']=result['generator_vectors'][hit['v_index']]
        recipe={'n':20400,'m':40800,'degree':4,'actual_D':hit['global_D'],
                'a':hit['a'],'b':hit['b'],'normal5_vector':hit['normal5_vector'],'c17':1,
                'first_generator':'purealpha^a','second_generator':'N(v5,c17=1)*actualHbeta*alpha^b',
                'source_semidirect_recipe':str(BASE/'h48_complement/SOURCE_SEMIDIRECT_RECIPE.json'),
                'permutations_file':str(OUT/'HIT_PERMUTATIONS.u32le.bin'),
                'permutation_layout':'4rows of20400uint32: first,firstinverse,second,secondinverse',
                'graph_file':str(OUT/'graph_d4_D10_n20400.edges'),
                'root_distance_file':str(OUT/'HIT_ROOT0_DISTANCES.u8.bin'),
                'edge_rule':'v--pi_s(v),leftCayley;notclaimoldsourceedgesubgraph',
                'diameter_proof':result['global_D_basis'],'parent_independent_acceptance_pending':True}
        save('HIT_RECIPE.json',recipe);result['hit']=hit;result['graph_file']=recipe['graph_file']
save('RESULT.json',result);save('terminal.json',result);save('checkpoint.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
