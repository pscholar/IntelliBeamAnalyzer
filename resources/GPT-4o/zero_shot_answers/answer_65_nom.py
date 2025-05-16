from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)

beam = Beam(12, E, I, A)

s1 = Support(0, (0, 1, 0))
s2 = Support(12, (0, 1, 0))
s3 = Support(6, (1, 1, 1))

beam.add_supports(s1, s2, s3)

l1 = UDLV(-15e3, (0, 12))

beam.add_loads(l1)

analyzer(beam)
