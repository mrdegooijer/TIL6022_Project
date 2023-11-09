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
    railway_network.add_node("Rotterdam Centraal 1", pos=(15, 0), type="platform")
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
    #railway_network.add_edge("Switch 2 1", "Switch 2 2", length=10, type="track1")
    railway_network.add_edge("Switch 2 2", "Switch 3 1", length=6500, type="track1")
    railway_network.add_edge("Switch 3 1", "Delft Campus 1", length=1500, type="track1")
    railway_network.add_edge("Delft Campus 1", "Switch 4 1", length=300, type="track1")
    railway_network.add_edge("Switch 4 1", "Delft 1", length=1600, type="track1")
    railway_network.add_edge("Delft 1", "Switch 5 2", length=2500, type="track1")
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

def railway_network_current_holo():
    railway_network = nx.DiGraph()

    # Add nodes - stations
    railway_network.add_node("Rotterdam Centraal", platforms=4, type="station")
    railway_network.add_node("Schiedam Centrum", platforms=4, type="station")
    railway_network.add_node("Delft Campus", platforms=2, type="station")
    railway_network.add_node("Delft", platforms=2, type="station")
    railway_network.add_node("Rijswijk", platforms=4, type="station")
    railway_network.add_node("Moerwijk", platforms=4, type="station")
    railway_network.add_node("Den Haag HS", platforms=4, type="station")

    # Add nodes - switches
    railway_network.add_node("Switch 1", type="switch")
    railway_network.add_node("Switch 2", type="switch")
    railway_network.add_node("Switch 3", type="switch")
    railway_network.add_node("Switch 4", type="switch")
    railway_network.add_node("Switch 5", type="switch")
    railway_network.add_node("Switch 6", type="switch")

    # Add invisible nodes - platforms
    railway_network.add_node("Rotterdam Centraal 1", type="platform")
    railway_network.add_node("Rotterdam Centraal 2", type="platform")
    railway_network.add_node("Rotterdam Centraal 3", type="platform")
    railway_network.add_node("Rotterdam Centraal 4", type="platform")

    railway_network.add_node("Schiedam Centrum 1", type="platform")
    railway_network.add_node("Schiedam Centrum 2", type="platform")
    railway_network.add_node("Schiedam Centrum 3", type="platform")
    railway_network.add_node("Schiedam Centrum 4", type="platform")

    railway_network.add_node("Delft Campus 1", type="platform")
    railway_network.add_node("Delft Campus 3", type="platform")

    railway_network.add_node("Delft 1", type="platform")
    railway_network.add_node("Delft 3", type="platform")

    railway_network.add_node("Rijswijk 1", type="platform")
    railway_network.add_node("Rijswijk 2", type="platform")
    railway_network.add_node("Rijswijk 3", type="platform")
    railway_network.add_node("Rijswijk 4", type="platform")

    railway_network.add_node("Moerwijk 1", type="platform")
    railway_network.add_node("Moerwijk 2", type="platform")
    railway_network.add_node("Moerwijk 3", type="platform")
    railway_network.add_node("Moerwijk 4", type="platform")

    railway_network.add_node("Den Haag HS 1", type="platform")
    railway_network.add_node("Den Haag HS 2", type="platform")
    railway_network.add_node("Den Haag HS 3", type="platform")
    railway_network.add_node("Den Haag HS 4", type="platform")

    # Add invisible nodes - switches
    railway_network.add_node("Switch 1 1", type="vswitch")
    railway_network.add_node("Switch 1 2", type="vswitch")
    railway_network.add_node("Switch 1 3", type="vswitch")
    railway_network.add_node("Switch 1 4", type="vswitch")

    railway_network.add_node("Switch 2 1", type="vswitch")
    railway_network.add_node("Switch 2 2", type="vswitch")
    railway_network.add_node("Switch 2 3", type="vswitch")
    railway_network.add_node("Switch 2 4", type="vswitch")

    railway_network.add_node("Switch 3 1", type="vswitch")
    railway_network.add_node("Switch 3 3", type="vswitch")

    railway_network.add_node("Switch 4 1", type="vswitch")
    railway_network.add_node("Switch 4 3", type="vswitch")

    railway_network.add_node("Switch 5 1", type="vswitch")
    railway_network.add_node("Switch 5 2", type="vswitch")
    railway_network.add_node("Switch 5 3", type="vswitch")
    railway_network.add_node("Switch 5 4", type="vswitch")

    railway_network.add_node("Switch 6 1", type="vswitch")
    railway_network.add_node("Switch 6 2", type="vswitch")
    railway_network.add_node("Switch 6 3", type="vswitch")
    railway_network.add_node("Switch 6 4", type="vswitch")

    # Add edges - Rotterdam to HS
    railway_network.add_edge("Rotterdam Centraal 1", "Switch 1 1", length=2100, type="track1")
    railway_network.add_edge("Rotterdam Centraal 2", "Switch 1 2", length=2100, type="track2")
    railway_network.add_edge("Switch 1 1", "Schiedam Centrum 1", length=1900, type="track1")
    railway_network.add_edge("Switch 1 2", "Schiedam Centrum 2", length=1900, type="track2")
    railway_network.add_edge("Schiedam Centrum 1", "Switch 2 1", length=400, type="track1")
    railway_network.add_edge("Schiedam Centrum 2", "Switch 2 2", length=400, type="track2")
    # railway_network.add_edge("Switch 2 1", "Switch 2 2", length=10, type="track1")
    railway_network.add_edge("Switch 2 2", "Switch 3 1", length=6500, type="track1")
    railway_network.add_edge("Switch 3 1", "Delft Campus 1", length=1500, type="track1")
    railway_network.add_edge("Delft Campus 1", "Switch 4 1", length=300, type="track1")
    railway_network.add_edge("Switch 4 1", "Delft 1", length=1600, type="track1")
    railway_network.add_edge("Delft 1", "Switch 5 2", length=2500, type="track1")
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

    # Add invisible nodes - platforms
    railway_network.add_node("Rotterdam Centraal 1", pos=(15, 0), type="platform")
    railway_network.add_node("Rotterdam Centraal 2", pos=(5, 0), type="platform")
    railway_network.add_node("Rotterdam Centraal 3", pos=(-5, 0), type="platform")
    railway_network.add_node("Rotterdam Centraal 4", pos=(-15, 0), type="platform")

    railway_network.add_node("Schiedam Centrum 1", pos=(15, 4000), type="platform")
    railway_network.add_node("Schiedam Centrum 2", pos=(5, 4000), type="platform")
    railway_network.add_node("Schiedam Centrum 3", pos=(-5, 4000), type="platform")
    railway_network.add_node("Schiedam Centrum 4", pos=(-15, 4000), type="platform")

    railway_network.add_node("Delft Campus 1", pos=(15, 12500), type="platform")
    railway_network.add_node("Delft Campus 2", pos=(5, 12500), type="platform")
    railway_network.add_node("Delft Campus 3", pos=(-5, 12500), type="platform")
    railway_network.add_node("Delft Campus 4", pos=(-15, 12500), type="platform")

    railway_network.add_node("Delft 1", pos=(15, 14400), type="platform")
    railway_network.add_node("Delft 2", pos=(5, 14400), type="platform")
    railway_network.add_node("Delft 3", pos=(-5, 14400), type="platform")
    railway_network.add_node("Delft 4", pos=(-15, 14400), type="platform")

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

    railway_network.add_node("Switch 3 1", pos=(15, 11000), type="vswitch")
    railway_network.add_node("Switch 3 2", pos=(5, 11000), type="vswitch")
    railway_network.add_node("Switch 3 3", pos=(-5, 11000), type="vswitch")
    railway_network.add_node("Switch 3 4", pos=(-15, 11000), type="vswitch")

    railway_network.add_node("Switch 4 1", pos=(15, 12800), type="vswitch")
    railway_network.add_node("Switch 4 2", pos=(5, 12800), type="vswitch")
    railway_network.add_node("Switch 4 3", pos=(-5, 12800), type="vswitch")
    railway_network.add_node("Switch 4 4", pos=(-15, 12800), type="vswitch")

    railway_network.add_node("Switch 5 1", pos=(15, 16900), type="vswitch")
    railway_network.add_node("Switch 5 2", pos=(5, 16900), type="vswitch")
    railway_network.add_node("Switch 5 3", pos=(-5, 16900), type="vswitch")
    railway_network.add_node("Switch 5 4", pos=(-15, 16900), type="vswitch")

    railway_network.add_node("Switch 6 1", pos=(15, 21200), type="vswitch")
    railway_network.add_node("Switch 6 2", pos=(5, 21200), type="vswitch")
    railway_network.add_node("Switch 6 3", pos=(-5, 21200), type="vswitch")
    railway_network.add_node("Switch 6 4", pos=(-15, 21200), type="vswitch")

    # Add edges - Rotterdam to HS
    railway_network.add_edge("Rotterdam Centraal 1", "Switch 1 1", length=2100, type="track")
    railway_network.add_edge("Rotterdam Centraal 2", "Switch 1 2", length=2100, type="track")
    railway_network.add_edge("Switch 1 1", "Schiedam Centrum 1", length=1900, type="track")
    railway_network.add_edge("Switch 1 2", "Schiedam Centrum 2", length=1900, type="track")
    railway_network.add_edge("Schiedam Centrum 1", "Switch 2 1", length=400, type="track")
    railway_network.add_edge("Schiedam Centrum 2", "Switch 2 2", length=400, type="track")
    railway_network.add_edge("Switch 2 1", "Switch 3 1", length=6500, type="track")
    railway_network.add_edge("Switch 2 2", "Switch 3 2", length=6500, type="track")
    railway_network.add_edge("Switch 3 1", "Delft Campus 1", length=1500, type="track")
    railway_network.add_edge("Switch 3 2", "Delft Campus 2", length=1500, type="track")
    railway_network.add_edge("Delft Campus 1", "Switch 4 1", length=300, type="track")
    railway_network.add_edge("Delft Campus 2", "Switch 4 2", length=300, type="track")
    railway_network.add_edge("Switch 4 1", "Delft 1", length=1600, type="track")
    railway_network.add_edge("Switch 4 2", "Delft 2", length=1600, type="track")
    railway_network.add_edge("Delft 1", "Switch 5 1", length=2500, type="track")
    railway_network.add_edge("Delft 2", "Switch 5 2", length=2500, type="track")
    railway_network.add_edge("Switch 5 1", "Rijswijk 1", length=1800, type="track")
    railway_network.add_edge("Switch 5 2", "Rijswijk 2", length=1800, type="track")
    railway_network.add_edge("Rijswijk 1", "Moerwijk 1", length=1900, type="track")
    railway_network.add_edge("Rijswijk 2", "Moerwijk 2", length=1900, type="track")
    railway_network.add_edge("Moerwijk 1", "Switch 6 1", length=600, type="track")
    railway_network.add_edge("Moerwijk 2", "Switch 6 2", length=600, type="track")
    railway_network.add_edge("Switch 6 1", "Den Haag HS 1", length=1400, type="track")
    railway_network.add_edge("Switch 6 2", "Den Haag HS 2", length=1400, type="track")

    # Add edges - HS to Rotterdam
    railway_network.add_edge("Switch 1 3", "Rotterdam Centraal 3", length=2100, type="track")
    railway_network.add_edge("Switch 1 4", "Rotterdam Centraal 4", length=2100, type="track")
    railway_network.add_edge("Schiedam Centrum 3", "Switch 1 3", length=1900, type="track")
    railway_network.add_edge("Schiedam Centrum 4", "Switch 1 4", length=1900, type="track")
    railway_network.add_edge("Switch 2 3", "Schiedam Centrum 3", length=400, type="track")
    railway_network.add_edge("Switch 2 4", "Schiedam Centrum 4", length=400, type="track")
    railway_network.add_edge("Switch 3 3", "Switch 2 3", length=6500, type="track")
    railway_network.add_edge("Switch 3 4", "Switch 2 4", length=6500, type="track")
    railway_network.add_edge("Delft Campus 3", "Switch 3 3", length=1500, type="track")
    railway_network.add_edge("Delft Campus 4", "Switch 3 4", length=1500, type="track")
    railway_network.add_edge("Switch 4 3", "Delft Campus 3", length=300, type="track")
    railway_network.add_edge("Switch 4 4", "Delft Campus 4", length=300, type="track")
    railway_network.add_edge("Delft 3", "Switch 4 3", length=1600, type="track")
    railway_network.add_edge("Delft 4", "Switch 4 4", length=1600, type="track")
    railway_network.add_edge("Switch 5 3", "Delft 3", length=2500, type="track")
    railway_network.add_edge("Switch 5 4", "Delft 4", length=2500, type="track")
    railway_network.add_edge("Rijswijk 3", "Switch 5 3", length=1800, type="track")
    railway_network.add_edge("Rijswijk 4", "Switch 5 4", length=1800, type="track")
    railway_network.add_edge("Moerwijk 3", "Rijswijk 3", length=1900, type="track")
    railway_network.add_edge("Moerwijk 4", "Rijswijk 4", length=1900, type="track")
    railway_network.add_edge("Switch 6 3", "Moerwijk 3", length=600, type="track")
    railway_network.add_edge("Switch 6 4", "Moerwijk 4", length=600, type="track")
    railway_network.add_edge("Den Haag HS 3", "Switch 6 3", length=1400, type="track")
    railway_network.add_edge("Den Haag HS 4", "Switch 6 4", length=1400, type="track")

    return railway_network

def railway_network_future_holo():
    railway_network = nx.DiGraph()

    # Add nodes - stations
    railway_network.add_node("Rotterdam Centraal", platforms=4, type="station")
    railway_network.add_node("Schiedam Centrum", platforms=4, type="station")
    railway_network.add_node("Delft Campus", platforms=4, type="station")
    railway_network.add_node("Delft", platforms=4, type="station")
    railway_network.add_node("Rijswijk", platforms=4, type="station")
    railway_network.add_node("Moerwijk", platforms=4, type="station")
    railway_network.add_node("Den Haag HS", platforms=4, type="station")

    # Add nodes - switches
    railway_network.add_node("Switch 1", type="switch")
    railway_network.add_node("Switch 2", type="switch")
    railway_network.add_node("Switch 3", type="switch")
    railway_network.add_node("Switch 4", type="switch")
    railway_network.add_node("Switch 5", type="switch")
    railway_network.add_node("Switch 6", type="switch")

    # Add invisible nodes - platforms
    railway_network.add_node("Rotterdam Centraal 1", type="platform")
    railway_network.add_node("Rotterdam Centraal 2", type="platform")
    railway_network.add_node("Rotterdam Centraal 3", type="platform")
    railway_network.add_node("Rotterdam Centraal 4", type="platform")

    railway_network.add_node("Schiedam Centrum 1", type="platform")
    railway_network.add_node("Schiedam Centrum 2", type="platform")
    railway_network.add_node("Schiedam Centrum 3", type="platform")
    railway_network.add_node("Schiedam Centrum 4", type="platform")

    railway_network.add_node("Delft Campus 1", type="platform")
    railway_network.add_node("Delft Campus 2", type="platform")
    railway_network.add_node("Delft Campus 3", type="platform")
    railway_network.add_node("Delft Campus 4", type="platform")

    railway_network.add_node("Delft 1", type="platform")
    railway_network.add_node("Delft 2", type="platform")
    railway_network.add_node("Delft 3", type="platform")
    railway_network.add_node("Delft 4", type="platform")

    railway_network.add_node("Rijswijk 1", type="platform")
    railway_network.add_node("Rijswijk 2", type="platform")
    railway_network.add_node("Rijswijk 3", type="platform")
    railway_network.add_node("Rijswijk 4", type="platform")

    railway_network.add_node("Moerwijk 1", type="platform")
    railway_network.add_node("Moerwijk 2", type="platform")
    railway_network.add_node("Moerwijk 3", type="platform")
    railway_network.add_node("Moerwijk 4", type="platform")

    railway_network.add_node("Den Haag HS 1", type="platform")
    railway_network.add_node("Den Haag HS 2", type="platform")
    railway_network.add_node("Den Haag HS 3", type="platform")
    railway_network.add_node("Den Haag HS 4", type="platform")

    # Add invisible nodes - switches
    railway_network.add_node("Switch 1 1", type="vswitch")
    railway_network.add_node("Switch 1 2", type="vswitch")
    railway_network.add_node("Switch 1 3", type="vswitch")
    railway_network.add_node("Switch 1 4", type="vswitch")

    railway_network.add_node("Switch 2 1", type="vswitch")
    railway_network.add_node("Switch 2 2", type="vswitch")
    railway_network.add_node("Switch 2 3", type="vswitch")
    railway_network.add_node("Switch 2 4", type="vswitch")

    railway_network.add_node("Switch 3 1", type="vswitch")
    railway_network.add_node("Switch 3 2", type="vswitch")
    railway_network.add_node("Switch 3 3", type="vswitch")
    railway_network.add_node("Switch 3 4", type="vswitch")

    railway_network.add_node("Switch 4 1", type="vswitch")
    railway_network.add_node("Switch 4 2", type="vswitch")
    railway_network.add_node("Switch 4 3", type="vswitch")
    railway_network.add_node("Switch 4 4", type="vswitch")

    railway_network.add_node("Switch 5 1", type="vswitch")
    railway_network.add_node("Switch 5 2", type="vswitch")
    railway_network.add_node("Switch 5 3", type="vswitch")
    railway_network.add_node("Switch 5 4", type="vswitch")

    railway_network.add_node("Switch 6 1", type="vswitch")
    railway_network.add_node("Switch 6 2", type="vswitch")
    railway_network.add_node("Switch 6 3", type="vswitch")
    railway_network.add_node("Switch 6 4", type="vswitch")

    # Add edges - Rotterdam to HS
    railway_network.add_edge("Rotterdam Centraal 1", "Switch 1 1", length=2100, type="track")
    railway_network.add_edge("Rotterdam Centraal 2", "Switch 1 2", length=2100, type="track")
    railway_network.add_edge("Switch 1 1", "Schiedam Centrum 1", length=1900, type="track")
    railway_network.add_edge("Switch 1 2", "Schiedam Centrum 2", length=1900, type="track")
    railway_network.add_edge("Schiedam Centrum 1", "Switch 2 1", length=400, type="track")
    railway_network.add_edge("Schiedam Centrum 2", "Switch 2 2", length=400, type="track")
    railway_network.add_edge("Switch 2 1", "Switch 3 1", length=6500, type="track")
    railway_network.add_edge("Switch 2 2", "Switch 3 2", length=6500, type="track")
    railway_network.add_edge("Switch 3 1", "Delft Campus 1", length=1500, type="track")
    railway_network.add_edge("Switch 3 2", "Delft Campus 2", length=1500, type="track")
    railway_network.add_edge("Delft Campus 1", "Switch 4 1", length=300, type="track")
    railway_network.add_edge("Delft Campus 2", "Switch 4 2", length=300, type="track")
    railway_network.add_edge("Switch 4 1", "Delft 1", length=1600, type="track")
    railway_network.add_edge("Switch 4 2", "Delft 2", length=1600, type="track")
    railway_network.add_edge("Delft 1", "Switch 5 1", length=2500, type="track")
    railway_network.add_edge("Delft 2", "Switch 5 2", length=2500, type="track")
    railway_network.add_edge("Switch 5 1", "Rijswijk 1", length=1800, type="track")
    railway_network.add_edge("Switch 5 2", "Rijswijk 2", length=1800, type="track")
    railway_network.add_edge("Rijswijk 1", "Moerwijk 1", length=1900, type="track")
    railway_network.add_edge("Rijswijk 2", "Moerwijk 2", length=1900, type="track")
    railway_network.add_edge("Moerwijk 1", "Switch 6 1", length=600, type="track")
    railway_network.add_edge("Moerwijk 2", "Switch 6 2", length=600, type="track")
    railway_network.add_edge("Switch 6 1", "Den Haag HS 1", length=1400, type="track")
    railway_network.add_edge("Switch 6 2", "Den Haag HS 2", length=1400, type="track")

    # Add edges - HS to Rotterdam
    railway_network.add_edge("Switch 1 3", "Rotterdam Centraal 3", length=2100, type="track")
    railway_network.add_edge("Switch 1 4", "Rotterdam Centraal 4", length=2100, type="track")
    railway_network.add_edge("Schiedam Centrum 3", "Switch 1 3", length=1900, type="track")
    railway_network.add_edge("Schiedam Centrum 4", "Switch 1 4", length=1900, type="track")
    railway_network.add_edge("Switch 2 3", "Schiedam Centrum 3", length=400, type="track")
    railway_network.add_edge("Switch 2 4", "Schiedam Centrum 4", length=400, type="track")
    railway_network.add_edge("Switch 3 3", "Switch 2 3", length=6500, type="track")
    railway_network.add_edge("Switch 3 4", "Switch 2 4", length=6500, type="track")
    railway_network.add_edge("Delft Campus 3", "Switch 3 3", length=1500, type="track")
    railway_network.add_edge("Delft Campus 4", "Switch 3 4", length=1500, type="track")
    railway_network.add_edge("Switch 4 3", "Delft Campus 3", length=300, type="track")
    railway_network.add_edge("Switch 4 4", "Delft Campus 4", length=300, type="track")
    railway_network.add_edge("Delft 3", "Switch 4 3", length=1600, type="track")
    railway_network.add_edge("Delft 4", "Switch 4 4", length=1600, type="track")
    railway_network.add_edge("Switch 5 3", "Delft 3", length=2500, type="track")
    railway_network.add_edge("Switch 5 4", "Delft 4", length=2500, type="track")
    railway_network.add_edge("Rijswijk 3", "Switch 5 3", length=1800, type="track")
    railway_network.add_edge("Rijswijk 4", "Switch 5 4", length=1800, type="track")
    railway_network.add_edge("Moerwijk 3", "Rijswijk 3", length=1900, type="track")
    railway_network.add_edge("Moerwijk 4", "Rijswijk 4", length=1900, type="track")
    railway_network.add_edge("Switch 6 3", "Moerwijk 3", length=600, type="track")
    railway_network.add_edge("Switch 6 4", "Moerwijk 4", length=600, type="track")
    railway_network.add_edge("Den Haag HS 3", "Switch 6 3", length=1400, type="track")
    railway_network.add_edge("Den Haag HS 4", "Switch 6 4", length=1400, type="track")

    return railway_network

def visualize_2(network):
    pos = nx.get_node_attributes(network, 'pos')

    empty_label = ['vswitch', 'platform']
    labels = {node: node if network.nodes[node]['type'] not in empty_label else '' for node in network.nodes}

    # Define the figure size
    plt.figure(figsize=(6, 12))

    # Draw nodes
    node_size = [20 if network.nodes[node]['type'] == 'switch' else 200 if network.nodes[node]['type'] == 'station' else 1 for node in network.nodes]

    node_color = ['red' if network.nodes[node]['type'] == 'switch' else 'lightblue' for node in network.nodes]
    nx.draw_networkx_nodes(network, pos, node_size=node_size, node_color=node_color)

    #Create edgelist
    edgelist = []
    for edge in network.edges(data=True):
        edgelist.append((edge[0], edge[1]))

    #Draw edges
    nx.draw_networkx_edges(network, pos, edgelist=edgelist, edge_color='gray', arrows=None)

    # Draw labels
    nx.draw_networkx_labels(network, pos, labels=labels, font_size=10, font_color='black', horizontalalignment='right')

    plt.title("Railway Network")
    plt.ylim(0, 22600)
    plt.axis('auto')

    # Save the figure
    plt.savefig("railway_network.png")

    plt.show()

def check_type(network):
    default_node_type = 'unknown'
    G = network
    for node in G.nodes:
        node_type = G.nodes[node].get('type', 'unknown')
        print(f"Node {node}: Type = {node_type}")
    return



