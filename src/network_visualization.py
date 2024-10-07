import networkx as nx
import matplotlib.pyplot as plt

def visualize_network(topology_data):
    G = nx.Graph()

    for node, neighbors in topology_data.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
    plt.show()

# Example Usage
if __name__ == "__main__":
    topology = {
        'Router1': ['Switch1', 'Router2'],
        'Router2': ['Router1', 'Switch2'],
        'Switch1': ['Router1', 'Host1'],
        'Switch2': ['Router2', 'Host2']
    }
    visualize_network(topology)
