from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(250, 450)
A = get_rect_section_area(250, 450)

beam = Beam(8 + 6, E, I, A)

s1 = Support(0, (1, 1, 0))
s2 = Support(8, (0, 1, 0))
s3 = Support(8, (0, 1, 0))

beam.add_supports(s1, s2, s3)

l1 = PointLoadV(-30e3, 3)
l2 = UDLV(-10e3, (8, 14))

beam.add_loads(l1, l2)

analyzer(beam)
