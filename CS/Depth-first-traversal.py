# This doesn't work
graph = {
        "A":["B", "D"],
        "B":["A","G"],
        "C":["D","F"],
         "D":["A","C","F"],
         "E":["F"],
         "F":["C","E","G"],
         "G":["B", "F"]}

currentNode = ""
visitedNodes = ""
node = ""

def dfs(graph, currentNode, visitedNodes):
    append(visitedNodes, currentNode)
    for node in graph(currentNode):
        if node != visitedNodes:
            dfs(graph, node, visitedNodes)
    return visitedNodes

dfs(graph, currentNode, visitedNodes)

