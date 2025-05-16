from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300, 500)
A = get_rect_section_area(300, 500)

beam = Beam(9, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(9, (1, 1, 1)))
beam.add_loads(PointLoadV(-10000, 2), PointLoadV(-10000, 7), UDLV(-4000, (3, 6)))
analyzer(beam)
