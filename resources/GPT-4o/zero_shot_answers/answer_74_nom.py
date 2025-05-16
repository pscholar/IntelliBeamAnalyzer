from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)

beam = Beam(4 + 5 + 6, E, I, A)

s1 = Support(0, (1, 1, 1))
s2 = Support(4, (1, 1, 1))
s3 = Support(9, (1, 1, 1))
s4 = Support(15, (1, 1, 1))

beam.add_supports(s1, s2, s3, s4)

l1 = UDLV(-20e3, (0, 4))
l2 = UDLV(-20e3, (4, 9))
l3 = UDLV(-20e3, (9, 15))

beam.add_loads(l1, l2, l3)

analyzer(beam)
