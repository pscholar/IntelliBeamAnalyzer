from indeterminatebeam.loading import TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(150, 300)
A = get_rect_section_area(150, 300)

beam = Beam(5, E, I, A)
support1 = Support(0, (1, 1, 1))
support2 = Support(5, (0, 1, 0))
beam.add_supports(support1, support2)

load = TrapezoidalLoadV((0, -8000), (0, 5))
beam.add_loads(load)

analyzer(beam)
