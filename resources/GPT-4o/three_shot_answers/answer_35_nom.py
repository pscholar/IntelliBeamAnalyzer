from indeterminatebeam.loading import UDLV, PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(120, 200)
A = get_rect_section_area(120, 200)
beam = Beam(14, E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 1)), Support(7, (1, 1, 0)), Support(14, (0, 1, 0)))
beam.add_loads(UDLV(-6000, (0, 7)), PointLoadV(-15000, 10))
analyzer(beam)
