from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(250, 350)
A = get_rect_section_area(250, 350)
beam = Beam(24, E, I=I, A=A)
s1 = Support(0, (1,1,0))
s2 = Support(8, (1,1,0))
s3 = Support(16, (1,1,0))
s4 = Support(24, (1,1,0))
beam.add_supports(s1, s2, s3, s4)
l1 = UDLV(-5000, (0,24))
l2 = PointLoadV(-20000, 4)
l3 = PointLoadV(-20000, 20)
beam.add_loads(l1, l2, l3)
analyzer(beam)
