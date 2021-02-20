# Name: Oana Alexandra Miron
# Section: G1 3-5

# lab3a

# All statements should only be in functions. Do not include statements outside functions in this file.


# Takes in an integer and returns the sum of all its digits as an integer
# this method does NOT have to handle negative numbers (i.e. i will always be >=0)
# this method must be recursive (i.e. it will call itself)
# Refer to hints in the requirements doc.
def sum_of_digits(i):
  input = str(i)

  if len(str(i)) == 1:
    return i
  else:
    sum = int(input[0]) + sum_of_digits(int(input[1:]))
    return sum
