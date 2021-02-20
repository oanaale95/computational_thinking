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


def get_sample_of_unvisited_flags(flags_graph):
    rand_sample = generate_random_sample(flags_graph)

    initial_len_rand_sample = len(rand_sample)

    for flag in rand_sample:
        if flag.visited:
            rand_sample.remove(flag)

            if len(rand_sample) <= int(0.75 * initial_len_rand_sample):
                return get_sample_of_unvisited_flags(flags_graph)  # get new sample

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


def v1(p, flags_graph):
    '''
    v1 represents a Greedy algorithm, where at each flag we generate a random sample of potential
    next flags and we go to the next closest one.

    :param p: int specifying the minimum no. of points that we need
    :param flags_graph: graph with all the vertices (flags)
    :return: list of flag names chosen
    '''
    flags_graph.startingPoint.visited = True
    list_solution_flags = [flags_graph.startingPoint]
    total_points_gained = 0

    while total_points_gained < p:
        random_sample = get_sample_of_unvisited_flags(flags_graph)

        # remove flags that are already part of our solution
        for flag in list_solution_flags:
            if flag in random_sample:
                random_sample.remove(flag)

        current_flag = list_solution_flags[len(list_solution_flags) - 1]

        next_flag = get_min_distance_vertex(current_flag, random_sample)
        next_flag.visited = True
        list_solution_flags.append(next_flag)

        total_points_gained += next_flag.points

        current_flag = next_flag

    list_solution_flags.remove(flags_graph.startingPoint)

    # final_flags_strings = []
    # for flag_vertex in list_solution_flags:
    #     final_flags_strings.append(flag_vertex.flag)

    return list_solution_flags


def v2(p, graph_flags):
    partial_solution = v1(p, graph_flags)

    #print([flag.flag for flag in partial_solution])
    min_distance_to_sp = partial_solution[-1].distance_to_vertex(graph_flags.startingPoint)
    # print(f'Min Dist: {min_distance_to_sp}')
    return_to_sp_flags_list = []
    prev_vertex = partial_solution[-1]
    distance_from_last_flag = 0
    # print(f'Partial Dist: {distance_from_last_flag}')

    for flag_vertex in reversed(partial_solution[:-1]):
        distance_from_last_flag += prev_vertex.distance_to_vertex(flag_vertex)
        # print(f'DIST BETWEEN VERTECIEs {prev_vertex.flag} and {flag_vertex.flag} is {prev_vertex.distance_to_vertex(flag_vertex)}')
        # print(f'Partial Dist2: {distance_from_last_flag}')
        # print(f'dist from {flag_vertex.flag} to sp :{flag_vertex.distance_to_vertex(graph_flags.startingPoint)}')
        if distance_from_last_flag + flag_vertex.distance_to_vertex(graph_flags.startingPoint) < min_distance_to_sp:
            min_distance_to_sp = distance_from_last_flag + flag_vertex.distance_to_vertex(graph_flags.startingPoint)
            return_to_sp_flags_list = list(reversed(partial_solution[partial_solution.index(flag_vertex):-1]))
            # print(f'Min Dist2: {min_distance_to_sp}')
        prev_vertex = flag_vertex

        if distance_from_last_flag > min_distance_to_sp:
            break

    # if len(return_to_sp_flags_list)==0:
    #     print('NU O MERS')
    partial_solution.extend(return_to_sp_flags_list)

    return partial_solution


def get_route(p, v, flags):
    graph_flags = create_graph(flags)

    if v == 1:
        solution = v1(p, graph_flags)

    if v == 2:
        solution = v2(p, graph_flags)

    final_flags_strings = []
    for flag_vertex in solution:
        final_flags_strings.append(flag_vertex.flag)

    # print(final_flags_strings)
    return final_flags_strings

    return solution


def get_routes(p, v, flags, n):
    graph_flags = create_graph(flags)
    players_numbers = range(0,n)
    picked_flags_by_players_dict= dict()
    points = 0
    graph_flags.startingPoint.visited = True

    for number in players_numbers:
        picked_flags_by_players_dict[number]= [graph_flags.startingPoint]

    if v == 1:

        while points < p:
            for player in picked_flags_by_players_dict:
                random_sample = get_sample_of_unvisited_flags(graph_flags)
                current_vertex = picked_flags_by_players_dict[player][-1]
                next_vertex = get_min_distance_vertex(current_vertex,random_sample)
                next_vertex.visited = True
                points += next_vertex.points
                picked_flags_by_players_dict[player].append(next_vertex)
                if points > p:
                    break
           # current_vertex = next_vertex
          # else:
            #     for player in picked_flags_by_players_dict:
            #         random_sample = get_sample_of_unvisited_flags(graph_flags)
            #         current_vertex = picked_flags_by_players_dict[player][-1]
            #         next_vertex = get_min_distance_vertex(current_vertex, random_sample)
            #         next_vertex.visited = True
            #         points += next_vertex.points
            #         picked_flags_by_players_dict[player].append(next_vertex)

        list_solution_str =[]

        for player_id in picked_flags_by_players_dict:
            players_and_flags_str = []
            for i in range(0, len(picked_flags_by_players_dict[player_id])):
                players_and_flags_str.append(picked_flags_by_players_dict[player_id][i].flag)

            list_solution_str.append(players_and_flags_str[1:])

        return(list_solution_str)

    elif v ==2 :
        return []





