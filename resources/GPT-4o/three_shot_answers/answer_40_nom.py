from indeterminatebeam.loading import UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(350, 500)
A = get_rect_section_area(350, 500)
beam = Beam(15, E=E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 0)), Support(10, (1, 1, 0)), Support(15, (1, 1, 1)))
beam.add_loads(UDLV(-3000, (0, 10)), TrapezoidalLoadV((-0, -6000), (10, 15)))
analyzer(beam)
