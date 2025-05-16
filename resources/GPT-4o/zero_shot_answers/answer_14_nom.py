from indeterminatebeam.loading import PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(300, 500)
A = get_rect_section_area(300, 500)

beam = Beam(5, E, I, A)
beam.add_supports(Support(0, (1,1,1)), Support(5, (0,1,0)))
beam.add_loads(PointTorque(-15000, 3))
analyzer(beam)
