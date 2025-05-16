from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E=material('steel')
I=get_rect_section_inertia(200,350)
A=get_rect_section_area(200,350)
beam=Beam(5,E,I,A)
s=Support(0,(1,1,1))
beam.add_supports(s)
load=UDLV(-3000,(0,5))
beam.add_loads(load)
analyzer(beam)
