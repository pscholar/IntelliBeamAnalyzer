from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(200,400)
A = get_rect_section_area(200,400)
beam = Beam(4, E, I=I, A=A)
beam.add_supports(Support(0,(1,1,1)))
beam.add_loads(PointLoadV(-30000,4))
analyzer(beam)
