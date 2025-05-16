def get_rect_section_area(b,h):
  return (b * h) / (1000 ** 2)

def get_rect_section_inertia(b,h):
  return (b * (h ** 3) / 12) * 1e-12