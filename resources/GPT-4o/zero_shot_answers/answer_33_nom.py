from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300, 500)
A = get_rect_section_area(300, 500)

beam = Beam(10, E, I, A)
support1 = Support(0, (1, 1, 1))
support2 = Support(6, (1, 1, 1))
support3 = Support(6, (0, 1, 0))
beam.add_supports(support1, support2, support3)

load1 = UDLV(-3000, (6, 10))
beam.add_loads(load1)

analyzer(beam)
