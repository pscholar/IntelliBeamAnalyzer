from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300, 500)
A = get_rect_section_area(300, 500)
beam = Beam(18, E, I, A)
beam.add_supports(Support(0, (1, 1, 0)), Support(5, (0, 1, 0)), Support(12, (0, 1, 0)), Support(18, (1, 1, 0)))
beam.add_loads(UDLV(-25000, (0, 5)))
beam.add_loads(UDLV(-25000, (5, 12)))
beam.add_loads(UDLV(-25000, (12, 18)))
analyzer(beam)
