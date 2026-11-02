import DegreeDiameter.Portfolio.F5Graph3750RouteData

namespace DegreeDiameter.Portfolio.F5Graph3750
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

theorem nb_decoder_word_0 : ∀ (d : Fin 125),
    routeFiber 0 0 0 (nbNoiseDecoder 0 d) 0 = d := by decide +kernel

theorem nb_decoder_word_2 : ∀ (d : Fin 125),
    routeFiber 2 0 0 (nbNoiseDecoder 2 d) 0 = d := by decide +kernel

theorem nb_decoder_word_3 : ∀ (d : Fin 125),
    routeFiber 3 0 0 (nbNoiseDecoder 3 d) 0 = d := by decide +kernel

theorem nb_decoder_word_8 : ∀ (d : Fin 125),
    routeFiber 0 2 0 (nbNoiseDecoder 8 d) 0 = d := by decide +kernel

theorem nb_decoder_word_9 : ∀ (d : Fin 125),
    routeFiber 1 2 0 (nbNoiseDecoder 9 d) 0 = d := by decide +kernel

theorem nb_decoder_word_10 : ∀ (d : Fin 125),
    routeFiber 2 2 0 (nbNoiseDecoder 10 d) 0 = d := by decide +kernel

theorem nb_decoder_word_12 : ∀ (d : Fin 125),
    routeFiber 0 3 0 (nbNoiseDecoder 12 d) 0 = d := by decide +kernel

theorem nb_decoder_word_13 : ∀ (d : Fin 125),
    routeFiber 1 3 0 (nbNoiseDecoder 13 d) 0 = d := by decide +kernel

theorem nb_decoder_word_15 : ∀ (d : Fin 125),
    routeFiber 3 3 0 (nbNoiseDecoder 15 d) 0 = d := by decide +kernel

theorem nb_decoder_word_21 : ∀ (d : Fin 125),
    routeFiber 1 1 1 (nbNoiseDecoder 21 d) 0 = d := by decide +kernel

theorem nb_decoder_word_22 : ∀ (d : Fin 125),
    routeFiber 2 1 1 (nbNoiseDecoder 22 d) 0 = d := by decide +kernel

theorem nb_decoder_word_23 : ∀ (d : Fin 125),
    routeFiber 3 1 1 (nbNoiseDecoder 23 d) 0 = d := by decide +kernel

theorem nb_decoder_word_24 : ∀ (d : Fin 125),
    routeFiber 0 2 1 (nbNoiseDecoder 24 d) 0 = d := by decide +kernel

theorem nb_decoder_word_25 : ∀ (d : Fin 125),
    routeFiber 1 2 1 (nbNoiseDecoder 25 d) 0 = d := by decide +kernel

theorem nb_decoder_word_26 : ∀ (d : Fin 125),
    routeFiber 2 2 1 (nbNoiseDecoder 26 d) 0 = d := by decide +kernel

theorem nb_decoder_word_28 : ∀ (d : Fin 125),
    routeFiber 0 3 1 (nbNoiseDecoder 28 d) 0 = d := by decide +kernel

theorem nb_decoder_word_29 : ∀ (d : Fin 125),
    routeFiber 1 3 1 (nbNoiseDecoder 29 d) 0 = d := by decide +kernel

theorem nb_decoder_word_31 : ∀ (d : Fin 125),
    routeFiber 3 3 1 (nbNoiseDecoder 31 d) 0 = d := by decide +kernel

theorem nb_decoder_word_32 : ∀ (d : Fin 125),
    routeFiber 0 0 2 (nbNoiseDecoder 32 d) 0 = d := by decide +kernel

theorem nb_decoder_word_34 : ∀ (d : Fin 125),
    routeFiber 2 0 2 (nbNoiseDecoder 34 d) 0 = d := by decide +kernel

theorem nb_decoder_word_35 : ∀ (d : Fin 125),
    routeFiber 3 0 2 (nbNoiseDecoder 35 d) 0 = d := by decide +kernel

theorem nb_decoder_word_37 : ∀ (d : Fin 125),
    routeFiber 1 1 2 (nbNoiseDecoder 37 d) 0 = d := by decide +kernel

theorem nb_decoder_word_38 : ∀ (d : Fin 125),
    routeFiber 2 1 2 (nbNoiseDecoder 38 d) 0 = d := by decide +kernel

theorem nb_decoder_word_39 : ∀ (d : Fin 125),
    routeFiber 3 1 2 (nbNoiseDecoder 39 d) 0 = d := by decide +kernel

theorem nb_decoder_word_40 : ∀ (d : Fin 125),
    routeFiber 0 2 2 (nbNoiseDecoder 40 d) 0 = d := by decide +kernel

theorem nb_decoder_word_41 : ∀ (d : Fin 125),
    routeFiber 1 2 2 (nbNoiseDecoder 41 d) 0 = d := by decide +kernel

theorem nb_decoder_word_42 : ∀ (d : Fin 125),
    routeFiber 2 2 2 (nbNoiseDecoder 42 d) 0 = d := by decide +kernel

theorem nb_decoder_word_48 : ∀ (d : Fin 125),
    routeFiber 0 0 3 (nbNoiseDecoder 48 d) 0 = d := by decide +kernel

theorem nb_decoder_word_50 : ∀ (d : Fin 125),
    routeFiber 2 0 3 (nbNoiseDecoder 50 d) 0 = d := by decide +kernel

theorem nb_decoder_word_51 : ∀ (d : Fin 125),
    routeFiber 3 0 3 (nbNoiseDecoder 51 d) 0 = d := by decide +kernel

theorem nb_decoder_word_53 : ∀ (d : Fin 125),
    routeFiber 1 1 3 (nbNoiseDecoder 53 d) 0 = d := by decide +kernel

theorem nb_decoder_word_54 : ∀ (d : Fin 125),
    routeFiber 2 1 3 (nbNoiseDecoder 54 d) 0 = d := by decide +kernel

theorem nb_decoder_word_55 : ∀ (d : Fin 125),
    routeFiber 3 1 3 (nbNoiseDecoder 55 d) 0 = d := by decide +kernel

theorem nb_decoder_word_60 : ∀ (d : Fin 125),
    routeFiber 0 3 3 (nbNoiseDecoder 60 d) 0 = d := by decide +kernel

theorem nb_decoder_word_61 : ∀ (d : Fin 125),
    routeFiber 1 3 3 (nbNoiseDecoder 61 d) 0 = d := by decide +kernel

theorem nb_decoder_word_63 : ∀ (d : Fin 125),
    routeFiber 3 3 3 (nbNoiseDecoder 63 d) 0 = d := by decide +kernel

theorem nb_decoder_valid : ∀ (w : Fin 64) (d : Fin 125), NBWord w →
    routeFiber (wordP0 w) (wordP1 w) (wordP2 w) (nbNoiseDecoder w d) 0 = d := by
  intro w d h
  fin_cases w
  · exact nb_decoder_word_0 d
  · exact False.elim ((by decide : ¬ NBWord (1 : Fin 64)) h)
  · exact nb_decoder_word_2 d
  · exact nb_decoder_word_3 d
  · exact False.elim ((by decide : ¬ NBWord (4 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (5 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (6 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (7 : Fin 64)) h)
  · exact nb_decoder_word_8 d
  · exact nb_decoder_word_9 d
  · exact nb_decoder_word_10 d
  · exact False.elim ((by decide : ¬ NBWord (11 : Fin 64)) h)
  · exact nb_decoder_word_12 d
  · exact nb_decoder_word_13 d
  · exact False.elim ((by decide : ¬ NBWord (14 : Fin 64)) h)
  · exact nb_decoder_word_15 d
  · exact False.elim ((by decide : ¬ NBWord (16 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (17 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (18 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (19 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (20 : Fin 64)) h)
  · exact nb_decoder_word_21 d
  · exact nb_decoder_word_22 d
  · exact nb_decoder_word_23 d
  · exact nb_decoder_word_24 d
  · exact nb_decoder_word_25 d
  · exact nb_decoder_word_26 d
  · exact False.elim ((by decide : ¬ NBWord (27 : Fin 64)) h)
  · exact nb_decoder_word_28 d
  · exact nb_decoder_word_29 d
  · exact False.elim ((by decide : ¬ NBWord (30 : Fin 64)) h)
  · exact nb_decoder_word_31 d
  · exact nb_decoder_word_32 d
  · exact False.elim ((by decide : ¬ NBWord (33 : Fin 64)) h)
  · exact nb_decoder_word_34 d
  · exact nb_decoder_word_35 d
  · exact False.elim ((by decide : ¬ NBWord (36 : Fin 64)) h)
  · exact nb_decoder_word_37 d
  · exact nb_decoder_word_38 d
  · exact nb_decoder_word_39 d
  · exact nb_decoder_word_40 d
  · exact nb_decoder_word_41 d
  · exact nb_decoder_word_42 d
  · exact False.elim ((by decide : ¬ NBWord (43 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (44 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (45 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (46 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (47 : Fin 64)) h)
  · exact nb_decoder_word_48 d
  · exact False.elim ((by decide : ¬ NBWord (49 : Fin 64)) h)
  · exact nb_decoder_word_50 d
  · exact nb_decoder_word_51 d
  · exact False.elim ((by decide : ¬ NBWord (52 : Fin 64)) h)
  · exact nb_decoder_word_53 d
  · exact nb_decoder_word_54 d
  · exact nb_decoder_word_55 d
  · exact False.elim ((by decide : ¬ NBWord (56 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (57 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (58 : Fin 64)) h)
  · exact False.elim ((by decide : ¬ NBWord (59 : Fin 64)) h)
  · exact nb_decoder_word_60 d
  · exact nb_decoder_word_61 d
  · exact False.elim ((by decide : ¬ NBWord (62 : Fin 64)) h)
  · exact nb_decoder_word_63 d

#print axioms nb_decoder_valid
end DegreeDiameter.Portfolio.F5Graph3750
