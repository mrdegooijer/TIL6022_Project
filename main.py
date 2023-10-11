#the main loop of the program


if __name__ == '__main__':
    from network import railway_network_current, railway_network_future
    railway_network = railway_network_current()
    from network import visualize_network, visualize_new, visualize
    visualize_network(railway_network)
    #visualize_new(railway_network)
    #visualize(railway_network)
