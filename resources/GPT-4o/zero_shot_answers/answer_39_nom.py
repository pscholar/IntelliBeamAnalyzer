from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia, get_rect_section_area

E = material('timber')
I = get_rect_section_inertia(140, 220)
A = get_rect_section_area(140, 220)

beam = Beam(11, E, I, A)
beam.add_supports(
    Support(0, (1,1,1)),
    Support(6, (0,1,0)),
    Support(11, (1,1,0))
)

beam.add_loads(
    PointLoadV(-18000, 3),
    UDLV(-4000, (6,11))
)

analyzer(beam)
