from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300, 600)
A = get_rect_section_area(300, 600)

beam = Beam(12, E, I, A)

s1 = Support(0, (1, 1, 0))
s2 = Support(12, (0, 1, 0))
s3 = Support(5, (0, 1, 0))

beam.add_supports(s1, s2, s3)

l1 = UDLV(-12e3, (0, 5))
l2 = UDLV(-18e3, (5, 12))
l3 = PointLoadV(-45e3, 8)

beam.add_loads(l1, l2, l3)

analyzer(beam)
