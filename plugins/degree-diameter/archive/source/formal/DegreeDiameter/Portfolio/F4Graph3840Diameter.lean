import DegreeDiameter.Portfolio.F4Graph3840Certificates
import DegreeDiameter.Portfolio.F4Graph3840DiameterInterface
namespace DegreeDiameter.Portfolio.F4Graph3840

theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  diameter_of_local_decoders controller_valid nb_noise_valid adjacent_valid

#print axioms diameterAtMost_three
end DegreeDiameter.Portfolio.F4Graph3840
