import json,time
from pathlib import Path
started=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
gate=D.parent.parent
groups=[g for g in json.loads((gate/'GLOBAL_COSET4_GROUPS.json').read_text())if g['complete']and g['controller_pairs']]
assert len(groups)==91
path=R/'formal/DegreeDiameter/Portfolio/F3Graph15552FullPackages.lean';assert not path.exists()
text='''import DegreeDiameter.Portfolio.F3Graph15552FullFirstFour
import DegreeDiameter.Portfolio.F3Graph15552Row0FullrankCertificate
'''
for i in range(22):text+=f'import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert{i:02d}\n'
text+='''namespace DegreeDiameter.Portfolio.F3Graph15552.FullKernel
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
def PairBound (a b : Fin 192) : Prop := ∀x y : Fin 81,
  ∃w : graph.Walk (liftAt a x) (liftAt b y),w.length≤4
abbrev RankIndex := Fin 173
def rankWord : RankIndex → List (Fin 5) := Fin.cases PilotFullrank.word Row0Fullrank.word
def rankInverse : RankIndex → Fin 4 → Vec := Fin.cases PilotFullrank.inverseBasis Row0Fullrank.inverseBasis
theorem rankBasis : ∀k j,routeVec (rankWord k) (rankInverse k j) 0=basisVec j :=
  Fin.cases PilotFullrank.basis_certificate Row0Fullrank.basis_certificate
theorem rankLength : ∀k,(rankWord k).length≤4 :=
  Fin.cases PilotFullrank.length_certificate Row0Fullrank.length_certificate
theorem rankBound (a b : Fin 192) (k : RankIndex)
    (hc : routeController a (rankWord k)=b) : PairBound a b :=
  inverse_walk_bound a b (rankWord k) (rankInverse k) (rankBasis k) hc (rankLength k)
structure CosetEndpoint where
  condition : Fin 192 → Fin 192 → Prop
  decideCondition : ∀a b,Decidable (condition a b)
  bound : ∀a b,condition a b → PairBound a b
def makeCoset {K : Type} [Fintype K] [DecidableEq K]
    (reference : List (Fin 5)) (word : K → List (Fin 5)) (column : K → Fin 4 → Vec)
    (choice : Fin 81 → K) (alpha : Fin 81 → Vec)
    (hcol : ∀k j,routeVec (word k) 0 (basisVec j)=
      routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0)
    (hcover : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z)
    (hlen : ∀k,(word k).length≤4) : CosetEndpoint where
  condition a b := ∀k,routeController a (word k)=b
  decideCondition a b := inferInstance
  bound a b hc := coset_walk_bound a b reference word column choice alpha hcol hcover hc hlen
theorem row0_word_length : ∀k,(Row0Coset.word k).length≤4 := by decide +kernel
def firstFourPackage (g : Fin 4) : CosetEndpoint where
  condition a b := ∀s : Fin 27,
    Row0Coset.slotGroup (FullFirstFour.slot s)=FullFirstFour.group g →
      routeController a (Row0Coset.word (FullFirstFour.slot s))=b
  decideCondition a b := inferInstance
  bound a b hc := by
    intro x y
    exact coset_walk_bound a b (Row0Coset.reference (FullFirstFour.group g))
      (fun z : Fin 81 => Row0Coset.word (Row0Coset.choice (FullFirstFour.group g) z))
      (fun z : Fin 81 => Row0Coset.column (Row0Coset.choice (FullFirstFour.group g) z))
      (fun z => z) (Row0Coset.alpha (FullFirstFour.group g))
      (by
        intro z j
        let s : Fin 27 := ⟨(Row0Coset.choice (FullFirstFour.group g) z).val,
          FullFirstFour.choice_slot_range g z⟩
        have he : FullFirstFour.slot s=Row0Coset.choice (FullFirstFour.group g) z := by
          apply Fin.ext
          rfl
        have h := FullFirstFour.column_certificate s j
        rw [he,FullFirstFour.choice_group_certificate g z] at h
        exact h)
      (fun z => FullFirstFour.cover_certificate g z)
      (by
        intro z
        let s : Fin 27 := ⟨(Row0Coset.choice (FullFirstFour.group g) z).val,
          FullFirstFour.choice_slot_range g z⟩
        have he : FullFirstFour.slot s=Row0Coset.choice (FullFirstFour.group g) z := by
          apply Fin.ext
          rfl
        have hg : Row0Coset.slotGroup (FullFirstFour.slot s)=FullFirstFour.group g := by
          rw [he]
          exact FullFirstFour.choice_group_certificate g z
        simpa only [he] using hc s hg)
      (fun z => row0_word_length (Row0Coset.choice (FullFirstFour.group g) z)) x y
'''
names=[]
for ordinal,g in enumerate(groups):
    gid=g['group_index'];name=f'packageG{gid}';names.append(name)
    if gid in [1,2,3,4]:rhs=f'firstFourPackage ({gid-1} : Fin 4)'
    else:
        ns='PilotLargestGroup'if gid==0 else f'FullCoset{gid}'
        fields=['reference','word','column','choice','alpha','column_certificate','cover_certificate','length_certificate']
        rhs='makeCoset '+' '.join(ns+'.'+v for v in fields)
    text+=f'def {name} : CosetEndpoint := {rhs}\n'
def balanced(values,var,lo=0):
    if len(values)==1:return values[0]
    m=len(values)//2
    return f'(if {var}.val < {lo+m} then {balanced(values[:m],var,lo)} else {balanced(values[m:],var,lo+m)})'
text+='def cosetPackage (g : Fin 91) : CosetEndpoint := '+balanced(names,'g')+'\n'
text+='''#print axioms rankBasis
#print axioms firstFourPackage
end DegreeDiameter.Portfolio.F3Graph15552.FullKernel
'''
path.write_text(text)
mapping=json.loads((D.parent/'formalization/ROW0_BRANCH_MAPPING.json').read_text())['branches']
rankmap={182:0}
rankmap.update({r['global_word_index']:1+r['index']for r in mapping if r['kind']=='Row0Fullrank'})
assert len(rankmap)==173
gmap={g['group_index']:i for i,g in enumerate(groups)}
reps=json.loads((gate/'SYMMETRY_REDUCED_KERNEL_SCOPE.json').read_text())['representatives']
pairs={(p['a'],p['b']):p for p in json.loads((gate/'GLOBAL_COSET4_PAIR_CERTIFICATES.json').read_text())['pairs']}
rows=[]
for a in reps:
    row=[]
    for b in range(192):
        p=pairs[a,b]
        row.append(f'(Sum.inl ({rankmap[p["word_index"]]} : RankIndex))'if p['kind']=='fullrank'else f'(Sum.inr ({gmap[p["group_index"]]} : Fin 91))')
    rows.append(balanced(row,'b'))
data=R/'formal/DegreeDiameter/Portfolio/F3Graph15552FullRowData.lean';assert not data.exists()
data.write_text('''import DegreeDiameter.Portfolio.F3Graph15552FullPackages
import DegreeDiameter.Portfolio.F3Graph15552FullSymmetryData
namespace DegreeDiameter.Portfolio.F3Graph15552.FullKernel
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
def pairDescriptor (r : Fin 8) (b : Fin 192) : RankIndex ⊕ Fin 91 :=
  '''+balanced(rows,'r')+'''
def pairCondition (r : Fin 8) (b : Fin 192) : Prop :=
  match pairDescriptor r b with
  | .inl k => routeController (FullSymmetry.representatives r) (rankWord k)=b
  | .inr g => (cosetPackage g).condition (FullSymmetry.representatives r) b
instance (r : Fin 8) (b : Fin 192) : Decidable (pairCondition r b) := by
  cases h : pairDescriptor r b with
  | inl k =>
      simp only [pairCondition,h]
      infer_instance
  | inr g =>
      simpa only [pairCondition,h] using
        (cosetPackage g).decideCondition (FullSymmetry.representatives r) b
end DegreeDiameter.Portfolio.F3Graph15552.FullKernel
''')
for r in range(8):
    out=R/f'formal/DegreeDiameter/Portfolio/F3Graph15552FullEndpointRow{r}.lean';assert not out.exists()
    out.write_text(f'''import DegreeDiameter.Portfolio.F3Graph15552FullRowData
namespace DegreeDiameter.Portfolio.F3Graph15552.FullKernel
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem endpoint_row{r} : ∀b,pairCondition ({r} : Fin 8) b := by decide +kernel
#print axioms endpoint_row{r}
end DegreeDiameter.Portfolio.F3Graph15552.FullKernel
''')
(D/'PACKAGES_PREPARATION_RESULT.json').write_text(json.dumps(dict(status='SHARED_PROOF_PACKAGES_AND1536_CONTROLLER_INPUTS_WRITTEN_UNCOMPILED',
    CPU_seconds=time.process_time()-started,fullrank_old_basis_rechecks=0,coset_packages=91,representative_pairs=1536,
    first4_reused_certificates=True,old_or_passed_modules_changed=False),indent=2)+'\n')
print(path)
