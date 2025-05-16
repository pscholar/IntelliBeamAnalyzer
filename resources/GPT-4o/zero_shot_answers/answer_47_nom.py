from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(250, 500)
A = get_rect_section_area(250, 500)

beam = Beam(5 + 7 + 6, E, I, A)

s1 = Support(0, (1, 1, 1))
s2 = Support(5, (1, 1, 0))
s3 = Support(12, (1, 1, 0))
s4 = Support(18, (0, 1, 0))

beam.add_supports(s1, s2, s3, s4)

l1 = UDLV(-8e3, (0, 5))
l2 = PointLoadV(-25e3, 8)
l3 = UDLV(-6e3, (12, 18))

beam.add_loads(l1, l2, l3)

analyzer(beam)
