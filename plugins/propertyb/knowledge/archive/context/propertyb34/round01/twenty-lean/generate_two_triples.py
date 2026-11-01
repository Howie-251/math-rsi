from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
original=(ROOT/'context/propertyb34-hour1-20261013/nineteen/generate_twenty_seven_triples.py').read_text()
start=original.index('D=[]');end=original.index("print('labelled'",start)
load='''D=[]
raw=json.load(open(ROOT/'context/propertyb34-hour1-20261013/low-math/SEVEN_TWO_VERIFIED.json'))['cases']
for r in raw:
 if r['ds'] != [7,7,8]:continue
 a,b,c=r['ls'];t=r['t'];pos=tuple(r['pos']);counts={int(k):v for k,v in r['counts'].items()}
 p0=Profile(20,5,pos,counts);loss=[];flags=[]
 for j,d in enumerate(r['ds']):
  total=link_certificate(p0,j,(4*d-19+2)//3)['deduction'];q=max(0,(4*counts[1<<j]+2-17)//3)
  pure=q*2*pair_weight(20,5,pos,1<<j,1<<j,pos[j]);loss.append(max(total,pure));flags.append(pure>total)
 bound=total_bound(rows(p0,deductions=dict(zip(pos,loss))))
 assert bound<1
 D.append(dict(a=a,b=b,c=c,t=t,high=True,pos=pos,counts=counts,loss=loss,pure=flags,bound=bound))
'''
script=original[:start]+load+original[end:]
script=script.replace('parents[3]','parents[4]').replace('TwentySevenTriples','TwentySevenTwoTriples').replace('Fin 39','Fin 41').replace('TWENTY_SEVEN_TRIPLE_DATA','TWO_TRIPLE_DATA')
a=script.index('theorem coverage_seven');b=script.index('\nend Aris4Math.ThirtyFour.TwentySevenTwoTriples',a)
script=script[:a]+'''theorem coverage : ∀ a b c t : Fin 4,
    (a.val=2 ∨ a.val=3) → 1 ≤ b.val → 1 ≤ c.val →
    t.val ≤ a.val → t.val ≤ b.val → t.val ≤ c.val →
    (a.val=3 ∨ (a.val=2 ∧ ¬ ((b.val=1 ∧ c.val=1 ∧ t.val=0) ∨ (b.val=2 ∧ c.val=2)))) →
    ∃ i, Matches a.val b.val c.val t.val true i := by decide +kernel

theorem residual_of_not_propertyB (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (edges34 : H.edges.card=34) (noB : ¬ PropertyB H) (x y z : Fin 20)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (dx : H.degree x=7) (dy : H.degree y=7) (dz : H.degree z=8)
    (ca : H.codegree x y=2 ∨ H.codegree x y=3)
    (cb : H.codegree x z ≤ 3) (cc : H.codegree y z ≤ 3) :
    H.codegree x y=2 ∧
    ((H.codegree x z=1 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=0) ∨
      (H.codegree x z=2 ∧ H.codegree y z=2)) := by
  have lb := H.one_le_codegree cover xz
  have lc := H.one_le_codegree cover yz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  by_contra hn
  have good : H.codegree x y=3 ∨ (H.codegree x y=2 ∧
      ¬ ((H.codegree x z=1 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=0) ∨
        (H.codegree x z=2 ∧ H.codegree y z=2))) := by
    rcases ca with ca | ca
    · exact Or.inr ⟨ca,fun h => hn ⟨ca,h⟩⟩
    · exact Or.inl ca
  obtain ⟨i,ha,hb,hc,ht,kind⟩ := coverage
    ⟨H.codegree x y,by omega⟩ ⟨H.codegree x z,by omega⟩ ⟨H.codegree y z,by omega⟩
    ⟨tripleCodegree H x y z,by omega⟩ ca lb lc ta tb tc good
  apply noB
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
script=script.replace('#print axioms Aris4Math.ThirtyFour.TwentySevenTwoTriples.propertyB_of_three_sevens','#print axioms Aris4Math.ThirtyFour.TwentySevenTwoTriples.residual_of_not_propertyB')
exec(compile(script,__file__,'exec'),globals())
