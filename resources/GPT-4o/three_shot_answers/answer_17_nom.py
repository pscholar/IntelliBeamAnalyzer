from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E=material('timber')
I=get_rect_section_inertia(225,225)
A=get_rect_section_area(225,225)
beam=Beam(4, E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 1)))
beam.add_loads(UDLV(-3000, (0, 4)), PointLoadV(-8000, 4))
analyzer(beam)
