# Name: Oana Alexandra Miron
# Section: G1 3-5

# lab3b

# All statements should only be in functions. Do not include statements outside functions in this file.
 

# Takes in a base-10 integer and returns the base-2 (binary) equivalent as a string
# this method does NOT have to handle negative numbers (i.e. d will always be >=0)
# this method must NOT use Python's bin() function.
# this method must be recursive (i.e. it calls itself)
# there should not be leading zeros in the string that this method returns.

def to_binary(d):
  binary_no = ''
  if d == 0:
    return binary_no
  else:
    binary_no = to_binary(d//2) + str(d % 2)
    return binary_no






