#the main loop of the program


if __name__ == '__main__':
    from network import railway_network_current, railway_network_future
    railway_network = railway_network_current()

    from model import RAIL_NETWORK
    rail_network = RAIL_NETWORK(railway_network)

    from physical_elements import TRAIN
    train_1 = TRAIN(1, "IC", 0, ['Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag HS'], 0)

    rail_network.add_train(train_1)



