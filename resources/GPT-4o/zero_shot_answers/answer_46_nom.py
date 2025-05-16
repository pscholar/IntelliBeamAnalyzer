from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)

beam = Beam(6 + 8, E, I, A)

support1 = Support(0, (1, 1, 1))
support2 = Support(6, (1, 1, 0))
support3 = Support(14, (0, 1, 0))

beam.add_supports(support1, support2, support3)

load1 = UDLV(-10e3, (0, 6))
load2 = PointLoadV(-30e3, 10)

beam.add_loads(load1, load2)

analyzer(beam)
