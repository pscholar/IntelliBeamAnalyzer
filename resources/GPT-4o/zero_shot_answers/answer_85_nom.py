from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(350, 350)
A = get_rect_section_area(350, 350)

beam = Beam(8, E, I, A)

s1 = Support(0, (1, 1, 0))
s2 = Support(8, (0, 1, 0))

beam.add_supports(s1, s2)

l1 = UDLV(-14e3, (0, 8))
l2 = UDLV(-20e3, (0, 8))
l3 = PointLoadV(-30e3, 4)

beam.add_loads(l1, l2, l3)

analyzer(beam)
