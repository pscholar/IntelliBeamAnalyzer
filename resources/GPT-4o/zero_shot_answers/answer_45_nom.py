from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(150,220)
A = get_rect_section_area(150,220)
beam = Beam(20, E, I=I, A=A)
s1 = Support(0, (1,1,1))
s2 = Support(6, (1,1,0))
s3 = Support(14, (1,1,0))
s4 = Support(20, (1,1,1))
beam.add_supports(s1, s2, s3, s4)
l1 = UDLV(-5000, (0,20))
l2 = PointTorque(-25000, 10)
l3 = PointLoadV(-30000, 3)
beam.add_loads(l1, l2, l3)
analyzer(beam)
