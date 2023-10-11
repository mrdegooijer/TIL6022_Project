#in this python file we will create the physical elements of the simulation
#this starts with the railway track, stations and the trains

import numpy as np
import matplotlib.pyplot as plt

class STATION:
    def __init__(self, name,  location, platforms):
        self.name = name
        self.location = location
        self.platforms = platforms


class TRAIN:
    def __init__(self, train_id, type, location, route, speed_distance):
        self.train_id = train_id
        self.type = type
        self.location = location
        self.route = route
        self.speed_distance = speed_distance # speed in meter (per time step of 10s)
        self.time = 0
#        self.acceleration = acceleration
#        self.deceleration = deceleration

    def move(self):
        if self.route:
            next_station = self.route[0]
            distance_to_next_station = abs(next_station - self.location)

            if distance_to_next_station >= self.speed_distance:
                self.location += self.speed_distance
            else:
                # The train arrives at next station
                self.location = next_station
                self.route.pop(0)

    def increase_time(self):
        self.time += 10  # Increase time with 10 seconds

#hierin uiteindelijk de stations plaatsen
route_HS_IC = [500, 1500, 800] # in m
route_HS_spr = [500, 1500, 800] # in m
route_R_IC = [500, 1500, 800] # in m
route_R_spr = [500, 1500, 800] # in m


#train data:
trains = ["HS", "R", "HS"] # start location
traintype = ["IC", "IC", "IC"]

# hierna misschien deze loop door de tijd heen laten loopen. Dan zou je alle treinen op die tijd aan kunnen roepen


# deze loop alleen voor de treinen de ene kant op. Een andere voor de andere kant op
for train in range(len(trains)):
    if trains[train] == "HS": # if the train from Den Haag HS to Rotterdam
        start_location = 0
        if traintype[train] == "IC":
            route = route_HS_IC
        else:
            route = route_HS_spr
    else:
        start_location = 0
        if traintype[train] == "IC":
            route = route_HS_IC
        else:
            route = route_R_spr

for _ in range(route_length):
            next_station = random.choice(stations)
            while next_station == route[-1]:
                next_station = random.choice(stations)
            route.append(next_station)
        train_speed = random.randint(1, 3)  # Willekeurige snelheid

        train = TRAIN(i, start_station, route, train_speed)
        trains.append(train)


def __init__(self, train_id, type, location, route, speed_distance):

# Simulation steps
#num_steps = 10
#for step in range(num_steps):
#    for train in trains:
#        train.move()
#        train.increase_time()