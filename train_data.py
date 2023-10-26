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

# At the following positions, it is possible to switch track. It is possible to switch between track 1 and 2 and it is possible to switch between track 3 and 4.
switch_points_route_R = [railway_network.nodes["Switch 1"].get("pos")[1], railway_network.nodes["Switch 2"].get("pos")[1], railway_network.nodes["Switch 3"].get("pos")[1], railway_network.nodes["Switch 4"].get("pos")[1], railway_network.nodes["Switch 5"].get("pos")[1], railway_network.nodes["Switch 6"].get("pos")[1]]
switch_points_route_HS = [railway_network.nodes["Switch 6"].get("pos")[1], railway_network.nodes["Switch 5"].get("pos")[1], railway_network.nodes["Switch 4"].get("pos")[1], railway_network.nodes["Switch 3"].get("pos")[1], railway_network.nodes["Switch 2"].get("pos")[1], railway_network.nodes["Switch 1"].get("pos")[1]]

route_HS_IC = [railway_network.nodes["Den Haag HS"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Rotterdam Centraal"].get("pos")[1]] # in m
route_HS_spr = [railway_network.nodes["Den Haag HS"].get("pos")[1], railway_network.nodes["Moerwijk"].get("pos")[1], railway_network.nodes["Rijswijk"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Delft Campus"].get("pos")[1], railway_network.nodes["Schiedam Centrum"].get("pos")[1], railway_network.nodes["Rotterdam Centraal"].get("pos")[1]] # in m
route_R_IC = [railway_network.nodes["Rotterdam Centraal"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Den Haag HS"].get("pos")[1]] # in m
route_R_spr = [railway_network.nodes["Rotterdam Centraal"].get("pos")[1], railway_network.nodes["Schiedam Centrum"].get("pos")[1], railway_network.nodes["Delft Campus"].get("pos")[1], railway_network.nodes["Delft"].get("pos")[1], railway_network.nodes["Rijswijk"].get("pos")[1], railway_network.nodes["Moerwijk"].get("pos")[1], railway_network.nodes["Den Haag HS"].get("pos")[1]] # in m
