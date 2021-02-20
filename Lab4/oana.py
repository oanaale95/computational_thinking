def sort_by_len(follower_tuple):
    '''
    follower tuple is a tuple which has on index 0 the user id
    and on index 1 de list of followers; so, we want to return
    the length of the list of followers from index 1, such that
    it will be used by the sort function
    '''
    return len(follower_tuple[1])

def select_tweeters(followers):
    if len(followers) < 5:
        raise Exception("Not enough users!")
    
    # make tuples from the initial list, where a tuple has at index 0 the user id
    # and at index one the list of followers
    # e.g:[(0,[2]), (1,[0,3]), (2,[0,1])...]
    followers = [(i,follower) for i,follower in enumerate(followers)]

    # sort in decreasing order; element at index 0 has the most followers
    followers.sort(key=sort_by_len, reverse=True)

    # dictionary which will contain the  five user ids with the most followers as keys
    # and their followers as values
    user_ids = {followers[0][0]: followers[0][1]}
    
    # set which contains the unique followers of the select user ids
    # for now it only contains the followers of the user id with the most followers
    unique_follwers = set(followers[0][1])

    while len(user_ids) < 5:
        # this variable holds the maximum number of unique users that we will have after this round (adica dupa ce mai adaugam followerii unui user id)
        # in the beginning it is initialized current number of users ids
        max_unique_followers = len(unique_follwers)

        # this variable will hold a tuple, where on index 0 it will have the user id and on index 1 it will have the list of followers of the user id
        # this variable will hold basically the next user id that brings us the most unique new followers
        next_user_id_and_followers = ()

        # traverse all the user ids and their followers
        for user_id, followers_list in followers:
            if user_ids.get(user_id) is None: # check to see that we didn't already add the current user id
                # make a set union of our unique followers with the followers of the current user id
                # we want to see if we will get new unique followers or not
                union = unique_follwers.union(set(followers_list))           
                
                # if we have more unique followers with the followers of the current user id
                if len(union) >= max_unique_followers:
                    # update the value of max
                    max_unique_followers = len(union)
                    # remember the user id and his followers
                    next_user_id_and_followers = (user_id, followers_list)
        
        # after we traversed the entire list and we selected the user id which brings us the most new unique followers we add it to our dictionary
        user_ids[next_user_id_and_followers[0]] = next_user_id_and_followers[1]

        # and we update the 'unique_follwers' variable to have now also the unique followers brought by the selected user id
        unique_follwers = unique_follwers.union(set(next_user_id_and_followers[1]))

    print("User ids: " + str(list(user_ids.keys())))
    print("Unique followers: " + str(unique_follwers))

    return list(user_ids.keys())


# asta ii exemplu din pdf
case1_followers = [[2], [0,3], [0,1], [1,2,4,5], [1,6,10], [], [7,8], [], [], [8], [9]]

# chemam function aici
select_tweeters(case1_followers)