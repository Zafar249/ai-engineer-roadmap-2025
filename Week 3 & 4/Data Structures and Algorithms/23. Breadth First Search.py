# Breadth First Search is a tree and graph searching algorithm
# Breadth First Search traverses a graph level by level utilizing a queue
# It is better if destination is closer to start on average
# Sibings are visited before children

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

    def breadth_first_search(self, src):
        # src = index of the node we would like to begin searching at
        queue = []
        visited = [False for i in range(5)] # Boolean Array containing all the nodes we have visited

        queue.append(src)
        visited[src] = True # We have visited the starting node

        while len(queue) != 0:
            src = queue.pop(0)
            print(self.alist[src][0].data, "= visited")

            for i in range(1, len(self.alist[src])):
                idx = -1
                for j in range(len(self.alist)):
                    if self.alist[j][0] == self.alist[src][i]:
                        idx = j
                        break

                if idx != -1 and not visited[idx]:
                    # If we have a node adjacent to the current node available 
                    # and we haven't visited it.
                    queue.append(idx)
                    visited[idx] = True

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
graph.breadth_first_search()