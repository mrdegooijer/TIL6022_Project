#the main loop of the program
import networkx as nx

if __name__ == '__main__':
    from network import railway_network_current
    railway_network = railway_network_current()
    from network import visualize, visualize_network, visualize_2, check_type
    #visualize(railway_network)
    #visualize_network(railway_network)
    visualize_2(railway_network)
    #check_type(railway_network)

    # from physical_elements import TRAIN
    #
    # #create trains
    # train1 = TRAIN(1, "IC", 0, [500, 800, 1000], 100)
    #
    # railway_network.add_node(train1.train_id, pos=(0, train1.location))



