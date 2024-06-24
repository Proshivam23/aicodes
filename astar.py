import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.heuristic = {}
    


graph = Graph()


path, total_cost = graph.astar(start, goal)
if path:
    print("->".join(path))
    print("Total cost: ", total_cost);
else:
    print("Path not found")    