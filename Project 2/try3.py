#<G1_T01>
#<Oana Alexanra Miron>


import numpy as np
import pandas as pd


class Vertex:
    def __init__(self, flag, points, x_coord, y_coord, visited=False):
        self.flag = flag
        self.points = points
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.visited = visited

    def __hash__(self):
        return hash((self.flag,self.points, self.x_coord,self.y_coord))

    def equals_vertex(self, v):
        if not isinstance(v, Vertex):
            return False

        return self.flag == v.flag and self.point == v.point and self.x_coord == v.x_coord and self.y_coord == v.y_coord

    def __eq__(self, v):
        if isinstance(v, Vertex):
            return self.equals_vertex(v)
        elif isinstance(v, list):
            for v_tmp in v:
                if self.equals_vertex(v_tmp):
                    return True
            return False  # none of the list elements are equal to vertex (self)

    def distance_to_vertex(self, v):
        '''
        :param v: Vertex
        '''

        return np.sqrt((self.x_coord - v.x_coord)**2 + (self.y_coord - v.y_coord)**2)

    def __str__(self):
        return f'flag is {self.flag}, no of points : {self.points}, x_coord:{self.x_coord}, y_coord:{self.y_coord}'


class Graph:
    def __init__(self):
        self.startingPoint = Vertex('SP', 0, 0, 0)
        self.adjLists = {self.startingPoint: []}

    def get_vertices(self):
        return list(self.adjLists.keys())

    def add_vertex_and_connect_to_all_vertices(self, new_vertex):
        if new_vertex in self.adjLists.keys():
            return
        for k in self.adjLists.keys():
            self.adjLists[k].append(new_vertex)

        self.adjLists[new_vertex] = self.get_vertices()

    def __str__(self):
        graph_str = ''
        for k, v_list in self.adjLists.items():
            graph_str += f'Vertex:{k.flag} Points: {k.points} Linked to:'

            for v in v_list:
                graph_str += f' {v.flag}'

            graph_str += '\n'

        return graph_str


def create_graph(flags):
    flags_graph = Graph()

    for element in flags:
        flags_graph.add_vertex_and_connect_to_all_vertices(
          Vertex(element[0], element[1], element[2], element[3])
        )

    return flags_graph


def generate_random_sample(flags_graph):
    flag_vertices = flags_graph.get_vertices()
    n = len(flag_vertices)
    sample_size = int(0.5*n)
    random_numbers = np.random.randint(low=0, high=n, size=sample_size)
    random_sample = {}

    for number in random_numbers:
        random_sample[flag_vertices[number]] = True

    return list(random_sample.keys())


def get_sample_of_unvisited_flags(flags_graph, depth=0):
    rand_sample = generate_random_sample(flags_graph)

    initial_len_rand_sample = len(rand_sample)

    i = 0
    len_rand_sample = len(rand_sample)
    while i < len_rand_sample:
        flag = rand_sample[i]
        if flag.visited == True:
            del rand_sample[i]
            len_rand_sample -= 1

            if depth < 3 and len_rand_sample <= int(0.25 * initial_len_rand_sample):
                return get_sample_of_unvisited_flags(flags_graph, depth+1)  # get new sample
            else:
                pass

        else:
            i += 1

    if len_rand_sample == 0:
        return get_sample_of_unvisited_flags(flags_graph, depth + 1)

    return rand_sample


def get_min_distance_vertex(current_vertex, list_random_sample):
    '''
    Returns the closest flag (Vertex object) to the current flag ('current_vertex')

    :param current_vertex: Vertex
    :param list_random_sample: list of Vertex objects
    :return: Vertex
    '''

    min_vertex = list_random_sample[0]
    min_distance = current_vertex.distance_to_vertex(min_vertex)

    for i in range(1, len(list_random_sample)):
        vertex_to_compare = list_random_sample[i]
        distance_to_compare = current_vertex.distance_to_vertex(vertex_to_compare)

        if distance_to_compare == min_distance:
            if vertex_to_compare.points > min_vertex.points:
                min_vertex = vertex_to_compare

        elif distance_to_compare < min_distance:
            min_vertex = vertex_to_compare
            min_distance = distance_to_compare

    return min_vertex


def q2_v1(p, picked_flags_by_players_dict, graph_flags):
    points = 0

    graph_flags.startingPoint.visited = True

    while points < p:
        min_distance = -1
        player = -1
        following_vertex = None

        for player_no in picked_flags_by_players_dict.keys():
            random_sample = get_sample_of_unvisited_flags(graph_flags)

            current_vertex_for_player = picked_flags_by_players_dict[player_no][-1]
            next_vertex = get_min_distance_vertex(current_vertex_for_player, random_sample)
            distance_between_vertices = current_vertex_for_player.distance_to_vertex(next_vertex)

            if min_distance == -1 or distance_between_vertices < min_distance:
                min_distance = distance_between_vertices
                player = player_no
                following_vertex = next_vertex

            elif distance_between_vertices == min_distance and following_vertex.points < next_vertex.points:
                min_distance = distance_between_vertices
                player = player_no
                following_vertex = next_vertex

        picked_flags_by_players_dict[player].append(following_vertex)
        points += following_vertex.points
        following_vertex.visited = True

    return picked_flags_by_players_dict



def q2_v2 (p, picked_flags_by_players_dict, graph_flags):
    solution_q1 = q2_v1(p, picked_flags_by_players_dict,graph_flags)

    for solution_of_player in solution_q1:


        min_distance_to_sp = solution_of_player[-1].distance_to_vertex(graph_flags.startingPoint)

        return_to_sp_flags_list = []
        prev_vertex = solution_of_player[-1]
        distance_from_last_flag = 0

        for flag_vertex in reversed(solution_of_player[:-1]):
            distance_from_last_flag += prev_vertex.distance_to_vertex(flag_vertex)

            if distance_from_last_flag + flag_vertex.distance_to_vertex(graph_flags.startingPoint) < min_distance_to_sp:
                min_distance_to_sp = distance_from_last_flag + flag_vertex.distance_to_vertex(graph_flags.startingPoint)
                return_to_sp_flags_list = list(reversed(solution_of_player[solution_of_player.index(flag_vertex):-1]))

            prev_vertex = flag_vertex

            if distance_from_last_flag > min_distance_to_sp:
                break



def get_routes(p, v, flags, n):
    graph_flags = create_graph(flags)
    players_numbers = range(0,n)
    picked_flags_by_players_dict= dict()
    graph_flags.startingPoint.visited = True

    for number in players_numbers:
        picked_flags_by_players_dict[number]= [graph_flags.startingPoint]

    if v == 1:
        solution = q2_v1(p,picked_flags_by_players_dict,graph_flags)

    elif v ==2 :
        solution = q2_v2()

    list_solution_str = []

    for player_id in solution.keys():
        players_and_flags_str = []
        for i in range(0, len(solution[player_id])):
            players_and_flags_str.append(solution[player_id][i].flag)

        list_solution_str.append(players_and_flags_str[1:])
    return list_solution_str





