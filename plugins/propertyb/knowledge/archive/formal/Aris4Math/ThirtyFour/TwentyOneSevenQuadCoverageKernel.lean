import Aris4Math.ThirtyFour.TwentyOneSevenQuadCoverageData
namespace Aris4Math.ThirtyFour.TwentyOneSevenQuadCoverage
open scoped BigOperators
open Aris4Math.ThirtyThree.QuadProfiles
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem coverage00 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 0 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 0 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 0) h)).2).toEmbedding)=μ (choose (code (coFn 0) h)).1 T) := by decide +kernel

theorem coverage01 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 1 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 1 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 1) h)).2).toEmbedding)=μ (choose (code (coFn 1) h)).1 T) := by decide +kernel

theorem coverage02 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 2 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 2 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 2) h)).2).toEmbedding)=μ (choose (code (coFn 2) h)).1 T) := by decide +kernel

theorem coverage03 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 3 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 3 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 3) h)).2).toEmbedding)=μ (choose (code (coFn 3) h)).1 T) := by decide +kernel

theorem coverage04 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 4 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 4 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 4) h)).2).toEmbedding)=μ (choose (code (coFn 4) h)).1 T) := by decide +kernel

theorem coverage05 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 5 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 5 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 5) h)).2).toEmbedding)=μ (choose (code (coFn 5) h)).1 T) := by decide +kernel

theorem coverage06 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 6 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 6 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 6) h)).2).toEmbedding)=μ (choose (code (coFn 6) h)).1 T) := by decide +kernel

theorem coverage07 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 7 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 7 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 7) h)).2).toEmbedding)=μ (choose (code (coFn 7) h)).1 T) := by decide +kernel

theorem coverage08 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 8 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 8 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 8) h)).2).toEmbedding)=μ (choose (code (coFn 8) h)).1 T) := by decide +kernel

theorem coverage09 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 9 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 9 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 9) h)).2).toEmbedding)=μ (choose (code (coFn 9) h)).1 T) := by decide +kernel

theorem coverage10 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 10 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 10 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 10) h)).2).toEmbedding)=μ (choose (code (coFn 10) h)).1 T) := by decide +kernel

theorem coverage11 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 11 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 11 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 11) h)).2).toEmbedding)=μ (choose (code (coFn 11) h)).1 T) := by decide +kernel

theorem coverage12 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 12 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 12 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 12) h)).2).toEmbedding)=μ (choose (code (coFn 12) h)).1 T) := by decide +kernel

theorem coverage13 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 13 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 13 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 13) h)).2).toEmbedding)=μ (choose (code (coFn 13) h)).1 T) := by decide +kernel

theorem coverage14 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 14 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 14 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 14) h)).2).toEmbedding)=μ (choose (code (coFn 14) h)).1 T) := by decide +kernel

theorem coverage15 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 15 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 15 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 15) h)).2).toEmbedding)=μ (choose (code (coFn 15) h)).1 T) := by decide +kernel

theorem coverage16 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 16 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 16 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 16) h)).2).toEmbedding)=μ (choose (code (coFn 16) h)).1 T) := by decide +kernel

theorem coverage17 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 17 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 17 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 17) h)).2).toEmbedding)=μ (choose (code (coFn 17) h)).1 T) := by decide +kernel

theorem coverage18 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 18 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 18 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 18) h)).2).toEmbedding)=μ (choose (code (coFn 18) h)).1 T) := by decide +kernel

theorem coverage19 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 19 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 19 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 19) h)).2).toEmbedding)=μ (choose (code (coFn 19) h)).1 T) := by decide +kernel

theorem coverage20 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 20 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 20 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 20) h)).2).toEmbedding)=μ (choose (code (coFn 20) h)).1 T) := by decide +kernel

theorem coverage21 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 21 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 21 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 21) h)).2).toEmbedding)=μ (choose (code (coFn 21) h)).1 T) := by decide +kernel

theorem coverage22 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 22 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 22 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 22) h)).2).toEmbedding)=μ (choose (code (coFn 22) h)).1 T) := by decide +kernel

theorem coverage23 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 23 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 23 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 23) h)).2).toEmbedding)=μ (choose (code (coFn 23) h)).1 T) := by decide +kernel

theorem coverage24 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 24 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 24 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 24) h)).2).toEmbedding)=μ (choose (code (coFn 24) h)).1 T) := by decide +kernel

theorem coverage25 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 25 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 25 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 25) h)).2).toEmbedding)=μ (choose (code (coFn 25) h)).1 T) := by decide +kernel

theorem coverage26 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 26 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 26 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 26) h)).2).toEmbedding)=μ (choose (code (coFn 26) h)).1 T) := by decide +kernel

theorem coverage27 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 27 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 27 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 27) h)).2).toEmbedding)=μ (choose (code (coFn 27) h)).1 T) := by decide +kernel

theorem coverage28 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 28 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 28 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 28) h)).2).toEmbedding)=μ (choose (code (coFn 28) h)).1 T) := by decide +kernel

theorem coverage29 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 29 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 29 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 29) h)).2).toEmbedding)=μ (choose (code (coFn 29) h)).1 T) := by decide +kernel

theorem coverage30 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 30 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 30 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 30) h)).2).toEmbedding)=μ (choose (code (coFn 30) h)).1 T) := by decide +kernel

theorem coverage31 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 31 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 31 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 31) h)).2).toEmbedding)=μ (choose (code (coFn 31) h)).1 T) := by decide +kernel

theorem coverage32 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 32 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 32 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 32) h)).2).toEmbedding)=μ (choose (code (coFn 32) h)).1 T) := by decide +kernel

theorem coverage33 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 33 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 33 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 33) h)).2).toEmbedding)=μ (choose (code (coFn 33) h)).1 T) := by decide +kernel

theorem coverage34 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 34 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 34 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 34) h)).2).toEmbedding)=μ (choose (code (coFn 34) h)).1 T) := by decide +kernel

theorem coverage35 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 35 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 35 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 35) h)).2).toEmbedding)=μ (choose (code (coFn 35) h)).1 T) := by decide +kernel

theorem coverage36 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 36 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 36 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 36) h)).2).toEmbedding)=μ (choose (code (coFn 36) h)).1 T) := by decide +kernel

theorem coverage37 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 37 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 37 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 37) h)).2).toEmbedding)=μ (choose (code (coFn 37) h)).1 T) := by decide +kernel

theorem coverage38 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 38 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 38 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 38) h)).2).toEmbedding)=μ (choose (code (coFn 38) h)).1 T) := by decide +kernel

theorem coverage39 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 39 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 39 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 39) h)).2).toEmbedding)=μ (choose (code (coFn 39) h)).1 T) := by decide +kernel

theorem coverage40 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 40 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 40 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 40) h)).2).toEmbedding)=μ (choose (code (coFn 40) h)).1 T) := by decide +kernel

theorem coverage41 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 41 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 41 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 41) h)).2).toEmbedding)=μ (choose (code (coFn 41) h)).1 T) := by decide +kernel

theorem coverage42 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 42 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 42 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 42) h)).2).toEmbedding)=μ (choose (code (coFn 42) h)).1 T) := by decide +kernel

theorem coverage43 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 43 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 43 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 43) h)).2).toEmbedding)=μ (choose (code (coFn 43) h)).1 T) := by decide +kernel

theorem coverage44 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 44 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 44 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 44) h)).2).toEmbedding)=μ (choose (code (coFn 44) h)).1 T) := by decide +kernel

theorem coverage45 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 45 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 45 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 45) h)).2).toEmbedding)=μ (choose (code (coFn 45) h)).1 T) := by decide +kernel

theorem coverage46 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 46 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 46 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 46) h)).2).toEmbedding)=μ (choose (code (coFn 46) h)).1 T) := by decide +kernel

theorem coverage47 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 47 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 47 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 47) h)).2).toEmbedding)=μ (choose (code (coFn 47) h)).1 T) := by decide +kernel

theorem coverage48 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 48 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 48 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 48) h)).2).toEmbedding)=μ (choose (code (coFn 48) h)).1 T) := by decide +kernel

theorem coverage49 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 49 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 49 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 49) h)).2).toEmbedding)=μ (choose (code (coFn 49) h)).1 T) := by decide +kernel

theorem coverage50 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 50 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 50 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 50) h)).2).toEmbedding)=μ (choose (code (coFn 50) h)).1 T) := by decide +kernel

theorem coverage51 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 51 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 51 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 51) h)).2).toEmbedding)=μ (choose (code (coFn 51) h)).1 T) := by decide +kernel

theorem coverage52 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 52 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 52 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 52) h)).2).toEmbedding)=μ (choose (code (coFn 52) h)).1 T) := by decide +kernel

theorem coverage53 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 53 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 53 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 53) h)).2).toEmbedding)=μ (choose (code (coFn 53) h)).1 T) := by decide +kernel

theorem coverage54 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 54 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 54 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 54) h)).2).toEmbedding)=μ (choose (code (coFn 54) h)).1 T) := by decide +kernel

theorem coverage55 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 55 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 55 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 55) h)).2).toEmbedding)=μ (choose (code (coFn 55) h)).1 T) := by decide +kernel

theorem coverage56 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 56 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 56 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 56) h)).2).toEmbedding)=μ (choose (code (coFn 56) h)).1 T) := by decide +kernel

theorem coverage57 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 57 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 57 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 57) h)).2).toEmbedding)=μ (choose (code (coFn 57) h)).1 T) := by decide +kernel

theorem coverage58 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 58 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 58 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 58) h)).2).toEmbedding)=μ (choose (code (coFn 58) h)).1 T) := by decide +kernel

theorem coverage59 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 59 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 59 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 59) h)).2).toEmbedding)=μ (choose (code (coFn 59) h)).1 T) := by decide +kernel

theorem coverage60 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 60 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 60 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 60) h)).2).toEmbedding)=μ (choose (code (coFn 60) h)).1 T) := by decide +kernel

theorem coverage61 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 61 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 61 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 61) h)).2).toEmbedding)=μ (choose (code (coFn 61) h)).1 T) := by decide +kernel

theorem coverage62 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 62 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 62 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 62) h)).2).toEmbedding)=μ (choose (code (coFn 62) h)).1 T) := by decide +kernel

theorem coverage63 : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn 63 j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn 63 j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn 63) h)).2).toEmbedding)=μ (choose (code (coFn 63) h)).1 T) := by decide +kernel

theorem coverage : ∀co : Fin 6→Fin 2,∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(co j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(co j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code co h)).2).toEmbedding)=μ (choose (code co h)).1 T) := by
  intro co h inventory
  obtain ⟨k,rfl⟩:=coFn_surjective co
  fin_cases k
  · exact coverage00 h inventory
  · exact coverage01 h inventory
  · exact coverage02 h inventory
  · exact coverage03 h inventory
  · exact coverage04 h inventory
  · exact coverage05 h inventory
  · exact coverage06 h inventory
  · exact coverage07 h inventory
  · exact coverage08 h inventory
  · exact coverage09 h inventory
  · exact coverage10 h inventory
  · exact coverage11 h inventory
  · exact coverage12 h inventory
  · exact coverage13 h inventory
  · exact coverage14 h inventory
  · exact coverage15 h inventory
  · exact coverage16 h inventory
  · exact coverage17 h inventory
  · exact coverage18 h inventory
  · exact coverage19 h inventory
  · exact coverage20 h inventory
  · exact coverage21 h inventory
  · exact coverage22 h inventory
  · exact coverage23 h inventory
  · exact coverage24 h inventory
  · exact coverage25 h inventory
  · exact coverage26 h inventory
  · exact coverage27 h inventory
  · exact coverage28 h inventory
  · exact coverage29 h inventory
  · exact coverage30 h inventory
  · exact coverage31 h inventory
  · exact coverage32 h inventory
  · exact coverage33 h inventory
  · exact coverage34 h inventory
  · exact coverage35 h inventory
  · exact coverage36 h inventory
  · exact coverage37 h inventory
  · exact coverage38 h inventory
  · exact coverage39 h inventory
  · exact coverage40 h inventory
  · exact coverage41 h inventory
  · exact coverage42 h inventory
  · exact coverage43 h inventory
  · exact coverage44 h inventory
  · exact coverage45 h inventory
  · exact coverage46 h inventory
  · exact coverage47 h inventory
  · exact coverage48 h inventory
  · exact coverage49 h inventory
  · exact coverage50 h inventory
  · exact coverage51 h inventory
  · exact coverage52 h inventory
  · exact coverage53 h inventory
  · exact coverage54 h inventory
  · exact coverage55 h inventory
  · exact coverage56 h inventory
  · exact coverage57 h inventory
  · exact coverage58 h inventory
  · exact coverage59 h inventory
  · exact coverage60 h inventory
  · exact coverage61 h inventory
  · exact coverage62 h inventory
  · exact coverage63 h inventory

end Aris4Math.ThirtyFour.TwentyOneSevenQuadCoverage
