from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = 3.2e8 / 1e12
A = 600e-4
beam = Beam(20, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(12, (1, 1, 1)), Support(20, (1, 1, 1)))
beam.add_loads(UDLV(-10000, (12, 20)), PointLoadV(-50000, 4))
analyzer(beam)
