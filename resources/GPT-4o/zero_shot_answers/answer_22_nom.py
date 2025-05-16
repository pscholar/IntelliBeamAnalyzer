from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(150, 300)
A = get_rect_section_area(150, 300)

beam = Beam(9, E, I, A)
support1 = Support(0, (1, 1, 0))
support2 = Support(9, (1, 1, 0))
beam.add_supports(support1, support2)

load1 = PointLoadV(-12000, 3)
load2 = PointLoadV(-18000, 6)
beam.add_loads(load1, load2)

analyzer(beam)
