from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(250, 500)
A = get_rect_section_area(250, 500)
beam = Beam(9, E, I, A)
beam.add_supports(Support(0, (0, 1, 0)), Support(9, (0, 1, 0)))
beam.add_loads(PointLoadV(-40000, 3))
analyzer(beam)
