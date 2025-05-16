from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(175, 350)
A = get_rect_section_area(175, 350)

beam = Beam(4 + 6, E, I, A)

s1 = Support(0, (1, 1, 1))
s2 = Support(4, (0, 1, 0))
s3 = Support(10, (0, 1, 0))

beam.add_supports(s1, s2, s3)

l1 = UDLV(-7e3, (0, 4))
l2 = PointLoadV(-20e3, 6)

beam.add_loads(l1, l2)

analyzer(beam)
