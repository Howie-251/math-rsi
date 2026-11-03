import json
from pathlib import Path
from time import process_time

start=process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
P='GQ77Published33CloneFamily';U=P+'Upper';ns='DegreeDiameter.Portfolio.'+U
Q=R/'formal/DegreeDiameter/Portfolio';F=R/'formal'
exact=f'import DegreeDiameter.Portfolio.{P}Exact\nnamespace {ns}\n'
targets=[]
for k in range(9,16):
    degree,n=64+k,160050+1650*k;name=f'd{degree}_{n}'
    target=f'Fintype.card ({P}.Vertex {k}) = {n} ∧\n  (∀ v, ({P}.graph {k}).degree v ≤ {degree}) ∧\n  DiameterAtMost ({P}.graph {k}) 3 ∧ ¬DiameterAtMost ({P}.graph {k}) 2'
    exact+=f'theorem {name} : {target} := {P}.fixed_family_target {k}\n'
    exact+=f'def FinalClaim{degree} : Prop := {target}\n'
    exact+=f'theorem final_claim{degree} : FinalClaim{degree} := {name}\n'
    exact+=f'#print axioms {name}\n#print axioms final_claim{degree}\n'
    targets.append({'k':k,'degree':degree,'n':n,'theorem':name,'FinalClaim':f'FinalClaim{degree}','final_claim':f'final_claim{degree}'})
exact+='end '+ns+'\n';(Q/(U+'Exact.lean')).write_text(exact)
audit=f'''import DegreeDiameter.Portfolio.{U}Exact
open DegreeDiameter.Portfolio
set_option pp.explicit true in
#print DiameterAtMost
#print OppositeGQ77Spread.Old
#print OppositeGQ77Spread.New
#print OppositeGQ77Spread.Vertex
#print {P}.Vertex
#print {P}.center
#print {P}.graph
#print FullNeighborhoodClones.graph
#print {P}.label
#check {P}.base_label
#check {P}.clone_label
#check {P}.center_source_label
#check {P}.label_old
#check {P}.label_new
#check {P}.label_new_coordinates
#check {P}.old_walk_bound_iff
#print axioms {P}.ovoid_unique
#print axioms {P}.copy_load_le
#print axioms {P}.old_walk_bound_iff
'''
for t in targets:
    k,n,degree,name=t['k'],t['n'],t['degree'],t['theorem']
    audit+=f'#check ({P}.label {k} : {P}.Vertex {k} ≃ Fin {n})\n'
    audit+=f'#check {U}.{name}\n#print {U}.{name}\n#print {U}.FinalClaim{degree}\n'
    audit+=f'#print axioms {U}.{name}\n#print axioms {U}.final_claim{degree}\n'
(F/(U+'Audit.lean')).write_text(audit)
parent=D.parent.parent/'multiplicity65_72_family/formalization'
compiler=(parent/'compile.py').read_text().replace(P,U).replace('spent+budget<=900','spent+budget<=300')
compiler=compiler.replace(f"assert mod.startswith('{U}')",f"assert mod in {{'{U}Exact','{U}Audit'}}")
(D/'compile.py').write_text(compiler)
(D/'TARGETS.json').write_text(json.dumps({'namespace':ns,'parent_namespace':'DegreeDiameter.Portfolio.'+P,'endpoints':targets},indent=2)+'\n')
(D/'PREPARATION_RESULT.json').write_text(json.dumps({'status':'TWO_NEW_UPPER_SOURCES_WRITTEN','CPU_seconds':process_time()-start,'modules':[U+'Exact',U+'Audit'],'old_modules_changed_or_recompiled':False,'new_finite_checks':0},indent=2)+'\n')
(D/'STAGE_STATE.json').write_text(json.dumps({'status':'UPPER_SOURCES_READY_NOT_YET_COMPILED','running':False,'active_modules':[],'exact_compiled':False,'audit_compiled':False,'external_binding_complete':False,'parent24_recompiled':False,'independent_acceptance':'actualPASS_reported_summary_pending'},indent=2)+'\n')
print(json.dumps({'status':'TWO_UPPER_MODULES_WRITTEN','original_targets':targets,'CPU_seconds':process_time()-start}))
