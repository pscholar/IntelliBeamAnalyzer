from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)

beam = Beam(21, E, I, A)

s1 = Support(0, (1, 1, 0))
s2 = Support(6, (0, 1, 0))
s3 = Support(14, (0, 1, 0))
s4 = Support(21, (0, 1, 0))

beam.add_supports(s1, s2, s3, s4)

l1 = UDLV(-9e3, (0, 6))
l2 = PointTorque(-35e3, 10)
l3 = PointLoadV(-15e3, 19)

beam.add_loads(l1, l2, l3)

analyzer(beam)
