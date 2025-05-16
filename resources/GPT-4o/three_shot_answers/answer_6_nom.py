from indeterminatebeam.loading import TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E=material('timber')
I=get_rect_section_inertia(150,300)
A=get_rect_section_area(150,300)
beam=Beam(2.5,E,I,A)
s=Support(0,(1,1,1))
beam.add_supports(s)
load=TrapezoidalLoadV((0,-4000),(0,2.5))
beam.add_loads(load)
analyzer(beam)
