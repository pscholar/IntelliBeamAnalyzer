from indeterminatebeam.loading import TrapezoidalLoadV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E=material('steel')
beam=Beam(5, E)
beam.add_supports(Support(0, (1, 1, 1)), Support(5, (0, 1, 0)))
beam.add_loads(TrapezoidalLoadV((0, -8000), (0, 5)))
analyzer(beam)
