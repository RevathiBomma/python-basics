def dynamic_dfs(graph, start_node, max_depth):
    """
    Performs a dynamic depth-first search on a graph.

    Args:
        graph: A dictionary representing the graph, where keys are nodes and values are lists of neighbors.
        start_node: The starting node for the search.
        max_depth: The maximum depth to explore.

    Returns:
        A list of visited nodes.
    """

    visited=set()
    stack=[(start_node,0)]
    while stack:
        node,depth=stack.pop()
        if node not in visited:
            visited.add(node)
            print(node,end=" ")
            if depth<max_depth:
                for neighbor in graph[node]:
                    stack.append((neighbor,depth+1))
    return visited
# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Dynamic DFS with maximum depth of 2
max_depth = 2
visited_nodes = dynamic_dfs(graph, 'A', max_depth)
print("\nVisited nodes:",visited_nodes)
