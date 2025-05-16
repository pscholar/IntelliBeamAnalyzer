from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300,600)
A = get_rect_section_area(300,600)
beam = Beam(12, E, I=I, A=A)
beam.add_supports(Support(0,(1,1,0)), Support(5,(0,1,0)), Support(12,(0,1,0)))
beam.add_loads(UDLV(-12000,(0,5)), UDLV(-18000,(0,5)), PointLoadV(-45000,8))
analyzer(beam)
