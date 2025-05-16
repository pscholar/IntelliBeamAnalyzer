from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)
beam = Beam(4 + 5 + 6, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(4, (1, 1, 1)), Support(9, (1, 1, 1)))
beam.add_loads(UDLV(-20000, (0, 4)), UDLV(-20000, (4, 9)), UDLV(-20000, (9, 15)))
analyzer(beam)
