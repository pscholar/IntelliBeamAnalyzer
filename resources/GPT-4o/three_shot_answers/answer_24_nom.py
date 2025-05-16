from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300, 500)
A = get_rect_section_area(300, 500)
beam = Beam(10, E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 1)), Support(10, (1, 1, 1)))
beam.add_loads(PointLoadV(-25000, 4), UDLV(-3000, (5, 10)))
analyzer(beam)
