#in this python file we will create the physical elements of the simulation
#this starts with the railway track, stations and the trains

import numpy as np
from mesa.space import NetworkGrid
from mesa import Agent, Model



    def move(self):
        if self.route:
            next_station = self.route[0]
            distance_to_next_station = abs(next_station - self.location)





            if distance_to_next_station >= self.speed:
                self.location += self.speed





            else:
                # Train arrives at next station
                self.location = next_station
                self.route.pop(0)



    def increase_time(self):
        self.time += 10  # increase time with 10 seconds




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



trains = [] #dit nog uitbreiden

# Simulation steps
num_steps = 10
for step in range(num_steps):
    for train in trains:
        train.move()
        train.increase_time()




