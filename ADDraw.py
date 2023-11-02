import networkx as nx
import holoviews as hv
from bokeh.models import HoverTool, Button
import matplotlib.pyplot as plt

def simulate(network, positions, train_locations):
    """
    Simulates the trains on the network
    :param network: Networkx graph
    :param positions: Dictionary with the positions of the nodes, created by get_node_dict()
    :param train_locations: List of dictionaries with keys 'train_id' and 'location'
    :return: graph
    """
    #Activate bokeh backend
    hv.extension('bokeh')

    #Create a holoviews graph from the networkx graph
    graph = hv.Graph.from_networkx(network, positionsk, nodes=)

    # print("vov", graph.data)
    #Define a node position dictionary to use for the trains
    trains = hv.Points(train_locations, kdims=['x', 'y'])

    #Define a hovertool to show the train_id and location
    hover = HoverTool(tooltips=[('train_id', '@train_id'), ('location', '@location')])
    #graph_with_trains = graph * trains

    #Create callable for plot function
    def locations(timestep):
        return hv.Points(train_locations[timestep])

    #Define a button to start the simulation
    #button = Button(label="Start Simulation", button_type="success")

    #Create a dynamic map to update the train locations
    train_dict = {i: locations(i) for i in range(len(train_locations))}
    map = hv.HoloMap(train_dict, kdims='Timestep')
    #view = map + graph
    return graph


def Convert_to_3D(network, z=0):
    """
    Converts a 2D network to a 3D network
    :param network: networkx graph 2D
    :param z: z-coordinate, default = 0
    :return: networkx graph 3D
    """

    for node in network.nodes:
        network.nodes[node]['pos'] = (network.nodes[node]['pos'][0], network.nodes[node]['pos'][1], z)

    return network

def get_3d_pos(network):
    """
    Returns the 3D positions of the nodes in the network
    :param network: networkx graph 3D
    :return: list of 3D positions
    """
    pos_dict = {}
    for node in network.nodes:
        pos_dict[node] = network.nodes[node]['pos']

    return pos_dict

def get_node_dict(network):
    """
    Returns a dictionary with the nodes and their coordinates
    :param network: networkx graph
    :return: dictionary with nodes and coordinates
    """

    #print(network.nodes)
    node_dict = {}
    for (i, node) in enumerate(network.nodes):
        try:
            node_dict['n{}'.format(i)] = network.nodes[node]['pos']
        except:
            print(node)

    return node_dict

def dict_dims(mydict):
    d1 = len(mydict)
    d2 = 0
    for d in mydict:
        if len(d) > d2:
            d2 = len(d)
            # print(d2, d)
        # d2 = max(d2, len(d))
    return d1, d2
