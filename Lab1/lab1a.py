# Name: <Oana Alexandra Miron>
# Section: <G1-3-5>

# lab1a (Brute force)

# All statements should only be in functions.
def gcd_a(x, y):
    t = min(x, y)
    while t >= 1:
        if x % t == 0 and y % t == 0:
            return t
        else:
            t = t - 1

