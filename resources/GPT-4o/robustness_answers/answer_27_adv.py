from indeterminatebeam.loading import UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(150,300)
A = get_rect_section_area(150,300)
beam = Beam(6,E,I,A)
beam.add_supports(Support(0,(1,1,1)))
beam.add_loads(UDLV(-3000,(0,3)), TrapezoidalLoadV((0,5000),(3,6)))
analyzer(beam)
