from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(150, 350)
A = get_rect_section_area(150, 350)
beam = Beam(12, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(12, (1, 1, 1)))
beam.add_loads(PointLoadV(-20000, 4), PointLoadV(-15000, 9))
analyzer(beam)
