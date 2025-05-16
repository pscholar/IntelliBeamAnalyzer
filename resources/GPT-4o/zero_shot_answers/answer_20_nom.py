
from indeterminatebeam.loading import UDLV, PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300, 500)
A = get_rect_section_area(300, 500)

beam = Beam(8, E, I, A)
support1 = Support(0, (1, 1, 0))
support2 = Support(8, (1, 1, 0))
beam.add_supports(support1, support2)

load1 = UDLV(-2000, (0, 8))
moment1 = PointTorque(15000, 3)
beam.add_loads(load1, moment1)

analyzer(beam)
