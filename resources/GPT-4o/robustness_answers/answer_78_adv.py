from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(250, 450)
A = get_rect_section_area(250, 450)
beam = Beam(8 + 6, E, I, A)
beam.add_supports(Support(0, (1, 1, 0)), Support(8, (0, 1, 0)), Support(14, (1, 1, 0)))
beam.add_loads(PointLoadV(-30000, 3), UDLV(-10000, (8, 14)))
analyzer(beam)
