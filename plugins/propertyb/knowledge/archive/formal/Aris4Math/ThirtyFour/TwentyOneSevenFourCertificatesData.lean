import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch000Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch001Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch002Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch003Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch004Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch005Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch006Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch007Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch008Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch009Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch010Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch011Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch012Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch013Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch014Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch015Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch016Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch017Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch018Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch019Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch020Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch021Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch022Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch023Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch024Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch025Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch026Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch027Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch028Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch029Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch030Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch031Data
import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch032Data
import Aris4Math.ThirtyFour.TwentyOneSevenJointFourEight0Data
import Aris4Math.ThirtyFour.TwentyOneSevenJointFourEight1Data
import Aris4Math.ThirtyFour.TwentyOneSevenJointFourEight3Data
import Aris4Math.ThirtyFour.TwentyOneSevenJointFourEight4Data
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCertificates
set_option maxRecDepth 100000
abbrev Choice := (Fin 33 × Fin 16) ⊕ Fin 4
def pureμ : Fin 33 → Fin 16 → Finset (Fin 5) → ℕ := ![fun i => TwentyOneSevenFive77778Batch000Data.μ i,fun i => TwentyOneSevenFive77778Batch001Data.μ i,fun i => TwentyOneSevenFive77778Batch002Data.μ i,fun i => TwentyOneSevenFive77778Batch003Data.μ i,fun i => TwentyOneSevenFive77778Batch004Data.μ i,fun i => TwentyOneSevenFive77778Batch005Data.μ i,fun i => TwentyOneSevenFive77778Batch006Data.μ i,fun i => TwentyOneSevenFive77778Batch007Data.μ i,fun i => TwentyOneSevenFive77778Batch008Data.μ i,fun i => TwentyOneSevenFive77778Batch009Data.μ i,fun i => TwentyOneSevenFive77778Batch010Data.μ i,fun i => TwentyOneSevenFive77778Batch011Data.μ i,fun i => TwentyOneSevenFive77778Batch012Data.μ i,fun i => TwentyOneSevenFive77778Batch013Data.μ i,fun i => TwentyOneSevenFive77778Batch014Data.μ i,fun i => TwentyOneSevenFive77778Batch015Data.μ i,fun i => TwentyOneSevenFive77778Batch016Data.μ i,fun i => TwentyOneSevenFive77778Batch017Data.μ i,fun i => TwentyOneSevenFive77778Batch018Data.μ i,fun i => TwentyOneSevenFive77778Batch019Data.μ i,fun i => TwentyOneSevenFive77778Batch020Data.μ i,fun i => TwentyOneSevenFive77778Batch021Data.μ i,fun i => TwentyOneSevenFive77778Batch022Data.μ i,fun i => TwentyOneSevenFive77778Batch023Data.μ i,fun i => TwentyOneSevenFive77778Batch024Data.μ i,fun i => TwentyOneSevenFive77778Batch025Data.μ i,fun i => TwentyOneSevenFive77778Batch026Data.μ i,fun i => TwentyOneSevenFive77778Batch027Data.μ i,fun i => TwentyOneSevenFive77778Batch028Data.μ i,fun i => TwentyOneSevenFive77778Batch029Data.μ i,fun i => TwentyOneSevenFive77778Batch030Data.μ i,fun i => TwentyOneSevenFive77778Batch031Data.μ i,fun i => TwentyOneSevenFive77778Batch032Data.μ ⟨i.val%10,Nat.mod_lt _ (by decide)⟩]
def jointμ : Fin 4 → Finset (Fin 5) → ℕ := ![TwentyOneSevenJointFourEight0Data.μ,TwentyOneSevenJointFourEight1Data.μ,TwentyOneSevenJointFourEight3Data.μ,TwentyOneSevenJointFourEight4Data.μ]
def counts (c : Choice) : Finset (Fin 5) → ℕ := match c with
  | Sum.inl bi => pureμ bi.1 bi.2
  | Sum.inr j => jointμ j
end Aris4Math.ThirtyFour.TwentyOneSevenFourCertificates
