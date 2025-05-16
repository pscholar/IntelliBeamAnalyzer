from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E=material('concrete')
I=get_rect_section_inertia(300,500)
A=get_rect_section_area(300,500)
beam=Beam(7,E,I,A)
s1=Support(0,(1,1,0))
s2=Support(7,(0,1,0))
beam.add_supports(s1,s2)
load=PointLoadV(-15000,2)
beam.add_loads(load)
analyzer(beam)
