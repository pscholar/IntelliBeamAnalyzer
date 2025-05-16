from indeterminatebeam.loading import PointLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E=material('steel')
I=get_rect_section_inertia(200,400)
A=get_rect_section_area(200,400)
beam=Beam(6,E,I,A)
s1=Support(0,(1,1,0))
s2=Support(6,(0,1,0))
beam.add_supports(s1,s2)
load=PointLoadV(-8000,1.5)
beam.add_loads(load)
analyzer(beam)
