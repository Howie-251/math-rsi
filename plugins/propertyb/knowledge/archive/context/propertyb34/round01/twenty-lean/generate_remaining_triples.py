from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
original=(ROOT/'context/propertyb34-hour1-20261013/nineteen/generate_twenty_seven_triples.py').read_text()
a=original.index('D=[]');b=original.index("print('labelled'",a)
load='''D=[];seen=set()
for filename in ('SEVEN_ONE_VERIFIED','EIGHT_VERIFIED'):
 raw=json.load(open(ROOT/f'context/propertyb34-hour1-20261013/low-math/{filename}.json'))['witnesses']
 for r in raw:
  if len(r['ds'])!=3:continue
  choices=permutations(range(3)) if r['ds']==[8,8,8] else [(0,1,2)]
  for perm in choices:
   counts={sum(1<<perm[j] for j in range(3) if int(m)>>j&1):n for m,n in r['counts'].items()}
   key=(tuple(r['ds']),tuple(counts.get(m,0) for m in range(8)))
   if key in seen:continue
   seen.add(key);positions=[0]*3
   for j in range(3):positions[perm[j]]=r['pos'][j]
   pos=tuple(positions);p0=Profile(20,5,pos,counts);loss=[];flags=[]
   for j,d in enumerate(r['ds']):
    total=link_certificate(p0,j,(4*d-19+2)//3)['deduction'];q=max(0,(4*counts[1<<j]+2-17)//3)
    pure=q*2*pair_weight(20,5,pos,1<<j,1<<j,pos[j]);loss.append(max(total,pure));flags.append(pure>total)
   bound=total_bound(rows(p0,deductions=dict(zip(pos,loss))));assert bound<1
   ls=[sum(n for m,n in counts.items() if m&mask==mask) for mask in (3,5,6)]
   D.append(dict(a=ls[0],b=ls[1],c=ls[2],t=counts.get(7,0),high=r['ds'][0]==7,pos=pos,counts=counts,loss=loss,pure=flags,bound=bound))
assert len(D)==88
'''
script=original[:a]+load+original[b:]
script=script.replace('parents[3]','parents[4]').replace('TwentySevenTriples','TwentyRemainingTriples').replace('Fin 39','Fin 88').replace('TWENTY_SEVEN_TRIPLE_DATA','REMAINING_TRIPLE_DATA')
script=script.replace('if (data i).high && decide (j=2) then 8 else 7','if (data i).high && decide (j=0) then 7 else 8')
script=script.replace('theorem p_eq_computed (i : Case)', 'set_option maxHeartbeats 0 in\\ntheorem p_eq_computed (i : Case)')
a=script.index('theorem coverage_seven');b=script.index('\nend Aris4Math.ThirtyFour.TwentyRemainingTriples',a)
script=script[:a]+'''def Suitable (seven : Bool) (a b c t : ℕ) : Prop := ∃ i : Case, Matches a b c t seven i
instance (seven : Bool) (a b c t : ℕ) : Decidable (Suitable seven a b c t) := by
  unfold Suitable Matches; infer_instance

set_option maxHeartbeats 0 in
theorem seven_high_strict : ∀ a b c t : Fin 4,
    1 ≤ a.val → 1 ≤ b.val → 1 ≤ c.val →
    t.val ≤ a.val → t.val ≤ b.val → t.val ≤ c.val →
    (a.val=3 ∨ b.val=3 ∨ c.val=3) → Suitable true a.val b.val c.val t.val := by decide +kernel

theorem propertyB_of_suitable (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (edges34 : H.edges.card=34) (x y z : Fin 20)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z) (seven : Bool)
    (dx : H.degree x=if seven then 7 else 8) (dy : H.degree y=8) (dz : H.degree z=8)
    (suitable : Suitable seven (H.codegree x y) (H.codegree x z) (H.codegree y z)
      (tripleCodegree H x y z)) : PropertyB H := by
  obtain ⟨i,ha,hb,hc,ht,kind⟩ := suitable
  apply propertyB_of_data H cover edges34 (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · simpa [degree,kind,threeVertices] using dx
    · simpa [degree,kind,threeVertices] using dy
    · simpa [degree,kind,threeVertices] using dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht
''' +script[b:]
script=script.replace('#print axioms Aris4Math.ThirtyFour.TwentyRemainingTriples.propertyB_of_three_sevens','#print axioms Aris4Math.ThirtyFour.TwentyRemainingTriples.propertyB_of_suitable')
# Literal newline in the generated Lean string, not in the Python source token.
script=script.replace('set_option maxHeartbeats 0 in\\ntheorem p_eq_computed','set_option maxHeartbeats 0 in\ntheorem p_eq_computed')
exec(compile(script,__file__,'exec'),globals())
