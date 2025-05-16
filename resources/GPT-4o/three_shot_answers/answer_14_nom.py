from indeterminatebeam.loading import PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material

E=material('steel')
beam=Beam(5,E)
beam.add_supports(Support(0,(1,1,1)))
beam.add_loads(PointTorque(-15000, 3))
analyzer(beam)
