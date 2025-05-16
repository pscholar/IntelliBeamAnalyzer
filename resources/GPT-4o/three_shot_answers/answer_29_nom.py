from indeterminatebeam.loading import PointLoadV, PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

beam = Beam(5)
beam.add_supports(Support(0, (1, 1, 1)), Support(5, (1, 1, 0)))
beam.add_loads(PointLoadV(-12000, 2), PointTorque(15000, 4))
analyzer(beam)
