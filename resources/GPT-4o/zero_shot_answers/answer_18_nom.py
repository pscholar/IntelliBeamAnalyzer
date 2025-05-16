
from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)

beam = Beam(5, E, I, A)
support1 = Support(0, (1, 1, 0))
support2 = Support(5, (1, 1, 0))
beam.add_supports(support1, support2)

load1 = PointLoadV(-15000, 2)
load2 = PointLoadV(-10000, 4)
beam.add_loads(load1, load2)

analyzer(beam)

