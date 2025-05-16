from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(250, 400)
A = get_rect_section_area(250, 400)
beam = Beam(18, E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 1)), Support(5, (1, 1, 0)), Support(12, (1, 1, 0)), Support(18, (1, 1, 1)))
beam.add_loads(UDLV(-4000, (0, 5)), UDLV(-6000, (5, 12)), UDLV(-3000, (12, 18)))
analyzer(beam)
