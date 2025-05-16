from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(150, 300)
A = get_rect_section_area(150, 300)
beam = Beam(7 + 8 + 6, E, I, A)
beam.add_supports(Support(0, (1, 1, 0)), Support(7 + 8, (0, 1, 0)))
beam.add_loads(UDLV(-12000, (0, 7)), PointLoadV(-28000, 5), UDLV(-6000, (15, 21)))
analyzer(beam)
