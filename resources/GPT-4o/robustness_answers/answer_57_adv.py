from indeterminatebeam.loading import UDLV, PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(250, 500)
A = get_rect_section_area(250, 500)
beam = Beam(15, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(15, (0, 1, 0)))
beam.add_loads(UDLV(-10000, (0, 5)), PointTorque(-50000, 10))
analyzer(beam)
