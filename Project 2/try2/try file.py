from p2q2 import *

df_flags = pd.read_csv('E:\SMUexchange\computational_thinking\Proj2\data\\flags_r1.csv',header= None)
flags_list = df_flags.values.tolist()



graph_flags = create_graph(flags_list)



#
print(get_routes(100,2,flags_list,2))

# d = {0: '1', 2:'sas', 3:'a'}
# for a in d.keys():
#     print(a)
#
# l = [1,2,3,4]
#
# min = l[0]
#
# for elem in l[1:]:
#     if elem < min:
#         min = elem
