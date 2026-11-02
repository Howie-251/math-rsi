import json
from pathlib import Path
ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;R={k:json.loads((D.parent/f'RECIPE_d{k}.json').read_text())for k in (21,22)}
def vec(v):return '!['+', '.join(map(str,v))+']'
s='''import DegreeDiameter.Portfolio.FullNeighborhoodClones
import DegreeDiameter.Portfolio.F4Graph3840Exact
import Mathlib.Logic.Equiv.Fin.Basic
namespace DegreeDiameter.Portfolio.F4PlaneBlockClones
open F4Graph3840
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

def planeCode : Fin 16 → Fin 64 := '''+vec(R[21]['plane_local_codes'])+'\n'
for k in (21,22):
 layers=[a for a,r in enumerate(R[k]['controller_multiplicities'])for _ in range(r)];assert len(layers)=={21:9,22:22}[k]
 s+=f'def layers{k} : Fin {len(layers)} → Fin 60 := '+vec(layers)+'\n'
s+='''
def form (x : Vec) : F := x 0 + x 1 + F.w * x 2

def blockIndex {K : Nat} (j : Fin (K*16)) : Fin K := ⟨j.val/16, by have hj:=j.isLt; omega⟩
def planeIndex {K : Nat} (j : Fin (K*16)) : Fin 16 := ⟨j.val%16,Nat.mod_lt _ (by decide)⟩
def center {K : Nat} (layers : Fin K → Fin 60) (j : Fin (K*16)) : Fin 3840 :=
  liftAt (layers (blockIndex j)) (planeCode (planeIndex j))
abbrev V21 := Fin 3840 ⊕ Fin (9*16)
abbrev V22 := Fin 3840 ⊕ Fin (22*16)
def graph21 : SimpleGraph V21 := FullNeighborhoodClones.graph F4Graph3840.graph (center layers21)
def graph22 : SimpleGraph V22 := FullNeighborhoodClones.graph F4Graph3840.graph (center layers22)
def label21 : V21 ≃ Fin 3984 := finSumFinEquiv
def label22 : V22 ≃ Fin 4192 := finSumFinEquiv

theorem card21 : Fintype.card V21 = 3984 := by decide
theorem card22 : Fintype.card V22 = 4192 := by decide
end DegreeDiameter.Portfolio.F4PlaneBlockClones
'''
(ROOT/'formal/DegreeDiameter/Portfolio/F4PlaneBlockClonesDefinitions.lean').write_text(s)
bind={}
for k in (21,22):
 r=R[k];layers=[a for a,t in enumerate(r['controller_multiplicities'])for _ in range(t)];owners=[64*a+c for a in layers for c in r['plane_local_codes']];actual=[x['owner']for x in r['steps']];assert owners==actual
 bind[str(k)]=dict(plane_codes=r['plane_local_codes'],selected_layers=layers,clone_owners_equal_every_recipe_step=True,owner_count=len(owners),old_vertices=3840,order=3840+len(owners),new_new_edges=False,clone_rule='full original source open neighborhood; old-old edges retained')
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(dict(status='PASS_ALL_RECIPE_OWNER_LABELS_AND_LITERAL_BLOCK_INPUTS',graphs=bind,ASCII_edge_parser_theorem=False,graph_BFS=False,solver=False),indent=2)+'\n')
