from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E=material('timber')
I=get_rect_section_inertia(120,250)
A=get_rect_section_area(120,250)
beam=Beam(4.5, E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 1)), Support(4.5, (1, 1, 1)))
beam.add_loads(PointLoadV(-7000, 2.7))
analyzer(beam)
