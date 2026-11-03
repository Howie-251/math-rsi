import DegreeDiameter.Portfolio.F3Graph15552FullFirstFour
import DegreeDiameter.Portfolio.F3Graph15552Row0FullrankCertificate
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert00
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert01
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert02
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert03
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert04
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert05
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert06
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert07
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert08
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert09
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert10
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert11
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert12
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert13
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert14
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert15
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert16
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert17
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert18
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert19
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert20
import DegreeDiameter.Portfolio.F3Graph15552FullCosetCert21
namespace DegreeDiameter.Portfolio.F3Graph15552.FullKernel
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
def packageG0 : CosetEndpoint := makeCoset PilotLargestGroup.reference PilotLargestGroup.word PilotLargestGroup.column PilotLargestGroup.choice PilotLargestGroup.alpha PilotLargestGroup.column_certificate PilotLargestGroup.cover_certificate PilotLargestGroup.length_certificate
def packageG1 : CosetEndpoint := firstFourPackage (0 : Fin 4)
def packageG2 : CosetEndpoint := firstFourPackage (1 : Fin 4)
def packageG3 : CosetEndpoint := firstFourPackage (2 : Fin 4)
def packageG4 : CosetEndpoint := firstFourPackage (3 : Fin 4)
def packageG6 : CosetEndpoint := makeCoset FullCoset6.reference FullCoset6.word FullCoset6.column FullCoset6.choice FullCoset6.alpha FullCoset6.column_certificate FullCoset6.cover_certificate FullCoset6.length_certificate
def packageG7 : CosetEndpoint := makeCoset FullCoset7.reference FullCoset7.word FullCoset7.column FullCoset7.choice FullCoset7.alpha FullCoset7.column_certificate FullCoset7.cover_certificate FullCoset7.length_certificate
def packageG9 : CosetEndpoint := makeCoset FullCoset9.reference FullCoset9.word FullCoset9.column FullCoset9.choice FullCoset9.alpha FullCoset9.column_certificate FullCoset9.cover_certificate FullCoset9.length_certificate
def packageG10 : CosetEndpoint := makeCoset FullCoset10.reference FullCoset10.word FullCoset10.column FullCoset10.choice FullCoset10.alpha FullCoset10.column_certificate FullCoset10.cover_certificate FullCoset10.length_certificate
def packageG11 : CosetEndpoint := makeCoset FullCoset11.reference FullCoset11.word FullCoset11.column FullCoset11.choice FullCoset11.alpha FullCoset11.column_certificate FullCoset11.cover_certificate FullCoset11.length_certificate
def packageG12 : CosetEndpoint := makeCoset FullCoset12.reference FullCoset12.word FullCoset12.column FullCoset12.choice FullCoset12.alpha FullCoset12.column_certificate FullCoset12.cover_certificate FullCoset12.length_certificate
def packageG13 : CosetEndpoint := makeCoset FullCoset13.reference FullCoset13.word FullCoset13.column FullCoset13.choice FullCoset13.alpha FullCoset13.column_certificate FullCoset13.cover_certificate FullCoset13.length_certificate
def packageG14 : CosetEndpoint := makeCoset FullCoset14.reference FullCoset14.word FullCoset14.column FullCoset14.choice FullCoset14.alpha FullCoset14.column_certificate FullCoset14.cover_certificate FullCoset14.length_certificate
def packageG15 : CosetEndpoint := makeCoset FullCoset15.reference FullCoset15.word FullCoset15.column FullCoset15.choice FullCoset15.alpha FullCoset15.column_certificate FullCoset15.cover_certificate FullCoset15.length_certificate
def packageG16 : CosetEndpoint := makeCoset FullCoset16.reference FullCoset16.word FullCoset16.column FullCoset16.choice FullCoset16.alpha FullCoset16.column_certificate FullCoset16.cover_certificate FullCoset16.length_certificate
def packageG17 : CosetEndpoint := makeCoset FullCoset17.reference FullCoset17.word FullCoset17.column FullCoset17.choice FullCoset17.alpha FullCoset17.column_certificate FullCoset17.cover_certificate FullCoset17.length_certificate
def packageG18 : CosetEndpoint := makeCoset FullCoset18.reference FullCoset18.word FullCoset18.column FullCoset18.choice FullCoset18.alpha FullCoset18.column_certificate FullCoset18.cover_certificate FullCoset18.length_certificate
def packageG19 : CosetEndpoint := makeCoset FullCoset19.reference FullCoset19.word FullCoset19.column FullCoset19.choice FullCoset19.alpha FullCoset19.column_certificate FullCoset19.cover_certificate FullCoset19.length_certificate
def packageG21 : CosetEndpoint := makeCoset FullCoset21.reference FullCoset21.word FullCoset21.column FullCoset21.choice FullCoset21.alpha FullCoset21.column_certificate FullCoset21.cover_certificate FullCoset21.length_certificate
def packageG22 : CosetEndpoint := makeCoset FullCoset22.reference FullCoset22.word FullCoset22.column FullCoset22.choice FullCoset22.alpha FullCoset22.column_certificate FullCoset22.cover_certificate FullCoset22.length_certificate
def packageG23 : CosetEndpoint := makeCoset FullCoset23.reference FullCoset23.word FullCoset23.column FullCoset23.choice FullCoset23.alpha FullCoset23.column_certificate FullCoset23.cover_certificate FullCoset23.length_certificate
def packageG24 : CosetEndpoint := makeCoset FullCoset24.reference FullCoset24.word FullCoset24.column FullCoset24.choice FullCoset24.alpha FullCoset24.column_certificate FullCoset24.cover_certificate FullCoset24.length_certificate
def packageG25 : CosetEndpoint := makeCoset FullCoset25.reference FullCoset25.word FullCoset25.column FullCoset25.choice FullCoset25.alpha FullCoset25.column_certificate FullCoset25.cover_certificate FullCoset25.length_certificate
def packageG26 : CosetEndpoint := makeCoset FullCoset26.reference FullCoset26.word FullCoset26.column FullCoset26.choice FullCoset26.alpha FullCoset26.column_certificate FullCoset26.cover_certificate FullCoset26.length_certificate
def packageG27 : CosetEndpoint := makeCoset FullCoset27.reference FullCoset27.word FullCoset27.column FullCoset27.choice FullCoset27.alpha FullCoset27.column_certificate FullCoset27.cover_certificate FullCoset27.length_certificate
def packageG28 : CosetEndpoint := makeCoset FullCoset28.reference FullCoset28.word FullCoset28.column FullCoset28.choice FullCoset28.alpha FullCoset28.column_certificate FullCoset28.cover_certificate FullCoset28.length_certificate
def packageG29 : CosetEndpoint := makeCoset FullCoset29.reference FullCoset29.word FullCoset29.column FullCoset29.choice FullCoset29.alpha FullCoset29.column_certificate FullCoset29.cover_certificate FullCoset29.length_certificate
def packageG30 : CosetEndpoint := makeCoset FullCoset30.reference FullCoset30.word FullCoset30.column FullCoset30.choice FullCoset30.alpha FullCoset30.column_certificate FullCoset30.cover_certificate FullCoset30.length_certificate
def packageG31 : CosetEndpoint := makeCoset FullCoset31.reference FullCoset31.word FullCoset31.column FullCoset31.choice FullCoset31.alpha FullCoset31.column_certificate FullCoset31.cover_certificate FullCoset31.length_certificate
def packageG32 : CosetEndpoint := makeCoset FullCoset32.reference FullCoset32.word FullCoset32.column FullCoset32.choice FullCoset32.alpha FullCoset32.column_certificate FullCoset32.cover_certificate FullCoset32.length_certificate
def packageG33 : CosetEndpoint := makeCoset FullCoset33.reference FullCoset33.word FullCoset33.column FullCoset33.choice FullCoset33.alpha FullCoset33.column_certificate FullCoset33.cover_certificate FullCoset33.length_certificate
def packageG34 : CosetEndpoint := makeCoset FullCoset34.reference FullCoset34.word FullCoset34.column FullCoset34.choice FullCoset34.alpha FullCoset34.column_certificate FullCoset34.cover_certificate FullCoset34.length_certificate
def packageG35 : CosetEndpoint := makeCoset FullCoset35.reference FullCoset35.word FullCoset35.column FullCoset35.choice FullCoset35.alpha FullCoset35.column_certificate FullCoset35.cover_certificate FullCoset35.length_certificate
def packageG36 : CosetEndpoint := makeCoset FullCoset36.reference FullCoset36.word FullCoset36.column FullCoset36.choice FullCoset36.alpha FullCoset36.column_certificate FullCoset36.cover_certificate FullCoset36.length_certificate
def packageG37 : CosetEndpoint := makeCoset FullCoset37.reference FullCoset37.word FullCoset37.column FullCoset37.choice FullCoset37.alpha FullCoset37.column_certificate FullCoset37.cover_certificate FullCoset37.length_certificate
def packageG38 : CosetEndpoint := makeCoset FullCoset38.reference FullCoset38.word FullCoset38.column FullCoset38.choice FullCoset38.alpha FullCoset38.column_certificate FullCoset38.cover_certificate FullCoset38.length_certificate
def packageG39 : CosetEndpoint := makeCoset FullCoset39.reference FullCoset39.word FullCoset39.column FullCoset39.choice FullCoset39.alpha FullCoset39.column_certificate FullCoset39.cover_certificate FullCoset39.length_certificate
def packageG40 : CosetEndpoint := makeCoset FullCoset40.reference FullCoset40.word FullCoset40.column FullCoset40.choice FullCoset40.alpha FullCoset40.column_certificate FullCoset40.cover_certificate FullCoset40.length_certificate
def packageG41 : CosetEndpoint := makeCoset FullCoset41.reference FullCoset41.word FullCoset41.column FullCoset41.choice FullCoset41.alpha FullCoset41.column_certificate FullCoset41.cover_certificate FullCoset41.length_certificate
def packageG42 : CosetEndpoint := makeCoset FullCoset42.reference FullCoset42.word FullCoset42.column FullCoset42.choice FullCoset42.alpha FullCoset42.column_certificate FullCoset42.cover_certificate FullCoset42.length_certificate
def packageG43 : CosetEndpoint := makeCoset FullCoset43.reference FullCoset43.word FullCoset43.column FullCoset43.choice FullCoset43.alpha FullCoset43.column_certificate FullCoset43.cover_certificate FullCoset43.length_certificate
def packageG44 : CosetEndpoint := makeCoset FullCoset44.reference FullCoset44.word FullCoset44.column FullCoset44.choice FullCoset44.alpha FullCoset44.column_certificate FullCoset44.cover_certificate FullCoset44.length_certificate
def packageG45 : CosetEndpoint := makeCoset FullCoset45.reference FullCoset45.word FullCoset45.column FullCoset45.choice FullCoset45.alpha FullCoset45.column_certificate FullCoset45.cover_certificate FullCoset45.length_certificate
def packageG46 : CosetEndpoint := makeCoset FullCoset46.reference FullCoset46.word FullCoset46.column FullCoset46.choice FullCoset46.alpha FullCoset46.column_certificate FullCoset46.cover_certificate FullCoset46.length_certificate
def packageG47 : CosetEndpoint := makeCoset FullCoset47.reference FullCoset47.word FullCoset47.column FullCoset47.choice FullCoset47.alpha FullCoset47.column_certificate FullCoset47.cover_certificate FullCoset47.length_certificate
def packageG48 : CosetEndpoint := makeCoset FullCoset48.reference FullCoset48.word FullCoset48.column FullCoset48.choice FullCoset48.alpha FullCoset48.column_certificate FullCoset48.cover_certificate FullCoset48.length_certificate
def packageG49 : CosetEndpoint := makeCoset FullCoset49.reference FullCoset49.word FullCoset49.column FullCoset49.choice FullCoset49.alpha FullCoset49.column_certificate FullCoset49.cover_certificate FullCoset49.length_certificate
def packageG50 : CosetEndpoint := makeCoset FullCoset50.reference FullCoset50.word FullCoset50.column FullCoset50.choice FullCoset50.alpha FullCoset50.column_certificate FullCoset50.cover_certificate FullCoset50.length_certificate
def packageG51 : CosetEndpoint := makeCoset FullCoset51.reference FullCoset51.word FullCoset51.column FullCoset51.choice FullCoset51.alpha FullCoset51.column_certificate FullCoset51.cover_certificate FullCoset51.length_certificate
def packageG52 : CosetEndpoint := makeCoset FullCoset52.reference FullCoset52.word FullCoset52.column FullCoset52.choice FullCoset52.alpha FullCoset52.column_certificate FullCoset52.cover_certificate FullCoset52.length_certificate
def packageG54 : CosetEndpoint := makeCoset FullCoset54.reference FullCoset54.word FullCoset54.column FullCoset54.choice FullCoset54.alpha FullCoset54.column_certificate FullCoset54.cover_certificate FullCoset54.length_certificate
def packageG55 : CosetEndpoint := makeCoset FullCoset55.reference FullCoset55.word FullCoset55.column FullCoset55.choice FullCoset55.alpha FullCoset55.column_certificate FullCoset55.cover_certificate FullCoset55.length_certificate
def packageG56 : CosetEndpoint := makeCoset FullCoset56.reference FullCoset56.word FullCoset56.column FullCoset56.choice FullCoset56.alpha FullCoset56.column_certificate FullCoset56.cover_certificate FullCoset56.length_certificate
def packageG57 : CosetEndpoint := makeCoset FullCoset57.reference FullCoset57.word FullCoset57.column FullCoset57.choice FullCoset57.alpha FullCoset57.column_certificate FullCoset57.cover_certificate FullCoset57.length_certificate
def packageG58 : CosetEndpoint := makeCoset FullCoset58.reference FullCoset58.word FullCoset58.column FullCoset58.choice FullCoset58.alpha FullCoset58.column_certificate FullCoset58.cover_certificate FullCoset58.length_certificate
def packageG59 : CosetEndpoint := makeCoset FullCoset59.reference FullCoset59.word FullCoset59.column FullCoset59.choice FullCoset59.alpha FullCoset59.column_certificate FullCoset59.cover_certificate FullCoset59.length_certificate
def packageG60 : CosetEndpoint := makeCoset FullCoset60.reference FullCoset60.word FullCoset60.column FullCoset60.choice FullCoset60.alpha FullCoset60.column_certificate FullCoset60.cover_certificate FullCoset60.length_certificate
def packageG61 : CosetEndpoint := makeCoset FullCoset61.reference FullCoset61.word FullCoset61.column FullCoset61.choice FullCoset61.alpha FullCoset61.column_certificate FullCoset61.cover_certificate FullCoset61.length_certificate
def packageG62 : CosetEndpoint := makeCoset FullCoset62.reference FullCoset62.word FullCoset62.column FullCoset62.choice FullCoset62.alpha FullCoset62.column_certificate FullCoset62.cover_certificate FullCoset62.length_certificate
def packageG63 : CosetEndpoint := makeCoset FullCoset63.reference FullCoset63.word FullCoset63.column FullCoset63.choice FullCoset63.alpha FullCoset63.column_certificate FullCoset63.cover_certificate FullCoset63.length_certificate
def packageG64 : CosetEndpoint := makeCoset FullCoset64.reference FullCoset64.word FullCoset64.column FullCoset64.choice FullCoset64.alpha FullCoset64.column_certificate FullCoset64.cover_certificate FullCoset64.length_certificate
def packageG65 : CosetEndpoint := makeCoset FullCoset65.reference FullCoset65.word FullCoset65.column FullCoset65.choice FullCoset65.alpha FullCoset65.column_certificate FullCoset65.cover_certificate FullCoset65.length_certificate
def packageG67 : CosetEndpoint := makeCoset FullCoset67.reference FullCoset67.word FullCoset67.column FullCoset67.choice FullCoset67.alpha FullCoset67.column_certificate FullCoset67.cover_certificate FullCoset67.length_certificate
def packageG68 : CosetEndpoint := makeCoset FullCoset68.reference FullCoset68.word FullCoset68.column FullCoset68.choice FullCoset68.alpha FullCoset68.column_certificate FullCoset68.cover_certificate FullCoset68.length_certificate
def packageG69 : CosetEndpoint := makeCoset FullCoset69.reference FullCoset69.word FullCoset69.column FullCoset69.choice FullCoset69.alpha FullCoset69.column_certificate FullCoset69.cover_certificate FullCoset69.length_certificate
def packageG70 : CosetEndpoint := makeCoset FullCoset70.reference FullCoset70.word FullCoset70.column FullCoset70.choice FullCoset70.alpha FullCoset70.column_certificate FullCoset70.cover_certificate FullCoset70.length_certificate
def packageG71 : CosetEndpoint := makeCoset FullCoset71.reference FullCoset71.word FullCoset71.column FullCoset71.choice FullCoset71.alpha FullCoset71.column_certificate FullCoset71.cover_certificate FullCoset71.length_certificate
def packageG72 : CosetEndpoint := makeCoset FullCoset72.reference FullCoset72.word FullCoset72.column FullCoset72.choice FullCoset72.alpha FullCoset72.column_certificate FullCoset72.cover_certificate FullCoset72.length_certificate
def packageG73 : CosetEndpoint := makeCoset FullCoset73.reference FullCoset73.word FullCoset73.column FullCoset73.choice FullCoset73.alpha FullCoset73.column_certificate FullCoset73.cover_certificate FullCoset73.length_certificate
def packageG74 : CosetEndpoint := makeCoset FullCoset74.reference FullCoset74.word FullCoset74.column FullCoset74.choice FullCoset74.alpha FullCoset74.column_certificate FullCoset74.cover_certificate FullCoset74.length_certificate
def packageG75 : CosetEndpoint := makeCoset FullCoset75.reference FullCoset75.word FullCoset75.column FullCoset75.choice FullCoset75.alpha FullCoset75.column_certificate FullCoset75.cover_certificate FullCoset75.length_certificate
def packageG76 : CosetEndpoint := makeCoset FullCoset76.reference FullCoset76.word FullCoset76.column FullCoset76.choice FullCoset76.alpha FullCoset76.column_certificate FullCoset76.cover_certificate FullCoset76.length_certificate
def packageG77 : CosetEndpoint := makeCoset FullCoset77.reference FullCoset77.word FullCoset77.column FullCoset77.choice FullCoset77.alpha FullCoset77.column_certificate FullCoset77.cover_certificate FullCoset77.length_certificate
def packageG78 : CosetEndpoint := makeCoset FullCoset78.reference FullCoset78.word FullCoset78.column FullCoset78.choice FullCoset78.alpha FullCoset78.column_certificate FullCoset78.cover_certificate FullCoset78.length_certificate
def packageG79 : CosetEndpoint := makeCoset FullCoset79.reference FullCoset79.word FullCoset79.column FullCoset79.choice FullCoset79.alpha FullCoset79.column_certificate FullCoset79.cover_certificate FullCoset79.length_certificate
def packageG80 : CosetEndpoint := makeCoset FullCoset80.reference FullCoset80.word FullCoset80.column FullCoset80.choice FullCoset80.alpha FullCoset80.column_certificate FullCoset80.cover_certificate FullCoset80.length_certificate
def packageG81 : CosetEndpoint := makeCoset FullCoset81.reference FullCoset81.word FullCoset81.column FullCoset81.choice FullCoset81.alpha FullCoset81.column_certificate FullCoset81.cover_certificate FullCoset81.length_certificate
def packageG83 : CosetEndpoint := makeCoset FullCoset83.reference FullCoset83.word FullCoset83.column FullCoset83.choice FullCoset83.alpha FullCoset83.column_certificate FullCoset83.cover_certificate FullCoset83.length_certificate
def packageG84 : CosetEndpoint := makeCoset FullCoset84.reference FullCoset84.word FullCoset84.column FullCoset84.choice FullCoset84.alpha FullCoset84.column_certificate FullCoset84.cover_certificate FullCoset84.length_certificate
def packageG85 : CosetEndpoint := makeCoset FullCoset85.reference FullCoset85.word FullCoset85.column FullCoset85.choice FullCoset85.alpha FullCoset85.column_certificate FullCoset85.cover_certificate FullCoset85.length_certificate
def packageG86 : CosetEndpoint := makeCoset FullCoset86.reference FullCoset86.word FullCoset86.column FullCoset86.choice FullCoset86.alpha FullCoset86.column_certificate FullCoset86.cover_certificate FullCoset86.length_certificate
def packageG87 : CosetEndpoint := makeCoset FullCoset87.reference FullCoset87.word FullCoset87.column FullCoset87.choice FullCoset87.alpha FullCoset87.column_certificate FullCoset87.cover_certificate FullCoset87.length_certificate
def packageG88 : CosetEndpoint := makeCoset FullCoset88.reference FullCoset88.word FullCoset88.column FullCoset88.choice FullCoset88.alpha FullCoset88.column_certificate FullCoset88.cover_certificate FullCoset88.length_certificate
def packageG89 : CosetEndpoint := makeCoset FullCoset89.reference FullCoset89.word FullCoset89.column FullCoset89.choice FullCoset89.alpha FullCoset89.column_certificate FullCoset89.cover_certificate FullCoset89.length_certificate
def packageG90 : CosetEndpoint := makeCoset FullCoset90.reference FullCoset90.word FullCoset90.column FullCoset90.choice FullCoset90.alpha FullCoset90.column_certificate FullCoset90.cover_certificate FullCoset90.length_certificate
def packageG91 : CosetEndpoint := makeCoset FullCoset91.reference FullCoset91.word FullCoset91.column FullCoset91.choice FullCoset91.alpha FullCoset91.column_certificate FullCoset91.cover_certificate FullCoset91.length_certificate
def packageG92 : CosetEndpoint := makeCoset FullCoset92.reference FullCoset92.word FullCoset92.column FullCoset92.choice FullCoset92.alpha FullCoset92.column_certificate FullCoset92.cover_certificate FullCoset92.length_certificate
def packageG93 : CosetEndpoint := makeCoset FullCoset93.reference FullCoset93.word FullCoset93.column FullCoset93.choice FullCoset93.alpha FullCoset93.column_certificate FullCoset93.cover_certificate FullCoset93.length_certificate
def packageG94 : CosetEndpoint := makeCoset FullCoset94.reference FullCoset94.word FullCoset94.column FullCoset94.choice FullCoset94.alpha FullCoset94.column_certificate FullCoset94.cover_certificate FullCoset94.length_certificate
def packageG95 : CosetEndpoint := makeCoset FullCoset95.reference FullCoset95.word FullCoset95.column FullCoset95.choice FullCoset95.alpha FullCoset95.column_certificate FullCoset95.cover_certificate FullCoset95.length_certificate
def packageG96 : CosetEndpoint := makeCoset FullCoset96.reference FullCoset96.word FullCoset96.column FullCoset96.choice FullCoset96.alpha FullCoset96.column_certificate FullCoset96.cover_certificate FullCoset96.length_certificate
def cosetPackage (g : Fin 91) : CosetEndpoint := (if g.val < 45 then (if g.val < 22 then (if g.val < 11 then (if g.val < 5 then (if g.val < 2 then (if g.val < 1 then packageG0 else packageG1) else (if g.val < 3 then packageG2 else (if g.val < 4 then packageG3 else packageG4))) else (if g.val < 8 then (if g.val < 6 then packageG6 else (if g.val < 7 then packageG7 else packageG9)) else (if g.val < 9 then packageG10 else (if g.val < 10 then packageG11 else packageG12)))) else (if g.val < 16 then (if g.val < 13 then (if g.val < 12 then packageG13 else packageG14) else (if g.val < 14 then packageG15 else (if g.val < 15 then packageG16 else packageG17))) else (if g.val < 19 then (if g.val < 17 then packageG18 else (if g.val < 18 then packageG19 else packageG21)) else (if g.val < 20 then packageG22 else (if g.val < 21 then packageG23 else packageG24))))) else (if g.val < 33 then (if g.val < 27 then (if g.val < 24 then (if g.val < 23 then packageG25 else packageG26) else (if g.val < 25 then packageG27 else (if g.val < 26 then packageG28 else packageG29))) else (if g.val < 30 then (if g.val < 28 then packageG30 else (if g.val < 29 then packageG31 else packageG32)) else (if g.val < 31 then packageG33 else (if g.val < 32 then packageG34 else packageG35)))) else (if g.val < 39 then (if g.val < 36 then (if g.val < 34 then packageG36 else (if g.val < 35 then packageG37 else packageG38)) else (if g.val < 37 then packageG39 else (if g.val < 38 then packageG40 else packageG41))) else (if g.val < 42 then (if g.val < 40 then packageG42 else (if g.val < 41 then packageG43 else packageG44)) else (if g.val < 43 then packageG45 else (if g.val < 44 then packageG46 else packageG47)))))) else (if g.val < 68 then (if g.val < 56 then (if g.val < 50 then (if g.val < 47 then (if g.val < 46 then packageG48 else packageG49) else (if g.val < 48 then packageG50 else (if g.val < 49 then packageG51 else packageG52))) else (if g.val < 53 then (if g.val < 51 then packageG54 else (if g.val < 52 then packageG55 else packageG56)) else (if g.val < 54 then packageG57 else (if g.val < 55 then packageG58 else packageG59)))) else (if g.val < 62 then (if g.val < 59 then (if g.val < 57 then packageG60 else (if g.val < 58 then packageG61 else packageG62)) else (if g.val < 60 then packageG63 else (if g.val < 61 then packageG64 else packageG65))) else (if g.val < 65 then (if g.val < 63 then packageG67 else (if g.val < 64 then packageG68 else packageG69)) else (if g.val < 66 then packageG70 else (if g.val < 67 then packageG71 else packageG72))))) else (if g.val < 79 then (if g.val < 73 then (if g.val < 70 then (if g.val < 69 then packageG73 else packageG74) else (if g.val < 71 then packageG75 else (if g.val < 72 then packageG76 else packageG77))) else (if g.val < 76 then (if g.val < 74 then packageG78 else (if g.val < 75 then packageG79 else packageG80)) else (if g.val < 77 then packageG81 else (if g.val < 78 then packageG83 else packageG84)))) else (if g.val < 85 then (if g.val < 82 then (if g.val < 80 then packageG85 else (if g.val < 81 then packageG86 else packageG87)) else (if g.val < 83 then packageG88 else (if g.val < 84 then packageG89 else packageG90))) else (if g.val < 88 then (if g.val < 86 then packageG91 else (if g.val < 87 then packageG92 else packageG93)) else (if g.val < 89 then packageG94 else (if g.val < 90 then packageG95 else packageG96)))))))
#print axioms rankBasis
#print axioms firstFourPackage
end DegreeDiameter.Portfolio.F3Graph15552.FullKernel
