#the main loop of the program
import networkx as nx

if __name__ == '__main__':
    from network import railway_network_current
    railway_network = railway_network_current()
    from network import visualize, visualize_network, visualize_2, check_type
    #visualize_2(railway_network)

    from ADDraw import draw, sim, Convert_to_3D, get_3d_pos
    #network3d = Convert_to_3D(railway_network)
    positions = get_3d_pos(railway_network)
    sim(railway_network, positions, train_locations = [(5, 200, 0), (5, 10000, 0), (15, 14000, 0)])



