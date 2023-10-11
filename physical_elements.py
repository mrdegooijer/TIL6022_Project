#in this python file we will create the physical elements of the simulation
#this starts with the railway track, stations and the trains

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mesa.space import NetworkGrid
from mesa import Agent, Model

railway_network = nx.DiGraph()

#Creating the railway track
railway_network.add_node("Rotterdam Centraal", pos = (0,0), platforms = 4, type = "station")
railway_network.add_node("Schiedam Centrum", pos = (0, 4.0), platforms = 4, type = "station")
railway_network.add_node("Delft Campus", pos = (0, 12.5), platforms = 2, type = "station")
railway_network.add_node("Delft", pos = (0, 14.4), platforms = 2, type = "station")
railway_network.add_node("Rijswijk", pos = (0, 18.7), platforms = 4, type = "station")
railway_network.add_node("Moerwijk", pos = (0, 20.6), platforms = 4, type = "station")
railway_network.add_node("Den Haag HS", pos = (0, 22.6), platforms = 4, type = "station")

railway_network.add_node("Switch 1", pos = (0, 2.1), type = "switch")
railway_network.add_node("Switch 2", pos = (0, 4.5), type = "switch")
railway_network.add_node("Switch 3", pos = (0, 11), type = "switch")
railway_network.add_node("Switch 4", pos = (0, 12.8), type = "switch")
railway_network.add_node("Switch 5", pos = (0, 16.9), type = "switch")
railway_network.add_node("Switch 6", pos = (0, 21.2), type = "switch")

#Creating the edges, they are monodirectional
railway_network.add_edge("Rotterdam Centraal", "Switch 1", length = 2.1, type = "track")
railway_network.add_edge("Rotterdam Centraal", "Switch 1", length = 2.1, type = "track")
railway_network.add_edge("Switch 1", "Schiedam Centrum", length = 1.9, type = "track")
railway_network.add_edge("Switch 1", "Schiedam Centrum", length = 1.9, type = "track")
railway_network.add_edge("Schiedam Centrum", "Switch 2", length = 0.4, type = "track")
railway_network.add_edge("Schiedam Centrum", "Switch 2", length = 0.4, type = "track")
railway_network.add_edge("Switch 2", "Switch 3", length = 6.5, type = "track")
railway_network.add_edge("Switch 3", "Delft Campus", length = 1.5, type = "track")
railway_network.add_edge("Delft Campus", "Switch 4", length = 0.3, type = "track")
railway_network.add_edge("Switch 4", "Delft", length = 1.6, type = "track")
railway_network.add_edge("Delft", "Switch 5", length = 2.5, type = "track")
railway_network.add_edge("Switch 5", "Rijswijk", length = 1.8, type = "track")
railway_network.add_edge("Switch 5", "Rijswijk", length = 1.8, type = "track")
railway_network.add_edge("Rijswijk", "Moerwijk", length = 1.9, type = "track")
railway_network.add_edge("Rijswijk", "Moerwijk", length = 1.9, type = "track")
railway_network.add_edge("Moerwijk", "Switch 6", length = 0.6, type = "track")
railway_network.add_edge("Moerwijk", "Switch 6", length = 0.6, type = "track")
railway_network.add_edge("Switch 6", "Den Haag HS", length = 1.4, type = "track")
railway_network.add_edge("Switch 6", "Den Haag HS", length = 1.4, type = "track")

#Creating the edges, in reverse of the previous edges
railway_network.add_edge("Switch 1", "Rotterdam Centraal", length = 2.1, type = "track")
railway_network.add_edge("Switch 1", "Rotterdam Centraal", length = 2.1, type = "track")
railway_network.add_edge("Schiedam Centrum", "Switch 1", length = 1.9, type = "track")
railway_network.add_edge("Schiedam Centrum", "Switch 1", length = 1.9, type = "track")
railway_network.add_edge("Switch 2", "Schiedam Centrum", length = 0.4, type = "track")
railway_network.add_edge("Switch 2", "Schiedam Centrum", length = 0.4, type = "track")
railway_network.add_edge("Switch 3", "Switch 2", length = 6.5, type = "track")
railway_network.add_edge("Delft Campus", "Switch 3", length = 1.5, type = "track")
railway_network.add_edge("Switch 4", "Delft Campus", length = 0.3, type = "track")
railway_network.add_edge("Delft", "Switch 4", length = 1.6, type = "track")
railway_network.add_edge("Switch 5", "Delft", length = 2.5, type = "track")
railway_network.add_edge("Rijswijk", "Switch 5", length = 1.8, type = "track")
railway_network.add_edge("Rijswijk", "Switch 5", length = 1.8, type = "track")
railway_network.add_edge("Moerwijk", "Rijswijk", length = 1.9, type = "track")
railway_network.add_edge("Moerwijk", "Rijswijk", length = 1.9, type = "track")
railway_network.add_edge("Switch 6", "Moerwijk", length = 0.6, type = "track")
railway_network.add_edge("Switch 6", "Moerwijk", length = 0.6, type = "track")
railway_network.add_edge("Den Haag HS", "Switch 6", length = 1.4, type = "track")
railway_network.add_edge("Den Haag HS", "Switch 6", length = 1.4, type = "track")


#Creating the future situation
railway_network_new = nx.DiGraph()

#Creating the railway track
railway_network.add_node("Rotterdam Centraal", pos = (0,0), platforms = 4, type = "station")
railway_network.add_node("Schiedam Centrum", pos = (0, 4.0), platforms = 4, type = "station")
railway_network.add_node("Delft Campus", pos = (0, 12.5), platforms = 2, type = "station")
railway_network.add_node("Delft", pos = (0, 14.4), platforms = 2, type = "station")
railway_network.add_node("Rijswijk", pos = (0, 18.7), platforms = 4, type = "station")
railway_network.add_node("Moerwijk", pos = (0, 20.6), platforms = 4, type = "station")
railway_network.add_node("Den Haag HS", pos = (0, 22.6), platforms = 4, type = "station")

railway_network.add_node("Switch 1", pos = (0, 2.1), type = "switch")
railway_network.add_node("Switch 2", pos = (0, 4.5), type = "switch")
railway_network.add_node("Switch 3", pos = (0, 11), type = "switch")
railway_network.add_node("Switch 4", pos = (0, 12.8), type = "switch")
railway_network.add_node("Switch 5", pos = (0, 16.9), type = "switch")
railway_network.add_node("Switch 6", pos = (0, 21.2), type = "switch")

#Creating the edges, they are monodirectional
railway_network.add_edge("Rotterdam Centraal", "Switch 1", length = 2.1, type = "track")
railway_network.add_edge("Rotterdam Centraal", "Switch 1", length = 2.1, type = "track")
railway_network.add_edge("Switch 1", "Schiedam Centrum", length = 1.9, type = "track")
railway_network.add_edge("Switch 1", "Schiedam Centrum", length = 1.9, type = "track")
railway_network.add_edge("Schiedam Centrum", "Switch 2", length = 0.4, type = "track")
railway_network.add_edge("Schiedam Centrum", "Switch 2", length = 0.4, type = "track")
railway_network.add_edge("Switch 2", "Switch 3", length = 6.5, type = "track")
railway_network.add_edge("Switch 2", "Switch 3", length = 6.5, type = "track")
railway_network.add_edge("Switch 3", "Delft Campus", length = 1.5, type = "track")
railway_network.add_edge("Switch 3", "Delft Campus", length = 1.5, type = "track")
railway_network.add_edge("Delft Campus", "Switch 4", length = 0.3, type = "track")
railway_network.add_edge("Delft Campus", "Switch 4", length = 0.3, type = "track")
railway_network.add_edge("Switch 4", "Delft", length = 1.6, type = "track")
railway_network.add_edge("Switch 4", "Delft", length = 1.6, type = "track")
railway_network.add_edge("Delft", "Switch 5", length = 2.5, type = "track")
railway_network.add_edge("Delft", "Switch 5", length = 2.5, type = "track")
railway_network.add_edge("Switch 5", "Rijswijk", length = 1.8, type = "track")
railway_network.add_edge("Switch 5", "Rijswijk", length = 1.8, type = "track")
railway_network.add_edge("Rijswijk", "Moerdijk", length = 1.9, type = "track")
railway_network.add_edge("Rijswijk", "Moerdijk", length = 1.9, type = "track")
railway_network.add_edge("Moerdijk", "Switch 6", length = 0.6, type = "track")
railway_network.add_edge("Moerdijk", "Switch 6", length = 0.6, type = "track")
railway_network.add_edge("Switch 6", "Den Haag HS", length = 1.4, type = "track")
railway_network.add_edge("Switch 6", "Den Haag HS", length = 1.4, type = "track")

#Creating the edges, in reverse of the previous edges
railway_network.add_edge("Switch 1", "Rotterdam Centraal", length = 2.1, type = "track")
railway_network.add_edge("Switch 1", "Rotterdam Centraal", length = 2.1, type = "track")
railway_network.add_edge("Schiedam Centrum", "Switch 1", length = 1.9, type = "track")
railway_network.add_edge("Schiedam Centrum", "Switch 1", length = 1.9, type = "track")
railway_network.add_edge("Switch 2", "Schiedam Centrum", length = 0.4, type = "track")
railway_network.add_edge("Switch 2", "Schiedam Centrum", length = 0.4, type = "track")
railway_network.add_edge("Switch 3", "Switch 2", length = 6.5, type = "track")
railway_network.add_edge("Switch 3", "Switch 2", length = 6.5, type = "track")
railway_network.add_edge("Delft Campus", "Switch 3", length = 1.5, type = "track")
railway_network.add_edge("Delft Campus", "Switch 3", length = 1.5, type = "track")
railway_network.add_edge("Switch 4", "Delft Campus", length = 0.3, type = "track")
railway_network.add_edge("Switch 4", "Delft Campus", length = 0.3, type = "track")
railway_network.add_edge("Delft", "Switch 4", length = 1.6, type = "track")
railway_network.add_edge("Delft", "Switch 4", length = 1.6, type = "track")
railway_network.add_edge("Switch 5", "Delft", length = 2.5, type = "track")
railway_network.add_edge("Switch 5", "Delft", length = 2.5, type = "track")
railway_network.add_edge("Rijswijk", "Switch 5", length = 1.8, type = "track")
railway_network.add_edge("Rijswijk", "Switch 5", length = 1.8, type = "track")
railway_network.add_edge("Switch 6", "Rijswijk", length = 1.9, type = "track")
railway_network.add_edge("Switch 6", "Rijswijk", length = 1.9, type = "track")
railway_network.add_edge("Moerdijk", "Switch 6", length = 0.6, type = "track")
railway_network.add_edge("Moerdijk", "Switch 6", length = 0.6, type = "track")
railway_network.add_edge("Den Haag HS", "Switch 6", length = 1.4, type = "track")
railway_network.add_edge("Den Haag HS", "Switch 6", length = 1.4, type = "track")


#Drawing the railway network
pos = nx.spring_layout(railway_network)
nx.draw(railway_network, pos, with_labels = True)

for edge in railway_network.edges(data=True):
    source, target, data = edge
    length = data.get("length", 1)  # Default length is 1 if not specified
    max_speed = data.get("max_speed", 1)  # Default max speed is 1 if not specified
    label = f"Length: {length}\nMax Speed: {max_speed}"
    nx.draw_networkx_edges(railway_network, pos, edgelist=[(source, target)], width=2, label=label)


plt.show()





class STATION:
    def __init__(self, name,  location, platforms):
        self.name = name
        self.location = location
        self.platforms = platforms


class TRAIN:
    def __init__(self, train_id, type, location, destination, speed, acceleration, deceleration):
        self.train_id = train_id
        self.type = type
        self.location = location
        self.direction = direction
        self.speed = speed
        self.acceleration = acceleration
        self.deceleration = deceleration





