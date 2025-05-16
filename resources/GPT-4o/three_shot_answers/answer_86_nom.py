from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(150,300)
A = get_rect_section_area(150,300)
beam = Beam(5, E, I=I, A=A)
beam.add_supports(Support(0,(1,1,0)), Support(5,(0,1,0)))
beam.add_loads(UDLV(-8000,(0,5)))
analyzer(beam)
