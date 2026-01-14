graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'], 
    'C': ['A', 'B', 'D', 'E', 'G'], 
    'D': ['A', 'C'], 'E': ['C', 'F'], 
    'F': ['E'], 'G': ['C', 'H'], 
    'H': ['G'] 
}

v = None

# Pre-order depth first search
def dfs_pre_order(v, visited=None, order=None):
    if visited is None: 
        visited = set() 
    if order is None: 
        order = [] 
    if v not in visited: 
        visited.add(v) 
        order.append(v) 
        for neighbour in graph[v]: 
            dfs_pre_order(neighbour, visited, order) 
    return order

# Post-order depth first search
def dfs_post_order(v, visited=None, order=None): 
    if visited is None: 
        visited = set()
    if order is None: 
        order = [] 
    if v not in visited: 
        visited.add(v) 
        for neighbour in graph[v]: 
            dfs_post_order(neighbour, visited, order) 
        order.append(v) 
    return order

# Custom in-order depth first search
def dfs_in_order(v, visited=None, order=None): 
    if visited is None: 
        visited = set() 
    if order is None: 
        order = [] 
    if v not in visited: 
        visited.add(v) 
        neighbours = graph[v] 
        mid = len(neighbours) // 2 
        for neighbour in neighbours[:mid]: 
            dfs_in_order(neighbour, visited, order) 
        order.append(v) 
        for neighbour in neighbours[mid:]: 
            dfs_in_order(neighbour, visited, order) 
    return order

dfs_pre_order(v)
print(order)



