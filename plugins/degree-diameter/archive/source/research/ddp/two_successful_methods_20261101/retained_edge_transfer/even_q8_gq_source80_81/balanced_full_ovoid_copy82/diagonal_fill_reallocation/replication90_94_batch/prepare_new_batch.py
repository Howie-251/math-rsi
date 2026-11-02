from pathlib import Path
import json,time
D=Path(__file__).resolve().parent;OLD=D.parent/'replication86_98_batch'
start=time.process_time()
def write(path,text):
    assert not path.exists(),f'New batch file already exists: {path}'
    path.parent.mkdir(exist_ok=True,parents=True);path.write_text(text)
def replace_required(text,before,after):
    assert before in text,before
    return text.replace(before,after)
cpp=(OLD/'produce_once.cpp').read_text()
cpp=replace_required(cpp,'Case c86(4,86,argv[2]),c98(16,98,argv[3]);','Case c90(8,90,argv[2]),c94(12,94,argv[3]);')
cpp=replace_required(cpp,'std::array<Case*,2> cases{&c86,&c98};','std::array<Case*,2> cases{&c90,&c94};')
write(D/'produce_once.cpp',cpp)
wrapper=(OLD/'produce_once.py').read_text()
wrapper=replace_required(wrapper,"degree=86,r=4,n=363420,m=15573870,directory='multiplicity5_degree86'","degree=90,r=8,n=380324,m=16942770,directory='multiplicity9_degree90'")
wrapper=replace_required(wrapper,"degree=98,r=16,n=414132,m=19680570,directory='multiplicity17_degree98'","degree=94,r=12,n=397228,m=18311670,directory='multiplicity13_degree94'")
wrapper=wrapper.replace('replication86_98_batch','replication90_94_batch')
wrapper=replace_required(wrapper,'return time.process_time()-start+u.ru_utime+u.ru_stime',
    "return time.process_time()-start+u.ru_utime+u.ru_stime+json.loads((D/'PRODUCER_PREPARATION_RESULT.json').read_text())['CPU_seconds']")
write(D/'produce_once.py',wrapper)
pred='''# Frozen G1 first-role replication: only degree90 and94

2026-11-01, before execution. This is a new two-endpoint batch of the fixed
rule. Source is actual G1/346516,14204970 edges/max82, read once. It is not
the86/98/83 graph. J consists of4225 first clones plus the first hub, labels
342290+h,h0..4225. Its frozen full neighborhoods are nonempty, disjoint and
all below342290, with union342225 source vertices of degree82.

Append r complete copies of each frozen role, with new label346516+4226*b+h,
center342290+h. Keep all14204970 G1 edges, no new-new edges.

|case|r|total multiplicity|n|m|predicted exact degree histogram|
|---|---:|---:|---:|---:|---|
|multiplicity9_degree90|8|9|380324|16942770|65:9,80:585,81:37505,90:342225|
|multiplicity13_degree94|12|13|397228|18311670|65:13,80:845,81:54145,94:342225|

Production budget30 CPU inclusive of preparation/compile/all attempts/writes,
one worker, one G1 stream for both complete strictlex tables. Check all actual
degrees/roleN sizes/headers/source edge preservation and ordered labels. No
BFS, field, finite geometry, old module compilation, solver, paid review,
hash, install, root/frozen-file writes or other cap. Fresh independent
acceptance is separate; producer PASS does not increment counts.

Every prefix is covered by actual G1-interior Walks from the existing full-N
cloning construction: replace endpoints of old center walks, use a common
old neighbor when centers coincide. No future copy is used. Each source pin
has one base role, so its load before/after that role in block b is b/b+1.
Collapse copies to source centers in G1 preserves non-D2, not a collapse to
the earlier H. Shared all-pair/prefix proof and per-j prefix recipes are saved.

Only these two endpoints are authorized. Public located guarantees4225Delta
give380250/397150 and margins74/78. If Hfill plus standard copying is public,
remaining gains are9/13; if the same rule is public,0. Global/exact priority
UNKNOWN. Older A/B/C do not certify these targets. Root owns acceptance,
counts, Wiki, remote reviews and delivery decisions.
'''
write(D/'PREDICTION_AND_SCOPE.md',pred)
prod_cpu=time.process_time()-start
write(D/'PRODUCER_PREPARATION_RESULT.json',json.dumps(dict(CPU_seconds=prod_cpu,old_files_modified=False),indent=2)+'\n')

toolstart=time.process_time();FD=D/'formalization';FD.mkdir(exist_ok=True)
oldcases="[(86,4,363420,'multiplicity5_degree86'),(98,16,414132,'multiplicity17_degree98')]"
newcases="[(90,8,380324,'multiplicity9_degree90'),(94,12,397228,'multiplicity13_degree94')]"
for filename in['prepare.py','compile.py','run_all.py','bind_inputs.py','finalize.py']:
    text=(OLD/'formalization'/filename).read_text()
    text=text.replace(oldcases,newcases)
    text=text.replace('Q8DiagonalFill86','Q8DiagonalFill90').replace('Q8DiagonalFill98','Q8DiagonalFill94')
    text=text.replace('D86_D98','D90_D94').replace('363420','380324').replace('414132','397228')
    text=text.replace('multiplicity5_degree86','multiplicity9_degree90').replace('multiplicity17_degree98','multiplicity13_degree94')
    text=text.replace('multiplicity5_17_independent_acceptance','multiplicity9_13_independent_acceptance')
    text=text.replace('d86_','d90_').replace('d98_','d94_')
    text=text.replace('(r4) and d94_397228 (r16)','(r8) and d94_397228 (r12)')
    text=text.replace('Append r4 or16','Append r8 or12').replace('margins70/82','margins74/78')
    text=text.replace('16836+67548','33740+50644')
    if filename=='compile.py':
        text=replace_required(text,"preparation_CPU_seconds=prep['CPU_seconds']", "preparation_CPU_seconds=prep['CPU_seconds']+json.loads((D/'TOOLS_PREPARATION_RESULT.json').read_text())['CPU_seconds']")
    write(FD/filename,text)
write(FD/'TOOLS_PREPARATION_RESULT.json',json.dumps(dict(CPU_seconds=time.process_time()-toolstart,
    role='New eight-module batch tooling preparation only',old_files_modified_or_executed=False),indent=2)+'\n')
print(json.dumps(dict(status='NEW90_94_PRODUCER_PRED_AND_FORMAL_TOOLS_PREPARED',producer_preparation_CPU_seconds=prod_cpu,
    formal_tooling_CPU_seconds=time.process_time()-toolstart)))
