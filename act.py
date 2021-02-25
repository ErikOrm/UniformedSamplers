import numpy as np
from collections import defaultdict


def prioAct(params):
    lighton = []
    lightprio = {i:defaultdict(int) for i in range(len(params.street_list))}
    for car in params.cars:
        for street1, street2 in zip(car.path_list[1:], car.path_list[:-1]):
            lightprio[street2][street1] += 1
    for light in lightprio:
        weight = np.array([np.exp(x/params.temp) for x in light.values()])
        weight /= np.sum(weight)
        time = np.random.binomial(20, p=weight)
        lighton.append(time)
    return lighton