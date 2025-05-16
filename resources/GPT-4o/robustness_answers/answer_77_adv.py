from indeterminatebeam.loading import TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(300, 300)
A = get_rect_section_area(300, 300)
beam = Beam(6, E, I, A)
beam.add_supports(Support(0, (1, 1, 1)), Support(6, (0, 1, 0)))
beam.add_loads(TrapezoidalLoadV((0, -25000), (0, 6)))
analyzer(beam)
