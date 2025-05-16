from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E=material('steel')
I=get_rect_section_inertia(300,300)
A=get_rect_section_area(300,300)
beam=Beam(6, E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 1)))
beam.add_loads(PointLoadV(-10000, 6), UDLV(-4000, (2, 5)))
analyzer(beam)
