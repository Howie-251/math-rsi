import json,time
from pathlib import Path
started=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
gate=D.parent.parent
p=json.loads((gate/'CONTROLLER_SYMMETRY_GENERATORS_RESULT.json').read_text())
gens=p['generators'];bindings=p['start_controller_bindings'];reps=p['orbit_representatives']
assert len(gens)==2 and len(bindings)==192
assert [v['controller']for v in bindings]==list(range(192))
assert all(i in [0,1]for v in bindings for i in v['generator_word'])
def tree(values,render,lo=0):
    if len(values)==1:return render(values[0])
    mid=len(values)//2
    return f'(if a.val < {lo+mid} then {tree(values[:mid],render,lo)} else {tree(values[mid:],render,lo+mid)})'
path=R/'formal/DegreeDiameter/Portfolio/F3Graph15552FullSymmetryData.lean'
assert not path.exists()
text='''import DegreeDiameter.Portfolio.F3Graph15552Definitions
namespace DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
'''
for i,g in enumerate(gens):
    text+=f'def gen{i} (a : Fin 192) : Fin 192 := '+tree(g['permutation'],lambda v:f'({v} : Fin 192)')+'\n'
    text+=f'def inv{i} (a : Fin 192) : Fin 192 := '+tree(g['inverse'],lambda v:f'({v} : Fin 192)')+'\n'
text+='def generator : Fin 2 → Fin 192 → Fin 192 := ![gen0,gen1]\n'
text+='def representatives : Fin 8 → Fin 192 := !['+', '.join(map(str,reps))+']\n'
text+='def representativeIndex (a : Fin 192) : Fin 8 := '+tree([reps.index(v['representative'])for v in bindings],lambda v:f'({v} : Fin 8)')+'\n'
text+='def transportWord (a : Fin 192) : List (Fin 2) := '+tree([v['generator_word']for v in bindings],lambda v:'['+', '.join(map(str,v))+']')+'\n'
text+='''def wordController : Fin 192 → List (Fin 2) → Fin 192
  | a,[] => a
  | a,i::word => wordController (generator i a) word
end DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
'''
path.write_text(text)
for i in range(2):
    out=R/f'formal/DegreeDiameter/Portfolio/F3Graph15552FullSymmetryCertificate{i}.lean'
    assert not out.exists()
    out.write_text(f'''import DegreeDiameter.Portfolio.F3Graph15552FullSymmetryData
namespace DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem gen{i}_left_inverse : ∀a,inv{i} (gen{i} a)=a := by decide +kernel
theorem gen{i}_right_inverse : ∀a,gen{i} (inv{i} a)=a := by decide +kernel
theorem gen{i}_commutes : ∀a p,gen{i} (controller a p)=controller (gen{i} a) p := by decide +kernel
#print axioms gen{i}_left_inverse
#print axioms gen{i}_commutes
end DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
''')
out=R/'formal/DegreeDiameter/Portfolio/F3Graph15552FullSymmetryCoverage.lean';assert not out.exists()
out.write_text('''import DegreeDiameter.Portfolio.F3Graph15552FullSymmetryData
namespace DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem controller_coverage : ∀a,
    wordController (representatives (representativeIndex a)) (transportWord a)=a := by decide +kernel
#print axioms controller_coverage
end DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
''')
(D/'SYMMETRY_PREPARATION_RESULT.json').write_text(json.dumps(dict(status='NEW_BALANCED_LOOKUP_SYMMETRY_MODULES_WRITTEN_NOT_COMPILED',
    CPU_seconds=time.process_time()-started,generators=2,commutation_cases=1920,positive_start_bindings=192,
    word_max_length=p['max_generator_word_length'],old_modules_modified=False),indent=2)+'\n')
print(path)
