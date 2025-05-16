from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)

beam = Beam(7 + 9, E, I, A)

s1 = Support(0, (1, 1, 0))
s2 = Support(7, (0, 1, 0))
s3 = Support(16, (1, 1, 0))

beam.add_supports(s1, s2, s3)

l1 = PointLoadV(-20e3, 4)
l2 = UDLV(-10e3, (7, 16))

beam.add_loads(l1, l2)

analyzer(beam)
