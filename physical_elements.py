# in this python file we will create the physical elements of the simulation

# import important libraries:
import numpy as np
import matplotlib.pyplot as plt

from network import railway_network_current
railway_network = railway_network_current()

from exceltrains_to_code import get_train_data
train_data = get_train_data()


#.......................................... INPUT DATA.................................................................

# The train routes voor the train types Sprinter and Intercity in different directions are defined.

# Route from Den haag HS to Rotterdam:
route_HS_IC = [railway_network.nodes["Den Haag HS"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1],
               railway_network.nodes["Rotterdam Centraal"].get("pos")[1]]  # Give distance of the stations in meters.

route_HS_spr = [railway_network.nodes["Den Haag HS"].get("pos")[1], railway_network.nodes["Moerwijk"].get("pos")[1],
                railway_network.nodes["Rijswijk"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1],
                railway_network.nodes["Delft Campus"].get("pos")[1],
                railway_network.nodes["Schiedam Centrum"].get("pos")[1],
                railway_network.nodes["Rotterdam Centraal"].get("pos")[1]]  # Give distance of the stations in meters.

# Route from Rotterdam to Den Haag HS:
route_R_IC = [railway_network.nodes["Rotterdam Centraal"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1],
              railway_network.nodes["Den Haag HS"].get("pos")[1]]  # Give distance of the stations in meters.

route_R_spr = [railway_network.nodes["Rotterdam Centraal"].get("pos")[1],
               railway_network.nodes["Schiedam Centrum"].get("pos")[1],
               railway_network.nodes["Delft Campus"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1],
               railway_network.nodes["Rijswijk"].get("pos")[1], railway_network.nodes["Moerwijk"].get("pos")[1],
               railway_network.nodes["Den Haag HS"].get("pos")[1]]  # Give distance of the stations in meters.


# At the following positions, it is possible to switch track.
# It is possible to switch between track 1 and 2 and it is possible to switch between track 3 and 4.
# The end stations are added as switchpoint.
# Otherwise the code will continue to search for a new switch point before the train reaches the final location.

switch_points_route_R = [railway_network.nodes["Switch 1"].get("pos")[1],  # Switch in route from Rotterdam to DH HS
                         railway_network.nodes["Switch 2"].get("pos")[1],
                         railway_network.nodes["Switch 3"].get("pos")[1],
                         railway_network.nodes["Switch 4"].get("pos")[1],
                         railway_network.nodes["Switch 5"].get("pos")[1],
                         railway_network.nodes["Switch 6"].get("pos")[1],
                         railway_network.nodes["Den Haag HS"].get("pos")[1]
                         ]

switch_points_route_HS = [railway_network.nodes["Switch 6"].get("pos")[1],  # Switch in route from DH HS to Rotterdam
                          railway_network.nodes["Switch 5"].get("pos")[1],
                          railway_network.nodes["Switch 4"].get("pos")[1],
                          railway_network.nodes["Switch 3"].get("pos")[1],
                          railway_network.nodes["Switch 2"].get("pos")[1],
                          railway_network.nodes["Switch 1"].get("pos")[1],
                          railway_network.nodes["Rotterdam Centraal"].get("pos")[1]
                          ]


# The following variable indicates the minimum distance between two trains on the same track (indicated in timesteps):
distance = 1  # There is chosen for a minimum distance of 30 seconds (1 timestep)

# The following speeds are used for the trains:
speed_IC = 900  # Speed of an Intercity (in meter per time step of 30s)
speed_spr = 750  # Speed of a Sprinter (in meter per time step of 30s)

# The train data for the NS timetable is now imported and placed in the correct variables.


# The list start_locations determines the start location of each train.
# R is for trains from Rotterdam to Den Haag HS and HS is for trains in the other direction.
start_locations = train_data['start_locations']

# The following list contains the train types of all trains (IC or spr).
traintype = train_data['traintypes']

# The following list, the departure times of the different trains are set (in timesteps of 30 seconds).
dep_time = train_data['departure_steps']

# The following dictionaries contain the locations of all trains within the different tracks.
# These are used to keep track of the current location of each train.
# Furthermore the start locations on the tracks are determined within these dictionaries.
track_1 = train_data['track_1']
track_2 = train_data['track_2']
track_3 = train_data['track_3']
track_4 = train_data['track_4']


#.......................................... DEFINE TRAIN CLASS........................................................

# Create a class for all different trains in the traject between Rotterdam and Den Haag HS:
class TRAIN:
    def __init__(self, train_id, type, location, route, switches, speed_distance, track):
        self.train_id = train_id
        self.type = type
        self.location = location
        self.route = route
        self.switches = switches
        self.speed_distance = speed_distance  # speed in meter (per time step of 30s).
        self.track = track


    # The move function is used to move the trains at one timestep (of 30 seconds)
    def move(self, track_1, track_2, track_3, track_4):
        if self.route:
            next_station = self.route[0]
            next_switch = self.switches[0]
            distance_to_next_station = abs(next_station - self.location)
            distance_to_next_switch = abs(next_switch - self.location)

            # If the train is not near a station or near a switch point:
            if distance_to_next_station >= abs(self.speed_distance) and distance_to_next_switch >= abs(
                    self.speed_distance):
                new_location = self.location + self.speed_distance  # Define new location of the train.

                # Check if there are already trains between the current location and
                # the required distance between trains (distance in timesteps).
                # If there is space, the train will move to new_location

                if self.track == 1:  # Train on track 1; self.speed_distance <= 0
                    if any(new_location <= value <= (new_location + distance*self.speed_distance) for value in
                           track_1.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train to new_location.
                        track_1[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters, on track {self.track}.")

                elif self.track == 2: # Train on track 2; self.speed_distance <= 0
                    if any(new_location <= value <= (new_location + distance*self.speed_distance) for value in
                           track_2.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train to new_location.
                        track_2[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters, on track {self.track}.")

                elif self.track==3:  # Train on track 3; self.speed_distance > 0
                    if any((new_location + distance * self.speed_distance) <= value <= new_location for value in
                           track_3.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train to new_location.
                        track_3[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters, on track {self.track}.")

                elif self.track==4:  # Train on track 4; self.speed_distance > 0
                    if any((new_location + distance * self.speed_distance) <= value <= new_location for value in
                           track_4.values()):
                        print(f"Train {self.train_id} cannot move to location {new_location}.")
                    else:
                        self.location = new_location  # move train to new_location.
                        track_4[self.train_id] = self.location
                        print(f"Train {self.train_id} is at location {self.location} meters, on track {self.track}.")


            # If the train is near the next station:
            elif distance_to_next_station < abs(self.speed_distance):
                # The train arrives at next station.
                self.location = next_station
                self.route = self.route[1:]  # The location of the current station is deleted from self.route.

                # The function self.station_reached checks if the station is the end station.
                if self.track == 1:
                    self.station_reached(track_1)
                elif self.track == 2:
                    self.station_reached(track_2)
                elif self.track == 3:
                    self.station_reached(track_3)
                else:
                    self.station_reached(track_4)

                print(f"Train {self.train_id} arrived at {next_station} meters.")


            else:  # The train passed a switch point.
                self.location += self.speed_distance

                # In the function self.track_switch, it is checked whether there is space on the other track.
                # Furthermore there is checked whether the other track is quieter than the current one.
                # In that case the train will change tracks.
                if self.track == 1:
                    if self.double_track():  # gives True if there is double track after the switch
                        if any(self.location <= value <= (self.location + distance * self.speed_distance) for value in track_2.values()):
                            # There is not enough space on track 2.
                            # The train stays on the current track.
                            occupation = False  # if there is not enough space on track 2, the variable occupation becomes False
                        else:  # There is enough space on track 2.
                            occupation = True

                        self.switches = self.switches[1:]
                        self.track_switch(track_1, track_2, 2, occupation)

                    else:  # in the situation, there is only single track after the switch:
                        # It is now being examined whether there is sufficient space on the new track.
                        # Otherwise the train has to wait before it can change tracks.
                        if any(self.location <= value <= (self.location + distance * self.speed_distance) for value in track_2.values()):
                            # There is not enough space on track 2, the train has to wait.
                            self.location -= self.speed_distance  # The train will remain at the old location and the location change is made undone.
                            print(f"Train {self.train_id} has to wait at the switch point, because new track is occupied.")

                        else: # There is enough space on track 2.
                            self.switches = self.switches[1:]

                            # The train changes track to track 2:
                            self.track = 2

                            # move the train from the old track dictionary to the new track dictionary.
                            del track_1[self.train_id]
                            track_2.update({self.train_id: self.location})

                            print(f"Train {self.train_id} is switched to track {self.track}.")

                elif self.track == 2:
                    if self.double_track():  # gives True if there is double track after the switch
                        if any(self.location <= value <= (self.location + distance * self.speed_distance) for value in track_1.values()):
                            occupation = False  #if there is not enough space on track 1, the train stays on track 2
                        else:
                            occupation = True  # in the case that there is enough space on track 1
                        self.track_switch(track_2, track_1, 1, occupation)

                    else: # in this situation, there is only single track after the switch:
                        print(f"Train {self.train_id} stays on track at the switch point, because there is only single track.")
                        # The train has to stay on the current track.

                    self.switches = self.switches[1:]

                elif self.track == 3:
                    if self.double_track():  # gives True if there is double track after the switch
                        if any((self.location + distance * self.speed_distance) <= value <= self.location for value in track_4.values()):
                            occupation = False  # if there is not enough space on track 4, the train stays on track 3
                        else:
                            occupation = True # in the case that there is enough space on track 4
                        self.track_switch(track_3, track_4, 4, occupation)

                    else: # in this situation, there is only single track after the switch:
                        print(f"Train {self.train_id} stays on track at the switch point, because there is only single track.")

                        # The train has to stay on the current track.

                    self.switches = self.switches[1:]


                else:  # If the train is on track 4
                    if self.double_track():  # gives True if there is double track after the switch
                        if any((self.location + distance * self.speed_distance) <= value <= self.location for value in
                               track_3.values()):
                            # There is not enough space on track 3.
                            # The train stays on the current track.
                            occupation = False  # if there is not enough space on track 3, the variable occupation becomes False
                        else:  # There is enough space on track 3.
                            occupation = True

                        self.switches = self.switches[1:]
                        self.track_switch(track_4, track_3, 3, occupation)

                    else:  # in the situation, there is only single track after the switch:
                        # It is now being examined whether there is sufficient space on the new track.
                        # Otherwise the train has to wait before it can change tracks.
                        if any((self.location + distance * self.speed_distance) <= value <= self.location for value in
                               track_3.values()):                            # There is not enough space on track 2, the train has to wait.
                            self.location -= self.speed_distance  # The train will remain at the old location and the location change is made undone.
                            print(f"Train {self.train_id} has to wait at the switch point, because new track is occupied.")

                        else: # There is enough space on track 3.
                            self.switches = self.switches[1:]

                            # The train changes track to track 3:
                            self.track = 3

                            # move the train from the old track dictionary to the new track dictionary.
                            del track_4[self.train_id]
                            track_3.update({self.train_id: self.location})

                            print(f"Train {self.train_id} is switched to track {self.track}.")

    def station_reached(self, track_name):
    # The function station_reached is used if a train reaches a station.
    # If the station is the end-station, the train is removed from its dictionary.

        if self.route:  # Self.route gives the value True if the train didn't reach the end station.
           track_name[self.train_id] = self.location  # Change the train location in the dictionary.
        else:  # In the case that the train reaches the end station, the value is deleted from the dictionary.
            del track_name[self.train_id]


    def track_switch(self, current_track, potential_track, potential_track_number, occupation):
        # This function is used in the situation where there is double track.
        # The function determines whether the train stays on its current track or switches tracks.

        if len(current_track) > len(potential_track):
            # In the case that the current track is bussier than the potential new track,
            # the train will switch track if there is space on the other track.
            if occupation:
                self.track = potential_track_number

                # move the train from the old track dictionary to the new track dictionary.
                del current_track[self.train_id]
                potential_track.update({self.train_id : self.location})

                print(f"Train {self.train_id} is switched to track {self.track}.")

            else:  # The potential track is occupied.
                print(f"Train {self.train_id} stays on track at the switch point, because the potential new track"
                      f" is occupied.")

        else:  # If the other track is bussier than the current track.
            print(f"Train {self.train_id} stays on track {self.track} at {self.location} meters.")


    def double_track(self):
        # This function checks if there are 2 tracks in the same direction after the switch.
        if railway_network.nodes["Switch 2"].get("pos")[1] <= self.location <= railway_network.nodes["Switch 5"].get("pos")[1]:
            two_tracks = False
        else:
            two_tracks = True
        # Outputs True if there are 2 tracks between the determined switch points.
        return two_tracks





def train_creator(train_id):
# This function creates a train using the class TRAIN and the train_id as input.

    # First, check in which track the train starts:
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

# Then, check
    # if the train is an IC from Den Haag HS to Rotterdam, create the train with the correct route and speed
    if start_locations[train_id] == "HS" and traintype[train_id] == "IC":
        route = route_HS_IC
        switches = switch_points_route_HS
        speed = -speed_IC  # speed in meter (per time step of 30s) (negative speed because the route is from Den Haag HS to Rotterdam)
        train = TRAIN(train_id, traintype[train_id], start_location, route, switches, speed, track)  # Create train with all specifications

    # if the train is a sprinter from Den Haag HS to Rotterdam, create the train with the correct route and speed
    elif start_locations[train_id] == "HS" and traintype[train_id] == "spr":
        route = route_HS_spr
        switches = switch_points_route_HS
        speed = -speed_spr  # speed in meter (per time step of 30s)
        train = TRAIN(train_id, traintype[train_id], start_location, route, switches, speed, track)  # Create train with all specifications

    # if the train is an IC from Rotterdam to Den Haag HS, create the train with the correct route and speed
    elif start_locations[train_id] == "R" and traintype[train_id] == "IC":
        route = route_R_IC
        switches = switch_points_route_R
        speed = speed_IC  # speed in meter (per time step of 30s)
        train = TRAIN(train_id, traintype[train_id], start_location, route, switches, speed, track)  # Create train with all specifications

    # if the train is an sprinter from Rotterdam to Den Haag HS, create the train with the correct route and speed
    else:
        route = route_R_spr
        switches = switch_points_route_R
        speed = speed_spr  # speed in meter (per time step of 30s)
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
        time += 30  # Increase time of the model with 30 seconds
        print(time)
        data_output.append(data_converter(track_1, track_2, track_3, track_4))
    return data_output


def data_converter(track_1, track_2, track_3, track_4):
    # This function converts the train data to the correct format for the visualization.
    # The data from the different track dictionaries is converted into the folllowing form:
    # [(x1.1, y1.1), (x1.2, y1.2), …]

    data = []

    def single_train(track, x_value_track): # this function converts the value of a single train to the correct format.
        result = [(x_value_track, value) for value in track.values()]
        return result

    data.extend(single_train(track_1, 15))
    data.extend(single_train(track_2, 5))
    data.extend(single_train(track_3, -5))
    data.extend(single_train(track_4, -15))
    return (data)


# print the output
print(run_simulation())