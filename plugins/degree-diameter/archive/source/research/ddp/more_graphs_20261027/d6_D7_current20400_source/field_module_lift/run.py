from array import array
import itertools
import json
import pathlib
import resource
import shutil
import struct
import subprocess
import sys
import time

HERE=pathlib.Path(__file__).resolve().parent
START=time.process_time()
CHILD0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+c.ru_utime+c.ru_stime-CHILD0.ru_utime-CHILD0.ru_stime
assert sys.byteorder=='little'
assert not (HERE/'RESULT.json').exists()
source=json.loads((HERE.parent/'h48_complement/SOURCE_SEMIDIRECT_RECIPE.json').read_text())
assert source['full_source_directed_adjacencies_matched']==122400
assert source['full_source_undirected_edges_matched']==61200
index=json.loads((HERE/'representation_tables/REPRESENTATIONS.json').read_text())
assert index['status']=='VALID_ALL_FOUR_D7_REPS_AND_SINGLE_Q11_D8_CONTROL'
reps=[r for r in index['representations'] if r['target_D']==7]
assert [r['name'] for r in reps]==['q7','q8','q9_plusg','q9_minusg']
models=[]
for rep in reps:
    tablepath=HERE/'representation_tables'/rep['TABLES']
    table=json.loads(tablepath.read_text())
    assert table['status']=='VALID_SPECIFIED_REPRESENTATION_AND_ORDERS'
    models.append((rep,table,tablepath))
first=models[0][1]
Hinv=first['H_inv'];Hmul=first['H_mul'];chi=first['chi17']
positive=source['positive_generators']
assert [(x['c17'],x['u'],x['v']) for x in positive]==[(0,0,1),(1,1,12),(5,2,11)]
gq=[];invh=[]
for x in positive:
    h=x['u']+3*x['v'];hi=Hinv[h];invh.append(hi)
    gq.extend([x['c17']+17*h,(-chi[hi]*x['c17'])%17+17*hi])
qmove=[]
for g in range(816):
    c,h=g%17,g//17
    for s in gq:
        d,k=s%17,s//17
        qmove.append((c+chi[h]*d)%17+17*Hmul[h][k])
for s in range(3):
    assert qmove[6*gq[2*s]+2*s+1]==0
    assert qmove[6*gq[2*s+1]+2*s]==0
bindings=[]
with (HERE/'prepared_models.bin').open('wb') as output:
    output.write(struct.pack('<4sI',b'FML1',4))
    array('H',gq).tofile(output);array('H',invh).tofile(output);array('H',qmove).tofile(output)
    for rep,t,path in models:
        f=t['field'];q=f['q'];p=f['characteristic'];L=q*q
        add,mul,neg,inv=f['add'],f['mul'],f['neg'],f['inv']
        points=[]
        for pivot in range(4):
            for suffix in itertools.product(range(q),repeat=3-pivot):
                points.append((0,)*pivot+(1,)+suffix)
        assert len(points)==rep['parameter_cases']
        control=[v%p for v in [0,2,0,-1]]
        if any(control):
            scalar=inv[next(v for v in control if v)]
            control=tuple(mul[scalar][v] for v in control)
            assert list(control)==t['control_tuple_Bx_By_Cx_Cy']
            points.remove(control);points.insert(0,control)
        else:
            control=None
        vectoradd=[add[x%q][y%q]+q*add[x//q][y//q] for x in range(L) for y in range(L)]
        vectorneg=[neg[x%q]+q*neg[x//q] for x in range(L)]
        rho=[v for row in t['rho_on_vectors'] for v in row]
        assert len(rho)==48*L and t['chi17']==chi and t['H_inv']==Hinv
        name=rep['name'].encode()
        output.write(struct.pack('<I',len(name)));output.write(name)
        output.write(struct.pack('<II',q,len(points)))
        output.write(bytes(vectoradd));output.write(bytes(vectorneg));output.write(bytes(rho))
        output.write(bytes(v for point in points for v in point))
        bindings.append({'name':rep['name'],'q':q,'characteristic':p,'TABLES':str(path),
                         'n':816*L,'cases':len(points),'control_first':list(control) if control else None,
                         'alpha':t['alpha_matrix'],'beta':t['beta_matrix']})
(HERE/'MODEL_BINDINGS.json').write_text(json.dumps({'status':'VALIDATED_INPUTS_BOUND_BEFORE_SEARCH','models':bindings,
       'quotient_generators_positive_and_true_inverses':gq,'inverse_H_positive':invh,
       'node_encoding':'module=x+q*y;Q=c+17*(u+3v);node=q²*Q+module',
       'source_recipe':'../h48_complement/SOURCE_SEMIDIRECT_RECIPE.json'},indent=2)+'\n')
prepared=cpu()
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],check=True)
compiled=cpu()-prepared
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'NATIVE_2625_RUNNING','budget_CPU_seconds':30,'input_prepare_CPU_seconds':prepared,'compile_CPU_seconds':compiled},indent=2)+'\n')
with (HERE/'search.log').open('w') as log:
    subprocess.run([str(HERE/'search'),str(HERE/'prepared_models.bin'),str(HERE),str(29.5-cpu())],
                   stdout=log,stderr=log,check=True,timeout=45)
r=json.loads((HERE/'NATIVE_RESULT.json').read_text())
r.update(input_prepare_CPU_seconds=prepared,compile_CPU_seconds=compiled,total_batch_CPU_seconds=cpu(),
         unattempted_settings=2625-r['settings_processed'],q11_control_included=False,
         actual_n=None,actual_D=None,ordinary_bad_unordered_pairs=None,
         prediction='SUPPORTED' if r['hit'] else 'UNRESOLVED' if r['CPU_limited'] else 'REFUTED',
         pending=[])
if r['hit']:
    hit=json.loads((HERE/'FIRST_HIT.json').read_text())
    selected=next((rep,t,path) for rep,t,path in models if rep['name']==hit['model'])
    rep,t,path=selected
    shutil.copyfile(path,HERE/'HIT_FIELD_TABLES.json')
    recipe={'model':rep['name'],'field_TABLES':'HIT_FIELD_TABLES.json','source_recipe':'../h48_complement/SOURCE_SEMIDIRECT_RECIPE.json',
            'normal_tuple':hit['normal_tuple'],'source_H_and_C17_parts':positive,
            'alpha':t['alpha_matrix'],'beta':t['beta_matrix'],
            'inverse':'(-rho(h^-1)V,-chi(h^-1)c,h^-1), computedintheactualnewfield',
            'node_encoding':'module=x+q*y;Q=c+17*(u+3v);node=q²*Q+module',
            'proof':'Valid semidirectgroup; inverseclosed sixdistinctgenerators; Cayleylefttranslations; onefreshcompleteidentityBFS gives exactD.'}
    (HERE/'FIRST_HIT_RECIPE.json').write_text(json.dumps(recipe,indent=2)+'\n')
    r.update(actual_n=hit['n'],actual_D=hit['actual_global_D'],ordinary_bad_unordered_pairs=0,
             graph_file=str(HERE/f'graph_d6_D7_n{hit["n"]}.edges'),
             pending=['Root independent first newparameter acceptance/Gemini'])
(HERE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':r['status'],'settings_processed':r['settings_processed'],'total_batch_CPU_seconds':r['total_batch_CPU_seconds'],'pending':r['pending']},indent=2)+'\n')
print(json.dumps(r,indent=2))
