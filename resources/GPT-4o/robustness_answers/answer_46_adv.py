from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)
beam = Beam(14, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(6, (1, 1, 0)), Support(14, (1, 1, 1)))
beam.add_loads(UDLV(-10000, (0, 6)), PointLoadV(-30000, 10))
analyzer(beam)
