from collections import deque

def Jug_BFS(jug1_capacity, jug2_capacity, size_req):
    queue = deque()
    visited = set()
    all_paths = []

    queue.append([(0, 0)])
    visited.add((0, 0))

    while queue:
        path = queue.pop()
        curr = path[-1]
        jug1, jug2 = curr

        if jug1 == size_req:
            all_paths.append(path)
            continue

        succ = [(jug1_capacity, jug2), (jug1, jug2_capacity), (0, jug2), (jug1, 0)]

        # Pour second Jug into First
        sp_l = jug1_capacity - jug1
        if sp_l >= jug2:
            succ.append((jug1 + jug2, 0))
        else:
            succ.append((jug1_capacity, jug2 - sp_l))

        # Pour into the second jug
        sp_r = jug2_capacity - jug2
        if sp_r >= jug1:
            succ.append((0, jug1 + jug2))
        else:
            succ.append((jug1 - sp_r, jug2_capacity))

        for s in succ:
            if s not in visited:
                new_path = list(path)
                new_path.append(s)
                queue.append(new_path)
                visited.add(s)

    return all_paths

# Take user input for jug capacities
jug1_capacity = int(input("Enter the capacity of the first jug: "))
jug2_capacity = int(input("Enter the capacity of the second jug: "))
size_req = int(input("Enter the desired amount of water in gallons: "))

# Run BFS
all_paths = Jug_BFS(jug1_capacity, jug2_capacity, size_req)

# Display all paths
for path in all_paths:
    print(path)
