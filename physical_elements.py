#in this python file we will create the physical elements of the simulation
#this starts with the railway track, stations and the trains

import numpy as np
import networkx as nx
from mesa.space import NetworkGrid
from mesa import Agent, Model

railway_network = nx.Graph()

#Creating the railway track
railway_network.add_node("Rotterdam Cetraal", pos = (0,0), platforms = 4, type = "station")
railway_





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





