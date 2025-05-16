from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(125, 275)
A = get_rect_section_area(125, 275)

beam = Beam(7, E, I, A)

s1 = Support(0, (1, 1, 1))
s2 = Support(7, (1, 1, 1))

beam.add_supports(s1, s2)

l1 = PointLoadV(-10e3, 2)
l2 = PointLoadV(-14e3, 5)

beam.add_loads(l1, l2)

analyzer(beam)
