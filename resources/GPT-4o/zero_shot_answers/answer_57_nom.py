from indeterminatebeam.loading import UDLV, PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(250, 500)
A = get_rect_section_area(250, 500)

beam = Beam(15, E, I, A)

s1 = Support(0, (1, 1, 1))
s2 = Support(15, (0, 1, 0))

beam.add_supports(s1, s2)

l1 = UDLV(-10e3, (0, 5))
l2 = PointTorque(-50e3, 10)

beam.add_loads(l1, l2)

analyzer(beam)
