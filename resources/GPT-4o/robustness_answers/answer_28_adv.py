from indeterminatebeam.loading import TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(150,300)
A = get_rect_section_area(150,300)
beam = Beam(7,E,I,A)
beam.add_supports(Support(0,(1,1,1)), Support(7,(1,1,1)))
beam.add_loads(TrapezoidalLoadV((2000,5000),(0,7)))
analyzer(beam)
