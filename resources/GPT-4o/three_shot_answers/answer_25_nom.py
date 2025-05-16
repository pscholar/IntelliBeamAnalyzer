from indeterminatebeam.loading import PointTorque, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(300, 500)
A = get_rect_section_area(300, 500)
beam = Beam(4, E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 0)), Support(4, (1, 1, 1)))
beam.add_loads(UDLV(-6000, (0, 4)), PointTorque(-10000, 2))
analyzer(beam)
