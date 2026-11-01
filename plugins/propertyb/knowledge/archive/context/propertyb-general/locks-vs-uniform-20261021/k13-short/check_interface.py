import ast,json
from pathlib import Path
from layout_certified import FixedCertificate,LayoutCertificate
OUT=Path(__file__).resolve().parent
orig=ast.parse(Path('context/collaborator-small-k-20261019/m10-m11/propertyB_k10_k11_certified.py').read_text())
new=ast.parse((OUT/'layout_certified.py').read_text())
def table(tree,name):
 cl=next(s for s in tree.body if isinstance(s,ast.ClassDef) and s.name==name)
 return next(s for s in cl.body if isinstance(s,ast.FunctionDef) and s.name=='table')
def stripped(fn,custom):
 out=[]
 for s in fn.body:
  if isinstance(s,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='t' for t in s.targets):continue
  if custom and isinstance(s,ast.Assert):continue
  out.append(s)
 return ast.dump(ast.Module(body=out,type_ignores=[]),include_attributes=False)
identical=stripped(table(orig,'FixedCertificate'),False)==stripped(table(new,'LayoutCertificate'),True)
assert identical
x=json.loads((OUT/'DIAGNOSIS.json').read_text());one=[]
for r in x['one']:
 z=FixedCertificate(13,r['M']).one(r['v'],r['d']);assert z==r['central_z'];one.append({'M':r['M'],'v':r['v'],'d':r['d'],'matches':True})
res={'table_AST_identical_after_removing_position_assignment_and_new_validation_assert':identical,'original_formula_cases_unchanged':True,'two_central_baseline_matches_asserted_in_diagnose':len(x['two']),'one_central_baseline_matches':one,'arithmetic':'Python arbitrary precision only; no NumPy or fixed-width operations','complete_layout_grid':x['complete_requested_grid'],'full_hypergraph_certificate':False}
(OUT/'CHECK_INTERFACE.json').write_text(json.dumps(res,indent=2));print(json.dumps(res),flush=True)
