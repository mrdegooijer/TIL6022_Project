#in this python file we will create the physical elements of the simulation
#this starts with the railway track, stations and the trains

import numpy as np
import matplotlib.pyplot as plt


from network import railway_network_current
railway_network = railway_network_current()
#from network import visualize_network
#graph = visualize_network(railway_network)


class TRAIN:
    def __init__(self, train_id, type, location, route, speed_distance):
        self.train_id = train_id
        self.type = type
        self.location = location
        self.route = route
        self.speed_distance = speed_distance # speed in meter (per time step of 10s)
        self.time = 0


    def move(self, train_locations):
        if self.route:
            next_station = self.route[0]
            distance_to_next_station = abs(next_station - self.location)

            if distance_to_next_station >= abs(self.speed_distance):

                #check if the new location is already used:
                distance = 3 #how many timesteps distance between two different trains
                new_location = self.location + self.speed_distance

                #if new_location not in train_locations.values():
                if self.speed_distance > 0:
                    if any(new_location <= value <= (new_location + distance*self.speed_distance) for value in train_locations.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train
                        train_locations[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters.")

                else:
                    if any((new_location + distance*self.speed_distance) <= value <= new_location for value in train_locations.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train
                        train_locations[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters.")


            else:
                # The train arrives at next station
                self.location = next_station
                self.route.pop(0)
                train_locations[self.train_id] = self.location
                print(f"Train {self.train_id} arrived at {next_station} meters.")
                #In deze situatie hebben de stations onbeperkt perron capaciteit
                #ook nog ergens erbij zetten dat er een bepaalde stoptijd is bij de stations
    def increase_time(self):
        self.time += 10  # Increase time with 10 seconds


route_HS_IC = [railway_network.nodes["Den Haag HS"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Rotterdam Centraal"].get("pos")[1]] # in m
route_HS_spr = [railway_network.nodes["Den Haag HS"].get("pos")[1], railway_network.nodes["Moerwijk"].get("pos")[1], railway_network.nodes["Rijswijk"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Delft Campus"].get("pos")[1], railway_network.nodes["Schiedam Centrum"].get("pos")[1], railway_network.nodes["Rotterdam Centraal"].get("pos")[1]] # in m
route_R_IC = [railway_network.nodes["Rotterdam Centraal"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Den Haag HS"].get("pos")[1]] # in m
route_R_spr = [railway_network.nodes["Rotterdam Centraal"].get("pos")[1], railway_network.nodes["Schiedam Centrum"].get("pos")[1], railway_network.nodes["Delft Campus"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Rijswijk"].get("pos")[1], railway_network.nodes["Moerwijk"].get("pos")[1], railway_network.nodes["Den Haag HS"].get("pos")[1]] # in m


#train data:
start_locations = ["R", "R", "R"] # start location
traintype = ["IC", "IC", "IC"]

#train_locations is used to keep track of the current location of each train. Furthermore the start location on the track is determined from train_locations
train_locations = {0:0, 1:0, 2:0}



def train_creator():
    trains_direction_1 = []
    trains_direction_2 = []

    for train in range(len(start_locations)):
        if start_locations[train] == "HS" and traintype[train] == "IC": # if the train from Den Haag HS to Rotterdam
            route = route_HS_IC
            speed = -300  # speed in meter (per time step of 10s)
            trains_direction_1.append(TRAIN(train, traintype[train], train_locations[train], route, speed))

        elif start_locations[train] == "HS" and traintype[train] == "spr":
            route = route_HS_spr
            speed = -250  # speed in meter (per time step of 10s)
            trains_direction_1.append(TRAIN(train, traintype[train], train_locations[train], route, speed))

        elif start_locations[train] == "R" and traintype[train] == "IC":
            route = route_R_IC
            speed = 300  # speed in meter (per time step of 10s)
            trains_direction_2.append(TRAIN(train, traintype[train], train_locations[train], route, speed))

        else:
            route = route_R_spr
            speed = 250  # speed in meter (per time step of 10s)
            trains_direction_2.append(TRAIN(train, traintype[train], train_locations[train], route, speed))

    return [trains_direction_1, trains_direction_2]


def run_simulation():
    # Simulation steps:
    num_steps = 100
    trains = train_creator()

    for step in range(num_steps):
        for train in trains[0]:
            train.move(train_locations)
            train.increase_time()

        for train in trains[1]:
            train.move(train_locations)
            train.increase_time()

    return

run_simulation()
