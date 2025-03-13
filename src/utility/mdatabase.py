
youngs_modulus = {
  "steel": 200000000000,
  "concrete": 30000000000,
  "timber":1500000000,
}
def material(key : str):
  key = key.lower()
  return youngs_modulus.get(key , 200000000000)
