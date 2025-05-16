from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(150, 350)
A = get_rect_section_area(150, 350)

beam = Beam(12, E, I, A)

s1 = Support(0, (1, 1, 1))
s2 = Support(12, (1, 1, 1))

beam.add_supports(s1, s2)

l1 = PointLoadV(-20e3, 4)
l2 = PointLoadV(-15e3, 9)

beam.add_loads(l1, l2)

analyzer(beam)
