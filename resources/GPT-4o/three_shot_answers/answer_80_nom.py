from indeterminatebeam.loading import PointLoadV, PointTorque, UDLV, TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(275,275)
A = get_rect_section_area(275,275)
beam = Beam(7, E, I=I, A=A)
beam.add_supports(Support(0,(1,1,0)), Support(7,(0,1,0)))
beam.add_loads(UDLV(-22000,(0,7)), PointTorque(-40000,3.5))
analyzer(beam)
