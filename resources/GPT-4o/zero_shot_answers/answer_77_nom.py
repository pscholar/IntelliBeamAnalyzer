from indeterminatebeam.loading import TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(300, 300)
A = get_rect_section_area(300, 300)

beam = Beam(6, E, I, A)

s1 = Support(0, (1, 1, 1))
s2 = Support(6, (0, 0, 0))

beam.add_supports(s1, s2)

l1 = TrapezoidalLoadV((0, -25e3), (0, 6))

beam.add_loads(l1)

analyzer(beam)
