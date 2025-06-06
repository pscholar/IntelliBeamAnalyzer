from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(125,275)
A = get_rect_section_area(125,275)
beam = Beam(7,E,I=I,A=A)
beam.add_supports(Support(0,(1,1,1)),Support(7,(1,1,1)))
beam.add_loads(PointLoadV(-10000,2),PointLoadV(-14000,5))
analyzer(beam)
