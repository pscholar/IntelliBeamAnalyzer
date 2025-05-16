from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(300, 600)
A = get_rect_section_area(300, 600)
beam = Beam(6, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(6, (1, 1, 1)))
beam.add_loads(PointLoadV(-40000, 3))
analyzer(beam)
