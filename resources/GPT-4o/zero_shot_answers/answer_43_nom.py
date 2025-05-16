from indeterminatebeam.loading import PointLoadV, UDLV
from indeterminatebeam.indeterminatebeam import Support, Beam
from utility.beam_analyzer import analyzer

E = 30e9
I = 3.2e-4
A = 0.06
beam = Beam(20, E, I=I, A=A)
s1 = Support(0, (1,1,0))
s2 = Support(12, (1,1,1))
s3 = Support(20, (1,1,0))
beam.add_supports(s1, s2, s3)
l1 = UDLV(-10000, (0,12))
l2 = PointLoadV(-50000, 16)
beam.add_loads(l1, l2)
analyzer(beam)
