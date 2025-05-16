from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(220, 350)
A = get_rect_section_area(220, 350)

beam = Beam(15, E, I, A)
beam.add_supports(Support(0, (1, 1, 0)), Support(4, (1, 1, 0)), Support(10, (1, 1, 0)), Support(15, (1, 1, 0)))
beam.add_loads(UDLV(-3000, (0, 4)), PointLoadV(-25000, 7), UDLV(-3000, (10, 15)))
analyzer(beam)
