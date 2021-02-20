# from p2q2 import *
from p2q2 import *
df_flags = pd.read_csv('E:\SMUexchange\computational_thinking\Proj2\data\\flags_r1.csv',header= None)
flags_list = df_flags.values.tolist()



graph_flags = create_graph(flags_list)


# graph_flags.add_vertex_and_connect_to_all_vertices(startingPoint)

# v = graph_flags.startingPoint
#
# l = [graph_flags.adjLists[v]]
# l.append(v)

# if isinstance(v, Vertex):
#     print("da")
# print(type(Vertex))
# if v in l:
#     print("da")
# else:
#     print("nu")

#print(get_min_distance(graph_flags.startingPoint,list_rand))

# rand_sample = get_sample_of_unvisited_flags(graph_flags)
#
print(get_routes(300,2,flags_list,3))

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
