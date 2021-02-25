import numpy as np

class GlobalQueue:
    def __init__(self, crossings, ):
        self.queue = {}
        self.crossings = crossings

    def add(self, car, t):
        self.queue[t].append(car)

    def remove(self, t):
        n_finished = 0
        for car in self.queue[t]:
            if len(car.path) >= 2:
                self.crossings[car.path[0]].append(car)
            else:
                n_finished += 1
        return n_finished



class Crossing:
    def __init__(self, street_list):
        self.crossings = {i:{} for i in range(len(street_list))}
        for street in street_list:
            self.crossings[street[1]][street[0]] = []

    def trafficlight(self, lightindex):
        #lightindex[i] is value of street
        moved_cars = []
        for crossing_id, light in enumerate(lightindex):
            car = self.crossings[crossing_id][light].pop()
            car.pointer +=1
            moved_cars.append(car)

        return moved_cars