from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200, 300)
A = get_rect_section_area(200, 300)

beam = Beam(15, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(5, (1, 1, 1)), Support(10, (1, 1, 1)), Support(15, (1, 1, 1)))
beam.add_loads(PointLoadV(-20000, 7.5))
analyzer(beam)
