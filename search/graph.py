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
        Generates path from start to end nodes using a linked-list-esque
        backtracking.

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
        # Reversing a backtrack gives the correct-order path.
        return path[::-1]

    def _handle_bfs_input_validation(self, start, end=None):
        """Helper method to handle incorrect inputs to bfs method."""
        try:
            self.graph[start]
        except KeyError:
            raise KeyError(
                f'Start node "{start}" does not exist in the graph.'
            )
        if end:
            try:
                self.graph[end]
            except KeyError:
                raise KeyError(
                    f'End node "{end}" does not exist in the graph.'
                )

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
        self._handle_bfs_input_validation(start, end)
        if start == end:
            # Return an empty list if start == end - no work needed.
            return []
        if end:
            breadcrumbs = {start: ''}

        # 'queue' and 'visited' are used for determining the next BFS-approved
        # node to explore, and 'order' is tracking the order of traversal.
        queue = [start]
        order = []
        visited = set()

        while queue:
            # Evaluate next node.
            current_name = queue.pop(0)
            # Prevent computational loop with the set 'visited'.
            if current_name in visited:
                continue
            visited.add(current_name)
            # Add node to traversal list if we're listing all of them.
            if not end:
                order.append(current_name)
            # Go through the outbound edges of the node and add to the queue if
            # they are unvisited.
            current_node = self.graph[current_name]
            for node in current_node.keys():
                # If returning a path, populate a "breadcrumb" dictionary that
                # keeps track of what each node's predecessor is.
                if end and (node not in visited):
                    breadcrumbs[node] = current_name
                    if node == end:
                        # Determine the path when the end node is reached.
                        return self._return_path(breadcrumbs, start, end)
                # Cut down on unnecessary appends by checking if node is
                # already explored.
                if node not in visited:
                    queue.append(node)

        # If traversing the graph, return every visited node. If looking for a
        # path and none was found, return None as a signal it doesn't exist.
        if end:
            return None
        return order