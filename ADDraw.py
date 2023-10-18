import networkx as nx
import holoviews as hv

def draw(network):
    hv_graph = hv.Graph.from_networkx(network, nx.layout.spring_layout, k=0.5)

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

    hv.save(hv_graph, 'railway_network.html')
    hv_graph

    return
