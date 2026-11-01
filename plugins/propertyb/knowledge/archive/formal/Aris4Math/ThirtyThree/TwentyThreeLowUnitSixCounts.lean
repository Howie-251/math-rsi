import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCatalogData
import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixBare
import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDual

namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCounts
open MultiLockRecovery TwentyThreeLowUnitSixCatalogData
set_option maxRecDepth 100000
set_option maxHeartbeats 0

def numericalChoice : Case → (Fin 234 ⊕ Fin 9) := ![Sum.inl 0,Sum.inl 1,Sum.inl 2,Sum.inl 3,Sum.inl 4,Sum.inl 5,Sum.inl 6,Sum.inl 7,Sum.inr 0,Sum.inl 8,Sum.inl 9,Sum.inl 10,Sum.inr 1,Sum.inl 11,Sum.inl 12,Sum.inr 2,Sum.inl 13,Sum.inl 14,Sum.inl 15,Sum.inl 16,Sum.inl 17,Sum.inl 18,Sum.inl 19,Sum.inl 20,Sum.inl 21,Sum.inl 22,Sum.inl 23,Sum.inl 24,Sum.inl 25,Sum.inl 26,Sum.inl 27,Sum.inl 28,Sum.inl 29,Sum.inl 30,Sum.inl 31,Sum.inl 32,Sum.inl 33,Sum.inl 34,Sum.inl 35,Sum.inr 3,Sum.inl 36,Sum.inl 37,Sum.inl 38,Sum.inl 39,Sum.inl 40,Sum.inl 41,Sum.inl 42,Sum.inl 43,Sum.inl 44,Sum.inl 45,Sum.inl 46,Sum.inl 47,Sum.inr 4,Sum.inl 48,Sum.inl 49,Sum.inl 50,Sum.inl 51,Sum.inl 52,Sum.inl 53,Sum.inl 54,Sum.inl 55,Sum.inl 56,Sum.inl 57,Sum.inl 58,Sum.inl 59,Sum.inl 60,Sum.inl 61,Sum.inl 62,Sum.inl 63,Sum.inl 64,Sum.inl 65,Sum.inl 66,Sum.inl 67,Sum.inl 68,Sum.inl 69,Sum.inl 70,Sum.inl 71,Sum.inl 72,Sum.inl 73,Sum.inl 74,Sum.inl 75,Sum.inl 76,Sum.inl 77,Sum.inl 78,Sum.inl 79,Sum.inl 80,Sum.inr 5,Sum.inl 81,Sum.inl 82,Sum.inl 83,Sum.inl 84,Sum.inl 85,Sum.inl 86,Sum.inl 87,Sum.inl 88,Sum.inr 6,Sum.inl 89,Sum.inl 90,Sum.inl 91,Sum.inl 92,Sum.inl 93,Sum.inl 94,Sum.inl 95,Sum.inl 96,Sum.inl 97,Sum.inl 98,Sum.inl 99,Sum.inl 100,Sum.inl 101,Sum.inl 102,Sum.inl 103,Sum.inl 104,Sum.inl 105,Sum.inl 106,Sum.inl 107,Sum.inl 108,Sum.inl 109,Sum.inl 110,Sum.inl 111,Sum.inl 112,Sum.inl 113,Sum.inl 114,Sum.inl 115,Sum.inl 116,Sum.inl 117,Sum.inl 118,Sum.inl 119,Sum.inl 120,Sum.inl 121,Sum.inl 122,Sum.inl 123,Sum.inl 124,Sum.inl 125,Sum.inl 126,Sum.inl 127,Sum.inl 128,Sum.inl 129,Sum.inl 130,Sum.inl 131,Sum.inl 132,Sum.inl 133,Sum.inl 134,Sum.inl 135,Sum.inl 136,Sum.inl 137,Sum.inl 138,Sum.inl 139,Sum.inl 140,Sum.inl 141,Sum.inl 142,Sum.inl 143,Sum.inl 144,Sum.inl 145,Sum.inl 146,Sum.inl 147,Sum.inl 148,Sum.inl 149,Sum.inl 150,Sum.inl 151,Sum.inl 152,Sum.inl 153,Sum.inl 154,Sum.inl 155,Sum.inl 156,Sum.inl 157,Sum.inl 158,Sum.inl 159,Sum.inl 160,Sum.inl 161,Sum.inl 162,Sum.inl 163,Sum.inl 164,Sum.inl 165,Sum.inl 166,Sum.inl 167,Sum.inl 168,Sum.inl 169,Sum.inl 170,Sum.inl 171,Sum.inl 172,Sum.inl 173,Sum.inl 174,Sum.inl 175,Sum.inl 176,Sum.inl 177,Sum.inl 178,Sum.inl 179,Sum.inl 180,Sum.inl 181,Sum.inl 182,Sum.inl 183,Sum.inl 184,Sum.inl 185,Sum.inl 186,Sum.inl 187,Sum.inl 188,Sum.inl 189,Sum.inl 190,Sum.inl 191,Sum.inl 192,Sum.inl 193,Sum.inl 194,Sum.inl 195,Sum.inl 196,Sum.inl 197,Sum.inl 198,Sum.inl 199,Sum.inl 200,Sum.inl 201,Sum.inl 202,Sum.inl 203,Sum.inl 204,Sum.inr 7,Sum.inl 205,Sum.inl 206,Sum.inl 207,Sum.inl 208,Sum.inl 209,Sum.inl 210,Sum.inl 211,Sum.inl 212,Sum.inl 213,Sum.inl 214,Sum.inl 215,Sum.inl 216,Sum.inl 217,Sum.inl 218,Sum.inl 219,Sum.inl 220,Sum.inl 221,Sum.inl 222,Sum.inl 223,Sum.inl 224,Sum.inr 8,Sum.inl 225,Sum.inl 226,Sum.inl 227,Sum.inl 228,Sum.inl 229,Sum.inl 230,Sum.inl 231,Sum.inl 232,Sum.inl 233]

theorem counts_match : ∀ c : Case, ∀ T : Finset (Fin 6),
    counts c T = match numericalChoice c with
      | Sum.inl k => TwentyThreeLowUnitSixBare.counts k T
      | Sum.inr k => TwentyThreeLowUnitSixDualData.counts k T := by
  intro c
  fin_cases c <;> decide +kernel

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 6 ↪ Fin 23) (c : Case)
    (actual : ∀ T, count H vertices T = counts c T) : PropertyB H := by
  cases hc : numericalChoice c with
  | inl k =>
    apply TwentyThreeLowUnitSixBare.propertyB_of_counts H vertices k
    intro T
    rw [actual,counts_match,hc]
  | inr k =>
    apply TwentyThreeLowUnitSixDual.propertyB_of_counts H vertices k
    intro T
    rw [actual,counts_match,hc]

end Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCounts
#print axioms Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCounts.propertyB_of_counts
