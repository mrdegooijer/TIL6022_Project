#in this python file we will create the physical elements of the simulation
#this starts with the railway track, stations and the trains

import numpy as np
import matplotlib.pyplot as plt

#class STATION:
#    def __init__(self, name,  location, platforms):
#        self.name = name
#        self.location = location
#        self.platforms = platforms


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

    def move(self, train_locations):

        if self.location == "HS":
            startlocation = "HS"
        else:
            start_locations = "R"
# nu iets aan de code aan zien te passen waardoor de treinen van een bepaalde richting niet op hetzelfde spoor rijden als van een andere richting

        if self.route:
            next_station = self.route[0]
            distance_to_next_station = abs(next_station - self.location)

            if distance_to_next_station >= self.speed_distance:

                #check if the new location is already used:
                new_location = self.location + self.speed_distance
                if new_location not in train_locations.values():
                    self.location = new_location  # move train
                    train_locations[self.train_id] = self.location
                    print(f"Train {self.train_id} is at location {self.location} meters.")
                else:
                    print(f"Train {self.train_id} cannot move to location {new_location}.")
            else:
                # The train arrives at next station
                self.location = next_station
                self.route.pop(0)
                train_locations[self.train_id] = self.location
                print(f"Train {self.train_id} arrived at {next_station} meters.")
                #In deze situ hebben de stations onbeperkt peron capaciteit

    def increase_time(self):
        self.time += 10  # Increase time with 10 seconds

#hierin uiteindelijk de stations plaatsen
route_HS_IC = [500, 800, 1000] # in m
route_HS_spr = [500, 800, 1000] # in m
route_R_IC = [500, 800, 1000] # in m
route_R_spr = [500, 800, 1000] # in m

# Constraint toevoegen waardoor er niet meerdere treinen op dezelfde locatie kunnen zijn

#train data:
start_locations = ["HS", "HS", "HS"] # start location
traintype = ["IC", "IC", "IC"]
train_locations = {0:0, 1:0, 2:0}


def train_creator():
    trains = []

    for train in range(len(start_locations)):
        start_location = 0
        if start_locations[train] == "HS" and traintype[train] == "IC": # if the train from Den Haag HS to Rotterdam
            route = route_HS_IC
            speed_distance = 100 #Waardes hiervoor nog aanpassen
        elif start_locations[train] == "HS" and traintype[train] == "spr":
            route = route_HS_spr
            speed_distance = 100 #Waardes hiervoor nog aanpassen
        elif start_locations[train] == "R" and traintype[train] == "IC":
            route = route_R_IC
            speed_distance = 100 #Waardes hiervoor nog aanpassen
        else:
            route = route_R_spr
            speed_distance = 100 #Waardes hiervoor nog aanpassen

        trains.append(TRAIN(train, traintype[train], start_location, route, speed_distance))

    return trains


def run_simulation():
    # Simulation steps:
    num_steps = 10
    trains = train_creator()

    for step in range(num_steps):
        for train in trains:
            train.move(train_locations)
            train.increase_time()

    return

run_simulation()