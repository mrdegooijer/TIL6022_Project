import networkx as nx
import matplotlib.pyplot as plt

def railway_network_current():
    railway_network = nx.DiGraph()

    # Add nodes - stations
    railway_network.add_node("Rotterdam Centraal", pos=(0, 0), platforms=4, type="station")
    railway_network.add_node("Schiedam Centrum", pos=(0, 4000), platforms=4, type="station")
    railway_network.add_node("Delft Campus", pos=(0, 12500), platforms=2, type="station")
    railway_network.add_node("Delft", pos=(0, 14400), platforms=2, type="station")
    railway_network.add_node("Rijswijk", pos=(0, 18700), platforms=4, type="station")
    railway_network.add_node("Moerwijk", pos=(0, 20600), platforms=4, type="station")
    railway_network.add_node("Den Haag HS", pos=(0, 22600), platforms=4, type="station")

    # Add nodes - switches
    railway_network.add_node("Switch 1", pos=(0, 2100), type="switch")
    railway_network.add_node("Switch 2", pos=(0, 4500), type="switch")
    railway_network.add_node("Switch 3", pos=(0, 11000), type="switch")
    railway_network.add_node("Switch 4", pos=(0, 12800), type="switch")
    railway_network.add_node("Switch 5", pos=(0, 16900), type="switch")
    railway_network.add_node("Switch 6", pos=(0, 21200), type="switch")

    # Add edges - Rotterdam to HS
    railway_network.add_edge("Rotterdam Centraal", "Switch 1", length=2100, type="track")
    railway_network.add_edge("Rotterdam Centraal", "Switch 1", length=2100, type="track")
    railway_network.add_edge("Switch 1", "Schiedam Centrum", length=1900, type="track")
    railway_network.add_edge("Switch 1", "Schiedam Centrum", length=1900, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 2", length=400, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 2", length=400, type="track")
    railway_network.add_edge("Switch 2", "Switch 3", length=6500, type="track")
    railway_network.add_edge("Switch 3", "Delft Campus", length=1500, type="track")
    railway_network.add_edge("Delft Campus", "Switch 4", length=300, type="track")
    railway_network.add_edge("Switch 4", "Delft", length=1600, type="track")
    railway_network.add_edge("Delft", "Switch 5", length=2500, type="track")
    railway_network.add_edge("Switch 5", "Rijswijk", length=1800, type="track")
    railway_network.add_edge("Switch 5", "Rijswijk", length=1800, type="track")
    railway_network.add_edge("Rijswijk", "Moerwijk", length=1900, type="track")
    railway_network.add_edge("Rijswijk", "Moerwijk", length=1900, type="track")
    railway_network.add_edge("Moerwijk", "Switch 6", length=600, type="track")
    railway_network.add_edge("Moerwijk", "Switch 6", length=600, type="track")
    railway_network.add_edge("Switch 6", "Den Haag HS", length=1400, type="track")
    railway_network.add_edge("Switch 6", "Den Haag HS", length=1400, type="track")

    # Add edges - HS to Rotterdam
    railway_network.add_edge("Switch 1", "Rotterdam Centraal", length=2100, type="track")
    railway_network.add_edge("Switch 1", "Rotterdam Centraal", length=2100, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 1", length=1900, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 1", length=1900, type="track")
    railway_network.add_edge("Switch 2", "Schiedam Centrum", length=400, type="track")
    railway_network.add_edge("Switch 2", "Schiedam Centrum", length=400, type="track")
    railway_network.add_edge("Switch 3", "Switch 2", length=6500, type="track")
    railway_network.add_edge("Delft Campus", "Switch 3", length=1500, type="track")
    railway_network.add_edge("Switch 4", "Delft Campus", length=300, type="track")
    railway_network.add_edge("Delft", "Switch 4", length=1600, type="track")
    railway_network.add_edge("Switch 5", "Delft", length=2500, type="track")
    railway_network.add_edge("Rijswijk", "Switch 5", length=1800, type="track")
    railway_network.add_edge("Rijswijk", "Switch 5", length=1800, type="track")
    railway_network.add_edge("Moerwijk", "Rijswijk", length=1900, type="track")
    railway_network.add_edge("Moerwijk", "Rijswijk", length=1900, type="track")
    railway_network.add_edge("Switch 6", "Moerwijk", length=600, type="track")
    railway_network.add_edge("Switch 6", "Moerwijk", length=600, type="track")
    railway_network.add_edge("Den Haag HS", "Switch 6", length=1400, type="track")
    railway_network.add_edge("Den Haag HS", "Switch 6", length=1400, type="track")

    return railway_network

def railway_network_future():
    railway_network = nx.DiGraph()

    # Add nodes - stations
    railway_network.add_node("Rotterdam Centraal", pos=(0, 0), platforms=4, type="station")
    railway_network.add_node("Schiedam Centrum", pos=(0, 4000), platforms=4, type="station")
    railway_network.add_node("Delft Campus", pos=(0, 12500), platforms=4, type="station")
    railway_network.add_node("Delft", pos=(0, 14400), platforms=4, type="station")
    railway_network.add_node("Rijswijk", pos=(0, 18700), platforms=4, type="station")
    railway_network.add_node("Moerwijk", pos=(0, 20600), platforms=4, type="station")
    railway_network.add_node("Den Haag HS", pos=(0, 22600), platforms=4, type="station")

    # Add nodes - switches
    railway_network.add_node("Switch 1", pos=(0, 2100), type="switch")
    railway_network.add_node("Switch 2", pos=(0, 4500), type="switch")
    railway_network.add_node("Switch 3", pos=(0, 11000), type="switch")
    railway_network.add_node("Switch 4", pos=(0, 12800), type="switch")
    railway_network.add_node("Switch 5", pos=(0, 16900), type="switch")
    railway_network.add_node("Switch 6", pos=(0, 21200), type="switch")

    # Add edges - Rotterdam to HS
    railway_network.add_edge("Rotterdam Centraal", "Switch 1", length=2100, type="track")
    railway_network.add_edge("Rotterdam Centraal", "Switch 1", length=2100, type="track")
    railway_network.add_edge("Switch 1", "Schiedam Centrum", length=1900, type="track")
    railway_network.add_edge("Switch 1", "Schiedam Centrum", length=1900, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 2", length=400, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 2", length=400, type="track")
    railway_network.add_edge("Switch 2", "Switch 3", length=6500, type="track")
    railway_network.add_edge("Switch 2", "Switch 3", length=6500, type="track")
    railway_network.add_edge("Switch 3", "Delft Campus", length=1500, type="track")
    railway_network.add_edge("Switch 3", "Delft Campus", length=1500, type="track")
    railway_network.add_edge("Delft Campus", "Switch 4", length=300, type="track")
    railway_network.add_edge("Delft Campus", "Switch 4", length=300, type="track")
    railway_network.add_edge("Switch 4", "Delft", length=1600, type="track")
    railway_network.add_edge("Switch 4", "Delft", length=1600, type="track")
    railway_network.add_edge("Delft", "Switch 5", length=2500, type="track")
    railway_network.add_edge("Delft", "Switch 5", length=2500, type="track")
    railway_network.add_edge("Switch 5", "Rijswijk", length=1800, type="track")
    railway_network.add_edge("Switch 5", "Rijswijk", length=1800, type="track")
    railway_network.add_edge("Rijswijk", "Moerwijk", length=1900, type="track")
    railway_network.add_edge("Rijswijk", "Moerwijk", length=1900, type="track")
    railway_network.add_edge("Moerwijk", "Switch 6", length=600, type="track")
    railway_network.add_edge("Moerwijk", "Switch 6", length=600, type="track")
    railway_network.add_edge("Switch 6", "Den Haag HS", length=1400, type="track")
    railway_network.add_edge("Switch 6", "Den Haag HS", length=1400, type="track")

    # Add edges - HS to Rotterdam
    railway_network.add_edge("Switch 1", "Rotterdam Centraal", length=2100, type="track")
    railway_network.add_edge("Switch 1", "Rotterdam Centraal", length=2100, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 1", length=1900, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 1", length=1900, type="track")
    railway_network.add_edge("Switch 2", "Schiedam Centrum", length=400, type="track")
    railway_network.add_edge("Switch 2", "Schiedam Centrum", length=400, type="track")
    railway_network.add_edge("Switch 3", "Switch 2", length=6500, type="track")
    railway_network.add_edge("Switch 3", "Switch 2", length=6500, type="track")
    railway_network.add_edge("Delft Campus", "Switch 3", length=1500, type="track")
    railway_network.add_edge("Delft Campus", "Switch 3", length=1500, type="track")
    railway_network.add_edge("Switch 4", "Delft Campus", length=300, type="track")
    railway_network.add_edge("Switch 4", "Delft Campus", length=300, type="track")
    railway_network.add_edge("Delft", "Switch 4", length=1600, type="track")
    railway_network.add_edge("Delft", "Switch 4", length=1600, type="track")
    railway_network.add_edge("Switch 5", "Delft", length=2500, type="track")
    railway_network.add_edge("Switch 5", "Delft", length=2500, type="track")
    railway_network.add_edge("Rijswijk", "Switch 5", length=1800, type="track")
    railway_network.add_edge("Rijswijk", "Switch 5", length=1800, type="track")
    railway_network.add_edge("Moerwijk", "Rijswijk", length=1900, type="track")
    railway_network.add_edge("Moerwijk", "Rijswijk", length=1900, type="track")
    railway_network.add_edge("Switch 6", "Moerwijk", length=600, type="track")
    railway_network.add_edge("Switch 6", "Moerwijk", length=600, type="track")
    railway_network.add_edge("Den Haag HS", "Switch 6", length=1400, type="track")
    railway_network.add_edge("Den Haag HS", "Switch 6", length=1400, type="track")

    return railway_network

def visualize_network(network):
    pos = nx.get_node_attributes(network, 'pos')
    labels = {node: node if network.nodes[node]['type'] != 'switch' else '' for node in network.nodes}

    # Define the figure size
    plt.figure(figsize=(6, 12))

    # Draw nodes
    node_size = [20 if network.nodes[node]['type'] == 'switch' else 200 for node in network.nodes]
    node_color = ['red' if network.nodes[node]['type'] == 'switch' else 'lightblue' for node in network.nodes]
    nx.draw_networkx_nodes(network, pos, node_size=node_size, node_color=node_color)

    # Draw edges
    #for edge in network.edges(data=True):
    #    if edge[2]['type'] == 'track':
    #        nx.draw_networkx_edges(network, pos, edgelist=[(edge[0], edge[1])], edge_color='gray')

    #edge_labels = {(edge[0], edge[1]): edge[2]['length'] for edge in network.edges(data=True) if
    #               edge[2]['type'] == 'track'}

    # Draw edges
    edge_labels = {}
    edge_colors = []
    for edge in network.edges(data=True):
        if edge[2]['type'] == 'track':
            source = edge[0]
            target = edge[1]
            edge_idx = list(network.edges(source, data=True)).index(edge)
            offset = (edge_idx - len(network.edges(source)) / 2) * 0.1  # Adjust the offset value as needed
            edge_labels[(source, target)] = edge[2]['length']
            edge_colors.append('gray')
            pos_source = pos[source]
            pos_target = pos[target]
            pos_edge = {
                source: (pos_source[0], pos_source[1] + offset),
                target: (pos_target[0], pos_target[1] + offset)
            }
            nx.draw_networkx_edges(network, pos_edge, edgelist=[(source, target)], edge_color='gray', width=1, connectionstyle='arc3, rad = 0.5')

    # Draw labels
    nx.draw_networkx_labels(network, pos, labels=labels, font_size=10, font_color='black')
    #nx.draw_networkx_edge_labels(network, pos, edge_labels=edge_labels, font_size=8, font_color='red')

    plt.title("Railway Network")
    plt.axis('off')

    #Save the figure
    plt.savefig("railway_network.png")

    plt.show()

def visualize_new(network):
    pos = nx.get_node_attributes(network, 'pos')
    nx.draw(network, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    edge_labels = dict([((u, v,), d['length']) for u, v, d in network.edges(data=True)])

    plt.show()

def visualize(network):
    pos = nx.get_node_attributes(network, 'pos')
    labels = {node: node if network.nodes[node]['type'] != 'switch' else '' for node in network.nodes}


