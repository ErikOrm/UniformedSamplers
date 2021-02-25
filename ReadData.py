import argparse
import numpy as np



def readInstance(instance_name):


    file = open(instance_name, 'r')
    data = {}

    # time steps, uintersections, streets, cars, bonus points
    D, I, S, V, F = [int(x) for x in file.readline().split()]

    # [start, end, ]
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


    cars = [(x, path_list[x], 0, time_left[x]) for x in range(len(path_list))]


    return D, I, S, V, F, street_list, street_names, path_list, time_left, cars



"""


"""



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
