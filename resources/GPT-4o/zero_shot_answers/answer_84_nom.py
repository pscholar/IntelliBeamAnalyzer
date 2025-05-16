from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(225, 475)
A = get_rect_section_area(225, 475)

beam = Beam(9, E, I, A)

s1 = Support(0, (1, 1, 1))
s2 = Support(9, (1, 1, 1))

beam.add_supports(s1, s2)

l1 = PointLoadV(-18e3, 3)
l2 = PointLoadV(-25e3, 6)

beam.add_loads(l1, l2)

analyzer(beam)
