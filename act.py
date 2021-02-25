import numpy as np


def thompsonAct(params):
    lighton = []
    for crossing in params.crossings:
        weight = np.array([np.exp(len(x)/params.temp) for x in crossing.values()])
        weight /= np.sum(weight)
        lighton.append(np.random.choice(crossing.keys,p=weight))
    return lighton


def prioAct(params):
    lighton = []
    for crossing in params.crossings:
        prioleft = []
        for x in crossing.values():
            prioleft.append(np.sum(np.array([len(car.path_list[car.pointer:]) for car in x] <= params.prioleft) + 0.2))
        weight = np.array([np.exp(x/params.gamma) for x in prioleft])
        weight /= np.sum(weight)
        lighton.append(np.random.choice(crossing.keys,p=weight))
    return lighton