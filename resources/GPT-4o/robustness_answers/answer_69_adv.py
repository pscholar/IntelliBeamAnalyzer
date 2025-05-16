from indeterminatebeam.loading import TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(150, 300)
A = get_rect_section_area(150, 300)
beam = Beam(10, E, I, A)
beam.add_supports(Support(0, (1, 1, 0)), Support(10, (1, 1, 0)))
beam.add_loads(TrapezoidalLoadV((0, -30000), (0, 10)))
analyzer(beam)
