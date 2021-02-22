import argparse
import numpy as np



def readInstance(instance_name):


    file = open(instance_name, 'r')
    data = {}
    a, b, c = [int(x) for x in file.readline().split()]


    for i in range(len(a)):
        pass # READ FIRST DATATYPE


    for i in range(len(b)):
        pass # READ SECOND DATATYPE


    for i in range(len(c)):
        pass # READ THIRD DATATYPE

    return data



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Basic data reader')
    parser.add_argument('instance_name', help='instance to read')

    try:
        args = parser.parse_args()
    except:
        print("Kindly provide a filename. Use -h for options.")
        sys.exit(1)

    data = readInstance(args.instance_name)
