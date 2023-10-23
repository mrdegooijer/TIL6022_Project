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

    # Add invisible nodes - platforms
    railway_network.add_node("Rotterdam Centraal1", pos=(15, 0), type="platform")
    railway_network.add_node("Rotterdam Centraal 2", pos=(5, 0), type="platform")
    railway_network.add_node("Rotterdam Centraal 3", pos=(-5, 0), type="platform")
    railway_network.add_node("Rotterdam Centraal 4", pos=(-15, 0), type="platform")

    railway_network.add_node("Schiedam Centrum 1", pos=(15, 4000), type="platform")
    railway_network.add_node("Schiedam Centrum 2", pos=(5, 4000), type="platform")
    railway_network.add_node("Schiedam Centrum 3", pos=(-5, 4000), type="platform")
    railway_network.add_node("Schiedam Centrum 4", pos=(-15, 4000), type="platform")

    railway_network.add_node("Delft Campus 1", pos=(5, 12500), type="platform")
    railway_network.add_node("Delft Campus 3", pos=(-5, 12500), type="platform")

    railway_network.add_node("Delft 1", pos=(5, 14400), type="platform")
    railway_network.add_node("Delft 3", pos=(-5, 14400), type="platform")

    railway_network.add_node("Rijswijk 1", pos=(15, 18700), type="platform")
    railway_network.add_node("Rijswijk 2", pos=(5, 18700), type="platform")
    railway_network.add_node("Rijswijk 3", pos=(-5, 18700), type="platform")
    railway_network.add_node("Rijswijk 4", pos=(-15, 18700), type="platform")

    railway_network.add_node("Moerwijk 1", pos=(15, 20600), type="platform")
    railway_network.add_node("Moerwijk 2", pos=(5, 20600), type="platform")
    railway_network.add_node("Moerwijk 3", pos=(-5, 20600), type="platform")
    railway_network.add_node("Moerwijk 4", pos=(-15, 20600), type="platform")

    railway_network.add_node("Den Haag HS 1", pos=(15, 22600), type="platform")
    railway_network.add_node("Den Haag HS 2", pos=(5, 22600), type="platform")
    railway_network.add_node("Den Haag HS 3", pos=(-5, 22600), type="platform")
    railway_network.add_node("Den Haag HS 4", pos=(-15, 22600), type="platform")

    # Add invisible nodes - switches
    railway_network.add_node("Switch 1 1", pos=(15, 2100), type="vswitch")
    railway_network.add_node("Switch 1 2", pos=(5, 2100), type="vswitch")
    railway_network.add_node("Switch 1 3", pos=(-5, 2100), type="vswitch")
    railway_network.add_node("Switch 1 4", pos=(-15, 2100), type="vswitch")

    railway_network.add_node("Switch 2 1", pos=(15, 4500), type="vswitch")
    railway_network.add_node("Switch 2 2", pos=(5, 4500), type="vswitch")
    railway_network.add_node("Switch 2 3", pos=(-5, 4500), type="vswitch")
    railway_network.add_node("Switch 2 4", pos=(-15, 4500), type="vswitch")

    railway_network.add_node("Switch 3 1", pos=(5, 11000), type="vswitch")
    railway_network.add_node("Switch 3 3", pos=(-5, 11000), type="vswitch")

    railway_network.add_node("Switch 4 1", pos=(5, 12800), type="vswitch")
    railway_network.add_node("Switch 4 3", pos=(-5, 12800), type="vswitch")

    railway_network.add_node("Switch 5 1", pos=(15, 16900), type="vswitch")
    railway_network.add_node("Switch 5 2", pos=(5, 16900), type="vswitch")
    railway_network.add_node("Switch 5 3", pos=(-5, 16900), type="vswitch")
    railway_network.add_node("Switch 5 4", pos=(-15, 16900), type="vswitch")

    railway_network.add_node("Switch 6 1", pos=(15, 21200), type="vswitch")
    railway_network.add_node("Switch 6 2", pos=(5, 21200), type="vswitch")
    railway_network.add_node("Switch 6 3", pos=(-5, 21200), type="vswitch")
    railway_network.add_node("Switch 6 4", pos=(-15, 21200), type="vswitch")


    # Add edges - Rotterdam to HS
    railway_network.add_edge("Rotterdam Centraal 1", "Switch 1 1", length=2100, type="track1")
    railway_network.add_edge("Rotterdam Centraal 2", "Switch 1 2", length=2100, type="track2")
    railway_network.add_edge("Switch 1 1", "Schiedam Centrum 1", length=1900, type="track1")
    railway_network.add_edge("Switch 1 2", "Schiedam Centrum 2", length=1900, type="track2")
    railway_network.add_edge("Schiedam Centrum 1", "Switch 2 1", length=400, type="track1")
    railway_network.add_edge("Schiedam Centrum 2", "Switch 2 2", length=400, type="track2")
    railway_network.add_edge("Switch 2 1", "Switch 3 1", length=6500, type="track1")
    railway_network.add_edge("Switch 3 1", "Delft Campus 1", length=1500, type="track1")
    railway_network.add_edge("Delft Campus 1", "Switch 4 1", length=300, type="track1")
    railway_network.add_edge("Switch 4 1", "Delft 1", length=1600, type="track1")
    railway_network.add_edge("Delft 1", "Switch 5 1", length=2500, type="track1")
    railway_network.add_edge("Switch 5 1", "Rijswijk 1", length=1800, type="track1")
    railway_network.add_edge("Switch 5 2", "Rijswijk 2", length=1800, type="track2")
    railway_network.add_edge("Rijswijk 1", "Moerwijk 1", length=1900, type="track1")
    railway_network.add_edge("Rijswijk 2", "Moerwijk 2", length=1900, type="track2")
    railway_network.add_edge("Moerwijk 1", "Switch 6 1", length=600, type="track1")
    railway_network.add_edge("Moerwijk 2", "Switch 6 2", length=600, type="track2")
    railway_network.add_edge("Switch 6 1", "Den Haag HS 1", length=1400, type="track1")
    railway_network.add_edge("Switch 6 2", "Den Haag HS 2", length=1400, type="track2")

    # Add edges - HS to Rotterdam
    railway_network.add_edge("Switch 1 3", "Rotterdam Centraal 3", length=2100, type="track3")
    railway_network.add_edge("Switch 1 4", "Rotterdam Centraal 4", length=2100, type="track4")
    railway_network.add_edge("Schiedam Centrum 3", "Switch 1 3", length=1900, type="track3")
    railway_network.add_edge("Schiedam Centrum 4", "Switch 1 4", length=1900, type="track4")
    railway_network.add_edge("Switch 2 3", "Schiedam Centrum 3", length=400, type="track3")
    railway_network.add_edge("Switch 2 4", "Schiedam Centrum 4", length=400, type="track4")
    railway_network.add_edge("Switch 3 3", "Switch 2 3", length=6500, type="track3")
    railway_network.add_edge("Delft Campus 3", "Switch 3 3", length=1500, type="track3")
    railway_network.add_edge("Switch 4 3", "Delft Campus 3", length=300, type="track3")
    railway_network.add_edge("Delft 3", "Switch 4 3", length=1600, type="track3")
    railway_network.add_edge("Switch 5 3", "Delft 3", length=2500, type="track3")
    railway_network.add_edge("Rijswijk 3", "Switch 5 3", length=1800, type="track3")
    railway_network.add_edge("Rijswijk 4", "Switch 5 4", length=1800, type="track4")
    railway_network.add_edge("Moerwijk 3", "Rijswijk 3", length=1900, type="track3")
    railway_network.add_edge("Moerwijk 4", "Rijswijk 4", length=1900, type="track4")
    railway_network.add_edge("Switch 6 3", "Moerwijk 3", length=600, type="track3")
    railway_network.add_edge("Switch 6 4", "Moerwijk 4", length=600, type="track4")
    railway_network.add_edge("Den Haag HS 3", "Switch 6 3", length=1400, type="track3")
    railway_network.add_edge("Den Haag HS 4", "Switch 6 4", length=1400, type="track4")

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

def visualize_2(network):
    pos = nx.get_node_attributes(network, 'pos')
    labels = {node: node if network.nodes[node]['type'] != 'switch' else '' for node in network.nodes}

    # Define the figure size
    plt.figure(figsize=(6, 12))

    # Draw nodes
    node_size = [20 if network.nodes[node]['type'] == 'switch' else 200 if network.nodes[node]['type'] == 'station' else 1 for node in network.nodes]

    node_color = ['red' if network.nodes[node]['type'] == 'switch' else 'lightblue' for node in network.nodes]
    nx.draw_networkx_nodes(network, pos, node_size=node_size, node_color=node_color)

    # Draw edges
    for edge in network.edges(data=True):
        if edge[2]['type'] == 'track':
            nx.draw_networkx_edges(network, pos, edgelist=[(edge[0], edge[1])], edge_color='gray')

    # Draw labels
    nx.draw_networkx_labels(network, pos, labels=labels, font_size=10, font_color='black')

    plt.title("Railway Network")
    plt.axis('off')

    # Save the figure
    plt.savefig("railway_network.png")

    plt.show()


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
    # Create a graph to visualize your network
    G = network

    # Filter nodes based on the 'pos' and 'type' attributes
    node_positions = {node: attributes.get('pos', (0, 0)) for node, attributes in G.nodes(data=True)}
    node_types = {node: attributes.get('type', '') for node, attributes in G.nodes(data=True)}

    # Create lists of nodes for each type
    station_nodes = [node for node, node_type in node_types.items() if node_type == 'station']
    switch_nodes = [node for node, node_type in node_types.items() if node_type == 'switch']
    platform_nodes = [node for node, node_type in node_types.items() if node_type == 'platform']
    vswitch_nodes = [node for node, node_type in node_types.items() if node_type == 'vswitch']

    # Draw nodes based on type
    plt.figure(figsize=(12, 6))

    nx.draw(G, pos=node_positions, nodelist=station_nodes, node_color='skyblue', node_size=300, font_size=10,
            node_shape='o', with_labels=True)
    nx.draw(G, pos=node_positions, nodelist=switch_nodes, node_color='lightgray', node_size=300, font_size=10,
            node_shape='o', with_labels=True)
    nx.draw(G, pos=node_positions, nodelist=platform_nodes, node_color='lightgray', node_size=300, font_size=10,
            node_shape='o', with_labels=True)
    nx.draw(G, pos=node_positions, nodelist=vswitch_nodes, node_color='lightgray', node_size=300, font_size=10,
            node_shape='o', with_labels=True)

    # Draw edges without considering edge types
    nx.draw_networkx_edges(G, pos=node_positions, edgelist=G.edges(), edge_color='gray')

    # Add a legend for node types
    legend_labels = {
        'station': 'Stations',
        'switch': 'Switches',
        'platform': 'Platforms',
        'vswitch': 'Virtual Switches',
    }
    for node_type, label in legend_labels.items():
        plt.scatter([], [], label=label, c='lightgray', s=100)
    plt.legend(scatterpoints=1, frameon=False, title='Node Types')

    plt.title("Network Visualization")
    plt.show()


def check_type(network):
    default_node_type = 'unknown'
    G = network
    for node in G.nodes:
        node_type = G.nodes[node].get('type', 'unknown')
        print(f"Node {node}: Type = {node_type}")
    return



