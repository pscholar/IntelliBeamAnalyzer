from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(250, 350)
A = get_rect_section_area(250, 350)
beam = Beam(24, E=E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 0)), Support(8, (1, 1, 0)), Support(16, (1, 1, 0)), Support(24, (1, 1, 0)))
beam.add_loads(UDLV(-5000, (0, 8)), PointLoadV(-20000, 4), UDLV(-5000, (8, 16)), PointLoadV(-20000, 12), UDLV(-5000, (16, 24)))
analyzer(beam)
