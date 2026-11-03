import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow00
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow01
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow02
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow03
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow04
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow05
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow06
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow07
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow08
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow09
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow10
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow11
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow12
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow13
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow14
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow15
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow16
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow17
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow18
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow19
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow20
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow21
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow22
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow23
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow24
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow25
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow26
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow27
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow28
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow29
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow30
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow31
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow32
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow33
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow34
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow35
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow36
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow37
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow38
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow39
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow40
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow41
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow42
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow43
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow44
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow45
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow46
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow47
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow48
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow49
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow50
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow51
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow52
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow53
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow54
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow55
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow56
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow57
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow58
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow59
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow60
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow61
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow62
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow63
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow64
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow65
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow66
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow67
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow68
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow69
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow70
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow71
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow72
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow73
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow74
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow75
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow76
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow77
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow78
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow79
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow80
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow81
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow82
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow83
import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputRow84
import Mathlib.Tactic.FinCases
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

theorem projection_rows : ∀ p, ProjectionRow p := by
  intro p
  fin_cases p
  · exact projection_row_00
  · exact projection_row_01
  · exact projection_row_02
  · exact projection_row_03
  · exact projection_row_04
  · exact projection_row_05
  · exact projection_row_06
  · exact projection_row_07
  · exact projection_row_08
  · exact projection_row_09
  · exact projection_row_10
  · exact projection_row_11
  · exact projection_row_12
  · exact projection_row_13
  · exact projection_row_14
  · exact projection_row_15
  · exact projection_row_16
  · exact projection_row_17
  · exact projection_row_18
  · exact projection_row_19
  · exact projection_row_20
  · exact projection_row_21
  · exact projection_row_22
  · exact projection_row_23
  · exact projection_row_24
  · exact projection_row_25
  · exact projection_row_26
  · exact projection_row_27
  · exact projection_row_28
  · exact projection_row_29
  · exact projection_row_30
  · exact projection_row_31
  · exact projection_row_32
  · exact projection_row_33
  · exact projection_row_34
  · exact projection_row_35
  · exact projection_row_36
  · exact projection_row_37
  · exact projection_row_38
  · exact projection_row_39
  · exact projection_row_40
  · exact projection_row_41
  · exact projection_row_42
  · exact projection_row_43
  · exact projection_row_44
  · exact projection_row_45
  · exact projection_row_46
  · exact projection_row_47
  · exact projection_row_48
  · exact projection_row_49
  · exact projection_row_50
  · exact projection_row_51
  · exact projection_row_52
  · exact projection_row_53
  · exact projection_row_54
  · exact projection_row_55
  · exact projection_row_56
  · exact projection_row_57
  · exact projection_row_58
  · exact projection_row_59
  · exact projection_row_60
  · exact projection_row_61
  · exact projection_row_62
  · exact projection_row_63
  · exact projection_row_64
  · exact projection_row_65
  · exact projection_row_66
  · exact projection_row_67
  · exact projection_row_68
  · exact projection_row_69
  · exact projection_row_70
  · exact projection_row_71
  · exact projection_row_72
  · exact projection_row_73
  · exact projection_row_74
  · exact projection_row_75
  · exact projection_row_76
  · exact projection_row_77
  · exact projection_row_78
  · exact projection_row_79
  · exact projection_row_80
  · exact projection_row_81
  · exact projection_row_82
  · exact projection_row_83
  · exact projection_row_84

theorem projection : ∀ p l, ∃ q m, Inc q l ∧ Inc p m ∧ Inc q m := projection_rows
#print axioms projection
end DegreeDiameter.Portfolio.OppositeGQ44Spread
