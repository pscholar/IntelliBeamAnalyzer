from indeterminatebeam.loading import UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(180, 270)
A = get_rect_section_area(180, 270)
beam = Beam(12, E=E, I=I, A=A)
beam.add_supports(Support(0, (1, 1, 0)), Support(5, (1, 1, 1)), Support(12, (0, 1, 0)))
beam.add_loads(TrapezoidalLoadV((2, 6), (0, 5)), UDLV(-4000, (5, 12)))
analyzer(beam)
