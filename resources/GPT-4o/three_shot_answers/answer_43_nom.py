from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(500, 800)
A = get_rect_section_area(500, 800)
beam = Beam(20, E=E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 0)), Support(12, (1, 1, 1)), Support(20, (1, 1, 0)))
beam.add_loads(UDLV(-10000, (0, 12)), PointLoadV(-50000, 16))
analyzer(beam)
