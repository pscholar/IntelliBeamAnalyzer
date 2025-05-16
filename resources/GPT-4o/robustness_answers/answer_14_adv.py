from indeterminatebeam.loading import PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(150, 150)
A = get_rect_section_area(150, 150)

beam = Beam(5, E, I, A)

s1 = Support(0, (1, 1, 1))

beam.add_supports(s1)

l1 = PointTorque(-15e3, 3)

beam.add_loads(l1)

analyzer(beam)
