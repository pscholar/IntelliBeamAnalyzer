from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E=material('steel')
I=get_rect_section_inertia(120,250)
A=get_rect_section_area(120,250)
beam=Beam(3,E,I,A)
beam.add_supports(Support(0,(1,1,1)))
beam.add_loads(UDLV(-5000, (1.5, 3)))
analyzer(beam)
