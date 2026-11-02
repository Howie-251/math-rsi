from pathlib import Path
import json,time
started=time.process_time()
D=Path(__file__).resolve().parent;P=D.parent.parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
F=R/'formal';portfolio=F/'DegreeDiameter/Portfolio'
cases=[(90,8,380324,'multiplicity9_degree90'),(94,12,397228,'multiplicity13_degree94')]
modules=[]
for cap,r,n,directory in cases:
    ns=f'Q8DiagonalFill{cap}';new=r*4226
    defs=f'''import DegreeDiameter.Portfolio.Q8DiagonalFill83Definitions
namespace DegreeDiameter.Portfolio.{ns}
namespace Source
abbrev Vertex := Q8DiagonalFill83.Source.Vertex
abbrev graph := Q8DiagonalFill83.Source.graph
abbrev label := Q8DiagonalFill83.Source.label
end Source
abbrev Role := Q8DiagonalFill83.Role
abbrev CopyIndex := Fin {r} × Role
abbrev Vertex := Source.Vertex ⊕ CopyIndex
def center (x : CopyIndex) : Source.Vertex := Q8DiagonalFill83.center x.2
abbrev graph : SimpleGraph Vertex := FullNeighborhoodClones.graph Source.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph Source.graph center).Adj)
def copyLabel : CopyIndex ≃ Fin {new} :=
  (Equiv.prodCongr (Equiv.refl (Fin {r})) Q8DiagonalFill83.roleLabel).trans finProdFinEquiv
def label : Vertex ≃ Fin {n} :=
  (Equiv.sumCongr Source.label copyLabel).trans finSumFinEquiv
theorem source_center_label (x : CopyIndex) :
    (Source.label (center x)).val = 342290+(Q8DiagonalFill83.roleLabel x.2).val :=
  Q8DiagonalFill83.source_center_label x.2
theorem label_old (v : Source.Vertex) : (label (.inl v)).val = (Source.label v).val := rfl
theorem copy_label (b : Fin {r}) (h : Role) :
    (copyLabel (b,h)).val = 4226*b.val+(Q8DiagonalFill83.roleLabel h).val := by
  change (Q8DiagonalFill83.roleLabel h).val+4226*b.val=_
  omega
theorem label_new (b : Fin {r}) (h : Role) :
    (label (.inr (b,h))).val = 346516+4226*b.val+(Q8DiagonalFill83.roleLabel h).val := by
  change 346516+((Q8DiagonalFill83.roleLabel h).val+4226*b.val)=_
  omega
theorem label_copy (b : Fin {r}) (i j : Fin 65) :
    (label (.inr (b,.inl (i,j)))).val = 346516+4226*b.val+65*i.val+j.val := by
  change 346516+((j.val+65*i.val)+4226*b.val)=_
  omega
theorem label_hub (b : Fin {r}) :
    (label (.inr (b,.inr ()))).val = 346516+4226*b.val+4225 := by
  change 346516+(4225+4226*b.val)=_
  omega
theorem card_vertex : Fintype.card Vertex={n} := by
  simpa only [Fintype.card_fin] using Fintype.card_congr label
def FinalClaim : Prop := Fintype.card Vertex={n} ∧
  (∀v,graph.degree v≤{cap}) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#check (label : Vertex ≃ Fin {n})
#print graph
end DegreeDiameter.Portfolio.{ns}
'''
    inputs=f'''import DegreeDiameter.Portfolio.{ns}Definitions
import DegreeDiameter.Portfolio.Q8DiagonalFill83Inputs
namespace DegreeDiameter.Portfolio.{ns}
theorem load_le (v : Source.Vertex) : FullNeighborhoodClones.load Source.graph center v≤{r} := by
  unfold FullNeighborhoodClones.load
  let copyIndex : {{x : CopyIndex // Source.graph.Adj v (center x)}} → Fin {r} := fun x => x.val.1
  have hinj : Function.Injective copyIndex := by
    intro x y h
    apply Subtype.ext
    have hb : x.val.1=y.val.1 := h
    have hr : x.val.2=y.val.2 :=
      Q8DiagonalFill83.adjacent_roles_unique v x.val.2 y.val.2 x.property y.property
    exact Prod.ext hb hr
  simpa only [Fintype.card_fin] using Fintype.card_le_of_injective copyIndex hinj
#print axioms load_le
end DegreeDiameter.Portfolio.{ns}
'''
    exact=f'''import DegreeDiameter.Portfolio.{ns}Inputs
import DegreeDiameter.Portfolio.Q8DiagonalFill83Exact
namespace DegreeDiameter.Portfolio.{ns}
theorem degree_le : ∀v,graph.degree v≤{cap} :=
  FullNeighborhoodClones.degree_le Source.graph center 82 {r}
    Q8DiagonalFill.final_claim.2.1 load_le
theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  FullNeighborhoodClones.diameterAtMost Source.graph center 3 (by decide)
    Q8DiagonalFill.final_claim.2.2.1 Q8DiagonalFill83.source_no_isolated
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  FullNeighborhoodClones.not_diameterAtMost Source.graph center 2 Q8DiagonalFill.final_claim.2.2.2
theorem d{cap}_{n} : Fintype.card Vertex={n} ∧ (∀v,graph.degree v≤{cap}) ∧
    DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := d{cap}_{n}
theorem old_walk_bound_iff (u v : Source.Vertex) (n : Nat) :
    (∃p:graph.Walk (.inl u) (.inl v),p.length≤n) ↔
      ∃p:Source.graph.Walk u v,p.length≤n :=
  FullNeighborhoodClones.old_walk_bound_iff Source.graph center u v n
#print axioms final_claim
end DegreeDiameter.Portfolio.{ns}
'''
    audit=f'''import DegreeDiameter.Portfolio.{ns}Exact
open DegreeDiameter.Portfolio.{ns}
#check (graph : SimpleGraph Vertex)
#check (label : Vertex ≃ Fin {n})
#print FinalClaim
#check d{cap}_{n}
#print d{cap}_{n}
#print axioms d{cap}_{n}
#print final_claim
#print axioms final_claim
#print axioms load_le
#print axioms old_walk_bound_iff
#print axioms copy_label
#print axioms label_old
#print axioms label_new
#print axioms label_copy
#print axioms label_hub
'''
    for suffix,text in [('Definitions',defs),('Inputs',inputs),('Exact',exact),('Audit',audit)]:
        name=ns+suffix;path=F/(name+'.lean') if suffix=='Audit' else portfolio/(name+'.lean')
        assert not path.exists(),f'New module unexpectedly exists: {path}'
        path.write_text(text);modules.append(name)
    caseD=P/directory/'formalization';caseD.mkdir(exist_ok=True)
    (caseD/'PRED.md').write_text(f'''# Fixed concrete degree{cap} target, before compilation

Target `DegreeDiameter.Portfolio.{ns}.d{cap}_{n}` and `FinalClaim/final_claim`.
Actual carrier is `Q8DiagonalFill.Vertex ⊕ (Fin {r} × Q8DiagonalFill83.Role)`;
the source is frozen G1/346516, not the83 graph. Explicit label equivalence
has codomain `Fin {n}`, new physical label346516+4226*b+h and center342290+h.
Prove base-role adjacency uniqueness via the already closed83 Inputs lemma;
the finite-copy index injection gives load≤{r}. Reuse true Walk D3,
no-isolated and non-D2 of G1 and the existing full-N clone theorems.
No new finite geometry or old module rebuild. All theorem assumptions must
close; the separate Audit prints original type/body and axioms (standard3).
The two cases share one300 CPU budget,60 CPU/module, one worker. Failed
attempts count. Fresh physical binding remains pending until its actual
receipt, and is not an ASCII parser theorem or a new Audit #eval.
''')
(D/'PRED.md').write_text('''# Two concrete frozen-G1 role-replication targets

One new bounded kernel batch,300 CPU inclusive of preparation/all failures/
external small-table binding;60 CPU/module; one worker. The only cases are
d90_380324 (r8) and d94_397228 (r12), each with its own carrier, explicit
Fin label, FinalClaim/final_claim and independent import Audit. Old PASS
sources/generics/finite tables are imported from pinned4.24 caches and never
modified/recompiled. New load proofs use copy-index injection and the closed
base-role uniqueness theorem. No geometry/field/BFS/solver/native_decide/
sorry/new axiom/install/hash. No review/count/Wiki/freeze scope is inherited.
''')
proof='''# Frozen G1 first-role replication: genuine Walks for every prefix

Source G1 has346516 vertices and14204970 edges and the already closed
true-Walk diameter3/non-D2/max82 claim. Its4226 independent first roles have
labels342290+h, h0..4225:4225 clones of original unfilled neighborhoods and
one hub on the65 fillers. Their complete G1 neighborhoods are disjoint and
all lie in old H<342290. The union has342225 old vertices, all of source
degree82. The other65 old H vertices stay degree81.

Append r8 or12 frozen full-neighborhood copies of every first role, never
copying a later graph's current neighborhood. Keep all14204970 G1 edges;
add exactly r342225 edges and no new-new edges. New index isj=4226b+h,
source center342290+h, new label346516+j. Production reads G1 once, writes
both complete strictlex tables and checks all degrees and4226 role N sizes.
Each fresh acceptance is separate from this producer receipt.

In any prefix, each old source vertex has at most one pinned base role;
before a role in block b is copied its old neighbors have load b and degree
82+b, then load b+1 and degree83+b. The new role has degree exactly that
frozen first role's degree65/80/81. Thus all intermediate prefixes obey cap
82+r, in any within-block order. PREFIX_LOAD_CHECKS.tsv records every j.

All old-old Walks remain inside G1. For new x copying center c and old v,
replace the first edge of a G1 c-to-v Walk by x's same first-neighbor edge.
If c=v, use x-u-c for any G1 neighbor u; no source role is isolated. For two
new vertices, replace both ends of a source center-to-center Walk. Equal
centers give a two-walk through a common old neighbor; adjacent centers give
a three-walk through their two old centers. Distinct nonadjacent centers use
the source length2/3 Walk. Every interior vertex is in frozen G1; no future
copy is needed. These are exactly the existing FullNeighborhoodClones actual
SimpleGraph.Walk lemmas, not an extrapolation from sampled BFS or a deletion
argument from the largest graph.

The edge-preserving retraction sends each new vertex to its G1 source center
and fixes G1. It transfers every short Walk to G1, so the G1 non-D2 witness
cannot acquire a two-shortcut. This collapse is to G1, not the earlier H.

Source pin load≤1 is the already closed Q8DiagonalFill83 adjacency uniqueness
lemma about G1 first roles. Among the new Fin r×Role centers adjacent to any
source vertex, projection to the copy coordinate is injective: equal copy
coordinates force equal base roles by that lemma. Hence load≤r without
enumerating large graphs. The generic degree theorem gives≤82+r, generic
Walks give D3 and the retraction gives non-D2. Explicit labels are symbolic
finite equivalences. External fresh ordered recipes bind each actual j to
those labels; no Lean ASCII edge parser or full regularity theorem is claimed.

These two endpoints instantiate one existing rule. Public margins74/78 are
only against the currently located4225Delta guarantees; global and exact-rule
priority remain UNKNOWN. Root owns graph acceptance/counts and all new remote
reviews. No unrelated cap, old module, root file or frozen package changes.
'''
(D/'PROOF.md').write_text(proof)
for _,_,_,directory in cases:(P/directory/'PROOF.md').write_text(proof)
receipt=dict(status='EIGHT_NEW_MODULES_AND_TYPED_TARGETS_WRITTEN',CPU_seconds=time.process_time()-started,
    modules=modules,budget_CPU_seconds=300,per_module_CPU_limit_seconds=60,worker_count=1,
    old_modules_modified_or_recompiled=False)
(D/'PREPARATION_RESULT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
