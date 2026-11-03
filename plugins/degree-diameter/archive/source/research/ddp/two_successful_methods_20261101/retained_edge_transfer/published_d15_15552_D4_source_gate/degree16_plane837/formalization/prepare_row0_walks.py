import json,time
from pathlib import Path
started=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
mapping=json.loads((D/'ROW0_BRANCH_MAPPING.json').read_text())['branches']
assert [v['b']for v in mapping]==list(range(192))
path=R/'formal/DegreeDiameter/Portfolio/F3Graph15552Row0Walks.lean';assert not path.exists()
text='''import DegreeDiameter.Portfolio.F3Graph15552Row0FullrankCertificate
import DegreeDiameter.Portfolio.F3Graph15552Row0ColumnCertificate
import DegreeDiameter.Portfolio.F3Graph15552Row0CoverCertificate
namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
namespace Row0Fullrank
theorem all_walk_bound (k : K) (x y : Fin 81) :
    ∃w : graph.Walk (liftAt 0 x) (liftAt (target k) y),w.length≤4 :=
  inverse_walk_bound 0 (target k) (word k) (inverseBasis k)
    (basis_certificate k) (controller_certificate k) (length_certificate k) x y
end Row0Fullrank
namespace Row0Coset
theorem all_walk_bound (g : G) (x y : Fin 81) :
    ∃w : graph.Walk (liftAt 0 x) (liftAt (target g) y),w.length≤4 := by
  exact coset_walk_bound 0 (target g) (reference g)
    (fun z : Fin 81 => word (choice g z))
    (fun z : Fin 81 => column (choice g z)) (fun z => z) (alpha g)
    (by
      intro z j
      have h := column_certificate (choice g z) j
      rw [choice_group_certificate g z] at h
      exact h)
    (fun z => cover_certificate g z)
    (by
      intro z
      have h := controller_certificate (choice g z)
      rw [choice_group_certificate g z] at h
      exact h)
    (fun z => length_certificate (choice g z)) x y
end Row0Coset
def CompleteTarget (b : Fin 192) : Prop := ∀x y : Fin 81,
  ∃w : graph.Walk (liftAt 0 x) (liftAt b y),w.length≤4
theorem all_controller_targets : ∀b,CompleteTarget b :=
'''
term='(fun b : Fin 0 => Fin.elim0 b)'
for branch in reversed(mapping):
    kind=branch['kind']
    if kind=='pilotLargest':value='PilotLargestGroup.all_walk_bound'
    elif kind=='pilotFullrank':value='PilotFullrank.all_walk_bound'
    elif kind=='Row0Fullrank':value=f"(Row0Fullrank.all_walk_bound ({branch['index']} : Row0Fullrank.K))"
    elif kind=='Row0Coset':value=f"(Row0Coset.all_walk_bound ({branch['index']} : Row0Coset.G))"
    else:raise ValueError(kind)
    term=f'(Fin.cases {value} {term})'
text+='  '+term+'\n'
text+='''theorem row0_full_walk_bound (x : Fin 81) (v : Fin 15552) :
    ∃w : graph.Walk (liftAt 0 x) v,w.length≤4 := by
  have h := all_controller_targets (controllerOf v) x (fiberOf v)
  change (∃w : graph.Walk (liftAt 0 x) (liftAt (controllerOf v) (fiberOf v)),w.length≤4) at h
  exact (liftAt_parts v) ▸ h
#print axioms row0_full_walk_bound
end DegreeDiameter.Portfolio.F3Graph15552
'''
path.write_text(text)
(D/'ROW0_WALKS_PREPARATION_RESULT.json').write_text(json.dumps(dict(status='NEW_ROW0_WALK_ASSEMBLY_WRITTEN_UNCOMPILED',
    CPU_seconds=time.process_time()-started,source=str(path.relative_to(R)),controller_branches=192,old_or_passed_modules_changed=False),indent=2)+'\n')
print(path)
