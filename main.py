#the main loop of the program
import networkx as nx
# import holoviews as hv
# from network import railway_network_current, railway_network_future, visualize_2
# from ADDraw import simulate, Convert_to_3D, get_3d_pos, get_node_dict

# if __name__ == '__main__':
#     railway_network = railway_network_current()

from physical_elements import run_simulation

run_simulation()

    #network3d = Convert_to_3D(railway_network)
#    positions = get_node_dict(railway_network)
#    print(positions)

    # train_locations_2 = [[(5, 200), (5, 10000), (15, 14000), (-5, 8000), (-15, 20000)],
    #                      [(5, 220), (5, 10020), (15, 14020), (-5, 8020), (-15, 20020)],
    #                      [(5, 240), (5, 10040), (15, 14040), (-5, 8040), (-15, 20040)],
    #                      [(5, 260), (5, 10060), (15, 14060), (-5, 8060), (-15, 20060)],
    #                      [(5, 280), (5, 10080), (15, 14080), (-5, 8080), (-15, 20080)],
    #                      [(5, 300), (5, 10100), (15, 14100), (-5, 8100), (-15, 20100)],
    #                      [(5, 320), (5, 10120), (15, 14120), (-5, 8120), (-15, 20120)],
    #                      [(5, 340), (5, 10140), (15, 14140), (-5, 8140), (-15, 20140)],
    #                      [(5, 360), (5, 10160), (15, 14160), (-5, 8160), (-15, 20160)]]
    #
    # map = simulate(railway_network, positions, train_locations_2)
    #
    # nx.draw(map)
    #
    #
