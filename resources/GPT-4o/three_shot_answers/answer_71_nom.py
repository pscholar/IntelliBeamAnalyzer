from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(250,400)
A = get_rect_section_area(250,400)
beam = Beam(15, E, I=I, A=A)
beam.add_supports(Support(0,(0,1,0)), Support(7.5,(1,1,1)), Support(15,(0,1,0)))
beam.add_loads(UDLV(-18000,(0,15)))
analyzer(beam)
