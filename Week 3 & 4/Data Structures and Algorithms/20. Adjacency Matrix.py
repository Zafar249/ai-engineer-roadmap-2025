# Adjacency matrix is a 2D array used to stores 1's and 0's to represent the edges between nodes.
# number of rows = number of unique nodes.
# number of columns = number of unique nodes
# Time Complexity: To check an edge O(1)
# Space Complexity : O(v^2) where v is the number of vertices(nodes)

class Graph:
    def __init__(self, size):
        # size is the number of nodes in the graph
        # self.matrix = [[0 for i in range(size)] for i in range(size)]
        self.nodes = []
        self.matrix = []
        for i in range(5):
            self.matrix.append([])
            for j in range(5):
                self.matrix[i].append(0)

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, src, dst):
        # src = source node
        # dst = destination node
        self.matrix[src][dst] = 1

    def check_edge(self, src, dst):
        # src = source node
        # dst = destination node
        if self.matrix[src][dst] == 1:
            return True
        else:
            return False

    def print_graph(self):
        print("   ", end = "")
        for i in range(len(self.nodes)):
            print(self.nodes[i].data," ", end="")
        print("")

        for i in range(len(self.matrix)):
            print(self.nodes[i].data," ", end="")
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], " ", end="")
            print("")


class Node:
    def __init__(self, data):
        self.data = data


graph = Graph(5)
graph.add_node(Node('A')) # First node has an index of 0
graph.add_node(Node('B')) # Second node has an index of 1
graph.add_node(Node('C'))
graph.add_node(Node('D'))
graph.add_node(Node('E'))

graph.add_edge(0, 1) # Creates an edge between A and B
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 0)
graph.add_edge(4, 2)

graph.print_graph()
print(graph.check_edge(2,0))