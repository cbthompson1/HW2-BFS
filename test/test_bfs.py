# write tests for bfs
import pytest
from search import graph

def test_bfs_no_graph():
    """No graph input should return KeyError."""
    g = graph.Graph('test/test_data/empty.adjlist')
    with pytest.raises(KeyError):
        g.bfs('Empty Node')

def test_bfs_unconnected_graph():
    """An unconnected graph should not be fully traversable."""
    g = graph.Graph('test/test_data/unconnected.adjlist')
    assert g.bfs('1') == ['1', '2', '3', '4']
    assert g.bfs('1', '6') == None

def test_bfs_no_path_graph():
    """A graph with no path from A to B should return None."""
    g = graph.Graph('test/test_data/no_path.adjlist')
    assert g.bfs('1', '12') == ['1', '2', '7', '9', '11', '12']
    assert g.bfs('12', '1') == None

def test_bfs_incorrect_start_node():
    """Incorrect input parameters should yield a KeyError."""
    g = graph.Graph('data/tiny_network.adjlist')
    with pytest.raises(KeyError):
        g.bfs('foobar')

def test_bfs_incorrect_end_node():
    """Incorrect input parameters should yield a KeyError."""
    g = graph.Graph('data/tiny_network.adjlist')
    with pytest.raises(KeyError):
        g.bfs('Tony Capra', 'foobar')

def test_bfs_traversal():
    """
    Run breadth first traversal with tiny_network.adjlist. Confirm general
    order.
    """
    g = graph.Graph('data/tiny_network.adjlist')
    res = g.bfs('Steven Altschuler')

    assert len(res) == 30 # Length matches.
    assert len(set(res)) == 30 # No repeats.
    assert res[1] == "32036252" # Only adj. node neighboring Steve's node.
    assert res[2] == "Lani Wu" # Only adj. node neighboring 320... node.

    # At this point divergence occurs between DFS and BFS, so confirm we only
    # hit the paper ids (?) adjacent to Lani.
    assert set(res[3:6]) == set(["30727954", "31806696", "32042149"])


def test_bfs():
    """
    Test BFS search and ensure:
    1. A simple two step works well (Ryan -> Tony)
    2. A farther reach also works (Ryan -> Hiten)
    3. Unconnected people don't return results (Hao -> Tony)
    """
    g = graph.Graph('data/citation_network.adjlist')

    ryan_to_tony = g.bfs('Ryan Corces', 'Tony Capra')
    assert ryan_to_tony == ['Ryan Corces', '33046896', 'Tony Capra']

    ryan_to_hiten = g.bfs('Ryan Corces', 'Hiten Madhani')
    assert ryan_to_hiten == [
        'Ryan Corces',
        '31178118',
        'Andrej Sali',
        '31955845',
        'Hiten Madhani',
    ]

    hao_to_tony = g.bfs("Hao Li", "Tony Capra")
    assert hao_to_tony == None