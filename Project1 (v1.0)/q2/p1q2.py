# Name: Oana Alexandra Miron
# Section: G1 3-5

# p1q2

# All statements should only be in functions. Do not include statements outside functions in this file.
# You may insert additional helper functions into this file if desired. 

import numpy as np
import pandas as pd

def is_stable(n,pref, solution):
  males_rank = pref.copy()
  females_rank =[]

  for i in range(len(pref)):
    if 'f' in pref[i][0]:
      list_now= pref[i]
      females_rank.append(list_now)
      males_rank.remove(list_now)

  df_males = pd.DataFrame(males_rank)
  df_females = pd.DataFrame(females_rank)

  df_list = [df_males, df_females]

  for dataframe in df_list:
    dataframe.set_index(dataframe.columns[0], inplace=True)

  df_males.columns = df_females.index.values.tolist()
  df_females.columns = df_males.index.values.tolist()


  for group in solution:
    husband = group[0]
    wife = group[1]
  # check value for given female
    score_wife = df_males[wife][husband]
  # male list for the other females to be checked
    list_females_col = df_males.columns.tolist()
    list_females_col.remove(wife)

    for candidate in list_females_col:
      score_other_woman = df_males[candidate][husband]

      if score_wife > score_other_woman:
        score_husband = df_females[husband][candidate]

        for pair in solution:
          if candidate in pair:
            candidate_husband = pair[0]
            candidate_husband_score = df_females[candidate_husband][candidate]

            if candidate_husband_score > score_husband:
              return False

  return True
