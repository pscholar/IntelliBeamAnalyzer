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
support1 = Support(0, (1, 1, 0))
support2 = Support(4, (1, 1, 0))
support3 = Support(10, (1, 1, 0))
support4 = Support(15, (1, 1, 0))
beam.add_supports(support1, support2, support3, support4)

load1 = UDLV(-3000, (0, 4))
load2 = UDLV(-3000, (4, 10))
load3 = UDLV(-3000, (10, 15))
load4 = PointLoadV(-25000, 7)
beam.add_loads(load1, load2, load3, load4)

analyzer(beam)

