from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer

beam = Beam(4)
beam.add_supports(Support(0, (1,1,1)))
beam.add_loads(UDLV(-3000, (0,4)), PointLoadV(-8000, 4))
analyzer(beam)
