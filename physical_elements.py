#in this python file we will create the physical elements of the simulation
#this starts with the railway track, stations and the trains

import numpy as np
import matplotlib.pyplot as plt
import random

from network import railway_network_current
railway_network = railway_network_current()
#from network import visualize_network
#graph = visualize_network(railway_network)


# Create a class for all different trains in the traject between Rotterdam and Den Haag HS
class TRAIN:
    def __init__(self, train_id, type, location, route, switches, speed_distance, track):
        self.train_id = train_id
        self.type = type
        self.location = location
        self.route = route
        self.switches = switches
        self.speed_distance = speed_distance # speed in meter (per time step of 10s)
        self.track = track


    def move(self, track_1, track_2, track_3, track_4):
        if self.route:
            next_station = self.route[0]
            next_switch = self.switches[0]
            distance_to_next_station = abs(next_station - self.location)
            distance_to_next_switch = abs(next_switch - self.location)

            distance = 3  # how many timesteps distance between two different trains

            # If the train is not near a station or near a switch point:
            if distance_to_next_station >= abs(self.speed_distance) and distance_to_next_switch >= abs(self.speed_distance):

                #check if there are already trains between the current location and the distance (distance in timesteps):
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
                        print(f"Train {self.train_id} is at location {self.location} meters, on track {self.track}.")

                elif self.track == 2: # self.speed_distance <= 0
                    if any(new_location <= value <= (new_location + distance*self.speed_distance) for value in track_2.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train
                        track_2[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters, on track {self.track}.")

            elif distance_to_next_station < abs(self.speed_distance):
                # The train arrives at next station
                # In this sitution, we assume unlimited platform capacity
                self.location = next_station
                self.route = self.route[1:]

                if self.track == 1:
                    self.station_reached(track_1)
                elif self.track == 2:
                    self.station_reached(track_2)
                elif self.track == 3:
                    self.station_reached(track_3)
                else:
                    self.station_reached(track_4)

                print(f"Train {self.train_id} arrived at {next_station} meters.")

            else:
                # The train passed at a switch point
                self.location += self.speed_distance

                self.switches = self.switches[1:]

                # In the function self.track_switch, it is checked whether there is space on the other track.
                # Furthermore there is checked whether the other track is quieter than the current one.
                # In that case the train will change tracks.
                if self.track == 1:
                    if any(self.location <= value <= (self.location + distance * self.speed_distance) for value in track_2.values()):
                        occupation = False  #if there is enough space on track 2
                    else:
                        occupation = True # in the case that there is enough space on track 2
                    self.track_switch(track_1, track_2, 2, occupation)

                elif self.track == 2:
                    if any(self.location <= value <= (self.location + distance * self.speed_distance) for value in track_1.values()):
                        occupation = False  #if there is enough space on track 1
                    else:
                        occupation = True # in the case that there is enough space on track 1
                    self.track_switch(track_2, track_1, 1, occupation)

                elif self.track == 3:
                    if any((self.location + distance * self.speed_distance) <= value <= self.location for value in track_4.values()):
                        occupation = False  #if there is enough space on track 4
                    else:
                        occupation = True # in the case that there is enough space on track 4
                    self.track_switch(track_3, track_4, 4, occupation)

                else:  # If the train is on track 4
                    if any((self.location + distance * self.speed_distance) <= value <= self.location for value in
                           track_3.values()):
                        occupation = False  # if there is enough space on track 3
                    else:
                        occupation = True  # in the case that there is enough space on track 3
                    self.track_switch(track_4, track_3, 3)


    def station_reached(self, track_name):  # This function is used if a train reaches a station. If the station is the end-station, the train is removed from its dictionary.
        if self.route:  # Self.route gives the value true if the train didn't reach the end station
           track_name[self.train_id] = self.location
        else:  # In the case that the train already reach the end station, the value is deleted from the dictionary
            del track_name[self.train_id]

    def track_switch(self, current_track, potential_track, potential_track_number, occupation):
        if len(current_track) > len(potential_track):  # in the case that the current track is bussier than the potential new track.
            # The train will switch track if there is space on the other track.
            if occupation:
                self.track = potential_track_number

                # move the train from the old track dictionary to the new track dictionary.
                del current_track[self.train_id]
                potential_track.update({self.train_id : self.location})

                print(f"Train {self.train_id} is switched to track {self.track}.")

            else:
                print(f"Train {self.train_id} stays on track {self.track} at {self.location} meters, because the potential new track is occupied.")

        else:
            print(f"Train {self.train_id} stays on track {self.track} at {self.location} meters.")


# At the following positions, it is possible to switch track. It is possible to switch between track 1 and 2 and it is possible to switch between track 3 and 4.
# The end stations are added as switchpoint. Otherwise the code will continue to search for a new switch point before the train reaches the final location.
switch_points_route_R = [railway_network.nodes["Switch 1"].get("pos")[1], railway_network.nodes["Switch 2"].get("pos")[1], railway_network.nodes["Switch 3"].get("pos")[1], railway_network.nodes["Switch 4"].get("pos")[1], railway_network.nodes["Switch 5"].get("pos")[1], railway_network.nodes["Switch 6"].get("pos")[1], railway_network.nodes["Den Haag HS"].get("pos")[1]]
switch_points_route_HS = [railway_network.nodes["Switch 6"].get("pos")[1], railway_network.nodes["Switch 5"].get("pos")[1], railway_network.nodes["Switch 4"].get("pos")[1], railway_network.nodes["Switch 3"].get("pos")[1], railway_network.nodes["Switch 2"].get("pos")[1], railway_network.nodes["Switch 1"].get("pos")[1], railway_network.nodes["Rotterdam Centraal"].get("pos")[1]]

route_HS_IC = [railway_network.nodes["Den Haag HS"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Rotterdam Centraal"].get("pos")[1]] # in m
route_HS_spr = [railway_network.nodes["Den Haag HS"].get("pos")[1], railway_network.nodes["Moerwijk"].get("pos")[1], railway_network.nodes["Rijswijk"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Delft Campus"].get("pos")[1], railway_network.nodes["Schiedam Centrum"].get("pos")[1], railway_network.nodes["Rotterdam Centraal"].get("pos")[1]] # in m
route_R_IC = [railway_network.nodes["Rotterdam Centraal"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Den Haag HS"].get("pos")[1]] # in m
route_R_spr = [railway_network.nodes["Rotterdam Centraal"].get("pos")[1], railway_network.nodes["Schiedam Centrum"].get("pos")[1], railway_network.nodes["Delft Campus"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Rijswijk"].get("pos")[1], railway_network.nodes["Moerwijk"].get("pos")[1], railway_network.nodes["Den Haag HS"].get("pos")[1]] # in m


#train data:
start_locations = ["R", "R", "R"]  # Determine the start location of each train. R is for trains from Rotterdam to Den Haag HS and HS is for trains in the other direction.
traintype = ["IC", "IC", "IC"]  # Determine the train type of all trains (IC or spr)
dep_time = [0, 0, 0]  # set departure time, in timesteps of 10 seconds

# dictionary with locations of trains within track.
# These are used to keep track of the current location of each train.
# Furthermore the start location on the track is determined within these dictionaries.
track_1 = {0:0, 1:0, 2:0}
track_2 = {}
track_3 = {}
track_4 = {}

# The following train


def train_creator(train_id):  # This function creates a train using the class TRAIN and the train_id as input
    #check in which track the train starts:
    if train_id in track_1:  # check if the train id exists in the dictionary track_1
        start_location = track_1[train_id]
        track = 1
    elif train_id in track_2:  # check if the train id exists in the dictionary track_2
        start_location = track_2[train_id]
        track = 2
    elif train_id in track_3:  # check if the train id exists in the dictionary track_3
        start_location = track_3[train_id]
        track = 3
    else:  # check if the train id exists in the dictionary track_4
        start_location = track_4[train_id]
        track = 4

    # if the train is an IC from Den Haag HS to Rotterdam, create the train with the correct route and speed
    if start_locations[train_id] == "HS" and traintype[train_id] == "IC":
        route = route_HS_IC
        switches = switch_points_route_HS
        speed = -300  # speed in meter (per time step of 10s) (negative speed because the route is from Den Haag HS to Rotterdam)
        train = TRAIN(train_id, traintype[train_id], start_location, route, switches, speed, track)  # Create train with all specifications

    # if the train is a sprinter from Den Haag HS to Rotterdam, create the train with the correct route and speed
    elif start_locations[train_id] == "HS" and traintype[train_id] == "spr":
        route = route_HS_spr
        switches = switch_points_route_HS
        speed = -250  # speed in meter (per time step of 10s)
        train = TRAIN(train_id, traintype[train_id], start_location, route, switches, speed, track)  # Create train with all specifications

    # if the train is an IC from Rotterdam to Den Haag HS, create the train with the correct route and speed
    elif start_locations[train_id] == "R" and traintype[train_id] == "IC":
        route = route_R_IC
        switches = switch_points_route_R
        speed = 300  # speed in meter (per time step of 10s)
        train = TRAIN(train_id, traintype[train_id], start_location, route, switches, speed, track)  # Create train with all specifications

    # if the train is an sprinter from Rotterdam to Den Haag HS, create the train with the correct route and speed
    else:
        route = route_R_spr
        switches = switch_points_route_R
        speed = 250  # speed in meter (per time step of 10s)
        train = TRAIN(train_id, traintype[train_id], start_location, route, switches, speed, track)  # Create train with all specifications
    return [train]


def run_simulation():  # This function is used for running the simulation.
    num_steps = 100  # Number of simulation steps (of 10s) is defined
    current_trains = []
    time = 0
    data_output = []

    for step in range(num_steps):
        for train_id in range(len(start_locations)):
            if dep_time[train_id] == step: # The train joins the simulation at the start time as defined in the list dep_time
                current_trains.append(train_creator(train_id))

        for train_list in current_trains:
            for train in train_list:
                train.move(track_1, track_2, track_3, track_4)
                #train.increase_time()
        time += 10  # Increase time of the model with 10 seconds
        print(time)
        data_output.append(data_converter(track_1, track_2, track_3, track_4))
    return data_output


# Create a function which converts the train data to the correct format for the visualization.
# The data from the different track dictionaries is converted into the folllowing form: [(x1.1, y1.1), (x1.2, y1.2), …]
def data_converter(track_1, track_2, track_3, track_4):
    data = []
    def single_train(track, x_value_track): # this function converts the value of a single train to the correct format
        result = [(x_value_track, value) for value in track.values()]
        return result

    data.extend(single_train(track_1, -15))
    data.extend(single_train(track_2, -5))
    data.extend(single_train(track_3, 5))
    data.extend(single_train(track_4, 15))
    return (data)


# print the output
print(run_simulation())