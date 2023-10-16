import networkx as nx

class RAIL_NETWORK():
    def __init__(self, network):
        self.network = network # Use the railway_network function to create a network

    def add_train(self, TRAIN):
        self.network.add_node[TRAIN.train_id]['Train'] = TRAIN

    def remove_train(self, TRAIN):
        self.network.remove_node[TRAIN.train_id]['Train'] = TRAIN

    def move_train(self, TRAIN, new_location):
        # Update the location of the train on the network
        self.network.node[TRAIN.train_id]['location'].location = new_location

    def update(self):
        for node_data in self.network.nodes(data=True):
            train = node_data['Train']
            current_location = node_data['location']

            train.move()
            new_location = train.location
            self.move_train(train, new_location)

            #here goes the stuff that does the train interactions
