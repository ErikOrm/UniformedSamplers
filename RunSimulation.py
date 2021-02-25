from Simulator import Crossing,GlobalQueue
from ReadData import readInstance, score
import argparse
import act

def run_simulation(instance_name, act_function, temp=1.0, prioleft=3, discount=0.5):

    D, I, S, V, F, street_list, street_names, path_list, time_left, cars = readInstance(instance_name)

    total_score = 0
    bonus = F
    crossings = Crossing(street_list)
    global_queue = GlobalQueue(crossings)


    list_of_traffic_light_assignments = []


    # initialise queues
    for car in cars:
        from_crossing = street_list[car.path_list[0]][0]
        current_crossing = street_list[car.path_list[0]][1]
        print(crossings.crossings[current_crossing])
        crossings.crossings[current_crossing][from_crossing].append(car)

    params = {'crossings': crossings, 'cars': cars, 'temp': temp, 'prioleft': prioleft,
              'discount': discount, 'street_list': street_list}

    traffic_light_assignments = act_function(params)
    print(traffic_light_assignments)
    traffic_lights = {}
    for i in range(len(traffic_light_assignments)):
        if len(traffic_light_assignments[i][0]) > 0:
            traffic_lights[i] =  (0, traffic_light_assignments[i][0][0])
        else:
            traffic_lights[i] =  (0, 1)
    # simulation loop
    for time_step in range(D):

        n_finished = global_queue.remove(time_step)

        #list_of_traffic_light_assignments.append(traffic_lights)

        moved_cars = crossings.trafficlight(traffic_lights)
        for car in moved_cars:
            global_queue.add(car, time_step + street_list[car.path_list[car.pointer]][2])
        total_score += score(D, time_step, n_finished, bonus)

    # check lights
    for i in range(len(traffic_light_assignments)):
        light = traffic_lights[i]
        tick = light[1] - 1
        if tick == 0:
            print(traffic_light_assignments[i])
            next = (light[0] + 1) % len(traffic_light_assignments[i])
            traffic_lights[i] = (next, traffic_light_assignments[i][0][next])




    return score, list_of_traffic_light_assignments


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Basic data reader')
    parser.add_argument('--instance_name', help='instance to read')
    #parser.add_argument('act', help='actor')
    print(parser)
    args = parser.parse_args()
    print(args)
    actor = act.prioAct

    data = run_simulation(args.instance_name, actor)
    print(data)
