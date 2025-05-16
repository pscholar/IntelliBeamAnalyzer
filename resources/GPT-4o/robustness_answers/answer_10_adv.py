from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(120, 250)
A = get_rect_section_area(120, 250)

beam = Beam(3, E, I, A)

s1 = Support(0, (1, 1, 1))
s2 = Support(3, (0, 1, 0))

beam.add_supports(s1, s2)

l1 = UDLV(-5e3, (1.5, 3))

beam.add_loads(l1)

analyzer(beam)
