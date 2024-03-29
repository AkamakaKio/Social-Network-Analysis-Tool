import networkx as nx
import matplotlib.pyplot as plt

class SocialNetworkAnalyzer:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node1, node2):
        self.graph.add_edge(node1, node2)

    def visualize_network(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()

# Example usage:
analyzer = SocialNetworkAnalyzer()
analyzer.add_edge("Alice", "Bob")
analyzer.add_edge("Bob", "Charlie")
analyzer.visualize_network()
