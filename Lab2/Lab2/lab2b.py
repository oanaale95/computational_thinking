# Name: Oana Alexandra Miron
# Section: G1 - 3 - 5

# lab2b

# All statements should only be in functions. Do not include statements outside functions in this file.

# INSTRUCTIONS: 
# Refer to the code in lab2b_main.py - perform_once will be called one time before 
# exist is called many times. You may modify perform_once if desired, or keep it as it is.
def sort_year(element):
  return element[1] # Element is a list of two elements (id,year)


def perform_once(employee_with_birthyear_list):
  return sorted(employee_with_birthyear_list, key=sort_year) # returns the matrix sorted by year

def bsearch(year, employee_with_birthyear_list):
  lower = -1
  upper = len(employee_with_birthyear_list)
  while not (lower + 1 == upper):
    mid = (lower + upper) // 2
    if year == employee_with_birthyear_list[mid][1]:
      return mid
    elif year < employee_with_birthyear_list[mid][1]:
      upper = mid
    else:
      lower = mid
  return -1 #if input year does not exist

# INSTRUCTIONS:
# Write a function called get_IDs_with_birthyear that takes in a year (as an integer) and an array (employee_with_birthyear_list)
# It then returns an array of employee IDs (integers) that have matching birthyears.
# If there is no match, this function returns an empty array (i.e. []).
def get_IDs_with_birthyear(year, employee_with_birthyear_list):
  found_idx = bsearch(year,employee_with_birthyear_list)

  if found_idx == -1:
    return []

  start_idx = found_idx - 1
  last_idx = found_idx + 1
  list_len = len(employee_with_birthyear_list)
  id_list=[employee_with_birthyear_list[found_idx][0]]

  while start_idx >=0 and employee_with_birthyear_list[found_idx][1] == employee_with_birthyear_list[start_idx][1]:
    id_list.append(employee_with_birthyear_list[start_idx][0])
    start_idx -= 1

  while last_idx < list_len and employee_with_birthyear_list[found_idx][1] == employee_with_birthyear_list[last_idx][1]:
    id_list.append(employee_with_birthyear_list[last_idx][0])
    last_idx += 1

  return id_list


# def get_IDs_with_birthyear(year, employee_with_birthyear_list):
#   list_id=[]
#   for pair in employee_with_birthyear_list:
#     if pair[1] == year:
#       list_id.append(pair[0])
#   return list_id