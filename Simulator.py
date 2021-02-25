import numpy as np

class GlobalQueue:
    def __init__(self, crossings, ):
        self.queue = {}
        self.crossings = crossings

    def add(self):

    def remove(self, t):
        n_finished = 0
        for car in self.queue[t]:
            if len(car.path) >= 2:
                self.crossings[car.path[0]].append(car)
            else:
                n_finished += 1
        return n_finished



class Crossing:
    def __init__(self, id, ):

