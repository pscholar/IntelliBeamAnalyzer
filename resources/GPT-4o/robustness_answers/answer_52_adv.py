from indeterminatebeam.loading import PointLoadV, UDLV, PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(250, 500)
A = get_rect_section_area(250, 500)
beam = Beam(5 + 6 + 7, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(5, (1, 1, 0)), Support(11, (1, 1, 1)))
beam.add_loads(PointLoadV(-18000, 3), UDLV(-10000, (5, 11)), PointTorque(-40000, 11))
analyzer(beam)
