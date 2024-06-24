a = []
def printn(node):
    a.append(node)
    for i in a:
        print(i, end = " ")

    print()

    
def dfs(adj, src):
    stack = [src]
    vis = set()
    vis.add(src)
    
    while stack:
        open_list = stack.copy()
        closed_list = list(vis)

        node = stack.pop()
        print("Open list:", open_list)
        print("Closed list:", closed_list)
        printn(node)

        # Iterate on adjacent nodes in reverse order for consistent ordering
        for adjNode in reversed(adj[node]):
            if adjNode not in vis:
                stack.append(adjNode)
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
adj = create_graph()
print("Graph:", adj)

# Take user input for the starting vertex
start_vertex = input("Enter the starting vertex for DFS traversal: ")

# Check if the starting vertex exists in the graph
if start_vertex not in adj:
    print("Starting vertex not found in the graph.")
else:
    print("DFS traversal starting from vertex", start_vertex, ":")
    dfs(adj, start_vertex)
