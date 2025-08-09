# Remember what we did in math in first year (Dr. Ferdinand)
# Also remember that complexity of algorithms matters when you code (Dr. Patrick)
# When you code, you always have to raise exceptions when the input is not what the program handles

def get_sum_of_nat(nat):
  if nat < 0:
    raise ValueError("Should be a natural number only")
  return (nat * (nat + 1)) / 2

def get_sum_of_cube(nat):
  return pow(get_sum_of_nat(nat), 2)

