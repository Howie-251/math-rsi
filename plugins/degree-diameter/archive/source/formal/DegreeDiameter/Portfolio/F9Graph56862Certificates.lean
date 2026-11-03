import DegreeDiameter.Portfolio.F9Graph56862ModelChunk00
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk01
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk02
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk03
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk04
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk05
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk06
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk07
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk08
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk09
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk10
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk11
import DegreeDiameter.Portfolio.F9Graph56862ModelChunk12
import DegreeDiameter.Portfolio.F9Graph56862PairChunk0
import DegreeDiameter.Portfolio.F9Graph56862PairChunk1
import DegreeDiameter.Portfolio.F9Graph56862PairChunk2
import DegreeDiameter.Portfolio.F9Graph56862PairChunk3
import DegreeDiameter.Portfolio.F9Graph56862PairChunk4
import DegreeDiameter.Portfolio.F9Graph56862PairChunk5
import DegreeDiameter.Portfolio.F9Graph56862ModelBridge
namespace DegreeDiameter.Portfolio.F9Graph56862
theorem model_basis_valid (k : Fin 169) (i : Fin 3) :
    modelNoise k (act (modelInverse k) (basisVec i)) = basisVec i := by
  obtain ⟨⟨b,j⟩,rfl⟩ := (finProdFinEquiv (m:=13) (n:=13)).surjective k
  fin_cases b
  · exact model_basis_chunk_0 j i
  · exact model_basis_chunk_1 j i
  · exact model_basis_chunk_2 j i
  · exact model_basis_chunk_3 j i
  · exact model_basis_chunk_4 j i
  · exact model_basis_chunk_5 j i
  · exact model_basis_chunk_6 j i
  · exact model_basis_chunk_7 j i
  · exact model_basis_chunk_8 j i
  · exact model_basis_chunk_9 j i
  · exact model_basis_chunk_10 j i
  · exact model_basis_chunk_11 j i
  · exact model_basis_chunk_12 j i
theorem pair_valid (a b : Fin 78) (h : ¬∃ p, controller a p = b) : PairCheck a b := by
  obtain ⟨⟨c,j⟩,rfl⟩ := (finProdFinEquiv (m:=6) (n:=13)).surjective a
  fin_cases c
  · exact pair_check_chunk_0 j b h
  · exact pair_check_chunk_1 j b h
  · exact pair_check_chunk_2 j b h
  · exact pair_check_chunk_3 j b h
  · exact pair_check_chunk_4 j b h
  · exact pair_check_chunk_5 j b h
theorem controller_valid (a b : Fin 78) (h : ¬∃ p, controller a p = b) :
    routeController a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) = b :=
  (pair_valid a b h).1
theorem nb_basis_valid (a b : Fin 78) (j : Fin 3) (h : ¬∃ p, controller a p = b) :
    routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b))
      (nbNoise a b (basisVec j)) 0 = basisVec j :=
  basis_of_pair_and_model a b j (pair_valid a b h) (model_basis_valid (modelIndex a b) j)
theorem nb_noise_valid (a b : Fin 78) (h : ¬∃ p, controller a p = b) (d : Vec) :
    routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b))
      (nbNoise a b d) 0 = d :=
  noise_decode_of_basis a b (fun j => nb_basis_valid a b j h) d
#print axioms nb_noise_valid
end DegreeDiameter.Portfolio.F9Graph56862
