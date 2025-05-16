from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material

E = material('timber')
beam = Beam(5, E)
beam.add_supports(Support(0,(1,1,0)), Support(5,(0,1,0)))
beam.add_loads(UDLV(-8000,(0,5)))
analyzer(beam)
