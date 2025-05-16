from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(400, 600)
A = get_rect_section_area(400, 600)

beam = Beam(14, E, I, A)
support1 = Support(0, (1, 1, 1))
support2 = Support(8, (1, 1, 0))
support3 = Support(14, (0, 1, 0))
beam.add_supports(support1, support2, support3)

load1 = UDLV(-5000, (0, 8))
load2 = UDLV(-5000, (8, 14))
beam.add_loads(load1, load2)

analyzer(beam)

