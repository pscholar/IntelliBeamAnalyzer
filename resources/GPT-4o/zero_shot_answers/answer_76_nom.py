from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)

beam = Beam(10, E, I, A)

s1 = Support(0, (1, 1, 0))
s2 = Support(10, (0, 1, 0))

beam.add_supports(s1, s2)

l1 = UDLV(-15e3, (0, 10))
l2 = PointLoadV(-50e3, 5)

beam.add_loads(l1, l2)

analyzer(beam)
