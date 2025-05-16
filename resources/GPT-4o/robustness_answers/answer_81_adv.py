from indeterminatebeam.loading import UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(150, 350)
A = get_rect_section_area(150, 350)
beam = Beam(6, E, I, A)
beam.add_supports(Support(0, (1,1,0)), Support(6, (0,1,0)))
beam.add_loads(UDLV(-25000, (0,6)))
analyzer(beam)
