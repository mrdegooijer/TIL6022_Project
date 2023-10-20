#in this python file we will create the physical elements of the simulation
#this starts with the railway track, stations and the trains

import numpy as np
import matplotlib.pyplot as plt
import random

from network import railway_network_current
railway_network = railway_network_current()
#from network import visualize_network
#graph = visualize_network(railway_network)


class TRAIN:
    def __init__(self, train_id, type, location, route, speed_distance, track):
        self.train_id = train_id
        self.type = type
        self.location = location
        self.route = route
        self.speed_distance = speed_distance # speed in meter (per time step of 10s)
        self.track = track
        self.time = 0


    def move(self, track_1, track_2, track_3, track_4):
        if self.route:
            next_station = self.route[0]
            distance_to_next_station = abs(next_station - self.location)

            if distance_to_next_station >= abs(self.speed_distance):

                #check if there are already trains between the current location and the distance (distance in timesteps):
                distance = 3 #how many timesteps distance between two different trains
                new_location = self.location + self.speed_distance


                if self.track==3:  # self.speed_distance > 0
                    if any((new_location + distance * self.speed_distance) <= value <= new_location for value in track_3.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train
                        track_3[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters, on track {self.track}.")

                elif self.track==4:  # self.speed_distance > 0
                    if any((new_location + distance*self.speed_distance) <= value <= new_location for value in track_4.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train
                        track_4[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters, on track {self.track}.")


                elif self.track == 1:  # self.speed_distance <= 0
                    if any(new_location <= value <= (new_location + distance*self.speed_distance) for value in track_1.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train
                        track_1[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters, on track {self.track}, {self.speed_distance}.")

                elif self.track == 2: # self.speed_distance <= 0
                    if any(new_location <= value <= (new_location + distance*self.speed_distance) for value in track_2.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train
                        track_2[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters, on track {self.track}.")


            else:
                # The train arrives at next station
                self.location = next_station
                self.route.pop(0)

                if self.track == 1:
                    track_1[self.train_id] = self.location
                elif self.track == 2:
                    track_2[self.train_id] = self.location
                elif self.track == 3:
                    track_3[self.train_id] = self.location
                else:
                    track_4[self.train_id] = self.location

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


# dictionary with locations of trains within track. This is used to keep track of the current location of each train. Furthermore the start location on the track is determined with this dictionaries.
track_1 = {0:0, 1:0, 2:0}
track_2 = {}
track_3 = {}
track_4 = {}

#bij de switch: kijken naar de kortste dictionary, daarin zet je vervolgens de trein.

def train_creator():
    trains_direction_1 = []
    trains_direction_2 = []

    for train in range(len(start_locations)):

        #check in which track the train starts:
        if train in track_1:
            start_location = track_1[train]
            track = 1
        elif train in track_2:
            start_location = track_2[train]
            track = 2
        elif train in track_3:
            start_location = track_3[train]
            track = 3
        else:
            start_location = track_4[train]
            track = 4

        if start_locations[train] == "HS" and traintype[train] == "IC": # if the train from Den Haag HS to Rotterdam
            route = route_HS_IC
            speed = -300  # speed in meter (per time step of 10s)

            trains_direction_1.append(TRAIN(train, traintype[train], start_location, route, speed, track))

        elif start_locations[train] == "HS" and traintype[train] == "spr":
            route = route_HS_spr
            speed = -250  # speed in meter (per time step of 10s)

            trains_direction_1.append(TRAIN(train, traintype[train], start_location, route, speed, track))

        elif start_locations[train] == "R" and traintype[train] == "IC":
            route = route_R_IC
            speed = 300  # speed in meter (per time step of 10s)

            trains_direction_2.append(TRAIN(train, traintype[train], start_location, route, speed, track))

        else:
            route = route_R_spr
            speed = 250  # speed in meter (per time step of 10s)

            trains_direction_2.append(TRAIN(train, traintype[train], start_location, route, speed, track))

    return [trains_direction_1, trains_direction_2]


def run_simulation():
    # Simulation steps:
    num_steps = 10
    trains = train_creator()

    for step in range(num_steps):
        for train in trains[0]:
            train.move(track_1, track_2, track_3, track_4)
            train.increase_time()

        for train in trains[1]:
            train.move(track_1, track_2, track_3, track_4)
            train.increase_time()

    return

run_simulation()