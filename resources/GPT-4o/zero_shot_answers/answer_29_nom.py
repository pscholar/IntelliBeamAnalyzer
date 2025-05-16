from indeterminatebeam.loading import PointLoadV, PointTorque
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia
from utility.calc import get_rect_section_area

beam = Beam(5)
support1 = Support(0, (1, 1, 1))
support2 = Support(5, (1, 1, 0))
beam.add_supports(support1, support2)

load1 = PointLoadV(-12000, 2)
load2 = PointTorque(15000, 4)
beam.add_loads(load1, load2)

analyzer(beam)
