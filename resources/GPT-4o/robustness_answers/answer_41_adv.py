from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(120, 180)
A = get_rect_section_area(120, 180)

beam = Beam(10, E, I, A)
beam.add_supports(Support(0, (0, 1, 0)), Support(4, (0, 1, 0)), Support(10, (1, 1, 1)))
beam.add_loads(UDLV(-2000, (0, 10)), PointLoadV(-15000, 3))
analyzer(beam)
