from queue import Queue

def bfs(adj, src):
    q = Queue()
    vis = set()

    q.put(src)
    vis.add(src)

    
    while not q.empty():
        node = q.get()

        for adjNode in adj[node]:
            if adjNode not in vis:
                q.put(adjNode)
                vis.add(adjNode)


def dfs(adj, src):
    stack = [src]
    vis = set()

    vis.add(src)

    while stack:
        node = stack.pop()

        for adjNode in reversed(adj[node]):
            if adjNode not in vis:
                stack.append(adjNode)
                vis.add(adjNode)