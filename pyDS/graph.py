from collections import defaultdict 

class Graph():
	"""An implementation of graph data structure."""
	
	def __init__(self):
		"""Initialize the graph."""
		
		self._edges = []
		self._graph = defaultdict(list) 

	def __len__(self):
		"""Return the size of the Graph."""
		
		return (len(self._edges))

	def __str__(self):
		"""Return the informal string representation of the Graph."""
		
		return str(self._items)

	def __repr__(self):
		"""Return the formal string representation of the Graph."""
		
		return "pyDS.graph.Graph({})".format(self._graph)

	def add_edge(self,u,v):
		"""Return the graph after adding the edge."""
		
		self._graph[u].append(v)
		return (self._graph) 

	def generate_edges(self):
		"""Returns all the edges in tuple inside a list."""
		
		edges = []
		for node in self._graph:
			for neighbour in self._graph[node]:
				edges.append((node, neighbour))

		return (edges) 

