from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
s=(ROOT/'context/propertyb34-hour1-20261013/nineteen/generate_twenty_seven_triples.py').read_text()
a=s.index('D=[]');b=s.index("print('labelled'",a)
s=s[:a]+'''D=[]
raw=json.load(open(ROOT/'context/propertyb34-hour1-20261013/low-math/TWENTYONE_FIVE_VERIFIED.json'))['witnesses']
for r in raw:
 if len(r['ds'])!=3:continue
 counts={int(m):n for m,n in r['counts'].items()};pos=tuple(r['pos']);p0=Profile(21,5,pos,counts);loss=[];flags=[]
 for j,d in enumerate(r['ds']):
  total=link_certificate(p0,j,max(0,(4*d-20+2)//3))['deduction'];q=max(0,(4*counts[1<<j]+2-18)//3)
  pure=q*2*pair_weight(21,5,pos,1<<j,1<<j,pos[j]);loss.append(max(total,pure));flags.append(pure>total)
 bound=total_bound(rows(p0,deductions=dict(zip(pos,loss))));assert bound<1
 ls=[sum(n for m,n in counts.items() if m&mask==mask) for mask in (3,5,6)]
 assert ls[0]==ls[1]==1
 D.append(dict(a=1,b=1,c=ls[2],t=counts.get(7,0),d=r['ds'][1],e=r['ds'][2],pos=pos,counts=counts,loss=loss,pure=flags,bound=bound))
assert len(D)==74
''' +s[b:]
s=s.replace('parents[3]','parents[4]').replace('TwentySevenTriples','TwentyOneFiveTriples').replace('Fin 39','Fin 74').replace('TWENTY_SEVEN_TRIPLE_DATA','FIVE_TRIPLE_DATA')
s=s.replace('  high : Bool','  d : ℕ\n  e : ℕ')
s=s.replace('{str(d["high"]).lower()}', '{d["d"]},{d["e"]}')
s=s.replace('if (data i).high && decide (j=2) then 8 else 7','![5,(data i).d,(data i).e] j')
s=s.replace('Fin 20','Fin 21').replace('⟨20,','⟨21,').replace('+2-17','+2-18').replace('(20-1-','(21-1-').replace('-19+2','-20+2')
s=s.replace('theorem p_eq_computed','set_option maxHeartbeats 0 in\ntheorem p_eq_computed')
a=s.index('def Matches');b=s.index('\nend Aris4Math.ThirtyFour.TwentyOneFiveTriples',a)
s=s[:a]+'''def Matches (d e c t : ℕ) (i : Case) : Prop :=
  d=(data i).d ∧ e=(data i).e ∧ c=(data i).c ∧ t=(data i).t
instance (d e c t : ℕ) (i : Case) : Decidable (Matches d e c t i) := by
  unfold Matches; infer_instance

def Suitable (d e c t : ℕ) : Prop := ∃ i : Case, Matches d e c t i
instance (d e c t : ℕ) : Decidable (Suitable d e c t) := by
  unfold Suitable Matches; infer_instance

theorem units (i : Case) : (data i).a=1 ∧ (data i).b=1 := by fin_cases i <;> decide

theorem propertyB_of_suitable (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (edges34 : H.edges.card=34) (x y z : Fin 21)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (dx : H.degree x=5) (a : H.codegree x y=1) (b : H.codegree x z=1)
    (suitable : Suitable (H.degree y) (H.degree z) (H.codegree y z)
      (tripleCodegree H x y z)) : PropertyB H := by
  obtain ⟨i,hd,he,hc,ht⟩ := suitable
  apply propertyB_of_data H cover edges34 (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · simpa [degree,threeVertices] using dx
    · simpa [degree,threeVertices] using hd
    · simpa [degree,threeVertices] using he
  · exact a.trans (units i).1.symm
  · exact b.trans (units i).2.symm
  · exact hc
  · exact ht

set_option maxHeartbeats 0 in
set_option synthInstance.maxSize 1000 in
theorem low_coverage : ∀ d e c : Fin 9, ∀ t : Fin 2,
    5 ≤ d.val → d.val ≤ 6 → d.val ≤ e.val →
    1 ≤ c.val → c.val ≤ d.val → 1+c.val ≤ d.val+t.val →
    (d.val=5 → c.val=1) → Suitable d.val e.val c.val t.val := by decide +kernel

set_option maxHeartbeats 0 in
theorem seven_coverage : ∀ c : Fin 8, ∀ t : Fin 2,
    1 ≤ c.val → 1+c.val ≤ 7+t.val →
    (c.val=2 ∧ t.val=1) ∨ Suitable 7 7 c.val t.val := by decide +kernel

set_option maxHeartbeats 0 in
theorem mixed_high : ∀ c : Fin 8, ∀ t : Fin 2,
    3 ≤ c.val → 1+c.val ≤ 7+t.val → Suitable 7 8 c.val t.val := by decide +kernel

set_option maxHeartbeats 0 in
theorem eight_high : ∀ c : Fin 9, ∀ t : Fin 2,
    3 ≤ c.val → 1+c.val ≤ 8+t.val → Suitable 8 8 c.val t.val := by decide +kernel
''' +s[b:]
s=s.replace('propertyB_of_three_sevens','propertyB_of_suitable')
exec(compile(s,__file__,'exec'),globals())
