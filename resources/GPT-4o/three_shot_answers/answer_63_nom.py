from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(150, 300)
A = get_rect_section_area(150, 300)
beam = Beam(6, E=E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 1)))
beam.add_loads(PointLoadV(-20000, 6))
analyzer(beam)
