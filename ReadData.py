import argparse
import numpy as np

#

class car:

    def __init__(self, ID, path_list, pointer, time_left):
        self.ID = ID
        self.path_list = path_list
        self.pointer = pointer
        self.time_left = time_left

    def __repr__(self):
        return "car: %i " % self.ID



def readInstance(instance_name):


    file = open(instance_name, 'r')
    data = {}

    # time steps, uintersections, streets, cars, bonus points
    D, I, S, V, F = [int(x) for x in file.readline().split()]

    # [start, end, tid]
    street_list = []
    street_names = []
    # street indices per car
    path_list = []
    # remaining time per car
    time_left = []

    for i in range(S):
        tmp_list = file.readline().split()
        street_list.append([int(tmp_list[0]), int(tmp_list[1]), int(tmp_list[3])])
        street_names.append(tmp_list[2])


    for i in range(V):
        tmp_list = file.readline().split()
        path_list.append([street_names.index(x) for x in tmp_list[1:]])
        time_left.append(np.sum(street_list[x][2] for x in path_list[-1]))


    cars = [car(x, path_list[x], 0, time_left[x]) for x in range(len(path_list))]


    return D, I, S, V, F, street_list, street_names, path_list, time_left, cars


def print_solution(list_of_traffic_light_assignments, I, S, street_list, street_names):

    # {cr : [(prev_cr, time)]}
    # [[prev_cr, time]]

    prev_crossing_next_crossing_to_street_dict = {(cr1, cr2): -1 for cr1 in range(I) for cr2 in range(I)}

    for st in range(S):
        prev_crossing_next_crossing_to_street_dict[(street_list[st][0], street_list[st][1])] = street_names[st]


    lines = {(cr, prev_cr) : -1 for cr in range(I) for prev_cr in range(I)}

    number_of_intersections_w_tl = 0
    number_streets_w_tl = [0]*I

    for cr in range(I):
        found = False
        number_streets_w_tl[cr] = 0
        for prev_cr, time in list_of_traffic_light_assignments[cr]:
            street_name = prev_crossing_next_crossing_to_street_dict[(prev_cr, cr)]
            assert street_name != -1, "failure at converting to street name"
            lines[cr, prev_cr] = (street_name, time)
            number_streets_w_tl[cr] += 1
            found = True
        if found:
            number_of_intersections_w_tl += 1

    print(number_of_intersections_w_tl)
    for cr in range(I):
        if number_streets_w_tl[cr] > 0:
            print(cr)
            print(number_streets_w_tl[cr])
            for prev_cr in range(I):
                l = lines[(cr, prev_cr)]
                if l != -1:
                    print(l[0], l[1])







def basic_act(time_step):
    return []

def score(D, time_step, n_cars, bonus):
    return n_cars*(bonus + (D - time_step))


if __name__ == "__main__":




    parser = argparse.ArgumentParser(description='Basic data reader')
    parser.add_argument('instance_name', help='instance to read')

    try:
        args = parser.parse_args()
    except:
        print("Kindly provide a filename. Use -h for options.")
        sys.exit(1)

    D, I, S, V, F, street_list, street_names, path_list, time_left, cars = readInstance(args.instance_name)
    print_solution([[(2, 2)], [(0, 1), (3,2)], [(1,1)], []], I, S, street_list, street_names)
