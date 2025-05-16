from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(150, 300)
A = get_rect_section_area(150, 300)
beam = Beam(15, E=E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 1)), Support(6, (1, 1, 1)), Support(15, (1, 1, 1)))
beam.add_loads(PointLoadV(-22000, 4), UDLV(-8000, (6, 15)))
analyzer(beam)
