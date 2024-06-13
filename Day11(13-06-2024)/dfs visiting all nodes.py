def fun(d,x):
    l.append(x)
    for i in d[x]:
        if(i not in l):
            fun(d,i)
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
fun(d,5)
print(l)

#or
def dfs(graph, node, visited):
    visited.append(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def depth_first_search(graph):
    visited_nodes = []
    for start_node in graph:
        if start_node not in visited_nodes:
            dfs(graph, start_node, visited_nodes)
    return visited_nodes
d = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}
visited_nodes = depth_first_search(d)
print(visited_nodes)
