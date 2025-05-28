class Graph:
    def __init__(self, edges):
        self.edges = edges # An array of routes
        self.graph_dict = {} # Create a dictionary to assign routes
        for start, end in edges: # For each item in edges
            if start in self.graph_dict: # If key alreadys exists in dict
                self.graph_dict[start].append(end) # Append the value to the key
            else: # If key doesn't exist in dict
                self.graph_dict[start] = [end] # Assign the value to the key
        print("Graph Dict:", self.graph_dict) # Print the graph

    def get_paths(self, start, end, path=[]):
        path = path + [start] # Convert start to a list and append to path

        if start == end:
            return [path]

        if start not in self.graph_dict: # If start doesn't exist in dict
            return []

        paths = []
        for node in self.graph_dict[start]: # For each value with the same(start) key
            if node not in path: 
                new_paths = self.get_paths(node, end, path) 
                # Recursively call the function with the next node as the start argument
                for p in new_paths:
                    paths.append(p) # Append the new_paths to the paths

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp: # If there is a path between start and end
                    if shortest_path is None or len(sp) < len(shortest_path):
                        # If path is unassigned or less than the current shortest path
                        shortest_path = sp

        return shortest_path

    # Problem: Given two nodes, determine if there’s a direct edge
    # (a flight/route with no intermediate stops) between them.

    def find_edge(self,start, end):
        for node in self.graph_dict[start]:
            if node == end:
                return True
        return False
    
    # Problem: Determine if the graph contains a cycle 
    # (a path where a node is reachable from itself).

    def cycle(self, start, path=[]):
        path.append(start)
        flag = False
        for node in self.graph_dict[start]:
            if node not in path:
                flag = self.cycle(node, path)
            else:
                flag = True
        
        return flag
    
    # Problem: Identify the node with the highest out-degree (most outgoing edges).
    def max_edges(self):
        edge = ""
        connection = 0
        for key, values in self.graph_dict.items():
            if len(values) > connection:
                edge = key
                connection = len(values)

        return edge



# if __name__ == '__main__':

#     routes = [
#         ("Mumbai","Pune"),
#         ("Mumbai", "Surat"),
#         ("Surat", "Bangaluru"),
#         ("Pune","Hyderabad"),
#         ("Pune","Mysuru"),
#         ("Hyderabad","Bangaluru"),
#         ("Hyderabad", "Chennai"),
#         ("Mysuru", "Bangaluru"),
#         ("Chennai", "Bangaluru")
#     ]

#     routes = [
#         ("Mumbai", "Paris"),
#         ("Mumbai", "Dubai"),
#         ("Paris", "Dubai"),
#         ("Paris", "New York"),
#         ("Dubai", "New York"),
#         ("New York", "Toronto"),
#     ]

#     route_graph = Graph(routes)

#     start = "Mumbai"
#     end = "New York"

#     print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
#     print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))

#     start = "Dubai"
#     end = "New York"

#     print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
#     print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))

    # print(route_graph.find_edge("Mumbai", "New York"))

routes = [("A", "B"), ("A", "C"), ("B", "C")]  
graph = Graph(routes)  
print(graph.max_edges())  # Output: "A" (2 edges)  
