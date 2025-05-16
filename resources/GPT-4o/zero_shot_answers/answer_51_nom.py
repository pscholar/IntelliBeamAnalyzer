from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300, 500)
A = get_rect_section_area(300, 500)

beam = Beam(18, E, I, A)

s1 = Support(0, (1, 1, 0))
s2 = Support(8, (1, 1, 0))
s3 = Support(18, (0, 1, 0))

beam.add_supports(s1, s2, s3)

l1 = UDLV(-7e3, (0, 8))
l2 = PointLoadV(-30e3, 15)

beam.add_loads(l1, l2)

analyzer(beam)
