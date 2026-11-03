import DegreeDiameter.Portfolio.F4Graph3840DecoderInterface
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow00
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow01
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow02
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow03
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow04
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow05
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow06
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow07
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow08
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow09
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow10
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow11
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow12
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow13
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow14
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow15
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow16
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow17
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow18
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow19
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow20
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow21
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow22
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow23
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow24
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow25
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow26
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow27
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow28
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow29
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow30
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow31
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow32
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow33
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow34
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow35
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow36
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow37
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow38
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow39
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow40
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow41
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow42
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow43
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow44
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow45
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow46
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow47
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow48
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow49
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow50
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow51
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow52
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow53
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow54
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow55
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow56
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow57
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow58
import DegreeDiameter.Portfolio.F4Graph3840CertificateRow59
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_valid (a b : Fin 60) : (¬∃ p, controller a p = b) → routeController a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) = b := by
  fin_cases a
  · exact controller_row_0 b
  · exact controller_row_1 b
  · exact controller_row_2 b
  · exact controller_row_3 b
  · exact controller_row_4 b
  · exact controller_row_5 b
  · exact controller_row_6 b
  · exact controller_row_7 b
  · exact controller_row_8 b
  · exact controller_row_9 b
  · exact controller_row_10 b
  · exact controller_row_11 b
  · exact controller_row_12 b
  · exact controller_row_13 b
  · exact controller_row_14 b
  · exact controller_row_15 b
  · exact controller_row_16 b
  · exact controller_row_17 b
  · exact controller_row_18 b
  · exact controller_row_19 b
  · exact controller_row_20 b
  · exact controller_row_21 b
  · exact controller_row_22 b
  · exact controller_row_23 b
  · exact controller_row_24 b
  · exact controller_row_25 b
  · exact controller_row_26 b
  · exact controller_row_27 b
  · exact controller_row_28 b
  · exact controller_row_29 b
  · exact controller_row_30 b
  · exact controller_row_31 b
  · exact controller_row_32 b
  · exact controller_row_33 b
  · exact controller_row_34 b
  · exact controller_row_35 b
  · exact controller_row_36 b
  · exact controller_row_37 b
  · exact controller_row_38 b
  · exact controller_row_39 b
  · exact controller_row_40 b
  · exact controller_row_41 b
  · exact controller_row_42 b
  · exact controller_row_43 b
  · exact controller_row_44 b
  · exact controller_row_45 b
  · exact controller_row_46 b
  · exact controller_row_47 b
  · exact controller_row_48 b
  · exact controller_row_49 b
  · exact controller_row_50 b
  · exact controller_row_51 b
  · exact controller_row_52 b
  · exact controller_row_53 b
  · exact controller_row_54 b
  · exact controller_row_55 b
  · exact controller_row_56 b
  · exact controller_row_57 b
  · exact controller_row_58 b
  · exact controller_row_59 b

theorem nb_basis_valid (a b : Fin 60) (j : Fin 3) : (¬∃ p, controller a p = b) → routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b (basisVec j)) 0 = basisVec j := by
  fin_cases a
  · exact nb_basis_row_0 b j
  · exact nb_basis_row_1 b j
  · exact nb_basis_row_2 b j
  · exact nb_basis_row_3 b j
  · exact nb_basis_row_4 b j
  · exact nb_basis_row_5 b j
  · exact nb_basis_row_6 b j
  · exact nb_basis_row_7 b j
  · exact nb_basis_row_8 b j
  · exact nb_basis_row_9 b j
  · exact nb_basis_row_10 b j
  · exact nb_basis_row_11 b j
  · exact nb_basis_row_12 b j
  · exact nb_basis_row_13 b j
  · exact nb_basis_row_14 b j
  · exact nb_basis_row_15 b j
  · exact nb_basis_row_16 b j
  · exact nb_basis_row_17 b j
  · exact nb_basis_row_18 b j
  · exact nb_basis_row_19 b j
  · exact nb_basis_row_20 b j
  · exact nb_basis_row_21 b j
  · exact nb_basis_row_22 b j
  · exact nb_basis_row_23 b j
  · exact nb_basis_row_24 b j
  · exact nb_basis_row_25 b j
  · exact nb_basis_row_26 b j
  · exact nb_basis_row_27 b j
  · exact nb_basis_row_28 b j
  · exact nb_basis_row_29 b j
  · exact nb_basis_row_30 b j
  · exact nb_basis_row_31 b j
  · exact nb_basis_row_32 b j
  · exact nb_basis_row_33 b j
  · exact nb_basis_row_34 b j
  · exact nb_basis_row_35 b j
  · exact nb_basis_row_36 b j
  · exact nb_basis_row_37 b j
  · exact nb_basis_row_38 b j
  · exact nb_basis_row_39 b j
  · exact nb_basis_row_40 b j
  · exact nb_basis_row_41 b j
  · exact nb_basis_row_42 b j
  · exact nb_basis_row_43 b j
  · exact nb_basis_row_44 b j
  · exact nb_basis_row_45 b j
  · exact nb_basis_row_46 b j
  · exact nb_basis_row_47 b j
  · exact nb_basis_row_48 b j
  · exact nb_basis_row_49 b j
  · exact nb_basis_row_50 b j
  · exact nb_basis_row_51 b j
  · exact nb_basis_row_52 b j
  · exact nb_basis_row_53 b j
  · exact nb_basis_row_54 b j
  · exact nb_basis_row_55 b j
  · exact nb_basis_row_56 b j
  · exact nb_basis_row_57 b j
  · exact nb_basis_row_58 b j
  · exact nb_basis_row_59 b j

theorem adjacent_valid (a : Fin 60) (p : Fin 5) (d : Fin 64) : routeVec a (adjP0 a p d) (adjP1 a p d) (adjP2 a p d) (adjNoise a p d) 0 = decodeVec d := by
  fin_cases a
  · exact adjacent_row_0 p d
  · exact adjacent_row_1 p d
  · exact adjacent_row_2 p d
  · exact adjacent_row_3 p d
  · exact adjacent_row_4 p d
  · exact adjacent_row_5 p d
  · exact adjacent_row_6 p d
  · exact adjacent_row_7 p d
  · exact adjacent_row_8 p d
  · exact adjacent_row_9 p d
  · exact adjacent_row_10 p d
  · exact adjacent_row_11 p d
  · exact adjacent_row_12 p d
  · exact adjacent_row_13 p d
  · exact adjacent_row_14 p d
  · exact adjacent_row_15 p d
  · exact adjacent_row_16 p d
  · exact adjacent_row_17 p d
  · exact adjacent_row_18 p d
  · exact adjacent_row_19 p d
  · exact adjacent_row_20 p d
  · exact adjacent_row_21 p d
  · exact adjacent_row_22 p d
  · exact adjacent_row_23 p d
  · exact adjacent_row_24 p d
  · exact adjacent_row_25 p d
  · exact adjacent_row_26 p d
  · exact adjacent_row_27 p d
  · exact adjacent_row_28 p d
  · exact adjacent_row_29 p d
  · exact adjacent_row_30 p d
  · exact adjacent_row_31 p d
  · exact adjacent_row_32 p d
  · exact adjacent_row_33 p d
  · exact adjacent_row_34 p d
  · exact adjacent_row_35 p d
  · exact adjacent_row_36 p d
  · exact adjacent_row_37 p d
  · exact adjacent_row_38 p d
  · exact adjacent_row_39 p d
  · exact adjacent_row_40 p d
  · exact adjacent_row_41 p d
  · exact adjacent_row_42 p d
  · exact adjacent_row_43 p d
  · exact adjacent_row_44 p d
  · exact adjacent_row_45 p d
  · exact adjacent_row_46 p d
  · exact adjacent_row_47 p d
  · exact adjacent_row_48 p d
  · exact adjacent_row_49 p d
  · exact adjacent_row_50 p d
  · exact adjacent_row_51 p d
  · exact adjacent_row_52 p d
  · exact adjacent_row_53 p d
  · exact adjacent_row_54 p d
  · exact adjacent_row_55 p d
  · exact adjacent_row_56 p d
  · exact adjacent_row_57 p d
  · exact adjacent_row_58 p d
  · exact adjacent_row_59 p d

theorem nb_noise_valid (a b : Fin 60) (h : ¬∃ p, controller a p = b) (d : Vec) :
  routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b d) 0 = d :=
  noise_decode_of_basis a b (fun j => nb_basis_valid a b j h) d

#print axioms nb_noise_valid
#print axioms adjacent_valid
end DegreeDiameter.Portfolio.F4Graph3840
