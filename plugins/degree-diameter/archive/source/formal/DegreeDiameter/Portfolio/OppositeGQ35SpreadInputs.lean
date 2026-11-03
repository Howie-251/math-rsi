import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow00
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow01
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow02
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow03
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow04
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow05
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow06
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow07
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow08
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow09
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow10
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow11
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow12
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow13
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow14
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow15
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow16
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow17
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow18
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow19
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow20
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow21
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow22
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow23
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow24
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow25
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow26
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow27
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow28
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow29
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow30
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow31
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow32
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow33
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow34
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow35
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow36
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow37
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow38
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow39
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow40
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow41
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow42
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow43
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow44
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow45
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow46
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow47
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow48
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow49
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow50
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow51
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow52
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow53
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow54
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow55
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow56
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow57
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow58
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow59
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow60
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow61
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow62
import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputRow63
import Mathlib.Tactic.FinCases
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

theorem inputRows : ∀ p, InputRow p := by
  intro p
  fin_cases p
  · exact input_row_00
  · exact input_row_01
  · exact input_row_02
  · exact input_row_03
  · exact input_row_04
  · exact input_row_05
  · exact input_row_06
  · exact input_row_07
  · exact input_row_08
  · exact input_row_09
  · exact input_row_10
  · exact input_row_11
  · exact input_row_12
  · exact input_row_13
  · exact input_row_14
  · exact input_row_15
  · exact input_row_16
  · exact input_row_17
  · exact input_row_18
  · exact input_row_19
  · exact input_row_20
  · exact input_row_21
  · exact input_row_22
  · exact input_row_23
  · exact input_row_24
  · exact input_row_25
  · exact input_row_26
  · exact input_row_27
  · exact input_row_28
  · exact input_row_29
  · exact input_row_30
  · exact input_row_31
  · exact input_row_32
  · exact input_row_33
  · exact input_row_34
  · exact input_row_35
  · exact input_row_36
  · exact input_row_37
  · exact input_row_38
  · exact input_row_39
  · exact input_row_40
  · exact input_row_41
  · exact input_row_42
  · exact input_row_43
  · exact input_row_44
  · exact input_row_45
  · exact input_row_46
  · exact input_row_47
  · exact input_row_48
  · exact input_row_49
  · exact input_row_50
  · exact input_row_51
  · exact input_row_52
  · exact input_row_53
  · exact input_row_54
  · exact input_row_55
  · exact input_row_56
  · exact input_row_57
  · exact input_row_58
  · exact input_row_59
  · exact input_row_60
  · exact input_row_61
  · exact input_row_62
  · exact input_row_63

theorem projection : ∀ p l, ∃ q m, Inc q l ∧ Inc p m ∧ Inc q m := by
  intro p l
  exact ⟨projectionPoint p l,projectionLine p l,(inputRows p).1 l⟩
theorem pointLine_covers : ∀ p l, Inc p l → ∃ i, pointLine p i = l :=
  fun p => (inputRows p).2.1
theorem spread_unique : ∀ p j, Inc p (spread j) → j = spreadOwner p :=
  fun p => (inputRows p).2.2
theorem linePoint_covers : ∀ p l, Inc p l → ∃ i, linePoint l i = p := by
  intro p l h
  exact h
theorem spread_nonempty : ∀ j, ∃ p, Inc p (spread j) := by
  intro j
  exact ⟨linePoint (spread j) 0,0,rfl⟩
#print axioms projection
#print axioms pointLine_covers
#print axioms spread_unique
end DegreeDiameter.Portfolio.OppositeGQ35Spread
