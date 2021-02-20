# Name: Oana Alexandra Miron
# Section: G1 3-5

# p1q3

# All statements should only be in functions. Do not include statements outside functions in this file.
# You may insert additional helper functions into this file if desired.

import numpy as np

def subset_sum(user_cost_dict, target, partial={}):
    s = np.sum(list(partial.values()))
    # check if the partial sum is equals to target
    if s == target:
        return [partial]
    if s > target:
        return [] # if we reach the number why bother to continue

    target_cost_combination = []

    k_prev = -1
    partial_copy = partial.copy()
    for i,k in enumerate(user_cost_dict.keys()):

        if k_prev != -1 and partial_copy.get(k_prev) != None:
            del partial_copy[k_prev]

        if s + user_cost_dict[k] > target:
            target_cost_combination.extend([partial_copy])
        else:
            remaining = dict(list(user_cost_dict.items())[i + 1:])
            partial_copy[k] = user_cost_dict[k]
            target_cost_combination.extend(subset_sum(remaining,target, partial_copy))
        k_prev= k

    return target_cost_combination


def get_total_value_sum(users,user_value_dict,user_follower_dict):
    added_users_and_followers ={}
    total_value_sum = 0
    for user in users:
        # access value, but if the dict is accessed and the key does not exist it will generate an exception
        # but with get it will return None instead
        if added_users_and_followers.get(user) == None:
            added_users_and_followers[user] = True
            total_value_sum += user_value_dict[user]

        for follower in user_follower_dict[user]:
            if added_users_and_followers.get(follower) == None:
                added_users_and_followers[follower] = True
                total_value_sum += user_value_dict[follower]

    return total_value_sum


def get_users_max_values(combinations, user_value_dict,user_follower_dict):
    picked_users = []
    max_value_sum = 0
    min_cost_sum = 0
    for i, dictionary in enumerate(combinations):
        current_value_sum = get_total_value_sum(list(dictionary.keys()),user_value_dict,user_follower_dict)
        current_cost_sum = np.sum(list(dictionary.values()))

        if i == 0 or current_value_sum > max_value_sum or (current_value_sum == max_value_sum and current_cost_sum <  min_cost_sum):
            max_value_sum = current_value_sum
            min_cost_sum = current_cost_sum
            picked_users = list(dictionary.keys())
    return picked_users


def select_advertisers(budget, followers, c, v):
  users = list(range(0,len(followers)+1))
  user_cost_dict = {u: cost for u, cost in zip(users, c)}
  user_value_dict = {u: value for u, value in zip(users, v)}
  user_follower_dict = {u: f for u, f in zip(users, followers)}
  combinations = subset_sum(user_cost_dict , budget)
  return get_users_max_values(combinations,user_value_dict,user_follower_dict)





