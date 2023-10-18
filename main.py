#the main loop of the program
import networkx as nx

if __name__ == '__main__':
    from network import railway_network_current
    railway_network = railway_network_current()
    from network import visualize, visualize_network, visualize_2, check_type
    #visualize_2(railway_network)

    from ADDraw import draw
    draw(railway_network)



