"""One fixedm34 controller gate. Total20 CPU including prep/compile/export."""
from pathlib import Path
import csv,json,math,os,resource,subprocess,time
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
os.chdir(HERE)
assert not (HERE/'TERMINAL.json').exists(),'this bounded scope has already run'
start=time.process_time();child0=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.monotonic();budget=20

def spent():
 c=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-start+c.ru_utime+c.ru_stime-child0.ru_utime-child0.ru_stime

def limit(n):
 def apply():resource.setrlimit(resource.RLIMIT_CPU,(n,n))
 return apply

def write(name,obj): (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
assert (HERE/'PRED.md').is_file()
units=[u for u in range(34) if math.gcd(u,34)==1]
legal_a0=[a for a in range(34) if a not in [0,17]]
assert len(units)==16 and len(legal_a0)==32
for a in legal_a0:
 target=math.gcd(a,34)
 assert target in [1,2]
 assert sum((u*a)%34==target for u in units)==1
assert all((17*u)%34==17 for u in units)
raw=2*33**4;valid=2*(33**4-33**3)
assert (raw,valid)==(2371842,2299968)
write('NORMALIZATION_AND_DOMAIN.json',{'m':34,'half':17,'units':units,'legal_alpha0_count':32,'normalized_alpha0':[1,2],'unit_orbits':2,'unique_unit_to_representative_each':True,'half_preserved':True,'raw_per_branch':33**4,'invalid_per_branch':33**3,'valid_per_branch':33**4-33**3,'raw_normalized_total':raw,'valid_normalized_total':valid,'valid_unnormalized_total':16*valid,'all_unnormalized_individually_enumerated':False,'scalar_prep_CPU':spent()})
record={'budget_total_CPU_seconds':budget,'workers':1,'started_UTC':datetime.now(timezone.utc).isoformat(),'normalization_prep_CPU_seconds':spent(),'scope':'onlym34/fixedsixport3base/alpha0=1,2/other4in1..33,sumalpha1alpha2!=0'}
cmd=['g++','-O3','-std=c++17','-Wall','-Wextra','search.cpp','-o','search']
with (HERE/'compile.log').open('w') as out:
 b=subprocess.run(cmd,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limit(6))
record.update(compile_command=cmd,compile_returncode=b.returncode,prep_compile_CPU_seconds=spent())
if b.returncode==0 and spent()<19.5:
 remaining=budget-spent()-.15
 cmd=['./search',str(remaining)]
 with (HERE/'search.log').open('w') as out:
  r=subprocess.run(cmd,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limit(math.ceil(remaining)))
 record.update(search_command=cmd,search_returncode=r.returncode)
 if (HERE/'SEARCH_RESULT.json').exists():
  result=json.loads((HERE/'SEARCH_RESULT.json').read_text());record['result']=result
  assert result['tested_simple_candidates']<=valid
  assert result['raw_prefix_candidates']==result['tested_simple_candidates']+result['skipped_nonsimple_prefix']
  if result['status']=='EXHAUSTED_FIXED_FAMILY':
   assert result['tested_simple_candidates']==valid and result['raw_prefix_candidates']==raw
   assert result['branch_tested']==[valid//2,valid//2]
  if result['status']=='WITNESS_PASS':
   pars=result['solution_parameters'];a0,a1,a2,s,t,h=pars
   def neighbor(v,p):
    c,g=divmod(v,34)
    row=[[(0,g+a0),(0,g-a0),(1,g),(2,g),(1,g+s),(2,g+t)],
         [(2,g+a1),(2,g-a2),(2,g),(0,g),(0,g-s),(1,g+h)],
         [(1,g+a2),(1,g-a1),(0,g),(1,g),(2,g+h),(0,g-t)]][c]
    d,z=row[p];return 34*d+z%34
   table=[list(map(int,row[1:])) for row in list(csv.reader((HERE/'controller102.porttable.tsv').open(),delimiter='\t'))[1:]]
   assert len(table)==102 and table==[[neighbor(v,p) for p in range(6)] for v in range(102)]
   inv=[1,0,3,2,4,5]
   for v,row in enumerate(table):
    assert len(set(row))==6 and v not in row
    for p,u in enumerate(row):assert table[u][inv[p]]==v
    assert table[table[table[v][2]][2]][2]==v
   edges={tuple(map(int,line.split())) for line in (HERE/'controller102.edges').read_text().splitlines()}
   assert len(edges)==306 and all(v<u for v,u in edges)
   assert edges=={tuple(sorted((v,u))) for v,row in enumerate(table) for u in row}
   words=[];ordered_pairs=0
   for rr in csv.DictReader((HERE/'THREE_PORT_WITNESSES.tsv').open(),delimiter='\t'):
    w={k:int(v) for k,v in rr.items()};ports=[w['p0'],w['p1'],w['p2']];c=w['root_base'];target=w['target_vertex']
    for g in range(34):
     v=34*c+g
     for p in ports:v=table[v][p]
     assert v==34*(target//34)+(target%34+g)%34
     ordered_pairs+=1
    words.append(w)
   assert len(words)==306 and ordered_pairs==10404
   write('PARAMETERS.json',{'m':34,'half':17,'base_count':3,'controller_order':102,'degree':6,'edges':306,'parameters':{'alpha0':a0,'alpha1':a1,'alpha2':a2,'sigma':s,'tau':t},'vertex_label':'34*c+g','ports':['a_plus','a_minus','b_plus','b_minus','s','t'],'inverse_ports':inv,'controller':table,'framework_author':'Bhakar three-base Schreier framework, same attribution as acceptedm26; newm34parameters/sixthmatching checked here','conditional_full_F9_target':{'order':74358,'degree':54,'D':3},'full_F9_graph_generated':False,'accepted_full_graph_count_increment':0})
   write('CONTROLLER_ROUTE_CERTIFICATE.json',{'status':'PASS','representatives':306,'all_translated_ordered_pairs':10404,'m':34,'vertices':102,'rows':words})
   record['independent_explicit_equation_and_literal_export_check']={'status':'PASS','controller_vertices':102,'edges':306,'route_representatives':306,'translated_pairs':10404,'BFS':0}
else:record['status']='COMPILE_FAILURE_OR_BUDGET_BEFORE_SEARCH'
record.update(total_measured_CPU_seconds=spent(),wall_seconds=time.monotonic()-wall,all_local_processes_terminal=True,fullfiber_graphs=0,BFS_solver_Lean_calls=0,measurement_boundary='driver normalization/preparation, wholecompilerchild, search/exportchild and Python literal witness export/aggregation; interactive source authoring/read-only inspection outside')
write('TERMINAL.json',record)
print(json.dumps({k:record[k] for k in ['budget_total_CPU_seconds','compile_returncode','result','total_measured_CPU_seconds','wall_seconds','all_local_processes_terminal'] if k in record},ensure_ascii=False,indent=2))
