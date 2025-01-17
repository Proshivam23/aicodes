from queue import Queue
a = []
def printn(node):
    a.append(node)
    for i in a:
        print(i, end = " ")

    print()
        
def bfs(adj, src):
    q = Queue()
    vis = set()
    q.put(src)
    vis.add(src)

    while not q.empty():
        node = q.get()
        
        open_list = list(q.queue)  # Get a list of elements in the queue
        closed_list = list(vis)

        # print("Current node:", printn(node))
        print("Open list:", open_list)
        print("Closed list:", closed_list)
        printn(node)

        # Iterate on adj Nodes
        for adjNode in adj[node]:
            if adjNode not in vis:
                q.put(adjNode)
                vis.add(adjNode)

def create_graph():
    graph = {}
    while True:
        try:
            edge_input = input("Enter an edge (Press Enter to stop)(e.g.'A B' for an edge from A to B): ")
            if not edge_input:
                break
            edge = edge_input.split()
            if len(edge) != 2:
                print("Invalid input. Please enter a valid edge.")
                continue
            u, v = edge
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)  # Assuming an undirected graph
        except ValueError:
            break
    return graph

# Create the graph
# adj = create_graph()
adj = {'A': ['B', 'C'], 'B': ['A', 'D'], 'D': ['B'], 'C': ['A', 'E', 'F'], 'E': ['C'], 'F': ['C']}
print("Graph:", adj)

# Take user input for the starting vertex
start_vertex = input("Enter the starting vertex for BFS traversal: ")

# Check if the starting vertex exists in the graph
if start_vertex not in adj:
    print("Starting vertex not found in the graph.")
else:
    print("BFS traversal starting from vertex", start_vertex, ":")
    bfs(adj, start_vertex)
