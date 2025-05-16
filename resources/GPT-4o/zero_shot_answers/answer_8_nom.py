from indeterminatebeam.loading import PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(200, 400)
A = get_rect_section_area(200, 400)

beam = Beam(4, E, I, A)
beam.add_supports(Support(4, (1,1,1)))
beam.add_loads(PointTorque(-12000, 0))
analyzer(beam)
