# Name: Oana Alexandra Miron
# Section: G1 3-5

# p1q1

# TODO: fill q1_recursive
# m is a matrix represented by a 2D list of integers. e.g. m = [[1,2,3],[4,5,6],[7,8,9]]
# This function returns the another 2D list based on the specified logic in the requirements.
import numpy as np
import pandas as pd
# DO NOT EDIT q1(m)
def q1(m):
  # creating an output 2D list with the same dimensions and initializing all values to None
  # q1_recursive function will update this 2D list accordingly with the computed values
  output = [[None for i in range(len(m[0]))] for j in range(len(m))]
  q1_recursive(m, output, 0, 0)
  return output
  
def q1_recursive(m, output, row, col):
    if row == len(m):
        return output
    else:
        sum_row = sum(m[row][col:])

        sum_col = 0
        for value in range(row, len(m)):
            sum_col += m[value][col]

        output[row][col] = sum_row + sum_col

        if col != len(m[row])-1:
          return q1_recursive(m, output, row, col+1)
        else:
          return q1_recursive(m, output, row+1, 0)






