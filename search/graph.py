import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def _return_path(self, breadcrumbs, start, end):
        """
        Generates path from start to end nodes.

        Args:
            breadcrumbs (dict): list of nodes to their previous nodes from start.
            start (str): start node
            end (str): end node
        Returns:
            List of nodes describing path from start to end using bfs method.
        """
        path = [end]
        curr = end
        while curr != start:
            curr = breadcrumbs[curr]
            path.append(curr)
        return path[::-1]

    def bfs(self, start, end=None):
        """
        Performs a breadth first traversal / pathfinding on graph object.

        Args:
            start (string): Key of the node to start traversal / pathfinding.
            end (string): Key of the goal node.
        Returns:
            List of nodes representing either a traversal of the connected
            component of the graph or a path from the start to end node.
        """
        queue = [start]
        order = []
        explored = set()
        if end:
            breadcrumbs = {start: ''}

        while queue:
            current_name = queue.pop(0)
            if current_name in explored:
                continue
            explored.add(current_name)
            if not end:
                order.append(current_name)
            current_node = self.graph[current_name]
            for node in current_node.keys():
                if end and node not in explored:
                    breadcrumbs[node] = current_name
                    if node == end:
                        return self._return_path(breadcrumbs, start, end)
                queue.append(node)
        return order or None
