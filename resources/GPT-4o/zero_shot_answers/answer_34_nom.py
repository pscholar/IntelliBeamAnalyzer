from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(180, 280)
A = get_rect_section_area(180, 280)

beam = Beam(12, E, I, A)
support1 = Support(0, (1, 1, 1))
support2 = Support(8, (0, 1, 0))
support3 = Support(12, (1, 1, 1))
beam.add_supports(support1, support2, support3)

load1 = UDLV(-4000, (0, 12))
beam.add_loads(load1)

analyzer(beam)

