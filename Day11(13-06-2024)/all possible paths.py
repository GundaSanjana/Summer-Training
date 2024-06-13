def dfs(graph, node, visited, path, all_paths):
    visited.add(node)
    path.append(node)
    if len(path) == len(graph):
        all_paths.append(path[:])  # Append a copy of the current path
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path, all_paths)
    path.pop()  # Backtrack by removing the last node from the path
    visited.remove(node)
def all_paths_dfs(graph):
    visited_nodes = set()
    all_paths = []
    for start_node in graph:
        dfs(graph, start_node, visited_nodes, [], all_paths)
    return all_paths
d = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}
all_possible_paths = all_paths_dfs(d)
print("All possible paths:")
for path in all_possible_paths:
    print(path)
