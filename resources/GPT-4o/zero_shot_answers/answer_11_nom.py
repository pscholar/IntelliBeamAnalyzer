from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(150, 300)
A = get_rect_section_area(150, 300)

beam = Beam(8, E, I, A)
beam.add_supports(Support(0, (1,1,0)), Support(8, (1,1,0)))
beam.add_loads(PointLoadV(-25000, 5))
analyzer(beam)
