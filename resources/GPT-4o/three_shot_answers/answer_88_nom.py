from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(175,350)
A = get_rect_section_area(175,350)
beam = Beam(10, E, I=I, A=A)
beam.add_supports(Support(0,(1,1,0)), Support(4,(0,1,0)), Support(10,(0,1,0)))
beam.add_loads(UDLV(-7000,(0,4)), PointLoadV(-20000,6))
analyzer(beam)
