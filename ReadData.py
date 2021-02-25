import argparse
import numpy as np
from Simulator import *

class car:

    def __init__(self, ID, path_list, pointer, time_left):
        self.ID = ID
        self. path_list = path_list
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


def run_simulation(instance_name, f_name):

    D, I, S, V, F, street_list, street_names, path_list, time_left, cars = readInstance(instance_name)

    crossings = []
    global_queue = GlobalQueue(crossings)

    for car in cars:
        pass
        # add_to_queue(car, 0)

    for time_step in range(len(D)):
        if "basic":
            basic_act(time_step)




def basic_act(time_step):
    pass

def score(D, time_step, n_cars, bonus):
    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Basic data reader')
    parser.add_argument('instance_name', help='instance to read')

    try:
        args = parser.parse_args()
    except:
        print("Kindly provide a filename. Use -h for options.")
        sys.exit(1)

    data = readInstance(args.instance_name)
    print(data)
