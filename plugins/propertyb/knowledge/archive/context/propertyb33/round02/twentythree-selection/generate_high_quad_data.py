"""Reindex the existing five numerical orbits to seven complete labeled inputs.

The generated Lean file independently checks every exact profile and dual.
This generator is not part of the proof's trust base.
"""
from pathlib import Path
from fractions import Fraction
from itertools import permutations, product
import json
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'computations'))
sys.dont_write_bytecode = True
from multilock import Profile, pair_weight

source = json.loads((ROOT / 'context/propertyb33/round01/large-math/SEVEN_PAIR3_FOUR_V23.json').read_text())
highs = [7,11,13,14,15]
pairs = [3,5,9,6,10,12]
co = [3,1,1,1,1,1]
valid = [h for h in product(range(2),repeat=5)
         if all(sum(n for b,n in zip(highs,h) if b&t==t)<=c for t,c in zip(pairs,co))]
assert len(valid) == 7

def trans(t, perm):
    return sum(1<<perm[i] for i in range(4) if t>>i&1)

def vector(xs):
    return '![' + ','.join(map(str,xs)) + ']'

def lean_list(xs):
    return '[' + ','.join(map(str,xs)) + ']'

def dual(p,j):
    bit = 1<<j
    k = p.positions[j]
    types = [t for t in p.counts if t&bit]
    inv = []
    for ix,t in enumerate(types):
        for u in types[ix:]:
            cap = p.counts[t]*(p.counts[t]-1)//2 if t==u else p.counts[t]*p.counts[u]
            if cap:
                w = pair_weight(23,5,p.positions,t,u,k)+pair_weight(23,5,p.positions,u,t,k)
                inv.append((cap,w,t==u==bit))
    r = max(0,(4*p.counts.get(bit,0)+2-19)//3)
    wpp = next((w for cap,w,pure in inv if pure),Fraction(0))
    options = []
    for c in sorted({Fraction(0),*(w for cap,w,pure in inv)}):
        for d in {Fraction(0),max(Fraction(0),wpp-c)}:
            loss = 2*c+r*d-sum(cap*max(Fraction(0),c+(d if pure else 0)-w)
                              for cap,w,pure in inv)
            options.append((loss,c,d))
    loss,c,d = max(options)
    return c,d,loss

rows = []
for h in valid:
    ns = {t:n for t,n in zip(highs,h)}
    ns.update({t:c-sum(n for b,n in zip(highs,h) if b&t==t) for t,c in zip(pairs,co)})
    for j in range(4):
        ns[1<<j] = 7-sum(n for b,n in ns.items() if b>>j&1)
    ns[0] = 33-sum(ns.values())
    ns = {t:n for t,n in ns.items() if n}
    chosen = None
    for r in source['results']:
        old = {int(t):n for t,n in r['counts'].items()}
        for perm in permutations(range(4)):
            if {trans(t,perm):n for t,n in old.items()} == ns:
                pos = [None]*4
                for oldj,newj in enumerate(perm):
                    pos[newj] = r['positions'][oldj]
                chosen = r,pos,perm
                break
        if chosen:
            break
    assert chosen
    r,pos,perm = chosen
    p = Profile(23,5,tuple(pos),ns)
    cert = [dual(p,j) for j in range(4)]
    for oldj,newj in enumerate(perm):
        assert cert[newj][2] == Fraction(r['certificates'][oldj]['loss'])
    rows.append(dict(h=h,ns=ns,pos=pos,cert=cert,source_group=r['group'],bound=r['bound']))

lines = ['import Aris4Math.ThirtyThree.QuadProfiles',
         'import Aris4Math.ThirtyThree.TwentyTwoPureDeletion',
         'import Aris4Math.ThirtyThree.CustomDeletion', '',
         '/-! Seven complete labeled four-lock profiles: degrees seven, pair 01',
         'of codegree three, every other pair of codegree one. -/',
         'namespace Aris4Math.ThirtyThree.TwentyThreeHighQuadData',
         'open Aris4Math.ThirtyThree.QuadProfiles',
         'open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)',
         'open scoped BigOperators', '',
         'def co : Fin 6 → ℕ := ![3,1,1,1,1,1]',
         'def high : Fin 7 → Fin 5 → ℕ := '+vector(vector(r['h']) for r in rows),
         'def positionFn : Fin 7 → Fin 4 → Fin 23 := '+vector(vector(p-1 for p in r['pos']) for r in rows),
         'theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide',
         'def positions (i : Fin 7) : Fin 4 ↪ Fin 23 := ⟨positionFn i,positionFn_injective i⟩',
         'def counts (i : Fin 7) : Finset (Fin 4) → ℕ := recovered 33 (fun _ => 7) co (high i)',
         'def p (i : Fin 7) : Numeric.Profile :=',
         '  pruneZero ⟨23, executableType (positions i) Finset.univ,',
         '    labels.map (fun T => ⟨executableType (positions i) T,counts i T⟩), none,',
         '    List.ofFn (fun j => (positions i j).val+1)⟩',
         'theorem p_eq (i : Fin 7) : p i =',
         '    profile (positions i) (counts i) (List.ofFn fun j => (positions i j).val+1) := by',
         '  simp only [p,executableType_eq,profile,rawProfile]', '']
computed=[]
for r in rows:
    types=[]
    for t,n in sorted(r['ns'].items()):
        labs=sorted(r['pos'][j] for j in range(4) if t>>j&1)
        types.append('⟨'+lean_list(labs)+','+str(n)+'⟩')
    computed.append('⟨23,'+lean_list(sorted(r['pos']))+','+lean_list(types)+',none,'+lean_list(r['pos'])+'⟩')
lines += ['def computed : Fin 7 → Numeric.Profile := '+vector(computed),
          'theorem p_eq_computed (i : Fin 7) : p i = computed i := by fin_cases i <;> rfl']
for name,idx in [('c',0),('d',1),('lossAt',2)]:
    lines.append(f'def {name} : Fin 7 → Fin 4 → ℚ := '+vector(vector(z[idx] for z in r['cert']) for r in rows))
lines += ['', 'def loss (i : Fin 7) (k : ℕ) : ℚ :=',
          '  if k=(positions i 0).val+1 then lossAt i 0 else',
          '  if k=(positions i 1).val+1 then lossAt i 1 else',
          '  if k=(positions i 2).val+1 then lossAt i 2 else',
          '  if k=(positions i 3).val+1 then lossAt i 3 else 0', '',
          'set_option maxHeartbeats 0 in', 'set_option maxRecDepth 100000 in',
          'theorem certificates : ∀ i : Fin 7,',
          '    Numeric.validProfile (p i) 33 ∧',
          '    (∑ k : Fin 23, min (Numeric.boundA (p i) (k.val+1))',
          '      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-loss i (k.val+1)))) < 1 ∧',
          '    ∀ j : Fin 4, let k := (positions i j).val+1',
          '      0 ≤ c i j ∧ 0 ≤ d i j ∧',
          '      loss i k ≤ 2*c i j + ((4*counts i {j}+2-19)/3 : ℕ)*d i j -',
          '        TwentyTwoPureDeletion.penaltySum (p i) k (c i j) (d i j) := by',
          '  simp only [p_eq_computed]', '  unfold Numeric.validProfile', '  decide +kernel','',
          'end Aris4Math.ThirtyThree.TwentyThreeHighQuadData','']
(ROOT/'formal/Aris4Math/ThirtyThree/TwentyThreeHighQuadData.lean').write_text('\n'.join(lines))
(Path(__file__).parent/'HIGH_QUAD_GENERATION.json').write_text(json.dumps([
    dict(high=r['h'],counts=r['ns'],positions=r['pos'],source_group=r['source_group'],
         bound=r['bound'],dual=[[str(x) for x in z] for z in r['cert']]) for r in rows],indent=2)+'\n')
print('Generated seven labeled profiles and exact dual certificates.')
