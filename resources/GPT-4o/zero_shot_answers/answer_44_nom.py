from indeterminatebeam.loading import UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(180,270)
A = get_rect_section_area(180,270)
beam = Beam(12, E, I=I, A=A)
s1 = Support(0, (1,1,0))
s2 = Support(5, (1,1,1))
s3 = Support(12, (0,1,0))
beam.add_supports(s1, s2, s3)
l1 = TrapezoidalLoadV((-2000,-6000), (0,5))
l2 = UDLV(-4000, (5,12))
beam.add_loads(l1, l2)
analyzer(beam)
