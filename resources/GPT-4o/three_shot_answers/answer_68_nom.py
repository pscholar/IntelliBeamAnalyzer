from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)
beam = Beam(14, E=E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 1)), Support(14, (0, 1, 0)))
beam.add_loads(UDLV(-12000, (0, 14)))
analyzer(beam)
