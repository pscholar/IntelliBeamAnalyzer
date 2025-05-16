from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(120, 200)
A = get_rect_section_area(120, 200)

beam = Beam(14, E, I, A)
support1 = Support(0, (1, 1, 1))
support2 = Support(7, (1, 1, 0))
support3 = Support(14, (0, 1, 0))
beam.add_supports(support1, support2, support3)

load1 = UDLV(-6000, (0, 7))
load2 = PointLoadV(-15000, 10)
beam.add_loads(load1, load2)

analyzer(beam)

