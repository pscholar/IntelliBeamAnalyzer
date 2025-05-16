from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(150, 220)
A = get_rect_section_area(150, 220)
beam = Beam(20, E=E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 1)), Support(6, (0, 1, 0)), Support(14, (0, 1, 0)), Support(20, (1, 1, 1)))
beam.add_loads(UDLV(-5000, (0, 20)), PointTorque(25000, 12), PointLoadV(-30000, 3))
analyzer(beam)
