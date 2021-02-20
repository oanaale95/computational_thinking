# Name: <TODO: replace with your name>
# Section: <TODO: replace with your section>

# lab4

# All statements should only be in functions. Do not include statements outside functions in this file.
def unique_followers(list1):
  unique_elements = []
  for element in list1:
    if element not in unique_elements:
      unique_elements.append(element)
  return(unique_elements)



  def sort_by_len(follower_tuple):
    return len(follower_tuple[1])



def select_tweeters(followers):
  if len(followers) < 5:
    raise Exception("Not enough users!")

  followers = [(i, follower) for i, follower in enumerate(followers)]

  followers.sort(key=len, reverse=True)

  user_ids = {followers[0][0]: followers[0][1]}

  unique_follwers = set(followers[0][1])

  while len(user_ids) < 5:

    max_unique_followers = len(unique_follwers)
    next_user_id_and_followers = ()

    # traverse all the user ids and their followers
    for user_id, followers_list in followers:
      if user_ids.get(user_id) is None:

        union = unique_follwers.union(set(followers_list))

        if len(union) >= max_unique_followers:
          max_unique_followers = len(union)
          next_user_id_and_followers = (user_id, followers_list)

    user_ids[next_user_id_and_followers[0]] = next_user_id_and_followers[1]

    unique_follwers = unique_follwers.union(set(next_user_id_and_followers[1]))


  return list(user_ids.keys())



# case1_followers = [[2], [0,3], [0,1], [1,2,4,5], [1,6,10], [], [7,8], [], [], [8], [9]]
# select_tweeters(case1_followers)