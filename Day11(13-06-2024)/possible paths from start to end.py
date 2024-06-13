"All possible paths from 5 to 2"
def dfs(graph, start, end, visited, path, all_paths):
    visited.add(start)
    path.append(start)
    if start == end:
        all_paths.append(path[:])  # Append a copy of the current path
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, end, visited, path, all_paths)
    path.pop()  # Backtrack by removing the last node from the path
    visited.remove(start)
def find_all_paths(graph, start, end):
    visited_nodes = set()
    all_paths = []
    dfs(graph, start, end, visited_nodes, [], all_paths)
    return all_paths
graph = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}
all_possible_paths = find_all_paths(graph, 5, 2)
print("All possible paths from node 5 to node 2:")
for path in all_possible_paths:
    print(path)

#or
print()
def fun(d,x,e):
    l.append(x)
    if(x==e):
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in l:
            fun(d,i,e)
    l.pop()
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
fun(d,5,2)

#or no of paths
print()
def fun(d,x,e,c):
    l.append(x)
    if(x==e):
        c=c+1
        l.pop()
        return c
    for i in d[x]:
        if i not in l:
            c=fun(d,i,e,c)
    l.pop()
    return c
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
print(fun(d,5,7,0))
