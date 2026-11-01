import Aris4Math.ThirtyFour.TwentyOneSevenManyActualCore
import Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogueKernel
namespace Aris4Math.ThirtyFour.TwentyOneSevenManyActual
/-- The complete catalogue theorem is supplied internally, with no local
certificate premise left on the actual five-vertex statement. -/
theorem propertyB_of_five_sevens (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34) (f : Fin 5↪Fin 21)
    (degrees : ∀i,H.degree (f i)=7) : PropertyB H :=
  TwentyOneSevenManyActualCore.propertyB_of_five_sevens H cover size f degrees
    TwentyOneSevenManyCatalogue.coverage
end Aris4Math.ThirtyFour.TwentyOneSevenManyActual
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenManyActual.propertyB_of_five_sevens
