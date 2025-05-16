from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(200,400)
A = get_rect_section_area(200,400)
beam = Beam(6,E,I=I,A=A)

s1 = Support(0,(1,1,0))
s2 = Support(6,(0,1,0))
beam.add_supports(s1,s2)

l1 = PointLoadV(-10000,3)
beam.add_loads(l1)

analyzer(beam)
