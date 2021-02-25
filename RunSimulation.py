
def run_simulation(instance_name, act_function):

    D, I, S, V, F, street_list, street_names, path_list, time_left, cars = readInstance(instance_name)

    total_score = 0

    crossings = Crossing(street_list)
    global_queue = GlobalQueue(crossings)


    list_of_traffic_light_assignments = []


    # initialise queues
    for car in cars:
        from_crossing = street_list[car.path_list[0]][0]
        current_crossing = street_list[car.path_list[0]][1]
        crossings[current_crossing][from_crossing].append(car)

    # simulation loop
    for time_step in range(len(D)):

        n_finished = global_queue.remove(time_step)

        traffic_light_assignments = act_function(time_step)

        list_of_traffic_light_assignments.append(traffic_light_assignments)

        moved_cars = crossings.trafficlight(traffic_light_assignments)
        for car in moved_cars:
            global_queue.add(car, time_step + street_list[car.path_list[car.pointer]][2])
        total_score += score(D, time_step, n_finished, bonus)

    return score, list_of_traffic_light_assignments
