import networkx as nx
import holoviews as hv

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


