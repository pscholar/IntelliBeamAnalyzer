from indeterminatebeam.loading import UDLV, PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300,500)
A = get_rect_section_area(300,500)
beam = Beam(8,E,I,A)
beam.add_supports(Support(0,(1,1,1)),Support(8,(1,1,1)))
beam.add_loads(UDLV(-2000,(0,8)), PointTorque(15000, 3))
analyzer(beam)
