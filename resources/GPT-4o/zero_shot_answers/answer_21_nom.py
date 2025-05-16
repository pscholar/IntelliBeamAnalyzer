from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(300, 300)
A = get_rect_section_area(300, 300)

beam = Beam(6, E, I, A)
support1 = Support(0, (1, 1, 1))
beam.add_supports(support1)

load1 = PointLoadV(-10000, 6)
load2 = UDLV(-4000, (2, 5))
beam.add_loads(load1, load2)

analyzer(beam)
