from indeterminatebeam.loading import PointLoadV, UDLV, PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(250, 500)
A = get_rect_section_area(250, 500)

beam = Beam(18, E, I, A)

s1 = Support(0, (1, 1, 0))
s2 = Support(5, (1, 1, 0))
s3 = Support(11, (1, 1, 0))
s4 = Support(18, (0, 1, 0))

beam.add_supports(s1, s2, s3, s4)

l1 = PointLoadV(-18e3, 3)
l2 = UDLV(-10e3, (5, 11))
l3 = PointTorque(40e3, 14.5)

beam.add_loads(l1, l2, l3)

analyzer(beam)
