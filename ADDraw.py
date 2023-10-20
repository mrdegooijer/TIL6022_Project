import networkx as nx
import holoviews as hv
from bokeh.models import HoverTool, Button

def draw(network):
    pos = nx.spring_layout(network, dim=2, k=0.5)
    print(pos)

    node_points = hv.Points(list(pos.values()))
    node_points = node_points.redim(x = 'x', y = 'y')

    hv_graph = hv.Graph.from_networkx(network, node_points)
    graph_with_nodes = hv_graph * node_points

    hv_graph.opts(
        node_size=10,
        node_color='blue',
        edge_color='black',
        directed=True,
        arrowhead_length=0.01,
        arrowhead_angle=0,
        width=800,
        height=800,
        padding=0.1,
        xaxis=None,
        yaxis=None,
        show_frame=False,
        show_grid=False,
        show_legend=False,
        title='Railway Network',
        fontsize={'title': 16, 'labels': 12, 'xticks': 8, 'yticks': 8}
    )
    graph_with_nodes.show()
    hv.save(hv_graph, 'railway_network.html')
    hv_graph

    return

def sim(network, pos_param, train_locations):
    #Activate bokeh backend
    hv.extension('bokeh')
    test = [(0, 0, 0), (0, 14400, 0), (0, 20600, 0)]
    print(pos_param)
    #Create a holoviews graph from the networkx graph
    graph = hv.Graph.from_networkx(network, [(0, 0, 0), (0, 14400, 0), (0, 20600, 0)])

    #Define a node position dictionary to use for the trains
    trains = hv.Points(train_locations, vdims=['train_id', 'location']) #or kdims=['x', 'y']
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
