#the main loop of the program
import networkx as nx
# import holoviews as hv
# from network import railway_network_current, railway_network_future, visualize_2
# from ADDraw import simulate, Convert_to_3D, get_3d_pos, get_node_dict

# if __name__ == '__main__':
#     railway_network = railway_network_current()

from physical_elements import run_simulation

run_simulation()


