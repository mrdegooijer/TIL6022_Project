import networkx as nx
import matplotlib.pyplot as plt

def railway_network_current():
    railway_network = nx.DiGraph()

    # Add nodes - stations
    railway_network.add_node("Rotterdam Centraal", pos=(0, 0), platforms=4, type="station")
    railway_network.add_node("Schiedam Centrum", pos=(0, 4.0), platforms=4, type="station")
    railway_network.add_node("Delft Campus", pos=(0, 12.5), platforms=2, type="station")
    railway_network.add_node("Delft", pos=(0, 14.4), platforms=2, type="station")
    railway_network.add_node("Rijswijk", pos=(0, 18.7), platforms=4, type="station")
    railway_network.add_node("Moerwijk", pos=(0, 20.6), platforms=4, type="station")
    railway_network.add_node("Den Haag HS", pos=(0, 22.6), platforms=4, type="station")

    # Add nodes - switches
    railway_network.add_node("Switch 1", pos=(0, 2.1), type="switch")
    railway_network.add_node("Switch 2", pos=(0, 4.5), type="switch")
    railway_network.add_node("Switch 3", pos=(0, 11), type="switch")
    railway_network.add_node("Switch 4", pos=(0, 12.8), type="switch")
    railway_network.add_node("Switch 5", pos=(0, 16.9), type="switch")
    railway_network.add_node("Switch 6", pos=(0, 21.2), type="switch")

    # Add edges - Rotterdam to HS
    railway_network.add_edge("Rotterdam Centraal", "Switch 1", length=2.1, type="track")
    railway_network.add_edge("Rotterdam Centraal", "Switch 1", length=2.1, type="track")
    railway_network.add_edge("Switch 1", "Schiedam Centrum", length=1.9, type="track")
    railway_network.add_edge("Switch 1", "Schiedam Centrum", length=1.9, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 2", length=0.4, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 2", length=0.4, type="track")
    railway_network.add_edge("Switch 2", "Switch 3", length=6.5, type="track")
    railway_network.add_edge("Switch 3", "Delft Campus", length=1.5, type="track")
    railway_network.add_edge("Delft Campus", "Switch 4", length=0.3, type="track")
    railway_network.add_edge("Switch 4", "Delft", length=1.6, type="track")
    railway_network.add_edge("Delft", "Switch 5", length=2.5, type="track")
    railway_network.add_edge("Switch 5", "Rijswijk", length=1.8, type="track")
    railway_network.add_edge("Switch 5", "Rijswijk", length=1.8, type="track")
    railway_network.add_edge("Rijswijk", "Moerwijk", length=1.9, type="track")
    railway_network.add_edge("Rijswijk", "Moerwijk", length=1.9, type="track")
    railway_network.add_edge("Moerwijk", "Switch 6", length=0.6, type="track")
    railway_network.add_edge("Moerwijk", "Switch 6", length=0.6, type="track")
    railway_network.add_edge("Switch 6", "Den Haag HS", length=1.4, type="track")
    railway_network.add_edge("Switch 6", "Den Haag HS", length=1.4, type="track")

    # Add edges - HS to Rotterdam
    railway_network.add_edge("Switch 1", "Rotterdam Centraal", length=2.1, type="track")
    railway_network.add_edge("Switch 1", "Rotterdam Centraal", length=2.1, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 1", length=1.9, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 1", length=1.9, type="track")
    railway_network.add_edge("Switch 2", "Schiedam Centrum", length=0.4, type="track")
    railway_network.add_edge("Switch 2", "Schiedam Centrum", length=0.4, type="track")
    railway_network.add_edge("Switch 3", "Switch 2", length=6.5, type="track")
    railway_network.add_edge("Delft Campus", "Switch 3", length=1.5, type="track")
    railway_network.add_edge("Switch 4", "Delft Campus", length=0.3, type="track")
    railway_network.add_edge("Delft", "Switch 4", length=1.6, type="track")
    railway_network.add_edge("Switch 5", "Delft", length=2.5, type="track")
    railway_network.add_edge("Rijswijk", "Switch 5", length=1.8, type="track")
    railway_network.add_edge("Rijswijk", "Switch 5", length=1.8, type="track")
    railway_network.add_edge("Moerwijk", "Rijswijk", length=1.9, type="track")
    railway_network.add_edge("Moerwijk", "Rijswijk", length=1.9, type="track")
    railway_network.add_edge("Switch 6", "Moerwijk", length=0.6, type="track")
    railway_network.add_edge("Switch 6", "Moerwijk", length=0.6, type="track")
    railway_network.add_edge("Den Haag HS", "Switch 6", length=1.4, type="track")
    railway_network.add_edge("Den Haag HS", "Switch 6", length=1.4, type="track")

    return railway_network

def railway_network_future():
    railway_network = nx.DiGraph()

    # Add nodes - stations
    railway_network.add_node("Rotterdam Centraal", pos=(0, 0), platforms=4, type="station")
    railway_network.add_node("Schiedam Centrum", pos=(0, 4.0), platforms=4, type="station")
    railway_network.add_node("Delft Campus", pos=(0, 12.5), platforms=2, type="station")
    railway_network.add_node("Delft", pos=(0, 14.4), platforms=2, type="station")
    railway_network.add_node("Rijswijk", pos=(0, 18.7), platforms=4, type="station")
    railway_network.add_node("Moerwijk", pos=(0, 20.6), platforms=4, type="station")
    railway_network.add_node("Den Haag HS", pos=(0, 22.6), platforms=4, type="station")

    # Add nodes - switches
    railway_network.add_node("Switch 1", pos=(0, 2.1), type="switch")
    railway_network.add_node("Switch 2", pos=(0, 4.5), type="switch")
    railway_network.add_node("Switch 3", pos=(0, 11), type="switch")
    railway_network.add_node("Switch 4", pos=(0, 12.8), type="switch")
    railway_network.add_node("Switch 5", pos=(0, 16.9), type="switch")
    railway_network.add_node("Switch 6", pos=(0, 21.2), type="switch")

    # Add edges - Rotterdam to HS
    railway_network.add_edge("Rotterdam Centraal", "Switch 1", length=2.1, type="track")
    railway_network.add_edge("Rotterdam Centraal", "Switch 1", length=2.1, type="track")
    railway_network.add_edge("Switch 1", "Schiedam Centrum", length=1.9, type="track")
    railway_network.add_edge("Switch 1", "Schiedam Centrum", length=1.9, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 2", length=0.4, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 2", length=0.4, type="track")
    railway_network.add_edge("Switch 2", "Switch 3", length=6.5, type="track")
    railway_network.add_edge("Switch 2", "Switch 3", length=6.5, type="track")
    railway_network.add_edge("Switch 3", "Delft Campus", length=1.5, type="track")
    railway_network.add_edge("Switch 3", "Delft Campus", length=1.5, type="track")
    railway_network.add_edge("Delft Campus", "Switch 4", length=0.3, type="track")
    railway_network.add_edge("Delft Campus", "Switch 4", length=0.3, type="track")
    railway_network.add_edge("Switch 4", "Delft", length=1.6, type="track")
    railway_network.add_edge("Switch 4", "Delft", length=1.6, type="track")
    railway_network.add_edge("Delft", "Switch 5", length=2.5, type="track")
    railway_network.add_edge("Delft", "Switch 5", length=2.5, type="track")
    railway_network.add_edge("Switch 5", "Rijswijk", length=1.8, type="track")
    railway_network.add_edge("Switch 5", "Rijswijk", length=1.8, type="track")
    railway_network.add_edge("Rijswijk", "Moerwijk", length=1.9, type="track")
    railway_network.add_edge("Rijswijk", "Moerwijk", length=1.9, type="track")
    railway_network.add_edge("Moerwijk", "Switch 6", length=0.6, type="track")
    railway_network.add_edge("Moerwijk", "Switch 6", length=0.6, type="track")
    railway_network.add_edge("Switch 6", "Den Haag HS", length=1.4, type="track")
    railway_network.add_edge("Switch 6", "Den Haag HS", length=1.4, type="track")

    # Add edges - HS to Rotterdam
    railway_network.add_edge("Switch 1", "Rotterdam Centraal", length=2.1, type="track")
    railway_network.add_edge("Switch 1", "Rotterdam Centraal", length=2.1, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 1", length=1.9, type="track")
    railway_network.add_edge("Schiedam Centrum", "Switch 1", length=1.9, type="track")
    railway_network.add_edge("Switch 2", "Schiedam Centrum", length=0.4, type="track")
    railway_network.add_edge("Switch 2", "Schiedam Centrum", length=0.4, type="track")
    railway_network.add_edge("Switch 3", "Switch 2", length=6.5, type="track")
    railway_network.add_edge("Switch 3", "Switch 2", length=6.5, type="track")
    railway_network.add_edge("Delft Campus", "Switch 3", length=1.5, type="track")
    railway_network.add_edge("Delft Campus", "Switch 3", length=1.5, type="track")
    railway_network.add_edge("Switch 4", "Delft Campus", length=0.3, type="track")
    railway_network.add_edge("Switch 4", "Delft Campus", length=0.3, type="track")
    railway_network.add_edge("Delft", "Switch 4", length=1.6, type="track")
    railway_network.add_edge("Delft", "Switch 4", length=1.6, type="track")
    railway_network.add_edge("Switch 5", "Delft", length=2.5, type="track")
    railway_network.add_edge("Switch 5", "Delft", length=2.5, type="track")
    railway_network.add_edge("Rijswijk", "Switch 5", length=1.8, type="track")
    railway_network.add_edge("Rijswijk", "Switch 5", length=1.8, type="track")
    railway_network.add_edge("Moerwijk", "Rijswijk", length=1.9, type="track")
    railway_network.add_edge("Moerwijk", "Rijswijk", length=1.9, type="track")
    railway_network.add_edge("Switch 6", "Moerwijk", length=0.6, type="track")
    railway_network.add_edge("Switch 6", "Moerwijk", length=0.6, type="track")
    railway_network.add_edge("Den Haag HS", "Switch 6", length=1.4, type="track")
    railway_network.add_edge("Den Haag HS", "Switch 6", length=1.4, type="track")

    return railway_network

def visualize_network(network):
    pos = nx.get_node_attributes(network, 'pos')
    labels = {node: node if network.nodes[node]['type'] != 'switch' else '' for node in network.nodes}

    plt.figure(figsize=(12, 6))

    # Draw nodes
    node_size = [50 if network.nodes[node]['type'] == 'switch' else 400 for node in network.nodes]
    node_color = ['red' if network.nodes[node]['type'] == 'switch' else 'lightblue' for node in network.nodes]
    nx.draw_networkx_nodes(network, pos, node_size=node_size, node_color=node_color)

    # Draw edges
    for edge in network.edges(data=True):
        if edge[2]['type'] == 'track':
            nx.draw_networkx_edges(network, pos, edgelist=[(edge[0], edge[1])], edge_color='gray')

    edge_labels = {(edge[0], edge[1]): edge[2]['length'] for edge in network.edges(data=True) if
                   edge[2]['type'] == 'track'}

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
            nx.draw_networkx_edges(network, pos_edge, edgelist=[(source, target)], edge_color='gray', width=1)

    # Draw labels
    nx.draw_networkx_labels(network, pos, labels=labels, font_size=10, font_color='black')
    #nx.draw_networkx_edge_labels(network, pos, edge_labels=edge_labels, font_size=8, font_color='red')

    plt.title("Railway Network")
    plt.axis('off')

    #Save the figure
    plt.savefig("railway_network.png")

    plt.show()
