# Depth First Search is a tree and graph searching algorithm
# In Depth First Search you pick a route and keep going
# If you reach a dead end, or a node you already visited
# You backtrack to a previous node with unvisited adjacent neighbours
# It traverses a graph branch by branch utilizing a stack



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

    def depth_first_search(self, src):
        # src = source node(i.e where we begin)
        visited = [False for i in range(5)] # boolean array that tells which nodes have been visited
        self.dfs_helper(src, visited)

    def dfs_helper(self, src, visited):
        if visited[src]: # If we have visited the node
            return 0
        else:
            visited[src] = True
            print(self.nodes[src].data, "= visited")

        for i in range(len(self.matrix[src])): # Iterate over a row of the matrix
            if self.matrix[src][i] == 1: # If the source node has a connection to an adjacent node
                self.dfs_helper(i, visited)
        return 0


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
print(graph.depth_first_search(4))