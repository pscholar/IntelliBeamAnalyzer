from indeterminatebeam.loading import TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I = get_rect_section_inertia(150, 300)
A = get_rect_section_area(150, 300)

beam = Beam(10, E, I, A)

s1 = Support(0, (1, 1, 0))
s2 = Support(10, (1, 1, 0))

beam.add_supports(s1, s2)

l1 = TrapezoidalLoadV((0, -30e3), (0, 10))

beam.add_loads(l1)

analyzer(beam)
