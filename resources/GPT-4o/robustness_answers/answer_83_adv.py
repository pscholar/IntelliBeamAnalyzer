from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('concrete')
I1 = get_rect_section_inertia(300,600)
A1 = get_rect_section_area(300,600)
I2 = get_rect_section_inertia(300,600)
A2 = get_rect_section_area(300,600)
beam = Beam(12, E, [I1,I2], [A1,A2], [5])
beam.add_supports(Support(0,(1,1,0)), Support(5,(0,1,0)), Support(12,(0,1,0)))
beam.add_loads(UDLV(-30000,(0,5)), PointLoadV(-45000,8))
analyzer(beam)
