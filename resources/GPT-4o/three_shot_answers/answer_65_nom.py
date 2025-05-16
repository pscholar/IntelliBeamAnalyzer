from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)
beam = Beam(12, E=E, I=I, A=A)
beam.add_supports(Support(0, (0, 1, 0)), Support(12, (0, 1, 0)), Support(6, (1, 1, 1)))
beam.add_loads(UDLV(-15000, (0, 12)))
analyzer(beam)
