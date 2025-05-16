from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(150, 250)
A = get_rect_section_area(150, 250)

beam = Beam(10, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(10, (1, 1, 1)))
beam.add_loads(UDLV(-5000, (0, 10)))
analyzer(beam)
