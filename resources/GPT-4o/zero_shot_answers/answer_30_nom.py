from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300, 500)
A = get_rect_section_area(300, 500)

beam = Beam(9, E, I, A)
support1 = Support(0, (1, 1, 0))
support2 = Support(9, (1, 1, 0))
beam.add_supports(support1, support2)

load1 = PointLoadV(-10000, 2)
load2 = PointLoadV(-10000, 7)
load3 = UDLV(-4000, (3, 6))
beam.add_loads(load1, load2, load3)

analyzer(beam)
