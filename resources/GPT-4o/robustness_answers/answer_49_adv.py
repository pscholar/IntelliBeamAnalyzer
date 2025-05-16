from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)
beam = Beam(6 + 8 + 7, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(6, (0, 1, 0)), Support(14, (0, 1, 0)))
beam.add_loads(UDLV(-9000, (0, 6)), PointTorque(-35000, 10), PointLoadV(-15000, 11))
analyzer(beam)
