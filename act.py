import numpy as np
from collections import defaultdict


def prioAct(params):
    lighton = []
    lightprio = {i:{} for i in range(len(params["street_list"]))}
    for car in params["cars"]:
        for street1, street2 in zip(car.path_list[1:], car.path_list[:-1]):
            if not street1 in lightprio[street2].keys():
                lightprio[street2][street1] = 0
            lightprio[street2][street1] += 1
    print(lightprio)
    for light in lightprio.values():
        weight = np.array([np.exp(x/params["temp"]) for x in light.values()])
        weight /= np.sum(weight)
        time = np.random.binomial(20, p=weight)
        lighton.append((time, light.keys()))
    return lighton