from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(350,350)
A = get_rect_section_area(350,350)
beam = Beam(6, E, I=I, A=A)
beam.add_supports(Support(0,(1,1,0)), Support(6,(0,1,0)))
beam.add_loads(UDLV(-14000,(0,6)), UDLV(-20000,(0,6)), PointLoadV(-30000,3))
analyzer(beam)
