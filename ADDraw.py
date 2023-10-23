import networkx as nx
import holoviews as hv
from bokeh.models import HoverTool, Button

def simulate(network, positions, train_locations):
    """
    Simulates the trains on the network
    :param network: Networkx graph
    :param positions: Dictionary with the positions of the nodes, created by get_node_dict()
    :param train_locations: List of dictionaries with keys 'train_id' and 'location'
    :return:
    """
    #Activate bokeh backend
    hv.extension('bokeh')
    #Create a holoviews graph from the networkx graph
    graph = hv.Graph.from_networkx(network, positions)
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

def sim(network, pos_param, train_locations):
    #Activate bokeh backend
    hv.extension('bokeh')
    # test = {(0, 0): 0, (0, 14400): 0, (0, 20600): 0}
    test2 = {'a': (0, 0), 'b': (0, 14400), 'c': (0, 20600)}
    # print(len(pos_param['0']))
    # print(len(test2['a']))
    print(dict_dims(pos_param), dict_dims(test2))
    print(pos_param)
    # print(pos_param['Rotterdam Centraal'], pos_param['Schiedam Centrum'])
    #Create a holoviews graph from the networkx graph
    graph = hv.Graph.from_networkx(network, pos_param)

    #Define a node position dictionary to use for the trains
    #trains = hv.Points(train_locations, vdims=['train_id', 'location']) #or kdims=['x', 'y']
    trains_test = hv.Points([(5, 200, 0), (5, 10000, 0), (15, 14000, 0)], vdims=['train_id', 'location'])

    #Define a hovertool to show the train_id and location
    hover = HoverTool(tooltips=[('train_id', '@train_id'), ('location', '@location')])
    # graph.opts(
    #     node_size=10,
    #     node_color='blue',
    #     edge_color='black',
    #     directed=True,
    #     arrowhead_length=0.01,
    #     arrowhead_angle=0,
    #     width=800,
    #     height=800,
    #     padding=0.1,
    #     xaxis=None,
    #     yaxis=None,
    #     show_frame=False,
    #     show_grid=False,
    #     show_legend=False,
    #     title='Railway Network',
    #     fontsize={'title': 16, 'labels': 12, 'xticks': 8, 'yticks': 8}
    # )

    graph_with_trains = graph * trains_test

    #Define a button to start the simulation
    button = Button(label="Start Simulation", button_type="success")

    #Create a dynamic map to update the train locations
    dynamic_plot = hv.DynamicMap(graph_with_trains, streams=[hv.streams.PlotReset(), hv.streams.PlotSize(), hv.streams.RangeXY(), hv.streams.Stream.define('NextFrame', None)()])
    layout = button + dynamic_plot


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
    node_dict = {}
    for (i, node) in enumerate(network.nodes):
        node_dict['n{}'.format(i)] = network.nodes[node]['pos']

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
