# Name: <Oana Alexandra Miron>
# Section: <G1-3-5>

# lab1b (Dijkstra's algo)

# All statements should only be in functions.
def gcd_b(x, y):
  while x != y:
    if x > y:
      x = x - y
    else:
      y = y - x
  return x


