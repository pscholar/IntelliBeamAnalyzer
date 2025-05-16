from indeterminatebeam.loading \
  import UDLV,PointTorque
from indeterminatebeam.indeterminatebeam \
    import Support, Beam
from utility.beam_analyzer import analyzer
from utility.mdatabase import material
from utility.calc import get_rect_section_inertia,\
  get_rect_section_area

E = material('steel')
I = get_rect_section_inertia(275, 275)
A = get_rect_section_area(275, 275)

beam = Beam(7, E, I, A)
s1 = Support(0, (1, 1, 0))
s2 = Support(7, (0, 1, 0))
beam.add_supports(s1, s2)
l1 = UDLV(-22e3, (0, 7))
l2 = PointTorque(-40e3, 3.5)
beam.add_loads(l1, l2)
analyzer(beam)



