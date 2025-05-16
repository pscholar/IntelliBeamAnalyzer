from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(120,250)
A = get_rect_section_area(120,250)
beam = Beam(4,E,I=I,A=A)
beam.add_supports(Support(0,(1,1,0)),Support(4,(0,1,0)))
beam.add_loads(UDLV(-2000,(0,4)))
analyzer(beam)
