import numpy as np


def ThompsonAct(params):
    lighton = []
    for crossing in params.crossings:
        weight = np.array([np.exp(len(x)/params.temp) for x in crossing.values()])
        weight /= np.sum(weight)
        lighton.append(np.random.choice(crossing.keys,p=weight))
    return lighton
