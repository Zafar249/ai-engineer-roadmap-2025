# Adjacency List is an array of linkedlists.
# Each linkedlist has a unique node at the head.
# All adjacent neighbours to that node are added to that node's linkedlist.
# Time Complexity: To check an edge O(v)
# Space Complexity: O(v+e) where v is the number of vertices(nodes) and e is the number of edges.

class Graph:
    def __init__(self):
        # alist is the adjacency list
        self.alist = []

    def add_node(self, node):
        currentlist = [node] # Create a new linked list with the node at the head
        self.alist.append(currentlist)

    def add_edge(self, src, dst):
        # src = source
        # dst = destination
        currentlist = self.alist[src]
        dstnode = self.alist[dst][0]
        currentlist.append(dstnode)


    def check_edge(self, src, dst):
        currentlist = self.alist[src]
        dstnode = self.alist[dst][0]
        for i in range(len(currentlist)):
            if currentlist[i] == dstnode:
                return True # Destination node found in currentlist
            
        return False # Destination node not found

    def print_graph(self):
        for i in range(len(self.alist)):
            for j in range(len(self.alist[i])):
                print(self.alist[i][j].data, " --> ", end="")
            print("")

class Node:
    def __init__(self, data):
        self.data = data

graph = Graph()
graph.add_node(Node('A')) # Each node has an index number. The first node has an index of 0
graph.add_node(Node('B')) # The second node has an index of 1
graph.add_node(Node('C'))
graph.add_node(Node('D'))
graph.add_node(Node('E'))

graph.add_edge(0, 1) # Creates an edge between A and B
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 0)
graph.add_edge(4, 2)

graph.print_graph()
